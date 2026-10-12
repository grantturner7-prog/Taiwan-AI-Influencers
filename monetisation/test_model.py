#!/usr/bin/env python3
"""Unit tests for model.py (standard library only).  Run:  python3 -m unittest -v test_model
(or: python3 test_model.py).  The tests check the assumptions table, the rate-card arithmetic against
independent hand calculations, the Phase 1 replay, the engine's accounting identities, the sensitivity
cases, and that the generated tables in the two documents are in sync with the model."""
import csv
import math
import os
import re
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import model as M  # noqa: E402


def read_csv_independently(path=M.CSV_PATH):
    """A second, deliberately separate reader of assumptions.csv, so tests do not rely on model.py's loader."""
    with open(path, encoding="utf-8", newline="") as fh:
        lines = [ln for ln in fh if ln.strip() and not ln.lstrip().startswith("#")]
    return {r["key"]: r for r in csv.DictReader(lines)}


def mini(rate=None, offer=None, extra=None):
    """A tiny assumptions table for hand-calculated cases. Every value is the same in all scenarios."""
    base = {
        "rate.op_hourly": 600, "rate.wife_hourly": 500, "rate.margin": 0.25, "rate.round_to": 100,
        "rate.cost_per_try": 10, "rate.revision_fraction": 0.2, "rate.rounds_included": 2,
        "rate.turnaround_hours_per_week": 1.5, "rate.turnaround_buffer_weeks": 1,
        "offer.X.fixed_op_min": 60, "offer.X.fixed_wife_min": 30, "offer.X.unit_op_min": 30,
        "offer.X.unit_wife_min": 6, "offer.X.tries": 2, "offer.X.s_units": 5, "offer.X.m_units": 10,
    }
    base.update(rate or {})
    base.update(offer or {})
    base.update(extra or {})
    rows = [{"key": k, "unit": "", "low": v, "mid": v, "high": v, "status": "assumption", "source": "test", "note": ""}
            for k, v in base.items()]
    return M.Assumptions(rows)


A0 = M.Assumptions.load()


class TestAssumptionsTable(unittest.TestCase):
    def test_loads_with_unique_keys(self):
        self.assertGreater(len(A0.rows), 100)
        self.assertEqual(len({r["key"] for r in A0.rows}), len(A0.rows))

    def test_statuses_are_valid(self):
        for r in A0.rows:
            self.assertIn(r["status"], M.VALID_STATUS, r["key"])

    def test_values_are_numeric_and_not_negative(self):
        for r in A0.rows:
            for s in M.SCENARIOS:
                self.assertIsInstance(r[s], float)
                self.assertGreaterEqual(r[s], 0.0, r["key"])

    def test_fractions_are_between_zero_and_one(self):
        for r in A0.rows:
            if r["unit"] == "fraction":
                for s in M.SCENARIOS:
                    self.assertLessEqual(r[s], 1.0, r["key"])

    def test_every_source_is_stated(self):
        for r in A0.rows:
            self.assertTrue(r["source"].strip(), r["key"])
            if r["status"] in ("sourced", "hypothetical", "computed", "excluded"):
                self.assertNotEqual(r["source"].strip().lower(), "none", r["key"])

    def test_placeholders_are_flagged_to_fill(self):
        placeholders = [r for r in A0.rows if r["status"] == "placeholder"]
        self.assertGreaterEqual(len(placeholders), 7)
        for r in placeholders:
            self.assertIn("TO FILL WHEN REAL", r["source"] + " " + r["note"], r["key"])

    def test_hypothetical_rows_cite_phase_1(self):
        for r in A0.rows:
            if r["status"] == "hypothetical":
                self.assertIn("monetisation.md", r["source"], r["key"])

    def test_more_is_better_inputs_are_ordered(self):
        keys = [k for k in A0.by_key if re.match(r"b2b\.(fangcun|buzhou|sehuan)\.[sm]_jobs$", k)]
        keys += [k for k in A0.by_key if k.startswith("aff.impressions.") or k.endswith(".units")]
        keys += ["aff.click_rate", "aff.commission", "b2b.realisation", "sp.realisation", "stk.sales_per_set_month", "b2b.samples",
                 "cap.op_hours_revenue_month", "cap.wife_hours_revenue_month"]
        for k in keys:
            r = A0.by_key[k]
            self.assertLessEqual(r["low"], r["mid"], k)
            self.assertLessEqual(r["mid"], r["high"], k)

    def test_first_months_are_not_later_in_better_scenarios(self):
        for k in ("b2b.first_paid_month", "sp.first_month", "prod.first_sale_month", "stk.first_month"):
            r = A0.by_key[k]
            self.assertGreaterEqual(r["low"], r["mid"], k)
            self.assertGreaterEqual(r["mid"], r["high"], k)

    def test_excluded_routes_are_zero_everywhere(self):
        for k in ("excl.platform_payouts", "excl.licensing"):
            for s in M.SCENARIOS:
                self.assertEqual(A0.get(k, s), 0.0)
        self.assertNotIn("payouts", M.ROUTES)
        self.assertNotIn("licensing", M.ROUTES)

    def test_tools_budget_is_the_stated_cap(self):
        self.assertEqual(A0.get("tools.budget", "mid"), 5000.0)  # DECISIONS.md Q1

    def test_every_key_renders_in_the_assumptions_table(self):
        text = M.render_assumptions(A0)
        for k in A0.by_key:
            self.assertIn("`%s`" % k, text)

    def test_duplicate_keys_are_rejected(self):
        row = {"key": "a", "unit": "", "low": 1, "mid": 1, "high": 1, "status": "assumption", "source": "x", "note": ""}
        with self.assertRaises(ValueError):
            M.Assumptions([row, row])

    def test_missing_key_raises(self):
        with self.assertRaises(KeyError):
            A0.get("no.such.key", "mid")


class TestRateCardMath(unittest.TestCase):
    def test_ceil_to(self):
        self.assertEqual(M.ceil_to(4300.0, 100), 4300)
        self.assertEqual(M.ceil_to(4300.01, 100), 4400)
        self.assertEqual(M.ceil_to(4299.99, 100), 4300)
        self.assertEqual(M.ceil_to(4300.0000000001, 100), 4300)  # float noise does not push it up
        self.assertEqual(M.ceil_to(1, 10), 10)

    def test_price_job_hand_calculation(self):
        A = mini()
        pj = M.price_job(A, "mid", "X", 5)
        # work = 5 x (1 + 2 x 0.2) = 7.0 unit-works
        # operator minutes = 60 + 30 x 7 = 270 (4.5 h x 600 = 2,700); wife minutes = 30 + 6 x 7 = 72 (1.2 h x 500 = 600)
        # tools = 2 tries x NT$10 x 7 = 140; floor = 3,440; with 25% margin = 4,300; turnaround ceil(4.5 / 1.5) + 1 = 4
        self.assertAlmostEqual(pj["work"], 7.0)
        self.assertAlmostEqual(pj["op_h"], 4.5)
        self.assertAlmostEqual(pj["wife_h"], 1.2)
        self.assertAlmostEqual(pj["op_value"], 2700.0)
        self.assertAlmostEqual(pj["wife_value"], 600.0)
        self.assertAlmostEqual(pj["tools"], 140.0)
        self.assertAlmostEqual(pj["floor"], 3440.0)
        self.assertAlmostEqual(pj["ask_raw"], 4300.0)
        self.assertEqual(pj["ask"], 4300)
        self.assertEqual(pj["weeks"], 4)

    def test_price_is_rounded_up_not_to_nearest(self):
        pj = M.price_job(mini(rate={"rate.margin": 0.26}), "mid", "X", 5)
        self.assertAlmostEqual(pj["ask_raw"], 4334.4)
        self.assertEqual(pj["ask"], 4400)

    def test_extra_minutes_are_added_once_and_not_multiplied_by_revisions(self):
        a = M.price_job(mini(), "mid", "X", 5)
        b = M.price_job(mini(), "mid", "X", 5, extra_op_min=60)
        self.assertAlmostEqual(b["op_h"] - a["op_h"], 1.0)
        self.assertAlmostEqual(b["floor"] - a["floor"], 600.0)

    def test_real_B1_small_matches_an_independent_hand_calculation(self):
        c = read_csv_independently()
        v = lambda k: float(c[k]["mid"])
        units = v("offer.B1.s_units")  # 3
        work = units * (1 + v("rate.rounds_included") * v("rate.revision_fraction"))  # 4.2
        op_min = v("offer.B1.fixed_op_min") + v("offer.B1.unit_op_min") * work  # 150 + 45 x 4.2 = 339
        wife_min = v("offer.B1.fixed_wife_min") + v("offer.B1.unit_wife_min") * work  # 75 + 10 x 4.2 = 117
        floor = op_min / 60 * v("rate.op_hourly") + wife_min / 60 * v("rate.wife_hourly") + \
            v("offer.B1.tries") * v("rate.cost_per_try") * work
        self.assertEqual((units, round(work, 6), op_min, wife_min), (3.0, 4.2, 339.0, 117.0))
        self.assertAlmostEqual(floor, 4581.72, places=2)  # 3,390 + 975 + 216.72
        self.assertAlmostEqual(floor * 1.25, 5727.15, places=2)
        pj = M.offer_price(A0, "mid", "B1", "s")
        self.assertAlmostEqual(pj["floor"], floor, places=6)
        self.assertEqual(pj["ask"], 5800)

    def test_every_offer_ask_is_above_floor_and_a_multiple_of_the_step(self):
        for code in ("B1", "B2", "B3"):
            for pkg in ("s", "m"):
                pj = M.offer_price(A0, "mid", code, pkg)
                self.assertGreater(pj["ask"], pj["floor"])
                self.assertEqual(pj["ask"] % 100, 0)
                self.assertLess(pj["ask"] - pj["ask_raw"], 100.0)
                self.assertGreaterEqual(pj["weeks"], 2)

    def test_medium_costs_more_than_small(self):
        for code in ("B1", "B2", "B3"):
            s = M.offer_price(A0, "mid", code, "s")
            m = M.offer_price(A0, "mid", code, "m")
            self.assertGreater(m["ask"], s["ask"])
            self.assertGreater(m["op_h"], s["op_h"])
            self.assertGreater(m["weeks"], s["weeks"])

    def test_sponsored_post_asks_never_fall_with_tier(self):
        asks = [M.sp_price(A0, "mid", t)["ask"] for t in (0, 1, 2, 3)]
        self.assertEqual(asks, sorted(asks))
        self.assertEqual(asks[0], 4200)
        self.assertEqual(asks[1], 4500)

    def test_price_rises_with_hourly_value(self):
        lo = M.Assumptions(A0.rows).set("rate.op_hourly", 400)
        hi = M.Assumptions(A0.rows).set("rate.op_hourly", 800)
        for code in ("B1", "B2", "B3"):
            self.assertLess(M.offer_price(lo, "mid", code, "s")["ask"], M.offer_price(hi, "mid", code, "s")["ask"])

    def test_price_rises_with_margin(self):
        a = M.Assumptions(A0.rows).set("rate.margin", 0.10)
        b = M.Assumptions(A0.rows).set("rate.margin", 0.40)
        self.assertLess(M.offer_price(a, "mid", "B1", "m")["ask"], M.offer_price(b, "mid", "B1", "m")["ask"])

    def test_incremental_extra_round_and_extra_unit(self):
        A = mini()
        rnd = M.incremental_price(A, "mid", "X", 5 * 0.2)  # one unit-work of revision on a 5-unit set
        # operator 30 min, wife 6 min, tools 2 x 10 = 20 -> 300 + 50 + 20 = 370 -> x 1.25 = 462.5 -> 500
        self.assertAlmostEqual(rnd["floor"], 370.0)
        self.assertEqual(rnd["ask"], 500)

    def test_extra_round_includes_fixed_handling_minutes(self):
        A = mini()
        rnd = M.incremental_price(A, "mid", "X", 5 * 0.2, fixed_op_min=20, fixed_wife_min=10)
        # operator 30 + 20 = 50 min (0.8333 h x 600 = 500); wife 6 + 10 = 16 min (0.2667 h x 500 = 133.33); tools 20
        self.assertAlmostEqual(rnd["floor"], 500.0 + 133.3333333 + 20.0, places=4)
        self.assertEqual(rnd["ask"], 900)  # 653.33 x 1.25 = 816.67 -> 900

    def test_real_extra_round_prices(self):
        text = M.render_addons(A0)
        self.assertIn("| B1 Lookbook stills set (fashion) |", text)
        b1s = M.offer_price(A0, "mid", "B1", "s")
        rnd = M.incremental_price(A0, "mid", "B1", b1s["units"] * 0.2, 20, 10)
        # 0.6 unit-works: operator (45 x 0.6 + 20) = 47 min -> 470; wife (10 x 0.6 + 10) = 16 min -> 133.33; tools 6 x 8.6 x 0.6 = 30.96
        self.assertAlmostEqual(rnd["floor"], 470.0 + 133.3333333 + 30.96, places=4)
        self.assertEqual(rnd["ask"], 800)

    def test_paid_media_handling_is_compliance_hours_only(self):
        pm = M.paid_media_price(A0, "mid")
        # 120 operator minutes = 2 h x 600 = 1,200; 30 wife minutes = 0.5 h x 500 = 250; floor 1,450; x 1.25 = 1,812.5 -> 1,900
        self.assertAlmostEqual(pm["floor"], 1450.0)
        self.assertEqual(pm["ask"], 1900)

    def test_product_price_repays_its_cost_at_the_payback_units(self):
        for pid in ("P1", "P2", "P3"):
            pj = M.product_price(A0, "mid", pid)
            fee = A0.get("prod.fee_rate", "mid")
            payback = A0.get("prod.payback_units", "mid")
            margin = A0.get("rate.margin", "mid")
            self.assertEqual(pj["price"] % 10, 0)
            self.assertGreaterEqual(pj["price"] * (1 - fee) * payback + 1e-6, pj["cost"] * (1 + margin))
            self.assertLess((pj["price"] - 10) * (1 - fee) * payback, pj["cost"] * (1 + margin))  # the smallest such step

    def test_product_hand_calculation(self):
        pj = M.product_price(A0, "mid", "P1")
        # 8 h x 600 + 3 h x 500 + 12 tries x 8.6 = 4,800 + 1,500 + 103.2 = 6,403.2; x 1.25 / 40 / 0.85 = 235.4 -> 240
        self.assertAlmostEqual(pj["cost"], 6403.2, places=6)
        self.assertEqual(pj["price"], 240)
        self.assertAlmostEqual(pj["net"], 204.0)

    def test_sticker_sales_needed_to_repay_hours(self):
        sc = M.sticker_set_cost(A0, "mid")
        # 12 h x 600 + 3 h x 500 + 40 tries x 8.6 = 7,200 + 1,500 + 344 = 9,044; share NT$12 -> about 754 sales
        self.assertAlmostEqual(sc["cost"], 9044.0, places=6)
        self.assertAlmostEqual(sc["sales_to_repay"], 9044.0 / 12.0, places=6)

    def test_licensing_has_no_price_in_the_table(self):
        self.assertFalse([k for k in A0.by_key if "licens" in k and k != "excl.licensing" and not k.startswith("phase1.")])


class TestPhase1Replay(unittest.TestCase):
    def test_totals_reproduce_the_phase_1_hypothesis(self):
        self.assertEqual(M.phase1_replay(A0, "low")["total"], 1000.0)
        self.assertEqual(M.phase1_replay(A0, "mid")["total"], 38000.0)
        self.assertEqual(M.phase1_replay(A0, "high")["total"], 202000.0)

    def test_route_cells(self):
        mid = M.phase1_replay(A0, "mid")["parts"]
        self.assertEqual((mid["b2b"], mid["sp"], mid["aff"], mid["stk"], mid["prod"]), (24000.0, 5000.0, 5000.0, 2000.0, 2000.0))
        high = M.phase1_replay(A0, "high")["parts"]
        self.assertEqual((high["b2b"], high["sp"], high["aff"], high["stk"], high["prod"]), (120000.0, 32000.0, 30000.0, 10000.0, 10000.0))
        self.assertEqual(M.phase1_replay(A0, "low")["parts"]["b2b"], 0.0)

    def test_versus_spend(self):
        self.assertEqual(M.phase1_replay(A0, "mid")["spend"], 60000.0)  # 12 x NT$5,000
        self.assertEqual([M.phase1_replay(A0, s)["delta"] for s in M.SCENARIOS], [-59000.0, -22000.0, 142000.0])

    def test_phase_1_range_endpoints(self):
        self.assertLessEqual(M.phase1_replay(A0, "low")["total"], 1000.0)
        self.assertAlmostEqual(M.phase1_replay(A0, "high")["total"], 200000.0, delta=5000.0)

    def test_nearest_package_for_the_phase_1_job_prices(self):
        self.assertEqual(M.nearest_package(A0, "mid", 8000.0)[:2], ("B3", "s"))
        self.assertEqual(M.nearest_package(A0, "high", 15000.0)[:2], ("B3", "m"))


class TestHelpers(unittest.TestCase):
    def test_spread_months(self):
        self.assertEqual(M.spread_months(6, 12, 3), [6, 9, 12])
        self.assertEqual(M.spread_months(3, 12, 3), [3, 8, 12])
        self.assertEqual(M.spread_months(5, 5, 4), [5, 5, 5, 5])
        self.assertEqual(M.spread_months(4, 12, 1), [4])
        self.assertEqual(M.spread_months(4, 12, 0), [])

    def test_month_labels(self):
        self.assertEqual(M.month_label(A0, 0), "2026-10")
        self.assertEqual(M.month_label(A0, 1), "2026-11")
        self.assertEqual(M.month_label(A0, 2), "2026-12")
        self.assertEqual(M.month_label(A0, 3), "2027-01")
        self.assertEqual(M.month_label(A0, 12), "2027-10")

    def test_money_and_number_formats(self):
        self.assertEqual(M.money(12345.4), "NT$12,345")
        self.assertEqual(M.money(-1200), "-NT$1,200")
        self.assertEqual(M.n0(1234567), "1,234,567")
        self.assertEqual(M.pct(0.255, 1), "25.5%")


class TestEngine(unittest.TestCase):
    def setUp(self):
        self.runs = {s: M.run(A0, s) for s in M.SCENARIOS}

    def test_deterministic(self):
        a, b = M.run(A0, "mid"), M.run(A0, "mid")
        self.assertEqual(M.total_rev(a), M.total_rev(b))
        self.assertEqual(a["hours_op"], b["hours_op"])

    def test_scenarios_are_ordered(self):
        r = self.runs
        self.assertLess(M.total_rev(r["low"]), M.total_rev(r["mid"]))
        self.assertLess(M.total_rev(r["mid"]), M.total_rev(r["high"]))
        self.assertLessEqual(sum(r["low"]["hours_op"]), sum(r["mid"]["hours_op"]))
        self.assertLessEqual(sum(r["mid"]["hours_op"]), sum(r["high"]["hours_op"]))

    def test_total_is_the_sum_of_the_five_routes(self):
        for res in self.runs.values():
            self.assertAlmostEqual(M.total_rev(res), sum(M.route_rev(res, r) for r in M.ROUTES))
            self.assertAlmostEqual(M.total_rev(res), sum(M.route_rev(res, "b2b", p) + M.route_rev(res, "sp", p) + M.route_rev(res, "aff", p)
                                                         + M.route_rev(res, "prod", p) + M.route_rev(res, "stk", p) for p in M.PERSONAS))

    def test_recognised_revenue_equals_cash_plus_receivable(self):
        for res in self.runs.values():
            for r in M.ROUTES:
                for p in M.PERSONAS:
                    got = sum(res["cash"][r][p]) + res["recv_end"][r][p]
                    self.assertAlmostEqual(sum(res["rev"][r][p]), got, places=6)

    def test_cash_never_arrives_before_the_lag(self):
        for res in self.runs.values():
            for r in M.ROUTES:
                lag = int(round(A0.get(M.LAG_KEY[r], res["scen"])))
                for p in M.PERSONAS:
                    first_rev = next((m for m, v in enumerate(res["rev"][r][p]) if v), None)
                    first_cash = next((m for m, v in enumerate(res["cash"][r][p]) if v), None)
                    if first_rev is not None and first_cash is not None:
                        self.assertGreaterEqual(first_cash, first_rev + lag)

    def test_cumulative_cash_identity(self):
        for res in self.runs.values():
            for inc in (False, True):
                net = M.net_series(res, inc)
                cum = M.cumulative(net)
                self.assertAlmostEqual(cum[-1], sum(net), places=6)
            gap = M.cumulative(M.net_series(res, False))[-1] - M.cumulative(M.net_series(res, True))[-1]
            self.assertAlmostEqual(gap, M.total_placeholders(res), places=6)
            expected = M.total_receipts(res) - sum(res["fees"]) - M.total_tools(res)
            self.assertAlmostEqual(M.cumulative(M.net_series(res, False))[-1], expected, places=6)

    def test_tools_plan_matches_the_cap_and_the_early_months_rule(self):
        res = self.runs["mid"]
        self.assertEqual(res["tools"][0], 0.0)
        self.assertEqual(res["tools"][1:4], [3000.0, 3000.0, 3000.0])  # 60% of NT$5,000 in months 1 to 3
        self.assertTrue(all(v == 5000.0 for v in res["tools"][4:]))
        self.assertEqual(M.total_tools(res), 54000.0)
        big = M.run(A0, "mid", tools_budget=10000.0)
        self.assertEqual(M.total_tools(big), 108000.0)
        self.assertEqual(max(big["tools"]), 10000.0)

    def test_placeholder_costs_sum(self):
        res = self.runs["mid"]
        self.assertEqual(sum(res["one_time"]), 10000 + 3000 + 10000 + 8000 + 10000)
        self.assertEqual(sum(res["bookkeeping"]), 12 * 1500)
        self.assertEqual(M.total_placeholders(res), 59000.0)
        self.assertEqual(res["one_time"][0], 23000.0)  # registration, bookkeeper set-up, launch-gate lawyer in M0

    def test_marketplace_fees_are_a_share_of_product_cash(self):
        for res in self.runs.values():
            prod_cash = sum(res["cash"]["prod"][p][m] for p in M.PERSONAS for m in range(res["T"] + 1))
            self.assertAlmostEqual(sum(res["fees"]), prod_cash * 0.15, places=6)

    def test_no_negative_flows(self):
        for res in self.runs.values():
            for r in M.ROUTES:
                for p in M.PERSONAS:
                    self.assertTrue(all(v >= 0 for v in res["rev"][r][p]))
                    self.assertTrue(all(v >= 0 for v in res["cash"][r][p]))
            self.assertTrue(all(v >= 0 for v in res["hours_op"]))

    def test_nothing_is_recognised_before_the_first_paid_month(self):
        res = self.runs["mid"]
        first = int(A0.get("b2b.first_paid_month", "mid"))
        for p in M.PERSONAS:
            self.assertTrue(all(v == 0 for v in res["rev"]["b2b"][p][:first]))

    def test_with_all_inputs_at_zero_nothing_is_earned(self):
        A = M.Assumptions(A0.rows)
        A.scale_prefix("b2b.", "_jobs", 0, ("mid",))
        A.scale_prefix("sp.", ".deals", 0, ("mid",))
        A.scale_prefix("aff.impressions.", "", 0, ("mid",))
        A.scale_prefix("prod.", ".units", 0, ("mid",))
        A.scale_prefix("stk.", ".sets", 0, ("mid",))
        res = M.run(A, "mid")
        self.assertEqual(M.total_rev(res), 0.0)
        self.assertEqual(M.total_receipts(res), 0.0)
        self.assertAlmostEqual(M.cumulative(M.net_series(res, False))[-1], -54000.0)

    def test_affiliate_funnel_arithmetic(self):
        A = M.Assumptions(A0.rows)
        for p in M.PERSONAS:
            A.set("aff.impressions." + p, 0)
        A.set("aff.impressions.fangcun", 100000)
        A.set("aff.ramp_months", 4).set("aff.first_month", 1)
        A.set("aff.click_rate", 0.01).set("aff.click_to_order", 0.02).set("aff.aov", 500).set("aff.commission", 0.05)
        res = M.run(A, "mid")
        # full month: 100,000 x 1% = 1,000 clicks; x 2% = 20 orders; x NT$500 = NT$10,000 GMV; x 5% = NT$500
        series = res["rev"]["aff"]["fangcun"]
        self.assertAlmostEqual(series[1], 500 * 0.25)
        self.assertAlmostEqual(series[2], 500 * 0.50)
        self.assertAlmostEqual(series[3], 500 * 0.75)
        self.assertAlmostEqual(series[4], 500.0)
        self.assertAlmostEqual(series[12], 500.0)
        self.assertAlmostEqual(sum(series), 500 * (0.25 + 0.5 + 0.75 + 9))
        self.assertAlmostEqual(res["aff"]["fangcun"]["gmv"], 10000 * 10.5)

    def test_b2b_job_timing_price_and_cash_lag(self):
        A = M.Assumptions(A0.rows)
        A.scale_prefix("b2b.", "_jobs", 0, ("mid",))
        A.set("b2b.sehuan.s_jobs", 3, ("mid",)).set("b2b.first_paid_month", 6).set("b2b.last_month", 12)
        A.set("b2b.realisation", 0.8).set("b2b.lag", 1)
        res = M.run(A, "mid")
        series = res["rev"]["b2b"]["sehuan"]
        realised = 5800 * 0.8
        self.assertEqual([m for m, v in enumerate(series) if v], [6, 9, 12])
        self.assertAlmostEqual(series[6], realised)
        cash = res["cash"]["b2b"]["sehuan"]
        self.assertEqual([m for m, v in enumerate(cash) if v], [7, 10])  # the M12 job is paid in M13, outside the horizon
        self.assertAlmostEqual(res["recv_end"]["b2b"]["sehuan"], realised)

    def test_cash_landing_exactly_in_month_12_is_counted_and_month_13_is_not(self):
        A = M.Assumptions(A0.rows)
        A.scale_prefix("b2b.", "_jobs", 0, ("mid",))
        A.set("b2b.sehuan.s_jobs", 1, ("mid",)).set("b2b.realisation", 1.0).set("b2b.lag", 1)
        A.set("b2b.first_paid_month", 11).set("b2b.last_month", 11)
        res = M.run(A, "mid")
        self.assertAlmostEqual(res["cash"]["b2b"]["sehuan"][12], 5800.0)
        self.assertEqual(res["recv_end"]["b2b"]["sehuan"], 0.0)
        A.set("b2b.first_paid_month", 12).set("b2b.last_month", 12)
        res = M.run(A, "mid")
        self.assertEqual(sum(res["cash"]["b2b"]["sehuan"]), 0.0)
        self.assertAlmostEqual(res["recv_end"]["b2b"]["sehuan"], 5800.0)

    def test_every_job_listed_is_priced_from_the_rate_card(self):
        res = self.runs["high"]
        for j in res["jobs"]:
            if j["route"] == "b2b":
                code, pkg = j["label"].split("-")
                self.assertEqual(j["ask"], M.offer_price(A0, "high", code, pkg.lower())["ask"])
                self.assertAlmostEqual(j["realised"], j["ask"] * A0.get("b2b.realisation", "high"))
            if j["route"] == "sample":
                self.assertEqual(j["realised"], 0.0)

    def test_samples_cost_hours_but_earn_nothing(self):
        res = self.runs["mid"]
        samples = [j for j in res["jobs"] if j["route"] == "sample"]
        self.assertEqual(len(samples), int(A0.get("b2b.samples", "mid")))
        self.assertTrue(all(j["op_h"] > 0 and j["realised"] == 0 for j in samples))
        self.assertEqual({j["persona"] for j in samples}, set(M.PERSONAS))

    def test_hours_by_persona_sum_to_the_monthly_totals(self):
        for res in self.runs.values():
            self.assertAlmostEqual(sum(h["op"] for h in res["hp"].values()), sum(res["hours_op"]))
            self.assertAlmostEqual(sum(h["wife"] for h in res["hp"].values()), sum(res["hours_wife"]))

    def test_capacity_flags(self):
        cap_mid = M.capacity(self.runs["mid"], A0)
        self.assertEqual(cap_mid["cap_op"], 7.5)
        self.assertAlmostEqual(cap_mid["total_op"], sum(self.runs["mid"]["hours_op"]))
        self.assertGreater(cap_mid["peak_op"], cap_mid["avg_op"])
        A = M.Assumptions(A0.rows).set("cap.op_hours_revenue_month", 1.0, ("mid",))
        cap = M.capacity(M.run(A, "mid"), A)
        self.assertFalse(cap["avg_within_cap"])
        self.assertGreater(cap["backlog_op_h"], 0)

    def test_effective_hourly_value_is_revenue_over_hours(self):
        res = self.runs["mid"]
        cap = M.capacity(res, A0)
        self.assertAlmostEqual(cap["effective_hourly"] * (cap["total_op"] + cap["total_wife"]), M.total_rev(res), places=6)

    def test_break_even_helpers(self):
        self.assertIsNone(M.first_cumulative_breakeven(self.runs["low"], False))
        self.assertIsNone(M.first_rolling_cover_month(self.runs["low"], False))
        self.assertIsNotNone(M.first_cumulative_breakeven(self.runs["high"], False))
        self.assertIsNone(M.first_cumulative_breakeven(self.runs["high"], True))  # the placeholders keep the high case below zero
        # with large B2B volume the sustained test is passed
        A = M.Assumptions(A0.rows).set("b2b.sehuan.m_jobs", 12, ("mid",))
        self.assertIsNotNone(M.first_rolling_cover_month(M.run(A, "mid"), False))

    def test_jobs_needed_for_a_target(self):
        self.assertIsNone(M.jobs_for_target(A0, "low", 200000.0))
        t = M.jobs_for_target(A0, "high", 200000.0)
        self.assertGreater(t["jobs"], 9)  # more than the high scenario's own 9 jobs
        self.assertAlmostEqual(t["jobs"] * t["avg_realised"], t["need"], places=6)

    def test_route_alone_figures(self):
        rows = M.route_alone(A0, "mid")
        b1 = next(r for r in rows if r["route"] == "B2B B1-S" and r["budget"] == 5000.0)
        self.assertAlmostEqual(b1["per_month"], 5000.0 / (5800 * 0.8))
        stk = next(r for r in rows if r["route"].startswith("LINE stickers") and r["budget"] == 5000.0)
        self.assertAlmostEqual(stk["per_month"], 5000.0 / 12.0)
        aff = next(r for r in rows if r["route"].startswith("Affiliate (Phase 1") and r["budget"] == 5000.0)
        self.assertAlmostEqual(aff["per_month"], 1000000.0)  # 5,000 / 5% = 100,000 GMV; / (1% x 2% x 500) = 1,000,000 impressions


class TestSensitivity(unittest.TestCase):
    def setUp(self):
        self.rows = {r["label"]: r for r in M.sensitivity(A0)}

    def test_base_row_equals_the_middle_scenario(self):
        res = M.run(A0, "mid")
        base = self.rows["Base: middle scenario"]
        self.assertAlmostEqual(base["rev"], M.total_rev(res))
        self.assertAlmostEqual(base["net_tools"], M.cumulative(M.net_series(res, False))[-1])
        self.assertEqual(base["d_rev"], 0.0)

    def test_the_input_table_is_not_changed_by_a_sensitivity_run(self):
        before = [dict(r) for r in A0.rows]
        M.sensitivity(A0)
        self.assertEqual(before, [dict(r) for r in A0.rows])

    def test_directions(self):
        r = self.rows
        self.assertLess(r["B2B realisation 0.6 (deeper discounts)"]["rev"], r["Base: middle scenario"]["rev"])
        self.assertGreater(r["B2B realisation 1.0 (full proposed price)"]["rev"], r["Base: middle scenario"]["rev"])
        self.assertEqual(r["B2B paid jobs: none (x0)"]["rev"], r["Base: middle scenario"]["rev"] - 15440)
        self.assertGreater(r["B2B paid jobs: triple (x3)"]["net_tools"], r["B2B paid jobs: double (x2)"]["net_tools"])
        self.assertLess(r["Impressions x0.5"]["rev"], r["Impressions x2"]["rev"])
        self.assertLess(r["No LINE stickers"]["rev"], r["Base: middle scenario"]["rev"])

    def test_cash_only_cases_leave_revenue_alone(self):
        base = self.rows["Base: middle scenario"]
        for label in ("Tools budget NT$10,000 (headroom used)", "Tools held at 60% of the cap (NT$3,000) all year",
                      "Compliance placeholders x0 (all free)", "Compliance placeholders x2"):
            self.assertAlmostEqual(self.rows[label]["rev"], base["rev"])
        self.assertAlmostEqual(self.rows["Tools budget NT$10,000 (headroom used)"]["d_net_tools"], -54000.0)
        self.assertAlmostEqual(self.rows["Tools held at 60% of the cap (NT$3,000) all year"]["d_net_tools"], 18000.0)

    def test_placeholders_scale(self):
        base = self.rows["Base: middle scenario"]
        self.assertAlmostEqual(self.rows["Compliance placeholders x0 (all free)"]["net_all"], base["net_tools"])
        self.assertAlmostEqual(self.rows["Compliance placeholders x2"]["net_all"], base["net_tools"] - 2 * 59000.0)

    def test_paying_the_wife_in_cash_lowers_net_cash_by_her_hours(self):
        res = M.run(A0, "mid")
        row = self.rows["Wife's review hours paid in cash at the assumed hourly value"]
        self.assertAlmostEqual(row["d_net_tools"], -sum(res["hours_wife"]) * 500.0, places=6)

    def test_late_cash_lands_outside_the_year(self):
        r = self.rows
        self.assertLess(r["B2B jobs all delivered in M12 (cash lands after the 12 months)"]["net_tools"],
                        r["B2B jobs delivered earlier (M4 to M10)"]["net_tools"])
        self.assertAlmostEqual(r["B2B jobs all delivered in M12 (cash lands after the 12 months)"]["rev"], r["Base: middle scenario"]["rev"])


class TestNoOutcomePromised(unittest.TestCase):
    """The model must never present a result as a promise or a market price."""

    def test_headline_names_every_scenario_and_stays_descriptive(self):
        text = M.render_headline(A0)
        for lab in ("Low", "Middle", "High"):
            self.assertIn(lab, text)
        for bad in ("will earn", "guarantee", "expect to earn"):
            self.assertNotIn(bad, text.lower())

    def test_module_docstring_disclaims_forecast(self):
        self.assertIn("NOTHING HERE IS A FORECAST OR A PROMISE", M.__doc__)

    def test_even_the_high_case_stays_below_the_phase_1_upper_end(self):
        self.assertLess(M.total_rev(M.run(A0, "high")), 202000.0)


class TestNarrativeClaims(unittest.TestCase):
    """Every sentence in revenue-model.md that interprets a number is asserted here, so editing an
    assumption cannot leave the prose saying something the numbers no longer support."""

    @classmethod
    def setUpClass(cls):
        cls.R = {s: M.run(A0, s) for s in M.SCENARIOS}
        cls.net_t = {s: M.cumulative(M.net_series(cls.R[s], False))[-1] for s in M.SCENARIOS}
        cls.net_a = {s: M.cumulative(M.net_series(cls.R[s], True))[-1] for s in M.SCENARIOS}
        cls.cap = {s: M.capacity(cls.R[s], A0) for s in M.SCENARIOS}

    def test_only_the_high_scenario_recovers_the_tools_spend(self):
        self.assertLess(self.net_t["low"], 0)
        self.assertLess(self.net_t["mid"], 0)
        self.assertGreater(self.net_t["high"], 0)

    def test_the_high_scenario_uses_more_than_half_of_the_operators_year(self):
        self.assertGreater(self.cap["high"]["share_of_year"], 0.5)

    def test_the_low_scenario_is_close_to_zero(self):
        self.assertLess(M.total_rev(self.R["low"]), 1000.0)

    def test_the_middle_scenario_recovers_less_than_half_of_the_tools_spend(self):
        res = self.R["mid"]
        covered = (M.total_receipts(res) - sum(res["fees"])) / M.total_tools(res)
        self.assertLess(covered, 0.5)

    def test_the_middle_scenarios_revenue_per_hour_is_below_half_the_assumed_value(self):
        c = self.cap["mid"]
        self.assertLess(c["effective_hourly"], 0.5 * c["blended_assumed_rate"])

    def test_no_scenario_recovers_the_spend_once_placeholders_are_included(self):
        for s in M.SCENARIOS:
            self.assertLess(self.net_a[s], 0)
            self.assertIsNone(M.first_cumulative_breakeven(self.R[s], True))

    def test_placeholders_are_the_same_order_as_the_tools_spend(self):
        ratio = M.total_placeholders(self.R["mid"]) / M.total_tools(self.R["mid"])
        self.assertGreater(ratio, 0.5)
        self.assertLess(ratio, 2.0)

    def test_the_high_scenario_only_roughly_covers_tools_plus_placeholders(self):
        res = self.R["high"]
        scale = M.total_tools(res) + M.total_placeholders(res)
        self.assertLess(abs(self.net_a["high"]), 0.25 * scale)

    def test_b2b_is_the_largest_route_in_the_middle_and_high_scenarios(self):
        for s in ("mid", "high"):
            res = self.R[s]
            b2b = M.route_rev(res, "b2b")
            for r in ("sp", "aff", "prod", "stk"):
                self.assertGreater(b2b, M.route_rev(res, r), (s, r))
            self.assertGreater(b2b / M.total_rev(res), 0.5)

    def test_reconciliation_directions(self):
        for s in ("mid", "high"):
            p1 = M.phase1_replay(A0, s)["parts"]
            res = self.R[s]
            self.assertLess(M.route_rev(res, "b2b"), p1["b2b"])
            self.assertLess(M.route_rev(res, "sp"), p1["sp"])
            self.assertLess(M.route_rev(res, "aff"), p1["aff"])
            self.assertGreater(M.route_rev(res, "prod"), p1["prod"])
            self.assertLess(M.route_rev(res, "stk"), p1["stk"])
        self.assertLess(M.total_rev(self.R["low"]), 1100.0)
        self.assertLess(M.phase1_replay(A0, "low")["total"], 1100.0)

    def test_the_phase_1_high_b2b_cell_is_about_eight_b3_m_jobs(self):
        code, pkg, pj = M.nearest_package(A0, "high", 15000.0)
        self.assertEqual((code, pkg), ("B3", "m"))
        self.assertGreater(8 * pj["op_h"] / (26.0 * 12), 0.3)

    def test_two_hundred_thousand_needs_more_jobs_than_the_high_scenario_has(self):
        t = M.jobs_for_target(A0, "high", 200000.0)
        self.assertGreater(t["jobs"], len([j for j in self.R["high"]["jobs"] if j["route"] == "b2b"]))

    def test_the_sustained_cover_for_the_high_scenario_is_after_the_lumpy_one(self):
        self.assertLessEqual(M.first_cover_month(self.R["high"], False), M.first_rolling_cover_month(self.R["high"], False))

    def test_break_even_by_b2b_alone_is_about_one_small_job_a_month(self):
        rows = {(r["route"], r["budget"]): r for r in M.route_alone(A0, "mid")}
        for code in ("B1-S", "B2-S"):
            r = rows[("B2B " + code, 5000.0)]
            self.assertGreater(r["per_month"], 0.8)
            self.assertLess(r["per_month"], 1.5)
            self.assertGreater(r["op_h"] / 26.0, 0.18)  # "a large share of the operator's 26 monthly hours"
            self.assertLess(r["op_h"] / 26.0, 0.35)
            self.assertGreater(rows[("B2B " + code, 10000.0)]["op_h"] / 26.0, 0.4)  # "about half" at NT$10,000
            self.assertLess(rows[("B2B " + code, 10000.0)]["op_h"] / 26.0, 0.6)

    def test_other_routes_alone_need_the_orders_of_magnitude_the_text_says(self):
        rows = {(r["route"], r["budget"]): r for r in M.route_alone(A0, "mid")}
        aff = [r for r in rows.values() if r["route"].startswith("Affiliate (this") and r["budget"] == 5000.0][0]
        self.assertGreater(aff["per_month"], 5e5)  # "on the order of a million impressions a month"
        self.assertLess(aff["per_month"], 5e6)
        stk = [r for r in rows.values() if r["route"].startswith("LINE stickers") and r["budget"] == 5000.0][0]
        self.assertGreater(stk["per_month"], 100)  # "hundreds of sales a month"
        prod = [r for r in rows.values() if r["route"].startswith("Product P1") and r["budget"] == 5000.0][0]
        self.assertGreater(prod["per_month"], 10)  # "tens of sales a month"
        self.assertLess(prod["per_month"], 100)

    def test_sensitivity_levers_in_the_order_the_text_gives(self):
        rows = {r["label"]: r for r in M.sensitivity(A0)}
        jobs = abs(rows["B2B paid jobs: double (x2)"]["d_net_tools"])
        tools = abs(rows["Tools budget NT$10,000 (headroom used)"]["d_net_tools"])
        for label in ("Impressions x2", "Affiliate commission 8% (Phase 1 axis)", "No LINE stickers",
                      "Sticker creator share NT$16 (Phase 1 axis)", "Link click rate halved"):
            self.assertLess(abs(rows[label]["d_net_tools"]), jobs, label)
            self.assertLess(abs(rows[label]["d_net_tools"]), tools, label)
        self.assertGreater(abs(rows["Own product units x3"]["d_net_tools"]), abs(rows["No LINE stickers"]["d_net_tools"]))

    def test_paying_the_wife_in_cash_makes_every_scenario_worse(self):
        for s in M.SCENARIOS:
            base = M.cumulative(M.net_series(M.run(A0, s), False))[-1]
            paid = M.cumulative(M.net_series(M.run(A0, s, wife_paid=True), False))[-1]
            self.assertLessEqual(paid, base)
        self.assertLess(M.cumulative(M.net_series(M.run(A0, "mid", wife_paid=True), False))[-1], self.net_t["mid"])

    def test_numbers_quoted_in_the_prose_match_the_table(self):
        c = read_csv_independently()
        v = lambda k: float(c[k]["mid"])
        self.assertEqual(v("prod.payback_units"), 40)          # "repaid at 40 sales"
        self.assertEqual(v("aff.ramp_months"), 8)              # "ramped linearly over 8 months"
        self.assertEqual(v("aff.admin_op_min_month"), 30)      # "30 operator minutes a month"
        self.assertEqual(v("tools.early_fraction"), 0.6)       # "at 60% in months 1 to 3"
        self.assertEqual(v("tools.early_months"), 3)
        self.assertEqual(v("tools.budget") * (3 * 0.6 + 9), 54000)  # "NT$54,000 over M1 to M12"
        self.assertEqual(v("rate.turnaround_hours_per_week"), 1.5)  # "about 1.5" in the rate card
        self.assertEqual(v("rate.revision_fraction"), 0.2)     # "about a fifth of a set"
        self.assertEqual(v("rate.rounds_included"), 2)         # "two rounds"
        self.assertEqual(v("prod.round_to"), 10)               # "rounded up to NT$10"
        self.assertEqual(v("rate.round_to"), 100)              # "next NT$100"
        self.assertEqual(v("cap.op_hours_month_total"), 26)    # "26 monthly hours"
        placeholders = [r for r in c.values() if r["status"] == "placeholder"]
        self.assertEqual(len(placeholders), 8)                 # "Placeholder (8 rows)"
        self.assertEqual(int(c["offer.SP.report_op_min.t1"]["mid"]), 30)

    def test_wife_cap_matches_the_portfolio_headroom(self):
        # 108 min/week headroom x 52 / 12 / 60 = 7.8 h a month; the middle cap is 8
        self.assertAlmostEqual(108 * 52 / 12 / 60, 7.8, places=6)
        self.assertEqual(A0.get("cap.wife_hours_revenue_month", "mid"), 8.0)


class TestDocuments(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(M.RATE_CARD_MD, encoding="utf-8") as fh:
            cls.rate = fh.read()
        with open(M.REVENUE_MD, encoding="utf-8") as fh:
            cls.rev = fh.read()
        cls.both = cls.rate + "\n" + cls.rev

    def test_generated_tables_are_in_sync_with_the_model(self):
        self.assertEqual(M.docs(False), [], "run: python3 model.py docs --write")

    def test_every_generated_block_is_used_exactly_once(self):
        for name in M.blocks(A0):
            self.assertEqual(self.both.count(M.GEN_BEGIN.format(name)), 1, name)
            self.assertEqual(self.both.count(M.GEN_END.format(name)), 1, name)

    def test_no_unknown_block_names(self):
        self.assertEqual(M.unknown_blocks(self.both, M.blocks(A0)), [])

    def test_monthly_csv_is_in_sync(self):
        with open(M.MONTHLY_CSV, encoding="utf-8") as fh:
            self.assertEqual(fh.read(), M.monthly_csv_text(A0), "run: python3 model.py csv")

    def test_rate_card_carries_the_required_caveats(self):
        t = self.rate
        for needle in ("[TO FILL WHEN REAL]", "3+ real quotes", "G1", "G11", "unverified, lawyer question",
                       "verify existence and current contact route before outreach", "no price", "not found"):
            self.assertIn(needle, t, needle)

    def test_rate_card_lists_the_exclusions(self):
        t = self.rate.lower()
        for needle in ("testimonial", "health", "weight-loss", "investment", "gambling", "politic", "loan"):
            self.assertIn(needle, t, needle)

    def test_rate_card_covers_every_offer(self):
        for needle in ("B1", "B2", "B3", "Sponsored post", "Affiliate", "checklist", "LINE sticker", "spokes-character"):
            self.assertIn(needle, self.rate, needle)

    def test_revenue_model_states_no_outcome_is_promised(self):
        t = self.rev
        self.assertIn("No outcome is promised", t)
        self.assertIn("NT$0 to about NT$200,000", t)
        self.assertIn("not a forecast", t.lower())
        self.assertIn("pre-tax", t.lower())

    def test_no_mainland_vocabulary_or_simplified_only_forms(self):
        for bad in ("視頻", "信息", "質量", "博主", "軟件", "網絡", "數據", "视频", "信息化", "质量", "软件", "网络", "数据"):
            self.assertNotIn(bad, self.both, bad)

    def test_no_invented_clients_results_or_contact_details(self):
        for pat in (r"\bour (clients|customers|followers|subscribers)\b", r"\bwe (have|had) (worked|delivered|served)\b",
                    r"[\w.]+@[\w.]+\.\w+", r"\b0\d{1,2}-\d{3,4}-\d{3,4}\b", r"https?://"):
            self.assertIsNone(re.search(pat, self.both, re.I), pat)

    def test_prices_in_the_rate_card_summary_match_the_model(self):
        for code in ("B1", "B2", "B3"):
            for pkg in ("s", "m"):
                ask = M.offer_price(A0, "mid", code, pkg)["ask"]
                row = [ln for ln in self.rate.splitlines() if ln.startswith("| %s-%s |" % (code, pkg.upper()))]
                self.assertTrue(row, code + pkg)
                self.assertIn("**{:,}**".format(ask), row[0])


if __name__ == "__main__":
    unittest.main(verbosity=2)
