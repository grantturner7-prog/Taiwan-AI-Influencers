#!/usr/bin/env python3
"""Offline checks for the 色環 (sehuan) content and review-queue drafts.

Run from the repository root:   python3 content/sehuan/verify.py

Standard library only. No network calls. It reuses the pipeline's word scanner (pipeline/scripts/ground_rules.py) so the
content files and `queue.py validate` apply the same net. This script is a first-pass filter for the operator and for Claude,
NOT a replacement for the wife's review: it cannot judge tone, naturalness or Taiwan vocabulary beyond the word lists, and it
does not check any fact against a source.

Update of 2026-10-12 (decisions D6, OPS-D1 and D3 in DECISIONS.md "recommended answers adopted"): the capacity arithmetic of
calendar section 8 is asserted; the 30-day table in calendar section 3 must respect the OPS-D1 cadence (at most 2 Instagram and
2 Threads posts a week, at least 2 Instagram posts in each of weeks 1 to 4, 18 posts in all, none of the deferred P09, P10, P19,
P20 scheduled; section 6.1 must list exactly those four); a Reel or Short draft (none exists) must carry the four D6 conditions in
review.notes; a lesson-graphic item must name its route (drawn by Claude as SVG) and no section-5 text may still say human-built.
None of this approves anything.

Exit code 0 = no errors; 1 = at least one error. Warnings are printed but do not fail the run.
"""
import datetime as dt
import glob
import json
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "pipeline", "scripts"))
import ground_rules as gr  # noqa: E402

QUEUE = os.path.join(ROOT, "pipeline", "review-queue", "sehuan", "*", "post.json")
CAL = os.path.join(ROOT, "content", "sehuan", "calendar-30d.md")
HOOKS = os.path.join(ROOT, "content", "sehuan", "hook-library.md")
REPLIES = os.path.join(ROOT, "content", "sehuan", "reply-guidelines.md")
TEXT_FILES = [os.path.join(ROOT, "content", "sehuan", n) for n in
              ("calendar-30d.md", "hook-library.md", "series.md", "trend-check.md", "reply-guidelines.md", "b2b-pitch.md")]

errors, warnings = [], []


def read_text(path):
    """Read a UTF-8 text file; report (not crash) when it is missing or not UTF-8."""
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    except (OSError, UnicodeDecodeError) as e:
        err("cannot read %s: %s" % (os.path.relpath(path, ROOT), e))
        return None


def err(m):
    errors.append(m)


def warn(m):
    warnings.append(m)


def scan(label, text, allow_info=True):
    for f in gr.scan_text(text, label):
        if f.level in ("ERROR", "FLAG"):
            err("%s: %s %s" % (label, f.code, f.message))
        elif f.level == "WARN":
            warn("%s: %s %s" % (label, f.code, f.message))


def expect(cond, msg):
    """Explicit check (an `assert` would vanish under python -O)."""
    if not cond:
        err("arithmetic/date check failed: " + msg)


def check_arithmetic():
    expect(6 + 3 + 1 == 10 and 60 + 30 + 10 == 100, "6:3:1 and 60/30/10")
    expect(50 * 2 == 100, "50 x 2")
    expect(round(0.035 * 1350) == 47 and round(0.08 * 1080) == 86 and round(0.08 * 1350) == 108, "badge sizes")
    expect(2 * 60 + 2 * 15 == 150 and 150 + 4 * 5 == 170 and round(170 / 360 * 100) == 47, "weekly build minutes")
    expect(2 * 10 + 2 * 3 == 26 and 26 + 2 * 7 == 40, "wife minutes")
    expect(sum((4, 3, 2, 2)) == 11, "pillar mix total (v0.1, before OPS-D1)")
    expect([round(x / 11 * 100) for x in (4, 3, 2, 2)] == [36, 27, 18, 18], "pillar mix percentages (v0.1)")
    # OPS-D1: 9 masters left after M5 and M10 are deferred
    expect(sum((3, 2, 2, 2)) == 9 and 11 - 2 == 9, "pillar mix total after OPS-D1")
    expect([round(x / 9 * 100) for x in (3, 2, 2, 2)] == [33, 22, 22, 22], "pillar mix percentages after OPS-D1")
    expect(abs(33 - 39) + abs(22 - 22) + abs(22 - 22) + abs(22 - 17) == 11 and abs(44 - 39) + 0 + 0 + abs(11 - 17) == 11,
           "section 6.1: both candidate cuts are 11 points from the bible mix")
    expect(4 + 4 + 4 + 4 + 2 == 18 and 4 + 4 + 6 + 6 + 2 == 22 and 22 - 4 == 18 and 3 * 4 == 12 and 3 * 6 == 18,
           "posts per week before and after OPS-D1")
    # capacity, calendar section 8 (assumptions: 20 min per carousel review, 5 per card; low case 10 and 3)
    expect(2 * 60 + 2 * 15 == 150 and 150 + 4 * 5 == 170 and 3 * 60 + 3 * 15 == 225 and 225 + 6 * 5 == 255, "v0.1 build load")
    expect(round(255 / 360 * 100) == 71, "v0.1 weeks 3 and 4 share")
    expect(3 * 20 + 3 * 5 == 75 and 75 + 30 == 105 and round(105 / 360 * 100) == 29, "D3 only, 3 + 3")
    expect(2 * 20 + 2 * 5 == 50 and 50 + 4 * 5 == 70 and round(70 / 360 * 100) == 19, "now, planning case")
    expect(2 * 10 + 2 * 3 == 26 and 26 + 20 == 46 and round(46 / 360 * 100) == 13, "now, low case")
    expect(255 - 105 == 150 and 105 - 70 == 35 and 255 - 70 == 185 and 170 - 70 == 100, "savings by decision")
    expect(20 + 5 + 2 * 5 == 35 and 4 * 70 + 35 == 315 and 2 * 170 + 2 * 255 + (60 + 15 + 2 * 5) == 935, "30-day totals")
    expect(round(935 / 60, 1) == 15.6 and 315 / 60 == 5.25 and 5 * 60 - 60 == 240, "hours")
    expect(70 / 4 == 17.5 and 46 / 4 == 11.5, "all-in minutes per approval")
    expect(round(50 / 110 * 100) == 45 and 110 - 50 == 60 and 60 - 36 == 24, "share of the 110 minutes of slack")
    expect(3 * 50 == 150 and 150 > 110 and 3 * 26 == 78 and 78 < 110 and 110 - 36 == 74 and 78 > 74, "three pilots against the slack")
    expect(3 * 10 + 3 * 3 == 39 and 3 * 7 == 21 and 39 + 21 == 60 and 2 * 10 + 2 * 3 == 26 and 2 * 7 == 14 and 26 + 14 == 40,
           "wife minutes, 3 + 3 against 2 + 2")
    expect(round(20 * 5 / 7) == 14 and 20 - round(20 * 5 / 7) == 6 and round(2 / 7 * 100) == 29, "five-slide carousel")
    w0 = dt.date(2026, 11, 16)
    expect(w0.strftime("%a") == "Mon" and dt.date(2026, 11, 28).strftime("%a") == "Sat", "W0 Mon / polling day Sat")
    expect(dt.date(2026, 12, 12).strftime("%a") == "Sat" and (w0 + dt.timedelta(days=29)).isoformat() == "2026-12-15", "day 30")
    expect(dt.date(2027, 1, 23).strftime("%a") == "Sat" and dt.date(2026, 12, 28).strftime("%a") == "Mon", "weekdays")
    expect(dt.date(2026, 11, 27).strftime("%a") == "Fri" and dt.date(2026, 11, 29).strftime("%a") == "Sun", "quiet block")


def check_json():
    required = ["id", "persona", "platform", "format", "scheduled_date", "pillar", "hook_zh", "caption_zh",
                "caption_gloss_en", "hashtags", "on_screen_label_zh", "ai_label_flag", "sponsorship_flag",
                "sponsorship_type", "sources", "media", "review"]
    files = sorted(glob.glob(QUEUE))
    if len(files) != 8:
        err("expected 8 sehuan drafts, found %d" % len(files))
    quiet = {"2026-11-27", "2026-11-28", "2026-11-29"}
    cal_text = read_text(CAL)
    dates = []
    for f in files:
        label = os.path.basename(os.path.dirname(f))
        try:
            with open(f, encoding="utf-8") as fh:
                d = json.load(fh)
        except (OSError, ValueError) as e:
            err("%s: post.json cannot be read as UTF-8 JSON (%s)" % (label, e))
            continue
        if not isinstance(d, dict):
            err("%s: post.json must be a JSON object" % label)
            continue
        for k, kind in (("hashtags", list), ("sources", list), ("media", list), ("review", dict),
                        ("caption_zh", str), ("hook_zh", str), ("on_screen_label_zh", str), ("id", str)):
            if k in d and not isinstance(d[k], kind):
                err("%s: field %s must be a %s" % (label, k, kind.__name__))
                d[k] = kind()
        d["hashtags"] = [t for t in d.get("hashtags", []) if isinstance(t, str)]
        d["sources"] = [x for x in d.get("sources", []) if isinstance(x, dict)]
        d["media"] = [x for x in d.get("media", []) if isinstance(x, dict)]
        for k in required:
            if k not in d:
                err("%s: missing field %s" % (label, k))
        for k in set(d) - set(required):
            err("%s: unexpected field %s" % (label, k))
        if d.get("persona") != "sehuan" or d.get("platform") not in ("instagram", "threads"):
            err("%s: persona/platform" % label)
        if d.get("format") not in ("carousel", "reel", "short", "text", "image"):
            err("%s: bad format" % label)
        if d.get("format") in ("reel", "short"):
            # decision D6: a still of her may appear in a Reel or Short only with four conditions, written into the production notes
            notes_l = d.get("review", {}).get("notes", "") if isinstance(d.get("review"), dict) else ""
            for mk in ("D6", "AI label", "persistent", "no animation of the face", "no synthetic voice"):
                if mk not in notes_l:
                    err("%s: a Reel or Short must carry the D6 condition %r in review.notes" % (label, mk))
            if d.get("platform") != "instagram":
                err("%s: 色環 has no YouTube presence in the pilot (series.md section 1); a Reel is Instagram only" % label)
        if d.get("ai_label_flag") is not True:
            err("%s: ai_label_flag must be true" % label)
        if d.get("sponsorship_flag") is not False or d.get("sponsorship_type") != "none":
            err("%s: no sponsored content in the 30 days" % label)
        rv = d.get("review", {})
        # Claude never approves; a HUMAN may later set these. Validate the values, and flag an approval that skips a reviewer.
        wl, of, ap = rv.get("wife_language"), rv.get("operator_facts"), rv.get("approved")
        if wl not in ("pending", "approved", "changes") or of not in ("pending", "approved", "changes") or not isinstance(ap, bool):
            err("%s: review fields must be wife_language/operator_facts in pending|approved|changes and approved a boolean" % label)
        elif ap is True and not (wl == "approved" and of == "approved"):
            err("%s: approved=true while a reviewer has not approved" % label)
        elif ap is True:
            warn("%s: marked approved by a human; this script cannot tell who set it, so check the history" % label)
        elif wl != "pending" or of != "pending":
            warn("%s: a human review field has been set (wife_language=%s, operator_facts=%s)" % (label, wl, of))
        if not re.match(r"^sehuan-\d{4}-\d{2}-\d{2}-\d{2}$", d.get("id", "")):
            err("%s: bad id" % label)
        if label.replace("_", "-") != d.get("id", "").replace("sehuan-", ""):
            err("%s: folder name does not match id" % label)
        if d.get("scheduled_date") in quiet:
            err("%s: scheduled in the quiet block 2026-11-27 to 11-29" % label)
        dates.append(d.get("scheduled_date"))
        try:
            wd = dt.date.fromisoformat(d["scheduled_date"]).strftime("%a")
        except Exception:
            err("%s: bad date" % label)
            wd = ""
        if d.get("platform") == "instagram" and wd not in ("Mon", "Wed", "Fri"):
            err("%s: Instagram posts are Mon, Wed or Fri (calendar section 2), got %s" % (label, wd))
        if d.get("platform") == "threads" and wd not in ("Tue", "Thu", "Sat"):
            err("%s: Threads posts are Tue, Thu or Sat (calendar section 2), got %s" % (label, wd))
        # post.json is the master after a human edit; the calendar copy then needs updating (a warning, not an error)
        if cal_text is not None:
            for fld in ("hook_zh", "caption_zh", "caption_gloss_en"):
                if isinstance(d.get(fld), str) and d[fld] and d[fld] not in cal_text:
                    warn("%s: %s differs from calendar-30d.md; update the calendar to match post.json" % (label, fld))
        if len(d.get("hook_zh", "")) > 20:
            err("%s: hook longer than 20 characters" % label)
        cap = d.get("caption_zh", "")
        if not cap.startswith("【AI 虛擬角色】"):
            err("%s: caption does not start with the AI disclosure line" % label)
        if "「色環」" not in cap.split("\n")[0]:
            err("%s: first line must name 「色環」" % label)
        lim = 2200 if d.get("platform") == "instagram" else 500
        if len(cap) > lim:
            err("%s: caption over %d characters" % (label, lim))
        if d.get("platform") == "threads" and len(d.get("hashtags", [])) > 1:
            err("%s: Threads takes 0 or 1 hashtag (bible 3.1)" % label)
        if d.get("platform") == "instagram" and not 3 <= len(d.get("hashtags", [])) <= 6:
            err("%s: Instagram takes 3 to 6 hashtags (bible 3.1)" % label)
        for bad in ("#ootd", "#今日穿搭", "#每日穿搭", "#穿搭日記", "#開箱", "#顯瘦", "#顯白", "#顯高", "#色"):
            if bad in [t.lower() for t in d.get("hashtags", [])]:
                err("%s: banned hashtag %s" % (label, bad))
        if not os.path.isfile(os.path.join(os.path.dirname(f), "media", ".gitkeep")):
            warn("%s: media/.gitkeep missing" % label)
        for m in d.get("media", []):
            if set(m) != {"path", "description", "shot_prompt"} or not all(isinstance(m.get(k), str) for k in m):
                err("%s: media item must have exactly path, description, shot_prompt (strings)" % label)
                m.setdefault("path", "")
                m["description"] = m["description"] if isinstance(m.get("description"), str) else ""
                m["shot_prompt"] = m["shot_prompt"] if isinstance(m.get("shot_prompt"), str) else ""
            elif m["path"] != "PENDING":
                # a human sets the real path once the file exists; it must stay inside the project
                pth = m["path"]
                if os.path.isabs(pth) or ".." in pth.replace("\\", "/").split("/"):
                    err("%s: media path must be relative and inside the project: %r" % (label, pth))
                elif not os.path.isfile(os.path.join(ROOT, pth)) and not os.path.isfile(os.path.join(os.path.dirname(f), pth)):
                    warn("%s: media path %r does not exist on disk" % (label, pth))
        if d.get("format") != "text" and not d.get("media"):
            err("%s: needs media" % label)
        for s in d.get("sources", []):
            if set(s) != {"claim", "url", "date"}:
                err("%s: source item keys" % label)
            if s.get("url") == "" and not s.get("claim", "").startswith(("NO FACTUAL CLAIM", "ARITHMETIC ONLY")):
                err("%s: an empty url is allowed only for NO FACTUAL CLAIM or ARITHMETIC ONLY entries" % label)
        blocked = any("UNVERIFIED-OPERATOR-TO-FILL" in s.get("url", "") for s in d.get("sources", []))
        if blocked:
            warn("%s: BLOCKED until the source placeholder is filled by the operator" % label)
        for fld in ("hook_zh", "caption_zh", "on_screen_label_zh"):
            scan("%s.%s" % (label, fld), d.get(fld, ""))
        for tag in d.get("hashtags", []):
            scan("%s.hashtag" % label, tag)
        # slide text inside the media descriptions (not scanned by queue.py): same net
        for i, m in enumerate(d.get("media", [])):
            mm = re.search(r"TEXT zh-TW \(DRAFT\): (.*?) \| GLOSS", m["description"], re.S)
            if mm:
                scan("%s.media[%d].slide_text" % (label, i), mm.group(1))
                if re.search(r"[0-9]{1,3}\s*°C", mm.group(1)) and "{待填}" not in mm.group(1):
                    err("%s.media[%d]: a temperature appears on a slide without a source fill" % (label, i))
            if "Alt text" in m["description"] and "AI 生成的" not in m["description"]:
                err("%s.media[%d]: alt text must say AI 生成的" % (label, i))
            # no hex or Chinese in AI image prompts; human-built items carry the standard line
            sp = m["shot_prompt"]
            if sp.startswith("NOT AI-GENERATED") and "DRAWN BY CLAUDE AS SVG" not in sp:
                err("%s.media[%d]: a lesson graphic must name its route: DRAWN BY CLAUDE AS SVG (decision D3)" % (label, i))
            if re.search(r"human-built|hand-built|built by hand", sp + " " + m["description"], re.I):
                err("%s.media[%d]: stale human-built wording after decision D3" % (label, i))
            if not sp.startswith("NOT AI-GENERATED"):
                if re.search(r"#[0-9A-Fa-f]{6}", sp):
                    err("%s.media[%d]: hex code in an AI prompt" % (label, i))
                if re.search(r"[\u3400-\u9fff]", sp):
                    err("%s.media[%d]: Chinese characters in an AI prompt" % (label, i))
        # P03/P07/P08 fill-in markers must be flagged as blocked
        txt = json.dumps(d, ensure_ascii=False)
        if "{待填}" in txt and not blocked:
            err("%s: {待填} fill-in present but the post is not blocked" % label)
    # no two drafts on one date; cadence
    if len(set(dates)) != len(dates):
        err("two drafts share a date")
    exp = ["2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-23", "2026-11-24", "2026-11-25", "2026-11-26"]
    if sorted(dates) != exp:
        err("draft dates differ from the calendar: %s" % sorted(dates))


def check_calendar():
    t = read_text(CAL)
    if t is None:
        return
    rows = re.findall(r"^\| (\d{1,2}) \| (\d{4}-\d{2}-\d{2}) \| (\w{3}) \| (W\d) \|", t, re.M)
    if len(rows) != 30:
        err("calendar section 3 has %d day rows, expected 30" % len(rows))
    for i, (n, date, wd, wk) in enumerate(rows, 1):
        d = dt.date.fromisoformat(date)
        if d.strftime("%a") != wd:
            err("calendar day %s: %s is a %s, not %s" % (n, date, d.strftime("%a"), wd))
        if (d - dt.date(2026, 11, 16)).days + 1 != int(n):
            err("calendar day number %s does not match %s" % (n, date))
    for (pid, wd, date, tm) in re.findall(r"^\| (P\d\d) \| (\w{3}) (\d{4}-\d{2}-\d{2}) (\d\d:\d\d) \|", t, re.M):
        d = dt.date.fromisoformat(date)
        if d.strftime("%a") != wd:
            err("calendar %s: %s is a %s, not %s" % (pid, date, d.strftime("%a"), wd))
        if date in ("2026-11-27", "2026-11-28", "2026-11-29"):
            err("calendar %s is in the quiet block" % pid)
    for (pid, wd, date, tm) in re.findall(r"^### (P\d\d) · (\w{3}) (\d{4}-\d{2}-\d{2}) (\d\d:\d\d)", t, re.M):
        d = dt.date.fromisoformat(date)
        if d.strftime("%a") != wd:
            err("calendar %s heading: %s is a %s, not %s" % (pid, date, d.strftime("%a"), wd))
    ids = set(re.findall(r"^### (P\d\d) ·", t, re.M))
    if ids != {"P%02d" % i for i in range(1, 9)}:
        err("section 5 must hold P01 to P08, found %s" % sorted(ids))
    deferred = {"P09", "P10", "P19", "P20"}
    outl = set(re.findall(r"^\| (P\d\d) \| (?:Mon|Tue|Wed|Thu|Fri|Sat|Sun) ", t, re.M))
    want = {"P%02d" % i for i in range(9, 23)} - deferred
    if outl != want:
        err("section 6 must hold the ten scheduled outlines %s, found %s" % (sorted(want), sorted(outl)))
    ded = set(re.findall(r"^\| (P\d\d) \| deferred \(was ", t, re.M))
    if ded != deferred:
        err("section 6.1 must list exactly the deferred posts %s, found %s" % (sorted(deferred), sorted(ded)))
    # weekday and platform of every outlined post (Instagram Mon/Wed/Fri, Threads Tue/Thu/Sat)
    for (pid, wd, date, plat) in re.findall(r"^\| (P\d\d) \| (\w{3}) (\d{4}-\d{2}-\d{2}) \d\d:\d\d \| (IG|Threads)", t, re.M):
        if dt.date.fromisoformat(date).strftime("%a") != wd:
            err("calendar outline %s: %s is not a %s" % (pid, date, wd))
        if (plat == "IG" and wd not in ("Mon", "Wed", "Fri")) or (plat == "Threads" and wd not in ("Tue", "Thu", "Sat")):
            err("calendar outline %s: %s on a %s breaks the section 2 weekday pattern" % (pid, plat, wd))
    # OPS-D1: the section 3 table
    sec = re.search(r"^## 3\. The 30 days at a glance.*?(?=^## 4\.)", t, re.S | re.M)
    if not sec:
        err("calendar section 3 not found")
    else:
        weeks, ids = {}, []
        for m in re.finditer(r"^\| (\d+) \| (\d{4}-\d{2}-\d{2}) \| (\w{3}) \| (W\d) \| (.*?) \|(.*)\|$", sec.group(0), re.M):
            _day, date, wd, wk, posts, _notes = m.groups()
            for pm in re.finditer(r"(P\d\d) (IG|Threads)", posts):
                pid, plat = pm.groups()
                ids.append(pid)
                weeks.setdefault(wk, {"IG": [], "Threads": []})[plat].append(pid)
        for pid in sorted(deferred & set(ids)):
            err("%s is deferred by OPS-D1 but is scheduled in the section 3 table" % pid)
        for wk, v in sorted(weeks.items()):
            if len(v["IG"]) > 2 or len(v["Threads"]) > 2:
                err("%s: more than 2 Instagram or 2 Threads posts (OPS-D1 holds 4 approvals a week)" % wk)
        for wk in ("W1", "W2", "W3", "W4"):
            if len(weeks.get(wk, {}).get("IG", [])) < 2:
                err("%s: fewer than 2 posts on the primary platform (Instagram)" % wk)
        if len(ids) != len(set(ids)) or len(ids) != 18:
            err("section 3 should schedule 18 distinct posts after OPS-D1, found %d" % len(ids))
        if sorted(ids) != sorted("P%02d" % i for i in range(1, 23) if "P%02d" % i not in deferred):
            err("section 3 post IDs differ from P01 to P22 minus the deferred four: %s" % sorted(ids))
    # D3: no stale human-built wording in sections 5 and 6 (section 8.1 and section 11 may name the v0.1 route)
    for name, pat in (("5", r"^## 5\..*?(?=^## 6\.)"), ("6", r"^## 6\..*?(?=^## 7\.)")):
        mm = re.search(pat, t, re.S | re.M)
        if mm and re.search(r"human-built|hand-built|built by hand", mm.group(0), re.I):
            err("calendar section %s still says human-built after decision D3" % name)
    # section 8 and this script must agree on the headline capacity numbers
    s8 = re.search(r"^## 8\..*?(?=^## 9\.)", t, re.S | re.M)
    if s8:
        for needle in ("**70**", "17.5", "11.5", "315 minutes", "935 minutes", "45% of the 110", "**40 a week**", "**60 a week**"):
            if needle not in s8.group(0):
                err("calendar section 8 no longer contains %r (script and text disagree)" % needle)
    if "gate 15" in t and not re.search(r"\| 15 \|[^\n]*Closed by D6", t):
        err("gate 15 should read Closed by D6")
    if "{{" in t:
        err("calendar still contains a template marker")
    # hook ids mentioned in the calendar exist in the library
    lib = set(re.findall(r"^\| (H\d\d) \|", read_text(HOOKS) or "", re.M))
    for h in set(re.findall(r"\bH\d\d\b", t)):
        if h not in lib:
            err("calendar mentions %s which is not in the hook library" % h)


def check_hooks():
    t = read_text(HOOKS)
    if t is None:
        return
    rows = re.findall(r"^\| (H\d\d) \| (P\d|ID) \| ([^|]*) \| ([^|]*) \| ([^|]*) \| (\d+) \| ", t, re.M)
    if len(rows) < 30:
        err("hook library has %d hooks, expected 30 or more" % len(rows))
    ids = [r[0] for r in rows]
    if len(set(ids)) != len(ids):
        err("duplicate hook ids")
    for (hid, pil, use, hook, gloss, n) in rows:
        hook = hook.strip()
        if len(hook) != int(n):
            err("%s: stated length %s but the hook has %d characters" % (hid, n, len(hook)))
        if len(hook) > 20:
            err("%s: longer than 20 characters" % hid)
        scan(hid, hook)
    # every post hook is in the library
    texts = {r[3].strip() for r in rows}
    for f in sorted(glob.glob(QUEUE)):
        try:
            with open(f, encoding="utf-8") as fh:
                d = json.load(fh)
        except (OSError, ValueError):
            continue  # already reported by check_json
        if isinstance(d, dict) and d.get("hook_zh") not in texts:
            err("%s: hook not found in the library" % d.get("id", f))


def check_replies():
    t = read_text(REPLIES)
    if t is None:
        return
    rows = re.findall(r"^\| (RP\d\d) \| ([^|]*) \| ([^|]*) \| ((?:[^|\\]|\\\|)*) \| ", t, re.M)
    if len(rows) != 12:
        err("reply guidelines has %d sample replies, expected 12" % len(rows))
    for r in rows:
        scan(r[0], r[3])
        if "：" in r[3] and r[0] not in ("RP04", "RP12"):
            pass
        if len(r[3]) > 110:
            warn("%s: reply is long (%d characters)" % (r[0], len(r[3])))


def check_chars():
    for p in TEXT_FILES + sorted(glob.glob(QUEUE)):
        if not os.path.isfile(p):
            err("missing file %s" % p)
            continue
        txt = read_text(p)
        if txt is None:
            continue
        bad = sorted({c for c in txt if c in gr.SIMPLIFIED_SET})
        if bad:
            err("%s: Simplified-only characters %s" % (os.path.relpath(p, ROOT), " ".join(bad)))
        if "\ufffd" in txt:
            err("%s: contains the replacement character" % os.path.relpath(p, ROOT))
    try:
        import opencc  # noqa: F401
        warn("OpenCC is installed but this script does not use it; run it by hand for a second opinion")
    except ImportError:
        pass


def main():
    for step in (check_arithmetic, check_json, check_calendar, check_hooks, check_replies, check_chars):
        try:
            step()
        except Exception as e:  # a malformed input must produce an ERROR line, not a traceback
            err("%s crashed on unexpected input: %s: %s" % (step.__name__, type(e).__name__, e))
    for w in warnings:
        print("WARN  " + w)
    for e in errors:
        print("ERROR " + e)
    print("%d error(s), %d warning(s)" % (len(errors), len(warnings)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
