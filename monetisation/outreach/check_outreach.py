#!/usr/bin/env python3
"""check_outreach.py - consistency checks for the outreach folder. Standard library only; no network; edits nothing.

    python3 -B monetisation/outreach/check_outreach.py                  # check lists, drafts, playbook, links
    python3 -B monetisation/outreach/check_outreach.py --scan           # also print every zh-TW wording finding (informational)
    python3 -B monetisation/outreach/check_outreach.py --filled FILE    # a built message is ready to send
    python3 -B monetisation/outreach/check_outreach.py --tracking FILE  # a filled tracking sheet: values, cadence, do-not-contact, funnel

Default mode checks
  1. the three target-list CSVs: header, ids, allowed values, the standard contact-route wording, the "verify" wording,
     no e-mail address, phone number, web address, business ID or NT$ amount anywhere, HOLD and SKIP rows say do not contact,
     rows sorted by priority, no duplicate names, cross-list consistency of type and of the `also_in` column,
     Traditional-only and Taiwan vocabulary in the Chinese fields
  2. that the generated pages (three list pages, the do-not-contact seed, the README counts) are up to date
  3. email-drafts.md: the block table, T1 to T6 present, {{B-...}} markers resolve, every template built and scanned with the
     project's zh-TW scanner (pipeline/scripts/ground_rules.py), honesty and disclosure lines present, no price, no address
  4. outreach-playbook.md: sections 0 to 11, gates G1 to G9, questions O1 to O7, the tracking columns equal the CSV header,
     the status and reply-type lists equal this script's lists
  5. relative links and backticked repo paths in every markdown file resolve
Exit code 1 if any ERROR. WARN and INFO are for a human to read. A clean run says nothing about whether a row is TRUE: every
row is unverified until a person checks it.
"""
from __future__ import annotations

import csv
import datetime as dt
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))
sys.path.append(str(ROOT / "pipeline" / "scripts"))
try:
    import ground_rules  # type: ignore  # noqa: E402
except Exception:  # pragma: no cover - the scanner is optional
    ground_rules = None
import render_lists  # noqa: E402

LISTS = {"fashion": "F", "ai-tools": "A", "home": "H"}
COLS = ["id", "name_zh", "name_en", "type", "subtype", "why_it_fits", "lead_with", "contact_route", "compliance_flags",
        "priority", "existence_confidence", "basis", "also_in", "group_note", "template", "warm_route_note", "verify",
        "verified_on", "status"]
STD_ROUTE = "official website contact form or listed business-inquiry page (to look up)"
VERIFY = "verify existence and current contact route"
TYPES = {"brand", "agency", "platform"}
PRIORITIES = ["P1", "P2", "P3", "HOLD", "SKIP"]
CONF = {"high", "medium-high", "medium"}
TEMPLATES = {"T1", "T2"}

TRACK_COLS = ["contact_id", "list_id", "entity_name", "niche", "entity_type", "priority", "route", "group_note", "verified_on",
              "contact_source", "channel", "recipient_role", "template", "sender", "wife_checked_zh", "compliance_checked",
              "first_sent_date", "follow_up_due", "follow_up_sent_date", "status", "reply_date", "reply_type", "do_not_contact",
              "dnc_reason", "dnc_date", "sample_offered", "sample_scope", "sample_delivered_date", "written_quote_received",
              "quote_date", "lead_signal_kind", "lead_signal_logged_on", "persona_tag", "next_action", "next_action_due", "notes"]
STATUS = ["not_started", "verified", "ready_to_send", "sent", "follow_up_sent", "replied", "in_conversation", "sample_scoped",
          "sample_delivered", "quote_pending", "closed_no_reply", "closed_declined_by_them", "closed_declined_by_us",
          "do_not_contact", "on_hold"]
CLOSED = {"closed_no_reply", "closed_declined_by_them", "closed_declined_by_us", "do_not_contact"}
SENT_OR_LATER = {"sent", "follow_up_sent", "replied", "in_conversation", "sample_scoped", "sample_delivered", "quote_pending"}
REPLY_TYPES = ["interested", "more_info", "not_now", "no_thanks", "opt_out", "noncompliant_brief", "bounce", "auto_reply",
               "rate_sheet", "other", "none"]
ENUMS = {
    "niche": {"fashion", "ai-tools", "home"}, "entity_type": TYPES, "priority": set(PRIORITIES),
    "route": {"warm", "cold", "introduction"}, "channel": {"web_form", "business_email", "in_person", "phone"},
    "template": {"T1", "T2", "T3", "T4", "T5", "T6", "custom"}, "sender": {"operator", "wife"},
    "wife_checked_zh": {"Y", "N", "n/a"}, "compliance_checked": {"Y", "N"}, "status": set(STATUS),
    "reply_type": set(REPLY_TYPES), "do_not_contact": {"Y"}, "sample_offered": {"Y", "N"}, "written_quote_received": {"Y", "N"},
    "lead_signal_kind": {"outreach_sent", "written_enquiry", "accepted_free_sample", "written_quote", "agency_budget_reply"},
    "persona_tag": {"sehuan", "buzhou", "fangcun"},
}
DATE_COLS = ["verified_on", "first_sent_date", "follow_up_due", "follow_up_sent_date", "reply_date", "dnc_date",
             "sample_delivered_date", "quote_date", "lead_signal_logged_on", "next_action_due"]
PERSONA_FOR_NICHE = {"fashion": "sehuan", "ai-tools": "buzhou", "home": "fangcun"}

CJK = re.compile(r"[一-鿿]")
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+|(?<![\w])@(?![\w])")
URL = re.compile(r"https?://|www\.|\b[a-z0-9-]+\.(?:com|tw|net|org|io|co)\b", re.I)
PHONE = re.compile(r"(?<!\d)(?:\+?886[-\s]?|0)\d{1,2}[-\s]?\d{3,4}[-\s]?\d{3,4}(?!\d)|(?<!\d)09\d{2}[-\s]?\d{3}[-\s]?\d{3}(?!\d)")
EIGHT = re.compile(r"(?<!\d)\d{8}(?!\d)")
PRICE = re.compile(r"NT\$|新台幣|新臺幣|\d[\d,]*\s*元|\d\s*萬\s*元")
SOFT_NUM = re.compile(r"\b\d+(?:\.\d+)?\s?(?:%|million|followers|subscribers)\b", re.I)


class Report:
    def __init__(self):
        self.errors, self.warns, self.infos = [], [], []

    def err(self, m): self.errors.append(m)
    def warn(self, m): self.warns.append(m)
    def info(self, m): self.infos.append(m)


def read_csv(path: Path):
    with path.open(encoding="utf-8", newline="") as fh:
        rd = csv.DictReader(fh)
        return rd.fieldnames or [], list(rd)


def no_contact_details(text: str, where: str, rep: Report, *, allow_address: bool = False):
    if not allow_address and EMAIL.search(text):
        rep.err(f"{where}: looks like an e-mail address: {EMAIL.search(text).group(0)!r}")
    if not allow_address and URL.search(text):
        rep.err(f"{where}: looks like a web address: {URL.search(text).group(0)!r}")
    if PHONE.search(text) and not allow_address:
        rep.err(f"{where}: looks like a phone number: {PHONE.search(text).group(0)!r}")
    if EIGHT.search(text) and not allow_address:
        rep.err(f"{where}: an 8-digit number (business ID?): {EIGHT.search(text).group(0)!r}")


PLACEHOLDER = re.compile(r"\[[^\[\]]*TO FILL[^\[\]]*\]")
# A sentence that starts a list of things the studio does NOT do. The scanner cannot see a negator across the Chinese list
# comma, so such a sentence is reported as INFO for a human, never silently dropped.
DENIAL_MARKERS = ("我們不做", "我們不製作", "角色不做", "也不製作這類內容", "不在我們能承接的範圍", "不接受移除或縮小")


def zh_findings(text: str, field: str):
    if ground_rules is None or not text:
        return []
    out = []
    for sentence in re.split(r"(?<=[。\n])", PLACEHOLDER.sub("", text)):
        if not sentence.strip():
            continue
        denial = any(m in sentence for m in DENIAL_MARKERS)
        for f in ground_rules.scan_text(sentence, field):
            if denial and f.level in ("FLAG", "ERROR") and f.code in (
                    "LIVED_EXPERIENCE", "HEALTH_CLAIM", "FINANCE_CLAIM", "GAMBLING", "POLITICS"):
                out.append(ground_rules.Finding("INFO", f.code + "_DENIED", f.field,
                                                "inside a sentence that says the studio does not do this (confirm): " + f.message))
            else:
                out.append(f)
    return out


# ----------------------------------------------------------------------------- 1. lists
def check_lists(rep: Report, scan: list | None = None, directory: Path = HERE):
    all_rows = {}
    for key, code in LISTS.items():
        path = directory / f"target-list-{key}.csv"
        name = path.name
        if not path.exists():
            rep.err(f"{name}: missing")
            continue
        header, rows = read_csv(path)
        if header != COLS:
            rep.err(f"{name}: header is {header}, expected {COLS}")
            continue
        all_rows[key] = rows
        names, ranks, last_rank = set(), {p: i for i, p in enumerate(PRIORITIES)}, -1
        for n, r in enumerate(rows, 2):
            where = f"{name}:{n} ({r['id']})"
            if not re.fullmatch(code + r"\d{2}", r["id"]) or r["id"] != f"{code}{n - 1:02d}":
                rep.err(f"{where}: id should be {code}{n - 1:02d}")
            if r["type"] not in TYPES:
                rep.err(f"{where}: type {r['type']!r} not in {sorted(TYPES)}")
            if r["priority"] not in ranks:
                rep.err(f"{where}: priority {r['priority']!r}")
            else:
                if ranks[r["priority"]] < last_rank:
                    rep.err(f"{where}: rows must be sorted by priority (P1, P2, P3, HOLD, SKIP)")
                last_rank = max(last_rank, ranks[r["priority"]])
            if r["existence_confidence"] not in CONF:
                rep.err(f"{where}: existence_confidence {r['existence_confidence']!r}")
            if r["template"] not in TEMPLATES:
                rep.err(f"{where}: template {r['template']!r}")
            if not re.fullmatch(r"([FAH](;[FAH])*)?", r["also_in"]):
                rep.err(f"{where}: also_in {r['also_in']!r}")
            if not r["contact_route"].startswith(STD_ROUTE) or "to look up" not in r["contact_route"]:
                rep.err(f"{where}: contact_route must start with the standard wording")
            if r["verify"] != VERIFY:
                rep.err(f"{where}: verify must read {VERIFY!r}")
            for c in ("name_zh", "name_en", "subtype", "why_it_fits", "lead_with", "compliance_flags", "basis"):
                if not r[c].strip():
                    rep.err(f"{where}: {c} is empty")
            if not CJK.search(r["name_zh"]) and not re.search(r"[A-Za-z]", r["name_zh"]):
                rep.err(f"{where}: name_zh has neither Chinese nor Latin letters")
            if r["status"].strip():
                rep.info(f"{where}: status is filled ({r['status']!r}); fine in a working copy, normally empty in the repo")
            if r["name_zh"] in names:
                rep.err(f"{where}: duplicate name_zh {r['name_zh']!r} in this list")
            names.add(r["name_zh"])
            if r["priority"] in ("HOLD", "SKIP") and not r["lead_with"].startswith("Do not contact"):
                rep.err(f"{where}: a {r['priority']} row must say 'Do not contact' in lead_with")
            if r["priority"] in ("P1", "P2", "P3") and r["lead_with"].startswith("Do not contact"):
                rep.err(f"{where}: an actionable row says 'Do not contact'")
            for c, v in r.items():
                if v:
                    no_contact_details(v, f"{where} {c}", rep)
                    if PRICE.search(v):
                        rep.err(f"{where} {c}: a price figure ({PRICE.search(v).group(0)!r}); no invented prices anywhere")
                    if "|" in v:
                        rep.err(f"{where} {c}: contains a pipe, which breaks the generated table")
            if SOFT_NUM.search(r["why_it_fits"]):
                rep.warn(f"{where}: a figure in why_it_fits ({SOFT_NUM.search(r['why_it_fits']).group(0)!r}); confirm it is sourced")
            for c in ("name_zh", "group_note"):
                for f in zh_findings(r[c], f"{where} {c}"):
                    if f.level in ("ERROR", "FLAG"):
                        rep.err(f.render())
                    elif scan is not None:
                        scan.append(f.render())
    # cross-list consistency
    where_is = defaultdict(list)
    for key, rows in all_rows.items():
        for r in rows:
            where_is[r["name_zh"]].append((LISTS[key], r))
    for name, occ in where_is.items():
        types = {r["type"] for _, r in occ}
        if len(types) > 1:
            rep.err(f"{name!r}: type differs between lists: {sorted(types)}")
        codes = {c for c, _ in occ}
        for c, r in occ:
            declared = set(filter(None, r["also_in"].split(";")))
            if declared != codes - {c}:
                rep.err(f"{name!r} in list {c}: also_in is {sorted(declared)} but it appears in {sorted(codes - {c})}")
    for key, rows in all_rows.items():
        c = Counter(r["priority"] for r in rows)
        rep.info(f"target-list-{key}.csv: {len(rows)} rows (" + ", ".join(f"{p} {c[p]}" for p in PRIORITIES if c[p]) + ")")
    uniq = len(where_is)
    rep.info(f"{sum(len(v) for v in all_rows.values())} rows, {uniq} distinct entities")
    return all_rows


def check_generated(rep: Report):
    try:
        for key, meta in render_lists.LISTS.items():
            path = HERE / f"{meta['file']}.md"
            if not path.exists() or path.read_text(encoding="utf-8") != render_lists.render_list(key):
                rep.err(f"{path.name}: out of date; run render_lists.py")
        dnc = HERE / render_lists.DNC_FILE
        if not dnc.exists() or dnc.read_text(encoding="utf-8") != render_lists.dnc_text():
            rep.err(f"{render_lists.DNC_FILE}: out of date; run render_lists.py")
        readme = HERE / "README.md"
        if readme.exists():
            old = readme.read_text(encoding="utf-8")
            if render_lists.replace_block(old, "counts", render_lists.counts_block()) != old:
                rep.err("README.md: counts block out of date; run render_lists.py")
        else:
            rep.err("README.md missing")
    except SystemExit as e:  # replace_block exits when markers are missing
        rep.err(str(e))


# ----------------------------------------------------------------------------- 3. drafts
def split_cells(line: str):
    s = line.strip()
    if not (s.startswith("|") and s.endswith("|")):
        return None
    return [c.strip() for c in s.strip("|").split("|")]


def parse_blocks(lines):
    blocks = {}
    for ln in lines:
        m = re.match(r"^\|\s*\*\*(B-[A-Z-]+)\*\*", ln)
        if m:
            cells = split_cells(ln)
            if cells and len(cells) >= 3:
                blocks[m.group(1)] = (cells[1], cells[2])
    return blocks


def expand(text: str, blocks, which=0):
    def sub(m):
        return blocks.get(m.group(1), ("", ""))[which].replace("<br>", "\n")
    return re.sub(r"\{\{(B-[A-Z-]+)\}\}", sub, text.replace("<br>", "\n"))


def template_sections(lines):
    """Return {'T1': [lines...], ...} for '## n. T<k>.' headings."""
    secs, cur = {}, None
    for ln in lines:
        m = re.match(r"^## \d+\. (T\d)\.", ln)
        if m:
            cur = m.group(1)
            secs[cur] = []
        elif ln.startswith("## "):
            cur = None
        elif cur:
            secs[cur].append(ln)
    return secs


def check_drafts(rep: Report, scan: list | None = None, path: Path | None = None):
    path = path or HERE / "email-drafts.md"
    if not path.exists():
        rep.err("email-drafts.md missing")
        return
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    blocks = parse_blocks(lines)
    for b in ["B-INTRO", "B-STATUS", "B-RULES", "B-SAMPLE-OPT", "B-RATESHEET-OPT", "B-OPTOUT", "B-CLOSE", "B-SIG"]:
        if b not in blocks:
            rep.err(f"email-drafts.md: block {b} missing from the blocks table")
    for m in sorted(set(re.findall(r"\{\{(B-[A-Z-]+)\}\}", text))):
        if m not in blocks:
            rep.err(f"email-drafts.md: marker {{{{{m}}}}} has no block")
    secs = template_sections(lines)
    for t in ["T1", "T2", "T3", "T4", "T5", "T6"]:
        if t not in secs:
            rep.err(f"email-drafts.md: template {t} missing")
    # no contact details or prices anywhere in the drafts
    for n, ln in enumerate(lines, 1):
        no_contact_details(ln, f"email-drafts.md:{n}", rep)
        if PRICE.search(ln):
            rep.err(f"email-drafts.md:{n}: a price figure {PRICE.search(ln).group(0)!r}")
    # Simplified characters anywhere outside section 9 (which quotes banned words)
    in9 = False
    for n, ln in enumerate(lines, 1):
        if ln.startswith("## 9."):
            in9 = True
        elif ln.startswith("## ") and not ln.startswith("## 9."):
            in9 = False
        if ground_rules and not in9:
            simp = sorted({c for c in ln if c in ground_rules.SIMPLIFIED_SET})
            if simp:
                rep.err(f"email-drafts.md:{n}: Simplified character(s) {' '.join(simp)}")
    # built texts
    built = {}
    for t, body in secs.items():
        zh_parts = []
        for ln in body:
            if ln.startswith("**Subject (zh-TW):**"):
                zh_parts.append(ln.split(":**", 1)[1].strip())
                continue
            cells = split_cells(ln)
            if cells and len(cells) == 2 and not set(cells[0]) <= set("-: "):
                zh_parts.append(cells[0])
        built[t] = expand("\n".join(zh_parts), blocks)
    must = {
        "T1": ["TO FILL", "[STUDIO LEGAL NAME / REGISTRATION: TO FILL]", "不需要", "AI 虛擬角色", "沒有可展示的合作案例", "【業配】", "WHY THIS RECIPIENT"],
        "T2": ["[STUDIO LEGAL NAME / REGISTRATION: TO FILL]", "不需要", "AI 虛擬角色", "我們不是代理商", "沒有可展示的合作案例", "WHY THIS RECIPIENT"],
        "T3": ["[STUDIO LEGAL NAME / REGISTRATION: TO FILL]", "不需要", "AI 虛擬角色"],
        "T4": ["[STUDIO LEGAL NAME / REGISTRATION: TO FILL]", "AI 生成", "沒有已完成的合作案例", "不承諾", "書面", "不需要"],
        "T5": ["[STUDIO LEGAL NAME / REGISTRATION: TO FILL]", "移除", "不會再"],
        "T6": ["AI 生成", "沒有實際使用過", "TO FILL"],
    }
    for t, needles in must.items():
        txt = built.get(t, "")
        for needle in needles:
            if needle not in txt:
                rep.err(f"email-drafts.md {t}: the built text lacks {needle!r}")
    for t in ("T1", "T2"):
        for bad in ("今天穿", "我們的客戶", "合作案例包括", "已合作", "粉絲數", "追蹤人數超過"):
            if bad in built.get(t, ""):
                rep.err(f"email-drafts.md {t}: wording that implies a client or audience: {bad!r}")
    # zh scan of the built text and of every block
    seen = set()
    texts = {f"{t} (built)": v for t, v in built.items()}
    texts.update({f"block {b}": z for b, (z, _) in blocks.items()})
    for field, txt in texts.items():
        for part in re.split(r"\n", txt):
            for f in zh_findings(part, field):
                key = (f.level, f.code, f.message)
                if key in seen:
                    continue
                seen.add(key)
                if f.level in ("ERROR", "FLAG"):
                    rep.err("email-drafts.md " + f.render())
                elif scan is not None:
                    scan.append("email-drafts.md " + f.render())
    for t, v in built.items():
        rep.info(f"email-drafts.md {t}: built text {len(v)} characters; {v.count('TO FILL')} placeholder(s)")
    # the gloss column must have Latin letters
    for t, body in secs.items():
        for ln in body:
            cells = split_cells(ln)
            if cells and len(cells) == 2 and CJK.search(cells[0]) and not re.search(r"[A-Za-z]", cells[1]):
                rep.err(f"email-drafts.md {t}: a zh-TW cell has no English gloss: {cells[0][:40]!r}")


def check_filled(path: Path):
    rep = Report()
    text = path.read_text(encoding="utf-8")
    for needle in ("TO FILL", "{{", "[OPTIONAL", "NICHE BLOCK", "WHY THIS RECIPIENT", "待填", "<B-"):
        if needle in text:
            rep.err(f"{path.name}: still contains {needle!r}")
    if PRICE.search(text):
        rep.err(f"{path.name}: contains a price figure {PRICE.search(text).group(0)!r}")
    for f in zh_findings(text, path.name):
        if f.level in ("ERROR", "FLAG"):
            rep.err(f.render())
        elif f.level == "WARN":
            rep.warn(f.render())
    if ground_rules:
        simp = sorted({c for c in text if c in ground_rules.SIMPLIFIED_SET})
        if simp:
            rep.err(f"{path.name}: Simplified character(s) {' '.join(simp)}")
    if "不需要" not in text and "T5" not in text and "AI" in text:
        rep.warn(f"{path.name}: no opt-out sentence found (first-contact messages need one)")
    if "AI" not in text:
        rep.err(f"{path.name}: does not say the characters are AI")
    return rep


# ----------------------------------------------------------------------------- 4. playbook
def check_playbook(rep: Report):
    path = HERE / "outreach-playbook.md"
    if not path.exists():
        rep.err("outreach-playbook.md missing")
        return
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    nums = [int(m.group(1)) for ln in lines if (m := re.match(r"^## (\d+)\.", ln))]
    if nums != list(range(0, 12)):
        rep.err(f"outreach-playbook.md: sections are {nums}, expected 0 to 11")
    for g in range(1, 10):
        if not re.search(rf"^\| G{g} \|", text, re.M):
            rep.err(f"outreach-playbook.md: gate G{g} missing")
    for o in range(1, 8):
        if not re.search(rf"^\| O{o} \|", text, re.M):
            rep.err(f"outreach-playbook.md: question O{o} missing")
    for needle in ("unverified, lawyer question", "outreach is sent by the two of you", "one open thread per entity"):
        if needle.lower() not in text.lower():
            rep.err(f"outreach-playbook.md: lacks {needle!r}")
    # section 6 columns equal the tracking header
    sec = []
    on = False
    for ln in lines:
        if ln.startswith("## 6."):
            on = True
        elif ln.startswith("## ") and on:
            break
        elif on:
            sec.append(ln)
    cols = []
    for ln in sec:
        cells = split_cells(ln)
        if cells and cells[0].startswith("`"):
            cols += re.findall(r"`([a-z_]+)`", cells[0])
    tmpl = HERE / "tracking-template.csv"
    header = read_csv(tmpl)[0] if tmpl.exists() else []
    if header != TRACK_COLS:
        rep.err(f"tracking-template.csv: header differs from the checker's list ({header})")
    if cols != header:
        missing = [c for c in header if c not in cols]
        extra = [c for c in cols if c not in header]
        rep.err(f"outreach-playbook.md section 6: columns differ from tracking-template.csv; missing {missing}, extra {extra}")
    for label, values in (("Status values", STATUS), ("Reply types", REPLY_TYPES)):
        m = re.search(rf"\*\*{label}:\*\*([^\n]+)", text)
        got = re.findall(r"`([a-z_]+)`", m.group(1)) if m else []
        if got != values:
            rep.err(f"outreach-playbook.md: {label} differ from the checker's list: {got}")


# ----------------------------------------------------------------------------- 5. links
def check_links(rep: Report):
    skip = re.compile(r"[<>*]|YYYY|filled|TO FILL|\.\.\.|\{")
    for md in sorted(HERE.glob("*.md")):
        text = md.read_text(encoding="utf-8")
        base = md.parent
        for m in re.finditer(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", text):
            tgt = m.group(1)
            if tgt.startswith(("http", "mailto:")):
                rep.err(f"{md.name}: external link {tgt!r}; none is allowed here (no unverified web address)")
            elif not (base / tgt).exists():
                rep.err(f"{md.name}: broken link {tgt!r}")
        for m in re.finditer(r"`([A-Za-z0-9_./~-]+\.(?:md|csv|py|json|html)|(?:[a-z_-]+/)+[A-Za-z0-9_./-]*)`", text):
            tok = m.group(1)
            if skip.search(tok):
                continue
            if not ((ROOT / tok).exists() or (base / tok).exists() or (base.parent / tok).exists()):
                rep.err(f"{md.name}: backticked path {tok!r} does not resolve")


# ----------------------------------------------------------------------------- tracking
def pdate(v):
    try:
        return dt.date.fromisoformat(v)
    except ValueError:
        return None


def check_tracking(path: Path):
    rep = Report()
    header, rows = read_csv(path)
    if header != TRACK_COLS:
        rep.err(f"{path.name}: header differs from tracking-template.csv")
        return rep, {}
    open_by_entity, by_entity = defaultdict(list), defaultdict(list)
    for n, r in enumerate(rows, 2):
        where = f"{path.name}:{n} ({r['contact_id'] or r['entity_name']})"
        if not r["entity_name"].strip():
            rep.err(f"{where}: entity_name is empty")
        for col, allowed in ENUMS.items():
            v = r[col].strip()
            if v and v not in allowed:
                rep.err(f"{where}: {col} = {v!r}, allowed {sorted(allowed)}")
        for col in DATE_COLS:
            if r[col].strip() and pdate(r[col].strip()) is None:
                rep.err(f"{where}: {col} = {r[col]!r} is not YYYY-MM-DD")
        for c, v in r.items():
            if c != "notes" and v:
                no_contact_details(v, f"{where} {c}", rep)
        if r["notes"]:
            no_contact_details(r["notes"], f"{where} notes", rep)
        first, due, fu = pdate(r["first_sent_date"]), pdate(r["follow_up_due"]), pdate(r["follow_up_sent_date"])
        st = r["status"].strip()
        if st in SENT_OR_LATER and not first and r["route"] != "warm":
            rep.err(f"{where}: status {st} but first_sent_date is empty")
        if first and due and (due - first).days != 7:
            rep.err(f"{where}: follow_up_due should be 7 days after first_sent_date")
        if first and fu and (fu - first).days < 7:
            rep.warn(f"{where}: follow-up sent {(fu - first).days} days after the first message; the cadence is day 7")
        if r["priority"] in ("SKIP", "HOLD") and (first or st in SENT_OR_LATER):
            rep.err(f"{where}: a {r['priority']} entity must never be contacted")
        if r["do_not_contact"].strip() == "Y":
            if st not in CLOSED:
                rep.err(f"{where}: do_not_contact = Y but status is {st!r}")
            if not r["dnc_reason"].strip() or not r["dnc_date"].strip():
                rep.err(f"{where}: do_not_contact = Y needs dnc_reason and dnc_date")
        if st == "do_not_contact" and r["do_not_contact"].strip() != "Y":
            rep.err(f"{where}: status do_not_contact needs do_not_contact = Y")
        if r["reply_type"] == "opt_out" and r["do_not_contact"].strip() != "Y":
            rep.err(f"{where}: an opt_out reply must set do_not_contact = Y the same day")
        if r["lead_signal_kind"] and not r["lead_signal_logged_on"]:
            rep.warn(f"{where}: lead_signal_kind set but lead_signal_logged_on empty")
        pt, niche = r["persona_tag"].strip(), r["niche"].strip()
        if pt and niche in PERSONA_FOR_NICHE and PERSONA_FOR_NICHE[niche] != pt:
            rep.warn(f"{where}: persona_tag {pt} for niche {niche} (usual: {PERSONA_FOR_NICHE[niche]})")
        key = re.sub(r"\s+", "", r["entity_name"]).casefold()
        by_entity[key].append((n, r))
        if st and st not in CLOSED:
            open_by_entity[key].append((n, r))
    for key, items in open_by_entity.items():
        if len(items) > 1:
            rep.err(f"{path.name}: {len(items)} open threads for {items[0][1]['entity_name']!r} (rows {[n for n, _ in items]}); one per entity")
    groups = defaultdict(list)
    for key, items in open_by_entity.items():
        for n, r in items:
            if r["group_note"].strip():
                groups[r["group_note"].strip()].append((n, r))
    for g, items in groups.items():
        sent = [(n, r) for n, r in items if r["first_sent_date"]]
        if len(sent) > 1:
            ds = sorted(pdate(r["first_sent_date"]) for _, r in sent if pdate(r["first_sent_date"]))
            if len(ds) > 1 and (ds[-1] - ds[0]).days < 30:
                rep.warn(f"{path.name}: two open threads inside group {g!r} within 30 days (rows {[n for n, _ in sent]})")
    for key, items in by_entity.items():
        dncs = [pdate(r["dnc_date"]) for _, r in items if r["do_not_contact"].strip() == "Y" and pdate(r["dnc_date"])]
        if dncs:
            d0 = min(dncs)
            for n, r in items:
                f = pdate(r["first_sent_date"])
                if f and f > d0:
                    rep.err(f"{path.name}:{n}: contact on {f} after the entity was marked do-not-contact on {d0}")
        firsts = sorted((pdate(r["first_sent_date"]), n) for n, r in items if pdate(r["first_sent_date"]))
        for (d1, _), (d2, n2) in zip(firsts, firsts[1:]):
            if (d2 - d1).days < 90:
                rep.err(f"{path.name}:{n2}: a second first-contact {(d2 - d1).days} days after the previous one; the rest is 90 days")
    # funnel
    sent_rows = [r for r in rows if r["first_sent_date"].strip()]
    warm = [r for r in rows if r["route"] == "warm" and (r["first_sent_date"].strip() or r["status"] in SENT_OR_LATER | CLOSED)]
    f = {
        "rows": len(rows),
        "approached (first message sent)": len(sent_rows),
        "warm contacts approached (any niche)": len(warm),
        "warm fashion contacts approached": sum(1 for r in warm if r["niche"] == "fashion"),
        "replied": sum(1 for r in rows if r["reply_date"].strip()),
        "interested (interested or more_info)": sum(1 for r in rows if r["reply_type"] in ("interested", "more_info")),
        "samples scoped": sum(1 for r in rows if r["sample_scope"].strip()),
        "samples delivered": sum(1 for r in rows if r["sample_delivered_date"].strip()),
        "written quotes or rate sheets received": sum(1 for r in rows if r["written_quote_received"] == "Y"),
        "closed with no reply": sum(1 for r in rows if r["status"] == "closed_no_reply"),
        "do-not-contact": sum(1 for r in rows if r["do_not_contact"].strip() == "Y"),
    }
    return rep, f


# ----------------------------------------------------------------------------- main
def main(argv):
    scan_flag = "--scan" in argv
    if "--filled" in argv:
        p = Path(argv[argv.index("--filled") + 1])
        rep = check_filled(p)
        return finish(rep, f"filled check of {p.name}")
    if "--tracking" in argv:
        p = Path(argv[argv.index("--tracking") + 1])
        rep, funnel = check_tracking(p)
        for k, v in funnel.items():
            rep.info(f"funnel: {k}: {v}")
        if funnel:
            rep.info("toward the week-8 checkpoint (portfolio 6.4; counts of what happened, not targets): "
                     f"warm fashion contacts approached {funnel['warm fashion contacts approached']} of 5; "
                     f"samples delivered {funnel['samples delivered']} of 1; "
                     f"written quotes or rate sheets {funnel['written quotes or rate sheets received']} of 3")
        return finish(rep, f"tracking check of {p.name}")
    rep = Report()
    scan: list = [] if scan_flag else None
    check_lists(rep, scan)
    check_generated(rep)
    check_drafts(rep, scan)
    check_playbook(rep)
    check_links(rep)
    if scan_flag and scan:
        print("zh-TW scan (informational):")
        for s in scan:
            print("  " + s)
    return finish(rep, "outreach folder")


def finish(rep: Report, label: str):
    for m in rep.infos:
        print("INFO  " + m)
    for m in rep.warns:
        print("WARN  " + m)
    for m in rep.errors:
        print("ERROR " + m)
    print(f"{label}: {len(rep.errors)} error(s), {len(rep.warns)} warning(s), {len(rep.infos)} note(s)")
    return 1 if rep.errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
