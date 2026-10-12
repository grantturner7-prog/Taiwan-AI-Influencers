#!/usr/bin/env python3
"""screenshot.py - full-page screenshots of the link pages with headless Chromium (no network, local files only).

    python3 launch/link-pages/screenshot.py                 # all four pages at 390 px (phone) into launch/link-pages/screenshots/
    python3 launch/link-pages/screenshot.py --widths 320 390 1280
    python3 launch/link-pages/screenshot.py --pages fangcun studio

Needs: Chromium (default path below; override with CHROMIUM_BIN) and Pillow (pip install pillow) to trim the blank space.
Headless Chromium lays pages out at no less than 500 px wide, so for phone widths the page is loaded inside an iframe of
exactly the requested width (a pixel-identical result to Chromium's headless shell, checked 2026-10-12).
The scratch HTML for that is written to a temporary folder and deleted.
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHROMIUM = os.environ.get("CHROMIUM_BIN", "/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
TALL = 4600  # window height; pages are about 2,000 to 3,300 px tall at phone width


def shoot(page: Path, width: int, out: Path) -> tuple[int, int]:
    from PIL import Image, ImageChops  # imported late so --help works without Pillow

    with tempfile.TemporaryDirectory() as tmp:
        raw = Path(tmp) / "raw.png"
        base = [CHROMIUM, "--headless", "--no-sandbox", "--disable-gpu", "--hide-scrollbars", f"--screenshot={raw}"]
        if width >= 500:
            cmd = base + [f"--window-size={width},{TALL}", page.resolve().as_uri()]
        else:
            harness = Path(tmp) / "h.html"
            harness.write_text(
                f'<!doctype html><body style="margin:0;background:#ff00ff"><iframe src="{page.resolve().as_uri()}" '
                f'width="{width}" height="{TALL - 150}" style="border:0;display:block"></iframe>',
                encoding="utf-8",
            )
            cmd = base + [f"--window-size=500,{TALL}", harness.as_uri()]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120, check=False)
        im = Image.open(raw).convert("RGB")
    if width < 500:
        im = im.crop((0, 0, width, min(im.height, TALL - 150)))
    bg = im.getpixel((2, 300))  # page background in the left margin
    bbox = ImageChops.difference(im, Image.new("RGB", im.size, bg)).getbbox()
    bottom = min(im.height, (bbox[3] + 24) if bbox else im.height)
    out.parent.mkdir(parents=True, exist_ok=True)
    im.crop((0, 0, im.width, bottom)).save(out, optimize=True)
    return im.width, bottom


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--widths", nargs="+", type=int, default=[390])
    ap.add_argument("--pages", nargs="+", default=["fangcun", "buzhou", "sehuan", "studio"])
    ap.add_argument("--out", type=Path, default=HERE / "screenshots")
    a = ap.parse_args()
    if not Path(CHROMIUM).exists():
        print(f"Chromium not found at {CHROMIUM}; set CHROMIUM_BIN", file=sys.stderr)
        return 2
    for slug in a.pages:
        for w in a.widths:
            out = a.out / f"{slug}_{w}.png"
            print(out, *shoot(HERE / slug / "index.html", w, out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
