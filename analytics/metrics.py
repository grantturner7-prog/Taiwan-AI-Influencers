"""metrics.py - every number the dashboard and weekly report show, computed from the tracker database.

Definitions follow strategy/portfolio.md section 6.1 (see thresholds.py for the numbers):
  * Week n of a persona = days [7*(n-1), 7*n) after its first PUBLISHED post (the assumed W0 until one exists).
  * Organic = sponsorship_type 'none'. Sponsored/gifted/affiliate posts are reported separately.
  * ER per post = (saves + shares + comments) / reach, using only the terms the platform reported. If reach is
    blank, views is the denominator and the result says so. Likes are excluded. Link clicks are reported
    separately (weekly, persona level).
  * Account figure = MEDIAN of post ERs in the window.  Minimum sample = 8 organic posts per platform.
  * The tree (decision.py) runs per account (persona x platform).

Nothing here writes to the database.
"""
from __future__ import annotations

import datetime as dt
import sqlite3
from collections import defaultdict
from statistics import mean, median

import thresholds as T
import tracker
from decision import decide

N7_PERSONA = "buzhou"   # the AI-tools persona: its demos need an operator recording (portfolio.md 5.1)
ONE_DAY = dt.timedelta(days=1)


def d2(s):
    return dt.date.fromisoformat(s) if s else None


def week_of(first: dt.date, day: dt.date) -> int:
    """1-based week number; 0 or negative before the first post."""
    return (day - first).days // 7 + 1


def week_start(first: dt.date, n: int) -> dt.date:
    return first + dt.timedelta(days=7 * (n - 1))


def week_end(first: dt.date, n: int) -> dt.date:
    return week_start(first, n + 1) - ONE_DAY


def _med(xs):
    xs = [x for x in xs if x is not None]
    return median(xs) if xs else None


# ---------------------------------------------------------------------------------------
# Posts and ER
# ---------------------------------------------------------------------------------------
def post_er(row: dict):
    """Return the ER record for one post row, or None if it cannot be computed."""
    reach, views = row.get("reach"), row.get("views")
    if reach:
        denom, kind = reach, "reach"
    elif views:
        denom, kind = views, "views"
    else:
        return None
    if row.get("shares") is None and row.get("comments") is None:
        return None
    num, terms = 0, []
    for name in ("saves", "shares", "comments"):
        v = row.get(name)
        if v is not None:
            num += v
            terms.append(name)
    if T.ER_INCLUDES_POST_LINK_CLICKS and row.get("link_clicks") is not None:
        num += row["link_clicks"]
        terms.append("link_clicks")
    return {"er": num / denom, "numerator": num, "denominator": denom, "denom_kind": kind, "terms": terms}


def load_posts(conn, persona, platform, start=None, end=None, organic=True, as_of=None):
    """Published posts of one account with their latest metrics snapshot and ER record."""
    sql = """SELECT p.post_id, p.persona, p.platform, p.master_id, p.format, p.pillar, p.hook_type,
                    p.published_date, p.sponsorship_type, p.status, p.url,
                    v.snapshot_date, v.reach, v.views, v.likes, v.saves, v.shares, v.comments, v.link_clicks
             FROM posts p LEFT JOIN v_post_latest v ON v.post_id = p.post_id
             WHERE p.persona=? AND p.platform=? AND p.status='published' AND p.published_date IS NOT NULL"""
    args = [persona, platform]
    if start:
        sql += " AND p.published_date >= ?"
        args.append(start.isoformat())
    if end:
        sql += " AND p.published_date <= ?"
        args.append(end.isoformat())
    if as_of:
        sql += " AND p.published_date <= ?"
        args.append(as_of.isoformat())
    if organic:
        sql += " AND p.sponsorship_type = 'none'"
    sql += " ORDER BY p.published_date, p.post_id"
    out = []
    for r in conn.execute(sql, args):
        row = dict(r)
        row["date"] = d2(row["published_date"])
        row["er_rec"] = post_er(row)
        row["er"] = row["er_rec"]["er"] if row["er_rec"] else None
        sv = [row.get("saves"), row.get("shares")]
        row["saves_shares"] = None if all(x is None for x in sv) else sum(x or 0 for x in sv)
        v = row.get("views")
        row["common"] = ((row.get("shares") or 0) + (row.get("comments") or 0)) / v * 1000 if v else None
        out.append(row)
    return out


def summarise_posts(posts):
    """Median ER, saves+shares share, denominators for a list of post rows (only posts with a computable ER)."""
    scored = [p for p in posts if p["er"] is not None]
    kinds = sorted({p["er_rec"]["denom_kind"] for p in scored})
    terms = sorted({t for p in scored for t in p["er_rec"]["terms"]})
    with_saves = [p for p in scored if p.get("saves") is not None]
    sv_share = None
    if with_saves:
        tot = sum((p["saves"] or 0) + (p["shares"] or 0) + (p["comments"] or 0) for p in with_saves)
        sv = sum((p["saves"] or 0) + (p["shares"] or 0) for p in with_saves)
        sv_share = sv / tot if tot else None
    return {
        "n_published": len(posts),
        "n_scored": len(scored),
        "n_missing_metrics": len([p for p in posts if p["er"] is None]),
        "er": _med([p["er"] for p in scored]),
        "er_min": min((p["er"] for p in scored), default=None),
        "er_max": max((p["er"] for p in scored), default=None),
        "sv_share": sv_share,
        "sv_median": _med([p["saves_shares"] for p in with_saves]),
        "common_per_1000_views": _med([p["common"] for p in scored if p["common"] is not None]),
        "denominators": kinds,
        "terms": terms,
        "median_reach_or_views": _med([p["er_rec"]["denominator"] for p in scored]),
        "median_interactions": _med([p["er_rec"]["numerator"] for p in scored]),
        "n_young": len([p for p in scored if p["snapshot_date"] and p["date"] and (d2(p["snapshot_date"]) - p["date"]).days < 7]),
    }


# ---------------------------------------------------------------------------------------
# Persona clock
# ---------------------------------------------------------------------------------------
def first_post(conn, persona):
    r = conn.execute("""SELECT MIN(published_date) m FROM posts
                        WHERE persona=? AND status IN ('published','taken_down') AND published_date IS NOT NULL""", (persona,)).fetchone()
    if r["m"]:
        return d2(r["m"]), "actual"
    r = conn.execute("SELECT assumed_first_post a FROM personas WHERE slug=?", (persona,)).fetchone()
    if r and r["a"]:
        return d2(r["a"]), "assumed"
    return None, None


# ---------------------------------------------------------------------------------------
# Weekly series
# ---------------------------------------------------------------------------------------
def weekly_series(conn, persona, platform, first, field, upto_week, mode="sum"):
    """{week: value or None} for weeks 1..upto_week from account_daily."""
    out = {w: None for w in range(1, max(upto_week, 0) + 1)}
    if not out:
        return out
    rows = conn.execute(f"SELECT day, {field} v FROM account_daily WHERE persona=? AND platform=? AND day>=? ORDER BY day",
                        (persona, platform, first.isoformat())).fetchall()
    for r in rows:
        if r["v"] is None:
            continue
        w = week_of(first, d2(r["day"]))
        if w not in out:
            continue
        if mode == "sum":
            out[w] = (out[w] or 0) + r["v"]
        else:
            out[w] = r["v"]   # rows are ordered by day, so the last write is the closing value
    return out


def weekly_reach_from_posts(conn, persona, platform, first, upto_week):
    out = {w: None for w in range(1, max(upto_week, 0) + 1)}
    for p in load_posts(conn, persona, platform, start=first, organic=False):
        w = week_of(first, p["date"])
        val = p["reach"] if p["reach"] is not None else p["views"]
        if w in out and val is not None:
            out[w] = (out[w] or 0) + val
    return out


def classify_trend(values):
    """Reach trend from the last weekly values (oldest first). See thresholds.REACH_FLAT_BAND."""
    v = [x for x in values if x is not None]
    if len(v) < 3:
        return "unknown"
    band = T.REACH_FLAT_BAND
    dirs = []
    for a, b in zip(v, v[1:]):
        if a == 0:
            dirs.append("up" if b > 0 else "flat")
            continue
        ch = (b - a) / a
        dirs.append("up" if ch > band else "down" if ch < -band else "flat")
    if len(dirs) >= 3 and dirs[-3:] == ["down"] * 3:
        return "falling3"
    if dirs[-2:] == ["down"] * 2:
        return "falling2"
    if "down" not in dirs[-2:] and v[-1] > v[-3] * (1 + band):
        return "rising"
    return "flat"


def follower_stats(series, up_to_week):
    """series {week: closing followers}. Returns growth weeks (of the first 6), biggest drop and flags."""
    weeks = [w for w in sorted(series) if w <= min(up_to_week, T.FOLLOWER_WEEKS)]
    growth, drop = 0, None
    prev = None
    for w in weeks:
        cur = series[w]
        if cur is None:
            continue
        if prev is not None and cur > prev:
            growth += 1
        if prev is not None and prev >= T.FOLLOWER_DROP_MIN_BASE and cur < prev * (1 - T.FOLLOWER_DROP):
            drop = (w, prev, cur)
        prev = cur
    return {"growth_weeks": growth, "weeks_counted": len(weeks), "big_drop": drop}


# ---------------------------------------------------------------------------------------
# Persona-level context: effort, rejection, link clicks, leads, standing
# ---------------------------------------------------------------------------------------
def effort_stats(conn, persona, win_start, win_end):
    rows = conn.execute("""SELECT e.role, e.task, e.minutes, e.post_id, e.master_id, e.log_date, p.published_date, p.master_id AS pm
                           FROM effort_log e LEFT JOIN posts p ON p.post_id = e.post_id
                           WHERE e.persona=?""", (persona,)).fetchall()
    units = {"operator_min_per_approval": defaultdict(list), "n7_min_per_master": defaultdict(list),
             "wife_min_per_master": defaultdict(list)}
    for r in rows:
        if r["role"] == "operator" and r["task"] == "approval" and r["post_id"]:
            key, m = r["post_id"], "operator_min_per_approval"
        elif r["task"] == "n7_recording" and (r["master_id"] or r["post_id"]):
            key, m = (r["master_id"] or r["pm"] or r["post_id"]), "n7_min_per_master"
        elif r["role"] == "wife" and r["task"] == "master_review" and (r["master_id"] or r["post_id"]):
            key, m = (r["master_id"] or r["pm"] or r["post_id"]), "wife_min_per_master"
        else:
            continue
        when = d2(r["published_date"]) or d2(r["log_date"])
        units[m][key].append((when, r["minutes"]))
    out = {}
    for m, bucket in units.items():
        vals = []
        for key, items in bucket.items():
            when = min(w for w, _ in items)
            if win_start <= when <= win_end:
                vals.append(sum(x for _, x in items))
        if m == "n7_min_per_master" and persona != N7_PERSONA:
            continue
        if not vals and m == "n7_min_per_master":
            out[m] = {"value": None, "n": 0, "scored": False}
            continue
        if m == "n7_min_per_master" or vals:
            out[m] = {"value": mean(vals) if vals else None, "n": len(vals), "scored": len(vals) >= T.MIN_EFFORT_UNITS}
        else:
            out[m] = {"value": None, "n": 0, "scored": False}
    return out


def rejection_stats(conn, persona, win_start, win_end):
    rows = conn.execute("""SELECT first_pass_verdict v, reason_category c, near_miss nm FROM review_events
                           WHERE persona=? AND reviewed_on BETWEEN ? AND ?""",
                        (persona, win_start.isoformat(), win_end.isoformat())).fetchall()
    n = len(rows)
    rej = [r for r in rows if r["v"] in ("changes", "rejected")]
    reasons = defaultdict(int)
    for r in rej:
        reasons[r["c"] or "not categorised"] += 1
    return {"value": (len(rej) / n) if n else None, "n": n, "rejected": len(rej), "scored": n >= T.MIN_REVIEWS_FOR_RATE,
            "reasons": dict(reasons), "near_misses": sum(r["nm"] for r in rows)}


def link_stats(conn, persona, first, as_of):
    """Weekly link clicks for a persona. Uses the link-page counter if it has any clicks, else platform insights."""
    week_now = week_of(first, as_of)
    last_w = min(T.FOLLOWER_WEEKS, week_now)
    src = None
    clicks = {w: 0 for w in range(1, max(last_w, 0) + 1)}
    lp = conn.execute("SELECT COUNT(*) c FROM account_daily WHERE persona=? AND platform='linkpage' AND link_clicks IS NOT NULL", (persona,)).fetchone()["c"]
    q = "SELECT day, link_clicks FROM account_daily WHERE persona=? AND link_clicks IS NOT NULL AND day>=? AND day<=? "
    if lp:
        src = "linkpage"
        q += "AND platform='linkpage'"
    else:
        q += "AND platform<>'linkpage'"
    rows = conn.execute(q, (persona, first.isoformat(), as_of.isoformat())).fetchall()
    if rows and src is None:
        src = "platform_insights"
    for r in rows:
        w = week_of(first, d2(r["day"]))
        if w in clicks:
            clicks[w] += r["link_clicks"]
    reach = {w: 0 for w in clicks}
    for r in conn.execute("""SELECT day, reach, views FROM account_daily WHERE persona=? AND platform<>'linkpage' AND day>=? AND day<=?""",
                          (persona, first.isoformat(), as_of.isoformat())):
        w = week_of(first, d2(r["day"]))
        if w in reach:
            reach[w] += r["reach"] if r["reach"] is not None else (r["views"] or 0)
    weekly = []
    for w in sorted(clicks):
        per1000 = clicks[w] / reach[w] * 1000 if reach[w] else None
        weekly.append({"week": w, "clicks": clicks[w], "reach": reach[w], "per_1000_reach": per1000})
    return {"source": src, "weekly": weekly, "weeks_with_clicks": sum(1 for x in weekly if x["clicks"] > 0),
            "weeks_counted": len(weekly), "total": sum(clicks.values())}


def lead_stats(conn, persona, as_of):
    rows = conn.execute("SELECT kind, COUNT(*) c FROM lead_signals WHERE persona=? AND signal_date<=? GROUP BY kind",
                        (persona, as_of.isoformat())).fetchall()
    by = {r["kind"]: r["c"] for r in rows}
    return {"by_kind": by, "signals": sum(v for k, v in by.items() if k != "outreach_sent"), "outreach": by.get("outreach_sent", 0)}


# ---------------------------------------------------------------------------------------
# Standing gates (portfolio.md 6.2)
# ---------------------------------------------------------------------------------------
def standing_events(conn, persona=None):
    sql = "SELECT * FROM standing_events"
    args = []
    if persona:
        sql += " WHERE persona=?"
        args.append(persona)
    sql += " ORDER BY event_date, ref"
    return [dict(r) for r in conn.execute(sql, args)]


def standing_for_account(events, persona, platform, as_of, win_start=None, win_end=None):
    """Open gates, retire triggers and in-window event count for one account."""
    mine = [e for e in events if e["persona"] == persona and e["event_date"] <= as_of.isoformat()
            and e["platform"] in (None, platform)]
    open_, retire = [], []
    for e in mine:
        if e["cleared_on"] is None or e["cleared_on"] > as_of.isoformat():
            label, hours, action = T.GATES[e["gate"]]
            days_open = (as_of - d2(e["event_date"])).days
            overdue = hours is not None and days_open * 24 > hours
            txt = f"{label}: {e['description']} (since {e['event_date']}, open {days_open} day(s); rule: {action})"
            if overdue:
                txt += " - OVERDUE"
            open_.append(txt)
            if e["gate"] == "strike_restriction" and days_open > T.STRIKE_STOP_DAYS:
                retire.append(f"Restriction open {days_open} days (over {T.STRIKE_STOP_DAYS}): stop this persona on this platform (6.2).")
    r6 = sorted(d2(e["event_date"]) for e in events if e["persona"] == persona and e["gate"] == "rule6_contact"
                and e["event_date"] <= as_of.isoformat())
    for a, b in zip(r6, r6[1:]):
        if (b - a).days <= T.RULE6_REPEAT_DAYS:
            retire.append(f"Second Ground-rule-6 event within 8 weeks ({a} and {b}): the persona or the pillar is retired (6.2).")
            break
    in_window = 0
    if win_start and win_end:
        in_window = len([e for e in mine if win_start.isoformat() <= e["event_date"] <= win_end.isoformat()])
    return {"open": open_, "retire": retire, "in_window": in_window}


def repeat_alerts(events, persona, as_of):
    """Alerts for repeat patterns that 6.2 says pause the persona (shown as notes; status follows open events)."""
    out = []
    mine = [e for e in events if e["persona"] == persona and e["event_date"] <= as_of.isoformat()]
    dis = sorted(d2(e["event_date"]) for e in mine if e["gate"] == "disclosure_failure")
    for a, b in zip(dis, dis[1:]):
        if (a.year, (a.month - 1) // 3) == (b.year, (b.month - 1) // 3):
            out.append(f"Repeat disclosure failure in the same quarter ({a}, {b}): 6.2 says pause the persona.")
            break
    gar = sorted(d2(e["event_date"]) for e in mine if e["gate"] == "garbled_or_wrong")
    for a, b in zip(gar, gar[1:]):
        if (b - a).days <= T.GARBLED_REPEAT_DAYS:
            out.append(f"Two garbled/wrong-fact events within 6 weeks ({a}, {b}): 6.2 says pause until the QA step is fixed.")
            break
    return out


def persona_alerts(conn, persona, first, as_of):
    """Alerts derived from hand-counted numbers (no stored event needed)."""
    alerts = []
    if first:
        wk = week_of(first, as_of)
        for w in range(max(1, wk - 1), wk + 1):
            tot, got = 0, False
            for r in conn.execute("""SELECT real_person_comments v FROM account_daily WHERE persona=? AND platform<>'linkpage'
                                     AND day BETWEEN ? AND ?""", (persona, week_start(first, w).isoformat(), min(week_end(first, w), as_of).isoformat())):
                if r["v"] is not None:
                    tot += r["v"]
                    got = True
            if got and tot >= T.REAL_PERSON_WEEKLY_ALERT:
                alerts.append(f"Week {w}: {tot} comments asking whether it is a real person (alert at {T.REAL_PERSON_WEEKLY_ALERT}). "
                              f"6.2: strengthen the first-line and on-screen label within 48 hours.")
    rows = conn.execute("""SELECT near_miss FROM review_events WHERE persona=? AND reviewed_on<=? ORDER BY reviewed_on DESC, ref DESC LIMIT ?""",
                        (persona, as_of.isoformat(), T.NEAR_MISS_WINDOW_DRAFTS)).fetchall()
    nm = sum(r["near_miss"] for r in rows)
    if len(rows) >= 10 and nm >= T.NEAR_MISS_ALERT:
        alerts.append(f"{nm} of the last {len(rows)} reviewed drafts were near misses (alert at {T.NEAR_MISS_ALERT} of any {T.NEAR_MISS_WINDOW_DRAFTS}). "
                      f"6.2: redesign the content pillars before continuing.")
    return alerts


# ---------------------------------------------------------------------------------------
# Experiments
# ---------------------------------------------------------------------------------------
def experiments_for(conn, persona=None):
    sql, args = "SELECT * FROM experiments", []
    if persona:
        sql += " WHERE persona=?"
        args.append(persona)
    sql += " ORDER BY start_date, exp_id"
    return [dict(r) for r in conn.execute(sql, args)]


# ---------------------------------------------------------------------------------------
# One account: facts -> decision
# ---------------------------------------------------------------------------------------
def account_assessment(conn, persona, platform, as_of, events=None):
    events = events if events is not None else standing_events(conn)
    first, first_kind = first_post(conn, persona)
    exps = experiments_for(conn, persona)
    acct = {"persona": persona, "platform": platform, "first_post": first, "first_post_kind": first_kind}
    handle = conn.execute("SELECT handle, role FROM accounts WHERE persona=? AND platform=?", (persona, platform)).fetchone()
    acct["handle"], acct["role"] = (handle["handle"], handle["role"]) if handle else (None, None)

    all_pub = load_posts(conn, persona, platform, organic=False, as_of=as_of)
    acct["posts_published_all"] = len(all_pub)
    acct["posts_sponsored"] = len([p for p in all_pub if p["sponsorship_type"] != "none"])

    if first is None or first_kind == "assumed" or first > as_of:
        # no real post anywhere for this persona (the assumed date is only a planning date)
        facts = {"persona": persona, "platform": platform, "data_state": "not_started", "n_scored": 0, "min_sample": T.MIN_ORGANIC_POSTS,
                 "window_label": "weeks 3 to 6", "gates_open": [], "retire_triggers": []}
        st = standing_for_account(events, persona, platform, as_of)
        facts["gates_open"], facts["retire_triggers"] = st["open"], st["retire"]
        acct.update({"facts": facts, "decision": decide(facts), "week_now": None, "review_date": None,
                     "window": None, "summary": summarise_posts([]), "posts": [], "followers": None,
                     "followers_series": {}, "reach_series": {}, "reach_source": None, "reach_trend": "unknown",
                     "weekly_er": {}, "follower_stats": None, "experiment_running": None, "sample_note": "",
                     "effort": {}, "rejection": None, "links": None, "leads": None, "audience": None, "events": st,
                     "state": "not_started", "provisional": False, "fix_retest": False, "window_label": "weeks 3 to 6"})
        return acct

    week_now = week_of(first, as_of)
    review_date = first + dt.timedelta(days=7 * T.WINDOW_LAST_WEEK)
    ext_date = first + dt.timedelta(days=7 * T.EXTENDED_LAST_WEEK)
    acct.update({"week_now": week_now, "review_date": review_date})

    done_fix = [e for e in exps if e["is_fix"] and e["status"] == "done" and e["end_date"] and e["end_date"] <= as_of.isoformat()
                and e["kind"] != "redesign" and e["platform"] in (None, platform)]
    redesign_done = any(e["kind"] == "redesign" and e["status"] == "done" for e in exps)
    running = [e for e in exps if e["status"] == "running" and e["platform"] in (None, platform)]
    acct["experiment_running"] = running[0] if running else None

    provisional = False
    if done_fix:
        fx = max(done_fix, key=lambda e: e["end_date"])
        w_start, w_end = d2(fx["start_date"]), d2(fx["end_date"])
        label = f"Fix re-test {w_start} to {w_end}"
        posts_w = [p for p in all_pub if p["sponsorship_type"] == "none" and w_start <= p["date"] <= w_end]
        summ = summarise_posts(posts_w)
        state = "scored" if summ["n_scored"] >= T.MIN_ORGANIC_POSTS else "hold"
        fix_retest = True
        w_end_week = week_of(first, w_end)
    else:
        fix_retest = False
        w_start = week_start(first, T.WINDOW_FIRST_WEEK)
        w_end = week_end(first, T.WINDOW_LAST_WEEK)
        label = f"weeks {T.WINDOW_FIRST_WEEK} to {T.WINDOW_LAST_WEEK}"
        organic = [p for p in all_pub if p["sponsorship_type"] == "none"]
        s6 = summarise_posts([p for p in organic if w_start <= p["date"] <= w_end])
        w_end_week = T.WINDOW_LAST_WEEK
        if as_of < review_date:
            if s6["n_scored"] >= T.MIN_ORGANIC_POSTS:
                state, provisional, summ, posts_w = "scored", True, s6, [p for p in organic if w_start <= p["date"] <= w_end]
            else:
                state, summ, posts_w = "in_progress", s6, [p for p in organic if w_start <= p["date"] <= w_end]
        elif s6["n_scored"] >= T.MIN_ORGANIC_POSTS:
            state, summ, posts_w = "scored", s6, [p for p in organic if w_start <= p["date"] <= w_end]
        elif as_of < ext_date:
            w_end = week_end(first, T.EXTENDED_LAST_WEEK)
            posts_w = [p for p in organic if w_start <= p["date"] <= w_end]
            state, summ = "extend", summarise_posts(posts_w)
            label = "weeks 3 to 6 (extending to week 8)"
        else:
            w_end = week_end(first, T.EXTENDED_LAST_WEEK)
            w_end_week = T.EXTENDED_LAST_WEEK
            posts_w = [p for p in organic if w_start <= p["date"] <= w_end]
            summ = summarise_posts(posts_w)
            label = "weeks 3 to 8 (extended)"
            state = "scored" if summ["n_scored"] >= T.MIN_ORGANIC_POSTS else "hold"
    acct["window"] = (w_start, w_end)
    acct["window_label"] = label

    # series
    last_complete = week_of(first, as_of) - 1
    end_week = max(0, min(w_end_week, last_complete)) if state != "in_progress" else max(0, last_complete)
    upto = max(week_of(first, as_of), 0)
    reach_series = weekly_series(conn, persona, platform, first, "reach", upto, "sum")
    reach_src = "account daily"
    if all(v is None for v in reach_series.values()):
        views_series = weekly_series(conn, persona, platform, first, "views", upto, "sum")
        if any(v is not None for v in views_series.values()):
            reach_series, reach_src = views_series, "account daily views"
        else:
            reach_series, reach_src = weekly_reach_from_posts(conn, persona, platform, first, upto), "post metrics"
        if all(v is None for v in reach_series.values()):
            reach_src = None
    trend_vals = [reach_series.get(w) for w in range(max(1, end_week - 3), end_week + 1)]
    trend = classify_trend(trend_vals) if reach_src else "unknown"
    fol_series = weekly_series(conn, persona, platform, first, "followers", upto, "last")
    fstats = follower_stats(fol_series, end_week)
    latest_f = conn.execute("SELECT followers FROM account_daily WHERE persona=? AND platform=? AND followers IS NOT NULL AND day<=? ORDER BY day DESC LIMIT 1",
                            (persona, platform, as_of.isoformat())).fetchone()
    acct["followers"] = latest_f["followers"] if latest_f else None
    age = conn.execute("SELECT target_age_share a, taiwan_share t FROM account_daily WHERE persona=? AND platform=? AND day<=? AND (target_age_share IS NOT NULL OR taiwan_share IS NOT NULL) ORDER BY day DESC LIMIT 1",
                       (persona, platform, as_of.isoformat())).fetchone()
    watch = []
    if fstats["big_drop"]:
        wk, a, b = fstats["big_drop"]
        watch.append(f"Followers dropped {a} to {b} in week {wk} (over 10%): record the cause; an unexplained drop is a Fix signal (6.1).")
    if age and age["a"] is not None and age["a"] < T.TARGET_AGE_SHARE_RETIRE:
        watch.append(f"Target age band is {age['a']*100:.0f}% of followers (under 40%): table 6.1 retire-review trigger; allow one re-target first.")

    # persona-level inputs, same window
    eff = effort_stats(conn, persona, w_start, w_end)
    rej_start = w_start if fix_retest else week_start(first, T.REJECTION_FIRST_WEEK)
    rej = rejection_stats(conn, persona, rej_start, w_end)
    links = link_stats(conn, persona, first, as_of)
    leads = lead_stats(conn, persona, as_of)
    if leads["outreach"] >= T.LEAD_OUTREACH_NO_SIGNAL and leads["signals"] == 0 and summ["er"] is not None and summ["er"] < T.ER_KEEP:
        watch.append(f"{leads['outreach']} outreach messages and no lead signal with ER under 0.6%: table 6.1 retire-review trigger for the revenue row.")
    st = standing_for_account(events, persona, platform, as_of, w_start, w_end)

    n_for_test = summ["n_scored"] if state != "extend" else summarise_posts(
        [p for p in posts_w if p["date"] <= week_end(first, T.WINDOW_LAST_WEEK)])["n_scored"]
    facts = {
        "persona": persona, "platform": platform, "data_state": state, "provisional": provisional,
        "n_scored": n_for_test, "n_extended": summ["n_scored"], "min_sample": T.MIN_ORGANIC_POSTS, "window_label": label,
        "er": summ["er"], "sv_share": summ["sv_share"], "reach_trend": trend,
        "gates_open": st["open"], "retire_triggers": st["retire"], "events_in_window": st["in_window"],
        "effort": eff, "rejection": rej, "redesign_done": redesign_done, "fix_retest_done": fix_retest,
        "lead_signals": leads["signals"], "link_weeks": links["weeks_with_clicks"], "watch": watch,
    }
    decision = decide(facts)
    # weekly median ER (for the report)
    by_week = defaultdict(list)
    for p in posts_w if state != "not_started" else []:
        if p["er"] is not None:
            by_week[week_of(first, p["date"])].append(p["er"])
    note = ""
    if summ["n_scored"] and summ["n_scored"] < 15:
        note = f"Median of only {summ['n_scored']} posts: one or two unusual posts can move it. Treat the status as indicative."
    acct.update({
        "facts": facts, "decision": decision, "summary": summ, "posts": posts_w, "followers_series": fol_series,
        "reach_series": reach_series, "reach_source": reach_src, "reach_trend": trend, "follower_stats": fstats,
        "weekly_er": {w: _med(v) for w, v in by_week.items()}, "audience": dict(age) if age else None,
        "effort": eff, "rejection": rej, "links": links, "leads": leads, "sample_note": note,
        "events": st, "state": state, "provisional": provisional, "fix_retest": fix_retest,
    })
    return acct


# ---------------------------------------------------------------------------------------
# Money and capacity
# ---------------------------------------------------------------------------------------
def finance(conn, as_of):
    as_s = as_of.isoformat()
    months = defaultdict(lambda: {"tool": 0.0, "one_time": 0.0, "received": 0.0, "invoiced": 0.0})
    for r in conn.execute("SELECT substr(cost_date,1,7) m, cost_kind k, SUM(amount_twd) s FROM costs WHERE cost_date<=? GROUP BY m, k", (as_s,)):
        months[r["m"]][r["k"]] += r["s"]
    for r in conn.execute("SELECT substr(revenue_date,1,7) m, status k, SUM(amount_twd) s FROM revenue WHERE revenue_date<=? GROUP BY m, k", (as_s,)):
        months[r["m"]][r["k"]] += r["s"]
    by_persona = {}
    for r in conn.execute("SELECT COALESCE(persona,'(studio)') p, source_type t, SUM(amount_twd) s FROM revenue WHERE revenue_date<=? AND status='received' GROUP BY p, t", (as_s,)):
        by_persona.setdefault(r["p"], {})[r["t"]] = r["s"]
    cost_persona_tagged = conn.execute("SELECT COALESCE(SUM(amount_twd),0) s FROM costs WHERE persona IS NOT NULL AND cost_kind='tool' AND cost_date<=?", (as_s,)).fetchone()["s"]
    m_now = as_of.strftime("%Y-%m")
    rows = []
    cum_cost = cum_rev = 0.0
    for m in sorted(months):
        v = months[m]
        cum_cost += v["tool"] + v["one_time"]
        cum_rev += v["received"]
        rows.append({"month": m, **v, "net": v["received"] - v["tool"] - v["one_time"], "cum_cost": cum_cost, "cum_revenue": cum_rev})
    cur = months.get(m_now, {"tool": 0.0, "one_time": 0.0, "received": 0.0, "invoiced": 0.0})
    return {
        "months": rows, "current_month": m_now, "current": dict(cur),
        "cum_cost": cum_cost, "cum_revenue": cum_rev, "cum_net": cum_rev - cum_cost,
        "revenue_by_persona": by_persona, "persona_tagged_cost": cost_persona_tagged,
        "cap_base": T.MONTHLY_TOOL_CAP_BASE, "cap_headroom": T.MONTHLY_TOOL_CAP_HEADROOM,
    }


def capacity(conn, as_of):
    """Average logged minutes per week over the last four complete weeks (portfolio.md 6.4)."""
    firsts = [first_post(conn, r["slug"]) for r in conn.execute("SELECT DISTINCT persona slug FROM accounts WHERE platform<>'linkpage'")]
    actual = [f for f, k in firsts if f and k == "actual"]
    if not actual:
        return {"available": False}
    w0 = min(actual)
    wk_now = week_of(w0, as_of)
    last = wk_now - 1
    if last < 1:
        return {"available": False}
    first_w = max(1, last - T.CAPACITY_AVG_WEEKS + 1)
    rows = []
    for w in range(first_w, last + 1):
        s, e = week_start(w0, w).isoformat(), week_end(w0, w).isoformat()
        op = conn.execute("SELECT COALESCE(SUM(minutes),0) m FROM effort_log WHERE role='operator' AND log_date BETWEEN ? AND ?", (s, e)).fetchone()["m"]
        wf = conn.execute("SELECT COALESCE(SUM(minutes),0) m FROM effort_log WHERE role='wife' AND log_date BETWEEN ? AND ?", (s, e)).fetchone()["m"]
        ap = conn.execute("SELECT COUNT(*) c FROM posts WHERE status='published' AND published_date BETWEEN ? AND ?", (s, e)).fetchone()["c"]
        rows.append({"week": w, "operator": op, "wife": wf, "approvals": ap})
    n = len(rows)
    avg = lambda k: sum(r[k] for r in rows) / n
    logged = any(r["operator"] or r["wife"] for r in rows)
    res = {"available": logged, "weeks": rows, "operator_avg": avg("operator"), "wife_avg": avg("wife"), "approvals_avg": avg("approvals"),
           "gate_operator": T.OPERATOR_PLANNED_LOAD_GATE, "gate_wife": T.WIFE_PLANNED_LOAD_GATE, "gate_approvals": T.MAX_APPROVALS_PER_WEEK}
    res["pass"] = (res["operator_avg"] <= res["gate_operator"] and res["wife_avg"] <= res["gate_wife"] and res["approvals_avg"] <= res["gate_approvals"])
    return res


# ---------------------------------------------------------------------------------------
# Whole portfolio
# ---------------------------------------------------------------------------------------
def live_accounts(conn):
    rows = conn.execute("""SELECT a.persona, a.platform, a.role, p.name_zh, p.status, p.wave
                           FROM accounts a JOIN personas p ON p.slug=a.persona JOIN platforms f ON f.code=a.platform
                           WHERE f.kind='social' ORDER BY p.rowid, CASE a.role WHEN 'primary' THEN 0 ELSE 1 END, a.platform""").fetchall()
    return [dict(r) for r in rows]


def portfolio_snapshot(conn, as_of=None):
    if as_of is None:
        meta = tracker.get_meta(conn, "demo_as_of") if tracker.is_demo(conn) else None
        as_of = d2(meta) if meta else dt.date.today()
    events = standing_events(conn)
    by_persona = {}
    for a in live_accounts(conn):
        pr = by_persona.setdefault(a["persona"], {"slug": a["persona"], "name_zh": a["name_zh"], "status": a["status"], "wave": a["wave"], "accounts": []})
        pr["accounts"].append(account_assessment(conn, a["persona"], a["platform"], as_of, events))
    personas = []
    for slug, pr in by_persona.items():
        first, kind = first_post(conn, slug)
        accts = pr["accounts"]
        active = [a for a in accts if a["decision"]["status"] not in ("PAUSE", "RETIRE")]
        best = max(active, key=lambda a: T.STATUS_RANK[a["decision"]["status"]], default=None)
        pr.update({
            "first_post": first, "first_post_kind": kind,
            "week_now": (week_of(first, as_of) if first and kind == "actual" else None),
            "review_date": (first + dt.timedelta(days=42) if first else None),
            "headline": best["decision"]["status"] if best else (accts[0]["decision"]["status"] if accts else "NOT_STARTED"),
            "headline_account": best["platform"] if best else None,
            "paused": [a["platform"] for a in accts if a["decision"]["status"] in ("PAUSE", "RETIRE")],
            "alerts": persona_alerts(conn, slug, first if kind == "actual" else None, as_of) + repeat_alerts(events, slug, as_of),
            "reviews_total": conn.execute("SELECT COUNT(*) c FROM review_events WHERE persona=?", (slug,)).fetchone()["c"],
        })
        first_acc = next((a for a in accts if a.get("rejection") is not None), None)
        pr["rejection"] = first_acc["rejection"] if first_acc else None
        pr["effort"] = first_acc["effort"] if first_acc else {}
        pr["links"] = first_acc["links"] if first_acc else None
        pr["leads"] = first_acc["leads"] if first_acc else None
        personas.append(pr)
    return {
        "as_of": as_of, "is_demo": tracker.is_demo(conn), "personas": personas, "finance": finance(conn, as_of),
        "capacity": capacity(conn, as_of), "standing": events, "experiments": experiments_for(conn),
        "n_posts": conn.execute("SELECT COUNT(*) c FROM posts WHERE status='published'").fetchone()["c"],
        "n_metric_rows": conn.execute("SELECT COUNT(*) c FROM post_metrics").fetchone()["c"] + conn.execute("SELECT COUNT(*) c FROM account_daily").fetchone()["c"],
    }
