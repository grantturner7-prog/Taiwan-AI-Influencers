"""步驟 (buzhou) front-view master, v0.1. Pure code-drawn flat vector (no outlines, no gradients).
Palette from personas/buzhou/bible.md 4.4. Shadow tones are DERIVED (about 8% darker), not in the bible.
Run: python3 buzhou_front.py <out.svg>
"""
import sys

INK, DUSK, FOG, BONE = "#3B4A5C", "#6F8197", "#C9D1DA", "#EEECE7"
CHAR, CHAR_L, SKIN, SKIN_S = "#2B3038", "#4A515B", "#D8B190", "#BE9371"
# derived flat shadow tones (assumption)
FOG_S, INK_S, BONE_S, CHAR_S = "#B3BEC9", "#323F4E", "#DCD9D2", "#23272E"

def svg():
    p = []
    a = p.append
    a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 1340" width="800" height="1340">')
    a(f'<rect width="800" height="1340" fill="{BONE}"/>')
    # ground shadow (flat)
    a(f'<rect x="0" y="1236" width="800" height="104" fill="#E3E6EA"/>')   # floor strip so bone shoes read (assumption)
    a(f'<ellipse cx="400" cy="1290" rx="170" ry="12" fill="#D2D7DD"/>')

    # ---- legs / trousers ----
    a(f'<path d="M334 680 L396 680 L394 1236 L338 1236 Z" fill="{CHAR}"/>')
    a(f'<path d="M404 680 L466 680 L462 1236 L406 1236 Z" fill="{CHAR}"/>')
    # one flat shadow shape per leg (inner side)
    a(f'<path d="M376 680 L396 680 L394 1236 L378 1236 Z" fill="{CHAR_S}"/>')
    a(f'<path d="M404 680 L420 680 L418 1236 L406 1236 Z" fill="{CHAR_S}"/>')
    # ---- sneakers (plain bone) ----
    a(f'<path d="M336 1236 L394 1236 L396 1262 Q396 1284 372 1284 L324 1284 Q306 1284 312 1268 Q318 1252 336 1246 Z" fill="{BONE}"/>')
    a(f'<path d="M464 1236 L406 1236 L404 1262 Q404 1284 428 1284 L476 1284 Q494 1284 488 1268 Q482 1252 464 1246 Z" fill="{BONE}"/>')
    a(f'<path d="M336 1236 L394 1236 L396 1256 L316 1262 Q320 1250 336 1246 Z" fill="{BONE_S}"/>')
    a(f'<path d="M464 1236 L406 1236 L404 1256 L484 1262 Q480 1250 464 1246 Z" fill="{BONE_S}"/>')
    a(f'<path d="M312 1272 L396 1272 L396 1284 L324 1284 Q306 1284 312 1272 Z" fill="{FOG}"/>')
    a(f'<path d="M488 1272 L404 1272 L404 1284 L476 1284 Q494 1284 488 1272 Z" fill="{FOG}"/>')

    # ---- tee (ink slate) ----
    a(f'<path d="M338 262 L462 262 L470 690 L330 690 Z" fill="{INK}"/>')
    a(f'<path d="M430 262 L462 262 L470 690 L440 690 Z" fill="{INK_S}"/>')

    # ---- neck ----
    a(f'<path d="M372 222 L428 222 L430 276 Q400 296 370 276 Z" fill="{SKIN}"/>')
    a(f'<path d="M372 222 L428 222 L428 246 Q400 262 372 246 Z" fill="{SKIN_S}"/>')
    # crew-neck collar band
    a(f'<path d="M364 262 Q400 304 436 262 L440 274 Q400 322 360 274 Z" fill="{INK_S}"/>')

    # ---- sleeves (coach jacket, fog) : viewer-left and viewer-right ----
    a(f'<path d="M286 276 L336 270 L330 650 L262 650 Q252 470 286 276 Z" fill="{FOG}"/>')
    a(f'<path d="M514 276 L464 270 L470 650 L538 650 Q548 470 514 276 Z" fill="{FOG}"/>')
    a(f'<path d="M262 650 L330 650 L329 668 L260 668 Z" fill="{FOG_S}"/>')   # cuffs
    a(f'<path d="M538 650 L470 650 L471 668 L540 668 Z" fill="{FOG_S}"/>')

    # ---- jacket body panels (boxy) ----
    a(f'<path d="M286 272 L350 262 L346 704 L282 704 Z" fill="{FOG}"/>')
    a(f'<path d="M514 272 L450 262 L454 704 L518 704 Z" fill="{FOG}"/>')
    # flat shadow shape on the right panel and under-hem band
    a(f'<path d="M486 268 L514 272 L518 704 L486 704 Z" fill="{FOG_S}"/>')
    a(f'<path d="M282 690 L346 690 L346 704 L282 704 Z" fill="{FOG_S}"/>')
    a(f'<path d="M518 690 L454 690 L454 704 L518 704 Z" fill="{FOG_S}"/>')
    # collar (flat stand collar)
    a(f'<path d="M340 246 L372 258 L362 292 L336 264 Z" fill="{FOG_S}"/>')
    a(f'<path d="M460 246 L428 258 L438 292 L464 264 Z" fill="{FOG_S}"/>')
    # hand pockets (hands hidden): slanted openings
    a(f'<path d="M290 600 L330 624 L330 646 L290 622 Z" fill="{FOG_S}"/>')
    a(f'<path d="M510 600 L470 624 L470 646 L510 622 Z" fill="{FOG_S}"/>')

    # ---- chest patch on character's LEFT chest (viewer's right) ----
    px, py, pw, ph = 466, 346, 58, 56
    a(f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="4" fill="{BONE}"/>')
    s, g = 12, 3
    base = py + ph - 7
    cols = [(px + 8, 1, FOG), (px + 8 + s + g, 2, DUSK), (px + 8 + 2 * (s + g), 3, INK)]
    for x, n, c in cols:
        for i in range(n):
            y = base - s - i * (s + g)
            a(f'<rect x="{x}" y="{y}" width="{s}" height="{s}" fill="{c}"/>')

    # ---- head ----
    a(f'<ellipse cx="326" cy="166" rx="10" ry="20" fill="{SKIN}"/><ellipse cx="474" cy="166" rx="10" ry="20" fill="{SKIN}"/>')
    a(f'<path d="M328 128 C328 80 352 56 400 56 C448 56 472 80 472 128 L464 196 L434 228 Q400 240 366 228 L336 196 Z" fill="{SKIN}"/>')
    a(f'<path d="M464 150 L472 140 L464 196 L434 228 Q426 232 418 234 L452 194 Z" fill="{SKIN_S}"/>')   # cheek/jaw shadow
    # hair (flat charcoal, side-parted to viewer's right) + one highlight
    a(f'<path d="M326 138 C322 78 352 47 402 47 C452 47 478 78 474 138 C470 112 458 96 436 90 C410 100 372 98 352 112 C342 120 334 128 326 138 Z" fill="{CHAR}"/>')
    a(f'<path d="M372 62 C392 54 424 56 440 68 C420 64 396 66 372 62 Z" fill="{CHAR_L}"/>')
    # brows
    a(f'<rect x="352" y="126" width="34" height="5" rx="2.5" fill="{CHAR}"/><rect x="414" y="126" width="34" height="5" rx="2.5" fill="{CHAR}"/>')
    # eyes: dark almonds with one highlight each
    for cx in (372, 428):
        a(f'<path d="M{cx-15} 154 Q{cx} 140 {cx+15} 154 Q{cx} 164 {cx-15} 154 Z" fill="{CHAR}"/>')
        a(f'<circle cx="{cx+5}" cy="150" r="2.6" fill="{BONE}"/>')
    # nose wedge shadow + mouth (slight asymmetric smile)
    a(f'<path d="M404 156 L416 190 L396 192 Z" fill="{SKIN_S}"/>')
    a(f'<path d="M382 210 Q400 214 420 205" stroke="{CHAR_L}" stroke-width="3.6" stroke-linecap="round" fill="none"/>')

    # ---- headphones: matte charcoal, generic over-ear, no logo ----
    a(f'<path d="M314 150 C314 70 356 40 400 40 C444 40 486 70 486 150" stroke="{CHAR}" stroke-width="12" fill="none" stroke-linecap="round"/>')
    a(f'<rect x="304" y="122" width="26" height="62" rx="12" fill="{CHAR}"/><rect x="470" y="122" width="26" height="62" rx="12" fill="{CHAR}"/>')
    a(f'<rect x="304" y="122" width="10" height="62" rx="5" fill="{CHAR_S}"/><rect x="486" y="122" width="10" height="62" rx="5" fill="{CHAR_S}"/>')
    a('</svg>')
    return "\n".join(p)

if __name__ == "__main__":
    open(sys.argv[1], "w").write(svg())
