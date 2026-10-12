# 色環 (sehuan): Visual identity v2, photoreal

**Document status: DRAFT v0.1, written 2026-10-11.** Addendum to `personas/sehuan/bible.md`. Reason: the user rejected the stylised look ("looks so fake, I need real people", `DECISIONS.md` 2026-10-11). The recorded reading is **photorealistic AI-generated characters that stay openly AI**. It is not a switch to human presenters. Every zh-TW string here is an AI draft for the wife, with an English gloss beside it because the operator does not read Chinese. Nothing in this file has been generated or tested: no photoreal reference image exists, and every statement about what Gemini or ChatGPT can do is a **hypothesis**. Labels: *assumption* (my planning figure), *unverified* (not confirmed from a primary source), *recalled* (from memory, not checked), *computed* (calculated this session).

The copy-paste procedure that goes with this file is `pipeline/image-pack/sehuan-photoreal.md` (the "pack"). Save outputs in `assets/sehuan/photoreal/`.

Two sibling addenda were written the same day (`personas/fangcun/photoreal-addendum.md`, `personas/buzhou/photoreal-addendum.md`). Section 10 compares against their drafts as they stand; they were not changed by this pass.

**At a glance (details in section 0).**

- **Supersedes, do not use the old text:** bible **4.1 face and build**; **4.5 art medium** (the typography rule in 4.5 stays); **section 5, the consistency sheet** (5.1 to 5.8; the 5.9 provenance template stays); 4.7 adult-reading check; the rendering side of 4.2 styling, 4.3 wardrobe and 4.4 skin, hair and lip swatches; and **every "stylised", "drawn", "illustration" or "mitten hand" wording about how she looks** (the full list is 0.1).
- **Stays:** voice (bible section 3, including the sample lines and reply templates), content pillars (6), disclosure lines (8, with additions in 8.2 here), the palette as wardrobe and set colours (4.4, with a deeper photo backdrop), Do and Don't (7.1, 7.2), tripwires (7.3, extended in 8.3 here), identity and jokes (2), choices C1 to C14 (C9 amended), monetisation (9) and the gates (1.2).
- **What is new:** a photoreal face and build described in generic terms (2); signature constants (3); a wardrobe lock (4); hands out of frame or in pockets (5); one studio look (6); photoreal risks (8); stricter adult-reading, age-guess and look-alike tests (9); a near-pair note against 方寸 and 步驟 (10); and a list of rulings for the wife (12).

---

## 0. What this file supersedes and what stays

Read this first. On a row marked **Superseded**, this file wins over `bible.md`. On a row marked **Stays**, the bible wins. The section numbers the request cited match the bible here: 4.1 is face and build, 4.5 is art medium, 5 is the consistency sheet.

### 0.1 Superseded

| `bible.md` | What it said | Now |
|---|---|---|
| Header table row "Medium"; Precedence bullet naming "stylised characters"; `portfolio.md` 2D row 3 ("deliberately no photoreal skin or fabric") | Fashion illustration, flat colour, ink-brush line | Photoreal AI-generated studio imagery (sections 1 and 6). `DECISIONS.md` 2026-10-11 prevails over the 2026-10-10 stylised decision |
| 1.1 rows "Style" and "Assets" | Stylised; no assets | Photoreal; still no assets. New folder `assets/sehuan/photoreal/` |
| 1.2 gate G4 (master reference image); G6 ("on a stylised character") | Hand-finished master sheet; label check | G4 is now the photoreal master set R01 to R16 (section 11) passing section 9. G6 is stricter: the "AI-generated profile" label is expected to apply and is switched on from day one (8.2) |
| 2.4 rows "Shape", "Limits stated by design" ("she is a drawing"), "Where she lives" ("illustrations") | Built from flat fields and a brush line; backgrounds are illustrations | "Shape" and "she is a drawing" are retired. Replacement wording: she is an AI-generated character with no body, no measurements and no fit information. Backgrounds follow 5.5 |
| 2.8 joke J2 and its example line (「只有一圈畫出來的色票」); J1 wording | The chips are "drawn"; "about one tenth of the frame" | The chips now look like real cards, so J2 is reworded (12.2). J1 stays as a cap, worded 「最多」 (12.2) |
| C9 "Puppet workflow"; C12 "on this drawing" | Cut-outs of a drawn character plus human-built flats | C9 stays in structure: cut-outs of the **photoreal master set** plus human-built flats, dress form, wheel diagram and typeset text. No new face is generated per post. C12 wording becomes 「在這張圖裡」 ("in this layout"); the rule stays |
| 4.1 face and build (all rows, including "seven and a half heads", flat fills, mitten hands) | Illustrated woman-presenting character | Section 2 here |
| 4.2 styling; the "Not a photo" bullet; earring and chip ring "drawn" | Brush-line tell | Section 3 here. The tells (wheel earring, persimmon accent, six-card ring) stay. The "not a photo" bullet is retired: **in photoreal nothing about the picture says "not a photo", so disclosure rests on the stack in 8.2** |
| 4.3 wardrobe | Outfits A, B, C and V1 to V3 | IDs and logic stay; rendered as real fabric (section 4). Three adjustments for photoreal crops: accent placement, sneakers, deferred objects |
| 4.4 palette: skin, skin shadow, hair, lips, eye highlight hex | Flat swatches | Skin, hair and lips are **photographs now** and are judged by eye against R01, not by hex. The garment and set colours stay. The photo backdrop is a deeper blush (4.4) |
| 4.5 art medium and typography | Illustration; Taiwan-glyph font, text typeset in post | Medium replaced by section 6. **The typography rule stays**: no generated Chinese, typeset in post in a Taiwan (TC) glyph font, read by the wife |
| 4.6 templates: "cut-outs from approved poses", "simple mitten hand", badge placement | Mitten-hand asset; badge in a corner | Cut-outs come from the photoreal set. No mitten-hand asset exists: hands are out of frame or in pockets (5.1). Badge becomes persistent and larger (8.2) |
| 4.7 adult-reading check | Thumbnail check; panel of wife plus 2 or 3 | Section 9 (stricter) |
| 4.8 recurring Taiwan settings | Backgrounds for covers, labelled 示意 | Stays as a checklist for **human-built 示意 plates that never contain her**. No photoreal setting with her in it in the pilot (5.5) |
| 4.9 last bullet "Style: photorealism, 3D renders, ..." | Photorealism banned | Photoreal is now the style. The rest of that bullet (3D, anime, chibi, large glossy eyes, "in the style of") stays |
| 5.1 to 5.8 (master prompt, Gemini and GPT variants, expressions, poses, locked-features list, same-face procedure, look-alike procedure, R01 to R18 list) | Illustration workflow | The pack, plus sections 3, 5, 9 and 11 here. Principles carried over unchanged: one change per generation, no text in the picture, log the same day, never image-to-image from a real person's photo, no telephone game |
| 7.1 Do 9; 3.5 "drawn character" wording | Wheel and chips built by hand; "sexual comments about the drawn character" | Do 9 stays **for lesson graphics**. The earring and the ring on the character are generated, with an object-only repair allowed (11.6). "Drawn character" now reads "the character" |
| 8.3 badge "or at least the first second"; 8.4 first bullet ("a flat stylised illustration may fall outside the platforms' photorealism wording") | Light badge; label maybe exempt | Persistent badge on every image and every video frame; platform label always on; account-level label expected (8.2) |

### 0.2 Stays

- **Voice and language:** all of section 3 of the bible (register, 我 rules, Taiwan vocabulary, banned words, comment handling R-codes, the 20 sample lines). S06 stays but gets a photoreal variant (12.2).
- **Identity:** 2.1 name 色環 (reading test still open), 2.2 handles, 2.3 stated age 30 (design value only), 2.5 personality, 2.6 values, 2.7 boundaries with the other personas, 2.8 jokes J3 and J4 as written.
- **Choices C1 to C14**, with C9 amended as above. **C1 (presenter, not wearer) matters more now**, see 8.1 row M. C2 (no skin-tone matching, no personal colour analysis, no viewer photos) and C3 and C4 (colour-word politics, rainbow policy) also matter more, see 7.
- **Pillars P1 to P4** and the cadence (section 6 of the bible).
- **Do and Don't** (7.1, 7.2) except as noted above. 7.1 Do 15 (look-alike check) is now governed by section 9 here.
- **Tripwires** (7.3), **extended** in 8.3.
- **Disclosure** (section 8 of the bible): bio lines, the first-line pattern, paid, gifted, affiliate and automated lines. 8.2 here adds to them.
- **Monetisation and brand-safety** (section 9), except that the client 虛擬試穿示意 route is on hold for a photoreal body (8.1 row N).
- **Palette as wardrobe and set colours** (4.4): cream `#F4E8DF`, charcoal `#3A3735`, warm stone `#B8AEA2`, persimmon `#CD8B6A`, the twelve wheel hues and the six chip tints. Changes are limited to the photo backdrop and the listed skin, hair and lip rows (4.4 here).
- **Gates** in 1.2 not named above, and the **look-alike log** location (`personas/sehuan/lookalike_log.md`, created when the first master is tested).

---

## 1. Design intent

色環 v2 is a **fictional adult woman-presenting character, stated age 30**, calm, precise and unhurried, shown in plain studio portraits. She has no wardrobe, no home and no belongings. Her three outfits are her fixed design, like a mascot's costumes. She is still openly an AI character from 明說角色工作室 (provisional name), she still "cannot wear, try on, buy or own clothes" (bible 2.4), and she is still a **presenter, not a wearer** (C1): lessons show outfits as human-built garment flats and a faceless dress form, and she stands beside the lesson.

Two things change:

1. **Realism makes disclosure more important, not less** (Ground rule 1). Nothing in this file is designed to make her pass as a real person. The studio look (section 6) is deliberately a *produced* look, not a phone snapshot, and every image carries a label (8.2).
2. **Realism makes the failure modes harsher.** Hands, ears, earrings, teeth, fabric seams and buttons are where "near-real but wrong" is punished fastest (the IKEA Taiwan hands case, `competitors.md` section 5). A fashion character is also judged on garments: an odd collar or a melted button on a photoreal blazer is an "invented garment detail", which is a standing tripwire (bible 7.3). The framing rules in section 5 are built around this.

**Not covered:** video, lip-sync and voice for a photoreal face. A synthetic voice on a photoreal face is a different order of risk and needs its own addendum and review first (8.1 row J).

---

## 2. Face and build (generic, original, non-identifiable)

The combination below was invented from generic attributes. It is not modelled on any real person, performer, public figure, existing virtual character or the user's wife, and no prompt may name one. That does **not** guarantee that a generator's output resembles nobody; a generated face can resemble a real person by chance. That is why section 9 is stricter than the stylised bible.

| Feature | Specification | Why / note |
|---|---|---|
| Presentation | Woman-presenting adult. Stated age **30** (design value, never a credential, never "when I was starting out"). Visible age target **about 30 to 35**; never younger-looking than 28 | Ground rule 3: visible age about the stated age or older |
| Overall impression | Composed, attentive, precise, quietly warm; teacherly in method but not stern | A look, not a life story |
| General features | Ordinary East Asian adult features, natural and unexaggerated, with mild natural asymmetry. Not an idol, model, influencer or screen-star template | `culture.md` 7.4: generators default to an "idol" look. Prompt wording is the wife's decision (end of this section, and 12.1 item 2) |
| Face shape | **Oval of medium length, widest at the cheekbones, tapering to a narrow, softly rounded chin.** Softly defined cheekbones and a gentle jaw shadow. Not squared, not long, not pointed | **Changed from the bible's "long-oval"** to separate her from 步驟 (long oval, defined jaw, straight chin) and 方寸 (softly squared, rounded chin). Wife rules (12.1 item 3) |
| Forehead and hairline | Medium forehead, natural hairline, partly framed by the side-swept parting. No fringe | |
| Eyes | Almond-shaped, dark brown, modest size (each about one fifth of the face width, the bible's figure), slightly upturned outer corners, natural eyelid fold, calm level gaze, faint natural fine lines at the outer corners when relaxed | No enlarged eyes, no coloured lenses, no glitter, no heavy lashes, no eyelid-tape look |
| Brows | Straight, medium thickness, dark brown-black, natural, very slightly uneven | The bible's "straight dark eyebrows of medium thickness" |
| Nose | Small-to-medium, narrow-to-medium bridge, soft tip | The bible's "short" nose stroke, translated |
| Mouth | Medium lips in a muted terracotta-brown (natural, not lipstick). **Closed**, with a very slight, calm, faintly asymmetric smile (the bible's default). Teeth not shown | Teeth are a top failure area. No gloss, no lipstick, no tint |
| Skin tone | **Medium, warm golden-beige**, even, **identical in every image**. Never whitened, brightened, tanned or darkened, in generation or in editing | The bible's "warm medium" family. Judged by eye against R01, not by hex. Skin tone is never mentioned in copy (C2). **Retouching to brighten skin is banned** (顯白 culture, Don't 4) |
| Skin texture | Natural: fine pores visible at 100%, faint fine lines, soft under-eye shadow, subtle tonal variation. No airbrushed, waxy, glossy or plastic look | The user's complaint was "looks so fake"; plastic skin is the most likely cause |
| Makeup | Minimal and natural. No blush, no contour, no eyeliner wings, no glitter, no gloss, no false-lash look | Ground rule 6: nothing that reads as a cosmetic claim |
| Hair | Natural dark brown-black, **shoulder-length with a blunt-cut line**, straight with very slight natural movement. **Deep side parting on her right (the viewer's left)**. The hair on her **left** side is tucked behind her left ear so the ear and earring show; the right side falls forward past the cheek to the shoulder and mostly covers the right ear. A few natural flyaways. Not dyed, no highlights, not glossy, no clips or bands | The bible's hair, with the parting side made explicit. Silhouette is distinct from both siblings (10) |
| Ears | **Left ear fully visible**, natural shape, pierced lobe wearing the earring. Right ear mostly covered in a front view; if the right earring shows below the hair edge it must match the left | Resolves the bible's "both ears visible" against "tucked behind the left ear" |
| Neck and shoulders | Natural, relaxed, level shoulders; neckline covers the collarbone | Modest wardrobe rule |
| Build | Average-to-slim, natural adult proportions, relaxed upright posture, natural soft shoulders, no waist, bust or hip shaping or emphasis. **Height, weight and size are never stated** | Ground rules 3 and 6. The bible's "seven and a half heads" was a fashion-illustration proportion and is dropped |
| Head size | Head about one seventh of standing height in full-body images; **fail above one sixth** | Carried over from the sibling checks. An elongated fashion proportion signals an idealised body |
| Hands | Not shown, or in pockets. See 5.1 | |
| Age cues (what a generator drops) | Faint smile lines at the eye corners; faint lines from nose to mouth corners at rest; defined, not round or baby-fat, cheeks; adult jaw and neck; composed expression; upright mature posture | Generators drift young and smooth |
| Absent on purpose | Tattoos, scars, birthmarks, freckles as a feature, glasses, hair dye, nail art, any jewellery other than the two earrings, watch, rings | Fewer features to drift; fewer things that could match a real person |
| Expression defaults | Calm and attentive, level brows, closed lips with a very slight smile. E01 to E10 as named in the bible (5.4) are redefined for a real face in 5.3 | |
| Pronouns in copy | Name or 「這個角色」, with 「我」 for her own voice, until the wife rules on 她 (12.1 item 1) | |

**Feature wording for prompts (decision for the wife).** Default neutral wording used in the pack: *"East Asian, with ordinary, natural, unexaggerated features, not an idol or model look."* Option B, only if she approves: *"... that read as Taiwanese."* Option C, a neutral alternative: *"an ordinary adult you could plausibly see on an everyday street in a large East Asian city."* Option D: drop the region and describe features only, then she judges the result for Taiwan plausibility. A generator cannot reliably produce "Taiwanese" and the phrase invites stereotype, so I recommend the default (this is the open item 5 in bible section 11).

---

## 3. Signature constants (always present)

If one is missing the image fails the "same person" check.

| # | Constant | Detail | Visible in |
|---|---|---|---|
| SC1 | **Colour-wheel earrings** | A matching pair of round drop earrings: a flat, matte, enamel-look disc hanging from a small plain hook, **twelve equal wedge segments** in the muted wheel hues in this order: dusty red, red-orange, soft orange (the persimmon), golden yellow-orange, muted yellow, yellow-green, sage green, blue-green, dusty blue, blue-violet, soft violet, red-violet. Diameter about **one fifth to one quarter of the face width, roughly 2.5 to 3 cm** (the bible's "a little larger than life so it survives a small avatar", scaled down so a photo does not look like a prop). No gloss, no gems, no metal rim detail, **no numerals or letters**. Saturation never above the persimmon's | **Left earring in every image** that shows the left side of the head; the right one when the hair leaves it visible. Back view: the tucked-side earring shows from behind |
| SC2 | **Hair silhouette** | Shoulder-length blunt cut, deep side parting, left side tucked behind the left ear, right side forward | Every image |
| SC3 | **One persimmon accent** | Soft, muted terracotta-orange (`#CD8B6A`), **at most about one tenth of the visible figure** (a cap, not a target; a neckerchief is usually 2 to 5% of a waist-up image). One accent item per outfit: the matte cotton neckerchief in A and C, the canvas tote with its strap in B, the scarf end stripe in V3 | Every image from headshot to full body |
| SC4 | **Chip ring** | A ring of **exactly six blank, muted colour-chip cards** (tints `#E6BBA3`, `#E4D6CB`, `#B8AEA2`, `#D2AE72`, `#C27F80`, `#9F8AAB`) fanned on a thin charcoal binder ring, **clipped** to the belt loop at the left hip (outfits A, C) or to the tote strap (B). Never held. **No text, numbers or codes on the cards** | Whenever the hip or the strap is in frame (knees-up, full body, and outfit B waist-up). Not required in headshot, half-body or waist-up of A and C |
| SC5 | **Palette** | Cream, warm stone, charcoal, one persimmon accent; no head-to-toe white or black | Every image |
| SC6 | **Studio Look v2** | Blush seamless backdrop, key light from the front right, the grade in section 6 | Every image |
| SC7 | **Calm default face** | Closed lips, very slight smile, level brows | Default. Expressions change only brows, eyes and lips (5.3) |
| SC8 | **Nothing else on her** | No necklace, ring, watch, bracelet, glasses, hair accessory, phone, lanyard or badge | Every image |
| SC9 | **Label** | On-screen badge on every published image and an "AI" chip on the avatar (8.2). Added in post, never generated | Every published image |

**Thumbnail tell (110 px, front, waist-up):** shoulder-length hair with one side tucked, a coloured dot at the left ear, a persimmon patch at the collar, a blush backdrop. If a thumbnail shows both ears covered, no earring dot, or no persimmon, it fails.

**Why a flat disc and not a hoop, ring or arc.** A flat disc holds twelve wedges better than anything else and is hard to mistake for a rainbow flag (C4). If a generator cannot hold twelve wedges at earring size, the ladder is: (1) accept any muted, segmented, round disc of 10 to 14 wedges while choosing a master; (2) on the final master, the human replaces the earring pixels with the hand-built twelve-segment wheel, matched to perspective and light. That is an **object-only** edit, logged, with the untouched original kept (11.6). It is never done to a face, skin, hand or body.

**If the neckerchief reads as a uniform.** A small knotted neckerchief with a blazer can read as airline-crew or shop-staff styling, and a satin sheen makes it worse. Specification: cotton-or-linen look, matte, folded to a narrow band, loosely knotted, ends tucked, never tight at the throat. If the wife still sees a uniform (12.1 item 5), the fallbacks in order are: a longer matte persimmon scarf draped open with both ends hanging; then the tote strap as the accent in every outfit.

---

## 4. Wardrobe lock

The wardrobe is the **character's fixed design**. She has no closet and does not choose outfits. Outfits are never taught, ranked, recommended or described as "what she wears today" (that would be a wearing claim and the FAS1 tripwire). Garments are never shown as products and never named. Nothing is all-white or all-black. Nothing carries a logo, text, tag, label, stripe, check or recognisable signature pattern, and no garment may copy the silhouette of a recognisable branded piece. Fabrics are matte, with a visible weave. Colours in prompts are written as words; hex values are for the colour checks (see 4.4).

### 4.1 Three core outfits

| ID | Name | Pieces (photoreal) | Persimmon | Framings allowed |
|---|---|---|---|---|
| **A** (default, about 70% of images; *assumption*) | 外套組 | Relaxed, unstructured single-breasted blazer in warm stone grey, worn **open**, plain buttons, real side pockets; cream fine-knit crew-neck top (a faint peach-pink cast), neckline covering the collarbone; charcoal straight wide trousers ending at the ankle, belt loops; flat charcoal loafers | Matte cotton-linen neckerchief at the collar | F1 to F6 |
| **B** | 背心裙裝組 | Cream long-sleeve collared shirt, collar open at the top button only, **sleeves rolled to the elbow**, no tie, no bow; charcoal sleeveless knit vest over it; warm stone midi skirt **below the knee** with in-seam pockets; charcoal ankle boots; a plain canvas tote on the right shoulder (the viewer's left) | The tote, with the chip ring clipped to its strap at chest height | F1 to F4, F6. Full body (F5) optional |
| **C** | 長版針織組 | Long open knit coat in charcoal, plain, hip-to-thigh length, over a cream crew-neck tee; warm stone straight trousers; flat canvas sneakers in warm stone (no logo, no stripe) | Matte neckerchief, as in A | F1 to F6 |

**Photoreal adjustments to the bible's wardrobe (all in 12.1 for the wife):** (1) outfit C's accent moves from the sneakers to the neckerchief, because headshot, half-body and waist-up crops never show shoes and an outfit without its accent fails the thumbnail tell; (2) the sneakers become plain warm-stone canvas; (3) outfit B's school-uniform risk (the "shirt, vest, skirt" combination that the stylised pack already flagged, and bible 4.7 item 3) is handled by the cut rules above and by the age-guess test.

### 4.2 Taiwan season variants

Season timing is recalled, not verified (`culture.md` 7.4; bible 4.3). Settings stay a plain studio: rain, a drying rack or a damp street are never generated with her in them.

| Variant | Change | Taiwan reason |
|---|---|---|
| **V1 熱濕版** hot and humid (about June to September) | Short-sleeve cream shirt worn untucked (sleeves end above the elbow); warm-stone wide trousers cropped at the ankle; plain closed-toe flat shoes; matte neckerchief. No shorts, no sleeveless-alone, no sandals | Heavy knitwear is wrong for most of the year. Closed-toe flats avoid the sandal-and-toes failure. Never described as sun protection (C11) |
| **V2 雨季版** rain (about May to June, typhoon season about July to October) | Short stone-grey rain jacket, **hood down** resting at the back of the neck, plain, no reflective strips, no logos; cropped charcoal trousers; matte neckerchief | Content theme P2. A label only, never a reason she "dressed for the weather" (bible 4.3) |
| **V3 濕冷版** damp cold in the north (roughly late October to December, northeast monsoon) | Long charcoal coat worn open over a cream knit; **cream scarf with a persimmon end stripe, draped with both ends hanging**; warm stone straight trousers; charcoal ankle boots. No snow, no maple leaves, no puffer coat, no gloves | Generators default to four-season scenes (`culture.md` 7.4) |
| 農曆新年 (2027-02-06) | **No clothing change.** No red garment. A red panel belongs in the lesson graphic, with text added and checked by the wife | Keeps the palette muted; collides with no other character's accent |
| **Deferred from the bible, not in the photoreal pilot** | The compact parasol (V1), the folded umbrella and rain boots (V2) | An object hooked on a strap invites a hand, a gift-umbrella taboo (`culture.md` 5.3) and a sun-protection implication. Revisit one at a time after the first approved set, with the wife's view |

### 4.3 The wardrobe lock

Only A, B, C and V1 to V3 exist. A new outfit needs a bible revision, the wife's approval and a fresh look-alike check (9.3). Seasonal variants change **garment shapes, not the palette**. The persimmon stays at or under about one tenth.

**Never:** a logo, text, tag, label or pattern; an all-black or all-white outfit (`culture.md` 5.5); a uniform or staff kit (apron, lab coat, lanyard, badge, name tag); a stylist, tailor or boutique-staff look; a school uniform (tie, bow, pleats, knee socks, a short skirt); sleepwear, swimwear or underwear-adjacent looks; sheer, tight, cropped, low-cut, off-shoulder or sleeveless-alone clothing; a dominant red, blue, green or yellow garment (party-colour read); a hood over the face; fortune-colour styling (C13).

**Modesty (Ground rule 3):** neckline covers the collarbone; sleeves reach the wrist (B: rolled to the elbow; V1: above the elbow at least); trousers to the ankle; the skirt below the knee; relaxed fit that does not outline the body; no belt or tie cinching the waist.

### 4.4 Palette in photographs

| Name | Hex | Use in a photo | Note |
|---|---|---|---|
| **Photo backdrop: dusty blush** 淡蜜桃色 (deeper) | `#EBCFC6` | Seamless studio backdrop | **Adjustment.** The bible's card ground `#F2DAD2` stays for cards, covers and lesson graphics. In a photo it is only 6.0 (CIE76, *computed*) from the cream garment, so cream would wash out; `#EBCFC6` is 9.7 from cream, 13.1 from 方寸's off-white (the bible ground was 9.5) and 21.0 from 步驟's studio grey. It is 4.0 from the bible ground, so card and photo still read as one family. Wife rules (12.1 item 7) |
| Cream 奶油白 | `#F4E8DF` | Knit top, shirt, tee, scarf | A peach-pink cast, never a yellow oat |
| Warm stone 暖灰 | `#B8AEA2` | Blazer, skirt, trousers, jacket | |
| Charcoal 炭灰 | `#3A3735` | Trousers, vest, coat, shoes | Not black |
| Persimmon 柿子橘 | `#CD8B6A` | The one accent | Muted terracotta-orange, never bright orange or red. 16.8 from the bible's flat skin swatch (*computed*), so it can blend with skin in shadow: keep it on fabric, matte, against cream or charcoal, and check at thumbnail size |
| Wheel hues and chip tints | per SC1, SC4 | Earring and chip ring | Muted; saturation at most the persimmon's |
| Hair | by eye | | Natural dark brown-black, not pure black, not dyed |
| Skin, lips | by eye | | Compared with R01, never with a hex. The bible's flat skin swatches (`#DDB38E`, `#C4946C`) were illustration fills and do not apply to photographs |

**Colour-read checks (wife and operator, on every master and new outfit):** party-colour read (no dominant saturated blue, green, teal or yellow; no blue-and-green or blue-and-white pairing); **rainbow read** (the earring is a small muted disc, not a flag, and the Pride window needs extra care, bible C4); **mourning read** (no all-white or all-black); and **the backdrop does not read as pink-childish or as skin-coloured** (bible 4.4 integration log).

---

## 5. Framing, pose and background rules

### 5.1 Hands: the top photoreal failure

Order of preference. Use the highest rung that works for the image.

1. **Out of frame.** Crop so no hand is in the picture (headshot, half-body, waist-up). Arms hang relaxed; hands fall below the crop line. The waist-up crop ends at the waist, just below the lowest blazer button.
2. **Inside pockets.** Both hands fully inside pockets, only sleeves (or, in outfit B, rolled-sleeve forearms) visible, no fingers or thumbs visible (knees-up and full body). Pockets must exist on the garment: blazer-and-trousers side pockets (A), in-seam skirt pockets (B), trouser pockets under the open coat (C).
3. **Simple and far.** Arms hanging naturally with relaxed fingers, only in a full-body image where hands are small, and only if every finger passes the 200% check (pack 9.1). **Not used for the master set.**

**Forbidden:** pointing (arrows are added in post); a hand touching her hair, earring, neckerchief, collar or face; **shown mid-tuck** (the hair is already tucked); holding the tote strap, the chip ring, a swatch, a fabric sample, a phone or any object; crossed or clasped arms; thumbs-up, V sign, heart or wave; hand on hip or chin; raised arms; an open-palm shrug or "stop" palm (can read as protest); walking with swinging arms; any close-up of a hand, nails or fingers.

If a kept image shows a hand with any defect, follow the hand fix procedure (pack 9.1). **A published hand defect is a tripwire** (8.3).

### 5.2 Framings and angles

| ID | Framing | Crop rule | Hands | Use |
|---|---|---|---|---|
| F1 | Headshot | Above the head, with margin, to the collarbone | none | Avatar source, reply images, expressions |
| F2 | Half-body | To the lower chest; the waist is not in frame | none | Quote cards, covers |
| F3 | **Waist-up (master)** | Ends at the waist | below frame | Default for most posts; R01 |
| F4 | Knees-up | Head to mid-thigh | in pockets | Beside a lesson panel; shows the chip ring |
| F5 | Full body | Head to shoes, 50 mm look | in pockets | Scale and silhouette check; rare |
| F6 | Avatar | 1:1 crop of F1; head about 60 to 70% of the height; face inside the central 70% | none | Profile picture with the "AI" chip |

Angles: **A1** front; **A2** three-quarter toward the viewer's left (about 40 degrees; this is the angle that shows the tucked left ear and the earring best); **A3** three-quarter toward the viewer's right (hair side; the right ear is mostly covered); **A4** side profile facing the viewer's left (left ear, earring and the tuck visible); **A5** back view (seen from behind, the tucked side and its earring are on the viewer's left). Camera always at eye level. **Forbidden:** low or high angles, wide-angle distortion, over-the-shoulder glances, glamour or body-emphasis framing, head tilt over 10 degrees.

Poses: **P1** standing, arms relaxed (F1 to F3); **P2** three-quarter (A2, A3); **P3** side and back (A4, A5); **P4** hands in pockets (F4, F5); **P5** glance toward the lesson: head turned **no more than about 15 degrees** toward the viewer's right, eyes directed to an empty space at the viewer's right, left earring still visible (F3). *Dropped from the bible for the pilot:* P08 and P09 (standing beside a dress form or flat-lay, which are composed in post from separate layers), and P12 walking (adds legs, arms and a street-style read). *Deferred:* seated.

Gaze: direct to the lens for portraits; off-camera only for P5, E03 and E04. Never a "caught unaware" look.

### 5.3 Expressions E01 to E10 for a real face

Names and uses are the bible's (5.4). Only brows, eyes and lips change. Lips stay **closed in every expression** (no parted lips), and **teeth never show**. No wide grin, laughing, tears, anger, wink, pout, kiss or tongue. One image per expression (several faces on one image come out as different people).

| ID | Name and use | Face |
|---|---|---|
| E01 | 平靜 neutral (default; avatar) | Calm, brows level, lips closed in a very slight smile |
| E02 | 說明 explaining | Brows level, head tilted about 5 degrees, lips closed and relaxed with the faintest lift of the chin, as if about to speak. **Lips are not parted** (a parted-lip pose is a banned sexualised cue, section 7), teeth not visible |
| E03 | 注意 pointing attention | Eyebrows slightly raised, eyes directed to an empty space at the viewer's right, lips closed |
| E04 | 比較 comparing | Eyes move toward one side, brows very slightly asymmetric, lips closed and flat |
| E05 | 微笑 mild smile | Soft closed-mouth smile, small smile lines at the eye corners |
| E06 | 不確定 uncertain | Small head tilt, lips pressed lightly together, brows slightly drawn in |
| E07 | 謹慎 careful | Brows drawn slightly inward, mouth level and closed |
| E08 | 更正 correcting | Small head bow of about 5 degrees, soft brows, lips closed |
| E09 | 輕鬆愉快 pleased, light | Small closed-mouth smile, eyes creasing slightly |
| E10 | 婉拒 polite decline | Slight tilt, lips pressed, soft brows; must read polite, not cold or angry |

### 5.4 No candid "my life" framing (Ground rules 1 and 4)

Not allowed: a phone in frame, a selfie or arm-length view, a **mirror or fitting-room shot (the classic outfit-of-the-day frame)**, motion blur, a snapshot crop, a timestamp or story-sticker look; a home, bed, closet, hanger, wardrobe, shopping bag, shop, street, café, MRT, market or commute; food or drink; any product; a street-style or "walking down the road" photo; catalogue-style model posing; **any location tag, map pin or geotag**; captions such as 「今日穿搭」, 「OOTD」, 「今天」, 「早上」, 「我在這裡」, 「get the look」; multi-image "day in the life" sets. The outfits are the same three, repeated, so they cannot be mistaken for a changing wardrobe.

### 5.5 Backgrounds

| ID | Background | Use |
|---|---|---|
| **B0** | **Plain dusty-blush seamless studio** (`#EBCFC6`), evenly lit, soft contact shadow for standing poses | Default, nearly everything, including the STOP 3 samples |
| B1 | The **cut-out** figure placed in a panel beside human-built flats, a faceless dress form or a wheel diagram | Lesson slides. Cut-out edges (hair strands) are checked at 200%; a halo or a hard edge fails. She is never composited into a photoreal scene, and never placed *on* the dress form or *in* a taught outfit |

Deferred: any photoreal Taiwan setting with her in it (騎樓, bus shelter, MRT exit, office, home). It invites "her life", a "visited this place" read, and the wrong-Taiwan-details tripwire. The bible's setting list (4.8) remains the checklist for **human-built 示意 plates that never contain her**. Never a real, named or recognisable place, landmark, shop, MRT station, street, number plate or address.

---

## 6. Lighting and photographic style ("Studio Look v2")

One look for every image, so a feed reads as one produced character and not a mix of photo styles. It differs from the two siblings' looks in backdrop colour and key-light side (10).

| Element | Setting (*assumption*; tools only approximate these) |
|---|---|
| Genre | Polished studio character-reference portrait. **Not** a phone snapshot, selfie, candid or editorial-glamour shot |
| Lens look | 85 mm for F1 to F3; 50 mm for F4 and F5; eye level; no wide-angle distortion |
| Key light | One large soft diffused source from the **front right** (the viewer's right), about 40 degrees, slightly above eye level. It lights the tucked left ear and the earring |
| Fill | Gentle, from the left; shadows soft, never harsh; no hard rim light |
| Colour | Neutral-warm balance; muted, low-saturation grade matching the palette |
| Surfaces | Matte skin with no shine and visible pores; fabric weave visible and matte; no satin sheen |
| Eyes | One soft window-shaped catchlight in each eye, upper right, same position in both |
| Background | B0, even, no gradient, no vignette |
| Formats | 4:5 for Instagram feed and Threads stills; 9:16 for Reels frames; 1:1 for avatars (check current platform guidance in the app, unverified) |
| Never | Filters, film grain, HDR, beauty filter or skin smoothing in editing, lens flare, bokeh lights, golden hour, "lifestyle" window light, dramatic or low-key lighting, glamour or beauty-campaign lighting, colour gels |

The pack carries this as a ready paragraph.

---

## 7. What NOT to render

Everything in bible 4.9 stays (except the "photorealism" bullet), plus:

- **Hands and fingers** in any visible form (5.1) other than the pocket pose; nails; any gesture.
- **Teeth**, open mouths, laughing, tears, tongue, kissing or pouting lips.
- **Other jewellery**, a watch, glasses, a phone, a held bag; any held object; any object hooked on a strap other than the chip ring.
- **Colour-analysis imagery (C2):** a swatch, chip, fabric or garment held against or draped near her face, "seasonal palette" drapes, skin-tone comparison, any framing that suggests her skin is a test card for a colour. Photoreal skin makes this temptation real. The chips hang on the ring and are never raised to the face.
- **Body imagery (Ground rule 6):** no measuring of a body, no body comparison or silhouette chart, no fitted clothing that outlines the body, no weight or "figure" framing, no skin close-ups, no dewy or glowing skin, no skincare, beauty or wellness look, no before-and-after.
- **Any sexualised cue (Ground rule 3):** glamour lighting, parted-lip pose, over-shoulder glance, low neckline, low camera angle, lying down, bed, swimwear, lingerie.
- **Candid and life framing** (5.4).
- **Another person**, a child or a pet; a mirror image; a second copy of her.
- **Real places, landmarks, shops, MRT, streets, number plates, addresses, signage.**
- **Brand logos** on clothing, shoes, bag, buttons, zips or the backdrop; a garment shown as a product; a "dupe" or counterfeit-looking item.
- **Generated Chinese, numerals, letters or hex codes** anywhere, including on the chip cards and the earring.
- **Money, charts, flags, party colours, maps,** red-blue or green-white pairings, election imagery (Ground rule 6). Rainbow imagery and a saturated full-spectrum wheel (C4).
- **A look-alike** of any real person, public or private, or of any existing virtual character.
- **Costume or credential:** stylist, tailor, boutique-staff, lab coat, uniform, apron, lanyard, name tag, badge.
- **Culture:** Indigenous patterns or costume, 客家花布 as generic decor, cheongsam, hanfu, kimono or hanbok as defaults, temple or religious dress, funeral objects, white-and-black pairings, sets of four.
- **Safety:** scooter riding, helmets, driving (C8).
- **Voice, video, lip-sync or animation** (not covered).

---

## 8. New risks of photoreal and mitigations

### 8.1 Risk table

Evidence comes from the research files and is not re-verified.

| # | Risk | Evidence | Mitigation | Owner |
|---|---|---|---|---|
| A | **Uncanny valley and visible AI defects**: hands, teeth, eyes, ears, earring wedges, a melted button or an asymmetric collar | IKEA Taiwan AI family image with distorted hands, ridiculed on Threads, 2026-06-01; the 民視 AI anchor whose lips and eyes viewers found unnatural (`competitors.md` 5, `culture.md` 6.1) | Framing that hides hands (5.1); closed-mouth default; natural-skin spec; the checklist (pack 5); 200% inspection; the wife's first look; reject, never retouch around a face; "near-real but wrong" is worse than clearly stylised (inference) | Operator, wife |
| B | **Mistaken for a real person** | A July 2025 AI influencer whose disclosure sat behind "Read More" caused mass confusion; the Guardian-reported brands using realistic AI "customers", relayed by TVBS, with 70% unable to tell real from fake (UK data, second-hand) (`competitors.md` 5, `culture.md` 6.1). A fashion account is read as human models by default | Disclosure in four places; persistent badge placed so a square crop cannot remove it (8.2); identical studio look; no real places; no candid framing (5.4); avatar chip; reply S07; a weekly 「是真人嗎」 count, and five or more in a week triggers a stronger label within 48 hours (`portfolio.md` 6.2) | Operator |
| C | **Likeness complaint** | Life8, July 2026: an apparel brand's AI product image drew a real model's claim that it copied his features; the brand apologised and stopped using it. Civil Code Art. 18 portrait-right commentary (`competitors.md` S7, `legal.md` 8.3; scope unverified). **This is the closest precedent to a fashion character** | Generic attributes only; no real person named in any prompt; no image-to-image from any photo; section 9 (face-crop reverse search, wife's local-public-figure check, stricter blind test); re-test after any model or tool change; take down within 24 hours, pause, an upheld complaint retires the face | Operator, wife, lawyer |
| D | **Instagram "AI-generated profile" label and recommendation limit** | Announced 2026-08-31; accounts prominently featuring a photorealistic AI person without the label may lose recommendation eligibility; Taiwan scope unconfirmed (`platforms.md` 2, 4.1, S27, S28). 色環 is fully on Meta (Instagram primary, Threads secondary), the known exposure of the pilots (bible header) | Apply the label when the account is created; check it on a Taiwan test account first (G6, now stricter); never open a second account to dodge it; reach effect unknown | Operator |
| E | **Platform AI labels** | Meta "AI info" from C2PA or IPTC signals or self-disclosure; YouTube altered-or-synthetic disclosure; Taiwan law makes AI-person disclosure mandatory for ads, with a reported NT$5 million Meta fine, date and articles unverified (`platforms.md` S29, S30, S40, S51) | Self-disclose on every post even if auto-detection would fire; do not strip metadata; an editor export may drop the markers, so never rely on auto-detection; use the AI-disclosure control on every boosted or partnership post (no boosting in the pilot) | Operator |
| F | **Drift toward youth, glamour or sexualisation** | Generator behaviour on women's fashion portraits (*inference*) | Age cues in 2; modest wardrobe (4.3); pack checklist rows 1 and 22; monthly sample of finals against R01; any glamour cue is a reject | Operator, wife |
| G | **The face changes when a tool updates** | Tools change often (*assumption*) | Record the model label in every provenance row; a model change is a new design; re-run section 9; keep the golden set read-only | Operator |
| H | **Ownership and licence** | Purely AI-generated images may lack copyright in Taiwan (`legal.md` 8.2). Commercial terms of the user's plans are **not checked** | Document human edits, keep layered files, no skin smoothing; register the name, not the face; lawyer question; no commercial use or client work until terms are recorded | User, lawyer |
| I | **Stereotype and idol template** | Generator defaults (`culture.md` 7.4) | Neutral wording (2); avoid-list; the wife's first look | Wife |
| J | **Video, voice, lip-sync** | A synthetic voice on a photoreal face reads as a deepfake; deepfake investment ads with officials' faces, Aug 2026 (`competitors.md` 5) | Out of scope: stills and captions only; a separate addendum and review before anything is made | User |
| K | **Reception unknown** | No Taiwan data on photoreal versus stylised (`culture.md` 6.2). Hypothesis H1 (stylised earns more saves per reach, `culture.md` 6.4) now has no stylised arm | Record saves and shares per reach and 「看起來好假」 comments at the week-6 review; the user can revisit. The stylised pack (`sehuan.md`) stays on file but the user rejected that look | User |
| L | **Three photoreal pilots look like one generator face** | Operator-run network risk (`portfolio.md` 3.3, Ground rule 8); Instagram hosts both 方寸 and 色環 | Section 10 near-pair note and test; separate chats per character; **never upload one character's image as a reference for another** | Operator, wife |
| M | **A photoreal body in a blazer reads as "she wore it" or as modelling a product** | Taiwan's recommendation genre is built on 上身 and 體驗文 (`culture.md` 1, 2.3); the FAS1 tripwire is any "I wore it" line or invented garment detail (`portfolio.md` 6.2) | Presenter not wearer (C1) stays absolute: her three outfits repeat unchanged and are never taught or named; no 「今日穿搭」 or 「get the look」 caption; no link to anything she wears; reply S06 variant (12.2); her garments are never reused as lesson garments; lesson flats stay human-built | Operator, wife |
| N | **Client 虛擬試穿示意 creative on a photoreal body** | Bible 8.5, 9.1 and open item 11: the lawyer has not said whether labelled try-on creative can mislead; a photoreal body makes it look like a real model in the brand's garment | **On hold.** The pack generates no client garment on her. Revisit only after the lawyer's answer and the licence terms are recorded | User, lawyer |
| O | **Photographic colour credibility** | The persona teaches colour; photographic colour shifts with light (bible 2.6 value 2) | A photo of her is never used as a colour reference in a lesson; lesson colours come from hex fills in the editor; keep the 色差 footer on colour-heavy slides | Operator |

### 8.2 Disclosure additions (on top of bible section 8)

- **Four places stay:** bio, first caption line, on-screen badge, platform label.
- **On-screen badge on every published image and every video frame.** Proposed wording: `AI 生成｜虛擬角色` ("AI-generated | virtual character") on any image that shows her; `AI 生成` on lesson slides without her; `搭配示意` and `示意圖` stay as in the bible. Solid charcoal pill with cream text, text height at least about 3.5% of the image height (*assumption*), inset at least 11% of the height from the top and bottom edges and at least 8% of the width from the sides (so a centred square crop of a 4:5 picture cannot remove it; see pipeline/qa-checklist.md D3), in the same corner every time. The "first second only" option is not used. The wife rules on the wording (12.1 item 8).
- **First caption line v2 (DRAFT):** 「【AI 虛擬角色】本篇由 AI 生成的虛擬角色「色環」發布，圖像為 AI 生成，並非真人。」 Gloss: *AI virtual character. This post is by the AI-generated virtual character 色環; the image is AI-generated and is not a real person.* This replaces 「圖為搭配示意」 on posts that show her, because "styling illustration" no longer says what a photoreal image needs to say. 「圖為搭配示意」 stays on lesson slides of flats.
- **Avatar:** 110 px cannot carry Chinese text. A small corner chip reading **`AI`** (Latin letters, added in post), the display name 「色環｜AI 虛擬角色」 and the account-level label.
- **Alt text** on every image (DRAFT): 「AI 生成的虛擬角色色環，非真人。」 Gloss: *AI-generated virtual character 色環, not a real person.*
- **Pinned post** (bible 8.1): add the line 「圖像為 AI 生成，並非真人；角色造型是設計，不是穿搭示範。」 (*The images are AI-generated and not of a real person; the character's outfits are a design, not an outfit demonstration.*)
- **Instagram:** the AI-generated-profile label from day one, plus the content-level disclosure on every post. **Threads:** same login; check that the label carries over (unverified).
- **Metadata and marks:** save as downloaded; do not strip metadata; do not screenshot (pack 7.5). Never remove, crop out, paint over or cover a visible mark or watermark that a tool adds, and never re-save or convert a file in order to lose its markers. If an editor export drops the markers, say so in the log and rely on the on-screen badge and the manual platform label.
- **No location tags, ever.**

### 8.3 Tripwires added to bible 7.3

| Event | Action |
|---|---|
| A **face, hand or earring defect** (extra or missing finger, merged teeth, mismatched ears or eyes, a wrong wedge count, garbled text on a chip card) reaches publication | Correct or take down within 24 hours; two in six weeks pauses the persona until the QA step is fixed (bible 7.3 AI-defect row) |
| A viewer says she looks like a named real person | Likeness procedure at once: take down within 24 hours, pause, re-run 9.3, retire the face if upheld |
| An image shows a hand holding anything, a location, a product, a mirror, or looks like a candid photo | Treated as a Ground rule 1 or 4 contact: take down within 24 hours, pause 7 days |
| An image of her carries a 「今日穿搭」-type caption, a link to her clothes, or a garment label | Treated as a testimony event (bible 7.3, first row) |
| A swatch or fabric held to her face, or any skin-tone talk | Treated as a C2 contact: take down within 24 hours |
| An image is published without the badge or without the platform label | Disclosure failure: fix within 24 hours, log; a repeat in the same quarter pauses the persona |
| The model label changes between two generations of the same image set | Stop; treat as a new design (8.1 row G) |

---

## 9. Adult-reading check, age-guess test and look-alike procedure (v2, stricter)

All thresholds are *assumptions* to calibrate. They are **stricter** than bible 4.7 and 5.7, which passed on "nobody under 25, nobody says student" and on a blind panel of 3 to 4.

### 9.1 Adult-reading check (every master, every new outfit, a sample each month)

Run at full size and at 64, 96 and 128 pixel head height.

| Check | Pass condition |
|---|---|
| Visible age | Reads about 30 to 35 at full size; still adult at 64 px |
| Face | Defined (not round or baby-fat) cheeks; faint age lines present; natural brow thickness; no enlarged eyes, blush circles or doll look |
| Skin | Visible texture; no airbrush |
| Hair and styling | Shoulder-length blunt cut, no pigtails, no clips or bows, no school-girl styling |
| Wardrobe | Adult blazer, knit, shirt and coat (4); no school-uniform cue in B; no airline or shop-staff cue in the neckerchief; no pastel candy colours |
| Posture | Upright and composed |
| Context | Plain studio only; no school, nursery or playground cue |
| Sexualisation | None: collarbone covered, no tight clothing, no glamour light, no parted-lip pose, no over-shoulder glance, no low camera angle, no body emphasis |
| Proportion (full body) | Head about one seventh of height; fail above one sixth |

### 9.2 Age-guess test

1. People: the wife plus **at least five others (six or more in all)**, a mix of ages including **at least two over 40**, **at least three living in Taiwan**, none of whom has seen the pictures. They do not follow or like any account and do not share the pictures.
2. Show each person, **one at a time, in a different random order, with no context** (do not say AI, character, mascot or account): R01 at full size, the same at about 110 px tall, the headshot at 64 px, and the avatar crop. Repeat once each for outfits B and C.
3. Ask only: **"How old is this person, and what might she do for a living?"** Write the number and the job word exactly.
4. **Hard fail:** any single guess **under 25**, a median guess **under 28**, or the word student (學生) or teenager.
5. **Warn (add the age-cue fix from pack 9.2 and retest):** a median of 28 or 29, or any single guess of 25 to 27.
6. **Target:** median 30 to 35.

### 9.3 Look-alike procedure

Done on every shortlisted master (at most three), on the final master again, on every new outfit family or hair or earring change, on any model or tool change, on a monthly sample of finals, annually, and on any complaint.

1. **Reverse-image search by hand, public tools only.** Use **Google Lens, Bing Visual Search and TinEye**, uploading the picture yourself, logged out of personal accounts, in a private window. No scripts, no scraping, no logins you would not normally use, **no face-recognition people-search services**. For each shortlisted image search: the head and shoulders; a tight face crop; an eyes-to-mouth crop; a three-quarter face; and, for the chosen final, the horizontally mirrored face and a crop of the tucked ear with the earring. Look at the first two pages of visual matches in each tool. Record tool, date, crop, and any result where **the operator or the wife thinks the character looks like a real person**, public or private. **These tools may return photos of real people: do not try to find out who anyone is, do not contact anyone, do not save or repost their photos.** A close match to a person is a stop-and-escalate event. Uploading shares an unpublished draft with each service; acceptable pre-launch, noted in the log. Screenshot result pages into `assets/sehuan/photoreal/lookalike/`.
2. **Text and stock-look searches** on generic terms in the same tools' image results: for example "woman shoulder-length black hair blazer studio portrait pink backdrop", "colour wheel earrings woman portrait", "segmented disc earrings". Compare the first page by eye. Generators sometimes reproduce a stock look, and the signature combination (a wheel earring plus a persimmon neckerchief) may already belong to another character or brand.
3. **Fashion-niche check.** Compare by eye with the AI-generated "model" images that apparel sellers use, in the first page of image results for generic descriptions. The Life8 dispute (8.1 row C) came from exactly this kind of image.
4. **The wife's local-public-figure check.** She looks at each shortlisted image and says whether the face resembles any local public figure (news presenter, actress, singer, model, influencer, politician, athlete, TV host) or anyone she knows personally, and writes the name or "the type". Names stay in the internal log only and never go into a prompt. **A resemblance to a politician is also a Ground rule 6 problem.** **No photo of any real person is ever placed beside the character for comparison.**
5. **Blind test.** The same people as 9.2, shown the picture with no context. Ask only: **"Who does this remind you of?"** (no names offered). Write the answer word for word.
6. **Existing virtual humans.** Compare side by side with the photoreal virtual influencers and Taiwan characters listed in `research/competitors.md` sections 3 and 4 (by file; the names do not go into any prompt, and nothing of theirs is ever uploaded to a generator). Similar hair, earring and neckerchief on a recognisable existing character is a fail.
7. **Fail** if the reverse search shows a real person who looks like her, **or** the wife names any real person, **or** *any one* tester names a real person (public or private) or a specific existing virtual character or influencer. "Someone, I can't say who" is recorded, not failed; two such answers trigger a follow-up question to the wife and an extra search round.
8. **Never repair a look-alike by editing.** Regenerate from the prompt with a changed attribute (face shape, hair length, parting side), or stop and tell Claude.
9. **Log** every result below. After a complaint: take down within 24 hours and pause until a documented check is complete.

| Check ID | Date | Candidate or asset | Tools, crops and searches | Search result | Wife's check | Blind-test answers | Age guesses | Verdict | Checked by |
|---|---|---|---|---|---|---|---|---|---|
| LA-PR-001 (empty) | | | | | | | | | |

### 9.4 Other tests (new in photoreal)

| Test | How | Pass |
|---|---|---|
| Uncanny read | Show five viewers the master at full and phone size, plus two closed-mouth smiling expressions (E05 and E09; no open-mouth or teeth-showing image is made). "Does anything look off, fake or creepy? Where?", then "How natural, 1 to 5?" | Median 4 or more, and no more than one person flags the eyes or the mouth. Two flagging the same area: fail and fix that area |
| Real-person read (information, not pass or fail) | "Is this a photo of a real person?" with no badge | Record the count. If four or five say yes, treat disclosure risk as high: largest badge and the strongest first line |
| Disclosure legibility (strict) | Show the image **with** badge and first caption line. "Is it clear whether this is a real person?" | All say it is an AI character. Any "not sure": enlarge or move the badge, strengthen the line, retest. Ground rule 1 depends on this |
| Same-person test | Six images mixed unlabelled (master, headshot, two expressions, outfit B, full body). "How many different people?" | Every viewer says one. A "two": find the drifting image and reject it |

---

## 10. Near-pair note: 方寸, 色環, 步驟

The three pilots must read as **three different people**, not a studio template (`portfolio.md` 3.3; Ground rule 8). The comparison uses the two sibling photoreal addenda as drafted on 2026-10-11 (方寸: woman, 32, softly squared face, low ponytail, thin walnut glasses, warm off-white backdrop, key light front left; 步驟: man, 28, long-oval face, short black side-parted hair, over-ear headphones, studio grey backdrop, key light front left). **Re-checked in the cross-pilot check of 2026-10-11** against the final text of both sibling addenda: the three-way table below now matches the one in each of them, and the plain-language version for the operator is `pipeline/image-pack/README-photoreal.md` section 3.

| | 方寸 v2 | **色環 v2 (this file)** | 步驟 v2 |
|---|---|---|---|
| Stated age | 32 | **30** | 28 |
| Presentation | Woman | **Woman-presenting** | Man |
| Face shape | Softly squared, rounded chin | **Oval, widest at cheekbones, narrow soft chin** | Long oval, defined jaw, straight chin |
| Hair | Dark brown-black, **pulled back in a low ponytail** | **Shoulder-length blunt, worn down, one side tucked behind the ear** | Short, side-parted |
| Face furniture | **Thin walnut glasses**, no jewellery | **Colour-wheel earrings** | Over-ear headphones |
| Skin undertone (by design, judged by eye) | Light-to-medium, slightly warm | **Medium, warm golden-beige** | Light-to-medium, neutral-to-warm |
| Palette | Oat, sage, walnut, cream belt | **Cream, warm stone, charcoal, persimmon** | Fog, slate, dusk, bone, charcoal |
| Signature | Glasses plus tick-mark belt | **Earring, persimmon accent, chip ring** | Headphones, rising-squares patch |
| Backdrop | Warm off-white `#F5F0E6` | **Dusty blush `#EBCFC6`** | Studio grey `#A9B0B8` |
| Key light | Front left | **Front right** | Front left |
| Platforms | Instagram, YouTube Shorts | **Instagram, Threads** | YouTube Shorts, Threads |

**Largest pair: 方寸 and 色環** (both woman-presenting, near in age, dark-haired, East Asian, both on Instagram, both in light neutral garments). Planned-hex distances (CIE76, *computed this session* with `personas/palette_check.py`; real photographs shift all of them):

| Pair | Distance | Reading |
|---|---|---|
| 色環 cream `#F4E8DF` and 方寸 oat `#E4D9C3` | 8.9 | Noticeable side by side. She never wears oat; her cream has a peach-pink cast |
| 色環 cream and 方寸 belt cream `#EFE6CF` | 7.4 | Noticeable |
| 色環 stone `#B8AEA2` and 方寸 sage `#A9B5A0` | 9.8 | Noticeable |
| 色環 stone and 方寸 putty `#CFC6B4` | 9.1 | Noticeable |
| 色環 charcoal `#3A3735` and 方寸 walnut `#6E5440` | 21.5 | Clearly different |
| 色環 photo backdrop `#EBCFC6` and 方寸 off-white | 13.1 | Clearly different (the bible ground was 9.5) |
| 色環 charcoal and 步驟 charcoal `#2B3038` | 8.4 | Noticeable; both are small masses, the cut and the face carry the difference |
| 色環 stone and 步驟 fog `#C9D1DA` | 17.7 | Clearly different |
| 色環 cream and 步驟 bone `#EEECE7` | 4.3 | Close (Threads). Garment cream against a photo, not a card ground; the faces, the hair and the backdrop differ |
| 色環 photo backdrop and 步驟 grey | 21.0 | Clearly different |

**Six-axis rule (adopted for all three designs, 2026-10-11).** Each photoreal character differs from each other on at least four of: face shape; hair (length, colour, style); eyewear, earrings, headphones or facial hair; apparent age; skin undertone; backdrop and light. **Apparent age is not counted for any pair**: the three visible bands overlap (28 to 33, 30 to 35, 30 to 36), generators cannot render a two-year gap, and under-reading is the main risk, so no design is pushed younger or older to separate it. 色環 against 方寸: face shape, hair, face furniture and backdrop and light differ clearly (four), and skin undertone is modest (a possible fifth). 色環 against 步驟: face shape (jaw and chin), hair, face furniture and backdrop and light differ clearly (four), skin undertone modest. Four with no spare margin for the largest pair (方寸 and 色環), so the side-by-side test below is not optional. The skin-undertone margin is thin, so the wife judges it by eye.

**Reserved for 色環** (the siblings should not use these): shoulder-length hair worn down, a wheel earring, a persimmon accent, a blush backdrop, key light from the front right. **Never on 色環:** glasses, a ponytail, oat, sage, walnut, headphones, a patch, a grey backdrop.

**Tests (when an R01 exists for each pilot).** (1) The three front waist-up images in one row at about 110 px tall, on a laptop and on a phone, unlabelled: can the wife tell them apart in two seconds with eyes half closed? (2) Show five viewers the three and ask "How many different people? Do any two look related?" **Pass:** three people, nobody sees a family resemblance. **Fail:** two or more say same person or sisters for any pair. **Fix by changing the design (a face-shape or hair attribute), not by editing.** (3) Generate each character in its own chat, and never upload one character's image as a reference for another (a cross-contaminated face is the commonest cause of "sisters").

`personas/palette_check.py` still models 色環 with the bible ground `#F2DAD2` and has no photo-backdrop entry; it was not edited. Re-run it with the real sampled values once the set exists.

---

## 11. Consistency sheet v2 (replaces bible section 5)

1. **Anchor.** Every follow-up image uses R01 as the reference, attached each time, plus at most two other golden images. **The only image of her you may ever upload is her own generated image** (and a plain colour swatch). Never a photograph of a real person, never another character's image, never a picture or fan art of any existing character.
2. **One change per generation:** one outfit, angle, expression or framing.
3. **Fresh chat for each follow-up** with R01 re-attached; if two images in a row fail the locked features, stop and re-anchor.
4. **Text-free output; the label is added in post.**
5. **Side rule.** The tucked side and the earring side are fixed by R01. If R01 comes out with the tuck on the viewer's left instead of the viewer's right, the master wins (if the wife is content) and the side is recorded once in the log; it never changes after that. **No image is ever flipped** (a flip moves the parting, the tuck and the faint smile asymmetry).
6. **Allowed human edits** are limited to: crop; colour correction to match the palette; removal of a stray mark; the badge, chip and text; and an **object-only** repair of the earring disc or a chip card (replaced with the hand-built wheel or a blank card layer, perspective and light matched). **No skin smoothing, no brightening, no reshaping, no hand repair, no face edits.** A "stray mark" never means a tool's visible AI mark or watermark, and a crop is never used to cut one out. Keep the layered file and the untouched original (the documented human contribution, `legal.md` 8.2).
7. **Golden set** (in `assets/sehuan/photoreal/`, read-only once approved): R01 master; R02 to R05 views; R06 headshot; R07 expressions; R08 framings; R09 outfits B and C; R10 seasons; R11 earring still; R12 chip-ring still; R13 glance; R14 avatar; R15 palette card (by hand); R16 badge and chip templates (by hand).
8. **Model and tool change = new design:** log the model label; re-run 9.1 to 9.3 before using the new output.
9. **Drift check every 4 weeks** (*assumption*): the latest three finals beside R01 at the same size; two failing locked features means regenerate from the golden set.
10. **Provenance:** one row per file, the same day (pack 7).

---

## 12. Changes the wife must rule on (and items for the user)

### 12.1 Wife

**Needed before R01 can be judged:** items 2, 3, 4, 5 and 7. The rest can wait for the first approved set. Until she rules, the pack runs the stated default.

| # | Question | Options and my recommendation |
|---|---|---|
| 1 | **Pronouns.** Keep name or 「這個角色」 and no 她 in third-person copy (my recommendation: it avoids claiming anything and the bible's 我 rules stay), or allow 她? | Wife decides |
| 2 | **Feature wording** in prompts: neutral "East Asian ..." (default), "... that read as Taiwanese", or "an ordinary adult you could plausibly see on an everyday street in a large East Asian city" (section 2). This is bible open item 5 | Recommend the neutral default |
| 3 | **Face.** Is it ordinary and natural, a calm 30 to 35, not an idol or 網美 template? Does she remind you of any local public figure, or anyone you know? Also: the face shape changed from the bible's "long-oval" to an oval that tapers to a narrow soft chin, to separate her from 步驟 and 方寸. Fine? | Run at the shortlist (9.3). A "yes" to resemblance fails the image. If she dislikes the face-shape change, keep long-oval and change something else |
| 4 | **Earring and colour read.** Does a muted twelve-segment disc read as a colour wheel, a rainbow flag, or a costume? Is 2.5 to 3 cm natural? At thumbnail size, any party-colour, rainbow or mourning impression? | If a flag: reduce saturation or size. If costume: a smaller disc |
| 5 | **Styling.** The persimmon neckerchief with the blazer and with the coat: natural, or airline-crew and shop-staff? Does outfit B (shirt, vest, midi skirt, tote) feel like a school uniform or a costume? Would a woman in her thirties in Taipei wear this? | If uniform: the fallbacks in section 3 |
| 6 | **Skin tone** (by eye): medium warm golden-beige, natural for an ordinary Taiwanese woman of 30, with no impression of whitening or tanning | Skin tone is never mentioned in copy (C2). Tell us only if it differs between images |
| 7 | **Backdrop.** Dusty blush `#EBCFC6` for photos (cards stay `#F2DAD2`). Too pink, childish, 少女感, or skin-coloured? Does the plain studio feel "lifeless" or "fake" given the user's complaint? | If pink-childish: a more neutral warm blush. If lifeless: a visibly staged set piece |
| 8 | **Wording.** Badge 「AI 生成｜虛擬角色」, first line v2, avatar chip, alt text and pinned-post line (8.2); J1 as 「最多十分之一」, J2 reworded and the S06 photoreal variant (12.2). Natural, or too heavy and 工商味? | Recommend as drafted |
| 9 | **Modesty and tone.** Relaxed fit, collarbone covered, ankle trousers, midi skirt below the knee, closed-toe summer shoes, no shorts. Right for Taiwan, or too stiff? Any glamour impression? | |
| 10 | **Lesson graphics beside a photoreal presenter.** The human-built flats and wheel diagram stay flat. Does a photoreal cut-out beside flat diagrams look natural or mismatched? | If mismatched, the user decides on a different treatment |
| 11 | **Two woman-presenting photoreal pilots on Instagram** (方寸 and 色環). Too similar? | Section 10 test; fix by changing design attributes |
| 12 | **Name fit:** 色環 for a photoreal woman. The reading test (bible 2.1, G3) is still open and is not decided here | |

### 12.2 Zh-TW drafts for the wife (all AI drafts)

| Item | Draft | English gloss |
|---|---|---|
| J1 wording | 「柿色最多佔十分之一，這是設計規則，不是心情。」 | "Persimmon takes at most one tenth. It's a design rule, not a mood." A cap, since a neckerchief is usually smaller |
| J2 replacement | 「我沒有衣櫃，連這圈色票也是 AI 生成的。」 | "I have no wardrobe; even this ring of colour chips is AI-generated." States a limit; claims no ownership |
| S06 photoreal variant (R-WHERE) | 「圖中的衣服是角色造型設計，不是實際商品，也沒有購買連結。想看真實款式的規格，請直接查品牌官方頁面～」 | "The clothes in the picture are the character's costume design, not a real product, and there is no buying link. For real specs, please check the brand's official page~" |
| Badge | 「AI 生成｜虛擬角色」 and 「AI 生成」 | "AI-generated, virtual character" and "AI-generated" |
| First line v2 | 「【AI 虛擬角色】本篇由 AI 生成的虛擬角色「色環」發布，圖像為 AI 生成，並非真人。」 | See 8.2 |
| Alt text | 「AI 生成的虛擬角色色環，非真人。」 | "AI-generated virtual character 色環, not a real person." |
| Pinned-post line | 「圖像為 AI 生成，並非真人；角色造型是設計，不是穿搭示範。」 | See 8.2 |

### 12.3 User and operator

1. **Licence terms are not checked.** Read the current commercial-use terms for the exact Gemini and ChatGPT plans, and record the date and the key sentence in every provenance row (`licence_notes`). Until then every image is internal design material and no client or sponsored work is made.
2. **Instagram label check (G6)** matters more now: test the "AI-generated profile" label on a Taiwan account before any 色環 post (`HUMAN_TODO.md` item 10).
3. **Confirm the interpretation:** "real people" is recorded as photoreal *AI* characters (`DECISIONS.md` 2026-10-11). If the user meant human presenters, that is a different business and must be raised.
4. **Cross-persona:** the siblings should reserve the differentiators in section 10; re-run the near-pair test when all three masters exist.
5. **LINE stickers and client try-on creative** (bible 9.1): the illustration route no longer applies to a photoreal face, and client 虛擬試穿示意 creative is on hold (8.1 row N). Revisit after the week-8 review and the lawyer's answer.
6. **Stale files not edited here:** the stylised pack `pipeline/image-pack/sehuan.md`, `pipeline/image-pack/README.md`, `personas/palette_check.py`, `DECISIONS.md` and `HUMAN_TODO.md`. Point to the photoreal pack when they are next revised.
7. **Time.** Hands-on time for the whole pack is about 7 to 9 hours (*assumption*) against a 6-hour weekly budget: plan two weeks, and do 色環 after 方寸 and 步驟.
