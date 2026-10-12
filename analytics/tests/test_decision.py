"""The 6.3 decision tree, one branch per test. Pure function: no database."""
import unittest

import _path  # noqa: F401
import thresholds as T
from decision import decide


def facts(**kw):
    base = dict(persona="p", platform="instagram", data_state="scored", provisional=False, n_scored=12, min_sample=8,
                window_label="weeks 3 to 6", er=0.010, sv_share=0.5, reach_trend="flat", gates_open=[], retire_triggers=[],
                events_in_window=0,
                effort={"operator_min_per_approval": {"value": 7.0, "n": 20, "scored": True},
                        "wife_min_per_master": {"value": 9.0, "n": 12, "scored": True}},
                rejection={"value": 0.08, "n": 18, "scored": True},
                redesign_done=False, fix_retest_done=False, lead_signals=0, link_weeks=0, watch=[])
    base.update(kw)
    return base


class Tree(unittest.TestCase):
    def status(self, **kw):
        return decide(facts(**kw))["status"]

    # ---- step 1 ----
    def test_open_gate_pauses_before_anything_else(self):
        r = decide(facts(gates_open=["Disclosure missing"], er=0.05))
        self.assertEqual(r["status"], "PAUSE")
        self.assertIn("Disclosure missing", r["reasons"])

    def test_retire_trigger_beats_pause(self):
        self.assertEqual(self.status(gates_open=["x"], retire_triggers=["second rule-6 event"]), "RETIRE")

    # ---- step 2 ----
    def test_not_started(self):
        self.assertEqual(self.status(data_state="not_started"), "NOT_STARTED")

    def test_in_progress_gives_no_reading(self):
        r = decide(facts(data_state="in_progress", n_scored=5))
        self.assertEqual(r["status"], "IN_PROGRESS")
        self.assertIn("5 of 8", r["reasons"][0])

    def test_extend_and_hold(self):
        self.assertEqual(self.status(data_state="extend", n_scored=6, n_extended=9), "EXTEND")
        r = decide(facts(data_state="hold", n_scored=7))
        self.assertEqual(r["status"], "HOLD")
        self.assertIn("no scoring", r["reasons"][0])

    # ---- step 3 ----
    def test_effort_breach_after_redesign_is_retire_review(self):
        e = {"operator_min_per_approval": {"value": 16.0, "n": 20, "scored": True}}
        self.assertEqual(self.status(effort=e, redesign_done=True), "RETIRE_REVIEW")

    def test_effort_breach_without_redesign_is_fix_and_asks_for_one(self):
        e = {"operator_min_per_approval": {"value": 16.0, "n": 20, "scored": True}}
        r = decide(facts(effort=e))
        self.assertEqual(r["status"], "FIX")
        self.assertTrue(r["need_redesign"])

    def test_n7_and_wife_and_rejection_breach_lines(self):
        self.assertEqual(self.status(effort={"n7_min_per_master": {"value": 41, "n": 9, "scored": True}}, redesign_done=True), "RETIRE_REVIEW")
        self.assertEqual(self.status(effort={"wife_min_per_master": {"value": 21, "n": 9, "scored": True}}, redesign_done=True), "RETIRE_REVIEW")
        self.assertEqual(self.status(rejection={"value": 0.31, "n": 20, "scored": True}, redesign_done=True), "RETIRE_REVIEW")
        # exactly on the line is still the Fix zone, not a breach
        self.assertEqual(self.status(effort={"operator_min_per_approval": {"value": 15.0, "n": 20, "scored": True}}, redesign_done=True), "FIX")

    # ---- steps 4 and 5 ----
    def test_er_boundaries(self):
        self.assertEqual(self.status(er=T.ER_FIX - 1e-9), "RETIRE_REVIEW")
        self.assertEqual(self.status(er=T.ER_FIX), "FIX")
        self.assertEqual(self.status(er=T.ER_KEEP - 1e-9), "FIX")
        self.assertEqual(self.status(er=T.ER_KEEP), "KEEP")

    def test_fix_band_after_retest_is_retire_review(self):
        self.assertEqual(self.status(er=0.004, fix_retest_done=True), "RETIRE_REVIEW")

    def test_retest_keep_needs_er_and_effort_within_keep(self):
        self.assertEqual(self.status(er=0.007, fix_retest_done=True), "KEEP")
        e = {"operator_min_per_approval": {"value": 13.0, "n": 20, "scored": True}}
        self.assertEqual(self.status(er=0.007, fix_retest_done=True, effort=e), "RETIRE_REVIEW")

    # ---- step 6 ----
    def test_keep(self):
        r = decide(facts())
        self.assertEqual(r["status"], "KEEP")

    def test_falling_reach_or_high_rejection_blocks_keep(self):
        self.assertEqual(self.status(reach_trend="falling2"), "FIX")
        self.assertEqual(self.status(reach_trend="falling3"), "FIX")
        self.assertEqual(self.status(rejection={"value": 0.25, "n": 20, "scored": True}), "FIX")
        e = {"operator_min_per_approval": {"value": 13.0, "n": 20, "scored": True}}
        self.assertEqual(self.status(effort=e), "FIX")

    def test_unlogged_effort_does_not_block_keep_but_is_flagged(self):
        r = decide(facts(effort={}, rejection=None))
        self.assertEqual(r["status"], "KEEP")
        self.assertTrue(any("not logged" in c for c in r["caveats"]))

    def test_unscored_small_effort_sample_is_unknown_not_bad(self):
        e = {"operator_min_per_approval": {"value": 40.0, "n": 2, "scored": False}}
        self.assertEqual(self.status(effort=e), "KEEP")

    # ---- step 7 ----
    def scale_facts(self, **kw):
        base = dict(er=0.025, sv_share=0.4, reach_trend="rising", lead_signals=1,
                    effort={"operator_min_per_approval": {"value": 6.0, "n": 20, "scored": True},
                            "wife_min_per_master": {"value": 9.0, "n": 12, "scored": True}},
                    rejection={"value": 0.05, "n": 20, "scored": True})
        base.update(kw)
        return facts(**base)

    def test_scale_eligible_when_every_condition_holds(self):
        r = decide(self.scale_facts())
        self.assertEqual(r["status"], "SCALE_ELIGIBLE")
        self.assertTrue(all(v is True for v in r["scale_checks"].values()))

    def test_scale_links_or_lead(self):
        self.assertEqual(decide(self.scale_facts(lead_signals=0, link_weeks=3))["status"], "SCALE_ELIGIBLE")
        r = decide(self.scale_facts(lead_signals=0, link_weeks=2))
        self.assertEqual(r["status"], "KEEP")
        self.assertIn("Scale blocked by", " ".join(r["reasons"]))

    def test_each_scale_condition_blocks_scale(self):
        for kw in (dict(sv_share=0.30), dict(reach_trend="flat"), dict(events_in_window=1),
                   dict(rejection={"value": 0.15, "n": 20, "scored": True}),
                   dict(effort={"operator_min_per_approval": {"value": 9.0, "n": 20, "scored": True}})):
            self.assertEqual(decide(self.scale_facts(**kw))["status"], "KEEP", kw)

    def test_scale_cannot_be_confirmed_without_saves_or_effort_data(self):
        r = decide(self.scale_facts(sv_share=None))
        self.assertEqual(r["status"], "KEEP")
        self.assertIn("cannot be confirmed", " ".join(r["reasons"]))
        r = decide(self.scale_facts(rejection=None))
        self.assertEqual(r["status"], "KEEP")

    def test_high_er_with_failed_keep_conditions_is_fix_not_scale(self):
        self.assertEqual(decide(self.scale_facts(reach_trend="falling2"))["status"], "FIX")

    # ---- provisional flag and watch ----
    def test_provisional_flag_only_on_scored_statuses(self):
        self.assertTrue(decide(facts(provisional=True))["provisional"])
        self.assertFalse(decide(facts(provisional=True, data_state="in_progress", n_scored=4))["provisional"])

    def test_reach_falling_3_with_low_er_adds_watch_but_follows_the_tree(self):
        r = decide(facts(er=0.004, reach_trend="falling3"))
        self.assertEqual(r["status"], "FIX")
        self.assertTrue(any("retire-review trigger" in w for w in r["watch"]))

    def test_every_status_has_label_icon_rank(self):
        import dashboard
        for st in T.STATUS_LABELS:
            self.assertIn(st, T.STATUS_RANK)
            self.assertIn(st, dashboard.ICONS)
            self.assertIn(st, dashboard.STATUS_CLASS)


if __name__ == "__main__":
    unittest.main()
