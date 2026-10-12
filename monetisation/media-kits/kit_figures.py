#!/usr/bin/env python3
"""kit_figures.py - print the tracker figures a media kit needs for one period. Read-only; standard library only; no network.

    python3 -B monetisation/media-kits/kit_figures.py --start 2026-12-01 --end 2026-12-28
    python3 -B monetisation/media-kits/kit_figures.py --persona fangcun --start 2026-12-01 --end 2026-12-28
    python3 -B monetisation/media-kits/kit_figures.py --demo --start 2026-12-01 --end 2026-12-28   # DEMO data, never for a kit

What it does: opens the tracker database (default analytics/data/real/tracker.db) READ-ONLY and prints, per persona and platform,
the numbers for section 10.1 and 10.4 of a kit (and section 8 of studio.md) over the dates you give, using the tracker's own
definitions (analytics/metrics.py: organic posts only, ER = (saves + shares + comments) / reach, likes excluded, latest snapshot).

What it does not do: it never writes, never fills a kit, and cannot see anything a platform did not export. Three things always
come from a dated platform screenshot instead (README.md section 5):
  * the period's reach or views total (a sum of daily unique reach would count one person many times),
  * the audience panels (age, gender, cities),
  * anything the tracker shows as blank. Blank means "not reported by platform", never 0.
Every number printed here is only as good as the CSVs that were imported. Check two or three against the screenshots.
"""
from __future__ import annotations

import argparse
import datetime as dt
import sys
from pathlib import Path
from statistics import median

sys.dont_write_bytecode = True

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / "analytics"))

try:
    import metrics  # type: ignore  # noqa: E402
    import tracker  # type: ignore  # noqa: E402
except Exception as exc:  # pragma: no cover
    print(f"cannot import the analytics modules from {ROOT / 'analytics'}: {exc}")
    sys.exit(2)

PILOTS = ["fangcun", "buzhou", "sehuan"]
NOT_REPORTED = "not reported by platform"


def fmt(x, pct=False):
    if x is None:
        return NOT_REPORTED
    if pct:
        return f"{x * 100:.2f}%"
    if isinstance(x, float) and not x.is_integer():
        return f"{x:.1f}"
    return f"{int(x):,}"


def med(xs):
    xs = [x for x in xs if x is not None]
    return median(xs) if xs else None


def accounts_for(conn, persona):
    return [r["platform"] for r in conn.execute(
        "SELECT platform FROM accounts WHERE persona=? AND platform != 'linkpage' ORDER BY role='primary' DESC, platform", (persona,))]


def account_block(conn, persona, platform, start, end):
    out = [f"  [{persona} / {platform}]"]
    org = metrics.load_posts(conn, persona, platform, start, end, organic=True)
    allp = metrics.load_posts(conn, persona, platform, start, end, organic=False)
    spons = [p for p in allp if p["sponsorship_type"] != "none"]
    out.append(f"    posts published in the period: {len(allp)} (organic {len(org)}, sponsored/gifted/affiliate {len(spons)})")
    summ = metrics.summarise_posts(org)
    out.append(f"    organic posts with a computable ER: {summ['n_scored']} of {summ['n_published']}"
               f"; {summ['n_missing_metrics']} have no metrics snapshot yet")
    if summ["n_scored"] < 8:
        out.append("    NOTE: fewer than 8 organic posts with metrics. The tracker's rule is that this is too few to score; "
                   "show the numbers only with that stated, or leave the row empty.")
    for field in ("saves", "shares", "comments"):
        vals = [p[field] for p in org]
        rep = [v for v in vals if v is not None]
        out.append(f"    median {field} per organic post: {fmt(med(vals))}  (reported for {len(rep)} of {len(vals)} posts)")
    out.append(f"    median ER, studio definition: {fmt(summ['er'], pct=True)}"
               f"  (denominator: {', '.join(summ['denominators']) or 'n/a'}; terms: {', '.join(summ['terms']) or 'n/a'})")
    if summ["n_young"]:
        out.append(f"    NOTE: {summ['n_young']} scored post(s) were read less than 7 days after publishing; their numbers may be low.")
    row = conn.execute("""SELECT day, followers FROM account_daily WHERE persona=? AND platform=? AND day BETWEEN ? AND ?
                          AND followers IS NOT NULL ORDER BY day DESC LIMIT 1""", (persona, platform, start.isoformat(), end.isoformat())).fetchone()
    out.append(f"    followers/subscribers at the last recorded day in the period: "
               + (f"{row['followers']:,} on {row['day']}" if row else NOT_REPORTED) + "  (the period end itself may differ; check the screenshot)")
    lab = conn.execute("""SELECT SUM(ai_label_on=1) on_, SUM(ai_label_on=0) off_, SUM(ai_label_on IS NULL) unk, COUNT(*) n FROM posts
                          WHERE persona=? AND platform=? AND status='published' AND published_date BETWEEN ? AND ?""",
                       (persona, platform, start.isoformat(), end.isoformat())).fetchone()
    if lab["n"]:
        out.append(f"    platform AI label recorded on: {lab['on_'] or 0} of {lab['n']} published posts"
                   f" (off: {lab['off_'] or 0}, not recorded: {lab['unk'] or 0})")
    ev = conn.execute("""SELECT event_date, gate, platform, cleared_on FROM standing_events WHERE persona=?
                         AND (platform=? OR platform IS NULL) AND event_date BETWEEN ? AND ? ORDER BY event_date""",
                      (persona, platform, start.isoformat(), end.isoformat())).fetchall()
    out.append(f"    standing events logged in the period: {len(ev)}"
               + ("" if not ev else " -> " + "; ".join(f"{e['event_date']} {e['gate']}" + ("" if e['cleared_on'] else " (open)") for e in ev)))
    if spons:
        out.append("    sponsored / gifted / affiliate posts (for section 10.4; a brand may be named only with written permission):")
        for p in spons:
            out.append(f"      {p['published_date']}  {p['post_id']}  type={p['sponsorship_type']}  url={p['url'] or '(none recorded)'}")
    return out, len(allp), len(spons), len(ev)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Print tracker figures for a media-kit period (read-only).")
    ap.add_argument("--start", required=True, help="YYYY-MM-DD, first day of the period")
    ap.add_argument("--end", required=True, help="YYYY-MM-DD, last day of the period")
    ap.add_argument("--persona", choices=PILOTS, help="one persona (default: all three pilots)")
    ap.add_argument("--db", help="database file (default: the real database)")
    ap.add_argument("--demo", action="store_true", help="use the DEMO database; its numbers are invented and must never go in a kit")
    a = ap.parse_args(argv)
    try:
        start, end = dt.date.fromisoformat(a.start), dt.date.fromisoformat(a.end)
    except ValueError:
        print("dates must be YYYY-MM-DD")
        return 2
    if end < start:
        print("--end is before --start")
        return 2
    db = Path(a.db) if a.db else (tracker.DEMO_DB if a.demo else tracker.REAL_DB)
    if not db.exists():
        print(f"database not found: {db}\nNothing has been imported yet, so there is nothing to put in a kit. "
              f"(Real data: python3 analytics/tracker.py init, then import the CSVs; see analytics/README.md.)")
        return 1
    conn = tracker.connect(db, read_only=True)
    try:
        return report(conn, db, a, start, end)
    finally:
        conn.close()


def report(conn, db, a, start, end):
    demo = tracker.is_demo(conn)
    if demo and not a.demo:
        print("This database is flagged DEMO. Its numbers are invented. Use --demo to look at it, and never copy from it into a kit.")
        return 1
    print(f"kit_figures: {db.relative_to(ROOT) if db.is_relative_to(ROOT) else db}")
    print(f"period: {start} to {end}  (generated {dt.date.today()})")
    if demo:
        print("*** DEMO DATA: invented numbers. NOT FOR A KIT. ***")
    print("Definitions: organic posts only; ER = (saves + shares + comments) / reach, likes excluded; latest snapshot per post.")
    print("Reach/views period totals, audience panels and anything shown as blank come from platform screenshots, not from here.\n")
    personas = [a.persona] if a.persona else PILOTS
    tot_posts = tot_spons = tot_ev = 0
    for p in personas:
        plats = accounts_for(conn, p)
        print(f"{p}:")
        if not plats:
            print("  no accounts in the tracker\n")
            continue
        for pl in plats:
            lines, n, s, e = account_block(conn, p, pl, start, end)
            print("\n".join(lines))
            tot_posts += n
            tot_spons += s
            tot_ev += e
        print()
    print("studio level (section 8 of studio.md):")
    print(f"  posts published in the period, all pilots and platforms: {tot_posts}")
    print(f"  of which sponsored / gifted / affiliate: {tot_spons}")
    print(f"  standing events logged in the period: {tot_ev}")
    print("  public corrections: not tracked in the tracker; count the 【更正】 lines you added from your own correction list (README.md section 5).")
    print("  date of the first post: " + ", ".join(
        f"{p}={(metrics.first_post(conn, p)[0] or 'none')}{'' if metrics.first_post(conn, p)[1] == 'actual' else ' (assumed, not a real post)'}" for p in personas))
    return 0


if __name__ == "__main__":
    sys.exit(main())
