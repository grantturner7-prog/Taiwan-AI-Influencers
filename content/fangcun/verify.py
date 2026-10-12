#!/usr/bin/env python3
"""Offline checks for the 方寸 (fangcun) content and review-queue drafts.

Run from the repository root:   python3 content/fangcun/verify.py

Standard library only. No network calls. The Simplified-character check uses OpenCC if it is installed and is
skipped otherwise. This script is a first-pass filter for the operator and for Claude, NOT a replacement for the
wife's review: it cannot judge tone, naturalness or Taiwan vocabulary beyond the word lists below, and it does not
check any fact against a source.

Exit code 0 = no errors; 1 = at least one error. Warnings are printed but do not fail the run.

Independent review of 2026-10-12 added: a bad or non-UTF-8 post.json is reported as an error (no traceback); caption_zh
must be paste-ready (no title-field note, no braces, no placeholder); a YouTube title must sit in review.notes; the R01
asset must carry its generation prompt; a slide or frame with a character panel must carry the 虛擬角色 badge; the
badge inset must be the 11% / 8% rule; caption_zh must equal the caption block in calendar-30d.md.

Update of 2026-10-12 (decisions D6, OPS-D1 and D3 in DECISIONS.md "recommended answers adopted"): the capacity
arithmetic of calendar section 8 is asserted; the 30-day table in calendar section 3 must respect the OPS-D1 cadence
(Instagram Mon and Thu, YouTube Shorts Tue and Fri, at most 2 of each a week, at least 2 Instagram posts in each of
weeks 1 to 4, no deferred post scheduled); a Reel or Short whose only hold was D6 must carry the D6 conditions in
review.notes and no HOLD or BLOCKED marker; a non-AI diagram asset must name its route (Claude-drawn SVG or
human-built). None of this approves anything.
"""
import datetime
import glob
import json
import math
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
QUEUE = os.path.join(ROOT, "pipeline", "review-queue", "fangcun", "*", "post.json")
HOOKS_MD = os.path.join(ROOT, "content", "fangcun", "hook-library.md")
CAL_MD = os.path.join(ROOT, "content", "fangcun", "calendar-30d.md")

MAINLAND = ["視頻", "質量", "信息", "博主", "軟件", "硬件", "屏幕", "默認", "設置", "鏈接", "賬", "保存", "打印", "卷尺",
            "平米", "厘米", "平方米", "小區", "衛生間", "租房", "戶型", "瓷磚", "吊頂", "排插", "螺絲刀", "空調", "塑料",
            "電飯煲", "煤氣", "家人們", "寶子", "絕絕子", "項目", "性價比", "快遞", "鼠標", "網絡", "登錄", "程序",
            "短視頻", "社交媒體", "智能", "人工智能"]
EXPERIENCE = ["用過", "試過", "買過", "住過", "租過", "去過", "看過", "量過", "摸過", "睡過", "搬過", "裝過", "改造",
              "試坐", "試躺", "愛用", "回購", "踩雷", "開箱", "實測", "親測", "心得", "好用", "神器", "必買", "我家",
              "我的房間", "我租", "我覺得", "推薦", "最好", "第一名", "最划算", "保證"]
HEALTH = ["防霉", "防潮", "除濕效果", "抗菌", "防蟎", "空氣更乾淨", "過敏", "黴", "霉", "睡眠", "健康", "減重", "瘦身", "殺菌"]
OTHER = ["選舉", "投票", "政黨", "候選", "兩岸", "雙11", "雙十一", "限時", "手刀", "最後一天", "折扣", "優惠", "特價",
         "投資", "股票", "基金", "貸款", "房貸", "預售屋", "買房", "房價", "押金", "房東", "租約", "他", "她"]
# Sentences that deny an experience and are therefore intended. Removed before the EXPERIENCE scan.
ALLOWED_DENIALS = ["我沒住過", "沒住過", "請用捲尺量過再算", "不會說好不好用", "沒辦法說好不好用", "沒有用過"]
SIMPLIFIED_FALSE_POSITIVES = {"床->牀", "具->俱", "家->傢", "台->臺", "布->佈", "占->佔"}

errors, warnings = [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def scan_zh(label, text):
    probs = []
    for w in MAINLAND + HEALTH + OTHER:
        if w in text:
            probs.append(w)
    t2 = text
    for a in ALLOWED_DENIALS:
        t2 = t2.replace(a, "")
    probs += [w for w in EXPERIENCE if w in t2]
    for p in probs:
        err("%s: banned or sensitive word %r in %r" % (label, p, text[:40]))
    try:
        import opencc
        conv = opencc.OpenCC("s2t").convert(text)
        if conv != text:
            diffs = {a + "->" + b for a, b in zip(text, conv) if a != b} - SIMPLIFIED_FALSE_POSITIVES
            if diffs:
                warn("%s: possible Simplified characters %s in %r" % (label, sorted(diffs), text[:40]))
    except ImportError:
        pass


def check_arithmetic():
    assert 300 - 150 - 55 == 95 and 95 - 60 == 35
    assert 300 - 120 - 55 == 125 and 125 - 60 == 65
    assert 300 - 150 == 150 and 300 - 55 == 245 and 245 - 60 == 185
    assert 190 + 120 == 310 and 400 - 310 == 90 and min(150, 185) == 150
    assert round(400 / 121, 4) == 3.3058 and 121 / 400 == 0.3025
    assert round(12 * 0.3025, 2) == 3.63 and round(5 * 3.3058, 2) == 16.53
    assert 300 * 400 == 120000 and 120000 / 10000 == 12
    assert round(math.pi * 0.8 * 0.8 / 4, 4) == 0.5027 and round(math.pi * 0.8 * 0.8 / 4 * 0.3025, 2) == 0.15
    assert 50 * 30 * 20 == 30000 and 30000 / 1000 == 30
    dims = {"w": 90, "d": 50, "h": 180}
    door = (80, 200)
    fits = {}
    for travel in dims:
        a, b = [v for k, v in dims.items() if k != travel]
        fits[travel] = (a <= door[0] and b <= door[1]) or (b <= door[0] and a <= door[1])
    assert fits == {"w": True, "d": False, "h": True}, fits
    w0 = datetime.date(2026, 11, 16)
    # Capacity arithmetic, calendar section 8 (decisions of 2026-10-12). The minutes are assumptions; the sums are computed.
    assert 4 * 5 == 20 and 6 * 5 == 30 and 2 * 10 + 2 * 3 == 26 and 3 * 10 + 3 * 3 == 39
    assert 3 * 4 == 12 and 3 * 6 == 18 and 12 * 5 == 60 and 18 * 5 == 90
    assert 6 * 10 + 6 * 3 == 78 and 9 * 10 + 9 * 3 == 117 and 4 * 10 + 4 * 3 == 52
    frames = {"M1": 9 + 8, "M2": 9 + 6, "M3": 1 + 6, "M4": 8 + 6}
    assert frames == {"M1": 17, "M2": 15, "M3": 7, "M4": 14} and sum(frames.values()) == 53
    low = {"M1": 17 + 5 + 10 + 20, "M2": 15 + 5 + 2 * 20, "M3": 7 + 5 + 20, "M4": 14 + 5 + 20}
    high = {"M1": 34 + 10 + 20 + 30, "M2": 30 + 10 + 2 * 30, "M3": 14 + 10 + 30, "M4": 28 + 10 + 30}
    assert low == {"M1": 52, "M2": 60, "M3": 32, "M4": 39} and high == {"M1": 94, "M2": 100, "M3": 54, "M4": 68}
    assert sum(low.values()) == 183 and sum(high.values()) == 316 and 183 / 2 == 91.5 and 316 / 2 == 158
    assert 150 + 65 + 50 + 90 == 355 and 195 + 75 + 65 + 120 == 455
    assert round(53 / 4, 2) == 13.25 and 14 + 5 + 20 == 39 and 28 + 10 + 30 == 68
    assert 2 * 39 == 78 and 2 * 68 == 136 and 78 + 20 == 98 and 136 + 30 == 166
    assert 22 - 4 == 18 and 11 - 2 == 9 and 4 * 4 + 2 == 18
    assert w0.strftime("%a") == "Mon" and datetime.date(2026, 11, 28).strftime("%a") == "Sat"
    assert datetime.date(2026, 12, 12).strftime("%a") == "Sat" and (w0 + datetime.timedelta(days=29)).isoformat() == "2026-12-15"


def check_against_calendar(label, d):
    """The queue JSON and calendar-30d.md are meant to carry identical captions (calendar section 5)."""
    if not os.path.isfile(CAL_MD):
        return
    with open(CAL_MD, encoding="utf-8") as fh:
        cal = fh.read()
    m = re.search(r"^### P\d\d · \w+ " + re.escape(d.get("scheduled_date", "?")) + r".*?(?=^### P\d\d · |^## 6\.)", cal, re.S | re.M)
    if not m:
        err("%s: no calendar block found for %s" % (label, d.get("scheduled_date")))
        return
    cap = re.search(r"\*\*Caption \(zh-TW DRAFT\)\*\*[^\n]*\n\n```\n(.*?)\n```", m.group(0), re.S)
    if not cap or cap.group(1) != d.get("caption_zh"):
        err("%s: caption_zh differs from the calendar block" % label)


def check_json():
    required = ["id", "persona", "platform", "format", "scheduled_date", "pillar", "hook_zh", "caption_zh",
                "caption_gloss_en", "hashtags", "on_screen_label_zh", "ai_label_flag", "sponsorship_flag",
                "sponsorship_type", "sources", "media", "review"]
    files = sorted(glob.glob(QUEUE))
    if not files:
        err("no review-queue files found")
    for f in files:
        label = os.path.basename(os.path.dirname(f))
        try:
            with open(f, encoding="utf-8") as fh:
                d = json.load(fh)
        except (OSError, ValueError) as e:  # bad JSON or bad UTF-8 must be an error, not a traceback
            err("%s: cannot read or parse post.json (%s)" % (label, e))
            continue
        if not isinstance(d, dict):
            err("%s: post.json must be a JSON object" % label)
            continue
        for k in required:
            if k not in d:
                err("%s: missing field %s" % (label, k))
        for k in set(d) - set(required):
            err("%s: unexpected field %s" % (label, k))
        if d.get("platform") not in ("instagram", "threads", "youtube_shorts", "facebook"):
            err("%s: bad platform" % label)
        if d.get("format") not in ("carousel", "reel", "short", "text", "image"):
            err("%s: bad format" % label)
        if d.get("ai_label_flag") is not True:
            err("%s: ai_label_flag must be true" % label)
        if d.get("sponsorship_type") not in ("none", "paid", "gifted", "affiliate"):
            err("%s: bad sponsorship_type" % label)
        rv = d.get("review", {})
        if rv.get("approved") is not False or rv.get("wife_language") != "pending" or rv.get("operator_facts") != "pending":
            err("%s: review fields must start pending and approved=false" % label)
        if not re.match(r"^fangcun-\d{4}-\d{2}-\d{2}-\d{2}$", d.get("id", "")):
            err("%s: bad id" % label)
        if label.replace("_", "-") != d.get("id", "").replace("fangcun-", ""):
            err("%s: folder name does not match id" % label)
        if d.get("scheduled_date") == "2026-11-28":
            err("%s: scheduled on the recalled polling day" % label)
        if len(d.get("hook_zh", "")) > 20:
            err("%s: hook longer than 20 characters" % label)
        if not d.get("caption_zh", "").startswith("【AI 虛擬角色】"):
            err("%s: caption does not start with the AI disclosure line" % label)
        if not os.path.isfile(os.path.join(os.path.dirname(f), "media", ".gitkeep")):
            warn("%s: media/.gitkeep missing" % label)
        for m in d.get("media", []):
            if set(m) != {"path", "description", "shot_prompt"} or m["path"] != "PENDING":
                err("%s: media item must have path PENDING, description, shot_prompt" % label)
        for s in d.get("sources", []):
            if set(s) != {"claim", "url", "date"}:
                err("%s: source item keys" % label)
            if s.get("url") == "" and "坪" in s.get("claim", "") and "ARITHMETIC" not in s.get("claim", ""):
                err("%s: a factual source has an empty url" % label)
        blocked = any("UNVERIFIED-OPERATOR-TO-FILL" in s.get("url", "") for s in d.get("sources", []))
        if blocked:
            warn("%s: BLOCKED until the source placeholder is filled by the operator" % label)
        # Added in the independent review of 2026-10-12.
        cap = d.get("caption_zh", "")
        if "標題欄" in cap or "{" in cap or "}" in cap or "UNVERIFIED" in cap:
            err("%s: caption_zh must be paste-ready: no title-field note, no braces, no placeholder" % label)
        if d.get("platform") == "youtube_shorts" and "YOUTUBE TITLE FIELD" not in d.get("review", {}).get("notes", ""):
            err("%s: YouTube title must be recorded in review.notes (it is not part of caption_zh)" % label)
        for s in d.get("sources", []):
            if s.get("url") == "" and not (s.get("claim", "").startswith("ARITHMETIC ONLY") or s.get("claim", "").startswith("NO FACTUAL CLAIM")):
                err("%s: a source with an empty url must start ARITHMETIC ONLY or NO FACTUAL CLAIM" % label)
        for m in d.get("media", []):
            desc, sp = m.get("description", ""), m.get("shot_prompt", "")
            if not sp.strip():
                err("%s: empty shot_prompt" % label)
            if "golden set R01" in desc and "SUBJECT:" not in sp:
                err("%s: the R01 asset must carry the R01 generation prompt, not only a pointer" % label)
            if "8% from the edges" in desc:
                err("%s: badge inset must be 11%% top/bottom and 8%% sides (qa-checklist D3)" % label)
            if "USES: A" in desc and "BADGE: 「AI 生成｜示意圖」" in desc:
                err("%s: a slide or frame with a character panel must carry the 虛擬角色 badge: %s" % (label, desc[:30]))
            if "AI-generated photoreal image" in desc and "label added in post" not in desc:
                err("%s: AI asset description must say the label is added in post" % label)
        check_against_calendar(label, d)
        for fld in ("hook_zh", "caption_zh", "on_screen_label_zh"):
            scan_zh("%s.%s" % (label, fld), d.get(fld, ""))
        for tag in d.get("hashtags", []):
            scan_zh("%s.hashtag" % label, tag)
        for m in d.get("media", []):
            mm = re.search(r"TEXT zh-TW \(DRAFT\): (.*?) \| GLOSS", m["description"], re.S)
            if mm:
                scan_zh("%s.media" % label, mm.group(1))
    return len(files)


DEFERRED = {"P13", "P14", "P19", "P20"}  # deferred by OPS-D1 (calendar section 6.1)
D6_NOTE_MARKERS = ["D6", "persistent", "no animation of the face", "no synthetic voice", "AI label"]


def check_decisions():
    """D6 and D3, as applied to the queue drafts (decisions of 2026-10-12)."""
    for f in sorted(glob.glob(QUEUE)):
        label = os.path.basename(os.path.dirname(f))
        try:
            with open(f, encoding="utf-8") as fh:
                d = json.load(fh)
        except (OSError, ValueError):
            continue  # check_json already reported it
        if not isinstance(d, dict):
            continue
        notes = d.get("review", {}).get("notes", "")
        held = "HOLD" in notes or "BLOCKED" in notes
        src_blocked = any("UNVERIFIED-OPERATOR-TO-FILL" in s.get("url", "") for s in d.get("sources", []))
        if d.get("format") in ("reel", "short"):
            for mk in D6_NOTE_MARKERS:
                if mk not in notes:
                    err("%s: a Reel or Short must carry the D6 condition %r in review.notes" % (label, mk))
            if held and not src_blocked:
                err("%s: HOLD or BLOCKED marker left on a video post that is no longer held for another reason" % label)
        for m in d.get("media", []):
            sp = m.get("shot_prompt", "")
            if sp.startswith("NOT AI-GENERATED") and "DRAWN BY CLAUDE AS SVG" not in sp and "HUMAN-BUILT" not in sp:
                err("%s: a non-AI asset must name its route (Claude-drawn SVG or human-built)" % label)
            if "approved" in m.get("path", "").lower():
                err("%s: media path must stay PENDING" % label)


def check_cadence():
    """OPS-D1: calendar section 3 must hold 2 Instagram + 2 YouTube Shorts a week and schedule no deferred post."""
    if not os.path.isfile(CAL_MD):
        return 0
    with open(CAL_MD, encoding="utf-8") as fh:
        txt = fh.read()
    sec = re.search(r"^## 3\. The 30 days at a glance.*?(?=^## 4\.)", txt, re.S | re.M)
    if not sec:
        err("calendar section 3 not found")
        return 0
    weeks, ids = {}, []
    for m in re.finditer(r"^\| (\d+) \| (\d{4}-\d{2}-\d{2}) \| (\w{3}) \| (W\d) \| (.*?) \|(.*)\|$", sec.group(0), re.M):
        _day, date, _wd, wk, posts, _notes = m.groups()
        wd = datetime.date.fromisoformat(date).weekday()  # Mon = 0
        for pm in re.finditer(r"(P\d\d) (IG|YT)", posts):
            pid, plat = pm.groups()
            ids.append(pid)
            weeks.setdefault(wk, {"IG": [], "YT": []})[plat].append(pid)
            if plat == "IG" and wd not in (0, 3):
                err("%s: Instagram post on a day other than Mon or Thu (OPS-D1 cadence)" % pid)
            if plat == "YT" and wd not in (1, 4):
                err("%s: YouTube Short on a day other than Tue or Fri (OPS-D1 cadence)" % pid)
    for pid in sorted(DEFERRED & set(ids)):
        err("%s is deferred by OPS-D1 but appears in the 30-day table" % pid)
    for wk, v in sorted(weeks.items()):
        if len(v["IG"]) > 2 or len(v["YT"]) > 2:
            err("%s: more than 2 Instagram or 2 YouTube posts (OPS-D1 holds 4 a week)" % wk)
    for wk in ("W1", "W2", "W3", "W4"):
        if len(weeks.get(wk, {}).get("IG", [])) < 2:
            err("%s: fewer than 2 posts on the primary platform (Instagram)" % wk)
    if len(ids) != len(set(ids)) or len(ids) != 18:
        err("30-day table should schedule 18 distinct posts after OPS-D1, found %d" % len(ids))
    return len(ids)


def check_hooks():
    n = 0
    for path, pat in ((HOOKS_MD, r"^\| H\d+ \| 「(.+?)」"), (CAL_MD, r"^\| P\d\d \|.*?\| 「(.+?)」<br>")):
        if not os.path.isfile(path):
            continue
        for line in open(path, encoding="utf-8"):
            m = re.match(pat, line)
            if m:
                n += 1
                h = m.group(1)
                if len(h) > 20:
                    err("hook longer than 20 characters: %s" % h)
                scan_zh("hook", h)
    return n


if __name__ == "__main__":
    try:
        check_arithmetic()
        print("arithmetic and dates: ok")
    except AssertionError as e:
        err("arithmetic or date assertion failed: %r" % (e,))
    n = check_json()
    check_decisions()
    scheduled = check_cadence()
    h = check_hooks()
    print("queue files checked: %d; hooks checked: %d; posts in the 30-day table: %d" % (n, h, scheduled))
    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    print("%d error(s), %d warning(s)" % (len(errors), len(warnings)))
    sys.exit(1 if errors else 0)
