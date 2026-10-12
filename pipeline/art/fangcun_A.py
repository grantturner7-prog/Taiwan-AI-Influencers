#!/usr/bin/env python3
"""fangcun_A.py - 方寸 master A 「尺寸算給你看」 (calendar M1 · 算給你看 #01), v0.1 DRAFT.

Draws the diagram, lesson-graphic and card layer of two posts as SVG (standard library only) and renders the
previews to PNG with pipeline/art/render.py (headless Chromium + Noto Sans TC; see INSTALL_FONT.md):

    P01  fangcun-2026-11-16-01  Instagram carousel   9 slides   1080 x 1350 (4:5)
    P02  fangcun-2026-11-17-01  YouTube Short        8 scenes   1080 x 1920 (9:16)

No image model is used: every shape, number, Chinese string and badge is code. Decision D3 (DECISIONS.md 2026-10-12):
Claude draws the diagram layer; the operator and the wife approve every asset; Claude cannot edit video, so the user
assembles the Short from the exported scene frames.

The three-number size arithmetic (post hook and caption: 床、衣櫃、門板 -> 走道還剩多少), all example values 示意數字:
    (1) room width 300   (2) bed width 150 + wardrobe depth 55   (3) wardrobe door leaf 60
    walkway = 300 - 150 - 55 = 95;   with the door open = 95 - 60 = 35;   what-if bed 120: 300 - 120 - 55 = 125, 125 - 60 = 65.
Every sum is asserted in check_arithmetic() before anything is drawn. Room 0 plan (series.md section 2, calendar 7.2):
room 300 x 400, bed 150 x 190 against the left wall, wardrobe 120 x 55 against the right wall, 60 leaf, window with a
grille on the far wall, split air conditioner on the right wall, tile floor, door on the near wall. The plan is general
geometry only: no product shape, no brand, no address, no 坪 conversion (P05 is blocked on the 坪 source).

Per frame, two outputs in assets/fangcun/diagrams/A/ :
    <id>.svg          FINAL LAYER. The photoreal character does not exist yet, so the picture slot is an empty,
                      transparent <g id="character-slot"> (geometry in its data-* attributes). Composite the approved
                      golden-set still into that rectangle later (clip to rx); the frame ring around it is drawn OUTSIDE
                      the slot and the post-added arrow (slide 2) is drawn after it, so nothing here needs to change.
    <id>_preview.png  PROOF RENDER. The same SVG with the slot filled by a neutral rounded rectangle and the small grey
                      English text CHARACTER PANEL: PENDING. Never publish a preview. Frames with no character (slide 8,
                      Short scene 7) have no slot, so their _preview.png is pixel-identical to the final.
frames.json lists every frame, its post, its media index in post.json, its badge and its slot rectangle.

Rules baked in (calendar-30d.md 7.2, photoreal-addendum 8.2, qa-checklist D3/D4/S2/T9):
  * Badge: solid charcoal pill, off-white text, text height 3.5% of the canvas height or more, same place on every frame
    of a post (persistent). Wording 「AI 生成｜虛擬角色」 on frames that carry the character slot, 「AI 生成｜示意圖」 on
    pure-diagram frames. Instagram 4:5: x = 90 (8.3% of the width), y = 149 (11% of the height), text 48 px (3.6%).
    Short 9:16: x = 90, y = 300 (the studio's 9:16 safe zone, same as fangcun_C.py), text 68 px (3.5%). A centred 1:1
    crop of a 4:5 slide keeps y 135..1215, so the badge survives it.
  * Short content stays inside x 90..930 and y 300..1560 (platform buttons, caption and progress bar; safe zones of
    Reels and Shorts are unverified, HUMAN_TODO 25). Instagram content stays inside x 90..990.
  * Palette only: ground #F5F0E6, oat #E4D9C3, putty #CFC6B4, walnut #6E5440, deep walnut #5C4636, belt cream #EFE6CF,
    charcoal #3B3631; walnut tint #BBA48F is the bible's diagram tint (4.5). Sage #A9B5A0 is a thin accent only. No red,
    no saturated blue, green, teal or yellow. The one exception is the grey of the preview-only slot label.
  * Text is Noto Sans TC, lang zh-Hant-TW, no fallback font. Smallest text on any frame is 32 px (28 px effective floor).
  * Every Chinese string is an approved string of the post (calendar-30d.md P01 / P02 and the queue post.json) or a word
    taken from one of them; EXTRA lists the few labels added to the plan (see its comment).

Usage:
    python3 pipeline/art/fangcun_A.py                    # write SVGs, render previews, write frames.json
    python3 pipeline/art/fangcun_A.py --svg-only         # SVGs and frames.json only (no Chromium needed)
    python3 pipeline/art/fangcun_A.py --only P01_s04_room --keep-preview-svg
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
OUT_REL = "assets/fangcun/diagrams/A"
OUT_DIR = os.path.join(ROOT, *OUT_REL.split("/"))
RENDER = os.path.join(HERE, "render.py")
SCRIPT_REL = "pipeline/art/fangcun_A.py"
VERSION = "v0.1"
FONT = "'Noto Sans TC'"

# ---- palette ----------------------------------------------------------------------------------------------------
GROUND, OAT, PUTTY, WALNUT = "#F5F0E6", "#E4D9C3", "#CFC6B4", "#6E5440"
DEEP, CREAM, SAGE, CHAR = "#5C4636", "#EFE6CF", "#A9B5A0", "#3B3631"
WALNUT_T = "#BBA48F"            # walnut tint, bible 4.5 diagram fill
PREVIEW_GREY = "#7A756D"        # preview-only label (the brief asks for small grey English text)

BADGE_CHAR = "AI 生成｜虛擬角色"
BADGE_DIAG = "AI 生成｜示意圖"
NOTE = "請以現場丈量為準"
TAG = "示意數字"

# Labels added to the plan that are not whole lines of the approved script (each is a word from the kit or the bible 4.9
# settings list; the wife reads them): window and grille, split air conditioner, door, bed, wardrobe, 100 cm scale bar
# label, series chip, the three 'what to compute' chips on the cover (same strings as slide 4's key).
EXTRA = ["窗＋鐵窗", "冷氣", "門", "床", "衣櫃", "100 公分", "算給你看 #01", "床寬 150 公分", "床寬 120 公分",
         "第一步", "第二步"]

# ---- the arithmetic (all example values, tagged 示意數字 on screen) --------------------------------------------------
ROOM_W, ROOM_D = 300, 400
BED_W, BED_L = 150, 190
WARD_W, WARD_D = 120, 55
LEAF = 60
BED_W2 = 120


def check_arithmetic():
    assert ROOM_W - BED_W - WARD_D == 95
    assert 95 - LEAF == 35
    assert ROOM_W - BED_W2 - WARD_D == 125
    assert 125 - LEAF == 65
    assert BED_W + 95 + WARD_D == ROOM_W
    assert BED_W + 35 + LEAF + WARD_D == ROOM_W
    assert BED_W2 + 125 + WARD_D == ROOM_W
    assert BED_W2 + 65 + LEAF + WARD_D == ROOM_W


# ---- text width estimate (em) for fit assertions; measured with Noto Sans TC ----------------------------------------
_ASCII = {" ": 0.224, "A": 0.608, "I": 0.293, "#": 0.6, ":": 0.278, ".": 0.278, ",": 0.278, "(": 0.338, ")": 0.338,
          "-": 0.347, "0": 0.555, "1": 0.555, "2": 0.555, "3": 0.555, "4": 0.555, "5": 0.555, "6": 0.555, "7": 0.555,
          "8": 0.555, "9": 0.555}


def em(s, weight=400):
    t = 0.0
    k = 1.06 if weight >= 700 else 1.0
    for ch in s:
        o = ord(ch)
        if ch == "−":
            t += 0.56 * k
        elif o < 0x80:
            t += _ASCII.get(ch, 0.62) * k
        else:
            t += 1.0
    return t


def tw(s, size, weight=400):
    return em(s, weight) * size


def fit(s, size, maxw, weight=400, what=""):
    w = tw(s, size, weight)
    if w > maxw + 0.5:
        raise SystemExit("text too wide (%.0f > %d): %s %r" % (w, maxw, what, s))
    return w


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def f1(v):
    return ("%.1f" % v).rstrip("0").rstrip(".")


# ---- svg primitives ---------------------------------------------------------------------------------------------------

MINSIZE = 32      # smallest text on a frame (the preview-only slot label is exempt)


def T(x, y, s, size, fill=CHAR, weight=500, anchor="start", maxw=None, halo=None):
    if size < MINSIZE:
        raise SystemExit("text smaller than %d px: %r at %s" % (MINSIZE, s, size))
    if maxw:
        fit(s, size, maxw, weight, "T")
    h = ""
    if halo:
        h = ' stroke="%s" stroke-width="%s" stroke-linejoin="round" paint-order="stroke"' % (halo, f1(size * 0.2))
    if anchor == "start" and s.startswith("（"):
        x -= 0.5 * size           # optical alignment: the full-width opening bracket sits in the right half of its box
    return ('<text x="%s" y="%s" font-size="%s" font-weight="%d" fill="%s" text-anchor="%s"%s>%s</text>'
            % (f1(x), f1(y), f1(size), weight, fill, anchor, h, esc(s)))


def Tc(cx, cy, s, size, fill=CHAR, weight=500, halo=None):
    """Text centred (horizontally and optically vertically) on (cx, cy)."""
    return T(cx, cy + 0.36 * size, s, size, fill, weight, "middle", None, halo)


def TR(x, y, parts, size, anchor="start", maxw=None):
    """Rich line: parts = [(text, dict(weight=, fill=)), ...]; one <text> with tspans."""
    if size < MINSIZE:
        raise SystemExit("text smaller than %d px: %r" % (MINSIZE, parts))
    total = sum(tw(p[0], size, (p[1] or {}).get("weight", 500)) for p in parts)
    if maxw and total > maxw + 0.5:
        raise SystemExit("rich text too wide (%.0f > %d): %r" % (total, maxw, parts))
    spans = "".join('<tspan font-weight="%d" fill="%s">%s</tspan>' % ((p[1] or {}).get("weight", 500),
                                                                       (p[1] or {}).get("fill", CHAR), esc(p[0]))
                    for p in parts)
    return '<text x="%s" y="%s" font-size="%s" text-anchor="%s">%s</text>' % (f1(x), f1(y), f1(size), anchor, spans)


def richw(parts, size):
    return sum(tw(p[0], size, (p[1] or {}).get("weight", 500)) for p in parts)


def nums(s, base=500, nweight=700, nfill=None, bfill=CHAR):
    """Split a string into digit runs (bold, optional fill) and the rest."""
    parts, cur, isd = [], "", False
    for ch in s:
        d = ch.isdigit()
        if cur and d != isd:
            parts.append(cur)
            cur = ""
        cur += ch
        isd = d
    if cur:
        parts.append(cur)
    out = []
    for p in parts:
        if p[0].isdigit():
            out.append((p, dict(weight=nweight, fill=nfill or bfill)))
        else:
            out.append((p, dict(weight=base, fill=bfill)))
    return out


def R(x, y, w, h, fill="none", rx=0, stroke=None, sw=0, dash=None, extra=""):
    a = '<rect x="%s" y="%s" width="%s" height="%s"' % (f1(x), f1(y), f1(w), f1(h))
    if rx:
        a += ' rx="%s"' % f1(rx)
    a += ' fill="%s"' % fill
    if stroke:
        a += ' stroke="%s" stroke-width="%s"' % (stroke, f1(sw))
    if dash:
        a += ' stroke-dasharray="%s"' % dash
    return a + extra + "/>"


def C(cx, cy, r, fill="none", stroke=None, sw=0):
    a = '<circle cx="%s" cy="%s" r="%s" fill="%s"' % (f1(cx), f1(cy), f1(r), fill)
    if stroke:
        a += ' stroke="%s" stroke-width="%s"' % (stroke, f1(sw))
    return a + "/>"


def L(x1, y1, x2, y2, stroke=CHAR, sw=2.5, dash=None, cap="butt", opacity=None):
    a = '<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" stroke-linecap="%s"' % (
        f1(x1), f1(y1), f1(x2), f1(y2), stroke, f1(sw), cap)
    if dash:
        a += ' stroke-dasharray="%s"' % dash
    if opacity is not None:
        a += ' stroke-opacity="%s"' % opacity
    return a + "/>"


def P(points, fill="none", stroke=None, sw=0):
    a = '<polygon points="%s" fill="%s"' % (" ".join("%s,%s" % (f1(x), f1(y)) for x, y in points), fill)
    if stroke:
        a += ' stroke="%s" stroke-width="%s" stroke-linejoin="round"' % (stroke, f1(sw))
    return a + "/>"


def ARC(x1, y1, x2, y2, r, sweep, stroke=CHAR, sw=2.5, dash=None):
    a = '<path d="M%s %s A%s %s 0 0 %d %s %s" fill="none" stroke="%s" stroke-width="%s"' % (
        f1(x1), f1(y1), f1(r), f1(r), sweep, f1(x2), f1(y2), stroke, f1(sw))
    if dash:
        a += ' stroke-dasharray="%s"' % dash
    return a + "/>"


def G(gid, *items):
    return '<g id="%s">%s</g>' % (gid, "".join(items))


# ---- badge, slot, arrows, dimensions ---------------------------------------------------------------------------------

class Canvas:
    def __init__(self, w, h, badge_xy, badge_size, badge_pad, badge_h, safe):
        self.w, self.h = w, h
        self.bx, self.by = badge_xy
        self.bsize, self.bpad, self.bh = badge_size, badge_pad, badge_h
        self.x0, self.x1, self.y0, self.y1 = safe     # content box (hard limits for fit checks)


IG = Canvas(1080, 1350, (90, 149), 48, 30, 72, (90, 990, 149, 1290))
SH = Canvas(1080, 1920, (90, 300), 68, 44, 104, (90, 930, 300, 1560))


def badge(cv, kind):
    txt = BADGE_CHAR if kind == "char" else BADGE_DIAG
    w = round(tw(txt, cv.bsize, 500) * 1.02 + 2 * cv.bpad)
    return ('<g id="badge">' + R(cv.bx, cv.by, w, cv.bh, CHAR, rx=cv.bh / 2)
            + Tc(cv.bx + w / 2, cv.by + cv.bh / 2, txt, cv.bsize, GROUND, 500) + "</g>")


def slot(spec, preview):
    """The character slot: empty and transparent in the final layer, neutral rectangle + label in the preview."""
    x, y, w, h, r = spec["x"], spec["y"], spec["w"], spec["h"], spec.get("r", 22)
    ring = R(x - 6, y - 6, w + 12, h + 12, "none", rx=r + 6, stroke=WALNUT, sw=12)
    attrs = ('data-asset="%s" data-golden-set="%s" data-x="%d" data-y="%d" data-w="%d" data-h="%d" data-rx="%d" '
             'data-aspect="%s"' % (spec["asset"], spec["golden"], x, y, w, h, r, spec["aspect"]))
    comment = ("<!-- CHARACTER SLOT %s (golden set %s, %s, %dx%d at %d,%d): PENDING. The photoreal image does not exist yet. "
               "Composite the approved still into this rectangle, clipped to rx=%d; the frame ring is drawn outside it. -->"
               % (spec["asset"], spec["golden"], spec["aspect"], w, h, x, y, r))
    if not preview:
        inner = R(x, y, w, h, "none", rx=r, extra=' fill-opacity="0"')
        return comment + ring + '<g id="character-slot" %s>%s</g>' % (attrs, inner)
    fs = max(22, min(30, round(w / 10)))
    lines = ["CHARACTER PANEL:", "PENDING"]
    cy = y + h / 2
    labels = "".join('<text x="%s" y="%s" font-size="%d" font-weight="500" fill="%s" text-anchor="middle">%s</text>'
                     % (f1(x + w / 2), f1(cy + (i - 0.5) * fs * 1.5 + 0.35 * fs), fs, PREVIEW_GREY, s)
                     for i, s in enumerate(lines))
    return comment + ring + '<g id="character-slot" %s>%s%s</g>' % (attrs, R(x, y, w, h, OAT, rx=r), labels)


def panel(asset, golden, aspect, x, y, w, r=22):
    ar = {"4:5": 1.25, "1:1": 1.0}[aspect]
    return dict(asset=asset, golden=golden, aspect=aspect, x=int(x), y=int(y), w=int(w), h=int(round(w * ar)), r=r)


def arrow(x1, y1, x2, y2, color=WALNUT, sw=6, head=26, halo=GROUND):
    """Single-headed pointing arrow (tip at x2, y2) with a ground-coloured halo so it reads over a photograph."""
    ang = math.atan2(y2 - y1, x2 - x1)
    bx, by = x2 - head * 0.9 * math.cos(ang), y2 - head * 0.9 * math.sin(ang)
    px, py = -math.sin(ang), math.cos(ang)
    tri = [(x2, y2), (bx + px * head * 0.5, by + py * head * 0.5), (bx - px * head * 0.5, by - py * head * 0.5)]
    return (L(x1, y1, bx, by, halo, sw + 8, cap="round") + P(tri, halo, halo, 8)
            + L(x1, y1, bx, by, color, sw, cap="round") + P(tri, color))


def head(x, y, ang, color=CHAR, ln=15, hw=7):
    """Arrow head with its tip at (x, y), pointing along angle ang (radians)."""
    bx, by = x - ln * math.cos(ang), y - ln * math.sin(ang)
    px, py = -math.sin(ang), math.cos(ang)
    return P([(x, y), (bx + px * hw, by + py * hw), (bx - px * hw, by - py * hw)], color)


def chip(cx, cy, n, r=26, size=32):
    return C(cx, cy, r, WALNUT) + Tc(cx, cy, str(n), max(size, MINSIZE), GROUND, 700)


def plate(cx, cy, label, size, hl=False, pad=10):
    w = tw(label, size, 700) + 2 * pad
    h = size * 1.3
    if hl:
        return R(cx - w / 2, cy - h / 2, w, h, WALNUT, rx=9) + Tc(cx, cy, label, size, GROUND, 700)
    return R(cx - w / 2, cy - h / 2, w, h, GROUND, rx=9) + Tc(cx, cy, label, size, CHAR, 700)


def hdim(x1, x2, y, label=None, size=40, hl=False, color=None, lw=2.5, dy=0, pad=10):
    color = color or (WALNUT if hl else CHAR)
    o = [L(x1, y, x2, y, color, lw), head(x1, y, math.pi, color), head(x2, y, 0, color)]
    o += [L(x1, y - 11, x1, y + 11, color, lw), L(x2, y - 11, x2, y + 11, color, lw)]
    if label:
        o.append(plate((x1 + x2) / 2, y + dy, label, size, hl, pad))
    return "".join(o)


def vdim(x, y1, y2, label=None, size=40, hl=False, color=None, lw=2.5, at=0.5):
    color = color or (WALNUT if hl else CHAR)
    o = [L(x, y1, x, y2, color, lw), head(x, y1, -math.pi / 2, color), head(x, y2, math.pi / 2, color)]
    o += [L(x - 11, y1, x + 11, y1, color, lw), L(x - 11, y2, x + 11, y2, color, lw)]
    if label:
        o.append(plate(x, y1 + (y2 - y1) * at, label, size, hl))
    return "".join(o)


def ext(x, y1, y2, color=CHAR):
    return L(x, y1, x, y2, color, 2, dash="3 6", opacity=0.7)


def scalebar(x, y, s, size=32):
    """100 cm scale bar (two 50 cm halves), label to the right."""
    half = 50 * s
    return (R(x, y - 7, half, 14, CHAR, stroke=CHAR, sw=2) + R(x + half, y - 7, half, 14, GROUND, stroke=CHAR, sw=2)
            + T(x + 100 * s + 14, y + 0.36 * size, "100 公分", size, CHAR, 500))


def tick_strip(x, y, w, h=40):
    """Cream strip with charcoal tick marks (no numerals): the belt motif as a divider."""
    o = [R(x, y, w, h, CREAM, rx=6)]
    n = int(w // 18)
    for i in range(1, n):
        tx = x + i * 18
        o.append(L(tx, y, tx, y + (h * 0.55 if i % 5 == 0 else h * 0.32), CHAR, 2.5))
    return "".join(o)


# ---- the Room 0 plan -------------------------------------------------------------------------------------------------

class Plan:
    """Top-down plan of Room 0. Coordinates in centimetres, origin at the top-left inside corner, far wall at y = 0."""
    BED_Y0 = 90          # bed y 90..280 (head against the free floor under the window wall)
    WARD_X0 = ROOM_W - WARD_D
    WARD_Y0 = 150        # wardrobe y 150..270, so it faces the lower part of the bed
    WIN = (90, 210)
    DOOR = (40, 120)

    def __init__(self, ox, oy, s):
        self.ox, self.oy, self.s = ox, oy, s
        self.wt = max(8.0, 6.5 * s)

    def X(self, cm):
        return self.ox + cm * self.s

    def Y(self, cm):
        return self.oy + cm * self.s

    @property
    def w(self):
        return ROOM_W * self.s

    @property
    def h(self):
        return ROOM_D * self.s

    @property
    def right(self):
        return self.ox + self.w

    @property
    def bottom(self):
        return self.oy + self.h

    def base(self, bed_w=BED_W, leaf=None, grille=True, ac=True, door=True, labels=False, tiles=True, furniture_labels=True):
        """leaf: None (wardrobe closed), 'arc' (dashed swing, leaf shown dashed), 'open' (leaf drawn solid, swing dashed)."""
        X, Y, s, wt = self.X, self.Y, self.s, self.wt
        o = [R(self.ox, self.oy, self.w, self.h, CREAM)]
        if tiles:
            for i in range(1, 6):
                o.append(L(X(50 * i), self.oy, X(50 * i), self.bottom, OAT, 2))
            for j in range(1, 8):
                o.append(L(self.ox, Y(50 * j), self.right, Y(50 * j), OAT, 2))
        # bed: against the left wall
        bx0, by0 = self.ox, Y(self.BED_Y0)
        o.append(R(bx0, by0, bed_w * s, BED_L * s, PUTTY, stroke=CHAR, sw=3))
        pw = (bed_w - 3 * 14) / 2.0
        for k in range(2):
            px = X(14 + k * (pw + 14))
            o.append(R(px, by0 + 10 * s, pw * s, 32 * s, CREAM, rx=5 * s, stroke=CHAR, sw=2))
        o.append(L(bx0 + 1.5, by0 + 80 * s, bx0 + bed_w * s - 1.5, by0 + 80 * s, CHAR, 2, opacity=0.5))
        if labels and furniture_labels:
            o.append(Tc(X(bed_w / 2.0), Y(self.BED_Y0 + 140), "床", 44 if s >= 1.2 else 40, DEEP, 700))
        # wardrobe: against the right wall, front face at x = 245, hinge at its top corner
        wx, wy = X(self.WARD_X0), Y(self.WARD_Y0)
        o.append(R(wx, wy, WARD_D * s, WARD_W * s, WALNUT_T, stroke=CHAR, sw=3))
        o.append(L(wx, wy, wx, wy + WARD_W * s, CHAR, 6))
        if labels and furniture_labels and s >= 1.2:
            o.append(Tc(X(self.WARD_X0 + WARD_D / 2.0), Y(self.WARD_Y0 + 92), "衣櫃", 34, DEEP, 700))
        if leaf:
            hx, hy = wx, wy
            tipx, tipy = X(self.WARD_X0 - LEAF), wy
            endx, endy = wx, Y(self.WARD_Y0 + LEAF)
            r = LEAF * s
            o.append(ARC(endx, endy, tipx, tipy, r, 1, WALNUT, 3, "8 7"))
            if leaf == "open":
                o.append(L(hx, hy, tipx, tipy, WALNUT, 7, cap="round"))
            else:
                o.append(L(hx, hy, tipx, tipy, WALNUT, 3, dash="8 7"))
            o.append(C(hx, hy, 6, CHAR))
        # walls (outside the interior), with the window gap on the far wall and the door gap on the near wall
        ox, oy, r_, b_ = self.ox, self.oy, self.right, self.bottom
        W0, W1 = self.WIN
        D0, D1 = self.DOOR
        walls = [
            (ox - wt, oy - wt, X(W0) - (ox - wt), wt),
            (X(W1), oy - wt, (r_ + wt) - X(W1), wt),
            (r_, oy - wt, wt, self.h + 2 * wt),
            (ox - wt, oy - wt, wt, self.h + 2 * wt),
            (ox - wt, b_, X(D0) - (ox - wt), wt),
            (X(D1), b_, (r_ + wt) - X(D1), wt),
        ]
        for wx_, wy_, ww, wh in walls:
            o.append(R(wx_, wy_, ww, wh, CHAR))
        # aluminium sliding window: two overlapping panes in the gap
        o.append(R(X(W0), oy - wt, X(W1) - X(W0), wt, OAT, stroke=CHAR, sw=2))
        o.append(L(X(W0), oy - wt * 0.66, X(W1), oy - wt * 0.66, CHAR, 2))
        o.append(L(X(W0), oy - wt * 0.33, X(W1), oy - wt * 0.33, CHAR, 2))
        o.append(L((X(W0) + X(W1)) / 2, oy - wt * 0.66, (X(W0) + X(W1)) / 2, oy - wt * 0.33, CHAR, 2))
        if grille:
            gx0, gx1 = X(W0 - 6), X(W1 + 6)
            gy1, gy0 = oy - wt, oy - wt - 20 * s
            o.append(R(gx0, gy0, gx1 - gx0, gy1 - gy0, GROUND, stroke=CHAR, sw=2.5))
            n = int((gx1 - gx0) // max(10, 15 * s))
            for i in range(1, n):
                gx = gx0 + i * (gx1 - gx0) / n
                o.append(L(gx, gy0, gx, gy1, CHAR, 2))
            o.append(L(gx0, (gy0 + gy1) / 2, gx1, (gy0 + gy1) / 2, CHAR, 2))
        # door: threshold line, leaf open 90 degrees (hinge on the right of the opening), swing arc
        if door:
            o.append(L(X(D0), b_, X(D1), b_, CHAR, 2.5))
            hx, hy = X(D1), b_
            o.append(L(hx, hy, hx, hy - (D1 - D0) * s, WALNUT, 4, cap="round"))
            o.append(ARC(X(D0), b_, hx, hy - (D1 - D0) * s, (D1 - D0) * s, 1, CHAR, 2, "5 6"))
            if labels and s >= 1.2:
                o.append(Tc(X(D0 + 42), Y(ROOM_D - 24), "門", 32, CHAR, 500))
        # split air conditioner (indoor unit, high on the right long wall): dashed because it is above the floor plane
        if ac:
            ax0, ay0 = X(ROOM_W - 17), Y(285)
            o.append(R(ax0, ay0, 17 * s, 70 * s, GROUND, stroke=CHAR, sw=2.5, dash="6 5"))
            o.append(L(ax0 + 6 * s, ay0 + 8 * s, ax0 + 6 * s, ay0 + 62 * s, CHAR, 2, opacity=0.6))
            if labels and s >= 1.2:
                o.append(T(X(ROOM_W - 24), Y(320) + 12, "冷氣", 32, CHAR, 500, "end"))
        if labels and s >= 1.2:
            o.append(T(X(W1 + 12), oy - wt - 10, "窗＋鐵窗", 32, CHAR, 500))
        return "".join(o)

    def walkway(self, bed_w=BED_W, y0=None, y1=None):
        """Shaded band between the bed edge and the wardrobe front, where both face each other."""
        y0 = self.WARD_Y0 if y0 is None else y0
        y1 = self.WARD_Y0 + WARD_W if y1 is None else y1
        x0, x1 = self.X(bed_w), self.X(self.WARD_X0)
        return (R(x0, self.Y(y0), x1 - x0, self.Y(y1) - self.Y(y0), WALNUT_T, extra=' fill-opacity="0.45"')
                + R(x0, self.Y(y0), x1 - x0, self.Y(y1) - self.Y(y0), "url(#hatch)"))


HATCH_DEFS = ('<defs><pattern id="hatch" width="14" height="14" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
              '<line x1="0" y1="0" x2="0" y2="14" stroke="%s" stroke-width="3" stroke-opacity="0.55"/></pattern></defs>' % WALNUT)


# ---- shared dimension sets -------------------------------------------------------------------------------------------

def dim_room_width(p, with_chip=False, size=40):
    y = p.bottom + p.wt + 42
    o = [ext(p.ox, p.bottom + 4, y + 11), ext(p.right, p.bottom + 4, y + 11),
         hdim(p.ox, p.right, y, str(ROOM_W), size)]
    if with_chip:
        o.append(chip(p.ox - p.wt - 34, y, 1))
    return "".join(o)


def dim_room_depth(p, size=36):
    x = p.right + p.wt + 50
    return (L(p.right, p.oy, x + 11, p.oy, CHAR, 2, dash="3 6", opacity=0.7)
            + L(p.right, p.bottom, x + 11, p.bottom, CHAR, 2, dash="3 6", opacity=0.7)
            + vdim(x, p.oy, p.bottom, str(ROOM_D), size, at=0.3))


def chain_top(p, kind, bed_w=BED_W, size=40, y_cm=60):
    """kind 'two' (slide 4: 150 + 55 with a plus sign), 'three' (slide 5: 150 | 95 | 55)."""
    y = p.Y(y_cm)
    ws = p.X(Plan.WARD_X0)
    o = [ext(p.X(bed_w), y, p.Y(Plan.BED_Y0)), ext(ws, y, p.Y(Plan.WARD_Y0))]
    o.append(hdim(p.ox, p.X(bed_w), y, str(bed_w), size))
    o.append(hdim(ws, p.right, y, str(WARD_D), size))
    if kind == "two":
        o.append(Tc((p.X(bed_w) + ws) / 2, y, "＋", 48, WALNUT, 700))
    else:
        o.append(hdim(p.X(bed_w), ws, y, str(ROOM_W - bed_w - WARD_D), size, hl=True))
    return "".join(o)


def chain_leaf(p, bed_w=BED_W, size=40, total=True, leaf_label=True, gap_dx=5):
    """Door-open dimensions: the remaining gap (highlight arrow on the leaf line, plate above), the 60 leaf, and the faint
    95 total above them (95 = gap + leaf)."""
    yl = p.Y(Plan.WARD_Y0)
    tipx = p.X(Plan.WARD_X0 - LEAF)
    ws = p.X(Plan.WARD_X0)
    gap = ROOM_W - bed_w - WARD_D - LEAF
    o = [hdim(p.X(bed_w), tipx, yl, None, hl=True, lw=3.5)]
    py = yl - size * 0.65 - 18
    o.append(plate((p.X(bed_w) + tipx) / 2 + gap_dx, py, str(gap), size, True, pad=5))
    if leaf_label:
        o.append(plate((tipx + ws) / 2, py, str(LEAF), size, False, pad=5))
    if total:
        yt = p.Y(70)
        o.append(ext(p.X(bed_w), yt, p.Y(Plan.BED_Y0)))
        o.append(ext(ws, yt, yl))
        o.append(hdim(p.X(bed_w), ws, yt, str(ROOM_W - bed_w - WARD_D), size - 6, color=WALNUT))
    return "".join(o)


def legend_row(x, y, size=38, rowmax=900):
    """The key of slide 4: 1 房間寬 / 2 床寬 ＋ 衣櫃深 / 3 衣櫃門板的長度 (one row)."""
    items = ["房間寬", "床寬 ＋ 衣櫃深", "衣櫃門板的長度"]
    r = size * 0.7
    widths = [2 * r + 12 + tw(t, size, 500) for t in items]
    gap = (rowmax - sum(widths)) / 2.0
    gap = min(gap, 44)
    if gap < 20:
        raise SystemExit("legend row too wide at size %d" % size)
    o, cx = [], x
    for n, (t, w) in enumerate(zip(items, widths), 1):
        o.append(chip(cx + r, y - 0.36 * size, n, r, int(size * 0.84)))
        o.append(T(cx + 2 * r + 12, y, t, size, CHAR, 500))
        cx += w + gap
    return "".join(o)


def tags_ig(show_note=True):
    """Top-right tag stack beside the badge on fit / clearance slides (kit: 示意數字 and 請以現場丈量為準)."""
    y = IG.by
    return G("tags", T(IG.x1, y + 28, TAG, 34, WALNUT, 700, "end"),
             T(IG.x1, y + 28 + 44, NOTE, 34, CHAR, 500, "end") if show_note else "")


# ---- frame builders: Instagram carousel (1080 x 1350) ----------------------------------------------------------------

def ig_s1(pv):
    """Cover: title on the left two-thirds, A1 panel on the right third, mini plan and the three things to compute."""
    o = [R(90, 258, 232, 60, CREAM, rx=30), Tc(206, 288, "算給你看 #01", 38, WALNUT, 700)]
    for i, line in enumerate(["小套房家具", "放不下？", "先算這三個數字"]):
        o.append(T(90, 428 + i * 98, line, 80, CHAR, 700, maxw=600))
    o.append(T(90, 720, "床、衣櫃、門板，走道還剩多少", 42, CHAR, 500, maxw=596))
    spec = panel("A1", "R01", "4:5", 694, 258, 284)
    # mini plan with the walkway as the unknown
    p = Plan(110, 818, 0.82)
    o.append(HATCH_DEFS)
    o.append(p.base(BED_W, None, grille=True, ac=True, door=True, labels=False))
    o.append(p.walkway())
    o.append(Tc((p.X(BED_W) + p.X(Plan.WARD_X0)) / 2, p.Y(210), "？", 56, DEEP, 700, halo=GROUND))
    o.append(scalebar(p.ox, p.bottom + p.wt + 34, p.s))
    # the three things to compute (same strings as slide 4's key)
    items = ["房間寬", "床寬 ＋ 衣櫃深", "衣櫃門板的長度"]
    for n, t in enumerate(items, 1):
        cy = 880 + (n - 1) * 100
        o.append(chip(480 + 30, cy, n, 30, 36))
        o.append(T(480 + 76, cy + 0.36 * 42, t, 42, CHAR, 500, maxw=420))
    return "".join(o), spec, "char"


def ig_s2(pv):
    o = [T(90, 340, "我是方寸，AI 虛擬角色。", 64, CHAR, 700, maxw=900)]
    spec = panel("A1", "R01", "4:5", 102, 420, 520)
    o.append(T(660, 486, "手不入鏡，", 46, CHAR, 500, maxw=330))
    o.append(T(660, 546, "所以用箭頭指。", 46, CHAR, 500, maxw=330))
    for i, line in enumerate(["腰上這條刻度帶", "只是造型，", "不是我量出來的。"]):
        o.append(T(660, 892 + i * 58, line, 40, CHAR, 500, maxw=330))
    belt_y = spec["y"] + spec["h"] - 36          # the belt sits at the bottom edge of a waist-up R01 (re-check on the real image)
    arr = G("annotations", "<!-- ARROW: tip placed for R01 waist-up (belt at the bottom edge of the panel). Re-check the tip "
            "against the real image when it is composited; the arrow is drawn after the slot, outside the photograph. -->",
            arrow(646, 1000, spec["x"] + spec["w"] - 56, belt_y))
    return "".join(o), spec, "char", arr


def ig_s3(pv):
    spec = panel("A3", "E09", "1:1", 728, 149, 250)
    o = [T(90, 540, "我沒住過任何房子，", 66, CHAR, 700, maxw=900),
         T(90, 626, "所以只整理尺寸和公開資料。", 66, CHAR, 700, maxw=900),
         R(90, 676, 130, 8, SAGE, rx=4),
         T(90, 780, "每個數字，", 48, CHAR, 500, maxw=900),
         TR(90, 846, [("不是標了「", {"weight": 500}), (TAG, {"weight": 700, "fill": WALNUT}),
                      ("」，就是附上出處。", {"weight": 500})], 48, maxw=900),
         TR(90, 990, nums("圖像為 AI 生成，並非真人。", 500, 700, None), 48, maxw=900),
         tick_strip(90, 1120, 900)]
    return "".join(o), spec, "char"


def _left_specs(x, y):
    """Slide 4 left column: the approved spec lines, split at the full-width spaces of the approved string."""
    lines = [("床：寬 150 公分", 0), ("衣櫃：寬 120、", 0), ("深 55 公分", 0), ("衣櫃門板：60 公分", 0), ("（示意數字）", 1)]
    o = []
    for i, (t, hl) in enumerate(lines):
        o.append(TR(x, y + i * 50, nums(t, 500, 700, WALNUT if hl else None, WALNUT if hl else CHAR), 36, maxw=350))
    return "".join(o)


def leaf_dim3(p, size=40):
    """Dimension 3 on slide 4 / scene 4: the 60 leaf, labelled above the swing; chip 3 to the right of it."""
    y = p.Y(112)
    tip, ws = p.X(Plan.WARD_X0 - LEAF), p.X(Plan.WARD_X0)
    return (ext(tip, y, p.Y(Plan.WARD_Y0)) + ext(ws, y, p.Y(Plan.WARD_Y0)) + hdim(tip, ws, y, str(LEAF), size)
            + chip(ws + 40, y, 3))


def ig_s4(pv):
    p = Plan(462, 590, 1.42)
    o = [T(90, 340, "先看這間示意房間", 72, CHAR, 700, maxw=900),
         TR(90, 408, nums("房間寬 300 公分、深 400 公分（示意數字）", 500, 700, None), 40, maxw=900),
         legend_row(90, 480, 36),
         HATCH_DEFS,
         p.base(BED_W, "arc", labels=True),
         chain_top(p, "two"), chip(p.ox - p.wt - 34, p.Y(60), 2),
         dim_room_width(p, True), dim_room_depth(p), leaf_dim3(p),
         _left_specs(90, 600), scalebar(90, 880, p.s)]
    spec = panel("A2", "R13", "4:5", 102, 920, 268)
    return "".join(o), spec, "char", None, tags_ig()


def ig_s5(pv):
    p = Plan(462, 590, 1.42)
    o = [TR(90, 340, [("第一步：走道有多寬？", {"weight": 700})], 66, maxw=900),
         TR(90, 408, [("走道 ＝ 房間寬 − 床寬 − 衣櫃深", {"weight": 500})], 42, maxw=900),
         HATCH_DEFS, p.base(BED_W, None, labels=True), p.walkway(),
         chain_top(p, "three"), dim_room_width(p),
         TR(90, 640, nums("300 − 150 − 55", 500, 700), 48, maxw=360),
         TR(90, 712, [("＝ ", {"weight": 700, "fill": WALNUT}), ("95", {"weight": 700, "fill": WALNUT}),
                      (" 公分", {"weight": 700, "fill": WALNUT})], 60, maxw=360),
         T(90, 770, "（示意數字）", 36, WALNUT, 700, maxw=350),
         scalebar(90, 880, p.s)]
    spec = panel("A2", "R13", "4:5", 102, 920, 268)
    return "".join(o), spec, "char", None, tags_ig()


def ig_s6(pv):
    p = Plan(462, 590, 1.42)
    o = [TR(90, 340, [("第二步：打開衣櫃門之後呢？", {"weight": 700})], 62, maxw=900),
         TR(90, 408, [("開門後的走道 ＝ 走道 − 門板長度", {"weight": 500})], 42, maxw=900),
         HATCH_DEFS, p.base(BED_W, "open", labels=True),
         chain_leaf(p), dim_room_width(p),
         TR(90, 640, nums("95 − 60", 500, 700), 56, maxw=360),
         TR(90, 712, [("＝ 35 公分", {"weight": 700, "fill": WALNUT})], 60, maxw=360),
         T(90, 766, "（門板開到 90 度，", 34, WALNUT, 700, maxw=360),
         T(90, 808, "示意）", 34, WALNUT, 700, maxw=360),
         scalebar(90, 880, p.s)]
    spec = panel("A2", "R13", "4:5", 102, 920, 268)
    return "".join(o), spec, "char", None, tags_ig()


def ig_s7(pv):
    pa, pb = Plan(165, 450, 1.0), Plan(615, 450, 1.0)
    o = [T(90, 340, "床寬換成 120 公分會怎樣？", 62, CHAR, 700, maxw=900), HATCH_DEFS]
    for p, bw in ((pa, BED_W), (pb, BED_W2)):
        o.append(p.base(bw, "open", grille=True, ac=True, door=True, labels=False, furniture_labels=False))
        o.append(p.walkway(bw))
        o.append(Tc((p.ox + p.X(bw)) / 2.0, p.Y(Plan.BED_Y0 + 140), "床", 40, DEEP, 700))
        y, ws = p.Y(60), p.X(Plan.WARD_X0)
        o += [ext(p.X(bw), y, p.Y(Plan.BED_Y0)), ext(ws, y, p.Y(Plan.WARD_Y0)),
              hdim(p.ox, p.X(bw), y, str(bw), 34, pad=8),
              hdim(p.X(bw), ws, y, str(ROOM_W - bw - WARD_D), 34, hl=True, pad=8),
              hdim(ws, p.right, y, str(WARD_D), 34, pad=8),
              chain_leaf(p, bw, 34, total=False, leaf_label=False, gap_dx=10 if bw == BED_W else 0),
              scalebar(p.X(26), p.Y(301), p.s)]
    o.append(Tc((pa.ox + pa.right) / 2, pa.bottom + 74, "床寬 150 公分", 38, CHAR, 700))
    o.append(Tc((pb.ox + pb.right) / 2, pb.bottom + 74, "床寬 120 公分", 38, WALNUT, 700))
    lx = 352
    o.append(TR(lx, 1040, nums("300 − 120 − 55 ＝ 125 公分", 500, 700, WALNUT), 44, maxw=640))
    o.append(TR(lx, 1100, nums("125 − 60 ＝ 65 公分", 500, 700, WALNUT), 44, maxw=640))
    o.append(T(lx, 1170, "一個數字變了，", 40, CHAR, 500, maxw=640))
    o.append(T(lx, 1218, "後面的數字都跟著變。", 40, CHAR, 500, maxw=640))
    o.append(T(lx, 1266, "（" + TAG + "）", 34, WALNUT, 700, maxw=640))
    o.append(T(lx + 200, 1266, NOTE, 34, CHAR, 500, maxw=420))
    spec = panel("A2", "R13", "4:5", 102, 985, 216)
    return "".join(o), spec, "char"


def _blank(x, y, w):
    return L(x, y + 8, x + w, y + 8, CHAR, 3.5, cap="round")


def _inline(x, y, tokens, size, gap=14):
    """tokens: ('t', text) | ('b', width). Returns (svg, end_x)."""
    o, cx = [], x
    for kind, v in tokens:
        if kind == "t":
            o.append(T(cx, y, v, size, CHAR, 500))
            cx += tw(v, size, 500) + gap
        else:
            o.append(_blank(cx, y, v))
            cx += v + gap
    return "".join(o), cx - gap


def ig_s8(pv):
    o = [T(90, 340, "換你填", 84, CHAR, 700)]
    size, bw = 46, 100
    # card 1: the approved line, wrapped before 「− 衣櫃深」; the full-width underscores are drawn as blank lines
    o.append(R(90, 410, 900, 350, CREAM, rx=26, stroke=OAT, sw=3))
    o.append(T(130, 474, "第一步", 36, WALNUT, 700))
    for y, toks in ((566, [("t", "走道 ＝ 房間寬"), ("b", bw), ("t", "− 床寬"), ("b", bw)]),
                    (676, [("t", "− 衣櫃深"), ("b", bw), ("t", "＝"), ("b", bw + 20), ("t", "公分")])):
        a_, ex = _inline(130, y, toks, size)
        if ex > 950:
            raise SystemExit("worksheet line too wide: %d" % ex)
        o.append(a_)
    # card 2
    o.append(R(90, 800, 900, 350, CREAM, rx=26, stroke=OAT, sw=3))
    o.append(T(130, 864, "第二步", 36, WALNUT, 700))
    for y, toks in ((956, [("t", "開門後 ＝ 走道"), ("b", bw), ("t", "− 門板長度"), ("b", bw)]),
                    (1066, [("t", "＝"), ("b", bw + 20), ("t", "公分")])):
        a_, ex = _inline(130, y, toks, size)
        if ex > 950:
            raise SystemExit("worksheet line too wide: %d" % ex)
        o.append(a_)
    # footer
    o.append(R(90, 1186, 900, 96, GROUND, rx=20, stroke=WALNUT, sw=4))
    o.append(Tc(540, 1234, NOTE, 52, DEEP, 700))
    return "".join(o), None, "diagram"


def stamp(cx, cy, w, h, angle, big=64, small=46):
    inner = (R(-w / 2, -h / 2, w, h, CREAM, rx=14, stroke=DEEP, sw=8)
             + R(-w / 2 + 14, -h / 2 + 14, w - 28, h - 28, "none", rx=8, stroke=DEEP, sw=3)
             + Tc(0, -h * 0.16, "出處章：", big, DEEP, 700) + Tc(0, h * 0.22, "示意數字・沒有外部出處", small, DEEP, 700))
    return '<g id="stamp" transform="translate(%s %s) rotate(%s)">%s</g>' % (f1(cx), f1(cy), f1(angle), inner)


def ig_s9(pv):
    spec = panel("A4", "E10", "1:1", 728, 149, 250)
    o = [T(90, 340, "蓋個出處章。", 76, CHAR, 700, maxw=600),
         stamp(396, 560, 600, 230, -3, 64, 44),
         T(90, 780, "本篇的數字都是示意數字，", 46, CHAR, 500, maxw=900),
         T(90, 842, "只用加減法，沒有外部出處。", 46, CHAR, 500, maxw=900),
         T(90, 940, "這是工作室整理的一般計算示範，", 46, CHAR, 500, maxw=900),
         T(90, 1002, "不是專業意見。", 46, CHAR, 500, maxw=900),
         T(90, 1110, "收藏起來，量自己房間的時候照著填～", 46, WALNUT, 700, maxw=900),
         tick_strip(90, 1170, 900)]
    return "".join(o), spec, "char"


# ---- frame builders: YouTube Short (1080 x 1920) ---------------------------------------------------------------------

def _sh_panel_scene(lines, size):
    """Scenes 1 to 3: the A1 still at the top, captions centred under it (one beat each)."""
    spec = panel("A1", "R01", "4:5", 210, 474, 600)
    o = [T(540, 1342 + i * (size + 30), t, size, CHAR, wgt, "middle", maxw=840) for i, (t, wgt) in enumerate(lines)]
    return "".join(o), spec


def sh_f1(pv):
    o, spec = _sh_panel_scene([("小套房家具放不下？", 700), ("先算這三個數字", 700)], 80)
    return o, spec, "char"


def sh_f2(pv):
    o, spec = _sh_panel_scene([("我是方寸，AI 虛擬角色。", 700), ("手不入鏡，所以用箭頭指。", 500)], 64)
    return o, spec, "char"


def sh_f3(pv):
    o, spec = _sh_panel_scene([("我沒住過任何房子，", 700), ("所以只整理尺寸和公開資料。", 700)], 60)
    return o, spec, "char"


def _sh_bottom_row(p):
    """Scale bar at the left and the clearance note at the right, on one baseline inside the safe zone."""
    return scalebar(90, 1514, p.s) + T(930, 1514 + 0.36 * 44, NOTE, 44, CHAR, 500, "end")


def sh_f4(pv):
    p = Plan(400, 800, 1.4)
    o = [T(90, 520, "這間示意房間：", 66, CHAR, 700, maxw=840),
         TR(90, 598, nums("寬 300 公分、深 400 公分", 700, 700, WALNUT, CHAR), 60, maxw=840),
         T(90, 656, "（示意數字）", 44, WALNUT, 700, maxw=840),
         legend_row(90, 728, 34, 840),
         HATCH_DEFS, p.base(BED_W, "arc", labels=True),
         chain_top(p, "two"), chip(p.ox - p.wt - 34, p.Y(60), 2),
         dim_room_width(p, True), dim_room_depth(p), leaf_dim3(p), _sh_bottom_row(p)]
    spec = panel("A2", "R13", "4:5", 102, int(p.bottom - 312), 250)
    return "".join(o), spec, "char"


def sh_f5(pv):
    p = Plan(400, 800, 1.4)
    o = [T(90, 520, "走道 ＝ 房間寬 − 床寬 − 衣櫃深", 56, CHAR, 500, maxw=840),
         TR(90, 620, nums("300 − 150 − 55 ＝ 95 公分", 700, 700, WALNUT, CHAR), 70, maxw=840),
         T(90, 678, "（示意數字）", 44, WALNUT, 700, maxw=840),
         HATCH_DEFS, p.base(BED_W, None, labels=True), p.walkway(),
         chain_top(p, "three"), dim_room_width(p), _sh_bottom_row(p)]
    spec = panel("A2", "R13", "4:5", 102, int(p.bottom - 312), 250)
    return "".join(o), spec, "char"


def sh_f6(pv):
    p = Plan(400, 800, 1.4)
    o = [T(90, 520, "打開衣櫃門之後", 66, CHAR, 700, maxw=840),
         TR(90, 620, nums("95 − 60 ＝ 35 公分", 700, 700, WALNUT, CHAR), 70, maxw=840),
         T(90, 678, "（示意數字）", 44, WALNUT, 700, maxw=840),
         HATCH_DEFS, p.base(BED_W, "open", labels=True),
         chain_leaf(p), dim_room_width(p), _sh_bottom_row(p)]
    spec = panel("A2", "R13", "4:5", 102, int(p.bottom - 312), 250)
    return "".join(o), spec, "char"


def sh_f7(pv):
    o = [T(90, 710, "以上是示意數字。", 84, CHAR, 700, maxw=840),
         T(90, 860, "你的房間尺寸，", 68, CHAR, 500, maxw=840),
         T(90, 950, "請用捲尺量過再算。", 68, CHAR, 500, maxw=840),
         R(90, 1050, 840, 150, CREAM, rx=26, stroke=WALNUT, sw=5),
         Tc(510, 1126, NOTE, 72, DEEP, 700),
         tick_strip(90, 1280, 840, 48)]
    return "".join(o), None, "diagram"


def sh_f8(pv):
    spec = panel("A4", "E10", "1:1", 340, 480, 400)
    o = [T(540, 1030, "收藏起來，下次照著填", 76, CHAR, 700, "middle", maxw=840),
         stamp(540, 1290, 760, 250, -3, 72, 50)]
    return "".join(o), spec, "char"


# ---- frame registry and assembly -------------------------------------------------------------------------------------

def frames():
    f = []

    def add(fid, post, cv, scene, media_index, builder, desc):
        f.append(dict(id=fid, post=post, cv=cv, scene=scene, media_index=media_index, builder=builder, desc=desc))

    p1 = "fangcun-2026-11-16-01"
    add("P01_s01_cover", p1, IG, "slide 1 (cover)", 4, ig_s1, "cover: hook title, A1 panel, mini plan, the three things to compute")
    add("P01_s02_who", p1, IG, "slide 2 (who I am)", 5, ig_s2, "identity lines, A1 panel, post-added arrow to the belt")
    add("P01_s03_rules", p1, IG, "slide 3 (the account's rules)", 6, ig_s3, "four rule lines, A3 small panel")
    add("P01_s04_room", p1, IG, "slide 4 (the example room)", 7, ig_s4, "Room 0 plan with dimensions 1 to 3, A2 panel")
    add("P01_s05_step1", p1, IG, "slide 5 (step 1)", 8, ig_s5, "walkway 300 - 150 - 55 = 95, A2 panel")
    add("P01_s06_step2", p1, IG, "slide 6 (step 2)", 9, ig_s6, "door open 95 - 60 = 35, A2 panel")
    add("P01_s07_whatif", p1, IG, "slide 7 (change one number)", 10, ig_s7, "two plans, bed 150 and bed 120, A2 panel")
    add("P01_s08_worksheet", p1, IG, "slide 8 (your turn)", 11, ig_s8, "blank worksheet, no character panel")
    add("P01_s09_stamp", p1, IG, "slide 9 (source stamp)", 12, ig_s9, "出處章 stamp, save prompt, A4 small panel")
    p2 = "fangcun-2026-11-17-01"
    add("P02_f1_hook", p2, SH, "scene 1 0:00-0:03", 3, sh_f1, "hook card, A1 still at the top")
    add("P02_f2_intro", p2, SH, "scene 2 0:03-0:08", 4, sh_f2, "identity captions, A1 still")
    add("P02_f3_rules", p2, SH, "scene 3 0:08-0:12", 5, sh_f3, "S09 replacement captions, A1 still")
    add("P02_f4_room", p2, SH, "scene 4 0:12-0:16", 6, sh_f4, "Room 0 plan with labels 1 to 3, A2 still")
    add("P02_f5_step1", p2, SH, "scene 5 0:16-0:21", 7, sh_f5, "walkway 300 - 150 - 55 = 95, gap highlighted, A2 still")
    add("P02_f6_step2", p2, SH, "scene 6 0:21-0:26", 8, sh_f6, "leaf open, 95 - 60 = 35, A2 still")
    add("P02_f7_closing", p2, SH, "scene 7 0:26-0:31", 9, sh_f7, "closing caption S08, no character panel")
    add("P02_f8_endcard", p2, SH, "scene 8 0:31-0:34", 10, sh_f8, "end card: stamp, save prompt, A4 still")
    return f


def assemble(fr, preview):
    out = fr["builder"](preview)
    body, spec, kind = out[0], out[1], out[2]
    annot = out[3] if len(out) > 3 and out[3] else ""
    tags = out[4] if len(out) > 4 and out[4] else ""
    cv = fr["cv"]
    slot_svg = slot(spec, preview) if spec else ""
    doc = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<!-- %s %s: DRAFT, code-drawn (no image model), not approved. Frame %s (%s, %s). %s. Do not edit by hand: '
           'edit %s and re-run. -->' % (SCRIPT_REL, VERSION, fr["id"], fr["post"], fr["scene"],
                                       "PREVIEW variant: the character slot is a placeholder" if preview else
                                       "FINAL layer: the character slot is empty and transparent", SCRIPT_REL),
           '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" lang="zh-Hant-TW" '
           'xml:lang="zh-Hant-TW" font-family="%s">' % (cv.w, cv.h, cv.w, cv.h, FONT),
           "<title>方寸 算給你看 %s</title>" % fr["id"],
           "<desc>%s. Generated by %s; arithmetic of the example room is asserted in the script.</desc>" % (fr["desc"], SCRIPT_REL),
           '<rect id="ground" width="%d" height="%d" fill="%s"/>' % (cv.w, cv.h, GROUND),
           G("content", body), slot_svg, annot, tags, badge(cv, "char" if kind == "char" else "diagram"), "</svg>"]
    svg = "\n".join(doc) + "\n"
    ET.fromstring(svg.split("?>", 1)[1])      # well-formedness check
    return svg, spec, kind


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--svg-only", action="store_true", help="write SVGs and frames.json, do not render PNGs")
    ap.add_argument("--only", action="append", help="frame id to build (repeatable)")
    ap.add_argument("--keep-preview-svg", action="store_true", help="also keep <id>_preview.svg next to the outputs")
    ap.add_argument("--out", default=OUT_DIR, help="output folder (default assets/fangcun/diagrams/A)")
    a = ap.parse_args()
    check_arithmetic()
    os.makedirs(a.out, exist_ok=True)
    manifest = []
    for fr in frames():
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
                subprocess.run([sys.executable, RENDER, tmp, png_path, str(fr["cv"].w), str(fr["cv"].h), "--bg", GROUND],
                               check=True)
        manifest.append(dict(id=fr["id"], post=fr["post"], scene=fr["scene"], media_index=fr["media_index"],
                             size=[fr["cv"].w, fr["cv"].h],
                             badge=BADGE_CHAR if kind == "char" else BADGE_DIAG,
                             svg="%s/%s.svg" % (OUT_REL, fr["id"]), preview_png="%s/%s_preview.png" % (OUT_REL, fr["id"]),
                             slot=({k: spec[k] for k in ("asset", "golden", "x", "y", "w", "h", "r", "aspect")} if spec else None),
                             note=fr["desc"]))
        print("ok", fr["id"])
    if not a.only:
        with open(os.path.join(a.out, "frames.json"), "w", encoding="utf-8") as fh:
            json.dump(dict(generator=SCRIPT_REL, version=VERSION, frames=manifest), fh, ensure_ascii=False, indent=1)
            fh.write("\n")


if __name__ == "__main__":
    main()
