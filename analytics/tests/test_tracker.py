"""Schema, CSV import and queue sync. All data is synthetic and lives in temporary folders."""
import csv
import hashlib
import json
import sqlite3
import tempfile
import unittest
from pathlib import Path

import _path  # noqa: F401
import tracker
from testutil import close_all, make_db


def tearDownModule():
    close_all()


def write_csv(dirpath, name, header, rows, encoding="utf-8"):
    p = Path(dirpath) / name
    with open(p, "w", encoding=encoding, newline="") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(rows)
    return p


class Schema(unittest.TestCase):
    def test_seed_has_ten_personas_and_pilot_accounts(self):
        c = make_db()
        self.assertEqual(c.execute("SELECT COUNT(*) FROM personas").fetchone()[0], 10)
        accts = {(r["persona"], r["platform"]) for r in c.execute("SELECT persona, platform FROM accounts")}
        self.assertIn(("fangcun", "instagram"), accts)
        self.assertIn(("buzhou", "threads"), accts)
        self.assertIn(("sehuan", "instagram"), accts)
        self.assertFalse(any(p == "jiehua" for p, _ in accts))      # wave 2+ have no accounts yet

    def test_real_database_starts_not_demo_and_empty(self):
        c = make_db()
        self.assertFalse(tracker.is_demo(c))
        self.assertEqual(c.execute("SELECT COUNT(*) FROM posts").fetchone()[0], 0)

    def test_init_db_is_idempotent_and_creates_folders(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "x" / "y" / "t.db"
            tracker.init_db(path).close()
            c = tracker.init_db(path)
            self.assertEqual(c.execute("SELECT COUNT(*) FROM personas").fetchone()[0], 10)
            c.close()

    def test_constraints_reject_bad_values(self):
        c = make_db()
        with self.assertRaises(sqlite3.IntegrityError):
            c.execute("INSERT INTO posts(post_id,persona,platform,published_date) VALUES ('a','fangcun','instagram','not-a-date')")
        with self.assertRaises(sqlite3.IntegrityError):
            c.execute("INSERT INTO posts(post_id,persona,platform,sponsorship_type) VALUES ('b','fangcun','instagram','sponsored')")
        with self.assertRaises(sqlite3.IntegrityError):
            c.execute("INSERT INTO posts(post_id,persona,platform) VALUES ('c','fangcun','facebook')")   # no such account
        with self.assertRaises(sqlite3.IntegrityError):
            c.execute("INSERT INTO account_daily(day,persona,platform,target_age_share) VALUES ('2026-11-16','fangcun','instagram',1.5)")

    def test_latest_snapshot_view(self):
        c = make_db()
        c.execute("INSERT INTO posts(post_id,persona,platform,status,published_date) VALUES ('a','fangcun','instagram','published','2026-11-16')")
        c.execute("INSERT INTO post_metrics(post_id,snapshot_date,reach,shares) VALUES ('a','2026-11-19',100,1)")
        c.execute("INSERT INTO post_metrics(post_id,snapshot_date,reach,shares) VALUES ('a','2026-11-23',300,4)")
        row = c.execute("SELECT reach, shares FROM v_post_latest WHERE post_id='a'").fetchone()
        self.assertEqual((row["reach"], row["shares"]), (300, 4))


class CsvImport(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.c = make_db()

    def posts_csv(self, rows, header=("post_id", "persona", "platform", "format", "published_date")):
        return write_csv(self.tmp.name, "posts.csv", header, rows)

    def test_import_posts_and_metrics(self):
        r = tracker.import_csv(self.c, "posts", self.posts_csv([("fangcun-2026-11-16-01", "fangcun", "instagram", "carousel", "2026-11-16")]))
        self.assertEqual((r.inserted, r.updated, r.errors), (1, 0, []))
        row = self.c.execute("SELECT status FROM posts").fetchone()
        self.assertEqual(row["status"], "published")          # published_date given, status blank
        m = write_csv(self.tmp.name, "m.csv", ["post_id", "snapshot_date", "reach", "saves", "shares", "comments"],
                      [("fangcun-2026-11-16-01", "2026-11-23", "1,204", "9", "0", "")])
        r = tracker.import_csv(self.c, "post_metrics", m)
        self.assertEqual(r.errors, [])
        row = self.c.execute("SELECT * FROM post_metrics").fetchone()
        self.assertEqual(row["reach"], 1204)                  # thousands separator accepted
        self.assertEqual(row["shares"], 0)                    # an explicit 0 stays 0
        self.assertIsNone(row["comments"])                    # a blank stays NULL (not reported), never 0
        self.assertIsNone(row["views"])

    def test_reimport_replaces_instead_of_duplicating(self):
        p = self.posts_csv([("a1", "fangcun", "instagram", "carousel", "2026-11-16")])
        tracker.import_csv(self.c, "posts", p)
        p2 = self.posts_csv([("a1", "fangcun", "instagram", "reel", "2026-11-16")])
        r = tracker.import_csv(self.c, "posts", p2)
        self.assertEqual((r.inserted, r.updated), (0, 1))
        self.assertEqual(self.c.execute("SELECT COUNT(*), MAX(format) FROM posts").fetchone()[:], (1, "reel"))

    def test_bad_rows_block_the_whole_file_with_line_numbers(self):
        p = self.posts_csv([("a1", "fangcun", "instagram", "carousel", "2026-11-16"),
                            ("a2", "fangcun", "instagram", "poster", "16 Nov 2026"),
                            ("a3", "nobody", "instagram", "reel", "2026-11-18")])
        r = tracker.import_csv(self.c, "posts", p)
        self.assertEqual(r.inserted, 0)
        self.assertEqual(self.c.execute("SELECT COUNT(*) FROM posts").fetchone()[0], 0)
        text = " ".join(r.errors)
        self.assertIn("line 3", text)
        self.assertIn("not one of", text)
        self.assertIn("YYYY-MM-DD", text)
        self.assertIn("line 4", text)
        self.assertIn("persona 'nobody'", text)

    def test_skip_bad_rows_imports_the_good_ones(self):
        p = self.posts_csv([("a1", "fangcun", "instagram", "carousel", "2026-11-16"), ("a2", "fangcun", "instagram", "poster", "2026-11-17")])
        r = tracker.import_csv(self.c, "posts", p, skip_bad_rows=True)
        self.assertEqual((r.inserted, len(r.errors)), (1, 1))

    def test_missing_required_column_is_a_clear_error(self):
        p = write_csv(self.tmp.name, "x.csv", ["post_id", "persona"], [("a", "fangcun")])
        with self.assertRaises(tracker.ImportErrorList) as cm:
            tracker.import_csv(self.c, "posts", p)
        self.assertIn("platform", str(cm.exception.errors[0]))

    def test_rename_maps_platform_headers_and_unknown_columns_warn(self):
        p = write_csv(self.tmp.name, "m.csv", ["Post", "Day", "Accounts reached", "Whatever"], [("a1", "2026-11-23", "50", "z")])
        tracker.import_csv(self.c, "posts", self.posts_csv([("a1", "fangcun", "instagram", "carousel", "2026-11-16")]))
        r = tracker.import_csv(self.c, "post_metrics", p, rename={"Post": "post_id", "Day": "snapshot_date", "Accounts reached": "reach"})
        self.assertEqual(r.errors, [])
        self.assertTrue(any("Whatever".lower() in w for w in r.warnings))
        self.assertEqual(self.c.execute("SELECT reach FROM post_metrics").fetchone()[0], 50)

    def test_unquoted_thousands_comma_is_an_error_not_a_silent_shift(self):
        p = Path(self.tmp.name) / "c.csv"
        p.write_text("cost_date,category,description,amount_twd\n2026-11-01,image_api,x,NT$1,200\n", encoding="utf-8")
        r = tracker.import_csv(self.c, "costs", p)
        self.assertEqual(r.inserted, 0)
        self.assertTrue(any("double quotes" in e for e in r.errors))
        self.assertEqual(self.c.execute("SELECT COUNT(*) FROM costs").fetchone()[0], 0)
        p.write_text('cost_date,category,description,amount_twd\n2026-11-01,image_api,x,"NT$1,200"\n', encoding="utf-8")
        r = tracker.import_csv(self.c, "costs", p)
        self.assertEqual(r.errors, [])
        self.assertEqual(self.c.execute("SELECT amount_twd FROM costs").fetchone()[0], 1200)

    def test_excel_bom_and_slash_dates(self):
        p = Path(self.tmp.name) / "b.csv"
        p.write_bytes("﻿post_id,persona,platform,published_date\nb1,fangcun,instagram,2026/11/16\n".encode("utf-8"))
        r = tracker.import_csv(self.c, "posts", p)
        self.assertEqual(r.errors, [])
        self.assertEqual(self.c.execute("SELECT published_date FROM posts").fetchone()[0], "2026-11-16")

    def test_share_accepts_percent_and_fraction_rejects_ambiguous(self):
        rows = [("2026-11-16", "fangcun", "instagram", "45%", "0.8"), ("2026-11-17", "fangcun", "instagram", "45", "")]
        p = write_csv(self.tmp.name, "d.csv", ["day", "persona", "platform", "target_age_share", "taiwan_share"], rows)
        r = tracker.import_csv(self.c, "account_daily", p)
        self.assertEqual(r.inserted, 0)
        self.assertIn("0.45 or 45%", " ".join(r.errors))
        rows = rows[:1]
        p = write_csv(self.tmp.name, "d2.csv", ["day", "persona", "platform", "target_age_share", "taiwan_share"], rows)
        self.assertEqual(tracker.import_csv(self.c, "account_daily", p).errors, [])
        self.assertAlmostEqual(self.c.execute("SELECT target_age_share FROM account_daily").fetchone()[0], 0.45)

    def test_auto_ref_makes_cost_reimport_idempotent(self):
        p = write_csv(self.tmp.name, "c.csv", ["cost_date", "category", "description", "amount_twd"],
                      [("2026-11-05", "image_api", "usage", "NT$1,450")])
        tracker.import_csv(self.c, "costs", p)
        r = tracker.import_csv(self.c, "costs", p)
        self.assertEqual((r.inserted, r.updated), (0, 1))
        row = self.c.execute("SELECT COUNT(*), SUM(amount_twd), MAX(cost_kind) FROM costs").fetchone()
        self.assertEqual(tuple(row), (1, 1450.0, "tool"))

    def test_negative_and_text_numbers_rejected(self):
        p = write_csv(self.tmp.name, "c.csv", ["cost_date", "category", "description", "amount_twd"], [("2026-11-05", "x", "y", "-5")])
        self.assertEqual(tracker.import_csv(self.c, "costs", p).inserted, 0)
        p = self.posts_csv([("a1", "fangcun", "instagram", "carousel", "2026-11-16")])
        tracker.import_csv(self.c, "posts", p)
        m = write_csv(self.tmp.name, "m.csv", ["post_id", "snapshot_date", "reach"], [("a1", "2026-11-23", "12.5")])
        self.assertIn("whole number", " ".join(tracker.import_csv(self.c, "post_metrics", m).errors))

    def test_published_status_needs_a_date_and_metrics_need_a_post(self):
        p = self.posts_csv([("a1", "fangcun", "instagram", "carousel", "")], header=("post_id", "persona", "platform", "format", "published_date"))
        self.assertEqual(tracker.import_csv(self.c, "posts", p).inserted, 1)      # blank date = draft
        self.assertEqual(self.c.execute("SELECT status FROM posts").fetchone()[0], "draft")
        m = write_csv(self.tmp.name, "m.csv", ["post_id", "snapshot_date", "reach"], [("ghost", "2026-11-23", "5")])
        self.assertIn("not in posts", " ".join(tracker.import_csv(self.c, "post_metrics", m).errors))

    def test_no_account_row_means_no_post(self):
        p = self.posts_csv([("a1", "jiehua", "threads", "text", "2026-11-16")])
        self.assertIn("no account row", " ".join(tracker.import_csv(self.c, "posts", p).errors))

    def test_standing_and_experiment_logic_checks(self):
        p = write_csv(self.tmp.name, "s.csv", ["event_date", "persona", "gate", "description", "cleared_on"],
                      [("2026-12-02", "fangcun", "rule6_contact", "x", "2026-12-01")])
        self.assertIn("before event_date", " ".join(tracker.import_csv(self.c, "standing", p).errors))
        p = write_csv(self.tmp.name, "e.csv", ["exp_id", "persona", "kind", "name", "start_date", "end_date", "status"],
                      [("E001", "fangcun", "hook", "n", "2026-12-10", "2026-12-01", "done")])
        self.assertIn("end_date is before", " ".join(tracker.import_csv(self.c, "experiments", p).errors))

    def test_every_documented_import_kind_has_a_working_empty_template(self):
        for kind in tracker.IMPORT_ORDER:
            cols = [c.name for c in tracker.SPECS[kind].cols]
            p = write_csv(self.tmp.name, f"{kind}.csv", cols, [])
            r = tracker.import_csv(self.c, kind, p)
            self.assertEqual((r.inserted, r.errors), (0, []), kind)


class DemoGuard(unittest.TestCase):
    def test_real_database_refuses_demo_ids_and_demo_files(self):
        c = make_db()
        with tempfile.TemporaryDirectory() as d:
            p = write_csv(d, "posts.csv", ["post_id", "persona", "platform", "published_date"],
                          [("DEMO-fangcun-2026-11-16-01", "fangcun", "instagram", "2026-11-16")])
            r = tracker.import_csv(c, "posts", p)
            self.assertEqual(r.inserted, 0)
            self.assertIn("DEMO data", " ".join(r.errors))
            p2 = write_csv(d, "DEMO_account_daily.csv", ["day", "persona", "platform", "followers"], [("2026-11-16", "fangcun", "instagram", "3")])
            with self.assertRaises(tracker.ImportErrorList):
                tracker.import_csv(c, "account_daily", p2)
            self.assertEqual(c.execute("SELECT COUNT(*) FROM account_daily").fetchone()[0], 0)

    def test_demo_database_accepts_demo_ids(self):
        with tempfile.TemporaryDirectory() as d:
            c = tracker.init_db(Path(d) / "demo.db", demo=True)
            p = write_csv(d, "DEMO_posts.csv", ["post_id", "persona", "platform", "published_date"],
                          [("DEMO-a", "fangcun", "instagram", "2026-11-16")])
            self.assertEqual(tracker.import_csv(c, "posts", p).errors, [])
            c.close()


class QueueSync(unittest.TestCase):
    def make_queue(self, root):
        for pid, persona, platform, wife in (("fangcun-2026-11-16-01", "fangcun", "instagram", "approved"),
                                              ("fangcun-2026-11-17-01", "fangcun", "youtube_shorts", "changes"),
                                              ("buzhou-2026-11-19-01", "buzhou", "youtube_shorts", "pending"),
                                              ("jiehua-2027-01-18-01", "jiehua", "threads", "pending")):
            d = Path(root) / persona / pid.split("-", 1)[1].rsplit("-", 1)[0]
            d.mkdir(parents=True, exist_ok=True)
            (d / "post.json").write_text(json.dumps({
                "id": pid, "persona": persona, "platform": platform, "format": "carousel", "scheduled_date": pid.split("-", 1)[1][:10],
                "pillar": "A", "sponsorship_type": "none", "ai_label_flag": True,
                "review": {"wife_language": wife, "operator_facts": "pending", "approved": False, "notes": ""}}, ensure_ascii=False), encoding="utf-8")

    def digest(self, root):
        h = hashlib.sha256()
        for p in sorted(Path(root).rglob("*")):
            if p.is_file():
                h.update(p.read_bytes())
        return h.hexdigest()

    def test_sync_registers_drafts_and_review_state_without_touching_the_queue(self):
        with tempfile.TemporaryDirectory() as d:
            self.make_queue(d)
            before = self.digest(d)
            c = make_db()
            r = tracker.import_queue(c, d)
            self.assertEqual(self.digest(d), before, "the queue must be read-only")
            self.assertEqual(r.drafts_seen, 4)
            self.assertEqual(r.posts_added, 3)                        # jiehua has no account yet: skipped, not an error
            self.assertEqual(len(r.skipped), 1)
            self.assertEqual(r.reviews_added, 2)                      # approved and changes recorded; pending is not a verdict
            self.assertEqual(c.execute("SELECT status FROM posts WHERE post_id='fangcun-2026-11-16-01'").fetchone()[0], "draft")
            v = {row["post_id"]: row["first_pass_verdict"] for row in c.execute("SELECT * FROM review_events")}
            self.assertEqual(v, {"fangcun-2026-11-16-01": "approved", "fangcun-2026-11-17-01": "changes"})
            r2 = tracker.import_queue(c, d)                           # idempotent
            self.assertEqual((r2.posts_added, r2.reviews_added), (0, 0))

    def test_sync_never_downgrades_a_published_post(self):
        with tempfile.TemporaryDirectory() as d:
            self.make_queue(d)
            c = make_db()
            tracker.import_queue(c, d)
            c.execute("UPDATE posts SET status='published', published_date='2026-11-16' WHERE post_id='fangcun-2026-11-16-01'")
            tracker.import_queue(c, d)
            self.assertEqual(c.execute("SELECT status FROM posts WHERE post_id='fangcun-2026-11-16-01'").fetchone()[0], "published")

    def test_sync_reads_the_real_queue_if_present(self):
        if not tracker.QUEUE_DIR.exists():
            self.skipTest("no review queue in this checkout")
        before = self.digest(tracker.QUEUE_DIR)
        c = make_db()
        tracker.import_queue(c)
        self.assertEqual(self.digest(tracker.QUEUE_DIR), before)

    def test_missing_queue_folder_is_reported_not_raised(self):
        r = tracker.import_queue(make_db(), "/nonexistent/queue")
        self.assertTrue(r.skipped)


class Docs(unittest.TestCase):
    def test_columns_markdown_covers_every_column(self):
        md = tracker.columns_markdown()
        for kind, spec in tracker.SPECS.items():
            for col in spec.cols:
                self.assertIn(f"`{col.name}`", md)

    def test_shipped_templates_match_the_specs(self):
        for kind, spec in tracker.SPECS.items():
            p = tracker.TEMPLATES_DIR / f"{kind}.csv"
            self.assertTrue(p.exists(), f"missing template {p.name}: run python3 analytics/tracker.py templates")
            self.assertEqual(p.read_text(encoding="utf-8").strip().split(","), [c.name for c in spec.cols], kind)

    def test_readme_names_every_import_kind_and_column(self):
        readme = (tracker.HERE / "README.md").read_text(encoding="utf-8")
        for kind, spec in tracker.SPECS.items():
            self.assertIn(f"`{kind}`", readme)
            for col in spec.cols:
                self.assertIn(f"`{col.name}`", readme, f"README does not document {kind}.{col.name}")


if __name__ == "__main__":
    unittest.main()
