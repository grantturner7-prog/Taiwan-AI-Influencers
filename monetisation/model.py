#!/usr/bin/env python3
"""Rate-card calculator and 12-month revenue model for the studio (standard library only).

Reads assumptions.csv (same folder) and recomputes:
  * the studio's PROPOSED prices (rate card): hours x assumed hourly value + tool cost + margin;
  * low / middle / high 12-month scenarios per revenue route and per persona;
  * a month-by-month cash view against the tools budget, plus one-time and recurring cost placeholders;
  * break-even figures, a sensitivity table and a reconciliation with the Phase 1 hypothesis.

NOTHING HERE IS A FORECAST OR A PROMISE. Every input is a sourced figure, a hypothetical axis value from
research/monetisation.md, a studio planning assumption or a placeholder. No Taiwan market price was found.

Usage (run from anywhere):
  python3 model.py                 summary of the three scenarios
  python3 model.py rates           the proposed prices and their derivation
  python3 model.py cash [scen]     month-by-month cash view (low, mid or high; default mid)
  python3 model.py breakeven       break-even figures
  python3 model.py sens            one-at-a-time sensitivity around the mid scenario
  python3 model.py reconcile       Phase 1 replay and the hours behind it
  python3 model.py docs --check    exit 1 if the generated tables in the .md files are stale
  python3 model.py docs --write    refresh the generated tables in rate-card.md and revenue-model.md
  python3 model.py csv             write monthly-cash.csv
  python3 -m unittest -v test_model   run the unit tests
"""
from __future__ import annotations

import csv
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(HERE, "assumptions.csv")
RATE_CARD_MD = os.path.join(HERE, "rate-card.md")
REVENUE_MD = os.path.join(HERE, "revenue-model.md")
MONTHLY_CSV = os.path.join(HERE, "monthly-cash.csv")

SCENARIOS = ("low", "mid", "high")
SCEN_LABEL = {"low": "Low", "mid": "Middle", "high": "High"}
PERSONAS = ("fangcun", "buzhou", "sehuan")
PERSONA_NAME = {
    "fangcun": "方寸 (home organisation)",
    "buzhou": "步驟 (AI tools)",
    "sehuan": "色環 (outfit logic and colour)",
}
ROUTES = ("b2b", "sp", "aff", "prod", "stk")
ROUTE_NAME = {
    "b2b": "B2B creative (studio level)",
    "sp": "Sponsored posts (業配)",
    "aff": "Affiliate (聯盟行銷)",
    "prod": "Own digital products",
    "stk": "LINE stickers",
}
LAG_KEY = {"b2b": "b2b.lag", "sp": "sp.lag", "aff": "aff.lag", "prod": "prod.lag", "stk": "stk.lag"}
OFFER_FOR_PERSONA = {"sehuan": "B1", "fangcun": "B2", "buzhou": "B3"}
PRODUCT_FOR_PERSONA = {"fangcun": "P1", "buzhou": "P2", "sehuan": "P3"}
SAMPLE_ORDER = ("sehuan", "fangcun", "buzhou")
OFFER_NAME = {
    "B1": "Lookbook stills set (fashion)",
    "B2": "Room-render diagram set (home)",
    "B3": "Explainer stills set (software and SMEs)",
    "SP": "Sponsored post (業配)",
}
UNIT_NAME = {"B1": "stills", "B2": "diagrams", "B3": "cards", "SP": "masters"}
PRODUCT_NAME = {
    "P1": "方寸 printable checklist and template pack",
    "P2": "步驟 template and prompt pack",
    "P3": "色環 colour guide (wheel and chip cards)",
}
COST_ITEMS = (
    ("registration", "Business registration"),
    ("bookkeeper_setup", "Bookkeeper (記帳士) set-up"),
    ("lawyer_launch", "Lawyer: launch-gate consult"),
    ("lawyer_contract", "Lawyer: contract template review"),
    ("trademark", "Trade mark filing (studio name)"),
)
VALID_STATUS = ("sourced", "computed", "assumption", "hypothetical", "placeholder", "excluded")
GEN_BEGIN = "<!-- BEGIN GENERATED:{} -->"
GEN_END = "<!-- END GENERATED:{} -->"
EPS = 1e-9


# ----------------------------------------------------------------------------------------------
# Assumptions table
# ----------------------------------------------------------------------------------------------
class Assumptions:
    """The assumptions table. Values are floats per scenario. Immutable by convention: use copy()."""

    def __init__(self, rows):
        self.rows = [dict(r) for r in rows]
        for r in self.rows:
            for s in SCENARIOS:
                r[s] = float(r[s])
        self.by_key = {r["key"]: r for r in self.rows}
        if len(self.by_key) != len(self.rows):
            raise ValueError("duplicate keys in the assumptions table")

    @classmethod
    def load(cls, path=CSV_PATH):
        with open(path, encoding="utf-8", newline="") as fh:
            lines = [ln for ln in fh if ln.strip() and not ln.lstrip().startswith("#")]
        return cls(list(csv.DictReader(lines)))

    def get(self, key, scen):
        try:
            return self.by_key[key][scen]
        except KeyError:
            raise KeyError("missing assumption: " + key) from None

    def copy(self):
        return Assumptions(self.rows)

    def set(self, key, value, scens=SCENARIOS):
        for s in scens:
            self.by_key[key][s] = float(value)
        return self

    def scale(self, key, factor, scens=SCENARIOS):
        for s in scens:
            self.by_key[key][s] = self.by_key[key][s] * factor
        return self

    def scale_prefix(self, prefix, suffix, factor, scens=SCENARIOS):
        for k, row in self.by_key.items():
            if k.startswith(prefix) and k.endswith(suffix):
                for s in scens:
                    row[s] = row[s] * factor
        return self


# ----------------------------------------------------------------------------------------------
# Small helpers
# ----------------------------------------------------------------------------------------------
def ceil_to(x, step):
    """Round UP to a multiple of step (tolerant of float noise)."""
    return int(math.ceil(x / step - EPS) * step)


def spread_months(first, last, count):
    """Spread `count` events evenly over months first..last (inclusive), deterministic."""
    if count <= 0:
        return []
    if count == 1 or last <= first:
        return [int(first)] * count
    return [int(first + math.floor(i * (last - first) / (count - 1) + 0.5)) for i in range(count)]


def month_label(A, m):
    y = int(A.get("model.start_year", "mid"))
    mo = int(A.get("model.start_month", "mid"))
    idx = (mo - 1) + (m - 1)
    return "%d-%02d" % (y + idx // 12, idx % 12 + 1)


def n0(x):
    return "{:,}".format(int(round(x)))


def money(x):
    return ("-" if round(x) < 0 else "") + "NT$" + "{:,}".format(abs(int(round(x))))


def pct(x, digits=0):
    return ("{:.%df}%%" % digits).format(x * 100)


def md_table(headers, rows, align=None):
    align = align or ["l"] + ["r"] * (len(headers) - 1)
    sep = {"l": ":---", "r": "---:", "c": ":---:"}
    out = ["| " + " | ".join(headers) + " |", "| " + " | ".join(sep[a] for a in align) + " |"]
    for r in rows:
        out.append("| " + " | ".join(str(c) for c in r) + " |")
    return "\n".join(out)


# ----------------------------------------------------------------------------------------------
# Rate card: proposed prices
# ----------------------------------------------------------------------------------------------
def price_job(A, scen, code, units, extra_op_min=0.0, extra_wife_min=0.0):
    """Proposed price of a job: hours x assumed hourly value + tool cost, plus margin, rounded up."""
    g = lambda k: A.get("offer.%s.%s" % (code, k), scen)
    r = lambda k: A.get("rate." + k, scen)
    work = units * (1.0 + r("rounds_included") * r("revision_fraction"))
    op_min = g("fixed_op_min") + g("unit_op_min") * work + extra_op_min
    wife_min = g("fixed_wife_min") + g("unit_wife_min") * work + extra_wife_min
    op_h, wife_h = op_min / 60.0, wife_min / 60.0
    op_value = op_h * r("op_hourly")
    wife_value = wife_h * r("wife_hourly")
    tools = g("tries") * r("cost_per_try") * work
    floor = op_value + wife_value + tools
    ask_raw = floor * (1.0 + r("margin"))
    ask = ceil_to(ask_raw, r("round_to"))
    weeks = int(math.ceil(op_h / r("turnaround_hours_per_week") - EPS)) + int(r("turnaround_buffer_weeks"))
    return {
        "code": code, "units": units, "work": work, "op_h": op_h, "wife_h": wife_h,
        "op_value": op_value, "wife_value": wife_value, "tools": tools, "floor": floor,
        "ask_raw": ask_raw, "ask": ask, "weeks": weeks,
    }


def offer_price(A, scen, code, pkg):
    """pkg is 's' or 'm' for B1, B2, B3."""
    return price_job(A, scen, code, A.get("offer.%s.%s_units" % (code, pkg), scen))


def sp_price(A, scen, tier):
    extra = A.get("offer.SP.report_op_min.t%d" % int(tier), scen)
    return price_job(A, scen, "SP", A.get("offer.SP.units", scen), extra_op_min=extra)


def incremental_price(A, scen, code, work_units, fixed_op_min=0.0, fixed_wife_min=0.0):
    """Price of `work_units` unit-works plus optional fixed handling minutes (extra round: the handling; extra unit: none)."""
    g = lambda k: A.get("offer.%s.%s" % (code, k), scen)
    r = lambda k: A.get("rate." + k, scen)
    op_h = (g("unit_op_min") * work_units + fixed_op_min) / 60.0
    wife_h = (g("unit_wife_min") * work_units + fixed_wife_min) / 60.0
    tools = g("tries") * r("cost_per_try") * work_units
    floor = op_h * r("op_hourly") + wife_h * r("wife_hourly") + tools
    return {"floor": floor, "ask": ceil_to(floor * (1.0 + r("margin")), r("round_to")), "op_h": op_h, "wife_h": wife_h}


def paid_media_price(A, scen):
    r = lambda k: A.get("rate." + k, scen)
    op_h, wife_h = r("paid_media_op_min") / 60.0, r("paid_media_wife_min") / 60.0
    floor = op_h * r("op_hourly") + wife_h * r("wife_hourly")
    return {"floor": floor, "ask": ceil_to(floor * (1.0 + r("margin")), r("round_to")), "op_h": op_h, "wife_h": wife_h}


def product_price(A, scen, pid):
    """List price: production cost plus margin, repaid at prod.payback_units net of fees, rounded up."""
    g = lambda k: A.get("prod.%s.%s" % (pid, k), scen)
    r = lambda k: A.get("rate." + k, scen)
    p = lambda k: A.get("prod." + k, scen)
    tools = p("tries") * r("cost_per_try")
    cost = g("op_h") * r("op_hourly") + g("wife_h") * r("wife_hourly") + tools
    fee = p("fee_rate")
    price_raw = cost * (1.0 + r("margin")) / p("payback_units") / (1.0 - fee)
    price = ceil_to(price_raw, p("round_to"))
    net = price * (1.0 - fee)
    return {
        "pid": pid, "op_h": g("op_h"), "wife_h": g("wife_h"), "tools": tools, "cost": cost,
        "price_raw": price_raw, "price": price, "net": net, "units_to_repay": cost / net,
    }


def sticker_set_cost(A, scen):
    r = lambda k: A.get("rate." + k, scen)
    s = lambda k: A.get("stk." + k, scen)
    tools = s("set_tries") * r("cost_per_try")
    cost = s("set_op_h") * r("op_hourly") + s("set_wife_h") * r("wife_hourly") + tools
    share = s("creator_share")
    return {"cost": cost, "tools": tools, "share": share, "sales_to_repay": cost / share}


# ----------------------------------------------------------------------------------------------
# The 12-month engine
# ----------------------------------------------------------------------------------------------
def run(A, scen, tools_budget=None, wife_paid=False):
    """Compute one scenario. Month index 0..T (0 = pre-launch). Money in NT$, hours in hours."""
    g = lambda k: A.get(k, scen)
    T = int(g("model.months"))
    z = lambda: [0.0] * (T + 1)
    rev = {r: {p: z() for p in PERSONAS} for r in ROUTES}
    hours_op, hours_wife, memo_tools = z(), z(), z()
    hp = {p: {"op": 0.0, "wife": 0.0} for p in PERSONAS}
    jobs = []

    def add_hours(m, p, op_h, wife_h, tools=0.0):
        hours_op[m] += op_h
        hours_wife[m] += wife_h
        memo_tools[m] += tools
        hp[p]["op"] += op_h
        hp[p]["wife"] += wife_h

    # B2B jobs, spread evenly; small jobs first, then medium
    real = g("b2b.realisation")
    first = min(T, max(1, int(round(g("b2b.first_paid_month")))))
    last = min(T, max(first, int(round(g("b2b.last_month")))))
    job_list = []
    for pkg in ("s", "m"):
        for p in PERSONAS:
            for _ in range(int(round(g("b2b.%s.%s_jobs" % (p, pkg))))):
                job_list.append((p, pkg))
    for (p, pkg), m in zip(job_list, spread_months(first, last, len(job_list))):
        pj = offer_price(A, scen, OFFER_FOR_PERSONA[p], pkg)
        realised = pj["ask"] * real
        rev["b2b"][p][m] += realised
        add_hours(m, p, pj["op_h"], pj["wife_h"], pj["tools"])
        jobs.append({"route": "b2b", "persona": p, "label": "%s-%s" % (pj["code"], pkg.upper()), "month": m,
                     "ask": pj["ask"], "realised": realised, "op_h": pj["op_h"], "wife_h": pj["wife_h"]})

    # Free private samples (small size, the persona's own offer), no revenue. One a month, cycling 色環, 方寸, 步驟.
    for i in range(int(round(g("b2b.samples")))):
        m = min(T, max(1, int(round(g("b2b.sample_first_month"))) + i))
        sp_persona = SAMPLE_ORDER[i % len(SAMPLE_ORDER)]
        code = OFFER_FOR_PERSONA[sp_persona]
        pj = offer_price(A, scen, code, "s")
        add_hours(m, sp_persona, pj["op_h"], pj["wife_h"], pj["tools"])
        jobs.append({"route": "sample", "persona": sp_persona, "label": "%s-S sample (free, private)" % code, "month": m,
                     "ask": 0.0, "realised": 0.0, "op_h": pj["op_h"], "wife_h": pj["wife_h"]})

    # Sponsored posts
    sp_first = min(T, max(1, int(round(g("sp.first_month")))))
    sp_list = [p for p in PERSONAS for _ in range(int(round(g("sp.%s.deals" % p))))]
    tier = int(round(g("sp.tier")))
    spj = sp_price(A, scen, tier)
    for p, m in zip(sp_list, spread_months(sp_first, T, len(sp_list))):
        realised = (spj["ask"] + g("sp.reach_premium")) * g("sp.realisation")
        rev["sp"][p][m] += realised
        add_hours(m, p, spj["op_h"], spj["wife_h"], spj["tools"])
        jobs.append({"route": "sp", "persona": p, "label": "SP tier %d" % tier, "month": m,
                     "ask": spj["ask"] + g("sp.reach_premium"), "realised": realised,
                     "op_h": spj["op_h"], "wife_h": spj["wife_h"]})

    # Affiliate funnel
    aff = {}
    a_first = min(T, max(1, int(round(g("aff.first_month")))))
    ramp_n = max(1.0, g("aff.ramp_months"))
    for p in PERSONAS:
        steady = g("aff.impressions." + p) * g("aff.weight." + p)
        tot = {"impr": 0.0, "clicks": 0.0, "orders": 0.0, "gmv": 0.0, "commission": 0.0}
        for m in range(a_first, T + 1):
            ramp = min(1.0, (m - a_first + 1) / ramp_n)
            impr = steady * ramp
            clicks = impr * g("aff.click_rate")
            orders = clicks * g("aff.click_to_order")
            gmv = orders * g("aff.aov")
            comm = gmv * g("aff.commission")
            rev["aff"][p][m] += comm
            for k, v in (("impr", impr), ("clicks", clicks), ("orders", orders), ("gmv", gmv), ("commission", comm)):
                tot[k] += v
            add_hours(m, p, g("aff.admin_op_min_month") / 60.0 / len(PERSONAS), 0.0)
        aff[p] = tot

    # Own digital products
    units_sold = {p: 0.0 for p in PERSONAS}
    pr_first = min(T, max(1, int(round(g("prod.first_sale_month")))))
    made = [p for p in PERSONAS if g("prod.%s.made" % p) >= 0.5]
    for idx, p in enumerate(made):
        pj = product_price(A, scen, PRODUCT_FOR_PERSONA[p])
        units = g("prod.%s.units" % p)
        active = T - pr_first + 1
        for m in range(pr_first, T + 1):
            rev["prod"][p][m] += units / active * pj["price"]
        units_sold[p] = units
        # packs are made one per month, the last one in the month before the first sale
        add_hours(max(1, pr_first - 1 - (len(made) - 1 - idx)), p, pj["op_h"], pj["wife_h"], pj["tools"])

    # LINE stickers
    stk_first = min(T, max(1, int(round(g("stk.first_month")))))
    sc = sticker_set_cost(A, scen)
    sticker_sales = {p: 0.0 for p in PERSONAS}
    set_owners = [p for p in PERSONAS for _ in range(int(round(g("stk.%s.sets" % p))))]
    for idx, p in enumerate(set_owners):
        for m in range(stk_first, T + 1):
            sales = g("stk.sales_per_set_month")
            rev["stk"][p][m] += sales * sc["share"]
            sticker_sales[p] += sales
        # sets are made one per month, the last one in the month before the first sale
        add_hours(max(1, stk_first - 1 - (len(set_owners) - 1 - idx)), p, g("stk.set_op_h"), g("stk.set_wife_h"), sc["tools"])

    # Cash: lag each route; whatever lands after month T is a receivable
    cash = {r: {p: z() for p in PERSONAS} for r in ROUTES}
    recv_end = {r: {p: 0.0 for p in PERSONAS} for r in ROUTES}
    for r in ROUTES:
        lag = int(round(g(LAG_KEY[r])))
        for p in PERSONAS:
            for m, v in enumerate(rev[r][p]):
                if not v:
                    continue
                if m + lag <= T:
                    cash[r][p][m + lag] += v
                else:
                    recv_end[r][p] += v
    fee_rate = g("prod.fee_rate")
    fees = z()
    for m in range(T + 1):
        fees[m] = sum(cash["prod"][p][m] for p in PERSONAS) * fee_rate

    # Costs
    budget = g("tools.budget") if tools_budget is None else tools_budget
    tools = z()
    tools[0] = g("tools.m0")
    for m in range(1, T + 1):
        tools[m] = budget * (g("tools.early_fraction") if m <= int(round(g("tools.early_months"))) else 1.0)
    one_time = z()
    for key, _label in COST_ITEMS:
        mth = min(T, max(0, int(round(g("cost.%s.month" % key)))))
        one_time[mth] += g("cost." + key) * g("cost.scale")
    bookkeeping = z()
    for m in range(1, T + 1):
        bookkeeping[m] = g("cost.bookkeeper_monthly") * g("cost.scale")

    wife_cash = [h * g("rate.wife_hourly") if wife_paid else 0.0 for h in hours_wife]
    return {
        "scen": scen, "T": T, "rev": rev, "cash": cash, "recv_end": recv_end, "fees": fees, "wife_cash": wife_cash,
        "tools": tools, "one_time": one_time, "bookkeeping": bookkeeping,
        "hours_op": hours_op, "hours_wife": hours_wife, "memo_tools": memo_tools, "hp": hp,
        "jobs": jobs, "aff": aff, "units_sold": units_sold, "sticker_sales": sticker_sales,
    }


# ---- result helpers
def route_rev(res, route, persona=None):
    ps = PERSONAS if persona is None else (persona,)
    return sum(sum(res["rev"][route][p]) for p in ps)


def total_rev(res):
    return sum(route_rev(res, r) for r in ROUTES)


def receipts(res, m):
    return sum(res["cash"][r][p][m] for r in ROUTES for p in PERSONAS)


def total_receipts(res):
    return sum(receipts(res, m) for m in range(res["T"] + 1))


def total_receivable(res):
    return sum(res["recv_end"][r][p] for r in ROUTES for p in PERSONAS)


def net_series(res, include_placeholders):
    out = []
    for m in range(res["T"] + 1):
        v = receipts(res, m) - res["fees"][m] - res["tools"][m] - res["wife_cash"][m]
        if include_placeholders:
            v -= res["one_time"][m] + res["bookkeeping"][m]
        out.append(v)
    return out


def cumulative(series):
    out, c = [], 0.0
    for v in series:
        c += v
        out.append(c)
    return out


def total_tools(res):
    return sum(res["tools"])


def total_placeholders(res):
    return sum(res["one_time"]) + sum(res["bookkeeping"])


def first_cover_month(res, include_placeholders=False):
    """First model month in which receipts net of fees cover that month's tools (and placeholders) spend."""
    for m in range(1, res["T"] + 1):
        spend = res["tools"][m] + (res["bookkeeping"][m] if include_placeholders else 0.0)
        if receipts(res, m) - res["fees"][m] >= spend - EPS and receipts(res, m) > 0:
            return m
    return None


def first_rolling_cover_month(res, include_placeholders=False, window=3):
    """First month in which the last `window` months of receipts (net of fees) cover the last `window` months of spend.
    A single lumpy invoice does not count as break-even; this is the sustained test."""
    for m in range(window, res["T"] + 1):
        ms = range(m - window + 1, m + 1)
        got = sum(receipts(res, k) - res["fees"][k] for k in ms)
        spend = sum(res["tools"][k] + (res["bookkeeping"][k] if include_placeholders else 0.0) for k in ms)
        if got > 0 and got >= spend - EPS:
            return m
    return None


def first_cumulative_breakeven(res, include_placeholders):
    cum = cumulative(net_series(res, include_placeholders))
    for m in range(res["T"] + 1):
        if cum[m] >= -EPS and m >= 1 and receipts(res, m) > 0:
            return m
    return None


def capacity(res, A):
    scen, T = res["scen"], res["T"]
    cap_op = A.get("cap.op_hours_revenue_month", scen)
    cap_wife = A.get("cap.wife_hours_revenue_month", scen)
    ho, hw = res["hours_op"], res["hours_wife"]
    backlog, worst = 0.0, 0.0
    for m in range(1, T + 1):
        backlog = max(0.0, backlog + ho[m] - cap_op)
        worst = max(worst, backlog)
    tot_op, tot_wife = sum(ho), sum(hw)
    return {
        "cap_op": cap_op, "cap_wife": cap_wife, "total_op": tot_op, "total_wife": tot_wife,
        "avg_op": tot_op / T, "avg_wife": tot_wife / T,
        "peak_op": max(ho[1:]), "peak_wife": max(hw[1:]),
        "months_over_op": [m for m in range(1, T + 1) if ho[m] > cap_op + EPS],
        "backlog_op_h": worst,
        "avg_within_cap": tot_op / T <= cap_op + EPS and tot_wife / T <= cap_wife + EPS,
        "share_of_year": tot_op / (A.get("cap.op_hours_month_total", scen) * T),
        "memo_tools": sum(res["memo_tools"]),
        "blended_assumed_rate": (
            (tot_op * A.get("rate.op_hourly", scen) + tot_wife * A.get("rate.wife_hourly", scen)) / (tot_op + tot_wife)
            if (tot_op + tot_wife) > 0 else 0.0),
        "effective_hourly": total_rev(res) / (tot_op + tot_wife) if (tot_op + tot_wife) > 0 else 0.0,
    }


# ----------------------------------------------------------------------------------------------
# Phase 1 replay and reconciliation
# ----------------------------------------------------------------------------------------------
def phase1_replay(A, scen):
    g = lambda k: A.get("phase1." + k, scen)
    parts = {
        "b2b": g("b2b_jobs") * g("b2b_price") if g("b2b_jobs") > 0 else 0.0,
        "sp": g("sp_deals") * g("sp_price") if g("sp_deals") > 0 else 0.0,
        "aff": g("affiliate"), "stk": g("stickers"), "prod": g("products"),
        "licensing": g("licensing"), "payouts": g("payouts"),
    }
    total = sum(parts.values())
    return {"parts": parts, "total": total, "spend": g("spend_cap"), "delta": total - g("spend_cap")}


def nearest_package(A, scen, price):
    """The B-offer package whose proposed price is closest to `price`."""
    best = None
    for code in ("B1", "B2", "B3"):
        for pkg in ("s", "m"):
            pj = offer_price(A, scen, code, pkg)
            d = abs(pj["ask"] - price)
            if best is None or d < best[0]:
                best = (d, code, pkg, pj)
    return best[1], best[2], best[3]


def jobs_for_target(A, scen, target):
    """B2B jobs needed to reach `target` gross, given the other routes of this scenario. Mix = this scenario's jobs."""
    res = run(A, scen)
    other = total_rev(res) - route_rev(res, "b2b")
    b2b_jobs = [j for j in res["jobs"] if j["route"] == "b2b"]
    if not b2b_jobs:
        return None
    avg_real = sum(j["realised"] for j in b2b_jobs) / len(b2b_jobs)
    avg_op = sum(j["op_h"] for j in b2b_jobs) / len(b2b_jobs)
    need = max(0.0, target - other)
    n = need / avg_real
    return {"other": other, "need": need, "avg_realised": avg_real, "avg_op_h": avg_op, "jobs": n, "op_h": n * avg_op}


# ----------------------------------------------------------------------------------------------
# Sensitivity
# ----------------------------------------------------------------------------------------------
def _sens_cases():
    S = ("mid",)

    def jobs_mult(f):
        return lambda A: A.scale_prefix("b2b.", "_jobs", f, S)

    def setv(k, v):
        return lambda A: A.set(k, v, S)

    def scalev(k, f):
        return lambda A: A.scale(k, f, S)

    def imp(f):
        return lambda A: A.scale_prefix("aff.impressions.", "", f, S)

    def prod_units(f):
        return lambda A: A.scale_prefix("prod.", ".units", f, S)

    def addv(k, v):
        return lambda A: A.set(k, A.get(k, "mid") + v, S)

    def stickers_off(A):
        for p in PERSONAS:
            A.set("stk.%s.sets" % p, 0, S)

    def sp_deals(n):
        def f(A):
            A.set("sp.fangcun.deals", 0, S)
            A.set("sp.buzhou.deals", 0, S)
            A.set("sp.sehuan.deals", n, S)
        return f

    return [
        ("Base: middle scenario", lambda A: A, None),
        ("B2B realisation 0.6 (deeper discounts)", setv("b2b.realisation", 0.6), None),
        ("B2B realisation 1.0 (full proposed price)", setv("b2b.realisation", 1.0), None),
        ("B2B paid jobs: none (x0)", jobs_mult(0), None),
        ("B2B paid jobs: double (x2)", jobs_mult(2), None),
        ("B2B paid jobs: triple (x3)", jobs_mult(3), None),
        ("B2B jobs delivered earlier (M4 to M10)", lambda A: [A.set("b2b.first_paid_month", 4, S), A.set("b2b.last_month", 10, S)], None),
        ("B2B jobs all delivered in M12 (cash lands after the 12 months)", lambda A: [A.set("b2b.first_paid_month", 12, S), A.set("b2b.last_month", 12, S)], None),
        ("Every payment lag +2 months", lambda A: [A.set(k, A.get(k, "mid") + 2, S) for k in ("b2b.lag", "sp.lag", "aff.lag", "prod.lag", "stk.lag")], None),
        ("Operator hourly value NT$400 (prices fall)", setv("rate.op_hourly", 400), None),
        ("Operator hourly value NT$800 (prices rise)", setv("rate.op_hourly", 800), None),
        ("Margin 10%", setv("rate.margin", 0.10), None),
        ("Margin 40%", setv("rate.margin", 0.40), None),
        ("Sponsored posts: none", sp_deals(0), None),
        ("Sponsored posts: 3 on 色環", sp_deals(3), None),
        ("Reach component NT$2,000 per sponsored post (hypothetical axis)", addv("sp.reach_premium", 2000), None),
        ("Reach component NT$5,000 per sponsored post (hypothetical axis)", addv("sp.reach_premium", 5000), None),
        ("Impressions x0.5", imp(0.5), None),
        ("Impressions x2", imp(2), None),
        ("Impressions x5", imp(5), None),
        ("Affiliate commission 2% (Phase 1 axis)", setv("aff.commission", 0.02), None),
        ("Affiliate commission 8% (Phase 1 axis)", setv("aff.commission", 0.08), None),
        ("Link click rate halved", scalev("aff.click_rate", 0.5), None),
        ("Own product units x0 (nothing sells)", prod_units(0), None),
        ("Own product units x3", prod_units(3), None),
        ("Own product list prices 40% lower (payback units 67 instead of 40)", setv("prod.payback_units", 40.0 / 0.6), None),
        ("No LINE stickers", stickers_off, None),
        ("Sticker creator share NT$8 (Phase 1 axis)", setv("stk.creator_share", 8), None),
        ("Sticker creator share NT$16 (Phase 1 axis)", setv("stk.creator_share", 16), None),
        ("Tools budget NT$10,000 (headroom used)", lambda A: A, {"tools_budget": 10000.0}),
        ("Tools held at 60% of the cap (NT$3,000) all year", setv("tools.early_months", 12), None),
        ("Wife's review hours paid in cash at the assumed hourly value", lambda A: A, {"wife_paid": True}),
        ("Compliance placeholders x0 (all free)", setv("cost.scale", 0), None),
        ("Compliance placeholders x2", setv("cost.scale", 2), None),
    ]


def sensitivity(A):
    rows = []
    base = None
    for label, fn, kw in _sens_cases():
        B = A.copy()
        fn(B)
        res = run(B, "mid", **(kw or {}))
        rec = total_rev(res)
        n_tools = cumulative(net_series(res, False))[-1]
        n_all = cumulative(net_series(res, True))[-1]
        row = {"label": label, "rev": rec, "net_tools": n_tools, "net_all": n_all, "cash": total_receipts(res)}
        if base is None:
            base = row
        row["d_rev"] = rec - base["rev"]
        row["d_net_tools"] = n_tools - base["net_tools"]
        rows.append(row)
    return rows


# ----------------------------------------------------------------------------------------------
# Break-even
# ----------------------------------------------------------------------------------------------
def route_alone(A, scen="mid"):
    """What each route alone must do per month to cover the tools budget (NT$5,000 and NT$10,000)."""
    out = []
    r = lambda k: A.get(k, scen)
    for budget in (5000.0, 10000.0):
        for code, pkg in (("B1", "s"), ("B2", "s"), ("B3", "s"), ("B1", "m"), ("B3", "m")):
            pj = offer_price(A, scen, code, pkg)
            realised = pj["ask"] * r("b2b.realisation")
            jobs = budget / realised
            out.append({"budget": budget, "route": "B2B %s-%s" % (code, pkg.upper()), "per_month": jobs, "unit": "jobs a month",
                        "op_h": jobs * pj["op_h"], "price": realised})
        spj = sp_price(A, scen, int(r("sp.tier")))
        realised = (spj["ask"] + r("sp.reach_premium")) * r("sp.realisation")
        out.append({"budget": budget, "route": "Sponsored post (tier %d)" % int(r("sp.tier")), "per_month": budget / realised,
                    "unit": "posts a month", "op_h": budget / realised * spj["op_h"], "price": realised})
        gmv = budget / r("aff.commission")
        imp = gmv / (r("aff.click_rate") * r("aff.click_to_order") * r("aff.aov"))
        out.append({"budget": budget, "route": "Affiliate (this scenario's funnel)", "per_month": imp,
                    "unit": "impressions a month", "op_h": None, "price": gmv})
        gmv1 = budget / 0.05
        imp1 = gmv1 / (0.01 * 0.02 * 500)
        out.append({"budget": budget, "route": "Affiliate (Phase 1 axis: 1%, 2%, NT$500, 5%)", "per_month": imp1,
                    "unit": "impressions a month", "op_h": None, "price": gmv1})
        for pid in ("P1", "P3"):
            pj = product_price(A, scen, pid)
            u = budget / pj["net"]
            out.append({"budget": budget, "route": "Product %s at NT$%s list" % (pid, n0(pj["price"])), "per_month": u,
                        "unit": "sales a month", "op_h": None, "price": pj["net"]})
        sc = sticker_set_cost(A, scen)
        out.append({"budget": budget, "route": "LINE stickers at NT$%s per sale" % n0(sc["share"]), "per_month": budget / sc["share"],
                    "unit": "sales a month", "op_h": None, "price": sc["share"]})
    return out


# ----------------------------------------------------------------------------------------------
# Rendering (markdown blocks that are pasted into the two documents)
# ----------------------------------------------------------------------------------------------
def render_rate_params(A):
    s = "mid"
    rows = []
    for k, lab in (("rate.op_hourly", "Operator hourly value (NT$/h)"), ("rate.wife_hourly", "Wife hourly value (NT$/h)"),
                   ("rate.margin", "Margin on cost"), ("rate.round_to", "Asks rounded up to (NT$)"),
                   ("rate.cost_per_try", "Image-API cost of one try (NT$)"),
                   ("rate.revision_fraction", "Share of a set redone per revision round"),
                   ("rate.rounds_included", "Revision rounds included"),
                   ("rate.turnaround_hours_per_week", "Operator hours per week a client job can get"),
                   ("rate.turnaround_buffer_weeks", "Approval buffer (weeks)")):
        row = A.by_key[k]
        rows.append((lab, ("%g" % row[s]), row["status"], row["source"]))
    return md_table(["Parameter", "Value", "Status", "Source or logic"], rows, ["l", "r", "l", "l"])


def _deriv_rows(A, scen, pjs):
    r = lambda k: A.get("rate." + k, scen)
    rows = [
        ("Deliverable units", [n0(p["units"]) for p in pjs]),
        ("Unit-works incl. %d revision rounds at %s of a set" % (int(r("rounds_included")), pct(r("revision_fraction"))), ["%.1f" % p["work"] for p in pjs]),
        ("Operator hours", ["%.2f" % p["op_h"] for p in pjs]),
        ("Wife hours", ["%.2f" % p["wife_h"] for p in pjs]),
        ("Operator time at NT$%s/h (NT$)" % n0(r("op_hourly")), [n0(p["op_value"]) for p in pjs]),
        ("Wife time at NT$%s/h (NT$)" % n0(r("wife_hourly")), [n0(p["wife_value"]) for p in pjs]),
        ("Image-tool cost (NT$)", [n0(p["tools"]) for p in pjs]),
        ("Floor: walk-away cost, no margin (NT$)", [n0(p["floor"]) for p in pjs]),
        ("Plus margin %s (NT$, before rounding)" % pct(r("margin")), [n0(p["ask_raw"]) for p in pjs]),
        ("**Proposed price, rounded up (NT$)**", ["**%s**" % n0(p["ask"]) for p in pjs]),
        ("Quoted turnaround (weeks, from complete brief and assets)", [str(p["weeks"]) for p in pjs]),
    ]
    return rows


def render_offer(A, code):
    s = "mid"
    pkgs = (("s", "Small"), ("m", "Medium"))
    pjs = [offer_price(A, s, code, k) for k, _ in pkgs]
    heads = ["%s-%s" % (code, k.upper()) for k, _ in pkgs]
    labels = ["%s %s (%s)" % (h, lab, UNIT_NAME[code]) for h, (_, lab) in zip(heads, pkgs)]
    rows = [[lab] + vals for lab, vals in _deriv_rows(A, s, pjs)]
    return md_table(["Step"] + labels, rows, ["l", "r", "r"])


def render_sp(A):
    s = "mid"
    rows = []
    for t, boundary in ((0, "no audience yet (under 1,000 followers on the platform)"), (1, "1,000 to under 10,000"),
                        (2, "10,000 to under 100,000"), (3, "100,000 and above")):
        pj = sp_price(A, s, t)
        rows.append(("T%d" % t, boundary, n0(A.get("offer.SP.report_op_min.t%d" % t, s)), n0(pj["floor"]), n0(pj["ask"]),
                     "[TO FILL WHEN REAL]" if t > 0 else "none (no reach to price)", str(pj["weeks"])))
    return md_table(["Tier", "Followers on the platform (assumption; replace with agency definitions, G1)", "Report minutes",
                     "Floor (NT$)", "Production price, rounded up (NT$)", "Reach component", "Turnaround (weeks)"], rows,
                    ["l", "l", "r", "r", "r", "l", "r"])


def render_sp_derivation(A):
    pjs = [sp_price(A, "mid", t) for t in (0, 1, 2, 3)]
    rows = [[lab] + vals for lab, vals in _deriv_rows(A, "mid", pjs)]
    return md_table(["Step", "T0", "T1", "T2", "T3"], rows, ["l", "r", "r", "r", "r"])


def render_addons(A):
    s = "mid"
    r = lambda k: A.get("rate." + k, s)
    work_per_unit = 1.0 + r("rounds_included") * r("revision_fraction")
    rows = []
    fo, fw = r("round_fixed_op_min"), r("round_fixed_wife_min")
    for code in ("B1", "B2", "B3"):
        pj_s = offer_price(A, s, code, "s")
        pj_m = offer_price(A, s, code, "m")
        rnd_s = incremental_price(A, s, code, pj_s["units"] * r("revision_fraction"), fo, fw)
        rnd_m = incremental_price(A, s, code, pj_m["units"] * r("revision_fraction"), fo, fw)
        unit = incremental_price(A, s, code, work_per_unit)
        rows.append(("%s %s" % (code, OFFER_NAME[code]), n0(rnd_s["ask"]), n0(rnd_m["ask"]), n0(unit["ask"])))
    pm = paid_media_price(A, s)
    sp_round = incremental_price(A, s, "SP", A.get("offer.SP.units", s) * r("revision_fraction"), fo, fw)
    out = md_table(["Offer", "Extra revision round, small (NT$)", "Extra revision round, medium (NT$)", "Extra unit (NT$)"], rows,
                   ["l", "r", "r", "r"])
    out += "\n\n" + md_table(["Add-on", "Floor (NT$)", "Proposed price (NT$)", "Derivation"], [
        ("Paid-media (boost) handling on a delivered piece", n0(pm["floor"]), n0(pm["ask"]),
         "%d operator minutes + %d wife minutes of compliance handling at the assumed hourly values, plus margin; a rights-value premium is [TO FILL WHEN REAL]" % (r("paid_media_op_min"), r("paid_media_wife_min"))),
        ("Extra revision round on a sponsored post", n0(sp_round["floor"]), n0(sp_round["ask"]), "revision share of one master plus %d operator and %d wife minutes of handling" % (fo, fw)),
        ("Rush delivery", "not offered", "not offered", "operator hours are shared with the personas (ops/risk-register.md PPL-1)"),
        ("Exclusivity, perpetual buy-out, model-training rights", "not offered", "not offered", "red flags in the persona bibles 9.3; discuss only a narrow, time-limited category scope, no price"),
    ], ["l", "r", "r", "l"])
    return out


def render_products(A):
    s = "mid"
    rows = []
    for pid in ("P1", "P2", "P3"):
        pj = product_price(A, s, pid)
        rows.append((pid, PRODUCT_NAME[pid], "%g" % pj["op_h"], "%g" % pj["wife_h"], n0(pj["tools"]), n0(pj["cost"]),
                     n0(pj["price_raw"]), "**%s**" % n0(pj["price"]), n0(pj["net"]), "%.0f" % pj["units_to_repay"]))
    return md_table(["ID", "Product", "Operator h", "Wife h", "Tools (NT$)", "Cost (NT$)", "Price before rounding (NT$)",
                     "Proposed list price (NT$)", "Net of assumed fees (NT$)", "Sales to repay the hours at zero margin"], rows,
                    ["l", "l", "r", "r", "r", "r", "r", "r", "r", "r"])


def render_stickers(A):
    sc = sticker_set_cost(A, "mid")
    return md_table(["Item", "Value"], [
        ("Production cost of one set (hours at assumed values + image tries), NT$", n0(sc["cost"])),
        ("Studio share per sale, hypothetical axis value (NT$)", n0(sc["share"])),
        ("Sales needed to repay one set's hours at zero margin", n0(sc["sales_to_repay"])),
        ("Studio-set sale price", "none: LINE sets the price tiers (not found, G5)"),
    ], ["l", "r"])


def render_rate_summary(A):
    s = "mid"
    rows = []
    for code in ("B1", "B2", "B3"):
        for k in ("s", "m"):
            pj = offer_price(A, s, code, k)
            rows.append(("%s-%s" % (code, k.upper()), OFFER_NAME[code], "%d %s" % (pj["units"], UNIT_NAME[code]), "%.1f" % pj["op_h"],
                         "%.1f" % pj["wife_h"], n0(pj["floor"]), "**%s**" % n0(pj["ask"]), str(pj["weeks"])))
    for t in (0, 1):
        pj = sp_price(A, s, t)
        rows.append(("SP-T%d" % t, "Sponsored post (業配), tier %d, production price only" % t, "1 master + 1 variant", "%.1f" % pj["op_h"],
                     "%.1f" % pj["wife_h"], n0(pj["floor"]), "**%s**" % n0(pj["ask"]), str(pj["weeks"])))
    for pid in ("P1", "P2", "P3"):
        pj = product_price(A, s, pid)
        rows.append((pid, PRODUCT_NAME[pid], "1 pack", "%g" % pj["op_h"], "%g" % pj["wife_h"], n0(pj["cost"]), "**%s**" % n0(pj["price"]), "n/a"))
    return md_table(["ID", "Offer", "Scope", "Operator h", "Wife h", "Floor or cost (NT$)", "Proposed price (NT$)", "Turnaround (weeks)"], rows,
                    ["l", "l", "l", "r", "r", "r", "r", "r"])


# ---- model blocks
def all_runs(A):
    return {s: run(A, s) for s in SCENARIOS}


def render_summary(A):
    runs = all_runs(A)
    rows = []
    for s in SCENARIOS:
        res = runs[s]
        rows.append([SCEN_LABEL[s]] + [n0(route_rev(res, r)) for r in ROUTES] + ["0", "0", "**%s**" % n0(total_rev(res))])
    t1 = md_table(["Scenario", "B2B", "Sponsored", "Affiliate", "Products", "Stickers", "Licensing", "Platform payouts", "Total recognised"],
                  rows, ["l"] + ["r"] * 8)
    rows2 = []
    for s in SCENARIOS:
        res = runs[s]
        net_t = cumulative(net_series(res, False))[-1]
        net_a = cumulative(net_series(res, True))[-1]
        rows2.append((SCEN_LABEL[s], n0(total_receipts(res)), n0(total_receivable(res)), n0(sum(res["fees"])), n0(total_tools(res)),
                      n0(total_placeholders(res)), n0(net_t), n0(net_a)))
    t2 = md_table(["Scenario", "Cash received by M12", "Receivable at M12 (not yet paid)", "Marketplace fees", "Tools spend M0 to M12",
                   "Placeholder compliance costs", "Net cash, tools only", "Net cash incl. placeholders"], rows2, ["l"] + ["r"] * 7)
    return t1 + "\n\nAll amounts in NT$, gross and pre-tax. Net cash = cash received minus fees minus spend.\n\n" + t2


def render_headline(A):
    runs = all_runs(A)
    lines = []
    for s in SCENARIOS:
        res = runs[s]
        cap = capacity(res, A)
        net_t = cumulative(net_series(res, False))[-1]
        net_a = cumulative(net_series(res, True))[-1]
        lines.append("- **%s:** %s recognised in 12 months (%s received in cash by M12), against %s of tools spend; net cash %s on tools alone and %s with the placeholder compliance costs. Operator hours on revenue work: %.0f (%s of the operator's year)."
                     % (SCEN_LABEL[s], money(total_rev(res)), money(total_receipts(res)), money(total_tools(res)), money(net_t), money(net_a),
                        cap["total_op"], pct(cap["share_of_year"])))
    return "\n".join(lines)


def render_persona(A):
    out = []
    runs = all_runs(A)
    for s in SCENARIOS:
        res = runs[s]
        cap = capacity(res, A)
        share = total_tools(res) / len(PERSONAS)
        rows = []
        for p in PERSONAS:
            vals = [route_rev(res, r, p) for r in ROUTES]
            tot = sum(vals)
            rows.append([PERSONA_NAME[p]] + [n0(v) for v in vals] + [n0(tot), n0(share), n0(tot - share),
                                                                   "%.0f" % res["hp"][p]["op"], "%.0f" % res["hp"][p]["wife"]])
        out.append("**%s scenario**\n\n" % SCEN_LABEL[s] + md_table(
            ["Persona", "B2B (tagged)", "Sponsored", "Affiliate", "Products", "Stickers", "Total recognised", "Allocated tools (1/3, display only)",
             "Revenue minus allocated tools", "Operator h", "Wife h"], rows, ["l"] + ["r"] * 10))
    return "\n\n".join(out)


def render_hours(A):
    rows = []
    for s in SCENARIOS:
        res = run(A, s)
        c = capacity(res, A)
        rows.append((SCEN_LABEL[s], "%.0f" % c["total_op"], "%.1f" % c["avg_op"], "%.0f" % c["cap_op"], "%.1f" % c["peak_op"],
                     str(len(c["months_over_op"])), "%.1f" % c["backlog_op_h"], pct(c["share_of_year"]), "%.0f" % c["total_wife"],
                     "%.1f" % c["avg_wife"], "%.0f" % c["cap_wife"], "yes" if c["avg_within_cap"] else "NO",
                     n0(c["blended_assumed_rate"]), n0(c["effective_hourly"])))
    return md_table(["Scenario", "Operator h, 12 months", "Avg h/month", "Cap h/month", "Peak month h", "Months over cap",
                     "Worst backlog h", "Share of operator year", "Wife h, 12 months", "Wife avg h/month", "Wife cap h/month",
                     "Average within both caps", "Assumed blended value (NT$/h)", "Revenue per hour worked (NT$/h)"], rows,
                    ["l"] + ["r"] * 10 + ["l", "r", "r"])


def render_schedule(A, scen="mid"):
    res = run(A, scen)
    rows = []
    for j in sorted(res["jobs"], key=lambda j: (j["month"], j["label"])):
        rows.append(("M%d (%s)" % (j["month"], month_label(A, j["month"])), PERSONA_NAME[j["persona"]],
                     {"b2b": "B2B", "sp": "Sponsored", "sample": "Free sample"}[j["route"]], j["label"],
                     n0(j["ask"]), n0(j["realised"]), "%.1f" % j["op_h"], "%.1f" % j["wife_h"]))
    return md_table(["Month", "Persona (showroom)", "Route", "Package", "Proposed price (NT$)", "Realised (NT$)", "Operator h", "Wife h"],
                    rows, ["l", "l", "l", "l", "r", "r", "r", "r"])


def b2b_funnel(A, scen):
    res = run(A, scen)
    paid = len([j for j in res["jobs"] if j["route"] == "b2b"])
    samples = len([j for j in res["jobs"] if j["route"] == "sample"])
    contacts = A.get("b2b.outreach_contacts", scen)
    return {"contacts": contacts, "samples": samples, "paid": paid,
            "paid_per_contact": paid / contacts if contacts else 0.0,
            "paid_per_sample": paid / samples if samples else 0.0}


def render_b2b_funnel(A):
    rows = []
    for s in SCENARIOS:
        f = b2b_funnel(A, s)
        rows.append((SCEN_LABEL[s], n0(f["contacts"]), n0(f["samples"]), n0(f["paid"]), pct(f["paid_per_contact"]), "%.2f" % f["paid_per_sample"]))
    return md_table(["Scenario", "Brands or agencies approached", "Free samples", "Paid jobs", "Paid jobs per contact approached",
                     "Paid jobs per free sample"], rows, ["l"] + ["r"] * 5)


def render_scenario_inputs(A):
    """A compact view of what each scenario assumes (every value comes from assumptions.csv)."""
    def per(fn):
        return [fn(sc) for sc in SCENARIOS]

    g = lambda k, sc: A.get(k, sc)
    tot = lambda pat, sc: sum(g(pat % p, sc) for p in PERSONAS)
    rows = [
        ("B2B paid jobs: small + medium", per(lambda sc: "%d + %d" % (tot("b2b.%s.s_jobs", sc), tot("b2b.%s.m_jobs", sc)))),
        ("B2B free private samples", per(lambda sc: "%d" % g("b2b.samples", sc))),
        ("B2B brands or agencies approached", per(lambda sc: "%d" % g("b2b.outreach_contacts", sc))),
        ("B2B first paid month (M#)", per(lambda sc: "M%d" % g("b2b.first_paid_month", sc))),
        ("B2B share of the proposed price realised", per(lambda sc: pct(g("b2b.realisation", sc)))),
        ("Sponsored posts (業配) in total", per(lambda sc: "%d" % tot("sp.%s.deals", sc))),
        ("Sponsored post audience tier / first month", per(lambda sc: "T%d / M%d" % (g("sp.tier", sc), g("sp.first_month", sc)))),
        ("Sponsored share of the proposed price realised", per(lambda sc: pct(g("sp.realisation", sc)))),
        ("Affiliate: steady monthly impressions per persona", per(lambda sc: n0(g("aff.impressions.fangcun", sc)))),
        ("Affiliate: link click rate / click-to-order", per(lambda sc: "%s / %s" % (pct(g("aff.click_rate", sc), 1), pct(g("aff.click_to_order", sc), 1)))),
        ("Affiliate: average order / commission", per(lambda sc: "NT$%s / %s" % (n0(g("aff.aov", sc)), pct(g("aff.commission", sc))))),
        ("Own products made / units sold in 12 months", per(lambda sc: "%d / %d" % (sum(1 for p in PERSONAS if g("prod.%s.made" % p, sc) >= 0.5),
                                                                                  sum(g("prod.%s.units" % p, sc) for p in PERSONAS)))),
        ("Own products first sale month", per(lambda sc: "M%d" % g("prod.first_sale_month", sc))),
        ("LINE sticker sets / sales per set per month", per(lambda sc: "%d / %d" % (tot("stk.%s.sets", sc), g("stk.sales_per_set_month", sc)))),
        ("LINE sticker first sales month / studio share per sale", per(lambda sc: "M%d / NT$%d" % (g("stk.first_month", sc), g("stk.creator_share", sc)))),
        ("Hours a month available for revenue work: operator / wife", per(lambda sc: "%g / %g" % (g("cap.op_hours_revenue_month", sc), g("cap.wife_hours_revenue_month", sc)))),
        ("Months from work to cash: B2B / sponsored / affiliate / products / stickers",
         per(lambda sc: " / ".join("%d" % g(LAG_KEY[r], sc) for r in ROUTES))),
        ("Platform payouts and licensing", ["NT$0 (excluded)"] * 3),
    ]
    return md_table(["Input (from assumptions.csv)", "Low", "Middle", "High"], [[lab] + vals for lab, vals in rows], ["l", "r", "r", "r"])


def render_status_counts(A):
    meaning = {
        "sourced": "taken from a project file with its own confidence label",
        "computed": "arithmetic on sourced values",
        "assumption": "the studio's own planning figure, logic stated, not market data",
        "hypothetical": "equals a Phase 1 hypothetical axis value, not market data",
        "placeholder": "no source exists; a stand-in to be replaced with a real quote [TO FILL WHEN REAL]",
        "excluded": "fixed at zero by rule",
    }
    rows = []
    for st in VALID_STATUS:
        keys = [r["key"] for r in A.rows if r["status"] == st]
        rows.append((st, str(len(keys)), meaning[st]))
    rows.append(("**all**", "**%d**" % len(A.rows), ""))
    return md_table(["Status", "Rows in assumptions.csv", "Meaning"], rows, ["l", "r", "l"])


def render_funnel(A):
    rows = []
    for s in SCENARIOS:
        res = run(A, s)
        impr = sum(res["aff"][p]["impr"] for p in PERSONAS)
        cl = sum(res["aff"][p]["clicks"] for p in PERSONAS)
        od = sum(res["aff"][p]["orders"] for p in PERSONAS)
        gmv = sum(res["aff"][p]["gmv"] for p in PERSONAS)
        cm = sum(res["aff"][p]["commission"] for p in PERSONAS)
        rows.append((SCEN_LABEL[s], n0(impr), n0(cl), n0(od), n0(gmv), n0(cm),
                     "%.0f" % sum(res["units_sold"].values()), "%.0f" % sum(res["sticker_sales"].values())))
    return md_table(["Scenario", "Impressions (12 m)", "Link clicks", "Orders", "GMV (NT$)", "Commission (NT$)", "Product units", "Sticker sales"],
                    rows, ["l"] + ["r"] * 7)


def render_cash(A, scen):
    res = run(A, scen)
    net_t = net_series(res, False)
    net_a = net_series(res, True)
    cum_t, cum_a = cumulative(net_t), cumulative(net_a)
    rows = []
    for m in range(res["T"] + 1):
        rec = [sum(res["cash"][r][p][m] for p in PERSONAS) for r in ROUTES]
        rows.append(["M%d %s" % (m, month_label(A, m))] + [n0(v) for v in rec] + [
            n0(res["fees"][m]), n0(res["tools"][m]), n0(res["one_time"][m] + res["bookkeeping"][m]),
            n0(net_t[m]), n0(cum_t[m]), n0(net_a[m]), n0(cum_a[m])])
    tot = ["Total"] + [n0(sum(res["cash"][r][p][m] for p in PERSONAS for m in range(res["T"] + 1))) for r in ROUTES] + [
        n0(sum(res["fees"])), n0(total_tools(res)), n0(total_placeholders(res)), n0(sum(net_t)), n0(cum_t[-1]), n0(sum(net_a)), n0(cum_a[-1])]
    rows.append(["**%s**" % c for c in tot])
    heads = ["Month", "B2B", "Sponsored", "Affiliate", "Products", "Stickers", "Fees", "Tools", "Placeholder costs", "Net (tools only)",
             "Cumulative (tools only)", "Net incl. placeholders", "Cumulative incl. placeholders"]
    return md_table(heads, rows, ["l"] + ["r"] * 12)


def render_cash_compact(A, scen):
    res = run(A, scen)
    cum_t = cumulative(net_series(res, False))
    cum_a = cumulative(net_series(res, True))
    rows = []
    for m in range(res["T"] + 1):
        rows.append(("M%d %s" % (m, month_label(A, m)), n0(receipts(res, m)), n0(res["tools"][m]), n0(res["one_time"][m] + res["bookkeeping"][m]),
                     n0(cum_t[m]), n0(cum_a[m])))
    return md_table(["Month", "Cash received", "Tools", "Placeholder costs", "Cumulative (tools only)", "Cumulative incl. placeholders"], rows,
                    ["l"] + ["r"] * 5)


def render_variants(A):
    rows = []
    for s in SCENARIOS:
        for label, kw in (("NT$5,000 cap (base)", {}), ("NT$10,000 headroom", {"tools_budget": 10000.0})):
            res = run(A, s, **kw)
            spend = total_tools(res)
            rec = total_receipts(res) - sum(res["fees"])
            rows.append((SCEN_LABEL[s], label, n0(spend), n0(rec), pct(rec / spend if spend else 0.0),
                         n0(cumulative(net_series(res, False))[-1]), n0(cumulative(net_series(res, True))[-1])))
    return md_table(["Scenario", "Tools budget", "Tools spend M0 to M12 (NT$)", "Cash received net of fees (NT$)",
                     "Share of tools spend covered", "Net cash, tools only", "Net cash incl. placeholders"], rows, ["l", "l", "r", "r", "r", "r", "r"])


def render_breakeven(A):
    rows = []
    for s in SCENARIOS:
        res = run(A, s)
        f = lambda m: "never within 12 months" if m is None else "M%d (%s)" % (m, month_label(A, m))
        rows.append((SCEN_LABEL[s], f(first_cover_month(res, False)), f(first_rolling_cover_month(res, False)),
                     f(first_rolling_cover_month(res, True)),
                     f(first_cumulative_breakeven(res, False)), f(first_cumulative_breakeven(res, True))))
    t1 = md_table(["Scenario", "First single month in which receipts cover that month's tools spend (lumpy)",
                   "First month the trailing 3 months of receipts cover the trailing 3 months of tools spend (sustained)",
                   "... and also the bookkeeping placeholder",
                   "Cumulative cash reaches zero (tools only)", "Cumulative cash reaches zero (incl. placeholders)"], rows,
                  ["l", "l", "l", "l", "l", "l"])
    alone = route_alone(A, "mid")
    rows2 = []
    for a in alone:
        if a["unit"] == "impressions a month":
            per = n0(a["per_month"])
        elif a["unit"] == "jobs a month" or a["unit"] == "posts a month":
            per = "%.2f" % a["per_month"]
        else:
            per = "%.0f" % a["per_month"]
        hrs = "" if a["op_h"] is None else "%.1f" % a["op_h"]
        share = "" if a["op_h"] is None else pct(a["op_h"] / A.get("cap.op_hours_month_total", "mid"))
        rows2.append((n0(a["budget"]), a["route"], per, a["unit"], hrs, share))
    t2 = md_table(["Monthly tools budget (NT$)", "Route alone (middle-scenario inputs)", "Needed", "Unit", "Operator h a month", "Share of the operator's 26 h"],
                  rows2, ["r", "l", "r", "l", "r", "r"])
    return t1 + "\n\n" + t2


def render_sens(A):
    rows = []
    for r in sensitivity(A):
        rows.append((r["label"], n0(r["rev"]), ("+" if r["d_rev"] > 0 else "") + n0(r["d_rev"]) if r["label"] != "Base: middle scenario" else "-",
                     n0(r["net_tools"]), ("+" if r["d_net_tools"] > 0 else "") + n0(r["d_net_tools"]) if r["label"] != "Base: middle scenario" else "-",
                     n0(r["net_all"])))
    return md_table(["Case (one change at a time from the middle scenario)", "Recognised revenue (NT$)", "Change", "Net cash, tools only (NT$)",
                     "Change", "Net cash incl. placeholders (NT$)"], rows, ["l", "r", "r", "r", "r", "r"])


def render_reconcile(A):
    rows = []
    for s in SCENARIOS:
        p1 = phase1_replay(A, s)
        res = run(A, s)
        rows.append((SCEN_LABEL[s], n0(p1["total"]), n0(total_rev(res)), n0(total_rev(res) - p1["total"]),
                     n0(p1["delta"]), n0(cumulative(net_series(res, False))[-1])))
    t1 = md_table(["Scenario", "Phase 1 total (replayed, NT$)", "This model, recognised (NT$)", "Difference (NT$)",
                   "Phase 1 vs NT$60,000 spend (NT$)", "This model: net cash, tools only (NT$)"], rows, ["l"] + ["r"] * 5)
    rows2 = []
    for s in SCENARIOS:
        p1 = phase1_replay(A, s)["parts"]
        res = run(A, s)
        for key, label in (("b2b", "B2B creative"), ("sp", "Sponsored posts"), ("aff", "Affiliate"), ("prod", "Own products"), ("stk", "Stickers")):
            rows2.append((SCEN_LABEL[s], label, n0(p1[key]), n0(route_rev(res, key)), n0(route_rev(res, key) - p1[key])))
    t2 = md_table(["Scenario", "Route", "Phase 1 cell (NT$)", "This model (NT$)", "Difference (NT$)"], rows2, ["l", "l", "r", "r", "r"])
    rows3 = []
    for s in ("mid", "high"):
        p1 = A.get("phase1.b2b_price", s)
        n_jobs = A.get("phase1.b2b_jobs", s)
        code, pkg, pj = nearest_package(A, s, p1)
        rows3.append((SCEN_LABEL[s], "%g jobs at NT$%s" % (n_jobs, n0(p1)), "%s-%s (proposed NT$%s)" % (code, pkg.upper(), n0(pj["ask"])),
                      "%.0f" % (n_jobs * pj["op_h"]), pct(n_jobs * pj["op_h"] / (A.get("cap.op_hours_month_total", s) * 12)),
                      "%.0f" % (n_jobs * pj["wife_h"])))
    t3 = md_table(["Phase 1 scenario", "Phase 1 B2B cell", "Nearest package by proposed price", "Operator hours implied", "Share of operator's 312 h",
                   "Wife hours implied"], rows3, ["l", "l", "l", "r", "r", "r"])
    tgt = jobs_for_target(A, "high", 200000.0)
    if tgt:
        t4 = ("To reach NT$200,000 recognised with the high scenario's other routes (%s) the B2B line must supply %s. At the high scenario's "
              "average realised job of %s that is about %.1f jobs and %.0f operator hours (%s of the operator's year), against %d jobs in the high scenario."
              % (money(tgt["other"]), money(tgt["need"]), money(tgt["avg_realised"]), tgt["jobs"], tgt["op_h"],
                 pct(tgt["op_h"] / (A.get("cap.op_hours_month_total", "high") * 12)),
                 len([j for j in run(A, "high")["jobs"] if j["route"] == "b2b"])))
    else:
        t4 = ""
    return t1 + "\n\n" + t2 + "\n\n" + t3 + "\n\n" + t4


def render_assumptions(A):
    groups = [
        ("A. Horizon and capacity", ("model.", "cap.")),
        ("B. Rate-card formula", ("rate.",)),
        ("C. Offer parameters", ("offer.",)),
        ("D. Own digital products (formula)", ("prod.P", "prod.tries", "prod.payback", "prod.fee", "prod.round")),
        ("E. Scenario inputs", ("b2b.", "sp.", "aff.", "prod.fangcun", "prod.buzhou", "prod.sehuan", "prod.first", "prod.lag", "stk.", "excl.")),
        ("F. Costs", ("tools.", "cost.")),
        ("G. Phase 1 hypothesis replayed", ("phase1.",)),
    ]
    out = []
    used = set()
    for title, prefixes in groups:
        rows = []
        for row in A.rows:
            k = row["key"]
            if k in used or not k.startswith(prefixes):
                continue
            used.add(k)
            fmt = lambda v: ("%g" % v)
            rows.append(("`%s`" % k, row["unit"], fmt(row["low"]), fmt(row["mid"]), fmt(row["high"]), row["status"],
                         (row["source"] + ". " + row["note"]).replace("|", "/").strip()))
        out.append("**%s**\n\n" % title + md_table(["Key", "Unit", "Low", "Mid", "High", "Status", "Source or logic"], rows,
                                                  ["l", "l", "r", "r", "r", "l", "l"]))
    missing = [r["key"] for r in A.rows if r["key"] not in used]
    if missing:
        raise ValueError("assumption keys not rendered: %s" % missing)
    return "\n\n".join(out)


def blocks(A):
    b = {
        "rate-params": render_rate_params(A),
        "rate-summary": render_rate_summary(A),
        "rate-B1": render_offer(A, "B1"),
        "rate-B2": render_offer(A, "B2"),
        "rate-B3": render_offer(A, "B3"),
        "rate-SP": render_sp(A),
        "rate-SP-derivation": render_sp_derivation(A),
        "rate-addons": render_addons(A),
        "rate-products": render_products(A),
        "rate-stickers": render_stickers(A),
        "model-headline": render_headline(A),
        "model-summary": render_summary(A),
        "model-persona": render_persona(A),
        "model-hours": render_hours(A),
        "model-status-counts": render_status_counts(A),
        "model-inputs": render_scenario_inputs(A),
        "model-funnel": render_funnel(A),
        "model-b2b-funnel": render_b2b_funnel(A),
        "model-schedule-mid": render_schedule(A, "mid"),
        "model-schedule-high": render_schedule(A, "high"),
        "model-cash-mid": render_cash(A, "mid"),
        "model-cash-low": render_cash_compact(A, "low"),
        "model-cash-high": render_cash_compact(A, "high"),
        "model-variants": render_variants(A),
        "model-breakeven": render_breakeven(A),
        "model-sens": render_sens(A),
        "model-reconcile": render_reconcile(A),
        "model-assumptions": render_assumptions(A),
    }
    return b


# ----------------------------------------------------------------------------------------------
# Document sync
# ----------------------------------------------------------------------------------------------
def _block_re(name):
    return re.compile(re.escape(GEN_BEGIN.format(name)) + r"\n(.*?)\n" + re.escape(GEN_END.format(name)), re.S)


def sync_text(text, bl):
    """Replace every generated block found in text. Returns (new_text, names_found)."""
    found = []
    for name, body in bl.items():
        rx = _block_re(name)
        if rx.search(text):
            found.append(name)
            text = rx.sub(lambda m: GEN_BEGIN.format(name) + "\n" + body + "\n" + GEN_END.format(name), text)
    return text, found


def unknown_blocks(text, bl):
    names = set(re.findall(r"<!-- BEGIN GENERATED:([A-Za-z0-9\-]+) -->", text))
    return sorted(names - set(bl))


def docs(write):
    A = Assumptions.load()
    bl = blocks(A)
    stale = []
    for path in (RATE_CARD_MD, REVENUE_MD):
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8") as fh:
            old = fh.read()
        bad = unknown_blocks(old, bl)
        if bad:
            raise SystemExit("unknown generated block(s) in %s: %s" % (path, bad))
        new, _found = sync_text(old, bl)
        if new != old:
            stale.append(os.path.basename(path))
            if write:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(new)
    return stale


def monthly_csv_text(A):
    lines = []
    head = ["scenario", "month_index", "month", "b2b_cash", "sponsored_cash", "affiliate_cash", "products_cash", "stickers_cash", "fees", "tools",
            "one_time_and_bookkeeping_placeholders", "net_tools_only", "cumulative_tools_only", "net_incl_placeholders", "cumulative_incl_placeholders",
            "operator_hours", "wife_hours"]
    lines.append(",".join(head))
    for s in SCENARIOS:
        res = run(A, s)
        nt, na = net_series(res, False), net_series(res, True)
        ct, ca = cumulative(nt), cumulative(na)
        for m in range(res["T"] + 1):
            rec = [sum(res["cash"][r][p][m] for p in PERSONAS) for r in ROUTES]
            vals = [s, str(m), month_label(A, m)] + ["%.2f" % v for v in rec] + [
                "%.2f" % res["fees"][m], "%.2f" % res["tools"][m], "%.2f" % (res["one_time"][m] + res["bookkeeping"][m]),
                "%.2f" % nt[m], "%.2f" % ct[m], "%.2f" % na[m], "%.2f" % ca[m], "%.2f" % res["hours_op"][m], "%.2f" % res["hours_wife"][m]]
            lines.append(",".join(vals))
    return "\n".join(lines) + "\n"


# ----------------------------------------------------------------------------------------------
# Command line
# ----------------------------------------------------------------------------------------------
def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    A = Assumptions.load()
    cmd = argv[0] if argv else "summary"
    if cmd == "summary":
        print(render_headline(A))
        print()
        print(render_summary(A))
    elif cmd == "rates":
        print(render_rate_summary(A))
        for c in ("B1", "B2", "B3"):
            print("\n" + c + "\n" + render_offer(A, c))
        print("\nSP\n" + render_sp(A))
        print("\nAdd-ons\n" + render_addons(A))
        print("\nProducts\n" + render_products(A))
        print("\nStickers\n" + render_stickers(A))
    elif cmd == "cash":
        scen = argv[1] if len(argv) > 1 else "mid"
        print(render_cash(A, scen))
    elif cmd == "breakeven":
        print(render_breakeven(A))
    elif cmd == "sens":
        print(render_sens(A))
    elif cmd == "reconcile":
        print(render_reconcile(A))
    elif cmd == "docs":
        write = "--write" in argv
        stale = docs(write)
        if stale and not write:
            print("stale generated tables in: " + ", ".join(stale) + "  (run: python3 model.py docs --write)")
            return 1
        print("generated tables refreshed in: " + ", ".join(stale) if (stale and write) else "generated tables are in sync")
    elif cmd == "csv":
        with open(MONTHLY_CSV, "w", encoding="utf-8", newline="") as fh:
            fh.write(monthly_csv_text(A))
        print("wrote " + MONTHLY_CSV)
    else:
        print(__doc__)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
