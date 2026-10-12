#!/usr/bin/env python3
"""schedule_check.py - merge the three pilots' 30-day posting slots, shift them with W0, and check them. Standard library only.
Makes NO network call, schedules nothing, publishes nothing and never edits any file.

    python3 launch/schedule_check.py                    # check with W0 = Mon 2026-11-16 (the assumption)
    python3 launch/schedule_check.py --w0 2026-11-30    # shift every slot by whole weeks (W0 must be a Monday)
    python3 launch/schedule_check.py --grid             # print the week-by-week grid (Markdown) used in schedule.md
    python3 launch/schedule_check.py --list             # print every post with its queue status
    python3 launch/schedule_check.py --with-deferred    # add back the 12 slots deferred by OPS-D1 (the superseded 18-a-week plan)
    python3 launch/schedule_check.py --no-post 2026-12-24 --no-post 2027-01-01   # add dates where nothing may publish

WHERE THE SLOTS COME FROM (read on 2026-10-12, not invented here): section 2 and the at-a-glance table (section 3) of
content/fangcun/calendar-30d.md, content/buzhou/calendar-30d.md and content/sehuan/calendar-30d.md. The three calendars were
written in parallel. If a calendar changes, edit ALL_SLOTS and DEFERRED below and re-run; the check is only as good as this table.

OPS-D1 (adopted on the user's behalf 2026-10-12, reversible, DECISIONS.md): the pilots are held at 12 approvals a week combined
(4 per pilot, 2 per platform) through the first 8 weeks. ALL_SLOTS is the superseded plan (66 slots, 18 approvals a week in weeks 3
and 4); DEFERRED lists the 12 slots in weeks 3 and 4 that are not scheduled; SLOTS = ALL_SLOTS minus DEFERRED (54 slots). The
deferred slots keep their calendar ids (nothing is renumbered). A deferred slot returns only if the ramp rule in
ops/weekly-routine.md 2.4 passes, with whole-week date moves; --with-deferred shows that plan and checks it.

WHAT IT CHECKS
  1. every slot's weekday matches its name (guards against a hand-edit error)
  2. no two personas post within MIN_GAP minutes of each other on the same date (studio rule: no same-hour posts, portfolio.md 3.3 item 6)
  3. nothing falls on a no-post date: the recalled polling day 2026-11-28 (UNVERIFIED), 228 (2027-02-28) and any --no-post date
  4. which posts sit inside 色環's own quiet block (polling day minus 1 to plus 1): decision D5 in launch/README.md
  5. approvals per week against the OPS-D1 hold of 12 and the planning ceiling of 22 (portfolio.md 5.1), and the operator and wife
     minutes per week against the 324 and 510 minute gates (portfolio.md 5.3 and 5.4), using the same assumption chain as portfolio.md.
     It also prints the operator's all-in figure with the routine's own overhead (ops/weekly-routine.md 2.3, Reading A). Neither figure
     includes the review of Claude-drawn graphics or the assembly of Reels and Shorts (the graphics decision): those are estimated in each
     calendar's section 8 and are NOT modelled here.
  6. for each post, the review-queue draft found (if any) and whether it is SCHEDULABLE under the approval gate. Only a human sets
     approval; this script only reads post.json.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import signal
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QUEUE = ROOT / "pipeline" / "review-queue"
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
MIN_GAP = 60  # minutes between two personas' posts on one date (studio rule; the three calendars keep at least 60)
CEILING_APPROVALS = 22  # portfolio.md 5.1
HELD_APPROVALS = 12  # OPS-D1 (adopted 2026-10-12): approvals a week, three pilots combined, through the first 8 weeks
# The routine's own weekly overhead in operator minutes (ops/weekly-routine.md 2.2 and 2.3, Reading A; all assumptions):
OPS_TREND, OPS_STATUS, OPS_LIVE_PER_POST, OPS_MONTHLY_AVG = 10, 10, 2, 21
OPERATOR_AVAILABLE = 360  # 6 hours a week (DECISIONS.md section 2 answer 2)
OPERATOR_GATE, WIFE_GATE = 324, 510  # portfolio.md 5.4
DEFAULT_W0 = dt.date(2026, 11, 16)

# Dates that are fixed in the calendar, not tied to W0 (culture.md 4; every one is computed or recalled, see that file).
FIXED_NO_POST = {
    dt.date(2026, 11, 28): "recalled polling day (UNVERIFIED: confirm with the Central Election Commission); portfolio.md: no post on an election day",
    dt.date(2027, 2, 28): "228 Peace Memorial Day: no post (portfolio.md 2.5)",
}
DATE_NOTES = {
    dt.date(2026, 11, 25): "統一發票 draw (方寸 posts no content)",
    dt.date(2026, 11, 27): "Black Friday: no sale wording",
    dt.date(2026, 12, 12): "雙12: no price, discount or sale wording",
    dt.date(2026, 12, 22): "冬至",
    dt.date(2026, 12, 25): "聖誕 / 行憲紀念日 (holiday status unverified)",
    dt.date(2026, 12, 31): "跨年",
    dt.date(2027, 1, 1): "元旦",
}
QUIET_BLOCK_OWNER = "sehuan"  # 色環's calendar keeps Fri to Sun around the recalled polling day quiet

# (persona, platform, week 0-4, weekday 0=Mon, "HH:MM", calendar id)
def _fc():
    ig, yt = "instagram", "youtube_shorts"
    return [
        ("fangcun", ig, 0, 0, "12:30", "P01"), ("fangcun", yt, 0, 1, "19:30", "P02"), ("fangcun", ig, 0, 3, "12:30", "P03"), ("fangcun", yt, 0, 4, "19:30", "P04"),
        ("fangcun", ig, 1, 0, "12:30", "P05"), ("fangcun", yt, 1, 1, "19:30", "P06"), ("fangcun", ig, 1, 3, "12:30", "P07"), ("fangcun", yt, 1, 4, "19:30", "P08"),
        ("fangcun", ig, 2, 0, "12:30", "P09"), ("fangcun", yt, 2, 1, "19:30", "P10"), ("fangcun", ig, 2, 3, "12:30", "P11"), ("fangcun", yt, 2, 4, "19:30", "P12"),
        ("fangcun", ig, 2, 5, "10:30", "P13"), ("fangcun", yt, 2, 6, "19:30", "P14"),
        ("fangcun", ig, 3, 0, "12:30", "P15"), ("fangcun", yt, 3, 1, "19:30", "P16"), ("fangcun", ig, 3, 3, "12:30", "P17"), ("fangcun", yt, 3, 4, "19:30", "P18"),
        ("fangcun", ig, 3, 5, "10:30", "P19"), ("fangcun", yt, 3, 6, "19:30", "P20"),
        ("fangcun", ig, 4, 0, "12:30", "P21"), ("fangcun", yt, 4, 1, "19:30", "P22"),
    ]


def _bz():
    th, yt = "threads", "youtube_shorts"
    plan = [(0, 3), (0, 6), (1, 3), (1, 6), (2, 1), (2, 3), (2, 6), (3, 1), (3, 3), (3, 6), (4, 1)]  # masters M1..M11
    out = []
    for i, (wk, wd) in enumerate(plan, 1):
        out.append(("buzhou", th, wk, wd, "08:15", f"T{i}"))
        out.append(("buzhou", yt, wk, wd, "21:00", f"S{i}"))
    return out


def _sh():
    ig, th = "instagram", "threads"
    plan = [  # (week, weekday, platform) in calendar order P01..P22; Instagram on Mon/Wed/Fri 20:30, Threads on Tue/Thu/Sat 18:00
        (0, 2, ig), (0, 3, th), (0, 4, ig), (0, 5, th),
        (1, 0, ig), (1, 1, th), (1, 2, ig), (1, 3, th),
        (2, 0, ig), (2, 1, th), (2, 2, ig), (2, 3, th), (2, 4, ig), (2, 5, th),
        (3, 0, ig), (3, 1, th), (3, 2, ig), (3, 3, th), (3, 4, ig), (3, 5, th),
        (4, 0, ig), (4, 1, th),
    ]
    return [("sehuan", p, wk, wd, "20:30" if p == ig else "18:00", f"P{i:02d}") for i, (wk, wd, p) in enumerate(plan, 1)]


ALL_SLOTS = _fc() + _bz() + _sh()  # the superseded plan: 22 slots per pilot, 66 in all (18 approvals a week in weeks 3 and 4)

# Deferred by OPS-D1 (12 slots, 6 in each of weeks 3 and 4; the third post on each platform of each pilot is the lowest-value first).
# Read from the three calendars on 2026-10-12; they must agree with this list (see launch/schedule.md section 7).
#   方寸 (fangcun): the weekend third posts, masters M7 and M10: P13 Sat IG, P14 Sun Short (week 3); P19 Sat IG, P20 Sun Short (week 4)
#   步驟 (buzhou):  masters M7 (Sun 2026-12-06) and M8 (Tue 2026-12-08): T7, S7, T8, S8 (the ids are not renumbered)
#   色環 (sehuan):  masters M5 (week 3) and M10 (week 4): P09 Mon IG, P10 Tue Threads; P19 Fri IG, P20 Sat Threads
DEFERRED = {
    ("fangcun", "P13"), ("fangcun", "P14"), ("fangcun", "P19"), ("fangcun", "P20"),
    ("buzhou", "T7"), ("buzhou", "S7"), ("buzhou", "T8"), ("buzhou", "S8"),
    ("sehuan", "P09"), ("sehuan", "P10"), ("sehuan", "P19"), ("sehuan", "P20"),
}
SLOTS = [s for s in ALL_SLOTS if (s[0], s[5]) not in DEFERRED]  # 54 slots, 12 approvals a week
NAMES = {"fangcun": "方寸", "buzhou": "步驟", "sehuan": "色環"}
SHORT = {"instagram": "IG", "threads": "Threads", "youtube_shorts": "YT Short"}


class Post:
    def __init__(self, persona, platform, week, wd, hhmm, cid, w0):
        self.persona, self.platform, self.cid, self.hhmm = persona, platform, cid, hhmm
        self.date = w0 + dt.timedelta(days=7 * week + wd)
        self.week, self.wd = week, wd
        self.minute = int(hhmm[:2]) * 60 + int(hhmm[3:])
        self.draft = None  # (folder, post.json dict) if a review-queue draft exists

    @property
    def approve_by(self) -> dt.date:
        """Thursday of the week before the post's own week (portfolio.md 5.5 weekly rhythm; the first batch needs a week more)."""
        monday = self.date - dt.timedelta(days=self.date.weekday())
        return monday - dt.timedelta(days=7) + dt.timedelta(days=3)


def attach_drafts(posts):
    for p in posts:
        base = QUEUE / p.persona
        if not base.exists():
            continue
        for folder in sorted(base.glob(f"{p.date.isoformat()}_*")):
            f = folder / "post.json"
            if f.exists():
                try:
                    d = json.loads(f.read_text(encoding="utf-8"))
                except Exception:
                    continue
                if d.get("platform") == p.platform:
                    p.draft = (folder, d)


def gate_state(p: Post) -> str:
    """Return a short status for the approval gate. Reads only; never decides approval."""
    if not p.draft:
        return "no draft"
    folder, d = p.draft
    r = d.get("review", {})
    media = d.get("media", [])
    pending = sum(1 for m in media if m.get("path") == "PENDING")
    notes = r.get("notes", "")
    hold = "HOLD" in notes or "BLOCKED" in notes
    if r.get("wife_language") == "approved" and r.get("operator_facts") == "approved" and r.get("approved") is True and pending == 0 and not hold:
        return "SCHEDULABLE"
    bits = []
    if r.get("wife_language") != "approved":
        bits.append("wife " + str(r.get("wife_language")))
    if r.get("operator_facts") != "approved":
        bits.append("operator " + str(r.get("operator_facts")))
    if r.get("approved") is not True:
        bits.append("not approved")
    if pending:
        bits.append(f"{pending} media PENDING")
    if hold:
        bits.append("HOLD/BLOCKED note")
    return "draft: " + ", ".join(bits)


def minutes(posts_in_week: list[Post]):
    """The portfolio.md 5.1 / 5.3 assumption chain. Masters: one idea per persona per platform pair."""
    approvals = len(posts_in_week)
    # One master (idea) feeds one post on each of a persona's two platforms, so masters = posts / 2 rounded up per persona;
    # the second post of each pair costs 3 wife minutes (portfolio.md 5.1, 5.3). 步驟 carries the extra 20 operator minutes per master.
    per_persona = {}
    for p in posts_in_week:
        per_persona.setdefault(p.persona, []).append(p)
    m_total, extra_variants, n7_masters = 0, 0, 0
    for persona, ps in per_persona.items():
        masters_p = (len(ps) + 1) // 2
        m_total += masters_p
        extra_variants += len(ps) - masters_p
        if persona == "buzhou":
            n7_masters = masters_p
    operator = 60 + 30 + 60 + 5 * approvals + 20 * n7_masters
    wife = 10 * m_total + 3 * extra_variants + 90 + 45 + 60 + 60 + 30
    return approvals, m_total, operator, wife


def build(w0: dt.date, extra_no_post: list[dt.date], with_deferred: bool = False):
    posts = [Post(*s, w0) for s in (ALL_SLOTS if with_deferred else SLOTS)]
    posts.sort(key=lambda p: (p.date, p.minute, p.persona))
    attach_drafts(posts)
    return posts


def all_in_operator(approvals: int, planned: int) -> int:
    """Operator minutes with the routine's own overhead (ops/weekly-routine.md 2.3, Reading A: the standup sits inside the admin line)."""
    return planned + OPS_TREND + OPS_STATUS + OPS_LIVE_PER_POST * approvals + OPS_MONTHLY_AVG


def run_checks(posts, w0, extra_no_post, quiet=False, with_deferred=False):
    errors, warns, infos = [], [], []
    if w0.weekday() != 0:
        errors.append(f"W0 {w0} is a {DAYS[w0.weekday()]}, not a Monday")
    for p in posts:
        if p.date.weekday() != p.wd:
            errors.append(f"{p.persona} {p.cid}: weekday mismatch on {p.date}")
    # 2. clock-hour clashes
    by_date = {}
    for p in posts:
        by_date.setdefault(p.date, []).append(p)
    closest = None
    for d, ps in sorted(by_date.items()):
        for i, a in enumerate(ps):
            for b in ps[i + 1:]:
                if a.persona == b.persona:
                    continue
                gap = abs(a.minute - b.minute)
                if gap < MIN_GAP:
                    errors.append(f"{d} {a.hhmm} {NAMES[a.persona]} {a.cid} and {b.hhmm} {NAMES[b.persona]} {b.cid} are {gap} min apart (rule: at least {MIN_GAP})")
                if closest is None or gap < closest[0]:
                    closest = (gap, d, a, b)
    if closest:
        g, d, a, b = closest
        infos.append(f"closest two personas: {g} min apart on {d} ({NAMES[a.persona]} {a.hhmm} and {NAMES[b.persona]} {b.hhmm})")
    # 3. no-post dates
    no_post = dict(FIXED_NO_POST)
    for d in extra_no_post:
        no_post[d] = "added with --no-post"
    for p in posts:
        if p.date in no_post:
            errors.append(f"{NAMES[p.persona]} {p.cid} {p.platform} is on {p.date}: {no_post[p.date]}")
    # 4. quiet block of 色環
    polling = dt.date(2026, 11, 28)
    block = {polling - dt.timedelta(days=1), polling, polling + dt.timedelta(days=1)}
    for p in posts:
        if p.date in block and p.persona != QUIET_BLOCK_OWNER:
            warns.append(f"{NAMES[p.persona]} {p.cid} {p.platform} {p.date} {p.hhmm} sits inside 色環's quiet block {min(block)} to {max(block)} (decision D5)")
    # 5. weekly load
    weeks = {}
    for p in posts:
        weeks.setdefault(p.week, []).append(p)
    load = []
    for wk in sorted(weeks):
        a, m, op, wf = minutes(weeks[wk])
        load.append((wk, a, m, op, wf))
        if a > CEILING_APPROVALS:
            errors.append(f"week {wk + 1}: {a} approvals is above the planning ceiling of {CEILING_APPROVALS}")
        if a > HELD_APPROVALS:
            msg = f"week {wk + 1}: {a} approvals is above the OPS-D1 hold of {HELD_APPROVALS} a week (the hold runs through week 8; a step up needs the ramp rule, ops/weekly-routine.md 2.4)"
            (warns if with_deferred else errors).append(msg)
        if op > OPERATOR_GATE:
            errors.append(f"week {wk + 1}: operator load {op} min is above the {OPERATOR_GATE} min gate")
        if wf > WIFE_GATE:
            errors.append(f"week {wk + 1}: wife load {wf} min is above the {WIFE_GATE} min gate")
    groups = {}  # operator all-in minutes -> full weeks with that figure (week 5 is a partial week and is not charged)
    for wk, a, m, op, wf in load:
        if wk < 4:
            groups.setdefault(all_in_operator(a, op), []).append(wk + 1)
    for total, wks in sorted(groups.items()):
        names = ", ".join(str(w) for w in wks)
        line = (f"weeks {names}: operator all-in with the routine's overhead = {total} min of 360 available (ops/weekly-routine.md 2.3, Reading A); "
                "excludes graphics review and video assembly (graphics decision, each calendar's section 8)")
        (warns if total > OPERATOR_AVAILABLE else infos).append(("OVER 360: " if total > OPERATOR_AVAILABLE else "") + line)
    # 6. gate state
    states = {}
    for p in posts:
        states[gate_state(p)] = states.get(gate_state(p), 0) + 1
    return errors, warns, infos, load, states


def print_grid(posts, w0):
    for wk in range(5):
        monday = w0 + dt.timedelta(days=7 * wk)
        print(f"\n**Week {wk + 1}: Mon {monday.isoformat()} to Sun {(monday + dt.timedelta(days=6)).isoformat()}**\n")
        print("| Day | Date | 方寸 | 步驟 | 色環 | Note |\n|---|---|---|---|---|---|")
        last = max((p.wd for p in posts if p.week == wk), default=6)
        for wd in range(last + 1 if wk == 4 else 7):  # the last week is printed only up to its last post
            d = monday + dt.timedelta(days=wd)
            cells = []
            for persona in ("fangcun", "buzhou", "sehuan"):
                ps = [p for p in posts if p.date == d and p.persona == persona]
                cells.append("<br>".join(f"{p.hhmm} {SHORT[p.platform]} {p.cid}" for p in ps) or "")
            note = []
            if d in FIXED_NO_POST:
                note.append("NO POST: " + ("recalled polling day, unverified" if d.year == 2026 else "228"))
            if d in DATE_NOTES:
                note.append(DATE_NOTES[d])
            print(f"| {DAYS[wd]} | {d.isoformat()} | " + " | ".join(cells) + " | " + "; ".join(note) + " |")


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--w0", default=DEFAULT_W0.isoformat(), help="Monday of the first week (default 2026-11-16, an assumption)")
    ap.add_argument("--no-post", action="append", default=[], help="extra date with no posting (YYYY-MM-DD)")
    ap.add_argument("--grid", action="store_true", help="print the week-by-week Markdown grid")
    ap.add_argument("--list", action="store_true", help="print every post with its review-queue status")
    ap.add_argument("--with-deferred", action="store_true", help="add back the 12 slots deferred by OPS-D1 (the superseded plan of 18 approvals a week in weeks 3 and 4)")
    a = ap.parse_args(argv)
    try:
        w0 = dt.date.fromisoformat(a.w0)
        extra = [dt.date.fromisoformat(x) for x in a.no_post]
    except ValueError as e:
        print(f"ERROR bad date (use YYYY-MM-DD): {e}", file=sys.stderr)
        return 2
    posts = build(w0, extra, a.with_deferred)
    if a.grid:
        print_grid(posts, w0)
        return 0
    if a.list:
        print("| Date | Day | Time | Persona | Platform | Calendar id | Approve by | Queue / gate |\n|---|---|---|---|---|---|---|---|")
        for p in posts:
            print(f"| {p.date} | {DAYS[p.wd]} | {p.hhmm} | {NAMES[p.persona]} | {SHORT[p.platform]} | {p.cid} | {p.approve_by} | {gate_state(p)} |")
        return 0
    errors, warns, infos, load, states = run_checks(posts, w0, extra, with_deferred=a.with_deferred)
    plan = "superseded plan with the 12 deferred slots" if a.with_deferred else "OPS-D1 hold at 12 approvals a week"
    print(f"W0 = {w0} ({DAYS[w0.weekday()]}); {len(posts)} posts from {posts[0].date} to {posts[-1].date}; {len(ALL_SLOTS)} slots in ALL_SLOTS, {len(DEFERRED)} deferred, {len(SLOTS)} in SLOTS; checking the {plan}")
    print("\nWeek  approvals  masters  operator min (gate %d)  wife min (gate %d)" % (OPERATOR_GATE, WIFE_GATE))
    for wk, ap_, m, op, wf in load:
        print(f"  {wk + 1}      {ap_:>3}       {m:>3}        {op:>4}                    {wf:>4}")
    print("\nReview-queue gate state of the %d slots:" % len(posts))
    for k, v in sorted(states.items(), key=lambda kv: -kv[1]):
        print(f"  {v:>3}  {k}")
    for m in infos:
        print("info ", m)
    for m in warns:
        print("WARN ", m)
    for m in errors:
        print("ERROR", m)
    print("\nRESULT:", "FAIL" if errors else "PASS", f"({len(errors)} error, {len(warns)} warn)")
    return 1 if errors else 0


if __name__ == "__main__":
    if hasattr(signal, "SIGPIPE"):
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)  # piping into head must not print a traceback
    sys.exit(main(sys.argv[1:]))
