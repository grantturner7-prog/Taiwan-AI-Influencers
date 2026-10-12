"""Definitions in portfolio.md 6.1 as computed by metrics.py, on small synthetic databases."""
import datetime as dt
import unittest

import _path  # noqa: F401
import metrics
import thresholds as T
from testutil import (FIRST, REVIEW_DAY, add_account_days, add_effort, add_post, add_review, close_all, day, fill_window, make_db)


def tearDownModule():
    close_all()


def acct(conn, persona="fangcun", platform="instagram", as_of=REVIEW_DAY):
    return metrics.account_assessment(conn, persona, platform, as_of)


class ErDefinition(unittest.TestCase):
    def test_er_uses_saves_shares_comments_over_reach(self):
        r = metrics.post_er({"reach": 1000, "views": 5000, "saves": 6, "shares": 3, "comments": 1, "likes": 900, "link_clicks": 40})
        self.assertAlmostEqual(r["er"], 0.010)
        self.assertEqual(r["denom_kind"], "reach")
        self.assertEqual(r["terms"], ["saves", "shares", "comments"])      # likes and link clicks are not in ER

    def test_views_is_the_denominator_only_when_reach_is_blank_and_is_labelled(self):
        r = metrics.post_er({"reach": None, "views": 2000, "saves": None, "shares": 4, "comments": 6})
        self.assertAlmostEqual(r["er"], 0.005)
        self.assertEqual(r["denom_kind"], "views")
        self.assertEqual(r["terms"], ["shares", "comments"])               # unreported saves are not counted as zero terms

    def test_uncomputable_posts_return_none(self):
        self.assertIsNone(metrics.post_er({"reach": None, "views": None, "shares": 1, "comments": 1}))
        self.assertIsNone(metrics.post_er({"reach": 100, "views": None, "saves": 3, "shares": None, "comments": None}))
        self.assertIsNone(metrics.post_er({"reach": 0, "views": 0, "shares": 1, "comments": 1}))

    def test_zero_interactions_is_a_real_zero(self):
        self.assertEqual(metrics.post_er({"reach": 500, "shares": 0, "comments": 0, "saves": 0})["er"], 0.0)


class Weeks(unittest.TestCase):
    def test_week_boundaries(self):
        self.assertEqual(metrics.week_of(FIRST, day(0)), 1)
        self.assertEqual(metrics.week_of(FIRST, day(6)), 1)
        self.assertEqual(metrics.week_of(FIRST, day(7)), 2)
        self.assertEqual(metrics.week_of(FIRST, day(41)), 6)
        self.assertEqual(metrics.week_of(FIRST, day(42)), 7)
        self.assertEqual(metrics.week_start(FIRST, 3), day(14))
        self.assertEqual(metrics.week_end(FIRST, 6), day(41))
        self.assertEqual(REVIEW_DAY, dt.date(2026, 12, 28))               # the portfolio's 6-week review date


class Trend(unittest.TestCase):
    def test_classification(self):
        c = metrics.classify_trend
        self.assertEqual(c([100, 120, 150]), "rising")
        self.assertEqual(c([100, 130, 160, 200]), "rising")
        self.assertEqual(c([100, 102, 99]), "flat")
        self.assertEqual(c([100, 90, 80]), "falling2")
        self.assertEqual(c([100, 90, 80, 70]), "falling3")
        self.assertEqual(c([150, 100, 90, 80]), "falling3")
        self.assertEqual(c([100, 150, 90, 80]), "falling2")
        self.assertEqual(c([100, 200]), "unknown")
        self.assertEqual(c([None, 100, 100]), "unknown")
        self.assertEqual(c([0, 0, 5]), "rising")

    def test_small_dips_inside_the_band_are_flat(self):
        self.assertEqual(metrics.classify_trend([100, 96, 93]), "flat")


class Window(unittest.TestCase):
    def setUp(self):
        self.c = make_db()

    def test_window_is_weeks_3_to_6_and_organic_only(self):
        fill_window(self.c, n=12, er=0.01, start=14, step=2)                      # days 14..36
        add_post(self.c, "early1", "fangcun", "instagram", 0, shares=300, comments=300, saves=300)     # week 1: warm-up, ignored
        add_post(self.c, "early2", "fangcun", "instagram", 10, shares=300, comments=300, saves=300)    # week 2: ignored
        add_post(self.c, "late", "fangcun", "instagram", 42, shares=300, comments=300, saves=300)      # week 7: ignored
        add_post(self.c, "spons", "fangcun", "instagram", 20, sponsorship="gifted", shares=300, comments=300, saves=300)
        a = acct(self.c)
        self.assertEqual(a["state"], "scored")
        self.assertEqual(a["summary"]["n_scored"], 12)
        self.assertAlmostEqual(a["summary"]["er"], 0.01, places=6)
        self.assertEqual(a["posts_sponsored"], 1)
        self.assertEqual(a["window"], (day(14), day(41)))

    def test_median_not_mean(self):
        fill_window(self.c, n=11, er=0.01)
        add_post(self.c, "viral", "fangcun", "instagram", 38, reach=1000, shares=200, comments=100, saves=0)     # ER 30%
        a = acct(self.c)
        self.assertAlmostEqual(a["summary"]["er"], 0.01, places=6)
        self.assertGreater(a["summary"]["er_max"], 0.29)

    def test_minimum_sample_is_exactly_eight(self):
        fill_window(self.c, n=7, er=0.01)
        a = acct(self.c)
        self.assertEqual(a["decision"]["status"], "EXTEND")                      # day 42, week 8 not over
        self.assertEqual(a["facts"]["n_scored"], 7)
        a = acct(self.c, as_of=day(56))
        self.assertEqual(a["decision"]["status"], "HOLD")                        # still 7 after week 8
        fill_window(self.c, n=1, er=0.01, start=36, prefix="Z")                  # an 8th post, still in week 6
        self.assertEqual(acct(self.c)["decision"]["status"], "KEEP")

    def test_extension_counts_weeks_7_and_8(self):
        fill_window(self.c, n=7, er=0.01)
        add_post(self.c, "w7", "fangcun", "instagram", 44, reach=1000, saves=3, shares=4, comments=3)
        a = acct(self.c, as_of=day(56))
        self.assertEqual(a["state"], "scored")
        self.assertIn("extended", a["window_label"])
        self.assertEqual(a["summary"]["n_scored"], 8)

    def test_in_progress_and_provisional(self):
        fill_window(self.c, n=5, er=0.01, start=14, step=1)                      # days 14..18
        a = acct(self.c, as_of=day(30))
        self.assertEqual(a["decision"]["status"], "IN_PROGRESS")
        fill_window(self.c, n=4, er=0.01, start=19, step=1, prefix="Y")
        a = acct(self.c, as_of=day(30))
        self.assertEqual(a["state"], "scored")
        self.assertTrue(a["provisional"])
        self.assertTrue(a["decision"]["provisional"])

    def test_posts_without_metrics_are_not_in_the_median_and_are_counted(self):
        fill_window(self.c, n=9, er=0.01)
        add_post(self.c, "nometrics", "fangcun", "instagram", 39, reach=None, views=None)
        a = acct(self.c)
        self.assertEqual(a["summary"]["n_scored"], 9)
        self.assertEqual(a["summary"]["n_missing_metrics"], 1)

    def test_latest_snapshot_wins(self):
        fill_window(self.c, n=8, er=0.01)
        self.c.execute("INSERT INTO post_metrics(post_id,snapshot_date,reach,shares,comments,saves) VALUES (?,?,?,?,?,?)",
                       ("Pfangcun-instagram-00", day(30).isoformat(), 1000, 100, 0, 0))
        self.c.commit()
        posts = {p["post_id"]: p for p in metrics.load_posts(self.c, "fangcun", "instagram")}
        self.assertAlmostEqual(posts["Pfangcun-instagram-00"]["er"], 0.10)

    def test_not_started_before_any_post_and_when_as_of_precedes_the_first_post(self):
        a = acct(self.c)
        self.assertEqual(a["decision"]["status"], "NOT_STARTED")
        fill_window(self.c, n=8, er=0.01)
        self.assertEqual(acct(self.c, as_of=day(-3))["decision"]["status"], "NOT_STARTED")


class SavesAndDenominators(unittest.TestCase):
    def test_unreported_saves_are_not_zero(self):
        c = make_db()
        fill_window(c, "buzhou", "threads", n=10, er=0.01, reach=None, saves_on=False)       # no reach: fill_window passes reach=None
        for i in range(10):
            pass
        a = acct(c, "buzhou", "threads")
        self.assertIsNone(a["facts"]["sv_share"])                                  # platform reports no saves -> row not scored

    def test_views_denominator_is_labelled_on_the_summary(self):
        c = make_db()
        for i in range(10):
            add_post(c, f"v{i}", "buzhou", "threads", 14 + 2 * i, reach=None, views=2000, saves=None, shares=10, comments=10)
        a = acct(c, "buzhou", "threads")
        self.assertEqual(a["summary"]["denominators"], ["views"])
        self.assertAlmostEqual(a["summary"]["er"], 0.01)
        self.assertAlmostEqual(a["summary"]["common_per_1000_views"], 10.0)

    def test_saves_share_when_reported_including_explicit_zero(self):
        c = make_db()
        for i in range(10):
            add_post(c, f"s{i}", "fangcun", "instagram", 14 + 2 * i, reach=1000, saves=6, shares=2, comments=2)
        a = acct(c)
        self.assertAlmostEqual(a["facts"]["sv_share"], 0.8)
        c2 = make_db()
        for i in range(10):
            add_post(c2, f"s{i}", "fangcun", "instagram", 14 + 2 * i, reach=1000, saves=0, shares=2, comments=2)
        self.assertAlmostEqual(acct(c2)["facts"]["sv_share"], 0.5)


class PersonaLevel(unittest.TestCase):
    def setUp(self):
        self.c = make_db()
        fill_window(self.c, n=12, er=0.01)

    def test_rejection_rate_counts_changes_and_rejected_in_weeks_4_to_6(self):
        for i in range(10):
            add_review(self.c, f"r{i}", f"x{i}", "fangcun", 22 + i, "approved" if i < 7 else ("changes" if i < 9 else "rejected"), None if i < 7 else "language")
        add_review(self.c, "early", "x", "fangcun", 3, "rejected", "fact")                  # week 1: outside weeks 4 to 6
        a = acct(self.c)
        self.assertEqual(a["rejection"]["n"], 10)
        self.assertAlmostEqual(a["rejection"]["value"], 0.3)
        self.assertEqual(a["rejection"]["reasons"], {"language": 3})
        self.assertTrue(a["rejection"]["scored"])

    def test_too_few_reviews_are_shown_but_not_scored(self):
        for i in range(3):
            add_review(self.c, f"r{i}", f"x{i}", "fangcun", 22 + i, "rejected", "fact")
        a = acct(self.c)
        self.assertEqual(a["rejection"]["value"], 1.0)
        self.assertFalse(a["rejection"]["scored"])
        self.assertEqual(a["decision"]["levels"]["rejection_rate"], "unknown")
        self.assertEqual(a["decision"]["status"], "KEEP")                          # not scored, so it cannot block Keep

    def test_effort_per_approval_and_per_master_sums(self):
        for i in range(6):
            pid = f"Pfangcun-instagram-{i:02d}"
            add_effort(self.c, f"o{i}", "fangcun", 10 + i, "operator", "approval", 6.0, post_id=pid)
            add_effort(self.c, f"w{i}a", "fangcun", 10 + i, "wife", "master_review", 7.0, post_id=pid, master_id=f"M{i}")
            add_effort(self.c, f"w{i}b", "fangcun", 10 + i, "wife", "master_review", 3.0, post_id=pid, master_id=f"M{i}")   # 2nd platform variant
        a = acct(self.c)
        self.assertAlmostEqual(a["effort"]["operator_min_per_approval"]["value"], 6.0)
        self.assertAlmostEqual(a["effort"]["wife_min_per_master"]["value"], 10.0)         # 7 + 3 per master
        self.assertEqual(a["effort"]["wife_min_per_master"]["n"], 6)
        self.assertNotIn("n7_min_per_master", a["effort"])                                 # N7 applies to buzhou only

    def test_effort_with_fewer_than_five_units_is_not_scored(self):
        for i in range(4):
            add_effort(self.c, f"o{i}", "fangcun", 10, "operator", "approval", 30.0, post_id=f"Pfangcun-instagram-{i:02d}")
        e = acct(self.c)["effort"]["operator_min_per_approval"]
        self.assertFalse(e["scored"])
        self.assertEqual(acct(self.c)["decision"]["status"], "KEEP")

    def test_link_clicks_prefer_the_link_page_and_count_weeks(self):
        for w, n in enumerate([0, 3, 0, 4, 1, 0]):
            self.c.execute("INSERT INTO account_daily(day,persona,platform,link_clicks) VALUES (?,?,?,?)", (day(7 * w + 2).isoformat(), "fangcun", "linkpage", n))
        self.c.execute("UPDATE account_daily SET link_clicks=999 WHERE day=? AND persona='fangcun' AND platform='instagram'", (day(2).isoformat(),))
        self.c.commit()
        lk = acct(self.c)["links"]
        self.assertEqual(lk["source"], "linkpage")
        self.assertEqual(lk["weeks_with_clicks"], 3)
        self.assertEqual(lk["total"], 8)                                                    # the platform's 999 is not double counted
        self.assertAlmostEqual(lk["weekly"][1]["clicks"], 3)

    def test_lead_signals_exclude_outreach(self):
        self.c.executemany("INSERT INTO lead_signals(ref,signal_date,persona,kind) VALUES (?,?,?,?)",
                           [("a", "2026-12-01", "fangcun", "outreach_sent"), ("b", "2026-12-02", "fangcun", "written_enquiry")])
        l = acct(self.c)["leads"]
        self.assertEqual((l["signals"], l["outreach"]), (1, 1))


class Standing(unittest.TestCase):
    def setUp(self):
        self.c = make_db()
        fill_window(self.c, n=12, er=0.01)

    def event(self, ref, d, gate, platform=None, cleared=None, persona="fangcun"):
        self.c.execute("INSERT INTO standing_events(ref,event_date,persona,platform,gate,description,cleared_on) VALUES (?,?,?,?,?,?,?)",
                       (ref, day(d).isoformat(), persona, platform, gate, "test", day(cleared).isoformat() if cleared is not None else None))
        self.c.commit()

    def test_open_event_pauses_that_account_only(self):
        self.event("e1", 40, "disclosure_failure", platform="instagram")
        self.assertEqual(acct(self.c)["decision"]["status"], "PAUSE")
        self.assertTrue(any("OVERDUE" in g for g in acct(self.c)["decision"]["reasons"]))          # open 2 days against a 24 hour rule
        self.assertNotEqual(acct(self.c, platform="youtube_shorts")["decision"]["status"], "PAUSE")

    def test_persona_wide_event_pauses_every_account(self):
        self.event("e1", 40, "rule6_contact")
        self.assertEqual(acct(self.c, platform="youtube_shorts")["decision"]["status"], "PAUSE")

    def test_cleared_events_do_not_pause_but_cleared_after_as_of_still_does(self):
        self.event("e1", 38, "garbled_or_wrong", platform="instagram", cleared=39)
        self.assertEqual(acct(self.c)["decision"]["status"], "KEEP")
        self.event("e2", 40, "garbled_or_wrong", platform="instagram", cleared=50)
        self.assertEqual(acct(self.c)["decision"]["status"], "PAUSE")                                # as of day 42 it was still open
        self.assertEqual(acct(self.c, as_of=day(60))["decision"]["status"], "KEEP")

    def test_second_rule6_event_within_8_weeks_retires(self):
        self.event("e1", 20, "rule6_contact", cleared=21)
        self.event("e2", 60, "rule6_contact", cleared=61)                                            # 40 days later
        self.assertEqual(acct(self.c, as_of=day(70))["decision"]["status"], "RETIRE")
        c2 = make_db()
        fill_window(c2, n=12, er=0.01)
        c2.execute("INSERT INTO standing_events(ref,event_date,persona,gate,description,cleared_on) VALUES ('a',?,?,?,?,?)", (day(0).isoformat(), "fangcun", "rule6_contact", "t", day(1).isoformat()))
        c2.execute("INSERT INTO standing_events(ref,event_date,persona,gate,description,cleared_on) VALUES ('b',?,?,?,?,?)", (day(70).isoformat(), "fangcun", "rule6_contact", "t", day(71).isoformat()))
        c2.commit()
        self.assertEqual(acct(c2, as_of=day(80))["decision"]["status"], "KEEP")                      # 70 days apart: not a repeat

    def test_strike_open_over_14_days_retires(self):
        self.event("e1", 20, "strike_restriction", platform="instagram")
        self.assertEqual(acct(self.c, as_of=day(30))["decision"]["status"], "PAUSE")
        self.assertEqual(acct(self.c, as_of=day(40))["decision"]["status"], "RETIRE")

    def test_event_in_window_blocks_scale_but_not_keep(self):
        self.event("e1", 20, "garbled_or_wrong", platform="instagram", cleared=21)
        a = acct(self.c)
        self.assertEqual(a["facts"]["events_in_window"], 1)
        self.assertEqual(a["decision"]["status"], "KEEP")

    def test_real_person_comment_alert_from_daily_counts(self):
        for j in range(5):
            self.c.execute("UPDATE account_daily SET real_person_comments=1 WHERE day=? AND persona='fangcun' AND platform='instagram'", (day(35 + j).isoformat(),))
        self.c.commit()
        alerts = metrics.persona_alerts(self.c, "fangcun", FIRST, day(42))
        self.assertTrue(any("real person" in a for a in alerts))

    def test_near_miss_alert_needs_10_reviews_and_3_hits(self):
        for i in range(12):
            add_review(self.c, f"r{i}", f"x{i}", "fangcun", 20 + i, "changes" if i < 3 else "approved", "safety" if i < 3 else None, near_miss=1 if i < 3 else 0)
        self.assertTrue(any("near miss" in a for a in metrics.persona_alerts(self.c, "fangcun", FIRST, day(42))))


class FollowersAndTrend(unittest.TestCase):
    def test_follower_stats(self):
        s = metrics.follower_stats({1: 50, 2: 80, 3: 120, 4: 100, 5: 130, 6: 140}, 6)
        self.assertEqual(s["growth_weeks"], 4)
        self.assertEqual(s["big_drop"], (4, 120, 100) if 100 < 120 * 0.9 else None)
        s = metrics.follower_stats({1: 50, 2: 30}, 6)                       # a 40% drop on a base under 100 is ignored (noise)
        self.assertIsNone(s["big_drop"])
        s = metrics.follower_stats({1: 200, 2: 150}, 6)
        self.assertEqual(s["big_drop"], (2, 200, 150))

    def test_reach_trend_flows_into_the_account(self):
        c = make_db()
        fill_window(c, n=12, er=0.01, flat_reach=False)
        add_account_days(c, "fangcun", "instagram", [700, 900, 1500, 1400, 1100, 900, 800])
        a = acct(c)
        self.assertEqual(a["reach_trend"], "falling3")
        self.assertEqual(a["decision"]["status"], "FIX")


class FixRetest(unittest.TestCase):
    def test_retest_window_replaces_the_standard_window(self):
        c = make_db()
        fill_window(c, n=12, er=0.004)                                          # weeks 3-6 at 0.4%: Fix band
        self.assertEqual(acct(c, as_of=day(56))["decision"]["status"], "FIX")
        c.execute("""INSERT INTO experiments(exp_id,persona,platform,kind,is_fix,name,start_date,end_date,status)
                     VALUES ('E1','fangcun','instagram','hook',1,'t',?,?,'done')""", (day(42).isoformat(), day(69).isoformat()))
        c.commit()
        for i in range(9):
            add_post(c, f"R{i}", "fangcun", "instagram", 42 + 3 * i, reach=1000, saves=2, shares=1, comments=1)          # 0.4% again
        a = acct(c, as_of=day(70))
        self.assertTrue(a["fix_retest"])
        self.assertEqual(a["summary"]["n_scored"], 9)
        self.assertEqual(a["decision"]["status"], "RETIRE_REVIEW")                 # still under 0.6% after the Fix re-test
        c.execute("DELETE FROM post_metrics WHERE post_id LIKE 'R%'")
        for i in range(9):
            c.execute("INSERT INTO post_metrics(post_id,snapshot_date,reach,saves,shares,comments) VALUES (?,?,?,?,?,?)", (f"R{i}", day(80).isoformat(), 1000, 4, 2, 2))
        c.commit()
        self.assertEqual(acct(c, as_of=day(70))["decision"]["status"], "KEEP")    # 0.8% after the re-test

    def test_non_fix_experiments_do_not_create_a_retest_window(self):
        c = make_db()
        fill_window(c, n=12, er=0.004)
        c.execute("INSERT INTO experiments(exp_id,persona,platform,kind,is_fix,name,start_date,end_date,status) VALUES ('E1','fangcun','instagram','hook',0,'t',?,?,'done')",
                  (day(42).isoformat(), day(69).isoformat()))
        c.commit()
        a = acct(c, as_of=day(70))
        self.assertFalse(a["fix_retest"])
        self.assertEqual(a["decision"]["status"], "FIX")

    def test_redesign_unlocks_the_effort_retire_review(self):
        c = make_db()
        fill_window(c, n=12, er=0.01)
        for i in range(6):
            add_effort(c, f"o{i}", "fangcun", 10, "operator", "approval", 20.0, post_id=f"Pfangcun-instagram-{i:02d}")
        a = acct(c)
        self.assertEqual(a["decision"]["status"], "FIX")
        self.assertTrue(a["decision"]["need_redesign"])
        c.execute("INSERT INTO experiments(exp_id,persona,kind,name,start_date,end_date,status) VALUES ('E9','fangcun','redesign','r',?,?,'done')", (day(30).isoformat(), day(40).isoformat()))
        c.commit()
        self.assertEqual(acct(c)["decision"]["status"], "RETIRE_REVIEW")


class Money(unittest.TestCase):
    def test_finance_rules(self):
        c = make_db()
        c.executemany("INSERT INTO costs(ref,cost_date,cost_kind,category,description,amount_twd) VALUES (?,?,?,?,?,?)", [
            ("a", "2026-11-05", "tool", "image_api", "x", 1450), ("b", "2026-11-20", "tool", "design", "x", 450),
            ("c", "2026-11-25", "one_time", "registration", "x", 1500), ("d", "2026-12-05", "tool", "image_api", "x", 1900),
            ("future", "2027-03-01", "tool", "x", "x", 9999)])
        c.executemany("INSERT INTO revenue(ref,revenue_date,source_type,amount_twd,status) VALUES (?,?,?,?,?)", [
            ("r1", "2026-12-02", "affiliate", 185, "received"), ("r2", "2026-12-03", "b2b_creative", 4000, "invoiced")])
        f = metrics.finance(c, dt.date(2026, 12, 10))
        nov, dec = f["months"]
        self.assertEqual((nov["tool"], nov["one_time"], nov["received"]), (1900, 1500, 0))
        self.assertEqual((dec["tool"], dec["received"], dec["invoiced"]), (1900, 185, 4000))
        self.assertEqual(f["cum_cost"], 1900 + 1500 + 1900)                                 # future-dated cost excluded
        self.assertEqual(f["cum_revenue"], 185)                                              # invoiced is not revenue
        self.assertEqual(f["current"]["tool"], 1900)
        self.assertEqual((f["cap_base"], f["cap_headroom"]), (5000, 10000))

    def test_capacity_averages_last_four_complete_weeks(self):
        c = make_db()
        fill_window(c, n=12, er=0.01, start=0, step=3)
        for w in range(1, 8):
            add_effort(c, f"op{w}", "fangcun", 7 * (w - 1) + 1, "operator", "admin", 300.0)
            add_effort(c, f"wf{w}", "fangcun", 7 * (w - 1) + 1, "wife", "moderation", 400.0)
        cap = metrics.capacity(c, day(49))
        self.assertTrue(cap["available"])
        self.assertEqual(len(cap["weeks"]), 4)
        self.assertEqual((cap["operator_avg"], cap["wife_avg"]), (300.0, 400.0))
        self.assertTrue(cap["pass"])
        add_effort(c, "big", "fangcun", 36, "operator", "admin", 100.0)                    # week 6 now 400 -> avg 325 > 324
        self.assertFalse(metrics.capacity(c, day(49))["pass"])

    def test_capacity_unavailable_without_a_time_log(self):
        c = make_db()
        fill_window(c, n=12, er=0.01, start=0, step=3)
        self.assertFalse(metrics.capacity(c, day(49))["available"])


class Snapshot(unittest.TestCase):
    def test_headline_is_the_best_active_account_and_paused_are_listed(self):
        c = make_db()
        fill_window(c, "sehuan", "instagram", n=12, er=0.004)                                # Fix
        fill_window(c, "sehuan", "threads", n=12, er=0.02)                                    # would be Keep or better...
        c.execute("INSERT INTO standing_events(ref,event_date,persona,platform,gate,description) VALUES ('g',?,?,?,?,?)", (day(40).isoformat(), "sehuan", "threads", "disclosure_failure", "t"))
        c.commit()
        snap = metrics.portfolio_snapshot(c, REVIEW_DAY)
        p = next(x for x in snap["personas"] if x["slug"] == "sehuan")
        self.assertEqual(p["headline"], "FIX")
        self.assertEqual(p["headline_account"], "instagram")
        self.assertEqual(p["paused"], ["threads"])

    def test_personas_follow_portfolio_order(self):
        snap = metrics.portfolio_snapshot(make_db(), REVIEW_DAY)
        self.assertEqual([p["slug"] for p in snap["personas"]], ["fangcun", "buzhou", "sehuan"])

    def test_empty_database_gives_not_started_everywhere(self):
        snap = metrics.portfolio_snapshot(make_db(), REVIEW_DAY)
        for p in snap["personas"]:
            self.assertEqual(p["headline"], "NOT_STARTED")
        self.assertFalse(snap["capacity"]["available"])
        self.assertEqual(snap["finance"]["months"], [])


if __name__ == "__main__":
    unittest.main()
