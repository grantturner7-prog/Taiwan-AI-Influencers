#!/usr/bin/env python3
"""check_kits.py - consistency checks for the media kits in this folder. Standard library only; no network; edits nothing.

    python3 -B monetisation/media-kits/check_kits.py                 # check the four template kits
    python3 -B monetisation/media-kits/check_kits.py --scan          # also list every zh-TW wording flag (informational)
    python3 -B monetisation/media-kits/check_kits.py --filled FILE   # send-ready check of a filled working copy

Template mode (default) checks, for fangcun.md, buzhou.md, sehuan.md and studio.md
  1. structure: every numbered section exists, in order, plus Part A and appendix C, and at least three OPERATOR ONLY boxes
  2. bilingual rows: in a zh|English table every left cell has Chinese and every right cell has Latin letters
  3. placeholders: every row with a zh placeholder (【待填) has the English one ([TO FILL WHEN REAL) and the reverse
  4. data tables (audience and performance figures; studio-level figures): every data cell is exactly the empty placeholder
     pair, so no number can sit in them by accident
  5. no invented facts anywhere in a kit: no NT$ amount, no follower or subscriber count, no e-mail address, no phone number,
     no 8-digit business ID, no "24 hours" take-down figure (an internal rule that must not appear in a public promise)
  6. zh-TW: no Simplified character, no mainland vocabulary from the project scanner, and no gendered pronoun (他 她) for a character
     (operator boxes are skipped for the pronoun check because they quote the rule)
  7. references: backticked repo paths resolve
Filled mode (--filled FILE) checks that a working copy is ready to send: no placeholder, no OPERATOR ONLY box, no appendix, no
[D8] or [C2] marker and no unfilled {brace} slot remains; and no leak of internal wording that survives deleting Part A and the boxes
(draft or "for the operator" headers, "v0.1", the wife named as reviewer, repo file names, HUMAN_TODO numbers, gate numbers, "A1"). It cannot tell whether a number is true: the wife and operator still check
every figure against its screenshot (README.md section 4).

Exit code 1 if any ERROR. WARN and INFO are for a human to read.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.append(str(ROOT / "pipeline" / "scripts"))
try:
    import ground_rules  # type: ignore  # noqa: E402
except Exception:  # pragma: no cover - the scanner is optional
    ground_rules = None

KITS = ["fangcun.md", "buzhou.md", "sehuan.md", "studio.md"]
PERSONA_SECTIONS = list(range(0, 13))
STUDIO_SECTIONS = list(range(0, 11))
CJK = re.compile(r"[一-鿿]")
LATIN = re.compile(r"[A-Za-z]")
PRONOUN_OK = re.compile(r"其他|排他|他人|他處|他方|他國|利他|其它")   # compounds that are not pronouns
PH_ZH = "【待填"
PH_EN = "[TO FILL WHEN REAL"
PH_PAIR = "【待填】 [TO FILL WHEN REAL]"

errors: list[str] = []
warns: list[str] = []
infos: list[str] = []


def err(m): errors.append(m)
def warn(m): warns.append(m)
def info(m): infos.append(m)


def cells(line: str):
    s = line.strip()
    if s.startswith(">"):
        s = s.lstrip(">").strip()
    return [c.strip() for c in s.strip("|").split("|")]


def is_table_row(line: str) -> bool:
    s = line.strip().lstrip(">").strip()
    return s.startswith("|") and s.endswith("|")


def is_sep(line: str) -> bool:
    return bool(re.fullmatch(r"\|?(\s*:?-{3,}:?\s*\|)+\s*", line.strip().lstrip(">").strip()))


def sections(lines):
    """Yield (line_no, line, current_section) where current_section is an int, 'A', 'C' or None."""
    cur = None
    for n, ln in enumerate(lines, 1):
        m = re.match(r"^## (\d+)\.", ln)
        if m:
            cur = int(m.group(1))
        elif ln.startswith("## Part A"):
            cur = "A"
        elif ln.startswith("## 附錄 C"):
            cur = "C"
        yield n, ln, cur


def check_template(path: Path, scan: bool):
    name = path.name
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    studio = name == "studio.md"
    expected = STUDIO_SECTIONS if studio else PERSONA_SECTIONS
    data_section = 8 if studio else 10

    # 1. structure
    found = [int(m.group(1)) for ln in lines if (m := re.match(r"^## (\d+)\.", ln))]
    if found != expected:
        err(f"{name}: numbered sections are {found}, expected {expected}")
    if not any(ln.startswith("## Part A") for ln in lines):
        err(f"{name}: no 'Part A' section")
    if not any(ln.startswith("## 附錄 C") for ln in lines):
        err(f"{name}: no appendix C")
    boxes = sum(1 for ln in lines if ln.startswith("> **OPERATOR ONLY"))
    if boxes < 3:
        err(f"{name}: expected at least 3 OPERATOR ONLY boxes, found {boxes}")
    else:
        info(f"{name}: {boxes} OPERATOR ONLY boxes")

    # 2 and 3 and 4: tables
    header = None
    ph_rows = 0
    for n, ln, sec in sections(lines):
        if not is_table_row(ln):
            header = None
            continue
        if is_sep(ln):
            continue
        cs = cells(ln)
        if header is None:
            header = cs
            continue
        row = " ".join(cs)
        has_zh_ph, has_en_ph = PH_ZH in row, PH_EN in row
        if has_zh_ph != has_en_ph and not ln.lstrip().startswith(">"):   # operator boxes talk about placeholders in general
            err(f"{name}:{n}: placeholder in only one language: {row[:80]}")
        if has_zh_ph:
            ph_rows += 1
        # bilingual two-column tables: header is exactly the zh/en pair
        if len(header) == 2 and header[0].startswith("繁體中文") and sec not in ("A", "C"):
            if not CJK.search(cs[0]):
                err(f"{name}:{n}: left (zh-TW) cell has no Chinese: {cs[0][:60]}")
            if not LATIN.search(cs[1]):
                err(f"{name}:{n}: right (English) cell has no Latin letters: {cs[1][:60]}")
        # data tables
        if sec == data_section and len(header) >= 3 and (
                any("資料來源" in h or "Source" in h for h in header) or header[0].startswith(("貼文編號", "日期", "欄位 / Item"))):
            if header[0].startswith("日期") and all(not c for c in cs):
                continue
            for i, c in enumerate(cs):
                if i == 0 and not header[0].startswith(("貼文編號", "日期")):
                    continue
                if c != PH_PAIR:
                    err(f"{name}:{n}: data cell is not the empty placeholder pair (column {i + 1}): {c[:70]}")
    info(f"{name}: {ph_rows} rows carry placeholders")

    # 5. invented facts
    for n, ln in enumerate(lines, 1):
        if re.search(r"NT\$\s?\d|NTD\s?\d|新台幣\s?\d|\d\s?元(?!件)", ln):
            err(f"{name}:{n}: a currency amount appears; the kits state no price: {ln[:80]}")
        if re.search(r"\d[\d,]*\s*(?:followers?|subscribers?|追蹤者|粉絲|訂閱者|訂閱)", ln, flags=re.I):
            err(f"{name}:{n}: a follower or subscriber count appears: {ln[:80]}")
        if re.search(r"[\w.+-]+@[\w-]+\.[\w.]+", ln):
            err(f"{name}:{n}: an e-mail address appears: {ln[:80]}")
        if re.search(r"(?<!\d)0\d{1,2}[- ]?\d{3,4}[- ]?\d{3,4}(?!\d)", ln):
            err(f"{name}:{n}: a phone-number shape appears: {ln[:80]}")
        if re.search(r"(?<![\d.])\d{8}(?![\d.])", ln):
            err(f"{name}:{n}: an 8-digit number (business-ID shape) appears: {ln[:80]}")
        if re.search(r"24\s*小時|24[- ]?hours?|二十四小時", ln, flags=re.I):
            err(f"{name}:{n}: a '24 hours' figure appears; the take-down time limit is internal and must not be in a kit: {ln[:80]}")

    # 6. zh-TW
    zh_cells = []
    for n, ln, sec in sections(lines):
        if not CJK.search(ln):
            continue
        in_box = ln.startswith(">")
        for c in (cells(ln) if is_table_row(ln) else [ln]):
            if CJK.search(c):
                zh_cells.append((n, c, in_box))
    simp = getattr(ground_rules, "SIMPLIFIED_SET", frozenset()) if ground_rules else frozenset()
    for n, c, in_box in zh_cells:
        bad = sorted({ch for ch in c if ch in simp})
        if bad:
            err(f"{name}:{n}: Simplified character(s) {' '.join(bad)}: {c[:60]}")
        if not in_box and re.search(r"[他她牠祂]", PRONOUN_OK.sub("", c)):
            err(f"{name}:{n}: gendered pronoun in brand-facing Chinese: {c[:60]}")
        if ground_rules:
            for w in getattr(ground_rules, "MAINLAND_HIGH", {}):
                if w in c:
                    err(f"{name}:{n}: mainland vocabulary 「{w}」 (use {ground_rules.MAINLAND_HIGH[w]}): {c[:60]}")
    if not ground_rules:
        warn(f"{name}: pipeline/scripts/ground_rules.py not found; Simplified and mainland-vocabulary checks skipped")
    if scan and ground_rules:
        counts: dict[str, int] = {}
        seen = set()
        for n, c, in_box in zh_cells:
            if in_box:
                continue
            for f in ground_rules.scan_text(c, f"{name}:{n}"):
                key = (f.code, c)
                if key in seen:
                    continue
                seen.add(key)
                counts[f.code] = counts.get(f.code, 0) + 1
                info(f"SCAN {f.level} {f.code} {name}:{n}: {f.message[:70]} :: {c[:50]}")
        info(f"{name}: scanner flags by code: {counts}")

    # 7. references
    for n, ln in enumerate(lines, 1):
        for ref in re.findall(r"`([^`\n]+)`", ln):
            r = ref.strip()
            if not re.search(r"\.(md|py|csv|html|json)$", r) or " " in r or "{" in r or "<" in r:
                continue
            if r in KITS or r in ("README.md", "check_kits.py"):
                continue
            if "/" in r:
                if not (ROOT / r).exists():
                    err(f"{name}:{n}: referenced path does not exist: {r}")
            else:
                if not (ROOT / r).exists() and not (HERE / r).exists():
                    warn(f"{name}:{n}: bare file name does not resolve at the repo root or here: {r}")


def check_filled(path: Path):
    text = path.read_text(encoding="utf-8")
    name = path.name
    tests = [
        (PH_ZH, "an unfilled 【待填】 placeholder"),
        (PH_EN, "an unfilled [TO FILL WHEN REAL] placeholder"),
        ("OPERATOR ONLY", "an OPERATOR ONLY box"),
        ("## Part A", "Part A"),
        ("## 附錄 C", "appendix C"),
        ("［D8］", "a [D8] marker (keep the sentence only if the wife and lawyer agreed, then delete the marker)"),
        ("[D8]", "a [D8] marker"),
        ("［待確認］", "a ［待確認］ marker"),
        ("[C2]", "a [C2] marker"),
    ]
    for needle, what in tests:
        for n, ln in enumerate(text.splitlines(), 1):
            if needle in ln:
                err(f"{name}:{n}: {what} remains: {ln.strip()[:80]}")
    # Draft headers and internal references survive the deletion of Part A, the boxes and appendix C unless they are edited by hand.
    # A brand must not see "待太太審閱", "for the operator", "DRAFT v0.1", a repo file name, a gate number or the reviewer's role.
    leaks = [
        (r"太太|[Tt]he wife\b", "the wife / reviewer's role named in brand-facing text (say 母語審閱者 / native reviewer)"),
        (r"for the operator|v0\.1|DRAFT", "a draft or operator-only header (edit the column headers and the status line after the wife's read)"),
        (r"繁體中文[（(]?草稿", "a 'zh-TW draft' column header"),
        (r"HUMAN_TODO|legal\.md|portfolio\.md|DECISIONS|rate-card\.md|research/|launch/|analytics/|bible|photoreal addendum|addendum",
         "an internal repo reference"),
        (r"附錄|[Aa]ppendix|\bGates? ?\d|\bA1\b", "a reference to Part A / appendix / a gate number, which the sent copy no longer has"),
    ]
    for n, ln in enumerate(text.splitlines(), 1):
        for pat, what in leaks:
            m = re.search(pat, ln)
            if m:
                err(f"{name}:{n}: {what}: 「{m.group(0)}」 in {ln.strip()[:70]}")
    for n, ln in enumerate(text.splitlines(), 1):
        if "……" in ln:
            warn(f"{name}:{n}: an abridged passage (……) remains; paste the full approved text from launch/personas/<slug>.md: {ln.strip()[:70]}")
    for n, ln in enumerate(text.splitlines(), 1):
        if re.search(r"\{[^}\n]{1,20}\}", ln) and not re.search(r"\{(廠商|品牌|角色名|工具|版本|方案|額度|YYYY/MM/DD|官方頁面名稱|內容|vendor|brand|name|tool)", ln):
            warn(f"{name}:{n}: a {{brace}} slot remains: {ln.strip()[:80]}")
    # the fixed disclosure templates keep {廠商}, {品牌} and similar slots on purpose: they are templates in the kit
    if re.search(r"NT\$\s?\d", text) and not re.search(r"NT\$\s?\d[\d,]*\s*[（(]?(?:報價|quote)", text):
        info(f"{name}: a currency amount appears; make sure it comes from a written quote or the rate card, never from this kit")
    info(f"{name}: send-ready check finished. It cannot tell whether a figure is true: the wife and operator check each against its screenshot")


def main(argv):
    scan = "--scan" in argv
    if "--filled" in argv:
        i = argv.index("--filled")
        if i + 1 >= len(argv):
            print("--filled needs a file")
            return 2
        check_filled(Path(argv[i + 1]))
    else:
        for k in KITS:
            p = HERE / k
            if not p.exists():
                err(f"missing {k}")
                continue
            check_template(p, scan)
    for lst, label in ((errors, "ERROR"), (warns, "WARN"), (infos, "INFO")):
        for m in lst:
            print(f"{label} {m}")
    print(f"\n{len(errors)} error(s), {len(warns)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
