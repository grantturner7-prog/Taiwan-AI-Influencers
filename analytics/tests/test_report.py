"""weekly_report.py: what worked, what did not, one experiment, with the sample-size rule stated."""
import contextlib
import csv
import datetime as dt
import io
import re
import tempfile
import unittest
from pathlib import Path

import _path  # noqa: F401
import demo_data
import metrics
import tracker
import weekly_report
from testutil import REVIEW_DAY, add_effort, add_post, close_all, day, fill_window, make_db

TMP = None
DEMO_DB = None


def setUpModule():
    global TMP, DEMO_DB
    TMP = tempfile.TemporaryDirectory()
    DEMO_DB, _ = demo_data.build_demo(Path(TMP.name))


def tearDownModule():
    close_all()
    TMP.cleanup()


def report_for(conn, as_of, show_all=False):
    snap = metrics.portfolio_snapshot(conn, as_of)
    return weekly_report.build_report(conn, snap, show_all)


def demo_report(show_all=False):
    c = tracker.connect(DEMO_DB, read_only=True)
    try:
        return report_for(c, None, show_all)
    finally:
        c.close()


class DemoReport(unittest.TestCase):
    def setUp(self):
        self.text = demo_report()

    def test_demo_banner_first(self):
        self.assertTrue(self.text.startswith("=" * 20))
        self.assertIn("DEMO DATA", self.text.splitlines()[1])

    def test_all_sections_present_in_order(self):
        marks = ["1. WHERE EACH ACCOUNT STANDS", "2. WHAT WORKED", "3. WHAT DID NOT WORK", "4. ONE EXPERIMENT TO RUN NEXT", "5. SAMPLE-SIZE CAVEATS"]
        pos = [self.text.index(m) for m in marks]
        self.assertEqual(pos, sorted(pos))

    def test_exactly_one_new_experiment_is_proposed(self):
        self.assertEqual(len(re.findall(r"^  Experiment ", self.text, re.M)), 1)
        self.assertEqual(self.text.count("Paste-ready row"), 1)

    def test_states_the_minimum_sample_rule_and_sample_sizes(self):
        self.assertIn("8 organic posts per platform", self.text)
        self.assertIn("minimum-sample rule", self.text)
        self.assertGreater(len(re.findall(r"\bn=\d+", self.text)), 10)
        self.assertIn("not a significance test", self.text)
        self.assertIn("never compared on ER", self.text)

    def test_default_is_capped_and_all_shows_more(self):
        short = demo_report()
        full = demo_report(show_all=True)
        for title in ("2. WHAT WORKED", "3. WHAT DID NOT WORK"):
            def bullets(t):
                body = t.split(title)[1].split("\n\n")[0]
                return len(re.findall(r"^  - ", body, re.M))
            self.assertLessEqual(bullets(short), weekly_report.MAX_LINES)
        self.assertGreater(len(full), len(short))
        self.assertIn("lower-priority line(s) hidden", short)

    def test_no_lived_experience_or_cross_platform_er_claims(self):
        for phrase in ("I tried", "I used", "we tested it ourselves"):
            self.assertNotIn(phrase, self.text)

    def test_deterministic(self):
        self.assertEqual(self.text, demo_report())

    def test_running_experiment_blocks_another_on_that_persona(self):
        self.assertIn("Already running: DEMO-E002", self.text)
        m = re.search(r"Account: (\w+) ", self.text)
        self.assertNotEqual(m.group(1), "fangcun")

    def test_paused_account_is_not_compared_on_platforms(self):
        full = demo_report(show_all=True)
        self.assertIn("platform comparison skipped", full)
        self.assertNotIn("sehuan 色環 H2", full)

    def test_cross_platform_metric_decides_only_for_h2_and_h3(self):
        """portfolio.md 6.1 allows the shares+comments-per-1,000-views comparison only for H2 and H3."""
        for slug, plats, tag in (("buzhou", ("youtube_shorts", "threads"), "context only"), ("sehuan", ("instagram", "threads"), "H2")):
            c = make_db()
            for plat, shares in zip(plats, (40, 10)):
                add_post(c, f"{slug}-{plat}-anchor", slug, plat, 0, reach=None, views=1000, saves=None, shares=1, comments=1)
                for i in range(10):
                    add_post(c, f"{slug}-{plat}-{i}", slug, plat, 14 + i * 2, reach=None, views=1000, saves=None, shares=shares, comments=5)
            text = report_for(c, REVIEW_DAY + dt.timedelta(days=3), show_all=True)
            line = " ".join(l.strip() for l in text.splitlines() if "cross-platform metric" in l or "context only" in l)
            self.assertIn(tag, line, slug)
            if tag == "context only":
                self.assertNotIn("candidate to drop", text)
                self.assertIn("decides nothing", text)
            else:
                self.assertIn("candidate to drop or hold", text)

    def test_pasteable_row_imports_into_a_database(self):
        c = tracker.connect(DEMO_DB, read_only=True)
        try:
            snap = metrics.portfolio_snapshot(c)
            analysis = {}
            for p in snap["personas"]:
                for a in p["accounts"]:
                    analysis[(p["slug"], a["platform"])] = weekly_report.account_posts_for_analysis(c, a, p["first_post"], snap["as_of"])
            exp, _, _ = weekly_report.choose_experiment(snap, c, analysis)
        finally:
            c.close()
        text = weekly_report.csv_row(exp)
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "DEMO_experiments.csv"
            f.write_text(text, encoding="utf-8")
            conn = tracker.init_db(Path(d) / "x.db", demo=True)
            res = tracker.import_csv(conn, "experiments", f)
            self.assertEqual(res.errors, [])
            row = conn.execute("SELECT status, persona, platform FROM experiments").fetchone()
            conn.close()
        self.assertEqual(row["status"], "planned")
        self.assertEqual((row["persona"], row["platform"]), (exp["persona"], exp["platform"]))


class SampleTooSmall(unittest.TestCase):
    def test_empty_database_recommends_no_experiment(self):
        text = report_for(make_db(), REVIEW_DAY)
        self.assertIn("No experiment yet", text)
        self.assertIn("no account has 8 organic posts", text)
        self.assertNotRegex(text, r"^  Experiment E\d+", )
        self.assertNotIn("DEMO DATA", text)

    def test_seven_posts_is_not_enough(self):
        c = make_db()
        fill_window(c, n=7, er=0.004)
        text = report_for(c, REVIEW_DAY)
        self.assertIn("No experiment yet", text)
        self.assertIn("Extend to week 8".upper(), text)


class ChoosingTheExperiment(unittest.TestCase):
    def fix_db(self):
        c = make_db()
        fill_window(c, n=12, er=0.004)                      # Fix band
        return c

    def test_a_fix_account_gets_a_four_week_one_variable_experiment(self):
        text = report_for(self.fix_db(), REVIEW_DAY)
        self.assertRegex(text, r"Experiment E001: ")
        self.assertIn("One variable only", text)
        self.assertIn("(4 weeks)", text)
        self.assertIn("Fix experiment", text)
        self.assertIn("Decision rule (fixed before the data)", text)
        self.assertIn("at least 4 posts per arm", text)

    def test_clear_format_contrast_becomes_the_variable(self):
        c = make_db()
        fill_window(c, n=4, er=0.004)                                                  # carousels at 0.4%
        for i in range(4):
            add_post(c, f"R{i}", "fangcun", "instagram", 24 + 2 * i, fmt="reel", reach=1000, saves=5, shares=3, comments=2)     # reels at 1.0%
        for i in range(4):
            add_post(c, f"S{i}", "fangcun", "instagram", 32 + i, fmt="carousel", reach=1000, saves=1, shares=1, comments=2)    # more carousels at 0.4%
        text = report_for(c, REVIEW_DAY)
        self.assertIn("Format: reel vs carousel", text)

    def test_effort_driven_fix_proposes_a_redesign_not_a_content_test(self):
        c = make_db()
        fill_window(c, "buzhou", "youtube_shorts", n=12, er=0.01, reach=1000)
        for i in range(6):
            add_effort(c, f"n{i}", "buzhou", 10 + i, "operator", "n7_recording", 45.0, master_id=f"M{i}", post_id=f"Pbuzhou-youtube_shorts-{i:02d}")
        text = report_for(c, REVIEW_DAY)
        self.assertIn("Kind: redesign", text)
        self.assertIn("Cut effort", text)
        self.assertNotIn("Fix experiment (", text.split("4. ONE EXPERIMENT")[1].split("5. SAMPLE")[0].replace("Kind: redesign", ""))

    def test_no_experiment_on_a_persona_that_already_has_one_running(self):
        c = self.fix_db()
        c.execute("INSERT INTO experiments(exp_id,persona,platform,kind,name,start_date,status,planned_posts) VALUES ('E001','fangcun','instagram','hook','x',?, 'running', 12)", (day(42).isoformat(),))
        c.commit()
        text = report_for(c, REVIEW_DAY)
        self.assertIn("Already running: E001", text)
        self.assertIn("No new experiment", text)
        self.assertNotIn("Experiment E002", text)

    def test_next_id_follows_existing_ids(self):
        c = self.fix_db()
        c.execute("INSERT INTO experiments(exp_id,persona,platform,kind,name,start_date,status) VALUES ('E007','sehuan','instagram','hook','x',?, 'done')", (day(30).isoformat(),))
        c.commit()
        self.assertIn("Experiment E008", report_for(c, REVIEW_DAY))

    def test_open_gate_means_no_experiment_on_that_account(self):
        c = self.fix_db()
        c.execute("INSERT INTO standing_events(ref,event_date,persona,platform,gate,description) VALUES ('g',?,?,?,?,?)", (day(40).isoformat(), "fangcun", "instagram", "disclosure_failure", "t"))
        c.commit()
        text = report_for(c, REVIEW_DAY)
        self.assertNotRegex(text, r"Experiment E\d+")
        self.assertIn("OPEN GATE fangcun/instagram", text)

    def test_group_contrast_needs_four_posts_in_each_group_and_1_5x(self):
        posts = []
        for i, (fmt, er) in enumerate([("a", .01)] * 3 + [("b", .004)] * 3):
            posts.append({"er": er, "format": fmt, "pillar": None, "hook_type": None})
        self.assertEqual(weekly_report.group_contrasts(posts), [])          # 3 posts per group: not named
        posts += [{"er": .01, "format": "a", "pillar": None, "hook_type": None}, {"er": .004, "format": "b", "pillar": None, "hook_type": None}]
        c = weekly_report.group_contrasts(posts)
        self.assertEqual(len(c), 1)
        self.assertTrue(c[0]["clear"])
        self.assertAlmostEqual(c[0]["ratio"], 2.5)
        close = [{"er": .010, "format": "a", "pillar": None, "hook_type": None}] * 4 + [{"er": .008, "format": "b", "pillar": None, "hook_type": None}] * 4
        self.assertFalse(weekly_report.group_contrasts(close)[0]["clear"])


class Cli(unittest.TestCase):
    def test_main_demo_and_out_file_and_missing_real_db(self):
        buf = io.StringIO()
        with tempfile.TemporaryDirectory() as d, contextlib.redirect_stdout(buf):
            out = Path(d) / "r" / "report.txt"
            rc = weekly_report.main(["--demo", "--db", str(DEMO_DB), "--out", str(out)])
            self.assertEqual(rc, 0)
            self.assertIn("DEMO DATA", out.read_text(encoding="utf-8"))
            rc = weekly_report.main(["--db", str(Path(d) / "nope.db"), "--as-of", "2026-12-28"])
            self.assertEqual(rc, 0)
        self.assertIn("does not exist yet", buf.getvalue())


if __name__ == "__main__":
    unittest.main()
