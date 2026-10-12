#!/usr/bin/env python3
"""check_launch_docs.py - consistency checks for everything in launch/. Standard library only; no network; edits nothing.

    python3 launch/check_launch_docs.py

Checks
  1. bio and name-field lengths: every table row `text` | N and every fenced block followed by "Length: N characters." matches len(text);
     every "B1 + B2 ...: **N** characters in total" line matches the joined table strings
  2. handles: every handle row in launch/personas/<slug>.md has length N correct, appears in personas/<slug>/bible.md and
     personas/README.md, and every platform cell says UNCHECKED (no availability is ever claimed)
  3. disclosure: every name field carries 「AI 虛擬角色」; every line-1 bio carries 「AI 虛擬角色」 and 「明說角色工作室」
  4. zh-TW: the project's scanners (pipeline/scripts/ground_rules.py) over every backticked, fenced and 「quoted」 Chinese string
     (flag, never fix), and a Simplified-character scan of every text file in launch/
  5. links and file references: markdown links and backticked repo paths resolve
  6. weekdays: every "Mon 2026-11-16" style date has the right weekday
  7. secrets: no e-mail address, phone number, API-key shape or "password:" assignment anywhere in launch/

Exit code 1 if any ERROR. WARN and INFO are for a human to read.
"""
from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.append(str(ROOT / "pipeline" / "scripts"))
import ground_rules  # type: ignore  # noqa: E402

PERSONAS = {"fangcun": "方寸", "buzhou": "步驟", "sehuan": "色環"}
CJK = re.compile(r"[一-鿿　-〿＀-￯]")
TEXT_SUFFIXES = {".md", ".html", ".css", ".csv", ".py", ".svg", ".txt"}
# Disclaimer sentences reviewed as disclaimers (also skipped by link-pages/check_pages.py).
REVIEWED_DISCLAIMERS = [
    "不提供健康、醫療、投資或理財建議，也不談政治議題。",
    "不提供投資、醫療、法律或賺錢相關的建議。",
    "各角色的帳號不會互相追蹤、留言或推薦對方。",
]

errors: list[str] = []
warns: list[str] = []
infos: list[str] = []


def err(m): errors.append(m)
def warn(m): warns.append(m)
def info(m): infos.append(m)


def rel(p: Path) -> str:
    return str(p.relative_to(ROOT))


def files(suffixes=TEXT_SUFFIXES):
    for p in sorted(HERE.rglob("*")):
        if p.is_file() and p.suffix in suffixes and "screenshots" not in p.parts and "__pycache__" not in p.parts:
            yield p


# ----------------------------------------------------------------------------- 1. lengths
def table_cells(line: str):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def check_lengths(p: Path, text: str):
    rows = {}
    for ln in text.splitlines():
        if not ln.startswith("|"):
            continue
        cells = table_cells(ln)
        for i, c in enumerate(cells[:-1]):
            m = re.fullmatch(r"`([^`]*)`", c)
            if m and CJK.search(m.group(1)) and re.fullmatch(r"\d+", cells[i + 1]):
                s, n = m.group(1), int(cells[i + 1])
                if len(s) != n:
                    err(f"{rel(p)}: stated length {n} but the text has {len(s)} characters: {s[:30]}...")
                else:
                    info(f"{rel(p)}: length {n} ok ({s[:12]}...)")
                if cells and re.fullmatch(r"[A-Z]\d+(-alt)?", cells[0]):
                    rows[cells[0]] = s
    # fenced blocks followed by "Length: N characters."
    for m in re.finditer(r"```\n(.*?)\n```\n\nLength: (\d+) characters\.", text, flags=re.S):
        s, n = m.group(1), int(m.group(2))
        if len(s) != n:
            err(f"{rel(p)}: fenced block states {n} characters but has {len(s)}")
        else:
            info(f"{rel(p)}: fenced block length {n} ok")
    # totals: "* B1 + B2 (...): **82** characters in total"
    for m in re.finditer(r"^\* ((?:B[\w-]+)(?: \+ B[\w-]+)+)[^:]*: \*\*(\d+)\*\* characters in total", text, flags=re.M):
        ids = re.findall(r"B[\w-]+", m.group(1))
        if all(i in rows for i in ids):
            n = len("\n".join(rows[i] for i in ids))
            if n != int(m.group(2)):
                err(f"{rel(p)}: total for {' + '.join(ids)} states {m.group(2)} but is {n}")
            else:
                info(f"{rel(p)}: total {' + '.join(ids)} = {n} ok")
        else:
            warn(f"{rel(p)}: cannot recompute total for {ids} (an id is not in a table row)")
    return rows


def check_persona(slug: str):
    p = HERE / "personas" / f"{slug}.md"
    text = p.read_text(encoding="utf-8")
    rows = check_lengths(p, text)
    # 3. disclosure
    name_row = re.search(r"\| N1 \|[^|]*\| `([^`]+)` \|", text)
    if not name_row or "AI 虛擬角色" not in name_row.group(1):
        err(f"{rel(p)}: N1 name field missing or lacks 「AI 虛擬角色」")
    for ln in text.splitlines():
        cells = table_cells(ln) if ln.startswith("|") else []
        if len(cells) >= 3 and re.fullmatch(r"B\d", cells[0]) and ("line 1" in cells[1] or "Threads bio" in cells[1] or "Instagram bio, line 1" in cells[1]):
            t = cells[2].strip("`")
            for need in ("AI 虛擬角色", "明說角色工作室"):
                if need not in t:
                    err(f"{rel(p)}: line-1 bio {cells[0]} lacks 「{need}」")
    # 2. handles
    bible = (ROOT / "personas" / slug / "bible.md").read_text(encoding="utf-8")
    readme = (ROOT / "personas" / "README.md").read_text(encoding="utf-8")
    seen = 0
    for ln in text.splitlines():
        m = re.match(r"\| (\d) \| `([A-Za-z0-9_.]+)` \| (\d+) \|(.*)\|", ln)
        if not m:
            continue
        seen += 1
        h, n, rest = m.group(2), int(m.group(3)), m.group(4)
        if len(h) != n:
            err(f"{rel(p)}: handle {h} stated {n} characters, is {len(h)}")
        if h not in bible:
            err(f"{rel(p)}: handle {h} does not appear in personas/{slug}/bible.md")
        if h not in readme:
            warn(f"{rel(p)}: handle {h} does not appear in personas/README.md")
        cells = [c.strip() for c in rest.split("|")]
        status_cells = [c for c in cells[:-1]]  # last cell is the risk text
        if not status_cells or any(c != "UNCHECKED" for c in status_cells):
            err(f"{rel(p)}: handle {h} row has a platform cell that is not UNCHECKED: {status_cells}")
    if seen != 3:
        err(f"{rel(p)}: expected 3 handle rows, found {seen}")
    else:
        info(f"{rel(p)}: 3 handles, all UNCHECKED, all in the bible")


# ----------------------------------------------------------------------------- 4. zh-TW
def zh_spans(text: str):
    spans = []
    for m in re.finditer(r"```\n(.*?)\n```", text, flags=re.S):
        if CJK.search(m.group(1)):
            spans.append(m.group(1))
    no_fence = re.sub(r"```.*?```", "", text, flags=re.S)
    for m in re.finditer(r"`([^`\n]*)`", no_fence):
        if CJK.search(m.group(1)):
            spans.append(m.group(1))
    for m in re.finditer(r"「([^」\n]+)」", no_fence):
        spans.append(m.group(1))
    return spans


def check_zh(p: Path, text: str):
    # the link-pages README keeps the page strings in table cells without backticks
    spans = zh_spans(text)
    if p.name == "README.md" and p.parent.name == "link-pages":
        for ln in text.splitlines():
            if ln.startswith("|") and not ln.startswith("|---"):
                c = table_cells(ln)
                if c and CJK.search(c[0]):
                    spans.append(c[0])
    hits = 0
    for s in spans:
        scan = s
        for d in REVIEWED_DISCLAIMERS:
            scan = scan.replace(d, "")
        for f in ground_rules.scan_text(scan, rel(p)):
            if f.level in ("ERROR", "FLAG"):
                hits += 1
                (warn if is_meta(s) else err)(f"{rel(p)}: {f.render()}")
            elif f.level == "WARN":
                warn(f"{rel(p)}: {f.render()}")
    return len(spans), hits


def is_meta(s: str) -> bool:
    """A short quoted term that the file is *talking about* (for example a banned word or a hashtag rule), not copy to publish."""
    return len(s) <= 8


# ----------------------------------------------------------------------------- 5. links
SEARCH_ROOTS = [ROOT, HERE, HERE / "link-pages", HERE / "personas", HERE / "templates", ROOT / "pipeline", ROOT / "pipeline" / "scripts",
                ROOT / "personas", ROOT / "research", ROOT / "strategy", ROOT / "content", ROOT / "pipeline" / "image-pack"]
# Shorthand used inside the persona files: `bible.md` means personas/<slug>/bible.md, `calendar-30d.md` means content/<slug>/calendar-30d.md,
# `<slug>-photoreal.md` means pipeline/image-pack/<slug>-photoreal.md.
SEARCH_ROOTS += sorted((ROOT / "personas").glob("*/")) + sorted((ROOT / "content").glob("*/"))


def resolves(ref: str, base: Path) -> bool:
    ref = ref.split("#")[0]
    if not ref:
        return True
    for root in [base] + SEARCH_ROOTS:
        if (root / ref).exists():
            return True
    # persona-file style references: personas/<slug>/bible.md resolved from ROOT already; a `pack` shorthand is skipped by the caller
    return False


def check_links(p: Path, text: str):
    for m in re.finditer(r"\]\(([^)\s]+)\)", text):
        ref = m.group(1)
        if re.match(r"^[a-z]+:", ref) or ref.startswith("#"):
            continue
        if not (p.parent / ref.split("#")[0]).exists():
            err(f"{rel(p)}: broken markdown link {ref}")
    for m in re.finditer(r"`([^`\n]+)`", text):
        s = m.group(1).strip()
        if not re.fullmatch(r"[\w./-]+\.(md|py|csv|svg|html|css|json)", s):
            continue
        if any(ch in s for ch in "<>{}*") or s.startswith("assets/") or s.startswith("pipeline/review-queue/"):
            continue
        if not resolves(s, p.parent):
            if s in {"avatar.webp", "post.json", "index.html", "media/.gitkeep"}:
                continue
            err(f"{rel(p)}: file reference not found: {s}")


# ----------------------------------------------------------------------------- 6. weekdays
DAYNAMES = {"Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4, "Sat": 5, "Sun": 6}


def check_weekdays(p: Path, text: str):
    for m in re.finditer(r"\b(Mon|Tue|Wed|Thu|Fri|Sat|Sun)\w* (20\d\d-\d\d-\d\d)\b", text):
        try:
            d = dt.date.fromisoformat(m.group(2))
        except ValueError:
            err(f"{rel(p)}: bad date {m.group(2)}")
            continue
        if d.weekday() != DAYNAMES[m.group(1)]:
            err(f"{rel(p)}: {m.group(1)} {m.group(2)} is a {list(DAYNAMES)[d.weekday()]}")


# ----------------------------------------------------------------------------- 7. secrets
SECRET_PATTERNS = [
    (r"[\w.+-]+@[\w-]+\.[\w.-]+", "e-mail address"),
    (r"(?<!\d)(?:\+?886[- ]?)?0?9\d{2}[- ]?\d{3}[- ]?\d{3}(?!\d)", "Taiwan mobile number shape"),
    (r"AIza[0-9A-Za-z_-]{20,}", "Google API key shape"),
    (r"sk-[A-Za-z0-9]{20,}", "secret key shape"),
    (r"(?i)\b(password|passwd|passphrase|secret|token)\s*[:=]\s*\S+", "credential assignment"),
    (r"otpauth://", "authenticator URI"),
]


def check_secrets(p: Path, text: str):
    for pat, what in SECRET_PATTERNS:
        for m in re.finditer(pat, text):
            frag = m.group(0)
            if what == "e-mail address" and (frag.endswith(".css") or "@HANDLE" in frag or frag.startswith("@")):
                continue
            err(f"{rel(p)}: looks like a secret ({what}): {frag[:4]}... (rest not printed)")


def main() -> int:
    for slug in PERSONAS:
        check_persona(slug)
    spans_total = 0
    for p in files():
        text = p.read_text(encoding="utf-8")
        if p.name == "check_launch_docs.py":
            continue  # this file contains the secret patterns it searches for
        check_secrets(p, text)
        simp = sorted({c for c in text if c in ground_rules.SIMPLIFIED_SET})
        if simp:
            err(f"{rel(p)}: Simplified character(s): {' '.join(simp)}")
        if p.suffix == ".md":
            check_links(p, text)
            check_weekdays(p, text)
            n, hits = check_zh(p, text)
            spans_total += n
    print(f"scanned {sum(1 for _ in files())} files, {spans_total} Chinese spans")
    for m in infos:
        if "ok (" in m or "ok" in m:
            pass
    ok_lengths = sum(1 for m in infos if "length" in m and "ok" in m)
    print(f"lengths verified: {ok_lengths}; handles: see below")
    for m in infos:
        if "handles, all UNCHECKED" in m:
            print("info ", m)
    for m in warns:
        print("WARN ", m)
    for m in errors:
        print("ERROR", m)
    print("\nRESULT:", "FAIL" if errors else "PASS", f"({len(errors)} error, {len(warns)} warn)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
