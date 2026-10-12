#!/usr/bin/env python3
"""reviewqueue.py - the review queue: scaffold, validate and list draft posts.

Standard library only. No network. The command line entry point is queue.py (same folder);
the logic lives here so that nothing needs to import a module called 'queue' (see queue.py).

A draft is a folder   pipeline/review-queue/<persona-slug>/<YYYY-MM-DD>_<NN>/
holding post.json and an empty media/ folder (with .gitkeep).

THE HARD LINE: this program never sets a review field to approved. It writes review fields
only when it scaffolds a NEW draft, and it writes them as pending / pending / false. After
that only a human edits them. `approve` only REPORTS whether a draft is ready.

Validation levels
  ERROR  breaks the post format or a hard rule (fix it)
  FLAG   banned wording found by the keyword net (a human edits the text; nothing is auto-fixed)
  WARN   advisory
  INFO   context (for example a sentence that denies an experience, or a reminder)
validate exits 1 if any ERROR or FLAG exists (and any WARN with --strict).

Every zh-TW string the scaffold writes is an AI draft for the wife to review.
"""
from __future__ import annotations

import csv
import datetime as dt
import json
import re
import sys
from pathlib import Path

import gen_image
import ground_rules as gr
from ground_rules import Finding

ROOT = Path(__file__).resolve().parents[2]
QUEUE_REL = Path("pipeline") / "review-queue"

PLATFORMS = ("instagram", "threads", "youtube_shorts", "facebook")
FORMATS = ("carousel", "reel", "short", "text", "image")
SPONSOR_TYPES = ("none", "paid", "gifted", "affiliate")
REVIEW_STATES = ("pending", "approved", "changes")

# slug: (zh-TW name, status, planned platforms in strategy/portfolio.md 2B). Names and handles are
# provisional and uncleared (personas/README.md).
PERSONAS = {
    "fangcun": ("方寸", "pilot", ("instagram", "youtube_shorts")),
    "buzhou": ("步驟", "pilot", ("youtube_shorts", "threads")),
    "sehuan": ("色環", "pilot", ("instagram", "threads")),
    "jiehua": ("接話", "provisional", ("threads", "youtube_shorts")),
    "zhuancheng": ("轉乘", "provisional", ("youtube_shorts", "instagram")),
    "suisui": ("歲歲", "provisional", ("facebook", "youtube_shorts")),
    "licheng": ("里程", "provisional", ("facebook", "youtube_shorts")),
    "guige": ("規格", "provisional", ("instagram",)),
    "dengyixia": ("等一下", "lawyer-gated", ("facebook", "youtube_shorts")),
    "guiwei": ("歸位", "lawyer-gated", ("youtube_shorts",)),
}
# Candidate handles from personas/README.md section 2 (none checked or cleared). Used only to
# catch one persona naming another (Ground rule 8).
HANDLE_CANDIDATES = {
    "fangcun": ["fangcun_ai", "fangcun.cm", "fangcun.plan"],
    "buzhou": ["step0_ai", "stepwise_ai", "buzhou_steps"],
    "sehuan": ["sehuan.hues", "sehuan.wheel", "sehuan_ai"],
    "jiehua": ["jiehua_ai", "jiehua_en", "jiehua.reply"],
    "zhuancheng": ["zhuancheng_ai", "zhuancheng.join", "zhuancheng.route"],
    "suisui": ["suisui.ai", "suisui.cards", "suisui.notes"],
    "licheng": ["licheng.ai", "licheng.rules", "licheng.manual"],
    "guige": ["specdecoder_ai", "guige.specs", "specsheet_ai"],
    "dengyixia": ["dengyixia.ai", "halfpace.ai"],
    "guiwei": ["rerack_ai", "guiwei.gym", "gymnotice_ai"],
}

FORMAT_PLATFORMS = {
    "reel": {"instagram", "facebook"},
    "short": {"youtube_shorts"},
    "carousel": {"instagram", "threads", "facebook"},
    "image": {"instagram", "threads", "facebook"},
    "text": {"threads", "facebook"},
}

DISCLOSURE_RE = re.compile(r"^【AI\s*虛擬角色】")
LABEL_RE = re.compile(r"AI\s*生成")
SPONSOR_TAGS = {
    "paid": ("【業配】", "【合作內容】"),
    "gifted": ("【廠商提供】",),
    "affiliate": ("【含分潤連結】",),
}
ALL_SPONSOR_TAGS = tuple(t for tags in SPONSOR_TAGS.values() for t in tags)
DEFAULT_LABEL = "AI 生成｜虛擬角色"

W0 = dt.date(2026, 11, 16)  # assumption (DECISIONS.md): first pilot post date
DATE_WARNINGS = {
    "2027-02-28": "228 Peace Memorial Day: do not post (strategy/portfolio.md 2.5)",
    "2026-11-28": "recalled local-election date, UNVERIFIED: no posting, no election hooks (portfolio.md 2.5)",
}
GHOST_MONTH = (dt.date(2027, 8, 2), dt.date(2027, 8, 31))  # computed in research/culture.md 5.4
WEEKLY_APPROVAL_CEILING = 22  # portfolio.md 5.1, assumption
NO_EXTERNAL_PREFIXES = ("ARITHMETIC ONLY", "NO FACTUAL CLAIM")
LIMITS = {"instagram": 2200, "threads": 500}  # caption characters, recalled and UNVERIFIED

REQUIRED_STR = ["id", "persona", "platform", "format", "scheduled_date", "pillar", "hook_zh", "caption_zh",
                "caption_gloss_en", "on_screen_label_zh", "sponsorship_type"]
REQUIRED_OTHER = {"hashtags": list, "ai_label_flag": bool, "sponsorship_flag": bool, "sources": list,
                  "media": list, "review": dict}
KNOWN_KEYS = set(REQUIRED_STR) | set(REQUIRED_OTHER)


# --------------------------------------------------------------------------- scaffold

class QueueError(Exception):
    pass


def queue_dir(root: Path) -> Path:
    return root / QUEUE_REL


def disclosure_line(persona: str, platform: str, fmt: str) -> str:
    name = PERSONAS[persona][0]
    if platform == "youtube_shorts":
        return f"【AI 虛擬角色】本影片由 AI 生成的虛擬角色「{name}」發布，畫面為 AI 生成，並非真人。"
    if fmt == "text":
        return f"【AI 虛擬角色】本篇由 AI 生成的虛擬角色「{name}」發布。"
    return f"【AI 虛擬角色】本篇由 AI 生成的虛擬角色「{name}」發布，圖像為 AI 生成，並非真人。"


def next_number(persona_dir: Path, date: str) -> int:
    used = set()
    if persona_dir.is_dir():
        for d in persona_dir.iterdir():
            m = re.fullmatch(re.escape(date) + r"_(\d{2})", d.name)
            if m:
                used.add(int(m.group(1)))
    n = 1
    while n in used:
        n += 1
    return n


def new_draft(root: Path, persona: str, platform: str, fmt: str, date: str, pillar: str = "",
              number: int | None = None) -> Path:
    if persona not in PERSONAS:
        raise QueueError(f"unknown persona {persona!r}; known: {', '.join(PERSONAS)}")
    if platform not in PLATFORMS:
        raise QueueError(f"platform must be one of {', '.join(PLATFORMS)}")
    if fmt not in FORMATS:
        raise QueueError(f"format must be one of {', '.join(FORMATS)}")
    try:
        d = dt.date.fromisoformat(date)
    except ValueError:
        raise QueueError(f"date must be YYYY-MM-DD: {date!r}")
    if d.isoformat() != date:
        raise QueueError(f"date must be YYYY-MM-DD: {date!r}")
    pdir = queue_dir(root) / persona
    n = number if number is not None else next_number(pdir, date)
    if not 1 <= n <= 99:
        raise QueueError("number must be 1 to 99")
    folder = pdir / f"{date}_{n:02d}"
    if folder.exists():
        raise QueueError(f"draft already exists: {folder}")
    post = {
        "id": f"{persona}-{date}-{n:02d}",
        "persona": persona,
        "platform": platform,
        "format": fmt,
        "scheduled_date": date,
        "pillar": pillar,
        "hook_zh": "",
        "caption_zh": disclosure_line(persona, platform, fmt) + "\n",
        "caption_gloss_en": "",
        "hashtags": [],
        "on_screen_label_zh": DEFAULT_LABEL,
        "ai_label_flag": True,
        "sponsorship_flag": False,
        "sponsorship_type": "none",
        "sources": [],
        "media": ([] if fmt == "text" else [{"path": "PENDING", "description": "", "shot_prompt": ""}]),
        "review": {"wife_language": "pending", "operator_facts": "pending", "approved": False, "notes": ""},
    }
    (folder / "media").mkdir(parents=True)
    (folder / "media" / ".gitkeep").write_text("", encoding="utf-8")
    write_post(folder / "post.json", post)
    return folder


def write_post(path: Path, post: dict) -> None:
    path.write_text(json.dumps(post, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


# --------------------------------------------------------------------------- loading

def load_post(path: Path):
    """Return (post, error_message)."""
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return None, "file is not valid UTF-8"
    except OSError as e:
        return None, f"cannot read file: {e.strerror}"
    try:
        return json.loads(text), None
    except ValueError as e:
        return None, f"invalid JSON: {e}"


def find_posts(root: Path, targets=None) -> list[Path]:
    """Paths of post.json files. targets: None for all drafts, else folders or post.json paths."""
    if not targets:
        return sorted(queue_dir(root).glob("*/*/post.json"))
    out = []
    for t in targets:
        p = Path(t)
        if not p.is_absolute() and not p.exists():
            p = root / p
        if p.is_dir():
            if (p / "post.json").exists():
                out.append(p / "post.json")
            else:
                out.extend(sorted(p.glob("*/post.json")) or sorted(p.glob("*/*/post.json")))
        else:
            out.append(p)
    return out


def load_provenance_paths(root: Path) -> set[str]:
    path = root / "assets" / "provenance.csv"
    if not path.exists():
        return set()
    out = set()
    with open(path, newline="", encoding="utf-8") as fh:
        rd = csv.DictReader(fh)
        for row in rd:
            if row.get("asset_path"):
                out.add(row["asset_path"].strip().replace("\\", "/"))
    return out


# --------------------------------------------------------------------------- validation

_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_PLACEHOLDER_RE = re.compile(r"UNVERIFIED|TODO|TBD|OPERATOR-TO-FILL|\{[^}]*\}|<[^>]*>|待補|待填", re.IGNORECASE)
_SRC_DATE_RE = re.compile(r"^\d{4}(?:-\d{2}(?:-\d{2})?)?$")


def _body_after_first_line(caption: str) -> str:
    parts = caption.strip().split("\n", 1)
    return parts[1].strip() if len(parts) > 1 else ""


def validate_post(post, folder: Path | None = None, root: Path = ROOT, *, today: dt.date | None = None,
                  prov_paths: set | None = None) -> list[Finding]:
    F: list[Finding] = []

    def add(level, code, field, msg):
        F.append(Finding(level, code, field, msg))

    if not isinstance(post, dict):
        add("ERROR", "FORMAT", "post.json", "top level must be a JSON object")
        return F

    # --- presence and types
    for key in REQUIRED_STR:
        if key not in post:
            add("ERROR", "MISSING_FIELD", key, "required field is missing")
        elif not isinstance(post[key], str):
            add("ERROR", "BAD_TYPE", key, "must be a string")
    for key, typ in REQUIRED_OTHER.items():
        if key not in post:
            add("ERROR", "MISSING_FIELD", key, "required field is missing")
        elif not isinstance(post[key], typ):
            add("ERROR", "BAD_TYPE", key, f"must be a {typ.__name__}")
    for key in post:
        if key not in KNOWN_KEYS:
            add("WARN", "UNKNOWN_FIELD", key, "not in the post.json format (typo?)")

    def s(key):
        v = post.get(key)
        return v if isinstance(v, str) else ""

    for key in ("pillar", "hook_zh", "caption_zh", "caption_gloss_en"):
        if key in post and isinstance(post[key], str) and not post[key].strip():
            add("ERROR", "EMPTY", key, "is empty (a scaffold starts empty; fill it in)")

    persona, platform, fmt, date = s("persona"), s("platform"), s("format"), s("scheduled_date")

    # --- enums
    if persona and persona not in PERSONAS:
        add("ERROR", "UNKNOWN_PERSONA", "persona", f"{persona!r} is not a known persona slug")
    if platform and platform not in PLATFORMS:
        add("ERROR", "BAD_ENUM", "platform", f"{platform!r} not in {', '.join(PLATFORMS)}")
    if fmt and fmt not in FORMATS:
        add("ERROR", "BAD_ENUM", "format", f"{fmt!r} not in {', '.join(FORMATS)}")

    # --- date
    d = None
    if date:
        if not _DATE_RE.match(date):
            add("ERROR", "BAD_DATE", "scheduled_date", "must be YYYY-MM-DD")
        else:
            try:
                d = dt.date.fromisoformat(date)
            except ValueError:
                add("ERROR", "BAD_DATE", "scheduled_date", "not a real calendar date")
    if d:
        if date in DATE_WARNINGS:
            add("WARN", "CALENDAR", "scheduled_date", DATE_WARNINGS[date])
        if GHOST_MONTH[0] <= d <= GHOST_MONTH[1]:
            add("WARN", "CALENDAR", "scheduled_date", "inside the 2027 ghost month (computed in research/culture.md 5.4): no launches; neutral explanation only")
        if d < W0:
            add("WARN", "CALENDAR", "scheduled_date", f"before the assumed first-post date W0 {W0.isoformat()} (assumption; shift if gates slip)")
        if today and d < today:
            add("WARN", "CALENDAR", "scheduled_date", "date is in the past")

    # --- id and folder consistency
    pid = s("id")
    if pid:
        m = re.fullmatch(r"([a-z]+)-(\d{4}-\d{2}-\d{2})-(\d{2})", pid)
        if not m:
            add("ERROR", "ID_FORMAT", "id", "must look like <slug>-YYYY-MM-DD-NN")
        else:
            if persona and m.group(1) != persona:
                add("ERROR", "ID_MISMATCH", "id", "slug part does not match persona")
            if date and m.group(2) != date:
                add("ERROR", "ID_MISMATCH", "id", "date part does not match scheduled_date")
            if folder is not None:
                if folder.name != f"{m.group(2)}_{m.group(3)}":
                    add("ERROR", "ID_MISMATCH", "id", f"folder name {folder.name!r} does not match the id")
                if folder.parent.name != m.group(1):
                    add("ERROR", "ID_MISMATCH", "id", f"parent folder {folder.parent.name!r} is not the persona slug")

    # --- persona / platform / format fit
    if persona in PERSONAS:
        zh, status, planned = PERSONAS[persona]
        if status == "provisional":
            add("WARN", "PERSONA_STATUS", "persona", f"{persona} ({zh}) is provisional: designed only, not launched (strategy/portfolio.md 2.5)")
        elif status == "lawyer-gated":
            add("WARN", "PERSONA_STATUS", "persona", f"{persona} ({zh}) is lawyer-gated: no launch until the lawyer's written answers are in")
        if platform in PLATFORMS and platform not in planned:
            add("WARN", "PLATFORM_PLAN", "platform", f"{platform} is not in {persona}'s planned platforms ({', '.join(planned)})")
    if fmt in FORMAT_PLATFORMS and platform in PLATFORMS and platform not in FORMAT_PLATFORMS[fmt]:
        add("WARN", "FORMAT_PLATFORM", "format", f"format {fmt} is unusual on {platform}")
    if platform == "youtube_shorts" and fmt in FORMATS and fmt != "short":
        add("WARN", "FORMAT_PLATFORM", "format", "youtube_shorts posts are normally format 'short'")

    # --- disclosure (Ground rule 1)
    caption = s("caption_zh")
    if caption.strip() and not DISCLOSURE_RE.match(caption.lstrip()):
        add("ERROR", "NO_DISCLOSURE_LINE", "caption_zh", "first line must start with 【AI 虛擬角色】 (Ground rule 1: first caption line)")
    if caption.strip() and DISCLOSURE_RE.match(caption.lstrip()) and not _body_after_first_line(caption):
        add("ERROR", "EMPTY", "caption_zh", "only the disclosure line is present; the caption body is empty")
    if post.get("ai_label_flag") is not True and "ai_label_flag" in post and isinstance(post["ai_label_flag"], bool):
        add("ERROR", "AI_LABEL", "ai_label_flag", "must be true: the platform's AI label is switched on by hand for every post (studio rule)")
    label = s("on_screen_label_zh")
    text_only = fmt == "text" and not post.get("media")
    if "on_screen_label_zh" in post and isinstance(post["on_screen_label_zh"], str):
        if not label.strip():
            add("ERROR", "NO_ONSCREEN_LABEL", "on_screen_label_zh", "on-screen label is required (Ground rule 1)")
        elif not LABEL_RE.search(label):
            add("WARN" if text_only else "ERROR", "NO_ONSCREEN_LABEL", "on_screen_label_zh",
                "label should contain 'AI 生成' (for example 「AI 生成｜虛擬角色」 or 「AI 生成｜示意圖」)")

    # --- hashtags
    tags = post.get("hashtags")
    if isinstance(tags, list):
        seen = set()
        for i, t in enumerate(tags):
            f = f"hashtags[{i}]"
            if not isinstance(t, str) or not t.strip():
                add("ERROR", "BAD_HASHTAG", f, "must be a non-empty string")
                continue
            if not t.startswith("#") or re.search(r"\s", t) or len(t) < 2:
                add("ERROR", "BAD_HASHTAG", f, f"{t!r} must start with # and contain no spaces")
            if t.lower() in seen:
                add("WARN", "BAD_HASHTAG", f, f"duplicate hashtag {t!r}")
            seen.add(t.lower())
            F.extend(gr.scan_text(t, f))
        if len(tags) > 30:
            add("WARN", "HASHTAG_COUNT", "hashtags", "more than 30 hashtags (Instagram limit as recalled, unverified; the live limit may be lower: check the composer)")

    # --- sponsorship
    flag, stype = post.get("sponsorship_flag"), s("sponsorship_type")
    if stype and stype not in SPONSOR_TYPES:
        add("ERROR", "BAD_ENUM", "sponsorship_type", f"{stype!r} not in {', '.join(SPONSOR_TYPES)}")
    elif isinstance(flag, bool) and stype:
        if flag and stype == "none":
            add("ERROR", "SPONSORSHIP_MISMATCH", "sponsorship_flag", "flag is true but sponsorship_type is 'none'")
        if not flag and stype != "none":
            add("ERROR", "SPONSORSHIP_MISMATCH", "sponsorship_flag", f"sponsorship_type is {stype!r} but flag is false")
    head = "\n".join(caption.strip().split("\n")[:4])
    if stype in SPONSOR_TAGS:
        if not any(t in head for t in SPONSOR_TAGS[stype]):
            add("ERROR", "SPONSOR_TAG_MISSING", "caption_zh",
                f"sponsorship_type {stype} needs {' or '.join(SPONSOR_TAGS[stype])} within the first lines (under the AI line)")
        if stype in ("paid", "gifted") and "沒有使用過" not in caption:
            add("WARN", "PAID_NO_USE_LINE", "caption_zh",
                "paid/gifted posts carry 「角色沒有使用過此商品，內容僅就公開規格與資料說明。」 (portfolio.md 1.4)")
        add("INFO", "PLATFORM_TOOLS", "sponsorship_flag",
            "also switch on the platform's paid-partnership tool and its AI-disclosure control by hand (BRIEF rule 5)")
    for ty, tg in SPONSOR_TAGS.items():
        for t in tg:
            if t in caption and stype != ty:
                add("ERROR", "SPONSOR_UNFLAGGED", "sponsorship_type", f"caption carries {t} but sponsorship_type is {stype!r}, expected {ty!r}")
    if stype == "none":
        sponsor_words = re.compile(r"業配|合作內容|贊助|廠商提供|分潤|聯盟行銷|折扣碼|優惠碼|\bsponsored\b|\baffiliate\b|#ad\b|\bgifted\b",
                                   re.IGNORECASE)
        for fname, txt in [("hook_zh", s("hook_zh")), ("caption_zh", caption)] + \
                [(f"hashtags[{i}]", t) for i, t in enumerate(post.get("hashtags") if isinstance(post.get("hashtags"), list) else [])
                 if isinstance(t, str)]:
            m = sponsor_words.search(txt)
            if m:
                add("WARN", "SPONSOR_WORD", fname,
                    f"mentions {m.group(0)!r} but sponsorship_type is 'none': if this is a paid, gifted or affiliate relationship, "
                    "set the type and add the caption tag (BRIEF rule 5); if it is a denial or a general explainer, ignore")
    if re.search(r"https?://", caption) and stype == "none":
        add("WARN", "LINK_NO_SPONSOR", "caption_zh", "a link in the caption: if it is an affiliate link set sponsorship_type 'affiliate'")

    # --- sources and claims
    hook = s("hook_zh")
    claim_text = hook + "\n" + caption
    strong = gr.has_strong_claim(claim_text)
    numeric = gr.has_numeric(claim_text)
    sources = post.get("sources")
    if isinstance(sources, list):
        n_arith = 0
        for i, src in enumerate(sources):
            f = f"sources[{i}]"
            if not isinstance(src, dict) or not all(isinstance(src.get(k), str) for k in ("claim", "url", "date")):
                add("ERROR", "BAD_SOURCE", f, "must be an object with string fields claim, url, date")
                continue
            if not src["claim"].strip():
                add("ERROR", "BAD_SOURCE", f, "claim is empty")
            url, dstr = src["url"].strip(), src["date"].strip()
            # Conventions used by the content stream: an entry that makes no external factual claim starts with
            # "ARITHMETIC ONLY" or "NO FACTUAL CLAIM" and may have an empty url and date.
            arith = src["claim"].strip().upper().startswith(NO_EXTERNAL_PREFIXES)
            n_arith += 1 if arith else 0
            placeholder = bool(_PLACEHOLDER_RE.search(url + " " + dstr))
            if placeholder:
                add("WARN", "PLACEHOLDER", f, "url/date is still a placeholder: the operator must paste the real page and date before approval")
            elif not url:
                if strong and not arith:
                    add("ERROR", "SOURCE_NO_URL", f, "url is empty but the post makes factual claims (url may be empty only when there is no claim; such entries start with 'ARITHMETIC ONLY' or 'NO FACTUAL CLAIM')")
            elif not re.match(r"https?://", url):
                add("WARN", "SOURCE_URL", f, "url does not start with http:// or https://")
            if not placeholder and not (arith and not dstr):
                if dstr.lower() == "unverified":
                    add("WARN", "SOURCE_DATE", f, "date is 'unverified'")
                elif not _SRC_DATE_RE.match(dstr):
                    add("WARN", "SOURCE_DATE", f, "date should be YYYY, YYYY-MM or YYYY-MM-DD (the date of the source or the check)")
        if sources and strong and n_arith == len(sources):
            add("ERROR", "NO_REAL_SOURCE", "sources", "the text makes factual claims but every source entry says arithmetic-only / no factual claim")
        if not sources:
            if strong:
                add("ERROR", "NO_SOURCES", "sources", "the text makes factual claims (official / spec / date / price / rule wording) but sources is empty")
            elif numeric:
                lvl = "INFO" if "示意" in claim_text else "WARN"
                add(lvl, "NUMBERS_NO_SOURCE", "sources", "the text contains numbers and no sources: add a source, or tag illustrative numbers 示意數字")

    # --- unfilled placeholders such as {廠商} (must not be posted)
    for field_name, text in (("hook_zh", hook), ("caption_zh", caption)):
        for m in re.finditer(r"\{[^}]*\}", text):
            add("WARN", "PLACEHOLDER", field_name, f"unfilled placeholder {m.group(0)}: fill it before approval")

    # --- banned-term scan (flag, never fix)
    F.extend(gr.scan_text(hook, "hook_zh"))
    F.extend(gr.scan_text(caption, "caption_zh"))
    F.extend(gr.scan_text(label, "on_screen_label_zh"))
    others = [slug for slug in PERSONAS if slug != persona]
    for field_name, text in (("hook_zh", hook), ("caption_zh", caption)):
        low = text.lower()
        for slug in others:
            if re.search(r"(?<![a-z0-9])" + re.escape(slug) + r"(?![a-z0-9])", low):
                add("FLAG", "PERSONA_CROSS_MENTION", field_name, f"names another persona ({slug}): personas never vouch for or tag each other (Ground rule 8)")
        for other in others:
            for h in HANDLE_CANDIDATES.get(other, []):
                if h in low:
                    add("FLAG", "PERSONA_CROSS_MENTION", field_name, f"contains another persona's handle candidate {h!r}: personas never tag or link each other")
        for slug in others:
            zh = PERSONAS[slug][0]
            z = re.escape(zh)
            if re.search("[「『《【]" + z + "[」』》】]|@" + z + "|" + z + "角色", text):
                add("WARN", "PERSONA_NAME_MENTION", field_name,
                    f"{zh!r} is another persona's name used like a name (quoted, @-tagged or followed by 角色): personas never vouch for or tag each other (Ground rule 8). Ignore if it is the ordinary word.")
        if "@" in text:
            add("WARN", "MENTION", field_name, "contains an @mention: personas never tag each other; sponsor tags use the paid-partnership tool")
    lim = LIMITS.get(platform)
    if lim and len(caption) > lim:
        add("WARN", "LENGTH", "caption_zh", f"{len(caption)} characters; {platform} limit is about {lim} (recalled, unverified)")

    # --- media
    media = post.get("media")
    n_pending = 0
    if isinstance(media, list):
        if not media and fmt in FORMATS and fmt != "text":
            add("ERROR", "NO_MEDIA", "media", f"format {fmt} needs at least one media entry (use path PENDING plus a shot_prompt)")
        for i, m in enumerate(media):
            f = f"media[{i}]"
            if not isinstance(m, dict) or not all(isinstance(m.get(k), str) for k in ("path", "description", "shot_prompt")):
                add("ERROR", "BAD_MEDIA", f, "must be an object with string fields path, description, shot_prompt")
                continue
            if m["path"].strip() == "PENDING":
                if not m["shot_prompt"].strip():
                    add("ERROR", "EMPTY", f + ".shot_prompt", "PENDING media must carry the generation prompt")
                if not m["description"].strip():
                    add("ERROR", "EMPTY", f + ".description", "describe what the media shows")
                n_pending += 1
            else:
                rel = m["path"].strip().replace("\\", "/")
                cands = []
                if folder is not None:
                    cands.append(folder / rel)
                cands.append(root / rel)
                if not any(c.is_file() for c in cands):
                    add("ERROR", "MEDIA_MISSING_FILE", f, f"file not found: {rel}")
                if prov_paths is not None:
                    alt = [rel]
                    if folder is not None:
                        try:
                            alt.append((folder / rel).resolve().relative_to(root.resolve()).as_posix())
                        except ValueError:
                            pass
                    if not any(a in prov_paths for a in alt):
                        add("WARN", "NO_PROVENANCE", f, f"no row in assets/provenance.csv for {rel} (Ground rule 2: log every asset)")
            if m["shot_prompt"].strip():
                pc = gen_image.check_prompt(m["shot_prompt"], gen_image.load_extra_blocklist())
                for b in pc.blocked:
                    add("ERROR", "PROMPT_BLOCKED", f + ".shot_prompt", b)
                for w in pc.warnings:
                    add("WARN", "PROMPT_WARN", f + ".shot_prompt", w)

    if n_pending:
        add("INFO", "MEDIA_PENDING", "media", f"{n_pending} media entr{'y' if n_pending == 1 else 'ies'} PENDING: no image exists yet")

    # --- review block
    rev = post.get("review")
    pending_media = isinstance(media, list) and any(isinstance(m, dict) and m.get("path") == "PENDING" for m in media)
    if isinstance(rev, dict):
        for k in ("wife_language", "operator_facts"):
            if rev.get(k) not in REVIEW_STATES:
                add("ERROR", "BAD_REVIEW", f"review.{k}", f"must be one of {', '.join(REVIEW_STATES)}")
        if not isinstance(rev.get("approved"), bool):
            add("ERROR", "BAD_REVIEW", "review.approved", "must be true or false")
        if not isinstance(rev.get("notes"), str):
            add("ERROR", "BAD_REVIEW", "review.notes", "must be a string")
        if rev.get("approved") is True:
            if rev.get("wife_language") != "approved" or rev.get("operator_facts") != "approved":
                add("ERROR", "APPROVAL_INCONSISTENT", "review.approved",
                    "approved is true but wife_language and operator_facts are not both 'approved'")
            if pending_media:
                add("ERROR", "APPROVAL_INCONSISTENT", "review.approved", "approved is true but media is still PENDING")
            if any(x.code == "PLACEHOLDER" for x in F):
                add("ERROR", "APPROVAL_INCONSISTENT", "review.approved", "approved is true but a placeholder is still unfilled")
            blocking = [x for x in F if x.level in ("ERROR", "FLAG") and x.code != "APPROVAL_INCONSISTENT"]
            if blocking:
                add("ERROR", "APPROVED_WITH_OPEN_ISSUES", "review.approved",
                    f"approved is true but {len(blocking)} ERROR/FLAG finding(s) remain; a human must re-review")
            add("INFO", "HUMAN_FIELD", "review.approved",
                "approved=true is a human field; this script cannot verify who set it or when (the first 30 days need a human on every post)")
    return F


def draft_status(post, findings: list[Finding]) -> str:
    errors = [f for f in findings if f.level == "ERROR"]
    if errors:
        if all(f.code == "EMPTY" for f in errors):
            return "incomplete"
        return "invalid"
    if any(f.level == "FLAG" for f in findings):
        return "flagged"
    rev = post.get("review") if isinstance(post, dict) else None
    if not isinstance(rev, dict):
        return "invalid"
    if rev.get("approved") is True:
        return "approved"
    w, o = rev.get("wife_language"), rev.get("operator_facts")
    if "changes" in (w, o):
        return "changes-requested"
    if w == "pending" and o == "pending":
        return "awaiting-both"
    if w == "pending":
        return "awaiting-wife"
    if o == "pending":
        return "awaiting-operator"
    return "ready-for-final-approval"


def validate_all(root: Path, targets=None, *, today: dt.date | None = None):
    """Return a list of dicts: {path, folder, post, findings, status}."""
    prov = load_provenance_paths(root)
    results = []
    ids = {}
    for path in find_posts(root, targets):
        folder = path.parent
        post, err = load_post(path)
        if err:
            fnd = [Finding("ERROR", "UNREADABLE", "post.json", err)]
            results.append({"path": path, "folder": folder, "post": None, "findings": fnd, "status": "invalid"})
            continue
        fnd = validate_post(post, folder, root, today=today, prov_paths=prov)
        results.append({"path": path, "folder": folder, "post": post, "findings": fnd, "status": draft_status(post, fnd)})
        if isinstance(post, dict) and isinstance(post.get("id"), str):
            ids.setdefault(post["id"], []).append(path)
    for pid, paths in ids.items():
        if len(paths) > 1:
            for r in results:
                if r["path"] in paths:
                    r["findings"].append(Finding("ERROR", "DUPLICATE_ID", "id", f"id {pid} is used by {len(paths)} drafts"))
                    r["status"] = "invalid"
    return results


def weekly_load(results) -> dict:
    """Drafts per ISO week (a rough check against the planning ceiling of portfolio.md 5.1)."""
    weeks: dict[str, int] = {}
    for r in results:
        p = r["post"]
        if isinstance(p, dict) and isinstance(p.get("scheduled_date"), str):
            try:
                d = dt.date.fromisoformat(p["scheduled_date"])
            except ValueError:
                continue
            y, w, _ = d.isocalendar()
            key = f"{y}-W{w:02d}"
            weeks[key] = weeks.get(key, 0) + 1
    return weeks


def approval_report(post, findings: list[Finding]) -> tuple[list[str], bool]:
    """Lines describing what stands between this draft and approval, and whether review.approved is
    already true and consistent. Read-only."""
    lines = []
    rev = post.get("review") if isinstance(post, dict) else None
    if not isinstance(rev, dict):
        rev = {}
    blockers = [f for f in findings if f.level in ("ERROR", "FLAG")]
    lines.append(f"[{'x' if not blockers else ' '}] validation clean ({len(blockers)} ERROR/FLAG open)")
    lines.append(f"[{'x' if rev.get('wife_language') == 'approved' else ' '}] wife_language: {rev.get('wife_language')!r} (set by the wife)")
    lines.append(f"[{'x' if rev.get('operator_facts') == 'approved' else ' '}] operator_facts: {rev.get('operator_facts')!r} (set by the operator)")
    raw_media = post.get("media") if isinstance(post, dict) else None
    pend = [m for m in (raw_media if isinstance(raw_media, list) else []) if isinstance(m, dict) and m.get("path") == "PENDING"]
    lines.append(f"[{'x' if not pend else ' '}] media generated, logged and badged ({len(pend)} still PENDING)")
    lines.append("[ ] by hand, outside this script: badge present on every image/frame; platform AI label ON; "
                 "paid-partnership tool ON if sponsored; screenshot of the four disclosure places kept")
    ok = rev.get("approved") is True and not blockers
    lines.append(f"[{'x' if rev.get('approved') is True else ' '}] review.approved: {rev.get('approved')!r} (a human edits post.json to set it)")
    return lines, ok


# --------------------------------------------------------------------------- command line

def _fmt_findings(findings, indent="  "):
    order = {l: i for i, l in enumerate(gr.LEVELS)}
    return [indent + f.render() for f in sorted(findings, key=lambda f: order.get(f.level, 9))]


def _counts(findings):
    c = {l: 0 for l in gr.LEVELS}
    for f in findings:
        c[f.level] = c.get(f.level, 0) + 1
    return c


def cmd_new_draft(args, root, out):
    try:
        folder = new_draft(root, args.persona, args.platform, args.format, args.date, args.pillar or "", args.number)
    except QueueError as e:
        out(f"error: {e}")
        return 2
    rel = folder.relative_to(root) if folder.is_relative_to(root) else folder
    out(f"Created {rel}/post.json and {rel}/media/.gitkeep")
    out("The scaffold starts with the AI disclosure line, label AI 生成｜虛擬角色, review pending/pending/false.")
    out("Fill hook_zh, the caption body, the gloss, hashtags, sources and the media shot_prompt; validate will list what is missing.")
    return 0


def cmd_validate(args, root, out):
    results = validate_all(root, args.paths or None, today=dt.date.today() if args.today else None)
    if not results:
        out("No drafts found." if not args.paths else "No post.json found at the given paths.")
        return 0 if not args.paths else 2
    if args.json:
        out(json.dumps([{"id": (r["post"] or {}).get("id") if isinstance(r["post"], dict) else None,
                         "path": str(r["path"]), "status": r["status"],
                         "findings": [f.__dict__ for f in r["findings"]]} for r in results],
                       ensure_ascii=False, indent=2))
    bad = 0
    for r in results:
        c = _counts(r["findings"])
        failing = c["ERROR"] + c["FLAG"] + (c["WARN"] if args.strict else 0)
        bad += 1 if failing else 0
        if args.json:
            continue
        pid = r["post"].get("id") if isinstance(r["post"], dict) else r["path"]
        out(f"== {pid}  [{r['status']}]  ERROR {c['ERROR']}  FLAG {c['FLAG']}  WARN {c['WARN']}  INFO {c['INFO']}")
        for line in _fmt_findings(r["findings"]):
            out(line)
    if not args.json:
        weeks = weekly_load(results)
        for wk, n in sorted(weeks.items()):
            if n > WEEKLY_APPROVAL_CEILING:
                out(f"WARN week {wk}: {n} drafts exceeds the planning ceiling of {WEEKLY_APPROVAL_CEILING} approvals a week (portfolio.md 5.1, assumption)")
        out(f"{len(results)} draft(s) checked, {bad} with blocking findings.")
        out("Banned-term hits are FLAGGED, never fixed: a human edits the wording. A clean run is not approval.")
    return 1 if bad else 0


def cmd_list(args, root, out):
    results = validate_all(root, None)
    rows = []
    for r in results:
        p = r["post"] if isinstance(r["post"], dict) else {}
        rev = p.get("review") if isinstance(p.get("review"), dict) else {}
        raw_media = p.get("media")
        media = [m for m in (raw_media if isinstance(raw_media, list) else []) if isinstance(m, dict)]
        npend = sum(1 for m in media if m.get("path") == "PENDING")
        c = _counts(r["findings"])
        # str() everything: a malformed post.json (numbers, nulls) must not crash the table
        rows.append({
            "id": str(p.get("id") or r["folder"].name), "persona": str(p.get("persona", "?")),
            "platform": str(p.get("platform", "?")),
            "date": str(p.get("scheduled_date", "?")), "status": r["status"],
            "wife": str(rev.get("wife_language", "?")), "operator": str(rev.get("operator_facts", "?")),
            "approved": "yes" if rev.get("approved") is True else "no",
            "media": f"{len(media) - npend}/{len(media)}", "E/F/W": f"{c['ERROR']}/{c['FLAG']}/{c['WARN']}",
        })
    if args.persona:
        rows = [x for x in rows if x["persona"] == args.persona]
    if args.status:
        rows = [x for x in rows if x["status"] == args.status]
    if not rows:
        out("No drafts match." if results else "The review queue is empty.")
        return 0
    cols = ["id", "persona", "platform", "date", "status", "wife", "operator", "approved", "media", "E/F/W"]
    widths = {c: max(len(c), *(len(str(x[c])) for x in rows)) for c in cols}
    out("  ".join(c.ljust(widths[c]) for c in cols))
    out("  ".join("-" * widths[c] for c in cols))
    for x in sorted(rows, key=lambda x: (x["date"], x["id"])):
        out("  ".join(str(x[c]).ljust(widths[c]) for c in cols))
    out(f"{len(rows)} draft(s). media = generated/total. E/F/W = errors/flags/warnings.")
    return 0


def cmd_approve(args, root, out):
    paths = find_posts(root, [args.draft])
    if not paths:
        out(f"No post.json found at {args.draft}")
        return 2
    path = paths[0]
    post, err = load_post(path)
    if err:
        out(f"cannot read {path}: {err}")
        return 2
    findings = validate_post(post, path.parent, root, prov_paths=load_provenance_paths(root))
    out("APPROVAL IS A HUMAN ACTION. This command only reports; it never changes post.json.")
    out("Only the wife sets review.wife_language, only the operator sets review.operator_facts, and only a human")
    out("sets review.approved to true, by editing post.json by hand, for every post in at least the first 30 days.")
    out("")
    lines, ok = approval_report(post, findings)
    for ln in lines:
        out("  " + ln)
    out("")
    out("READY: review.approved is true and nothing blocks it." if ok else "NOT APPROVED (or not consistent). Nothing was changed.")
    return 0 if ok else 1


def build_parser():
    import argparse
    ap = argparse.ArgumentParser(prog="queue.py", description="Review queue: scaffold, validate, list, report. Never approves.")
    ap.add_argument("--root", type=Path, default=ROOT, help="project folder (default: two levels above this script)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    nd = sub.add_parser("new-draft", help="scaffold a draft folder")
    nd.add_argument("--persona", required=True, choices=sorted(PERSONAS))
    nd.add_argument("--platform", required=True, choices=PLATFORMS)
    nd.add_argument("--format", required=True, choices=FORMATS)
    nd.add_argument("--date", required=True, help="scheduled date YYYY-MM-DD")
    nd.add_argument("--pillar", default="")
    nd.add_argument("--number", type=int, help="NN; default: next free number for that persona and date")

    va = sub.add_parser("validate", help="check drafts against the format and the ground rules")
    va.add_argument("paths", nargs="*", help="draft folders or post.json files (default: all)")
    va.add_argument("--strict", action="store_true", help="WARN also fails")
    va.add_argument("--json", action="store_true")
    va.add_argument("--today", action="store_true", help="warn about dates in the past")

    ls = sub.add_parser("list", help="table of drafts and their status")
    ls.add_argument("--persona")
    ls.add_argument("--status")

    ap_ = sub.add_parser("approve", help="REPORT whether a draft is ready; never approves, never edits")
    ap_.add_argument("draft", help="draft folder or post.json")
    return ap


def main(argv=None, *, out=print) -> int:
    args = build_parser().parse_args(argv)
    root = args.root.resolve()
    return {"new-draft": cmd_new_draft, "validate": cmd_validate, "list": cmd_list, "approve": cmd_approve}[args.cmd](args, root, out)


if __name__ == "__main__":
    sys.exit(main())
