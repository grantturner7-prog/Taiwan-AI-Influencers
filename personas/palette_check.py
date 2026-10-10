#!/usr/bin/env python3
"""Cross-persona palette check (Phase 3 integration pass, 2026-10-10).

Standard library only. Prints every pair of colours from two different
personas that is closer than a threshold, split into card grounds, figure
colours and accents. Distances are CIE76 delta E (lower is closer) with
CIEDE2000 beside it. Rough guide used in personas/README.md section 5:
under 3 is hard to tell apart, 3 to 6 is close, 6 to 10 is noticeable side
by side, above 10 is clearly different.

The hex values are copied by hand from section 4.5 of each bible
(personas/<slug>/bible.md). If a palette changes, edit PERSONAS below and
re-run. Nothing here reads the bibles, so a stale value is possible.

Usage:  python3 personas/palette_check.py [threshold, default 6]
"""
import math
import sys
from itertools import combinations

# role: g = card or image ground, f = figure colour, a = accent
PERSONAS = {
    "方寸 fangcun": {"platforms": {"IG", "YT"}, "g": {"off-white": "F5F0E6"},
                   "f": {"oat": "E4D9C3", "walnut": "6E5440"}, "a": {"sage": "A9B5A0"}},
    "步驟 buzhou": {"platforms": {"YT", "TH"}, "g": {"bone": "EEECE7"},
                  "f": {"ink slate": "3B4A5C", "dusk": "6F8197", "fog": "C9D1DA", "charcoal": "2B3038"}, "a": {}},
    "色環 sehuan": {"platforms": {"IG", "TH"}, "g": {"pale blush": "F2DAD2"},
                  "f": {"charcoal": "3A3735", "stone": "B8AEA2", "cream (garments)": "F4E8DF"}, "a": {"persimmon": "CD8B6A"}},
    "接話 jiehua": {"platforms": {"TH"}, "g": {"cream": "F3E9D8"},
                  "f": {"plum": "6B3A4F", "graphite": "4B4348"}, "a": {"ochre": "C4A05A"}},
    "轉乘 zhuancheng": {"platforms": {"YT"}, "g": {"paper": "E6E3D6"},
                      "f": {"sand": "D8C6A4", "taupe": "665B50"}, "a": {"dusty teal": "5C7F7B"}},
    "歲歲 suisui": {"platforms": {"FB"}, "g": {"aged paper": "D6C39A"},
                  "f": {"clay grey": "8A7E70", "slate brown": "5B534B", "canvas": "B7AA8E"}, "a": {"brick red": "98503F"}},
    "里程 licheng": {"platforms": {"FB"}, "g": {"concrete": "CFD2D0"},
                   "f": {"slate": "626669", "deep slate": "3E4345"}, "a": {"burgundy": "733235"}},
    "規格 guige": {"platforms": {"IG"}, "g": {"paper": "DEE3E1"},
                 "f": {"graphite": "454B48", "lead": "868B88", "mist": "BFC4C2", "film (tee, panels)": "F1F3F0"}, "a": {"lichen": "B7BE6F"}},
    "等一下 dengyixia": {"platforms": {"FB"}, "g": {"paper": "E6E1D9"},
                      "f": {"charcoal": "45414A", "stone": "A29CA2", "rain shell": "7F6A6D"}, "a": {"magenta": "A9508A"}},
    "歸位 guiwei": {"platforms": {"YT"}, "g": {"mist": "E7E5EB"},
                  "f": {"steel": "6E6B7B", "graphite": "4C4958", "light steel": "A9A7B3", "film (panels)": "F4F3F6"}, "a": {"violet": "7A6C96"}},
}


def lab(h):
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    f = lambda c: c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = f(r), f(g), f(b)
    x = (0.4124 * r + 0.3576 * g + 0.1805 * b) / 0.95047
    y = 0.2126 * r + 0.7152 * g + 0.0722 * b
    z = (0.0193 * r + 0.1192 * g + 0.9505 * b) / 1.08883
    t = lambda v: v ** (1 / 3) if v > 0.008856 else 7.787 * v + 16 / 116
    return 116 * t(y) - 16, 500 * (t(x) - t(y)), 200 * (t(y) - t(z))


def de76(a, b):
    return math.dist(lab(a), lab(b))


def de2000(a, b):
    L1, a1, b1 = lab(a)
    L2, a2, b2 = lab(b)
    C1, C2 = math.hypot(a1, b1), math.hypot(a2, b2)
    Cb = (C1 + C2) / 2
    G = 0.5 * (1 - math.sqrt(Cb ** 7 / (Cb ** 7 + 25 ** 7)))
    a1p, a2p = (1 + G) * a1, (1 + G) * a2
    C1p, C2p = math.hypot(a1p, b1), math.hypot(a2p, b2)
    h1 = math.degrees(math.atan2(b1, a1p)) % 360
    h2 = math.degrees(math.atan2(b2, a2p)) % 360
    dL, dC = L2 - L1, C2p - C1p
    if C1p * C2p == 0:
        dh = 0
    else:
        dh = h2 - h1
        dh -= 360 if dh > 180 else 0
        dh += 360 if dh < -180 else 0
    dH = 2 * math.sqrt(C1p * C2p) * math.sin(math.radians(dh / 2))
    Lb, Cbp = (L1 + L2) / 2, (C1p + C2p) / 2
    if C1p * C2p == 0:
        hb = h1 + h2
    else:
        hb = (h1 + h2) / 2
        if abs(h1 - h2) > 180:
            hb += 180 if h1 + h2 < 360 else -180
    T = (1 - 0.17 * math.cos(math.radians(hb - 30)) + 0.24 * math.cos(math.radians(2 * hb))
         + 0.32 * math.cos(math.radians(3 * hb + 6)) - 0.20 * math.cos(math.radians(4 * hb - 63)))
    dth = 30 * math.exp(-(((hb - 275) / 25) ** 2))
    Rc = 2 * math.sqrt(Cbp ** 7 / (Cbp ** 7 + 25 ** 7))
    Sl = 1 + 0.015 * (Lb - 50) ** 2 / math.sqrt(20 + (Lb - 50) ** 2)
    Sc, Sh = 1 + 0.045 * Cbp, 1 + 0.015 * Cbp * T
    Rt = -math.sin(math.radians(2 * dth)) * Rc
    return math.sqrt((dL / Sl) ** 2 + (dC / Sc) ** 2 + (dH / Sh) ** 2 + Rt * (dC / Sc) * (dH / Sh))


def main():
    thr = float(sys.argv[1]) if len(sys.argv) > 1 else 6.0
    names = {"g": "CARD GROUNDS", "f": "FIGURE COLOURS", "a": "ACCENTS"}
    for role in ("g", "f", "a"):
        print(f"== {names[role]} closer than {thr} (CIE76 / CIEDE2000)")
        rows = []
        for (pa, da), (pb, db) in combinations(PERSONAS.items(), 2):
            for ka, va in da[role].items():
                for kb, vb in db[role].items():
                    d = de76(va, vb)
                    if d < thr:
                        shared = "/".join(sorted(da["platforms"] & db["platforms"])) or "-"
                        rows.append((d, de2000(va, vb), pa, ka, va, pb, kb, vb, shared))
        for r in sorted(rows):
            print(f"  {r[0]:4.1f} / {r[1]:4.1f}  {r[2]} {r[3]} #{r[4]}  ~  {r[5]} {r[6]} #{r[7]}   shared platform: {r[8]}")
        if not rows:
            print("  none")


if __name__ == "__main__":
    main()
