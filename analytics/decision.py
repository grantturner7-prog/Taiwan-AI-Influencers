"""decision.py - the scale / keep / retire decision tree (strategy/portfolio.md section 6.3) as a pure function.

`decide(facts)` takes a plain dict (no database) so it can be unit-tested and so the dashboard and weekly
report cannot disagree. It runs once per ACCOUNT (persona x platform), because the thresholds are per platform
and platforms are not compared with each other (6.1). The persona-level inputs (effort, rejection, lead
signals, link clicks) are the same for every account of a persona.

facts keys
  persona, platform          str
  data_state                 'not_started' | 'in_progress' | 'extend' | 'hold' | 'scored'
  provisional                bool   scored before the week-6 review date (a reading, not the review)
  n_scored, min_sample       int    organic posts with a computable ER in the window, and the minimum (8)
  window_label               str    for example 'weeks 3 to 6'
  er                         float | None   median ER over the window (0.006 = 0.6%)
  sv_share                   float | None   (saves+shares)/(counted interactions); None = platform reports no saves
  reach_trend                'rising' | 'flat' | 'falling2' | 'falling3' | 'unknown'
  gates_open                 list[str]      open standing events for this account (6.2)
  retire_triggers            list[str]      standing rules that retire (second rule-6 event in 8 weeks, strike open > 14 days)
  events_in_window           int            standing events (open or cleared) inside the window
  effort                     dict  metric -> {'value': float|None, 'n': int, 'scored': bool}
  rejection                  dict | None    same shape, metric rejection_rate
  redesign_done              bool           an experiment of kind 'redesign' is done ("after one redesign")
  fix_retest_done            bool           a Fix experiment (hook/format/platform) is done and this IS its re-test window
  lead_signals               int            positive lead signals for the persona (enquiry, free sample, quote, budget reply)
  link_weeks                 int            weeks (of the first 6) with tracked link clicks
  watch                      list[str]      extra flags from the thresholds table (followers); advisory only

Returns dict: status, provisional, steps, reasons, caveats, watch, levels, scale_checks, need_redesign.

Reading choices where portfolio.md is silent (also README section 8):
  * The tree is applied per account. A persona's headline is its best non-paused account.
  * ER at or above 2.0% that fails any Scale condition falls to the Keep test (step 6), not to Fix.
  * Scale also requires a rising reach trend, because the 6.1 table lists it in the Scale column.
  * Effort / rejection data that has not been logged is 'unknown': it does not block Keep (flagged as provisional)
    but it does block Scale.
  * The table's other retire-review triggers (reach falling 3 weeks with ER under 0.6%, audience share under 40%)
    are shown as WATCH flags; the status follows the tree.
"""
from __future__ import annotations

import thresholds as T

EFFORT_METRICS = ("operator_min_per_approval", "n7_min_per_master", "wife_min_per_master")
GOOD_FOR_KEEP = ("scale", "keep", "unknown")


def _pct(x):
    return "n/a" if x is None else f"{x * 100:.2f}%"


class _Out:
    def __init__(self, f):
        self.f = f
        self.steps, self.reasons, self.caveats = [], [], []
        self.watch = list(f.get("watch") or [])
        self.levels, self.scale_checks = {}, {}
        self.need_redesign = False

    def step(self, n, question, answer, detail=""):
        self.steps.append({"n": n, "question": question, "answer": answer, "detail": detail})

    def done(self, status, reason=None):
        if reason:
            self.reasons.insert(0, reason)
        return {
            "status": status,
            "provisional": bool(self.f.get("provisional")) and status in ("SCALE_ELIGIBLE", "KEEP", "FIX", "RETIRE_REVIEW"),
            "steps": self.steps,
            "reasons": self.reasons,
            "caveats": self.caveats,
            "watch": self.watch,
            "levels": self.levels,
            "scale_checks": self.scale_checks,
            "need_redesign": self.need_redesign,
        }


def decide(f: dict) -> dict:
    o = _Out(f)

    # ---- Step 1: account-standing gates -------------------------------------------------
    q1 = "1. Any account-standing gate open (6.2)?"
    if f.get("retire_triggers"):
        o.step(1, q1, "YES, retire trigger", "; ".join(f["retire_triggers"]))
        o.reasons.extend(f["retire_triggers"])
        return o.done("RETIRE", "A standing rule that retires is met; the owner decides and records it.")
    if f.get("gates_open"):
        o.step(1, q1, "YES", "; ".join(f["gates_open"]))
        o.reasons.extend(f["gates_open"])
        return o.done("PAUSE", "Pause this account until the gate is fixed, cleared and the root cause is written.")
    o.step(1, q1, "no", "")

    state = f.get("data_state")
    n, need = f.get("n_scored", 0), f.get("min_sample", T.MIN_ORGANIC_POSTS)
    q2 = f"2. Enough data ({need} organic posts per platform)?"
    if state == "not_started":
        o.step(2, q2, "no", "No published organic post yet.")
        return o.done("NOT_STARTED", "No published post yet, so nothing to score.")
    if state == "in_progress":
        o.step(2, q2, "not yet", f"{n} of {need} organic posts so far in {f.get('window_label')}; the persona is still before its week-6 review date or inside warm-up.")
        return o.done("IN_PROGRESS", f"{n} of {need} organic posts counted so far. No reading is given below the minimum sample.")
    if state == "extend":
        ext = f.get("n_extended")
        more = f" ({ext} so far counting weeks 7 and 8)" if ext is not None and ext != n else ""
        o.step(2, q2, "no, extend", f"{n} of {need} in weeks 3 to 6{more}; keep posting and re-run when week 8 ends (6.3 step 2).")
        return o.done("EXTEND", f"Only {n} of {need} organic posts in weeks 3 to 6{more}: extend the window to week 8, then re-run.")
    if state == "hold":
        o.step(2, q2, "no, hold", f"{n} of {need} even after extending to week 8.")
        return o.done("HOLD", f"Still only {n} of {need} organic posts after week 8: hold, no scoring (6.3 step 2).")
    o.step(2, q2, "yes", f"{n} organic posts with ER in {f.get('window_label')}" + (" (provisional reading)" if f.get("provisional") else ""))

    # ---- Levels for effort / rejection ---------------------------------------------------
    eff = f.get("effort") or {}
    for m in EFFORT_METRICS:
        e = eff.get(m)
        if e is None:
            continue
        o.levels[m] = T.effort_level(m, e["value"]) if e.get("scored") else "unknown"
    rej = f.get("rejection")
    o.levels["rejection_rate"] = T.effort_level("rejection_rate", rej["value"]) if rej and rej.get("scored") else "unknown"
    for m, lv in o.levels.items():
        if lv == "unknown":
            o.caveats.append(f"{T.EFFORT_LABELS[m]}: not logged or too few units to score; Keep is provisional on this point.")

    reach_trend = f.get("reach_trend", "unknown")
    er = f.get("er")
    if reach_trend == "unknown":
        o.caveats.append("Reach trend: fewer than 3 weeks of reach data, so it cannot be assessed.")
    if reach_trend == "falling3" and er is not None and er < T.ER_KEEP:
        o.watch.append("Table 6.1 retire-review trigger: reach falling 3 weeks in a row with ER under 0.6%. The tree (6.3) sets the status; you decide whether to act on this.")

    # ---- Step 3: effort breach -----------------------------------------------------------
    q3 = "3. Effort breach (operator over 15 min, N7 over 40, wife over 20, rejection over 30%) after one redesign?"
    breaches = [m for m, lv in o.levels.items() if lv == "retire"]
    if breaches and f.get("redesign_done"):
        names = "; ".join(T.EFFORT_LABELS[m] for m in breaches)
        o.step(3, q3, "YES", names)
        return o.done("RETIRE_REVIEW", f"Capacity breach after one redesign: {names}.")
    if breaches:
        o.need_redesign = True
        names = "; ".join(T.EFFORT_LABELS[m] for m in breaches)
        o.step(3, q3, "over the line, no redesign recorded", names + ". Run the one redesign first, log it as an experiment of kind redesign.")
        o.reasons.append(f"Over the retire line, but no completed redesign is logged: {names}.")
    else:
        o.step(3, q3, "no", "")

    # ---- Step 4: ER under 0.3% ----------------------------------------------------------
    q4 = "4. ER under 0.3%?"
    if er is None:
        o.step(4, q4, "cannot tell", "No ER could be computed.")
        return o.done("HOLD", "ER could not be computed; check that reach or views and shares/comments are imported.")
    if er < T.ER_FIX:
        o.step(4, q4, "YES", f"median ER {_pct(er)}")
        return o.done("RETIRE_REVIEW", f"Median ER {_pct(er)} is under {_pct(T.ER_FIX)}: pause, keep the assets for stickers and products.")
    o.step(4, q4, "no", f"median ER {_pct(er)}")

    # ---- Step 5: ER 0.3 to under 0.6 -> Fix ----------------------------------------------
    q5 = "5. ER 0.3% to under 0.6%, or Keep conditions partly unmet?"
    if er < T.ER_KEEP:
        if f.get("fix_retest_done"):
            o.step(5, q5, "YES, after a Fix re-test", f"median ER {_pct(er)}")
            return o.done("RETIRE_REVIEW", f"Still under {_pct(T.ER_KEEP)} after the Fix re-test (median ER {_pct(er)}).")
        o.step(5, q5, "YES", f"median ER {_pct(er)}")
        return o.done("FIX", f"Median ER {_pct(er)} is in the Fix band ({_pct(T.ER_FIX)} to under {_pct(T.ER_KEEP)}): change ONE variable (format, hook or platform) for 4 weeks, then re-test.")

    effort_ok = all(o.levels.get(m, "unknown") in GOOD_FOR_KEEP for m in EFFORT_METRICS if m in o.levels)
    rej_ok = o.levels["rejection_rate"] in GOOD_FOR_KEEP
    reach_ok = reach_trend not in ("falling2", "falling3")

    if f.get("fix_retest_done"):
        if effort_ok:
            o.step(5, q5, "no (this is the Fix re-test)", f"median ER {_pct(er)}, effort within Keep")
            return o.done("KEEP", f"After the Fix re-test: ER {_pct(er)} is at or above {_pct(T.ER_KEEP)} and effort is within Keep.")
        o.step(5, q5, "YES (Fix re-test, effort not within Keep)", "")
        return o.done("RETIRE_REVIEW", "After the Fix re-test the effort rows are still outside Keep.")

    # ---- Step 7 before 6 for ER >= 2.0% ---------------------------------------------------
    sv = f.get("sv_share")
    checks = {}
    if er >= T.ER_SCALE:
        checks["ER 2.0% or more"] = True
        checks["Saves + shares at least one third of interactions"] = None if sv is None else sv >= T.SAVES_SHARES_SCALE_SHARE
        checks["Reach trend rising"] = None if reach_trend == "unknown" else reach_trend == "rising"
        scale_effort = [o.levels[m] for m in EFFORT_METRICS if m in o.levels]
        checks["Effort within Scale"] = None if any(x == "unknown" for x in scale_effort) else all(x == "scale" for x in scale_effort)
        checks["Rejection rate within Scale"] = None if o.levels["rejection_rate"] == "unknown" else o.levels["rejection_rate"] == "scale"
        checks["Zero standing events in the window"] = f.get("events_in_window", 0) == 0
        checks["Lead signal, or link clicks in 3 of 6 weeks"] = (f.get("lead_signals", 0) > 0) or (f.get("link_weeks", 0) >= T.LINK_WEEKS_SCALE)
        o.scale_checks = checks
        failed = [k for k, v in checks.items() if v is False]
        unknown = [k for k, v in checks.items() if v is None]
        q7 = "7. ER 2.0% or more AND every Scale condition?"
        if not failed and not unknown:
            o.step(7, q7, "YES", f"median ER {_pct(er)}; all Scale conditions hold")
            return o.done("SCALE_ELIGIBLE", "All Scale conditions hold. Scale is one step at a time and only if the capacity check passes (6.4).")
        o.step(7, q7, "no", ("not met: " + "; ".join(failed) if failed else "") + (" ; cannot confirm: " + "; ".join(unknown) if unknown else ""))
        if failed:
            o.reasons.append("Scale blocked by: " + "; ".join(failed) + ".")
        if unknown:
            o.reasons.append("Scale cannot be confirmed (no data): " + "; ".join(unknown) + ".")

    # ---- Step 6: Keep ----------------------------------------------------------------------
    q6 = "6. ER 0.6% to under 2.0% (or Scale not met), reach flat or rising, effort within Keep, rejection 20% or less?"
    unmet = []
    if not reach_ok:
        unmet.append(f"reach is falling ({'3 weeks' if reach_trend == 'falling3' else '2 weeks'})")
    if not effort_ok:
        bad = [T.EFFORT_LABELS[m] for m in EFFORT_METRICS if m in o.levels and o.levels[m] not in GOOD_FOR_KEEP]
        unmet.append("effort over the Keep line: " + "; ".join(bad))
    if not rej_ok:
        unmet.append("rejection rate over 20%")
    if not unmet:
        o.step(6, q6, "YES", f"median ER {_pct(er)}")
        return o.done("KEEP", f"Median ER {_pct(er)}; reach not falling; effort and rejection within Keep. Continue 6 more weeks, one experiment at a time.")
    o.step(6, q6, "no", "; ".join(unmet))
    o.step(6, "6b. So step 5 applies: Keep conditions partly unmet?", "YES", "; ".join(unmet))
    return o.done("FIX", "ER is fine but Keep conditions are partly unmet: " + "; ".join(unmet) + ". Change ONE variable for 4 weeks, then re-test.")
