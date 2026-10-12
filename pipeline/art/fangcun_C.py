#!/usr/bin/env python3
"""fangcun_C.py - 方寸 master C 「買前先量・搬家清單」 (calendar M2 · 先量再買 #01), v0.1 DRAFT.

Draws the frames of two posts as SVG (standard library only) and renders the previews to PNG with
pipeline/art/render.py (headless Chromium + Noto Sans TC; see INSTALL_FONT.md):

    P03  fangcun-2026-11-19-01  Instagram Reel      9 scenes
    P04  fangcun-2026-11-20-01  YouTube Short       6 scenes (scene 2 is three cumulative reveal steps)

Canvas 1080 x 1920 (9:16). No image model is used: every shape, number, Chinese string and badge is code.
Decision D3 (DECISIONS.md 2026-10-12): Claude draws the diagram layer; the operator and the wife approve every
asset; Claude cannot edit video, so the user assembles the Reel and Short from these frames.

Per frame, two outputs in assets/fangcun/diagrams/C/ :
    <id>.svg          FINAL LAYER. The photoreal character does not exist yet, so the picture slot is an empty,
                      transparent <g id="character-slot"> (geometry in its data-* attributes). Composite the approved
                      golden-set still into that rectangle later (clip to rx); the frame ring around it is already drawn
                      OUTSIDE the slot, so nothing here needs to change.
    <id>_preview.png  PROOF RENDER. The same SVG with the slot filled by a neutral rounded rectangle and the small grey
                      English text CHARACTER PANEL: PENDING. Never publish a preview.
Frames with no character (the closing frames) have no slot; their preview PNG is pixel-identical to the final.
frames.json lists every frame, its post, its scene, its badge and its slot rectangle.

Rules baked in (calendar-30d.md 7.2, photoreal-addendum 8.2, qa-checklist D3/S2/T9):
  * Badge: solid charcoal pill, off-white text, text 68 px (3.5% of the height), top-left at x=90 (8.3% of the
    width) and y=300 (15.6% of the height; the rule is at least 11%, and a 4:5 centre crop removes 285 px at the top).
    Wording 「AI 生成｜虛擬角色」 on frames that carry the character slot, 「AI 生成｜示意圖」 on pure-diagram frames.
    Same place on every frame, so it is persistent from the first frame to the last.
  * Content stays inside x 90..930 and y 300..1560 (wide margins for platform buttons, captions, progress bar;
    Reels and Shorts safe zones are unverified, HUMAN_TODO 25).
  * Palette only: ground #F5F0E6, oat #E4D9C3, putty #CFC6B4, walnut #6E5440, deep walnut #5C4636, belt cream
    #EFE6CF, sage #A9B5A0 (small accent), charcoal #3B3631. The one exception is the grey of the preview-only label.
  * No dimensions, no product shapes, no brands, no people other than the empty character slot. The only digits are the
    ordinals 1 to 5 of the checklist. Text is Noto Sans TC with lang zh-Hant-TW and no fallback font.
  * Every Chinese string is the approved string of the post (or a word taken from one of them); see STRINGS.

Usage:
    python3 pipeline/art/fangcun_C.py                 # write SVGs, render previews, write frames.json
    python3 pipeline/art/fangcun_C.py --svg-only      # SVGs and frames.json only (no Chromium needed)
    python3 pipeline/art/fangcun_C.py --only reel_s03_width --keep-preview-svg
"""
import argparse
import json
import math
import os
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT_DIR = os.path.join(ROOT, "assets", "fangcun", "diagrams", "C")
OUT_REL = "assets/fangcun/diagrams/C"
RENDER = os.path.join(HERE, "render.py")
SCRIPT_REL = "pipeline/art/fangcun_C.py"
VERSION = "v0.1"

W, H = 1080, 1920
MX0, MX1 = 90, 930            # content box (840 wide)
BADGE_X, BADGE_Y = 90, 300
FONT = "'Noto Sans TC'"

# ---- palette (photoreal-addendum 4.1, calendar 7.2) ---------------------------------------------------------
GROUND, OAT, PUTTY, WALNUT = "#F5F0E6", "#E4D9C3", "#CFC6B4", "#6E5440"
DEEP, CREAM, SAGE, CHAR = "#5C4636", "#EFE6CF", "#A9B5A0", "#3B3631"
PREVIEW_GREY = "#7A756D"      # preview-only label (the brief asks for small grey English text)

BADGE_CHAR = "AI 生成｜虛擬角色"
BADGE_DIAG = "AI 生成｜示意圖"
NOTE = "請以現場丈量為準"

# approved strings, verbatim from calendar-30d.md P03 / P04 (and the queue post.json)
STRINGS = {
    "reel_hook": ["買收納櫃之前，", "先確認五件事"],
    "short_hook": ["收納櫃下單前，", "五件事先確認"],
    "intro": "我是方寸，AI 虛擬角色。",
    "1": ("寬", ["要放的那面牆，", "寬度夠不夠"]),
    "2": ("深", ["櫃子越深，", "前面的走道越窄"]),
    "3": ("高", ["天花板高度、", "窗台高度要一起看"]),
    "4": ("門怎麼開", ["門板轉出來，", "要留多少位置"]),
    "5": ("搬運路線", ["大門、走廊、電梯、", "轉角，都要過得去"]),
    "short_three": ["三個數字，", "決定櫃子放得進哪裡"],
    "closing": ["五件事都量好，", "再決定要不要買。"],
    "end_a": "工作室整理的一般清單，非法律或專業意見",
    "end_reel_cta": ["收藏起來，", "下單前逐項對照～"],
    "end_short_cta": ["收藏起來，", "下單前逐項對照"],
}
HEADINGS = [STRINGS[str(i)][0] for i in range(1, 6)]

# ---- text width estimate (em) for fit assertions only; measured with Noto Sans TC ----------------------------


def em(s):
    t = 0.0
    for ch in s:
        o = ord(ch)
        if o < 0x80:
            t += 0.22 if ch == " " else 0.555 if ch.isdigit() else 0.29 if ch == "I" else 0.62
        else:
            t += 1.0
    return t


def fit(s, size, maxw, what=""):
    w = em(s) * size
    if w > maxw + 0.5:
        raise SystemExit("text too wide (%.0f > %d): %s %r" % (w, maxw, what, s))
    return w


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def f1(v):
    return ("%.1f" % v).rstrip("0").rstrip(".")


# ---- svg primitives ------------------------------------------------------------------------------------------


def T(x, y, s, size, fill=CHAR, weight=400, anchor="start", halo=None, extra=""):
    h = ""
    if halo:
        h = ' stroke="%s" stroke-width="%s" stroke-linejoin="round" paint-order="stroke"' % (halo, f1(size * 0.28))
    return ('<text x="%s" y="%s" font-size="%s" font-weight="%d" fill="%s" text-anchor="%s"%s%s>%s</text>'
            % (f1(x), f1(y), f1(size), weight, fill, anchor, h, extra, esc(s)))


def Tc(cx, cy, s, size, fill=CHAR, weight=400, halo=None):
    """Text centred (horizontally and optically vertically) on (cx, cy)."""
    return T(cx, cy + 0.36 * size, s, size, fill, weight, "middle", halo)


def R(x, y, w, h, fill="none", rx=0, stroke=None, sw=0, dash=None, extra=""):
    s = ' stroke="%s" stroke-width="%s"' % (stroke, f1(sw)) if stroke else ""
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s"%s%s%s/>'
            % (f1(x), f1(y), f1(w), f1(h), f1(rx), fill, s, d, extra))


def C(cx, cy, r, fill="none", stroke=None, sw=0):
    s = ' stroke="%s" stroke-width="%s"' % (stroke, f1(sw)) if stroke else ""
    return '<circle cx="%s" cy="%s" r="%s" fill="%s"%s/>' % (f1(cx), f1(cy), f1(r), fill, s)


def L(x1, y1, x2, y2, stroke, sw, dash=None, cap="butt"):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" stroke-linecap="%s"%s/>'
            % (f1(x1), f1(y1), f1(x2), f1(y2), stroke, f1(sw), cap, d))


def P(points, fill="none", stroke=None, sw=0, join="round"):
    pts = " ".join("%s,%s" % (f1(a), f1(b)) for a, b in points)
    s = ' stroke="%s" stroke-width="%s" stroke-linejoin="%s"' % (stroke, f1(sw), join) if stroke else ""
    return '<polygon points="%s" fill="%s"%s/>' % (pts, fill, s)


def PL(points, stroke, sw, dash=None):
    pts = " ".join("%s,%s" % (f1(a), f1(b)) for a, b in points)
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<polyline points="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linejoin="round" '
            'stroke-linecap="round"%s/>' % (pts, stroke, f1(sw), d))


def arrow2(a, b, color, sw, head=30):
    """Double-headed dimension arrow from a to b (heads drawn as polygons)."""
    ax, ay = a
    bx, by = b
    ln = math.hypot(bx - ax, by - ay)
    ux, uy = (bx - ax) / ln, (by - ay) / ln
    nx, ny = -uy, ux
    hw = head * 0.55

    def tri(tip, sgn):
        tx, ty = tip
        bxx, byy = tx + sgn * ux * head, ty + sgn * uy * head
        return [(tx, ty), (bxx + nx * hw, byy + ny * hw), (bxx - nx * hw, byy - ny * hw)]
    p1 = (ax + ux * head * 0.8, ay + uy * head * 0.8)
    p2 = (bx - ux * head * 0.8, by - uy * head * 0.8)
    return (L(p1[0], p1[1], p2[0], p2[1], color, sw) + P(tri(a, 1), color) + P(tri(b, -1), color))


def dim(a, b, off, color, sw, label=None, size=54, halo=CREAM, head=30, lab_shift=(0, 0), ext=True):
    """Dimension line for the span a-b, drawn at offset `off` from it, with extension lines."""
    ox, oy = off
    a2, b2 = (a[0] + ox, a[1] + oy), (b[0] + ox, b[1] + oy)
    out = []
    if ext:
        k = 1.12
        out.append(L(a[0], a[1], a[0] + ox * k, a[1] + oy * k, color, max(2, sw * 0.4)))
        out.append(L(b[0], b[1], b[0] + ox * k, b[1] + oy * k, color, max(2, sw * 0.4)))
    out.append(arrow2(a2, b2, color, sw, head))
    if label:
        mx, my = (a2[0] + b2[0]) / 2 + lab_shift[0], (a2[1] + b2[1]) / 2 + lab_shift[1]
        out.append(Tc(mx, my, label, size, color, 700, halo))
    return "".join(out)


def tick(cx, cy, s, color=CHAR, sw=9):
    """Check mark centred on (cx, cy), drawn as a path (no glyph)."""
    return PL([(cx - 0.30 * s, cy + 0.02 * s), (cx - 0.08 * s, cy + 0.26 * s), (cx + 0.34 * s, cy - 0.26 * s)], color, sw)


# ---- badge, tracker, slot ------------------------------------------------------------------------------------


def badge(kind):
    txt = BADGE_CHAR if kind == "char" else BADGE_DIAG
    size, pad, h = 68, 44, 104
    w = round(em(txt) * size * 1.02 + 2 * pad)
    return ('<g id="badge">' + R(BADGE_X, BADGE_Y, w, h, CHAR, rx=h / 2)
            + Tc(BADGE_X + w / 2, BADGE_Y + h / 2, txt, size, GROUND, 500) + '</g>')


def tracker(x, y, current):
    d, gap = 60, 16
    out = []
    for i in range(5):
        n = i + 1
        cx, cy = x + d / 2 + i * (d + gap), y + d / 2
        if n == current:
            out.append(C(cx, cy, d / 2, WALNUT))
            out.append(Tc(cx, cy, str(n), 34, GROUND, 700))
        else:
            out.append(C(cx, cy, d / 2, OAT))
            out.append(Tc(cx, cy, str(n), 34, WALNUT, 500))
    return '<g id="tracker">' + "".join(out) + "</g>"


def numeral(cx, cy, n, r, fill=WALNUT, tc=GROUND, size=None):
    return C(cx, cy, r, fill) + Tc(cx, cy, str(n), size or r * 1.2, tc, 700)


def slot(spec, preview):
    """The character slot: empty and transparent in the final layer, neutral rectangle + label in the preview."""
    x, y, w, h, r = spec["x"], spec["y"], spec["w"], spec["h"], spec.get("r", 24)
    ring = R(x - 6, y - 6, w + 12, h + 12, "none", rx=r + 6, stroke=WALNUT, sw=12)
    attrs = ('data-asset="%s" data-golden-set="%s" data-x="%d" data-y="%d" data-w="%d" data-h="%d" data-rx="%d" '
             'data-aspect="%s"' % (spec["asset"], spec["golden"], x, y, w, h, r, spec["aspect"]))
    comment = ("<!-- CHARACTER SLOT %s (golden set %s, %s, %dx%d at %d,%d): PENDING. The photoreal image does not exist yet. "
               "Composite the approved still into this rectangle, clipped to rx=%d; the frame ring is drawn outside it. -->"
               % (spec["asset"], spec["golden"], spec["aspect"], w, h, x, y, r))
    if not preview:
        inner = R(x, y, w, h, "none", rx=r, extra=' fill-opacity="0"')
        return comment + ring + '<g id="character-slot" %s>%s</g>' % (attrs, inner)
    fs = max(28, min(34, round(w / 9)))
    lines = ["CHARACTER", "PANEL:", "PENDING"]
    cy = y + h / 2
    labels = "".join(T(x + w / 2, cy + (i - 1) * fs * 1.45 + 0.35 * fs, s, fs, PREVIEW_GREY, 500, "middle")
                     for i, s in enumerate(lines))
    return comment + ring + '<g id="character-slot" %s>%s%s</g>' % (attrs, R(x, y, w, h, OAT, rx=r), labels)


def body_lines(lines, size=72, y1=830, lh=100, x=MX0, fill=CHAR, weight=400, anchor="start"):
    out = []
    for i, s in enumerate(lines):
        fit(s, size, MX1 - MX0, "body")
        out.append(T(x, y1 + i * lh, s, size, fill, weight, anchor))
    return "".join(out)


def footer_note():
    fit(NOTE, 42, 840, "note")
    return T(MX0, 1548, NOTE, 42, WALNUT, 500)


CARD = dict(x=90, y=1000, w=840, h=500)


def card_open():
    return ('<g id="diagram"><rect x="%d" y="%d" width="%d" height="%d" rx="40" fill="%s"/><g transform="translate(%d %d)">'
            % (CARD["x"], CARD["y"], CARD["w"], CARD["h"], CREAM, CARD["x"], CARD["y"]))


CARD_CLOSE = "</g></g>"

SLOT_HEAD = dict(asset="A5", golden="E07", x=658, y=452, w=260, h=260, r=24, aspect="1:1")   # frame ring ends at x=930


# ---- box drawings ---------------------------------------------------------------------------------------------
# Oblique (cabinet) projection used for the Reel cards 1 and 3. Card-local coordinates.
FF = dict(x0=100, y0=200, w=330, h=190)   # front face
DEP = (140, -95)                          # depth vector (up and to the right)


def ob_box():
    x0, y0, w, h = FF["x0"], FF["y0"], FF["w"], FF["h"]
    dx, dy = DEP
    front = [(x0, y0), (x0 + w, y0), (x0 + w, y0 + h), (x0, y0 + h)]
    top = [(x0, y0), (x0 + w, y0), (x0 + w + dx, y0 + dy), (x0 + dx, y0 + dy)]
    right = [(x0 + w, y0), (x0 + w + dx, y0 + dy), (x0 + w + dx, y0 + h + dy), (x0 + w, y0 + h)]
    return (P(right, DEEP, CHAR, 4) + P(top, PUTTY, CHAR, 4) + P(front, WALNUT, CHAR, 4))


def ob_room():
    """Wall with ceiling strip, baseboard line and a plain sliding window, behind the box."""
    out = [R(170, 40, 655, 255, GROUND)]
    out.append(R(170, 40, 655, 16, PUTTY))                       # ceiling strip
    out.append(L(170, 295, 825, 295, CHAR, 4))                   # wall / floor line
    wx, wy, ww, wh = 500, 125, 190, 125
    out.append(R(wx, wy, ww, wh, CREAM, stroke=CHAR, sw=4))
    out.append(L(wx + ww / 2, wy, wx + ww / 2, wy + wh, CHAR, 4))
    out.append(R(wx - 14, wy + wh, ww + 28, 14, PUTTY, stroke=CHAR, sw=3))   # sill ledge
    for gx in (wx + ww * 0.25, wx + ww * 0.75):
        out.append(L(gx, wy + 6, gx, wy + wh - 6, PUTTY, 3))
    return "".join(out)


def scene_width():
    out = [ob_room(), ob_box()]
    x0, y0, w, h = FF["x0"], FF["y0"], FF["w"], FF["h"]
    out.append(dim((x0, y0 + h), (x0 + w, y0 + h), (0, 56), CHAR, 9, STRINGS["1"][0], 56, CREAM))
    out.append(T(184, 96, "牆", 46, WALNUT, 500))
    return "".join(out)


def scene_depth():
    """Top-down comparison: the same room depth, a shallower and a deeper cabinet, the walkway left in front of each."""
    out = [R(100, 30, 640, 34, PUTTY, stroke=CHAR, sw=4), R(100, 440, 640, 34, PUTTY, stroke=CHAR, sw=4)]
    for cx, depth in ((200, 120), (520, 190)):
        out.append(R(cx, 64, 160, depth, WALNUT, stroke=CHAR, sw=4))
        out.append(dim((cx, 64), (cx, 64 + depth), (-44, 0), CHAR, 9, STRINGS["2"][0], 56, CREAM, lab_shift=(-52, 0)))
        mid = cx + 80
        out.append(arrow2((mid, 64 + depth + 14), (mid, 426), WALNUT, 7, 28))
        out.append(T(mid + 22, (64 + depth + 440) / 2 + 0.36 * 50, "走道", 50, WALNUT, 700, extra=""))
    return "".join(out)


def scene_height():
    out = [ob_room(), ob_box()]
    x0, y0, w, h = FF["x0"], FF["y0"], FF["w"], FF["h"]
    out.append(dim((x0, y0), (x0, y0 + h), (-60, 0), CHAR, 9, STRINGS["3"][0], 56, CREAM))
    out.append(T(815, 100, "天花板", 46, WALNUT, 500, "end"))
    out.append(T(718, 262, "窗台", 46, WALNUT, 500, "start"))
    return "".join(out)


OBLIQUE = {1: scene_width, 2: scene_depth, 3: scene_height}


# Isometric box (Short scene 2). Card-local coordinates; steps reveal the arrows one after another.
def iso_scene(step):
    ux, uy = math.cos(math.radians(30)), -math.sin(math.radians(30))     # width axis (up and to the right)
    vx, vy = -ux, uy                                                      # depth axis (up and to the left)
    Wd, Dp, Ht = 240, 190, 170
    ox, oy = 430, 410
    O = (ox, oy)

    def at(a, b, c):
        return (ox + a * ux * Wd + b * vx * Dp, oy + a * uy * Wd + b * vy * Dp - c * Ht)
    p000, p100, p010, p110 = at(0, 0, 0), at(1, 0, 0), at(0, 1, 0), at(1, 1, 0)
    p001, p101, p011, p111 = at(0, 0, 1), at(1, 0, 1), at(0, 1, 1), at(1, 1, 1)
    out = []
    # ground footprint (flat, a little larger than the box)
    g = 36
    fp = [(p000[0], p000[1] + g * 0.55), (p100[0] + g, p100[1] + g * 0.25), (p110[0], p110[1] - g * 0.2),
          (p010[0] - g, p010[1] + g * 0.25)]
    out.append(P(fp, OAT))
    out.append(P([p000, p100, p101, p001], WALNUT, CHAR, 4))     # right face (width)
    out.append(P([p000, p010, p011, p001], DEEP, CHAR, 4))       # left face (depth)
    out.append(P([p001, p101, p111, p011], PUTTY, CHAR, 4))      # top
    labels = {1: "寬", 2: "深", 3: "高"}
    # width: along the bottom-right edge, offset toward the viewer (down and to the right)
    if step >= 1:
        out.append(dim(p000, p100, (0.5 * 62, 0.866 * 62), CHAR, 9, labels[1], 56, CREAM, lab_shift=(24, 18)))
    if step >= 2:
        out.append(dim(p000, p010, (-0.5 * 62, 0.866 * 62), CHAR, 9, labels[2], 56, CREAM, lab_shift=(-24, 18)))
    if step >= 3:
        out.append(dim(p010, p011, (-64, 0), CHAR, 9, labels[3], 56, CREAM, lab_shift=(-4, 0)))
    return "".join(out)


def scene_door():
    out = ['<g transform="translate(70 24)">']
    out.append(R(130, 30, 570, 34, PUTTY, stroke=CHAR, sw=4))                  # wall (top-down)
    cx0, cy0, cw, chh = 190, 64, 360, 130
    out.append(R(cx0, cy0, cw, chh, WALNUT, stroke=CHAR, sw=4))              # cabinet, top-down
    hx, hy = cx0 + cw, cy0 + chh                                              # hinge: front-right corner
    leaf = cw / 2
    out.append(L(cx0 + cw / 2, hy, cx0 + cw / 2, cy0, CHAR, 3, "6 6"))         # split between the two leaves
    # swept area of the right leaf opening to 90 degrees
    sector = "M%s,%s L%s,%s A%s,%s 0 0 0 %s,%s Z" % (f1(hx), f1(hy), f1(hx - leaf), f1(hy), f1(leaf), f1(leaf), f1(hx), f1(hy + leaf))
    out.append('<path d="%s" fill="%s" stroke="%s" stroke-width="5" stroke-dasharray="14 10" stroke-linejoin="round"/>'
               % (sector, PUTTY, CHAR))
    out.append(L(hx - leaf, hy, hx, hy, CHAR, 6, "10 8"))                      # leaf, closed position
    out.append(L(hx, hy, hx, hy + leaf, WALNUT, 18, cap="round"))             # leaf, open to 90 degrees
    out.append(C(hx, hy, 11, CHAR))
    out.append(T(hx + 38, hy + leaf * 0.62, "門板", 56, WALNUT, 700))
    out.append("</g>")
    return "".join(out)


def scene_route():
    out = []
    y1, y2 = 160, 380
    xs = [210, 390, 570, 750]
    out.append(PL([(116, y1), (750, y1), (750, y2), (540, y2)], WALNUT, 16))
    out.append(P([(500, y2), (546, y2 - 24), (546, y2 + 24)], WALNUT))         # arrow head into the target
    out.append(R(40, y1 - 38, 76, 76, WALNUT, rx=10, stroke=CHAR, sw=4))      # the cabinet that has to travel
    out.append(R(414, y2 - 38, 76, 76, "none", rx=10, stroke=WALNUT, sw=6, dash="12 10"))   # where it is going
    for x, lab in zip(xs, ["大門", "走廊", "電梯", "轉角"]):
        out.append(C(x, y1, 34, CREAM, CHAR, 8))
        out.append(C(x, y1, 11, CHAR))
        out.append(Tc(x, y1 - 82, lab, 54, CHAR, 700))
    return "".join(out)


# ---- frame builders ------------------------------------------------------------------------------------------


def head_row(step, heading):
    r = 48
    cy = 500
    fit(heading, 100, 400, "heading")
    return numeral(MX0 + r, cy, step, r, size=60) + T(MX0 + 2 * r + 28, cy + 36, heading, 100, CHAR, 700)


def build_card(step, preview, scene_svg, tracker_current=None):
    heading, lines = STRINGS[str(step)]
    parts = [head_row(step, heading), tracker(MX0, 604, tracker_current or step), slot(SLOT_HEAD, preview),
             body_lines(lines), card_open(), scene_svg, CARD_CLOSE, footer_note()]
    return "".join(parts)


def build_hook(variant, preview):
    lines = STRINGS["reel_hook" if variant == "reel" else "short_hook"]
    out = [T(MX0, 560, lines[0], 112, CHAR, 700), T(MX0, 700, lines[1], 112, CHAR, 700)]
    for s in lines:
        fit(s, 112, 840, "hook")
    spec = dict(asset="A1", golden="R01", x=102, y=800, w=460, h=575, r=28, aspect="4:5")   # frame ring starts at x=90
    out.append(slot(spec, preview))
    cx = 654
    ys = [1087 + (i - 2) * 118 for i in range(5)]
    out.append(L(cx, ys[0], cx, ys[-1], OAT, 10, cap="round"))
    for i, (y, hd) in enumerate(zip(ys, HEADINGS)):
        out.append(numeral(cx, y, i + 1, 38, size=46))
        fit(hd, 56, MX1 - 706, "hook list")
        out.append(T(706, y + 0.36 * 56, hd, 56, CHAR, 500))
    return "".join(out), spec


def build_intro(preview):
    spec = dict(asset="A5", golden="E07", x=180, y=470, w=720, h=720, r=32, aspect="1:1")
    fit(STRINGS["intro"], 68, 840, "intro")
    return slot(spec, preview) + T(540, 1330, STRINGS["intro"], 68, CHAR, 700, "middle"), spec


def build_closing(preview):
    lines = STRINGS["closing"]
    out = [T(MX0, 570, lines[0], 96, CHAR, 700), T(MX0, 690, lines[1], 96, CHAR, 700)]
    for s in lines:
        fit(s, 96, 840, "closing")
    y0 = 790
    for i, hd in enumerate(HEADINGS):
        cy = y0 + i * 104 + 40
        out.append(R(MX0, cy - 38, 76, 76, SAGE, rx=16, stroke=CHAR, sw=4))
        out.append(tick(MX0 + 38, cy + 2, 62, CHAR, 9))
        out.append(T(MX0 + 118, cy + 0.36 * 64, str(i + 1), 64, WALNUT, 700))
        out.append(T(MX0 + 190, cy + 0.36 * 64, hd, 64, CHAR, 500))
        if i < 4:
            out.append(L(MX0, cy + 52, MX1, cy + 52, OAT, 3))
    bw = 8 * 72 + 90
    bx = (W - bw) / 2
    out.append(R(bx, 1380, bw, 126, GROUND, rx=30, stroke=WALNUT, sw=6))
    out.append(Tc(W / 2, 1380 + 63, NOTE, 72, WALNUT, 700))
    return "".join(out), None


def build_end(variant, preview):
    spec = dict(asset="A4", golden="E10", x=300, y=470, w=480, h=480, r=28, aspect="1:1")
    cta = STRINGS["end_reel_cta" if variant == "reel" else "end_short_cta"]
    out = [slot(spec, preview)]
    for i, s in enumerate(cta):
        fit(s, 92, 840, "cta")
        out.append(T(W / 2, 1100 + i * 116, s, 92, CHAR, 700, "middle"))
    a = STRINGS["end_a"]
    out.append(L(MX0, 1336, MX1, 1336, OAT, 4))
    out.append(T(W / 2, 1408, a[:a.index("，") + 1], 52, WALNUT, 500, "middle"))
    out.append(T(W / 2, 1480, a[a.index("，") + 1:], 52, WALNUT, 500, "middle"))
    fit(a[:a.index("，") + 1], 52, 840, "end a1")
    return "".join(out), spec


def build_short_head3(step, preview):
    """Short scene 2: three stacked chips (1 寬, 2 深, 3 高) that light up with the arrows."""
    rows = [("寬", 1), ("深", 2), ("高", 3)]
    out = []
    for i, (hd, n) in enumerate(rows):
        cy = 490 + i * 88
        on = n <= step
        r = 34
        out.append(numeral(MX0 + r, cy, n, r, WALNUT if on else OAT, GROUND if on else WALNUT, 42))
        out.append(T(MX0 + 2 * r + 26, cy + 0.36 * 76, hd, 76, CHAR if on else PUTTY, 700))
    out.append(slot(SLOT_HEAD, preview))
    lines = STRINGS["short_three"]
    out.append(body_lines(lines))
    out.append(card_open() + iso_scene(step) + CARD_CLOSE)
    out.append(footer_note())
    return "".join(out), SLOT_HEAD


# ---- frame table ---------------------------------------------------------------------------------------------


def make_frames():
    F = []

    def add(fid, post, scene, media_index, kind, builder, desc):
        F.append(dict(id=fid, post=post, scene=scene, media_index=media_index, kind=kind, builder=builder, desc=desc))
    R_, S_ = "2026-11-19_01", "2026-11-20_01"

    def card_builder(step):
        return lambda pv: (build_card(step, pv, OBLIQUE[step]()), SLOT_HEAD)

    def door(pv):
        return build_card(4, pv, scene_door()), SLOT_HEAD

    def route(pv):
        return build_card(5, pv, scene_route()), SLOT_HEAD
    add("reel_s01_hook", R_, 1, 3, "char", lambda pv: build_hook("reel", pv), "hook card, R01 slot")
    add("reel_s02_intro", R_, 2, 4, "char", build_intro, "identity line, E07 slot")
    add("reel_s03_width", R_, 3, 5, "char", card_builder(1), "check 1 width")
    add("reel_s04_depth", R_, 4, 6, "char", card_builder(2), "check 2 depth")
    add("reel_s05_height", R_, 5, 7, "char", card_builder(3), "check 3 height")
    add("reel_s06_door", R_, 6, 8, "char", door, "check 4 door leaf")
    add("reel_s07_route", R_, 7, 9, "char", route, "check 5 moving route")
    add("reel_s08_closing", R_, 8, 10, "diagram", build_closing, "closing recap, no character")
    add("reel_s09_end", R_, 9, 11, "char", lambda pv: build_end("reel", pv), "end card, E10 slot")
    add("short_s01_hook", S_, 1, 3, "char", lambda pv: build_hook("short", pv), "hook card, R01 slot")
    add("short_s02_iso_1_width", S_, 2, None, "char", lambda pv: build_short_head3(1, pv), "isometric box, step 1 of 3")
    add("short_s02_iso_2_depth", S_, 2, None, "char", lambda pv: build_short_head3(2, pv), "isometric box, step 2 of 3")
    add("short_s02_iso_3_height", S_, 2, 4, "char", lambda pv: build_short_head3(3, pv), "isometric box, step 3 of 3 (all arrows)")
    add("short_s03_door", S_, 3, 5, "char", door, "check 4 door leaf (same as reel_s06)")
    add("short_s04_route", S_, 4, 6, "char", route, "check 5 moving route (same as reel_s07)")
    add("short_s05_closing", S_, 5, 7, "diagram", build_closing, "closing recap (same as reel_s08)")
    add("short_s06_end", S_, 6, 8, "char", lambda pv: build_end("short", pv), "end card, E10 slot")
    return F


def assemble(frame, preview):
    body, spec = frame["builder"](preview)
    kind = frame["kind"]
    if spec is None:
        kind = "diagram"
    doc = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<!-- %s %s: DRAFT, code-drawn (no image model), not approved. Frame %s (%s). %s. Do not edit by hand: '
           'edit %s and re-run. -->' % (SCRIPT_REL, VERSION, frame["id"], frame["post"],
                                       "PREVIEW variant: the character slot is a placeholder" if preview else
                                       "FINAL layer: the character slot is empty and transparent", SCRIPT_REL),
           '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" lang="zh-Hant-TW" '
           'xml:lang="zh-Hant-TW" font-family="%s">' % (W, H, W, H, FONT),
           '<title>方寸 先量再買 %s</title>' % frame["id"],
           '<rect id="ground" width="%d" height="%d" fill="%s"/>' % (W, H, GROUND),
           body, badge("char" if kind == "char" else "diagram"), "</svg>"]
    svg = "\n".join(doc) + "\n"
    ET.fromstring(svg.split("?>", 1)[1])      # well-formedness check
    return svg, spec, kind


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--svg-only", action="store_true", help="write SVGs and frames.json, do not render PNGs")
    ap.add_argument("--only", action="append", help="frame id to build (repeatable)")
    ap.add_argument("--keep-preview-svg", action="store_true", help="also keep <id>_preview.svg next to the outputs")
    ap.add_argument("--out", default=OUT_DIR, help="output folder (default assets/fangcun/diagrams/C)")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    manifest = []
    for fr in make_frames():
        if a.only and fr["id"] not in a.only:
            continue
        final, spec, kind = assemble(fr, False)
        prev, _, _ = assemble(fr, True)
        svg_path = os.path.join(a.out, fr["id"] + ".svg")
        png_path = os.path.join(a.out, fr["id"] + "_preview.png")
        with open(svg_path, "w", encoding="utf-8") as fh:
            fh.write(final)
        if a.keep_preview_svg:
            with open(os.path.join(a.out, fr["id"] + "_preview.svg"), "w", encoding="utf-8") as fh:
                fh.write(prev)
        if not a.svg_only:
            with tempfile.TemporaryDirectory() as td:
                tmp = os.path.join(td, fr["id"] + ".svg")
                with open(tmp, "w", encoding="utf-8") as fh:
                    fh.write(prev)
                subprocess.run([sys.executable, RENDER, tmp, png_path, str(W), str(H), "--bg", GROUND], check=True)
        manifest.append(dict(id=fr["id"], post=fr["post"], scene=fr["scene"], media_index=fr["media_index"],
                             badge=BADGE_CHAR if kind == "char" else BADGE_DIAG,
                             svg="%s/%s.svg" % (OUT_REL, fr["id"]), preview_png="%s/%s_preview.png" % (OUT_REL, fr["id"]),
                             slot=({k: spec[k] for k in ("asset", "golden", "x", "y", "w", "h", "r", "aspect")} if spec else None),
                             note=fr["desc"]))
        print("ok", fr["id"])
    if not a.only:
        with open(os.path.join(a.out, "frames.json"), "w", encoding="utf-8") as fh:
            json.dump(dict(generator=SCRIPT_REL, version=VERSION, canvas=[W, H], frames=manifest), fh, ensure_ascii=False, indent=1)
            fh.write("\n")


if __name__ == "__main__":
    main()
