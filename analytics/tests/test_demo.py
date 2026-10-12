"""The DEMO generator: reproducible, clearly labelled, and kept away from the real data path."""
import csv
import tempfile
import unittest
from pathlib import Path

import _path  # noqa: F401
import demo_data
import metrics
import tracker
from testutil import close_all, make_db

TMP1 = TMP2 = None
DB1 = DB2 = None


def setUpModule():
    global TMP1, TMP2, DB1, DB2
    TMP1, TMP2 = tempfile.TemporaryDirectory(), tempfile.TemporaryDirectory()
    DB1, _ = demo_data.build_demo(Path(TMP1.name))
    DB2, _ = demo_data.build_demo(Path(TMP2.name))


def tearDownModule():
    close_all()
    TMP1.cleanup()
    TMP2.cleanup()


class Demo(unittest.TestCase):
    def test_output_is_deterministic(self):
        for p in sorted((Path(TMP1.name) / "csv").glob("*.csv")):
            self.assertEqual(p.read_bytes(), (Path(TMP2.name) / "csv" / p.name).read_bytes(), p.name)

    def test_database_is_flagged_demo_with_its_own_as_of_date(self):
        c = tracker.connect(DB1, read_only=True)
        try:
            self.assertTrue(tracker.is_demo(c))
            self.assertEqual(tracker.get_meta(c, "demo_as_of"), "2027-01-04")
            self.assertIn("DEMO", tracker.get_meta(c, "demo_note"))
        finally:
            c.close()

    def test_every_file_and_key_is_labelled_demo(self):
        files = list((Path(TMP1.name) / "csv").glob("*.csv"))
        self.assertTrue(files)
        for p in files:
            self.assertTrue(p.name.startswith("DEMO_"), p.name)
        for name, col in (("posts", "post_id"), ("costs", "ref"), ("revenue", "ref"), ("lead_signals", "ref"), ("effort", "ref"),
                          ("reviews", "ref"), ("standing", "ref"), ("experiments", "exp_id")):
            with open(Path(TMP1.name) / "csv" / f"DEMO_{name}.csv", encoding="utf-8", newline="") as fh:
                for row in csv.DictReader(fh):
                    self.assertTrue(row[col].startswith("DEMO-"), (name, row[col]))

    def test_a_real_database_refuses_every_demo_file(self):
        c = make_db()
        for p in (Path(TMP1.name) / "csv").glob("*.csv"):
            kind = p.stem.replace("DEMO_", "")
            with self.assertRaises(tracker.ImportErrorList, msg=p.name):
                tracker.import_csv(c, kind, p)
        self.assertEqual(c.execute("SELECT COUNT(*) FROM posts").fetchone()[0], 0)

    def test_refuses_to_write_inside_the_real_data_folder_and_leaves_it_alone(self):
        real_db_existed = tracker.REAL_DB.exists()
        before = sorted(p.name for p in tracker.REAL_DB.parent.glob("*")) if tracker.REAL_DB.parent.exists() else None
        with self.assertRaises(SystemExit):
            demo_data.build_demo(demo_data.REAL_DIR / "oops")
        self.assertEqual(tracker.REAL_DB.exists(), real_db_existed)
        after = sorted(p.name for p in tracker.REAL_DB.parent.glob("*")) if tracker.REAL_DB.parent.exists() else None
        self.assertEqual(before, after)
        self.assertFalse((demo_data.REAL_DIR / "oops").exists())

    def test_shipped_real_folder_holds_no_database_unless_the_operator_made_one(self):
        # The folder is meant to be empty (a .gitkeep) at hand-off. If the operator has run `init`, a database is theirs; skip.
        if tracker.REAL_DB.exists():
            self.skipTest("a real database exists in this checkout (the operator ran init)")
        self.assertEqual([p.name for p in tracker.REAL_DB.parent.glob("*") if p.name not in (".gitkeep", ".gitignore")], [])

    def test_scenario_exercises_the_tree(self):
        c = tracker.connect(DB1, read_only=True)
        try:
            snap = metrics.portfolio_snapshot(c)
        finally:
            c.close()
        got = {(p["slug"], a["platform"]): a["decision"]["status"] for p in snap["personas"] for a in p["accounts"]}
        self.assertEqual(got, {
            ("fangcun", "instagram"): "KEEP", ("fangcun", "youtube_shorts"): "FIX",
            ("buzhou", "youtube_shorts"): "FIX", ("buzhou", "threads"): "EXTEND",
            ("sehuan", "instagram"): "FIX", ("sehuan", "threads"): "PAUSE"})
        self.assertTrue(snap["is_demo"])
        self.assertEqual(snap["as_of"].isoformat(), "2027-01-04")

    def test_demo_has_sponsored_posts_kept_out_of_organic_medians(self):
        c = tracker.connect(DB1, read_only=True)
        try:
            a = metrics.account_assessment(c, "sehuan", "instagram", metrics.d2("2027-01-04"))
        finally:
            c.close()
        self.assertGreaterEqual(a["posts_sponsored"], 1)
        self.assertTrue(all(p["sponsorship_type"] == "none" for p in a["posts"]))

    def test_platforms_that_report_no_saves_have_blank_saves_not_zero(self):
        c = tracker.connect(DB1, read_only=True)
        try:
            n = c.execute("""SELECT COUNT(*) FROM v_post_latest WHERE platform IN ('threads','youtube_shorts') AND saves IS NOT NULL""").fetchone()[0]
            m = c.execute("""SELECT COUNT(*) FROM v_post_latest WHERE platform IN ('threads','youtube_shorts') AND reach IS NOT NULL""").fetchone()[0]
        finally:
            c.close()
        self.assertEqual((n, m), (0, 0))


if __name__ == "__main__":
    unittest.main()
