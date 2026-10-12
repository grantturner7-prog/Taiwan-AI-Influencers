#!/usr/bin/env python3
"""Render an SVG to PNG with headless Chromium (Noto Sans TC must be installed: see INSTALL_FONT.md).
Usage: render.py in.svg out.png WIDTH HEIGHT [--bg "#RRGGBB"]
Headless Chromium reserves ~88px of the window for browser chrome, so the window is made taller and the PNG cropped (needs Pillow).
Exits non-zero if the font is missing, so a fallback font is never shipped silently.
"""
import os, subprocess, sys, tempfile

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

def font_ok():
    out = subprocess.run(["fc-list", ":lang=zh-tw", "family"], capture_output=True, text=True).stdout
    return "Noto Sans TC" in out

def render(svg, png, w, h, bg="#FFFFFF"):
    if not font_ok():
        sys.exit("Noto Sans TC not installed: see pipeline/art/INSTALL_FONT.md")
    svg = os.path.abspath(svg)
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write(f'<!doctype html><html lang="zh-Hant-TW"><body style="margin:0;background:{bg}">'
                f'<img src="file://{svg}" style="display:block;width:{w}px;height:{h}px"></body></html>')
        html = f.name
    tmp = png + ".tmp.png"
    subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                    "--allow-file-access-from-files", f"--screenshot={tmp}",
                    f"--window-size={w},{h + 120}", f"file://{html}"],
                   check=True, capture_output=True)
    os.unlink(html)
    from PIL import Image
    im = Image.open(tmp)
    im.crop((0, 0, w, h)).save(png)
    os.unlink(tmp)

if __name__ == "__main__":
    a = sys.argv[1:]
    bg = "#FFFFFF"
    if "--bg" in a:
        i = a.index("--bg"); bg = a[i + 1]; del a[i:i + 2]
    render(a[0], a[1], int(a[2]), int(a[3]), bg)
