#!/usr/bin/env python3
"""weekly_report.py - prints what worked, what did not, and ONE experiment to run next, from the tracker data.

  python3 analytics/weekly_report.py                 # real database, as of today
  python3 analytics/weekly_report.py --demo          # DEMO database (every number invented)
  python3 analytics/weekly_report.py --as-of 2027-01-04 --out analytics/reports/2027-01-04.txt

Rule-based and deterministic: the same data gives the same report. There is no statistics model and no
language model in here. Every comparison states its sample size; a group needs at least 4 posts to be named,
a difference counts as "clear" only at 1.5x or more, and even then it is a hypothesis for the next experiment,
not a finding. The scoring rule is the portfolio.md 6.1 minimum sample: 8 organic posts per platform.

Report week = the 7 days before the as-of date (run it on a Monday for Monday to Sunday).
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import io
import re
import sys
import textwrap
from collections import defaultdict
from pathlib import Path

import metrics
import thresholds as T
import tracker

HERE = Path(__file__).resolve().parent
WIDTH = 96
PLAT = {"instagram": "Instagram", "threads": "Threads", "youtube_shorts": "YouTube Shorts", "facebook": "Facebook Page"}

ALT_FORMATS = {"instagram": ("carousel", "reel"), "threads": ("text", "image"), "youtube_shorts": ("short",), "facebook": ("image", "reel")}
HOOK_PAIR = ("number-first", "question-first")
REASON_FIX = {
    "language": "Before each draft reaches the wife, run `queue.py validate` and a mainland-vocabulary pass, and feed her last 10 corrections back into the drafting prompt.",
    "culture": "Add a culture and taboo pre-check line (mourning colours, religion, politics, ghost month, 228) to the draft checklist.",
    "fact": "Add a source-slip line to every draft: each number has a link and a date, checked by the operator before the wife sees it.",
    "safety": "Review the near-miss drafts and tighten the pillar brief on testimony, health, finance and income wording.",
}


def pct(x, d=2):
    return "n/a" if x is None else f"{x * 100:.{d}f}%"


def wrap(text, indent=0, hang=2):
    return textwrap.fill(text, width=WIDTH, initial_indent=" " * indent, subsequent_indent=" " * (indent + hang))


def bullet(text, indent=2):
    return textwrap.fill(text, width=WIDTH, initial_indent=" " * indent + "- ", subsequent_indent=" " * (indent + 2))


def name(p):
    return f"{p['slug']} {p['name_zh']}"


def acct_name(p, a):
    return f"{name(p)} / {PLAT.get(a['platform'], a['platform'])}"


def med(xs):
    xs = [x for x in xs if x is not None]
    if not xs:
        return None
    return metrics.median(xs)


# ---------------------------------------------------------------------------------------
# analysis helpers
# ---------------------------------------------------------------------------------------
def group_contrasts(posts):
    """For each dimension, the best and worst group by median ER (each group needs MIN_GROUP_POSTS posts)."""
    out = []
    for dim in ("format", "pillar", "hook_type"):
        groups = defaultdict(list)
        for p in posts:
            if p["er"] is not None and p.get(dim):
                groups[p[dim]].append(p["er"])
        groups = {k: v for k, v in groups.items() if len(v) >= T.MIN_GROUP_POSTS}
        if len(groups) < 2:
            continue
        stats = sorted(((med(v), len(v), k) for k, v in groups.items()), key=lambda t: (t[0], t[2]))
        lo, hi = stats[0], stats[-1]
        ratio = (hi[0] / lo[0]) if lo[0] else None
        clear = (ratio is None and hi[0] > 0) or (ratio is not None and ratio >= T.GROUP_RATIO)
        out.append({"dim": dim, "best": hi[2], "best_med": hi[0], "best_n": hi[1], "worst": lo[2], "worst_med": lo[0],
                    "worst_n": lo[1], "ratio": ratio, "clear": clear})
    return out


def ratio_text(c):
    if c["ratio"] is None:
        return f"{pct(c['best_med'])} against {pct(c['worst_med'])}"
    return f"{pct(c['best_med'])} against {pct(c['worst_med'])} ({c['ratio']:.1f}x)"


def sum_field(conn, persona, platform, field, start, end):
    r = conn.execute(f"SELECT SUM({field}) s, COUNT({field}) c FROM account_daily WHERE persona=? AND platform=? AND day BETWEEN ? AND ?",
                     (persona, platform, start.isoformat(), end.isoformat())).fetchone()
    return r["s"] if r["c"] else None


def followers_on(conn, persona, platform, day):
    r = conn.execute("SELECT followers f FROM account_daily WHERE persona=? AND platform=? AND followers IS NOT NULL AND day<=? ORDER BY day DESC LIMIT 1",
                     (persona, platform, day.isoformat())).fetchone()
    return r["f"] if r else None


def week_figures(conn, p, a, as_of):
    this_s, this_e = as_of - dt.timedelta(days=7), as_of - dt.timedelta(days=1)
    prev_s, prev_e = as_of - dt.timedelta(days=14), as_of - dt.timedelta(days=8)
    org = lambda s, e: [x for x in metrics.load_posts(conn, a["persona"], a["platform"], start=s, end=e)]
    tp, pp = org(this_s, this_e), org(prev_s, prev_e)
    field = "reach" if any(x["reach"] for x in tp + pp) or sum_field(conn, a["persona"], a["platform"], "reach", this_s, this_e) is not None else "views"
    return {
        "this": (this_s, this_e), "prev": (prev_s, prev_e), "posts_this": tp, "posts_prev": pp,
        "er_this": med([x["er"] for x in tp]), "er_prev": med([x["er"] for x in pp]),
        "n_this": len([x for x in tp if x["er"] is not None]), "n_prev": len([x for x in pp if x["er"] is not None]),
        "reach_field": field,
        "reach_this": sum_field(conn, a["persona"], a["platform"], field, this_s, this_e),
        "reach_prev": sum_field(conn, a["persona"], a["platform"], field, prev_s, prev_e),
        "f_now": followers_on(conn, a["persona"], a["platform"], this_e),
        "f_prev": followers_on(conn, a["persona"], a["platform"], prev_e),
    }


def account_posts_for_analysis(conn, a, first, as_of):
    """Organic posts from week 3 on (the scoring era) up to the day before the as-of date."""
    if first is None:
        return []
    return metrics.load_posts(conn, a["persona"], a["platform"], start=metrics.week_start(first, T.WINDOW_FIRST_WEEK),
                              end=as_of - dt.timedelta(days=1))


# ---------------------------------------------------------------------------------------
# experiment chooser
# ---------------------------------------------------------------------------------------
def next_exp_id(conn, demo):
    nums = []
    for r in conn.execute("SELECT exp_id FROM experiments"):
        m = re.search(r"E(\d+)$", r["exp_id"])
        if m:
            nums.append(int(m.group(1)))
    return ("DEMO-" if demo else "") + f"E{(max(nums) + 1 if nums else 1):03d}"


def choose_experiment(snap, conn, analysis):
    """Return (experiment dict | None, reason text, notes list). One experiment at a time per persona."""
    running_personas = {e["persona"] for e in snap["experiments"] if e["status"] == "running"}
    cands = []
    for p in snap["personas"]:
        for a in p["accounts"]:
            d = a["decision"]
            if d["status"] not in ("FIX", "KEEP"):
                continue
            if p["slug"] in running_personas:
                continue
            er = a["summary"]["er"] if a["summary"]["er"] is not None else 9
            rank = 0 if d["need_redesign"] else (1 if d["status"] == "FIX" else 2)
            cands.append((rank, er, p["slug"], a["platform"], p, a))
    if not cands:
        if running_personas:
            return None, ("No new experiment: every persona with a scored account already has one running (rule: one experiment at a time). "
                          "Let the running experiment finish before starting another."), []
        scored = [a for p in snap["personas"] for a in p["accounts"] if a["decision"]["status"] in ("FIX", "KEEP", "SCALE_ELIGIBLE", "RETIRE_REVIEW")]
        if not scored:
            return None, (f"No experiment yet: no account has {T.MIN_ORGANIC_POSTS} organic posts in its scoring window, so there is no baseline to change. "
                          "Changing a variable now would make the baseline unreadable. Keep format, hooks and cadence fixed and let the sample build."), []
        return None, "No experiment recommended: no account is in a state where the decision tree asks for one (Fix, or Keep with room to test).", []
    cands.sort(key=lambda t: (t[0], t[1], t[2], t[3]))
    rank, er, slug, platform, p, a = cands[0]
    d = a["decision"]
    posts = analysis.get((slug, platform), [])
    contrasts = group_contrasts(posts)
    notes = []
    exp = {"persona": slug, "platform": platform, "status": "planned", "is_fix": 1 if d["status"] == "FIX" else 0,
           "primary_metric": "median ER (" + ("/".join(a["summary"]["denominators"]) or "reach") + ")",
           "baseline_value": a["summary"]["er"], "planned_posts": 12}
    why = [f"{acct_name(p, a)} is {metrics.T.STATUS_LABELS[d['status']]}"
           + (f" (median ER {pct(a['summary']['er'])}, n={a['summary']['n_scored']})" if a['summary']['er'] is not None else "") + "."]
    if d["reasons"]:
        why.append(d["reasons"][0])
    if d["need_redesign"] or (d["status"] == "FIX" and er >= T.ER_KEEP and any(lv in ("fix", "retire") for lv in d["levels"].values())):
        rej = a.get("rejection") or {}
        reasons = rej.get("reasons") or {}
        top = max(reasons.items(), key=lambda kv: kv[1])[0] if reasons else None
        bad = [m for m, lv in d["levels"].items() if lv in ("fix", "retire")]
        what = ", ".join(T.EFFORT_LABELS[m] for m in bad)
        exp.update(kind="redesign", is_fix=0, name=f"Cut effort: {what}",
                   hypothesis="A small change to the review workflow brings the over-limit row back inside the Keep line without hurting ER.",
                   variable_changed="review workflow (not content)",
                   control="current workflow", treatment=REASON_FIX.get(top, "Log a reason category on every returned draft first, then pick the top one; there is not enough categorised data to name a fix."),
                   primary_metric=T.EFFORT_LABELS[bad[0]] if bad else "effort",
                   baseline_value=(a["effort"].get(bad[0], {}).get("value") if bad and bad[0] in a.get("effort", {}) else (rej.get("value") if "rejection_rate" in bad else None)))
        exp["success"] = ("The over-limit row is at or under its Keep line over the next 4 weeks AND median ER does not fall by more than a third. "
                          "This is the 'one redesign' that 6.3 step 3 asks for before a capacity retire-review.")
        notes.append("This is a process experiment, so the 4-post-per-arm rule does not apply; it needs the logged minutes (5+ units) or 5+ reviewed drafts to be scored.")
    else:
        clear = [c for c in contrasts if c["clear"]]
        if clear:
            c = max(clear, key=lambda c: (c["ratio"] if c["ratio"] is not None else 1e9))
            kind = {"format": "format", "pillar": "other", "hook_type": "hook"}[c["dim"]]
            label = {"format": "format", "pillar": "content pillar", "hook_type": "hook type"}[c["dim"]]
            exp.update(kind=kind, name=f"{label.capitalize()}: {c['best']} vs {c['worst']}",
                       hypothesis=f"Posts with {label} '{c['best']}' earn a higher median ER than '{c['worst']}' (seen so far: {ratio_text(c)}, n={c['best_n']} and {c['worst_n']}; observational, so confounded).",
                       variable_changed=label, control=f"'{c['worst']}' (the weaker group so far)", treatment=f"'{c['best']}'")
            why.append(f"The only clear contrast in the data is by {label}: {c['best']} {ratio_text(c)}. It is a hypothesis, not a finding, so the next step is to test it on purpose.")
        else:
            alts = ALT_FORMATS.get(platform, ())
            used = {x["format"] for x in posts if x.get("format")}
            if len(alts) >= 2 and len(used) < 2:
                other = next((f for f in alts if f not in used), alts[0])
                cur = next(iter(used), alts[0])
                exp.update(kind="format", name=f"Format: {cur} vs {other}", hypothesis=f"A {other} earns a different median ER than a {cur} on this account.",
                           variable_changed="format", control=f"{cur} (current)", treatment=other)
                why.append("The data has no clear contrast, and only one format has been used, so the cheapest informative change is the format (6.3 step 5 allows format, hook or platform).")
            else:
                exp.update(kind="hook", name=f"Hook: {HOOK_PAIR[0]} vs {HOOK_PAIR[1]}",
                           hypothesis="A first line that leads with a concrete number earns a different median ER than one that leads with a question.",
                           variable_changed="hook type (first line)", control=HOOK_PAIR[1], treatment=HOOK_PAIR[0])
                why.append("The data has no clear contrast (no group pair differs by 1.5x with 4+ posts each). The hook is the cheapest variable to change: it needs no new production.")
                if not any(x.get("hook_type") for x in posts):
                    notes.append("No post has a hook_type label yet. Start labelling hook_type in the posts import, or this experiment cannot be analysed.")
        exp["success"] = (f"Treatment median ER at least {T.GROUP_RATIO}x the control's, with at least {T.MIN_ARM_POSTS} posts per arm. Anything less is 'no clear difference' and the control stays. "
                          "Written before the data; no significance test is run at this sample size, so even a pass is a hypothesis for the next test.")
    exp["why"] = why
    exp["exp_id"] = next_exp_id(conn, snap["is_demo"])
    start = snap["as_of"]
    exp["start_date"] = start.isoformat()
    exp["end_date"] = (start + dt.timedelta(weeks=T.FIX_EXPERIMENT_WEEKS) - dt.timedelta(days=1)).isoformat()
    exp["a"], exp["p"] = a, p
    return exp, "", notes


def csv_row(exp):
    spec = tracker.SPECS["experiments"]
    cols = [c.name for c in spec.cols]
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(cols)
    w.writerow(["" if exp.get(c) is None else (round(exp[c], 5) if isinstance(exp.get(c), float) else exp.get(c)) for c in cols])
    return buf.getvalue()


# ---------------------------------------------------------------------------------------
# the report
# ---------------------------------------------------------------------------------------
MAX_LINES = 8
TREND_WORDS = {"rising": "rising", "flat": "flat", "falling2": "falling for 2 weeks", "falling3": "falling for 3 weeks", "unknown": "not enough weeks to tell"}


def build_report(conn, snap, show_all=False):
    as_of = snap["as_of"]
    demo = snap["is_demo"]
    L = []
    add = L.append
    bar = "=" * WIDTH
    if demo:
        add(bar)
        add("DEMO DATA: every number in this report was invented by analytics/demo_data.py. It is not evidence about any")
        add("persona, platform or audience. Do not quote it.")
        add(bar)
    add(f"WEEKLY REPORT, as of {as_of.isoformat()}  (the 7 days {as_of - dt.timedelta(days=7)} to {as_of - dt.timedelta(days=1)})")
    add("")
    add(wrap("Read this first: figures are medians of small samples (usually 8 to 15 posts per account). The minimum-sample rule (portfolio.md 6.1) is "
             f"{T.MIN_ORGANIC_POSTS} organic posts per platform in the scoring window; below that no status is given. Platforms are never compared on ER with each "
             "other. Statuses are indications for you to confirm; this report changes nothing.", 0, 0))
    add("")

    analysis = {}
    figs = {}
    for p in snap["personas"]:
        for a in p["accounts"]:
            analysis[(p["slug"], a["platform"])] = account_posts_for_analysis(conn, a, p["first_post"] if p["first_post_kind"] == "actual" else None, as_of)
            figs[(p["slug"], a["platform"])] = week_figures(conn, p, a, as_of)

    # ---- 1. where each account stands ----
    add("1. WHERE EACH ACCOUNT STANDS  (portfolio.md 6.3; the tree runs per persona x platform)")
    for p in snap["personas"]:
        if p["first_post_kind"] == "actual":
            add(f"  {name(p)}   week {p['week_now']}, first post {p['first_post']}")
        else:
            add(f"  {name(p)}   no post published yet (planned first post {p['first_post'] or 'not set'}; an assumption)")
        for a in p["accounts"]:
            d, s = a["decision"], a["summary"]
            label = metrics.T.STATUS_LABELS[d["status"]].upper() + (" (provisional)" if d["provisional"] else "")
            if d["status"] == "NOT_STARTED":
                add(wrap(f"{PLAT.get(a['platform'], a['platform'])}: {label}. Nothing to score yet.", 4, 4))
                continue
            er = f"median ER {pct(s['er'])}, " if s["er"] is not None and d["status"] in ("SCALE_ELIGIBLE", "KEEP", "FIX", "RETIRE_REVIEW") else ""
            if d["status"] in ("IN_PROGRESS", "EXTEND", "HOLD"):
                add(wrap(f"{PLAT.get(a['platform'], a['platform'])}: {label}. {s['n_scored']} organic posts with ER so far ({a.get('window_label', '')}).", 4, 4))
            else:
                add(wrap(f"{PLAT.get(a['platform'], a['platform'])}: {label}. {er}n={s['n_scored']} organic posts with ER, {a.get('window_label', '')}; reach {TREND_WORDS[a['reach_trend']]}.", 4, 4))
            if d["reasons"]:
                add(wrap(d["reasons"][0], 6, 0))
            for w in d["watch"]:
                add(wrap("WATCH: " + w, 6, 7))
        for al in p["alerts"]:
            add(wrap("ALERT: " + al, 4, 7))
    add("")

    # ---- 2 and 3. what worked, what did not (priority-ranked, capped unless --all) ----
    worked, failed = [], []
    best_posts, weak_posts, contrast_lines = [], [], []
    for p in snap["personas"]:
        fol_bits = []
        for a in p["accounts"]:
            key = (p["slug"], a["platform"])
            posts = analysis[key]
            f = figs[key]
            who = acct_name(p, a)
            d = a["decision"]
            scored_posts = [x for x in posts if x["er"] is not None]
            if len(scored_posts) >= T.MIN_ORGANIC_POSTS:
                best_posts.append(max(scored_posts, key=lambda x: (x["er"], x["post_id"])) | {"_who": who})
                weak_posts.append(min(scored_posts, key=lambda x: (x["er"], x["post_id"])) | {"_who": who})
            cs = [c for c in group_contrasts(posts) if c["clear"]]
            if cs:
                c = max(cs, key=lambda c: (c["ratio"] if c["ratio"] is not None else 1e9))
                label = {"format": "format", "pillar": "pillar", "hook_type": "hook type"}[c["dim"]]
                contrast_lines.append((c["ratio"] if c["ratio"] is not None else 99.0,
                                       f"{who}, by {label}: '{c['best']}' (n={c['best_n']}) against '{c['worst']}' (n={c['worst_n']}), median ER {ratio_text(c)}."))
            st = d["status"]
            if st in ("KEEP", "SCALE_ELIGIBLE"):
                worked.append((0, f"{who}: {metrics.T.STATUS_LABELS[st]}. Median ER {pct(a['summary']['er'])} over {a['summary']['n_scored']} posts"
                                  f"{' (provisional reading)' if d['provisional'] else ''}; reach trend {TREND_WORDS[a['reach_trend']]}."))
            if st in ("FIX", "RETIRE_REVIEW"):
                failed.append((1, f"{who}: {metrics.T.STATUS_LABELS[st]}. " + (d["reasons"][0] if d["reasons"] else "")))
            if a["reach_trend"] == "rising":
                vals = [a["reach_series"].get(w) for w in sorted(a["reach_series"])][-4:]
                worked.append((1, f"{who}: weekly {f['reach_field']} has risen over the last 3 weeks ({' > '.join(f'{v:,}' for v in vals if v is not None)})."))
            if a["reach_trend"] in ("falling2", "falling3"):
                vals = [a["reach_series"].get(w) for w in sorted(a["reach_series"])][-4:]
                failed.append((1, f"{who}: weekly {f['reach_field']} has fallen {'3 weeks' if a['reach_trend'] == 'falling3' else '2 weeks'} in a row ({' > '.join(f'{v:,}' for v in vals if v is not None)})."))
            if f["f_now"] is not None and f["f_prev"] is not None:
                delta = f["f_now"] - f["f_prev"]
                fol_bits.append(f"{PLAT.get(a['platform'], a['platform'])} {delta:+,}")
                if f["f_prev"] >= T.FOLLOWER_DROP_MIN_BASE and delta < -T.FOLLOWER_DROP * f["f_prev"]:
                    failed.append((1, f"{who}: followers fell {f['f_prev']:,} to {f['f_now']:,} this week (over 10%). Find the cause before the next post."))
            if f["n_this"] >= 3 and f["n_prev"] >= 3 and f["er_this"] is not None and f["er_prev"]:
                r = f["er_this"] / f["er_prev"]
                line = (f"{who}: this week's median ER {pct(f['er_this'])} (n={f['n_this']}) against {pct(f['er_prev'])} last week (n={f['n_prev']}), {r:.1f}x. "
                        "Two single weeks of about 3 posts are noise-prone; check the 4-week view before reacting.")
                if r >= T.GROUP_RATIO:
                    worked.append((4, line))
                elif r <= 1 / T.GROUP_RATIO:
                    failed.append((4, line))
            miss = a["summary"]["n_missing_metrics"]
            if miss:
                failed.append((2, f"DATA GAP {who}: {miss} published organic post(s) in the window have no metrics snapshot, so they are in no median. Import post_metrics for them."))
        if fol_bits:
            worked.append((4, f"{name(p)}: net followers this week {', '.join(fol_bits)}. Followers are recorded, not decided on."))
        accts = [a for a in p["accounts"]]
        if len(accts) == 2:
            a1, a2 = accts
            c1, c2 = a1["summary"]["common_per_1000_views"], a2["summary"]["common_per_1000_views"]
            paused = [PLAT[x["platform"]] for x in (a1, a2) if x["decision"]["status"] in ("PAUSE", "RETIRE")]
            if paused and c1 is not None and c2 is not None:
                worked.append((4, f"{name(p)}: platform comparison skipped because {', '.join(paused)} is paused (an open standing gate overrides the numbers)."))
            elif c1 is not None and c2 is not None and a1["summary"]["n_scored"] >= T.MIN_ORGANIC_POSTS and a2["summary"]["n_scored"] >= T.MIN_ORGANIC_POSTS:
                hi, lo = (a1, a2) if c1 >= c2 else (a2, a1)
                chi, clo = max(c1, c2), min(c1, c2)
                r = (chi / clo) if clo else None
                tag = {"sehuan": "H2", "fangcun": "H3"}.get(p["slug"], "context only")
                clear = r is None or r >= T.GROUP_RATIO
                if p["slug"] in ("sehuan", "fangcun"):
                    verdict = ("at least 1.5x, so the stronger platform is the one to keep and the weaker is a candidate to drop or hold (portfolio.md 4.2)" if clear
                               else "under 1.5x: not a clear difference, keep both")
                else:
                    # portfolio.md 6.1 allows this cross-platform metric only for H2 and H3; H4 is not a platform-versus-platform test
                    tag = "context only"
                    verdict = ("context only: portfolio.md 6.1 allows the cross-platform comparison for H2 and H3 only, so this decides nothing about keeping or dropping a platform")
                worked.append((1 if clear and p["slug"] in ("sehuan", "fangcun") else 3, f"{name(p)} {tag}, the one cross-platform metric (shares + comments per 1,000 views): {PLAT[hi['platform']]} {chi:.1f} against "
                                                  f"{PLAT[lo['platform']]} {clo:.1f}{'' if r is None else f' ({r:.1f}x)'}; {verdict}. Views are the only denominator all platforms are expected to report (unverified)."))
        rj = p["rejection"]
        if rj and rj["n"]:
            top = max(rj["reasons"].items(), key=lambda kv: kv[1])[0] if rj["reasons"] else "not categorised"
            if rj["value"] is not None and rj["value"] > T.EFFORT_LEVELS["rejection_rate"][1]:
                failed.append((1, f"{name(p)}: the wife returned {rj['rejected']} of {rj['n']} drafts on the first pass ({pct(rj['value'], 0)}; Keep needs 20% or less). Top reason: {top}."
                                  + ("" if rj["scored"] else f" Fewer than {T.MIN_REVIEWS_FOR_RATE} reviews, so this is not scored.")))
            elif rj["scored"] and rj["value"] is not None and rj["value"] <= T.EFFORT_LEVELS["rejection_rate"][0]:
                worked.append((2, f"{name(p)}: rejection rate {pct(rj['value'], 0)} ({rj['rejected']} of {rj['n']} drafts), inside the Scale line."))
        for m, e in (p["effort"] or {}).items():
            if e and e["scored"] and T.effort_level(m, e["value"]) in ("fix", "retire"):
                failed.append((1, f"{name(p)}: {T.EFFORT_LABELS[m]} is {e['value']:.1f} min (n={e['n']}), over the Keep line of {T.EFFORT_LEVELS[m][1]:g}."))
        lk = p["links"]
        if lk and lk["weekly"] and lk["weeks_with_clicks"] >= T.LINK_WEEKS_SCALE:
            worked.append((3, f"{name(p)}: link clicks in {lk['weeks_with_clicks']} of the first {min(6, lk['weeks_counted'])} weeks (Scale test is {T.LINK_WEEKS_SCALE} of 6). Reported separately from ER."))
    for r_, t in sorted(contrast_lines, key=lambda x: -x[0])[:3]:
        worked.append((2, "Pattern to test (hypothesis, not a result; it passes the 1.5x and " + str(T.MIN_GROUP_POSTS) + "-post rules): " + t))
    for x in sorted(best_posts, key=lambda x: -x["er"])[:2]:
        worked.append((3, f"Strongest single post: {x['_who']}, {x['post_id']} ({x['published_date']}, {x['format'] or 'format n/a'}) at ER {pct(x['er'])} on {x['er_rec']['denominator']:,} {x['er_rec']['denom_kind']}. One post is an anecdote."))
    for x in sorted(weak_posts, key=lambda x: x["er"])[:2]:
        failed.append((3, f"Weakest single post: {x['_who']}, {x['post_id']} ({x['published_date']}, {x['format'] or 'format n/a'}) at ER {pct(x['er'])} on {x['er_rec']['denominator']:,} {x['er_rec']['denom_kind']}. One post: compare it with its neighbours before changing anything."))
    cap = snap["capacity"]
    if cap.get("available") and not cap["pass"]:
        failed.append((1, f"Capacity gate (6.4) fails: operator {cap['operator_avg']:.0f} min/week (gate {cap['gate_operator']}), wife {cap['wife_avg']:.0f} (gate {cap['gate_wife']}), "
                          f"{cap['approvals_avg']:.1f} approvals/week (ceiling {cap['gate_approvals']}). No scaling step until it passes."))
    fin = snap["finance"]
    if fin["current"]["tool"] > fin["cap_base"]:
        failed.append((1, f"Tool spend this month {fin['current']['tool']:,.0f} is above the NT${fin['cap_base']:,} base cap."))
    open_events = [e for e in snap["standing"] if e["event_date"] <= as_of.isoformat() and (e["cleared_on"] is None or e["cleared_on"] > as_of.isoformat())]
    for e in open_events:
        label, hours, action = T.GATES[e["gate"]]
        days = (as_of - dt.date.fromisoformat(e["event_date"])).days
        failed.append((0, f"OPEN GATE {e['persona']}{'/' + e['platform'] if e['platform'] else ''}: {label}, since {e['event_date']} ({days} day(s) open). Rule: {action}."))

    cap_n = None if show_all else MAX_LINES

    def emit(title, items, empty):
        add(title)
        items = sorted(items, key=lambda t: t[0])
        if not items:
            add("  " + empty)
        shown = items if cap_n is None else items[:cap_n]
        for _, t in shown:
            add(bullet(t))
        if len(items) > len(shown):
            add(f"  ({len(items) - len(shown)} lower-priority line(s) hidden; run with --all to see them.)")
        add("")

    emit("2. WHAT WORKED", worked, "Nothing to report yet: not enough posts with metrics.")
    emit("3. WHAT DID NOT WORK", failed, "Nothing flagged this week.")

    add("4. ONE EXPERIMENT TO RUN NEXT  (rule-based suggestion; you decide)")
    exp, reason, notes = choose_experiment(snap, conn, analysis)
    running = [e for e in snap["experiments"] if e["status"] == "running"]
    for e in running:
        sofar = len([x for x in metrics.load_posts(conn, e["persona"], e["platform"], start=dt.date.fromisoformat(e["start_date"]), end=as_of - dt.timedelta(days=1))]) if e["platform"] else 0
        add(wrap(f"Already running: {e['exp_id']} ({e['persona']} {PLAT.get(e['platform'] or '', e['platform'] or '')}, {e['kind']}) {e['start_date']} to {e['end_date'] or 'open'}; "
                 f"{sofar} organic post(s) so far of {e['planned_posts'] or '?'} planned. Do not start another on that persona.", 2, 2))
    if exp is None:
        add(wrap(reason, 2, 2))
    else:
        add(f"  Experiment {exp['exp_id']}: {exp['name']}")
        add(wrap(f"Account: {acct_name(exp['p'], exp['a'])}. Kind: {exp['kind']}{' (this is the Fix experiment: its 4 weeks become the re-test window)' if exp['is_fix'] else ''}.", 4, 2))
        for w in exp["why"]:
            add(wrap("Why: " + w, 4, 5))
        add(wrap(f"Hypothesis: {exp['hypothesis']}", 4, 4))
        add(wrap(f"One variable only: {exp['variable_changed']}. Control: {exp['control']}. Treatment: {exp['treatment']}.", 4, 4))
        add(wrap(f"Run: {exp['start_date']} to {exp['end_date']} (4 weeks)" + ("" if exp["kind"] == "redesign" else f", at least {T.MIN_ARM_POSTS} posts per arm, alternating arms, same pillar and slot where possible") + ".", 4, 4))
        add(wrap(f"Primary metric: {exp['primary_metric']}. Baseline: {pct(exp['baseline_value']) if exp['baseline_value'] is not None and exp['baseline_value'] < 1 else exp['baseline_value']}.", 4, 4))
        add(wrap("Decision rule (fixed before the data): " + exp["success"], 4, 4))
        add(wrap("Stop early only for a Ground-rule or account-standing problem (portfolio.md 6.2). Change nothing else on this persona while it runs.", 4, 4))
        for n_ in notes:
            add(wrap("Note: " + n_, 4, 6))
        add("")
        add("    Paste-ready row for `python3 analytics/tracker.py import experiments FILE.csv` (check every field first):")
        for line in csv_row({**exp, "status": "planned"}).splitlines():
            add("      " + line)
    add("")

    # ---- 5. caveats ----
    add("5. SAMPLE-SIZE CAVEATS AND THE MINIMUM-SAMPLE RULE")
    for t in [
        f"Minimum sample: {T.MIN_ORGANIC_POSTS} organic posts per platform inside weeks 3 to 6 (extend to week 8, then hold). Sponsored posts are excluded from every median.",
        "A median of 8 to 15 posts moves when one or two posts change. Small accounts have few interactions per post, so ER moves in steps; the dashboard shows what one interaction is worth at each account's median reach.",
        f"A group (format, pillar, hook) is named only with {T.MIN_GROUP_POSTS}+ posts, and a difference is called clear only at {T.GROUP_RATIO}x or more. That is a screening rule, not a significance test; with these sizes false alarms are likely.",
        "Observed contrasts are confounded (different weeks, topics, reach), and looking at many groups finds a 1.5x gap by chance (the report names at most one pattern per account for that reason). Only a deliberate experiment with a written decision rule can support a change.",
        "Posts less than 7 days old can still gain reach and interactions; their latest snapshot may understate them.",
        "Platform metric availability (reach, saves, link clicks) in Taiwan is unverified (HUMAN_TODO 10). Threads and YouTube Shorts ER uses views and has no saves, so it is not comparable with Instagram.",
        "Every threshold is an assumption awaiting your confirmation (portfolio.md section 6 header). Recalibrate against each persona's own week-2 baseline before relying on a status.",
    ]:
        add(bullet(t))
    return "\n".join(L) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description="Print the weekly report: what worked, what did not, one experiment to run next.")
    ap.add_argument("--demo", action="store_true", help="use the DEMO database")
    ap.add_argument("--db", help="database file")
    ap.add_argument("--as-of", help="YYYY-MM-DD (default today; the DEMO database has its own date)")
    ap.add_argument("--out", help="also write the report to this file")
    ap.add_argument("--all", action="store_true", help="show every flagged line (default: the 8 highest-priority per list)")
    a = ap.parse_args(argv)
    db = Path(a.db) if a.db else (tracker.DEMO_DB if a.demo else tracker.REAL_DB)
    if db.exists():
        conn = tracker.connect(db, read_only=True)
    elif a.demo:
        print(f"{db} does not exist: run python3 analytics/demo_data.py first", file=sys.stderr)
        return 2
    else:
        conn = tracker.memory_db()
        print("(the real database does not exist yet: reporting on an empty tracker. Run python3 analytics/tracker.py init)\n")
    try:
        snap = metrics.portfolio_snapshot(conn, dt.date.fromisoformat(a.as_of) if a.as_of else None)
        text = build_report(conn, snap, a.all)
    finally:
        conn.close()
    print(text, end="")
    if a.out:
        Path(a.out).parent.mkdir(parents=True, exist_ok=True)
        Path(a.out).write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
