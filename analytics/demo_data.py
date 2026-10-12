#!/usr/bin/env python3
"""demo_data.py - DEMO DATA GENERATOR.  EVERYTHING THIS WRITES IS MADE UP.

Purpose: let the tracker, dashboard and weekly report be tested before any real number exists.
  * Every id starts with DEMO- and every file is named DEMO_*.csv, so the real importer refuses them.
  * The demo database lives in analytics/data/demo/ and is flagged is_demo=1, so dashboard.py draws a
    "DEMO DATA" banner. The real database path (analytics/data/real/) is never touched.
  * Numbers are random draws from invented rates (seeded, so the output is reproducible). They are NOT
    benchmarks, forecasts or evidence of anything about Taiwan audiences or about these personas.
  * The story is deliberately varied so every branch of the decision tree has something to show:
    one Keep, three Fix (rate, effort), one Extend (too few posts), one Pause (open standing event).

Usage:  python3 analytics/demo_data.py [--out analytics/data/demo]
Then:   python3 analytics/dashboard.py --demo      (writes analytics/dashboard_demo.html)
        python3 analytics/weekly_report.py --demo
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import math
import random
import shutil
import sys
from pathlib import Path

import tracker

SEED = 20261116
W0 = dt.date(2026, 11, 16)          # Monday; the doc's ASSUMED first-post date
AS_OF = dt.date(2027, 1, 4)         # Monday of week 8
DATA_END = AS_OF - dt.timedelta(days=1)
DAY = dt.timedelta(days=1)
DEMO_DIR = tracker.HERE / "data" / "demo"
REAL_DIR = tracker.HERE / "data" / "real"

# account -> invented profile.  reach_week = invented weekly reach (or views where reach is not reported).
ACCOUNTS = {
    ("fangcun", "instagram"): dict(offsets=(0, 2, 4), er=0.0115, reach_week=[900, 1100, 1500, 1900, 2300, 2900, 3300],
                                   has_reach=True, has_saves=True, split=(0.55, 0.25, 0.20), followers_end=640,
                                   formats=["carousel", "carousel", "reel"], mult={"carousel": 1.2, "reel": 0.75}, post_share=0.7),
    ("fangcun", "youtube_shorts"): dict(offsets=(1, 3, 5), er=0.0050, reach_week=[400, 600, 800, 900, 1100, 1150, 1200],
                                        has_reach=False, has_saves=False, split=(0.0, 0.3, 0.7), followers_end=180,
                                        formats=["short"], mult={"short": 1.0}, post_share=0.8),
    ("buzhou", "youtube_shorts"): dict(offsets=(1, 3, 5), er=0.0085, reach_week=[700, 900, 1400, 1700, 1500, 1500, 1450],
                                       has_reach=False, has_saves=False, split=(0.0, 0.3, 0.7), followers_end=310,
                                       formats=["short"], mult={"short": 1.0}, post_share=0.8, n7=True),
    ("buzhou", "threads"): dict(offsets=(0, 3, 6), er=0.0070, reach_week=[300, 380, 500, 520, 300, 310, 330],
                                has_reach=False, has_saves=False, split=(0.0, 0.2, 0.8), followers_end=190,
                                formats=["text"], mult={"text": 1.0}, post_share=0.8,
                                thin_weeks={4: 1, 5: 1, 6: 1}, drop=(30, 0.14)),
    ("sehuan", "instagram"): dict(offsets=(0, 2, 4), er=0.0050, reach_week=[800, 1000, 1500, 1400, 1100, 900, 700],
                                  has_reach=True, has_saves=True, split=(0.5, 0.3, 0.2), followers_end=260,
                                  formats=["carousel", "reel"], mult={"carousel": 1.1, "reel": 0.85}, post_share=0.7),
    ("sehuan", "threads"): dict(offsets=(1, 4, 6), er=0.0072, reach_week=[250, 330, 450, 520, 600, 640, 700],
                                has_reach=False, has_saves=False, split=(0.0, 0.2, 0.8), followers_end=150,
                                formats=["image", "text"], mult={"image": 1.1, "text": 0.9}, post_share=0.8),
}
REACH_SCALE = 6        # invented: keeps interaction counts above single digits so the demo medians are not all zero
FOLLOWER_SCALE = 3
PILLARS = {"fangcun": ["A size arithmetic", "B checklists", "C layout compare"],
           "buzhou": ["A dated demos", "B doc digests", "C prompt templates"],
           "sehuan": ["A colour rules", "B climate layering", "C occasion dress codes"]}
PILLAR_MULT = [1.1, 1.0, 0.9]
HOOKS = {"number": 1.15, "question": 0.95, "how-to": 1.0, "claim": 0.85}
OPERATOR_MIN = {"fangcun": (5.0, 1.2), "buzhou": (6.0, 1.5), "sehuan": (7.0, 1.8)}      # (mean, sd) per approval
WIFE_MIN = {"fangcun": 9.0, "buzhou": 12.0, "sehuan": 14.0}                              # per master, all platforms
REJECT_P = {"fangcun": 0.12, "buzhou": 0.24, "sehuan": 0.08}
LINK_WEEKLY = {"fangcun": [0, 2, 4, 6, 7, 9, 8], "buzhou": [0, 0, 3, 0, 0, 5, 1], "sehuan": [0, 0, 0, 0, 2, 0, 0]}
AUDIENCE = {("fangcun", "instagram"): (0.62, 0.86), ("sehuan", "instagram"): (0.44, 0.82), ("buzhou", "youtube_shorts"): (0.55, 0.78)}


def poisson(rng, lam):
    if lam <= 0:
        return 0
    if lam > 30:
        return max(0, int(round(rng.gauss(lam, math.sqrt(lam)))))
    L, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= L:
            return k
        k += 1


def build():
    rows = {k: [] for k in tracker.IMPORT_ORDER}
    post_no = {}
    posts = []   # internal records
    for (persona, platform), cfg in ACCOUNTS.items():
        for week in range(1, 8):
            n = cfg.get("thin_weeks", {}).get(week, 2 if week <= 2 else 3)
            slots = {3: (0, 1, 2), 2: (0, 2), 1: (1,)}[n]
            for slot in slots:
                day = W0 + dt.timedelta(days=7 * (week - 1) + cfg["offsets"][slot])
                if day > DATA_END:
                    continue
                key = (persona, day)
                post_no[key] = post_no.get(key, 0) + 1
                posts.append(dict(persona=persona, platform=platform, cfg=cfg, week=week, slot=slot, day=day,
                                  pid=f"DEMO-{persona}-{day.isoformat()}-{post_no[key]:02d}",
                                  master=f"DEMO-M-{persona}-w{week}-s{slot}"))
    posts.sort(key=lambda p: (p["day"], p["pid"]))
    # a sponsored (gifted) post, to show that sponsored posts are kept out of the organic median
    gifted_pid = None
    for p in posts:
        if p["persona"] == "sehuan" and p["platform"] == "instagram" and p["day"] >= dt.date(2026, 12, 16):
            p["sponsorship"] = "gifted"
            gifted_pid = p["pid"]
            break

    # ---- posts and metrics ----
    final = {}
    for p in posts:
        cfg = p["cfg"]
        prng = random.Random(f"{SEED}:post:{p['pid']}")      # one stream per post, so tuning one account leaves the others alone
        fmt = prng.choice(cfg["formats"])
        pillar_i = prng.randrange(3)
        hook = prng.choice(list(HOOKS))
        npw = sum(1 for q in posts if q["persona"] == p["persona"] and q["platform"] == p["platform"] and q["week"] == p["week"])
        base_reach = cfg["reach_week"][p["week"] - 1] * REACH_SCALE * cfg["post_share"] / max(npw, 1)
        denom = max(25, int(base_reach * math.exp(prng.gauss(0, 0.30))))
        mult = cfg["mult"][fmt] * PILLAR_MULT[pillar_i] * HOOKS[hook]
        if p.get("sponsorship") == "gifted":
            mult *= 2.2
        total = poisson(prng, cfg["er"] * mult * denom)
        sv, sh, cm = cfg["split"]
        saves = poisson(prng, total * sv) if cfg["has_saves"] else None
        shares = poisson(prng, total * sh)
        comments = poisson(prng, total * cm)
        likes = poisson(prng, total * (9 if cfg["has_reach"] else 6))
        p.update(fmt=fmt, pillar=PILLARS[p["persona"]][pillar_i], hook=hook, denom=denom,
                 saves=saves, shares=shares, comments=comments, likes=likes)
        final[p["pid"]] = p
        rows["posts"].append(dict(
            post_id=p["pid"], persona=p["persona"], platform=p["platform"], master_id=p["master"], format=fmt,
            pillar="DEMO " + p["pillar"], hook_type=hook, scheduled_date=p["day"].isoformat(), published_date=p["day"].isoformat(),
            status="published", sponsorship_type=p.get("sponsorship", "none"), ai_label_on=1,
            url="", notes="DEMO post (invented)"))
        snaps = [(p["day"] + dt.timedelta(days=3), 0.75), (p["day"] + dt.timedelta(days=7), 1.0)]
        snaps = [(d, f) for d, f in snaps if d <= DATA_END]
        if not snaps:
            snaps = [(DATA_END, 0.5)]
        for d, f in snaps:
            r = dict(post_id=p["pid"], snapshot_date=d.isoformat())
            if cfg["has_reach"]:
                r["reach"] = int(round(denom * f))
                r["views"] = int(round(denom * 1.35 * f))
            else:
                r["views"] = int(round(denom * f))     # reach NOT reported: blank, not zero
            r["likes"] = int(round(likes * f))
            if cfg["has_saves"]:
                r["saves"] = int(round(saves * f))
            r["shares"] = int(round(shares * f))
            r["comments"] = int(round(comments * f))
            rows["post_metrics"].append(r)

    # ---- daily account rows ----
    by_day = {}
    for p in posts:
        by_day.setdefault((p["persona"], p["platform"], p["day"]), []).append(p)
    for (persona, platform), cfg in ACCOUNTS.items():
        drng = random.Random(f"{SEED}:daily:{persona}:{platform}")
        followers, ndays = 0, (DATA_END - W0).days + 1
        drop_day, drop_frac = cfg.get("drop", (None, None))
        for i in range(ndays):
            day = W0 + dt.timedelta(days=i)
            week = i // 7 + 1
            target_inc = cfg["followers_end"] * FOLLOWER_SCALE / ndays * (1.4 - 0.8 * i / ndays)
            followers += max(0, int(round(drng.gauss(target_inc, target_inc * 0.5))))
            if drop_day is not None and i == drop_day:
                followers = int(followers * (1 - drop_frac))
            wk_reach = cfg["reach_week"][week - 1] * REACH_SCALE / 7 * math.exp(drng.gauss(0, 0.15))
            r = dict(day=day.isoformat(), persona=persona, platform=platform, followers=followers)
            if cfg["has_reach"]:
                r["reach"] = int(wk_reach)
                r["views"] = int(wk_reach * 1.35)
            else:
                r["views"] = int(wk_reach)
            dayposts = by_day.get((persona, platform, day), [])
            r["likes"] = int(sum(x["likes"] for x in dayposts) * 1.2) + poisson(drng, 2)
            if cfg["has_saves"]:
                r["saves"] = int(sum(x["saves"] for x in dayposts) * 1.2) + poisson(drng, 0.5)
            r["shares"] = int(sum(x["shares"] for x in dayposts) * 1.2) + poisson(drng, 0.3)
            r["comments"] = int(sum(x["comments"] for x in dayposts) * 1.2) + poisson(drng, 0.4)
            r["real_person_comments"] = poisson(drng, 0.04)
            if persona == "buzhou" and platform == "youtube_shorts" and week == 7:
                r["real_person_comments"] = 1 if i % 7 in (0, 1, 2, 3, 4, 5) else 0
                if i % 7 == 6:
                    r["real_person_comments"] = 0
            if (persona, platform) in AUDIENCE and i % 7 == 6:
                r["target_age_share"], r["taiwan_share"] = AUDIENCE[(persona, platform)]
            rows["account_daily"].append(r)
    for persona, weekly in LINK_WEEKLY.items():
        lrng = random.Random(f"{SEED}:links:{persona}")
        for w, total in enumerate(weekly, start=1):
            if total == 0:
                days = [0] * 7
            else:
                days = [0] * 7
                for _ in range(total):
                    days[lrng.randrange(7)] += 1
            for j in range(7):
                day = W0 + dt.timedelta(days=7 * (w - 1) + j)
                if day <= DATA_END:
                    rows["account_daily"].append(dict(day=day.isoformat(), persona=persona, platform="linkpage", link_clicks=days[j]))

    # ---- effort log and review events ----
    masters_seen, acc = {}, {}
    for p in posts:
        erng = random.Random(f"{SEED}:effort:{p['pid']}")
        mean_, sd = OPERATOR_MIN[p["persona"]]
        before = p["day"] - dt.timedelta(days=3)
        rows["effort"].append(dict(ref=f"DEMO-eff-op-{p['pid']}", log_date=before.isoformat(), persona=p["persona"], post_id=p["pid"],
                                   master_id=p["master"], role="operator", task="approval",
                                   minutes=round(max(2.0, erng.gauss(mean_, sd)), 1), notes="DEMO"))
        primary = (p["persona"], p["master"]) not in masters_seen
        masters_seen[(p["persona"], p["master"])] = True
        w_mean = WIFE_MIN[p["persona"]]
        rows["effort"].append(dict(ref=f"DEMO-eff-wf-{p['pid']}", log_date=before.isoformat(), persona=p["persona"], post_id=p["pid"],
                                   master_id=p["master"], role="wife", task="master_review",
                                   minutes=round(max(3.0, erng.gauss(w_mean - 2.5 if primary else 2.5, 1.2 if primary else 0.5)), 1), notes="DEMO"))
        if p["persona"] == "buzhou" and p["platform"] == "youtube_shorts":
            rows["effort"].append(dict(ref=f"DEMO-eff-n7-{p['pid']}", log_date=before.isoformat(), persona="buzhou", post_id=p["pid"],
                                       master_id=p["master"], role="operator", task="n7_recording",
                                       minutes=round(max(12.0, erng.gauss(27, 5)), 1), notes="DEMO recording + claims check"))
        # first-pass review
        pc = REJECT_P[p["persona"]] * (1.8 if p["week"] <= 3 else 1.0)
        acc[p["persona"]] = acc.get(p["persona"], 0.0) + pc       # evenly spaced, so the demo rate is stable
        verdict = "approved"
        if acc[p["persona"]] >= 1.0:
            acc[p["persona"]] -= 1.0
            verdict = "changes"
        row = dict(ref=f"DEMO-rev-{p['pid']}", post_id=p["pid"], persona=p["persona"], platform=p["platform"],
                   reviewed_on=before.isoformat(), reviewer="wife", first_pass_verdict=verdict, near_miss=0, notes="DEMO")
        if verdict == "changes":
            cat = erng.choices(["language", "culture", "fact", "safety"], weights=[5, 2, 2, 1])[0]
            row["reason_category"] = cat
            row["near_miss"] = 1 if cat == "safety" else 0
        rows["reviews"].append(row)
    for w in range(1, 8):
        mon = W0 + dt.timedelta(days=7 * (w - 1))
        if mon + dt.timedelta(days=6) > DATA_END:
            pass
        for task, mins in (("admin", 60), ("analytics", 30), ("moderation", 60)):
            rows["effort"].append(dict(ref=f"DEMO-eff-op-{task}-w{w}", log_date=mon.isoformat(), role="operator", task=task, minutes=mins, notes="DEMO weekly fixed time"))
        for task, mins in (("moderation", 90), ("admin", 60), ("other", 75)):
            rows["effort"].append(dict(ref=f"DEMO-eff-wf-{task}-w{w}", log_date=mon.isoformat(), role="wife", task=task, minutes=mins, notes="DEMO weekly fixed time"))

    # ---- money, leads, standing, experiments (all invented) ----
    for ref, d, kind, cat, desc, amt in [
        ("DEMO-cost-01", "2026-10-28", "one_time", "registration", "DEMO: business registration fee (invented amount)", 1500),
        ("DEMO-cost-02", "2026-11-05", "tool", "image_api", "DEMO: image API usage, November", 1450),
        ("DEMO-cost-03", "2026-11-06", "tool", "design_tool", "DEMO: design tool", 450),
        ("DEMO-cost-04", "2026-11-10", "tool", "domain", "DEMO: link page domain", 300),
        ("DEMO-cost-05", "2026-12-05", "tool", "image_api", "DEMO: image API usage, December", 1900),
        ("DEMO-cost-06", "2026-12-06", "tool", "design_tool", "DEMO: design tool", 450),
        ("DEMO-cost-07", "2027-01-03", "tool", "image_api", "DEMO: image API usage, January so far", 600),
    ]:
        rows["costs"].append(dict(ref=ref, cost_date=d, cost_kind=kind, category=cat, description=desc, amount_twd=amt, notes="DEMO"))
    rows["revenue"].append(dict(ref="DEMO-rev-01", revenue_date="2026-12-22", persona="fangcun", source_type="affiliate", amount_twd=185,
                                status="received", counterparty="DEMO programme", notes="DEMO"))
    rows["revenue"].append(dict(ref="DEMO-rev-02", revenue_date="2026-12-29", persona="sehuan", source_type="b2b_creative", amount_twd=4000,
                                status="invoiced", counterparty="DEMO brand", notes="DEMO invoice not yet paid"))
    for i, d in enumerate(["2026-12-02", "2026-12-04", "2026-12-08", "2026-12-10", "2026-12-15"]):
        rows["lead_signals"].append(dict(ref=f"DEMO-lead-s{i}", signal_date=d, persona="sehuan", kind="outreach_sent", notes="DEMO"))
    rows["lead_signals"].append(dict(ref="DEMO-lead-s5", signal_date="2026-12-20", persona="sehuan", kind="accepted_free_sample", notes="DEMO"))
    for i, d in enumerate(["2026-12-03", "2026-12-09", "2026-12-17"]):
        rows["lead_signals"].append(dict(ref=f"DEMO-lead-f{i}", signal_date=d, persona="fangcun", kind="outreach_sent", notes="DEMO"))
    rows["lead_signals"].append(dict(ref="DEMO-lead-f3", signal_date="2027-01-02", persona="fangcun", kind="written_enquiry", notes="DEMO"))
    rows["standing"].append(dict(ref="DEMO-stand-1", event_date="2026-12-01", persona="fangcun", platform="instagram", gate="garbled_or_wrong",
                                 description="DEMO: an on-image text defect found after publishing", action_taken="DEMO: corrected within 24 hours",
                                 cleared_on="2026-12-02"))
    rows["standing"].append(dict(ref="DEMO-stand-2", event_date="2027-01-02", persona="sehuan", platform="threads", gate="disclosure_failure",
                                 description="DEMO: paid-partnership tag missing on a gifted-item post", action_taken="", cleared_on=""))
    rows["experiments"].append(dict(
        exp_id="DEMO-E001", persona="fangcun", platform="instagram", kind="hook", is_fix=0, name="DEMO number-first hook vs question hook",
        hypothesis="DEMO: a number in the first line earns more saves", variable_changed="hook type", control="question hooks", treatment="number hooks",
        start_date="2026-12-07", end_date="2026-12-27", planned_posts=8, status="done", primary_metric="median ER",
        baseline_value=0.0102, result_value=0.0116, sample_n=9, decision="No clear difference (1.14x, under the 1.5x rule). Keep both.", notes="DEMO"))
    rows["experiments"].append(dict(
        exp_id="DEMO-E002", persona="fangcun", platform="youtube_shorts", kind="format", is_fix=1, name="DEMO Shorts cut length 25 s vs 45 s",
        hypothesis="DEMO: shorter cuts raise shares per view", variable_changed="video length", control="45 s", treatment="25 s",
        start_date="2026-12-28", end_date="2027-01-25", planned_posts=12, status="running", primary_metric="median ER (views)",
        baseline_value=0.0045, notes="DEMO Fix experiment started at the week-6 review"))
    rows["experiments"].append(dict(
        exp_id="DEMO-E003", persona="buzhou", platform="youtube_shorts", kind="redesign", is_fix=0, name="DEMO record two demos per sitting",
        hypothesis="DEMO: batching recordings cuts the N7 minutes per master", variable_changed="recording workflow", control="one demo per sitting",
        treatment="two per sitting", start_date="2027-01-05", planned_posts=6, status="planned", primary_metric="N7 minutes per master",
        baseline_value=32, notes="DEMO planned redesign"))
    return rows, gifted_pid


def write_csvs(rows, out_dir: Path):
    csv_dir = out_dir / "csv"
    if csv_dir.exists():
        shutil.rmtree(csv_dir)
    csv_dir.mkdir(parents=True)
    paths = {}
    for kind, items in rows.items():
        if not items:
            continue
        cols = [c.name for c in tracker.SPECS[kind].cols]
        p = csv_dir / f"DEMO_{kind}.csv"
        with open(p, "w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=cols, extrasaction="raise")
            w.writeheader()
            for r in items:
                w.writerow({k: ("" if v is None else v) for k, v in r.items()})
        paths[kind] = p
    return paths


def build_demo(out_dir: Path = DEMO_DIR):
    out_dir = Path(out_dir).resolve()
    if REAL_DIR.resolve() in (out_dir, *out_dir.parents):
        raise SystemExit("refusing to write DEMO data inside analytics/data/real/ (that folder stays empty until real data)")
    out_dir.mkdir(parents=True, exist_ok=True)
    rows, gifted = build()
    paths = write_csvs(rows, out_dir)
    db_path = out_dir / "tracker.db"
    for suffix in ("", "-journal", "-wal", "-shm"):
        f = Path(str(db_path) + suffix)
        if f.exists():
            f.unlink()
    conn = tracker.init_db(db_path, demo=True)
    tracker.set_meta(conn, "is_demo", "1")
    tracker.set_meta(conn, "demo_as_of", AS_OF.isoformat())
    tracker.set_meta(conn, "demo_note", "DEMO DATA: every number is invented by analytics/demo_data.py")
    summary = []
    for kind in tracker.IMPORT_ORDER:
        if kind in paths:
            res = tracker.import_csv(conn, kind, paths[kind])
            if res.errors:
                raise SystemExit(f"demo import failed for {kind}: {res.errors[:3]}")
            summary.append(res.summary())
    conn.close()
    return db_path, summary


def main(argv=None):
    ap = argparse.ArgumentParser(description="Generate DEMO data (invented) for testing the analytics tools.")
    ap.add_argument("--out", default=str(DEMO_DIR))
    a = ap.parse_args(argv)
    db, summary = build_demo(Path(a.out))
    print("DEMO DATA written (all numbers invented).")
    print("database:", db)
    for s in summary:
        print("  ", s)
    print("as-of date for the demo:", AS_OF.isoformat())
    return 0


if __name__ == "__main__":
    sys.exit(main())
