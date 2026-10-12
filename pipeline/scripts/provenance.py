#!/usr/bin/env python3
"""provenance.py - append validated rows to assets/provenance.csv (BRIEF ground rule 2).

Standard library only. No network.

Columns, in this order, never changed:
    timestamp,asset_path,persona,tool,model,prompt,licence_notes

Rules enforced (a row that breaks one is REFUSED, nothing is written):
  * every column present and not blank
  * timestamp is ISO 8601: YYYY-MM-DD or YYYY-MM-DDTHH:MM[:SS][+08:00]  (Taiwan time with
    offset is the project convention; see pipeline/image-pack/README-photoreal.md section 6)
  * asset_path is relative to the project folder, uses no '..', and the file exists
    (override with --allow-missing-file only when logging a file you will move there today)
  * persona is a known slug (a folder under personas/ that holds bible.md) or 'studio'
  * no API-key-shaped text in prompt or licence_notes (secrets must never reach the log)
  * the existing file's header must match exactly; this script never edits or deletes old rows

Usage:
  python3 pipeline/scripts/provenance.py add --asset assets/fangcun/photoreal/R01_cand_gemini_1.png \\
      --persona fangcun --tool "Gemini (app)" --model "<label exactly as shown>" \\
      --prompt-file prompt.txt --licence-notes "Status: KEPT; ... commercial use per those terms: NOT CONFIRMED"
  python3 pipeline/scripts/provenance.py check          # validate the whole file

Exit codes: 0 ok, 1 row or file invalid (nothing written), 2 usage error.
"""
from __future__ import annotations

import argparse
import csv
import io
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path, PurePosixPath

COLUMNS = ["timestamp", "asset_path", "persona", "tool", "model", "prompt", "licence_notes"]
ROOT = Path(__file__).resolve().parents[2]
CSV_RELPATH = Path("assets") / "provenance.csv"

_TS_RE = re.compile(
    r"^\d{4}-\d{2}-\d{2}(?:[T ]\d{2}:\d{2}(?::\d{2})?(?:Z|[+-]\d{2}:\d{2})?)?$"
)
# Shapes of API keys / bearer tokens. Deliberately loose: a false alarm is cheap.
_SECRET_RES = [
    re.compile(r"AIza[0-9A-Za-z_\-]{30,}"),
    re.compile(r"\bsk-[A-Za-z0-9_\-]{20,}"),
    re.compile(r"\bBearer\s+[A-Za-z0-9_\-\.]{20,}"),
    re.compile(r"\b(?:x-goog-api-key|api[_-]?key)\s*[:=]\s*\S{12,}", re.IGNORECASE),
]


class ProvenanceError(Exception):
    """Raised with a list of human-readable problems; nothing was written."""

    def __init__(self, problems):
        self.problems = list(problems)
        super().__init__("; ".join(self.problems))


def taiwan_now() -> str:
    tz = timezone(timedelta(hours=8))
    return datetime.now(tz).isoformat(timespec="seconds")


def known_personas(root: Path) -> set[str] | None:
    """Slugs of folders under personas/ that hold bible.md, plus 'studio'.
    None if there is no personas/ folder (then the slug check is only a pattern check)."""
    pdir = root / "personas"
    if not pdir.is_dir():
        return None
    slugs = {p.name for p in pdir.iterdir() if p.is_dir() and (p / "bible.md").exists()}
    slugs.add("studio")
    return slugs


def contains_secret(text: str) -> bool:
    return any(rx.search(text) for rx in _SECRET_RES)


def validate_row(row: dict, root: Path = ROOT, *, check_exists: bool = True) -> list[str]:
    """Return a list of problems (empty list = valid)."""
    problems: list[str] = []
    extra = set(row) - set(COLUMNS)
    if extra:
        problems.append("unknown column(s): " + ", ".join(sorted(extra)))
    for col in COLUMNS:
        val = row.get(col)
        if val is None or not isinstance(val, str) or not val.strip():
            problems.append(f"missing or blank field: {col}")
    if problems:
        return problems  # no point checking shapes of missing values

    ts = row["timestamp"].strip()
    if not _TS_RE.match(ts):
        problems.append(f"timestamp not ISO 8601 (YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS+08:00): {ts!r}")
    else:
        try:
            datetime.fromisoformat(ts.replace("Z", "+00:00"))
        except ValueError:
            problems.append(f"timestamp is not a real date/time: {ts!r}")

    ap = row["asset_path"].strip()
    posix = PurePosixPath(ap.replace("\\", "/"))
    if posix.is_absolute() or re.match(r"^[A-Za-z]:", ap):
        problems.append("asset_path must be relative to the project folder, not absolute")
    elif ".." in posix.parts:
        problems.append("asset_path must not contain '..'")
    elif check_exists and not (root / Path(*posix.parts)).is_file():
        problems.append(f"asset_path does not exist as a file under the project folder: {ap}")

    persona = row["persona"].strip()
    slugs = known_personas(root)
    if not re.match(r"^[a-z][a-z0-9_\-]*$", persona):
        problems.append(f"persona must be a lower-case slug, got {persona!r}")
    elif slugs is not None and persona not in slugs:
        problems.append(f"unknown persona {persona!r}; known: {', '.join(sorted(slugs))}")

    for col in ("prompt", "licence_notes", "tool", "model"):
        if contains_secret(row[col]):
            problems.append(f"{col} looks like it contains an API key or bearer token; remove it")
    return problems


def _read_header_and_tail(csv_path: Path):
    raw = csv_path.read_bytes()
    text = raw.decode("utf-8")
    first = next(csv.reader(io.StringIO(text)), None)
    return first, text


def append_row(row: dict, root: Path = ROOT, *, check_exists: bool = True, csv_path: Path | None = None) -> Path:
    """Validate and append one row. Creates the file with the header if it does not exist.
    Never rewrites existing bytes. Raises ProvenanceError (nothing written) on any problem."""
    csv_path = csv_path or (root / CSV_RELPATH)
    clean = dict(row)
    problems = validate_row(clean, root, check_exists=check_exists)
    if problems:
        raise ProvenanceError(problems)
    clean = {c: clean[c].strip() if c in ("timestamp", "asset_path", "persona", "tool", "model") else clean[c]
             for c in COLUMNS}

    if csv_path.exists() and csv_path.stat().st_size > 0:
        header, text = _read_header_and_tail(csv_path)
        if header != COLUMNS:
            raise ProvenanceError([f"existing header is {header!r}; refusing to append (never change the header)"])
        needs_newline = not text.endswith("\n")
        mode = "ab"
    else:
        csv_path.parent.mkdir(parents=True, exist_ok=True)
        needs_newline = False
        mode = "wb"

    buf = io.StringIO()
    w = csv.writer(buf)  # default lineterminator \r\n matches the existing file
    if mode == "wb":
        w.writerow(COLUMNS)
    w.writerow([clean[c] for c in COLUMNS])
    payload = buf.getvalue().encode("utf-8")
    with open(csv_path, mode) as fh:
        if needs_newline:
            fh.write(b"\r\n")
        fh.write(payload)
    return csv_path


def check_file(root: Path = ROOT, csv_path: Path | None = None, *, check_exists: bool = True) -> list[str]:
    """Validate every row of the existing file. Returns problems (empty = fine)."""
    csv_path = csv_path or (root / CSV_RELPATH)
    if not csv_path.exists():
        return [f"{csv_path} does not exist"]
    problems = []
    with open(csv_path, newline="", encoding="utf-8") as fh:
        rd = csv.reader(fh)
        header = next(rd, None)
        if header != COLUMNS:
            problems.append(f"header is {header!r}, expected {COLUMNS!r}")
            return problems
        for n, rec in enumerate(rd, start=2):
            if not rec:
                continue
            if len(rec) != len(COLUMNS):
                problems.append(f"row {n}: {len(rec)} fields, expected {len(COLUMNS)}")
                continue
            row = dict(zip(COLUMNS, rec))
            for p in validate_row(row, root, check_exists=check_exists):
                problems.append(f"row {n} ({row['asset_path']}): {p}")
    return problems


# --------------------------------------------------------------------------- CLI

def _build_parser():
    ap = argparse.ArgumentParser(description="Append validated rows to assets/provenance.csv")
    ap.add_argument("--root", type=Path, default=ROOT, help="project folder (default: two levels above this script)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    add = sub.add_parser("add", help="append one row")
    add.add_argument("--asset", required=True, help="path of the asset, relative to the project folder")
    add.add_argument("--persona", required=True)
    add.add_argument("--tool", required=True)
    add.add_argument("--model", required=True, help="label exactly as the tool shows it that day; never guess")
    g = add.add_mutually_exclusive_group(required=True)
    g.add_argument("--prompt")
    g.add_argument("--prompt-file", type=Path)
    h = add.add_mutually_exclusive_group(required=True)
    h.add_argument("--licence-notes")
    h.add_argument("--licence-notes-file", type=Path)
    add.add_argument("--timestamp", help="default: now, Taiwan time with +08:00")
    add.add_argument("--allow-missing-file", action="store_true",
                     help="log a file that is not under the project folder yet (use sparingly)")

    chk = sub.add_parser("check", help="validate every row already in the file")
    chk.add_argument("--no-check-exists", action="store_true", help="do not require files to exist")
    return ap


def main(argv=None) -> int:
    args = _build_parser().parse_args(argv)
    root = args.root.resolve()
    if args.cmd == "check":
        probs = check_file(root, check_exists=not args.no_check_exists)
        if probs:
            print("provenance.csv has problems:")
            for p in probs:
                print("  -", p)
            return 1
        print("provenance.csv: all rows pass.")
        return 0

    try:
        prompt = args.prompt if args.prompt is not None else args.prompt_file.read_text(encoding="utf-8").rstrip("\n")
        notes = (args.licence_notes if args.licence_notes is not None
                 else args.licence_notes_file.read_text(encoding="utf-8").rstrip("\n"))
    except (OSError, UnicodeDecodeError) as e:
        print(f"REFUSED, nothing written: cannot read a prompt or notes file as UTF-8 text ({type(e).__name__})", file=sys.stderr)
        return 2
    row = {
        "timestamp": args.timestamp or taiwan_now(),
        "asset_path": args.asset,
        "persona": args.persona,
        "tool": args.tool,
        "model": args.model,
        "prompt": prompt,
        "licence_notes": notes,
    }
    try:
        path = append_row(row, root, check_exists=not args.allow_missing_file)
    except ProvenanceError as e:
        print("REFUSED, nothing written:", file=sys.stderr)
        for p in e.problems:
            print("  -", p, file=sys.stderr)
        return 1
    print(f"Appended 1 row to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
