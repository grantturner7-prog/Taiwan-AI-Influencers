#!/usr/bin/env python3
"""Offline checks for the 步驟 (buzhou) content and review-queue drafts.

Run from the repository root:   python3 content/buzhou/verify.py

Standard library only. No network calls. This script is a first-pass filter for the operator and for Claude, NOT a
replacement for the wife's review: it cannot judge tone, naturalness or Taiwan vocabulary beyond the word lists, and it
checks no fact against any source (no vendor fact in these files has been checked).

What it checks
  1. The four queue drafts in pipeline/review-queue/buzhou/: fields, enumerations, folder name = id, first line is the
     AI disclosure line, review fields still pending / approved false, AI-label flag true, sponsorship none.
  2. The caption and gloss in each post.json equal the blocks in calendar-30d.md (the calendar is the source).
  3. The shared pipeline scanner (pipeline/scripts/ground_rules.py, loaded by file path, not imported by name) over every
     fenced block, scene caption, hook, reply and queue string: no ERROR or FLAG apart from the deliberate allow-list.
  4. Subtitle lines in the scene tables are 16 characters or fewer, two lines at most, and the scene times are
     contiguous and end within 60 seconds.
  5. Hooks in hook-library.md: 20 characters or fewer, unique, end with 。 or ？, no brace; the hooks the calendar uses
     exist and match; no window of four consecutive LIVE masters holds more than one 先看-pattern hook.
  6. Dates and weekdays: the day table, the master headings, the cadence (2 masters a week in every week under OPS-D1,
     masters M7 and M8 cut), no post on the recalled polling day, 雙12, Black Friday or 228; the 90-day re-check dates
     in trend-check.md.
  9. Decision D6 (still image of the character inside a Short): each queued Short carries the five production
     conditions in review.notes and still carries a HOLD note for the reasons that remain; the calendar has the
     section 7.10 conditions. Decision OPS-D1: 18 posts in the day table, none of T7, S7, T8, S8.
  7. Twelve sample replies in reply-guidelines.md.
  8. `queue.py validate` on the drafts (via subprocess; the pipeline validator is the authority on the post format).

Exit code 0 = no errors; 1 = at least one error. Warnings are printed but do not fail the run.
"""
import sys

sys.dont_write_bytecode = True  # never leave __pycache__ folders in the repository

import datetime as dt
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CAL = ROOT / "content/buzhou/calendar-30d.md"
HOOKS = ROOT / "content/buzhou/hook-library.md"
REPLY = ROOT / "content/buzhou/reply-guidelines.md"
TREND = ROOT / "content/buzhou/trend-check.md"
SERIES = ROOT / "content/buzhou/series.md"
QDIR = ROOT / "pipeline/review-queue/buzhou"

errors, warnings = [], []

# The 30-day plan after decision OPS-D1 (2026-10-12): hold at 12 approvals a week across the three pilots, so 步驟 posts
# 2 masters a week in every week. Masters M7 and M8 are cut (backlog outlines only); their IDs are not reused.
PLAN = {"M1": "2026-11-19", "M2": "2026-11-22", "M3": "2026-11-26", "M4": "2026-11-29", "M5": "2026-12-01",
        "M6": "2026-12-03", "M7": "2026-12-06", "M8": "2026-12-08", "M9": "2026-12-10", "M10": "2026-12-13",
        "M11": "2026-12-15"}
CUT = {"M7", "M8"}
LIVE = [m for m in PLAN if m not in CUT]
LIVE_DATES = [PLAN[m] for m in LIVE]


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def load_gr():
    path = ROOT / "pipeline/scripts/ground_rules.py"
    spec = importlib.util.spec_from_file_location("buzhou_ground_rules", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["buzhou_ground_rules"] = mod
    spec.loader.exec_module(mod)
    return mod


GR = load_gr()

# Deliberate sentences the keyword net flags or downgrades: identity negations and declines. Listed so a human can see
# exactly what is allowed. Anything else the scanner flags is an error.
ALLOWED = [
    "我沒有用過任何工具",          # identity line, T1 and S1 intro only
    "我沒有實際用過任何工具",      # RP02
    "我不提供賺錢或收入相關的建議",  # RP06: names the topic only to decline it
]
ALLOWED_CODES = {"LIVED_EXPERIENCE_DENIED", "FINANCE_CLAIM_DENIED", "HEALTH_CLAIM_DENIED", "UNDISCLOSING_DENIED"}

MAINLAND_EXTRA = ["視頻", "信息", "博主", "軟件", "硬件", "屏幕", "默認", "設置", "鏈接", "賬", "打印", "模板", "文檔",
                  "用戶", "界面", "數據", "網絡", "程序", "智能", "人工智能", "導出", "粘貼", "菜單", "質量", "項目",
                  "性價比", "插件", "代碼", "服務器", "分辨率", "激活", "兼容", "支持", "關注", "評論", "點贊", "轉發"]
EXPERIENCE_EXTRA = ["實測", "親測", "試用", "好用", "神器", "必裝", "最強", "效率", "輕鬆", "一鍵", "推薦", "開箱",
                    "心得", "愛用", "踩雷", "避雷", "我試", "我測", "我用了", "我用過", "我發現", "副業", "被動收入",
                    "月入", "限時", "馬上", "立刻", "必看", "保證", "絕對"]
PRONOUNS = ["他", "她"]  # the character is referred to by name; 它 is allowed for a tool


def scan_zh(label, text):
    t = text
    for a in ALLOWED:
        t = t.replace(a, "")
    t_pron = t.replace("其他", "").replace("他人", "")
    for w in MAINLAND_EXTRA:
        if w in t:
            err(f"{label}: mainland or banned vocabulary {w!r} in {text[:50]!r}")
    for w in EXPERIENCE_EXTRA:
        if w in t:
            err(f"{label}: experience, hype, income or urgency word {w!r} in {text[:50]!r}")
    for w in PRONOUNS:
        if w in t_pron:
            err(f"{label}: pronoun {w!r} (the character is named, not gendered) in {text[:50]!r}")
    for f in GR.scan_text(t, label):
        if f.level in ("ERROR", "FLAG") and f.code not in ALLOWED_CODES:
            err(f"{label}: scanner {f.level} {f.code}: {f.message[:120]}")
        elif f.level == "WARN" and f.code not in ("MAINLAND_SOFT", "SUPERLATIVE", "PERFORMANCE_CLAIM"):
            warn(f"{label}: scanner WARN {f.code}: {f.message[:100]}")
        elif f.level == "WARN" and f.code == "MAINLAND_SOFT" and "保存期限" in t and "'保存'" in f.message:
            continue  # deliberate: the food-packaging sense (joke J4); flagged for the wife in hook-library.md and the calendar
        elif f.level == "WARN" and f.code == "MAINLAND_SOFT":
            warn(f"{label}: soft mainland word for the wife to rule on: {f.message[:100]}")
    try:
        import opencc  # optional
        conv = opencc.OpenCC("s2t").convert(t)
        if conv != t:
            diffs = {a + "->" + b for a, b in zip(t, conv) if a != b}
            diffs -= {"床->牀", "具->俱", "家->傢", "台->臺", "布->佈", "占->佔", "著->着", "裡->裏", "里->裡", "面->麵", "後->后"}
            if diffs:
                warn(f"{label}: possible Simplified characters {sorted(diffs)} in {t[:40]!r}")
    except ImportError:
        pass


def fenced_blocks(md):
    return re.findall(r"```\n(.*?)\n```", md, re.S)


def check_queue():
    cal = CAL.read_text(encoding="utf-8")
    folders = sorted(p for p in QDIR.glob("*") if p.is_dir())
    if len(folders) != 8:
        err(f"expected 8 queue folders (T1 to T4 Threads as _01, S1 to S4 Shorts as _02), found {len(folders)}")
    required = ["id", "persona", "platform", "format", "scheduled_date", "pillar", "hook_zh", "caption_zh",
                "caption_gloss_en", "hashtags", "on_screen_label_zh", "ai_label_flag", "sponsorship_flag",
                "sponsorship_type", "sources", "media", "review"]
    for folder in folders:
        f = folder / "post.json"
        label = folder.name
        if not f.exists():
            err(f"{label}: post.json missing")
            continue
        if not (folder / "media" / ".gitkeep").exists():
            err(f"{label}: media/.gitkeep missing")
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:  # unreadable file, bad UTF-8 or invalid JSON
            err(f"{label}: post.json cannot be read as JSON ({type(exc).__name__}: {str(exc)[:80]})")
            continue
        if not isinstance(d, dict):
            err(f"{label}: post.json must hold a JSON object")
            continue
        types = {"id": str, "persona": str, "platform": str, "format": str, "scheduled_date": str, "pillar": str,
                 "hook_zh": str, "caption_zh": str, "caption_gloss_en": str, "hashtags": list,
                 "on_screen_label_zh": str, "ai_label_flag": bool, "sponsorship_flag": bool,
                 "sponsorship_type": str, "sources": list, "media": list, "review": dict}
        wrong = [k for k, t in types.items() if k in d and not isinstance(d[k], t)]
        if wrong:
            err(f"{label}: wrong JSON type for field(s) {wrong}")
            continue
        for k in required:
            if k not in d:
                err(f"{label}: missing field {k}")
        for k in set(d) - set(required):
            err(f"{label}: unexpected field {k}")
        if d.get("persona") != "buzhou":
            err(f"{label}: persona must be buzhou")
        is_short = d.get("platform") == "youtube_shorts"
        if is_short:
            if d.get("format") != "short" or not label.endswith("_02"):
                err(f"{label}: a YouTube Shorts draft must be format short in an _02 folder")
        elif d.get("platform") != "threads" or d.get("format") not in ("text", "image", "carousel") or not label.endswith("_01"):
            err(f"{label}: expected a Threads text or image draft in an _01 folder")
        if d.get("id") != f"buzhou-{d.get('scheduled_date')}-{folder.name.split('_')[1]}" or folder.name != f"{d.get('scheduled_date')}_{folder.name.split('_')[1]}":
            err(f"{label}: folder name and id disagree")
        if d.get("ai_label_flag") is not True:
            err(f"{label}: ai_label_flag must be true")
        if d.get("sponsorship_flag") is not False or d.get("sponsorship_type") != "none":
            err(f"{label}: sponsorship must be false / none in the 30 days")
        rv = d.get("review", {})
        if rv.get("approved") is not False or rv.get("wife_language") != "pending" or rv.get("operator_facts") != "pending":
            err(f"{label}: review fields must start pending and approved=false")
        cap = d.get("caption_zh", "")
        if is_short:
            first = cap.split("\n")[0]
            if not first.startswith("【AI 虛擬角色】本影片由 AI 生成的虛擬角色「步驟」說明，畫面中的角色為 AI 生成，並非真人；螢幕錄影由工作室真人操作"):
                err(f"{label}: first description line is not the YouTube disclosure line (calendar 7.4)")
            if "畫面為 AI 生成" in first:
                err(f"{label}: first line calls the real screen recording AI-generated")
            rv0 = d.get("review", {})
            notes = str(rv0.get("notes", ""))
            if "HOLD" not in notes:
                err(f"{label}: a Short with no recording yet must carry a HOLD note (gate G7 and the fill-ins remain)")
            # decision D6 (2026-10-12): the conditions are written into the production notes; D6 is no longer a hold reason
            for frag in ("D6 HOLD LIFTED", "D6 PRODUCTION CONDITIONS", "YouTube altered-or-synthetic-content = Yes",
                         "「AI 生成｜虛擬角色」 on every frame", "slow pan or zoom of a still", "no animation of the face",
                         "no synthetic or cloned voice"):
                if frag not in notes:
                    err(f"{label}: review.notes lacks the D6 condition text {frag!r}")
            if "has not confirmed" in notes or "(2) the user" in notes:
                err(f"{label}: review.notes still treats the D6 question as open")
            if "G7" not in notes:
                err(f"{label}: review.notes must keep the remaining G7 hold")
            med = d.get("media", [])
            if len(med) != 3 or "decision D6" not in str(med[1].get("description", "")):
                err(f"{label}: the stills media entry must cite decision D6")
        elif not cap.startswith("【AI 虛擬角色】本篇由 AI 生成的虛擬角色「步驟」發布"):
            err(f"{label}: first caption line is not the disclosure line")
        if d.get("format") == "image" and "圖像為 AI 生成，並非真人" not in cap.split("\n")[0] and "圖上沒有人物" not in cap.split("\n")[0]:
            err(f"{label}: image post first line lacks the image disclosure")
        if len(cap) > (5000 if is_short else 500):
            err(f"{label}: caption has {len(cap)} characters, over the recalled limit (Threads 500, YouTube description 5000; both unverified)")
        # the caption in the calendar is the source
        m = re.search(r"<!-- QUEUE:" + re.escape(d.get("id", "")) + r":caption -->\s*\n```\n(.*?)\n```", cal, re.S)
        g = re.search(r"<!-- QUEUE:" + re.escape(d.get("id", "")) + r":gloss -->\s*\n```\n(.*?)\n```", cal, re.S)
        if not m or m.group(1) + "\n" != cap:
            err(f"{label}: caption differs from the calendar block")
        if not g or g.group(1) != d.get("caption_gloss_en"):
            err(f"{label}: gloss differs from the calendar block")
        # structure of the nested lists (a missing key must be an error, not a crash)
        if not all(isinstance(t, str) for t in d.get("hashtags", [])):
            err(f"{label}: hashtags must be strings")
        for i, s in enumerate(d.get("sources", [])):
            if not isinstance(s, dict) or set(s) != {"claim", "url", "date"} or not all(isinstance(v, str) for v in s.values()):
                err(f"{label}: sources[{i}] must be an object with exactly claim, url, date (strings)")
        for i, mm in enumerate(d.get("media", [])):
            if not isinstance(mm, dict) or set(mm) != {"path", "description", "shot_prompt"}:
                err(f"{label}: media[{i}] must have exactly path, description, shot_prompt")
        if set(d.get("review", {})) != {"wife_language", "operator_facts", "approved", "notes"}:
            err(f"{label}: review must have exactly wife_language, operator_facts, approved, notes")
        if any(not isinstance(s, dict) or "claim" not in s or "url" not in s for s in d.get("sources", [])) or \
                any(not isinstance(mm, dict) for mm in d.get("media", [])):
            continue  # structure errors are already reported; the checks below need well-formed lists
        # media: pending only
        for mm in d.get("media", []):
            if mm.get("path") != "PENDING":
                err(f"{label}: media path must be PENDING before any file exists")
        if (d.get("format") == "image" or is_short) and not d.get("media"):
            err(f"{label}: image or short post has no media entry")
        if d.get("format") == "text" and d.get("media"):
            err(f"{label}: text post must have no media entry")
        # sources: at least one real-source entry (placeholder allowed) and no invented url
        real = [s for s in d.get("sources", []) if not s["claim"].upper().startswith(("NO FACTUAL CLAIM", "ARITHMETIC ONLY"))]
        if not real:
            err(f"{label}: no real-source entry (placeholder expected)")
        for s in real:
            if s["url"] not in ("UNVERIFIED-OPERATOR-TO-FILL",) and not s["url"].startswith("https://"):
                err(f"{label}: source url is neither a placeholder nor https: {s['url']!r}")
            if s["url"].startswith("https://"):
                warn(f"{label}: a real URL is present: confirm the operator opened it")
        # text scans
        for field in ("hook_zh", "caption_zh", "on_screen_label_zh"):
            scan_zh(f"{label}.{field}", d.get(field, ""))
        for t in d.get("hashtags", []):
            scan_zh(f"{label}.hashtag", t)
        if "{" in cap:
            warn(f"{label}: caption holds a fill-in brace (expected until the operator fills it)")
    return folders


def check_calendar():
    cal = CAL.read_text(encoding="utf-8")

    # day table
    rows = re.findall(r"^\| (\d+) \| (2026-\d\d-\d\d) \| (\w{3}) \| (W\d) \| (.*?) \|", cal, re.M)
    if len(rows) != 30:
        err(f"day table: expected 30 rows, found {len(rows)}")
    w0 = dt.date(2026, 11, 16)
    posts_by_date = {}
    for n, date, wd, wk, posts in rows:
        d = dt.date.fromisoformat(date)
        if (d - w0).days + 1 != int(n):
            err(f"day table: day {n} is not {date}")
        if d.strftime("%a") != wd:
            err(f"day table: {date} is {d.strftime('%a')}, table says {wd}")
        if not posts.startswith("none"):
            posts_by_date[date] = posts
    expected = LIVE_DATES
    if sorted(posts_by_date) != expected:
        err(f"posting days differ from the plan: {sorted(posts_by_date)}")
    # OPS-D1: the cut masters have no post in the day table; 18 posts in all
    ids = re.findall(r"\b([ST]\d+)\b", " ".join(posts_by_date.values()))
    if len(ids) != 18 or any(i in ids for i in ("S7", "T7", "S8", "T8")):
        err(f"day table lists {len(ids)} post ids ({sorted(ids)}); expected 18 and none of S7, T7, S8, T8")
    for cut_date in (PLAN["M7"], PLAN["M8"]):
        if cut_date in posts_by_date:
            err(f"{cut_date} is a cut master's date (OPS-D1) but the day table has a post")
    if dt.date(2026, 11, 28).isoformat() in posts_by_date or "2026-12-12" in posts_by_date or "2026-11-27" in posts_by_date:
        err("a post is scheduled on the recalled polling day, 雙12 or Black Friday")
    if "2027-02-28" in posts_by_date:
        err("a post on 228")
    # cadence: two masters in every week (OPS-D1: 12 approvals a week across the three pilots, held through week 8)
    per_week = {}
    for date in expected:
        d = dt.date.fromisoformat(date)
        wk = (d - w0).days // 7 + 1
        per_week[wk] = per_week.get(wk, 0) + 1
    if per_week != {1: 2, 2: 2, 3: 2, 4: 2, 5: 1}:
        err(f"cadence by week is {per_week}")
    # weekdays allowed: weeks 1-2 Thu/Sun; 3-4 Tue/Thu/Sun (two of them are kept per week); day 30 Tue
    for date in expected:
        wd = dt.date.fromisoformat(date).strftime("%a")
        wk = (dt.date.fromisoformat(date) - w0).days // 7 + 1
        ok = (wk <= 2 and wd in ("Thu", "Sun")) or (wk in (3, 4) and wd in ("Tue", "Thu", "Sun")) or (wk == 5 and wd == "Tue")
        if not ok:
            err(f"{date} ({wd}) is outside the cadence pattern")

    # master headings M1..M4 and outline table M5..M11
    for m in re.finditer(r"^### (M\d+) · (\w{3}) (2026-\d\d-\d\d)", cal, re.M):
        d = dt.date.fromisoformat(m.group(3))
        if d.strftime("%a") != m.group(2):
            err(f"{m.group(1)}: heading weekday wrong for {m.group(3)}")
    ms = re.findall(r"^\| (M\d+) \| (\w{3}) (2026-\d\d-\d\d) \|", cal, re.M)
    if len(ms) != 7:
        err(f"outline table: expected 7 masters (M5 to M11), found {len(ms)}")
    for mid, wd, date in ms:
        if dt.date.fromisoformat(date).strftime("%a") != wd:
            err(f"{mid}: outline weekday wrong for {date}")
    for mid, wd, date in ms:
        if PLAN.get(mid) != date:
            err(f"{mid}: outline date {date} differs from the plan")
    # OPS-D1 status column: M7 and M8 are cut, the other outlines are live
    status = dict(re.findall(r"^\| (M\d+) \| \w{3} 2026-\d\d-\d\d \|.*\| ([^|]+?) \|$", cal, re.M))
    for mid, _, _ in ms:
        want_cut = mid in CUT
        got = status.get(mid, "")
        if want_cut != ("CUT" in got) or (not want_cut and "Live" not in got):
            err(f"{mid}: OPS-D1 status column reads {got!r}")
    for mid in CUT:
        if not re.search(r"^### " + mid + r" · .*CUT under OPS-D1", cal, re.M):
            err(f"{mid}: heading does not say CUT under OPS-D1")
    # decision D6: the conditions section exists and the gate is closed
    if "### 7.10 Still-in-video conditions (decision D6" not in cal:
        err("calendar lacks section 7.10 (the D6 conditions)")
    for frag in ("**Decided 2026-10-12 (D6)", "**Answered 2026-10-12 (D6"):
        if frag not in cal:
            err(f"calendar still treats the D6 question as open: lacks {frag!r}")

    # scene tables: continuity and subtitle line length
    for tbl in re.finditer(r"\| Time \| Caption on screen.*?\n((?:\|.*\n)+)", cal):
        prev_end = 0
        last = None
        for line in tbl.group(1).strip().split("\n"):
            cells = [c.strip() for c in line.strip().strip("|").split(" | ")]
            if len(cells) < 5 or cells[0].startswith("---"):
                continue
            m = re.match(r"(\d):(\d\d) to (\d):(\d\d)", cells[0])
            if not m:
                continue
            start = int(m.group(1)) * 60 + int(m.group(2))
            end = int(m.group(3)) * 60 + int(m.group(4))
            if start != prev_end:
                err(f"scene table: gap or overlap at {cells[0]}")
            if end <= start:
                err(f"scene table: bad time {cells[0]}")
            prev_end = end
            lines = cells[1].split("<br>")
            if len(lines) > 2:
                err(f"scene {cells[0]}: more than two caption lines")
            for ln in lines:
                if len(ln) > 16:
                    err(f"scene {cells[0]}: caption line has {len(ln)} characters (limit 16): {ln!r}")
                scan_zh(f"scene {cells[0]}", ln)
            # PiP stills named in the last column are in the set
            if cells[4] not in ("E01", "E04", "E06", "E07", "R06"):
                err(f"scene {cells[0]}: unknown PiP still {cells[4]!r}")
            last = cells[0]
        if prev_end > 60:
            err(f"scene table ends at {prev_end} s, over 60")
        if prev_end == 0:
            err("a scene table has no rows")

    # fenced blocks: captions, descriptions, templates, sample kit
    for i, blk in enumerate(fenced_blocks(cal)):
        if blk.startswith("TREND NOTE"):
            continue
        scan_zh(f"calendar fenced block {i + 1}", blk)

    # sample kit weekdays quoted in the text (2026)
    for date, wd in (("2026-12-04", "Fri"), ("2026-12-07", "Mon"), ("2026-12-09", "Wed"), ("2026-12-01", "Tue"),
                     ("2026-12-02", "Wed"), ("2026-12-08", "Tue")):
        if dt.date.fromisoformat(date).strftime("%a") != wd:
            err(f"sample kit weekday for {date} should be {wd}")
    for frag in ("12 月 9 日（週三）", "12 月 4 日（週五）", "12 月 7 日（週一）", "12 月 1 日（週二）", "12 月 2 日（週三）", "12 月 8 日（週二）"):
        if frag not in cal:
            err(f"sample kit lacks {frag}")
    # the sample kit must stay consistent with every weekday written inside it
    for day, wd in re.findall(r"12 月 (\d+) 日（週(.)）", cal):
        want = "一二三四五六日"[dt.date(2026, 12, int(day)).weekday()]
        if want != wd:
            err(f"sample kit: 12 月 {day} 日 is 週{want}, text says 週{wd}")
    return cal


def check_hooks(cal):
    md = HOOKS.read_text(encoding="utf-8")
    rows = re.findall(r"^\| (H\d\d) \| (\S+) \| (.*?) \| (.*?) \| (.*?) \| (\d+) \| (.*?) \|$", md, re.M)
    if len(rows) < 30:
        err(f"hook library has {len(rows)} hooks, need 30 or more")
    ids = set()
    texts = {}
    for hid, pillar, use, zh, gloss, n, note in rows:
        if hid in ids:
            err(f"{hid}: duplicate id")
        ids.add(hid)
        texts[hid] = zh
        if len(zh) > 20:
            err(f"{hid}: {len(zh)} characters, over 20")
        if int(n) != len(zh):
            err(f"{hid}: stated length {n} is not {len(zh)}")
        if not zh.endswith(("。", "？")):
            err(f"{hid}: must end with 。 or ？")
        if "{" in zh:
            err(f"{hid}: brace in a hook")
        scan_zh(hid, zh)
    if len(set(texts.values())) != len(texts):
        err("two hooks have the same text")
    # hooks the calendar uses
    used = {"M1": "H08", "M2": "H12", "M3": "H22", "M4": "H18", "M5": "H20", "M6": "H24", "M7": "H35", "M8": "H40",
            "M9": "H16", "M10": "H36", "M11": "H19"}
    cal_hooks = {}
    for mid, hid in used.items():
        if hid not in texts:
            err(f"{mid}: hook {hid} not in the library")
    # the Short / Threads hook text for M1..M4 equals the library
    for hid, anchor in (("H08", "AI 回答完，先別轉貼。"), ("H12", "長 PDF 先抓重點？先看上限。"), ("H22", "同一個提示詞，每次輸出可能不一樣。"),
                        ("H18", "價格頁這三格，別漏看。")):
        if texts.get(hid) != anchor:
            err(f"{hid}: library text differs from the calendar hook {anchor!r}")
    for p in QDIR.glob("*/post.json"):
        d = json.loads(p.read_text(encoding="utf-8"))
        if d["hook_zh"] not in texts.values():
            err(f"{p.parent.name}: hook_zh is not in the hook library")
    # 先看 window rule, over the LIVE masters in posting order (M7 and M8 are cut under OPS-D1)
    order = [used[m] for m in LIVE]
    flags = ["先看" in texts[h] for h in order]
    for i in range(len(flags) - 3):
        if sum(flags[i:i + 4]) > 1:
            err(f"先看 hooks: more than one in the live masters {LIVE[i]} to {LIVE[i + 3]}")
    for mid in CUT:
        if not re.search(r"\| " + mid + r" \| .*?\| " + used[mid] + r" \| .*cut", md, re.I):
            err(f"hook-library section 4 does not mark {mid} as cut")
    # the calendar's hook table in hook-library section 4 lists the same ids
    for mid, hid in used.items():
        if not re.search(r"\| " + mid + r" \| .*? \| " + hid + r" \|", md):
            err(f"hook-library section 4 does not list {hid} for {mid}")
    return texts


def check_replies():
    md = REPLY.read_text(encoding="utf-8")
    rows = re.findall(r"^\| (RP\d\d) \| (.*?) \| (.*?) \| (.*?) \| (.*?) \|$", md, re.M)
    if len(rows) != 12:
        err(f"reply guidelines: expected 12 sample replies, found {len(rows)}")
    for rid, when, zh, gloss, notes in rows:
        if not gloss.strip():
            err(f"{rid}: no gloss")
        scan_zh(rid, zh)
    extras = re.findall(r"^\| (RX\d) \| (.*?) \| (.*?) \| (.*?) \| (.*?) \|$", md, re.M)
    for rid, when, zh, gloss, notes in extras:
        scan_zh(rid, zh)
    # the bible's R1..R8 wording is reused verbatim where the bible's review fixed it
    bible = (ROOT / "personas/buzhou/bible.md").read_text(encoding="utf-8")
    byid = {r[0]: r[2] for r in rows}
    for rid, key in (("RP01", "不是，我是 AI 虛擬角色"), ("RP04", "這則已由工作室先隱藏"), ("RP06", "這題我不回答"),
                     ("RP08", "這個我不會教")):
        if key not in byid.get(rid, "") or key not in bible:
            err(f"{rid}: wording does not match the bible's reply")


def check_trend():
    md = TREND.read_text(encoding="utf-8")
    for post, pub in (("M1", "2026-11-19"), ("M2", "2026-11-22"), ("M3", "2026-11-26"), ("M4", "2026-11-29")):
        due = dt.date.fromisoformat(pub) + dt.timedelta(days=90)
        if due.isoformat() not in md:
            err(f"trend-check: re-check due date {due.isoformat()} for {post} missing")
        do_on = due
        while do_on.weekday() >= 5:
            do_on -= dt.timedelta(days=1)
        if f"Do it on" in md and do_on.isoformat() not in md:
            err(f"trend-check: 'do it on' date {do_on.isoformat()} for {post} missing")
    for date, wd in (("2027-02-17", "Wed"), ("2027-02-20", "Sat"), ("2027-02-24", "Wed"), ("2027-02-27", "Sat"),
                     ("2027-02-28", "Sun"), ("2027-02-06", "Sat"), ("2026-12-12", "Sat"), ("2026-11-28", "Sat")):
        if dt.date.fromisoformat(date).strftime("%a") != wd:
            err(f"weekday for {date} should be {wd}")
    for blk in fenced_blocks(md):
        if "TREND NOTE" in blk:
            continue
    # no real number in the DEMO block
    demo = re.search(r"TREND NOTE v0\.1 \(DEMO\).*?```", md, re.S)
    if demo and re.search(r"\d{2,}", demo.group(0).replace("2026-00-00", "")):
        warn("trend-check DEMO block contains digits: check that no real number was written")


def check_arithmetic():
    """Recompute the capacity figures quoted in calendar-30d.md section 8 and section 10.

    The edit column is the old steady-state edit (M2/M3 40-60, M4 35-50, M1 90-120 with the project build) minus 15 minutes
    of layers that Claude now draws, plus 5 minutes for the operator's review of each Claude-drawn asset (one overlay set per
    Short, one card for M4), plus a one-off 15 minutes on M1 for the first import and template. All are assumptions."""
    def round(x):  # half up, as the file does (Python's round() is banker's rounding)
        return int(x + 0.5)

    layers, review_set, review_card, first_import = 15, 5, 5, 15
    old = {"M1": (90, 120), "M2": (40, 60), "M3": (40, 60), "M4": (35, 50)}
    steady = (40, 60)
    new = {
        "M1": (steady[0] - layers + review_set + first_import, steady[1] - layers + review_set + first_import),
        "M2": (old["M2"][0] - layers + review_set, old["M2"][1] - layers + review_set),
        "M3": (old["M3"][0] - layers + review_set, old["M3"][1] - layers + review_set),
        "M4": (old["M4"][0] - layers + review_set + review_card, old["M4"][1] - layers + review_set + review_card),
    }
    old_lo, old_hi = sum(v[0] for v in old.values()), sum(v[1] for v in old.values())
    edit_lo, edit_hi = sum(v[0] for v in new.values()), sum(v[1] for v in new.values())
    rec = 4 * 20
    reserve = 360 - 250
    overhead = 10 + 10 + 24 + 21   # ops/weekly-routine.md 2.3: trend, status look, live checks at 12 approvals, monthly bundle
    slack = reserve - overhead
    wk_lo, wk_hi = round(edit_lo / 2), round(edit_hi / 2)
    checks = [
        ((old_lo, old_hi), (205, 290)),
        (new, {"M1": (45, 65), "M2": (30, 50), "M3": (30, 50), "M4": (30, 45)}),
        ((edit_lo, edit_hi), (135, 210)),
        ((edit_lo + rec, edit_hi + rec), (215, 290)),
        ((round((edit_lo + rec) / 2), round((edit_hi + rec) / 2)), (108, 145)),
        ((wk_lo, wk_hi), (68, 105)),
        ((round(edit_lo / 2 / reserve * 100), round(edit_hi / 2 / reserve * 100)), (61, 95)),
        (reserve, 110),
        (12 * 5 + 30 + 60 + 60 + 2 * 20 + 0, 250),            # OPS-D1: 12 approvals x 5, 2 masters x 20, admin 60, analytics 30, comments 60
        ((2 * new["M2"][0], 2 * new["M2"][1]), (60, 100)),   # weeks 3 to 8: 2 steady masters a week
        ((3 * steady[0], 3 * steady[1]), (120, 180)),        # the plan before the decisions: 3 masters at the old steady edit
        ((3 * steady[0] - 2 * new["M2"][0], 3 * steady[1] - 2 * new["M2"][1]), (60, 80)),
        (slack, 45),
        ((min(wk_lo, 60) - slack, wk_hi - slack), (15, 60)),
        (4 * (10 + 3 + 3), 64),
        (2 * (10 + 3 + 3), 32),
        (3 * (10 + 3 + 3), 48),
    ]
    for got, want in checks:  # explicit errors instead of assert, so `python -O` cannot skip them
        if got != want:
            err(f"capacity arithmetic: computed {got}, the file quotes {want}")
    cal = CAL.read_text(encoding="utf-8")
    for frag in ("215 to 290", "108 to 145", "61% to 95%", "64 minutes", "205 to 290", "135 to 210", "68 to 105",
                 "60 to 100", "120 to 180", "60 to 80 minutes", "45 minutes", "32 minutes a week",
                 "15 to 60 minutes"):
        if frag not in cal:
            err(f"calendar lacks the figure {frag!r}")
    for stale in ("285 to 370", "143 to 185", "93% to 132%", "103 to 145"):
        if stale in cal.split("## 11. Review log")[0].replace("(down from 103 to 145)", ""):
            err(f"calendar still quotes the pre-decision figure {stale!r} outside the review log")


def check_misc():
    for p in (CAL, HOOKS, SERIES, REPLY, TREND):
        t = p.read_text(encoding="utf-8")
        for w in ("TODO", "TBD", "lorem"):
            if w in t.replace("HUMAN_TODO", ""):
                warn(f"{p.name}: contains {w}")
        # no URL in the content files that could be mistaken for a checked source
        for u in re.findall(r"https?://\S+", t):
            warn(f"{p.name}: URL present {u[:60]!r}: confirm it is a project source, not an invented one")


def run_pipeline_validator():
    script = ROOT / "pipeline/scripts/queue.py"
    r = subprocess.run([sys.executable, "-B", str(script), "--root", str(ROOT), "validate", str(QDIR)],
                       capture_output=True, text=True, cwd=str(ROOT))
    out = r.stdout
    errs = re.findall(r"ERROR\s+(\d+)\s+FLAG\s+(\d+)", out)
    bad = sum(int(a) + int(b) for a, b in errs)
    if bad:
        err(f"queue.py validate reports {bad} ERROR or FLAG finding(s):\n" + out)
    return out


def guarded(name, fn, *args):
    """Run one check; a crash (missing file, bad input) becomes an ERROR line, never a traceback."""
    try:
        return fn(*args)
    except Exception as exc:  # noqa: BLE001 - deliberate: report and carry on with the other checks
        err(f"check {name} could not run ({type(exc).__name__}: {str(exc)[:100]})")
        return None


def main():
    folders = guarded("queue", check_queue) or []
    cal = guarded("calendar", check_calendar)
    if cal is not None:
        guarded("hooks", check_hooks, cal)
    guarded("replies", check_replies)
    guarded("trend", check_trend)
    guarded("arithmetic", check_arithmetic)
    guarded("misc", check_misc)
    pv = guarded("pipeline validator", run_pipeline_validator) or ""
    print("queue drafts checked:", ", ".join(f.name for f in folders))
    print("pipeline validator summary:", [l for l in pv.splitlines() if "draft(s) checked" in l])
    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    print(f"{len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
