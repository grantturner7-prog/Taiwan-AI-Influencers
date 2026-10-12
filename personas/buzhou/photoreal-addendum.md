# 步驟 (buzhou): Visual identity v2, photoreal

Addendum to `personas/buzhou/bible.md`. Version 0.1 DRAFT, written 2026-10-11. Slug `buzhou` is still a placeholder (bible 2.2). Studio name 明說角色工作室 / Plainspoken Studio is provisional and uncleared.

## Read this first

- **Why this file exists.** On 2026-10-11 the user rejected the stylised look ("looks so fake, I need real people") and DECISIONS.md records the reading: **photorealistic AI-generated characters, still openly AI**. This is not a switch to human presenters. If the user meant hiring real human creators, that is a different business and must be raised with them.
- **Precedence.** BRIEF.md section 3 (ground rules) wins over everything. Then DECISIONS.md (2026-10-11 entry). Then this addendum, where section 0 below says it supersedes the bible. Everything else in the bible stands.
- **Nothing exists yet.** No photoreal image, account or recording. This file is the specification; the prompts and procedure the user runs are in `pipeline/image-pack/buzhou-photoreal.md`. Claude cannot generate photoreal images; the user runs Gemini and ChatGPT.
- **Labels.** *assumption* = my planning figure; *unverified* = could not confirm from a primary source; *computed* = calculated in this session; *idea only* = not cleared. Tool features (what Gemini or ChatGPT can do, what marks they add) are **hypotheses** until the user checks the live app. Commercial-licence terms of the user's subscriptions have **not** been checked.
- **Every zh-TW string is an AI draft for the wife.** English glosses are beside each one because the operator does not read Chinese.
- **Openly virtual is non-negotiable and photoreal makes it harder, not easier.** Nothing in this file is designed to make the character pass as a real human. Photoreal raises the disclosure burden (section 7).

---

## 0. What this supersedes, and what stays

### 0.1 Superseded (do not use the old text for the photoreal look)

| bible.md section | What changes |
|---|---|
| Header table, rows "Medium" and "Signature tell" | Medium is now photorealistic AI-generated studio imagery. The patch becomes a small sewn patch (2.2 here) |
| 1.1 status row "Style: Stylised, not photoreal", and the Precedence bullet that cites "stylised characters" | Replaced by DECISIONS.md 2026-10-11 and this file |
| 2.4 lore rows **Shape** ("flat planes", "staircase patch"), **Patch** ("a drawn, AI-made character", "doubles as disclosure"), **Props it carries** ("drawn props") and **Where it lives** ("Backgrounds are illustrations") | In photoreal the patch is only a recognition mark and **no longer works as a disclosure**. Disclosure rests on the stack in section 7.1. Backgrounds follow 4.4 here. The rows **Origin**, **Name logic**, **Headphones** (plugged into nothing), **Limits stated by design** and "Never invent" stay |
| 4 introduction ("Style is stylised, not photoreal") and the "designed out" list | Replaced by this file. The two designed-out items that still apply: the screen-face robot look and guru or "AI scientist" styling |
| **4.1 Face and build** (all of it, including "gender not stated") | Replaced by section 1 |
| **4.2 Styling and signature tell** | Patch rendering replaced by 2.2. The sentences on headphones and on clothing ("plain, practical, unbranded, no text, no logos, no uniform, no expert costume") stay |
| **4.3 Wardrobe** | Same IDs A, B, C and the same seasonal logic, now rendered as real fabric (section 3) |
| **4.4 Colour palette** | The eight swatches stay as the **wardrobe and prop colours**. Two changes: skin is no longer a flat swatch (1.3), and the **background becomes studio grey** instead of bone (5.2) |
| **4.5 Art medium and typography** | Medium replaced. The typography rule stays: on-image Chinese is never generated; it is typeset in post in a Taiwan-glyph font such as Noto Sans TC with the language set to zh-TW and checked by eye by the wife |
| **4.6 Thumbnail and PiP rules** | The rounded-square bone frame, "faces toward the content" and "never cover the interface" stay. The badge becomes persistent on every image (7.1) |
| **4.7 Adult-reading check** | Replaced by 8.1 and 8.2 (stricter) |
| **4.8 Recurring Taiwan settings** | Replaced by 4.4 here (neutral studio by default; generic 示意 sets only after sign-off) |
| **4.9 What NOT to render** | Extended by section 6. The old list still applies |
| **5 Character consistency sheet** (5.1 to 5.8, including the locked-features checklist 5.6, the same-face procedure 5.7 and the look-alike procedure inside it, and the R-list 5.8) | Replaced by the pack `pipeline/image-pack/buzhou-photoreal.md` and by 8.3 here. **5.9 provenance template stays** (the pack uses it) |
| **8.3 On-screen badge, 8.4 Platform label** | Amended by 7.1: badge on every image; platform AI label always ON for photoreal |
| Any wording "stylised", "drawn", "illustrated", "flat vector", "outline-free" anywhere in the bible | Superseded for the visual look |

### 0.2 Stays unchanged

- **Voice and language:** section 3 in full (register, "I" rules, Taiwan vocabulary, banned words, comment handling, the 20 sample lines).
- **Identity:** 2.1 name, 2.2 handles, 2.3 stated age 28 (design value only), 2.5 personality, 2.6 values, 2.7 boundaries, 2.8 running jokes (J2 needs a wife check, see 10).
- **Content pillars** (section 6), **Do and Don't** (7.1, 7.2), **tripwires** (7.3, plus the additions in section 7 here).
- **Disclosure lines** (section 8) except the two amendments above.
- **Monetisation and brand-safety** (section 9), **reviewer notes** (section 10), **gates** (1.2), the **palette family** (ink slate, dusk, fog, bone, charcoal) as wardrobe and prop colours.
- The limits stated by design: the character cannot operate a computer, has never used or worn anything, has no daily life. Photoreal images must never contradict that (section 4 and 6).

---

## 1. Face and build

All of this is **generic and original**. Nobody is described, copied or approximated. No feature below is a reference to any real person, performer, public figure, existing virtual character or the user's wife, and none may be added in a prompt (BRIEF ground rule 2).

### 1.1 Presentation and age

| Item | Spec |
|---|---|
| Presentation | **Man-presenting** adult. The bible's gender-neutral design is replaced (wife rules, section 10 item 1). Studio copy still refers to the character by name or as 這個角色 until she rules on pronouns |
| Stated age | **28** (design value only, never used for a life story) |
| Visible age target | Reads **about 28 to 33** (assumption). Should not read younger than the stated age (Ground rule 3: visible age about the stated age or older). Guesses are noisy, so the age-guess test (8.2) warns on a median of 28 or 29 and a single guess of 25 to 27, and fails any single guess under 25 or a median under 28 |
| Photoreal risk | Generators may skew young and smooth for East Asian male faces (hypothesis). The age cues in 1.5 and the stricter tests in section 8 exist for this reason |

### 1.2 Face

| Feature | Description (generic) |
|---|---|
| Overall | Ordinary adult face, everyday and unexaggerated. A plain, everyday look (no job or daily-life cue), not a glamour, idol, anime or beauty-retouched template |
| Face shape | Long oval, moderately defined jaw, straight and slightly square chin, medium forehead |
| Eyebrows | Straight, medium-thick, dark brown-black, natural and very slightly uneven |
| Eyes | Medium-sized (each about one fifth of the face width, carried over from bible 4.1), dark brown, almond-shaped, natural eyelids with a subtle single fold, calm level gaze, natural catchlights. Not oversized, not glassy |
| Nose | Medium length, moderate bridge, medium width |
| Mouth | Medium-full lips, relaxed. Closed by default |
| Ears | Natural, medium. Covered by the headphone cups when worn (see 2.1) |
| Facial hair | None. Clean-shaven, no heavy stubble |
| Eyewear | None |
| Distinguishing marks | None designed in (no mole, scar, dimple, gap teeth, tattoo). Deliberately unremarkable, which also helps the look-alike checks |
| What the face must not do | Look like a template idol face, look babyface, have exaggerated V-line jaw, doll-like symmetry, heavy double-eyelid surgery look, or any caricature of East Asian features (no "slanted eyes" wording anywhere) |

### 1.3 Skin, hair

| Item | Spec |
|---|---|
| Skin tone | Light-to-medium, neutral-to-warm beige, matte. Judged by eye by the wife, not by hex (a photo has lighting, so the bible's flat `#D8B190` and `#BE9371` no longer apply). No orange tan, no rosy pink cast, no grey cast |
| Skin texture | Natural fine texture: visible pores on nose and cheeks, faint shading under the eyes, slight natural unevenness. **No airbrushing, no glow, no plastic smoothness** |
| Skin and health imagery | Ground rule 6: no skin-care or "glowing complexion" look, no acne or skin-condition depiction, no before-and-after feel |
| Hair | Short black (very dark brown-black), about 4 to 6 cm on top, neat side parting, tapered sides and back, natural texture with a few loose strands, natural hairline, **not dyed**. The headphone band sits on top and may slightly press the hair, as real headphones do. The ordinary haircut must not be a trend cut copied from any pop-culture look; the wife checks |

### 1.4 Expression defaults

- **Default (E01):** calm, relaxed, lips closed with a very slight asymmetric smile (carried from the bible), steady gaze at the camera, eyebrows level.
- Ten-expression set carried over from bible 5.4, adapted for photoreal: restrained, **closed or barely parted lips, no teeth-baring grin, no laughing, no tears, no anger, no wink, no flirtatious look, no raised-palm gesture**. Teeth are the second photoreal failure after hands; the set keeps them out of frame wherever possible.
- Gaze to camera in most images. Off-camera gaze is allowed only for the E03 and E04 expressions.

### 1.5 Age cues (what makes him read as an adult of about 28 to 33)

Defined cheekbones and jaw; adult neck and shoulders; fine natural lines at the outer corners of the eyes; a faint line from nose to mouth corner when the face is relaxed; slight natural under-eye shading; natural hairline (no baby hairline); adult haircut; plain adult clothing; no school or student cues (no backpack, no uniform, no lanyard). A child-like softness, glassy skin or very large eyes fails the adult read (8.1).

### 1.6 Build

Slim-to-average build, natural shoulders (slightly broad is fine), upright relaxed posture, natural adult proportions (about 7 to 7.5 heads tall; assumption). No gym build, no muscle definition on display, no body comparison, no shirt-tight fit. No weight or body imagery of any kind (Ground rule 6).

### 1.7 Wording for region and ethnicity in generator prompts (wife decides)

The open item from the other pilots ("features that read as Taiwanese") applies here. This addendum and the pack use the **neutral** wording below. The wife may choose a different option (section 10 item 2).

| Option | Wording | Note |
|---|---|---|
| **N (default in the pack)** | "ordinary East Asian adult features, everyday and unexaggerated" | Describes an attribute, claims no nationality |
| L | N plus "plausibly local to Taiwan" | Only if the wife wants it. A generator cannot reliably do this and it risks stereotype. Not recommended by me |
| D | Drop the region; describe features only | Generators may default to another look. Then the wife checks the result for Taiwan plausibility |

Whatever the option, the wife's blind check is "does he look like an ordinary adult man you could meet in Taiwan, or like a template?" (pack section 9).

---

## 2. Signature constants (always present)

| # | Constant | Spec | Visible in |
|---|---|---|---|
| 1 | **Over-ear headphones** | Closed-back, **matte charcoal** (palette `#2B3038`), thin padded band, plain round-oval cups, fabric ear pads. **No logo, no text, no cable, no microphone, no lights, no metallic shine.** Worn on the head, cups over the ears, in every image. Around the neck is allowed in a few full-body shots (ears then visible and must match) | Every framing, including headshots and avatar |
| 2 | **Chest patch** (three rising columns of squares) | See 2.2 | Half-body and below. Not in headshots or avatar crops cut above the chest |
| 3 | **Same face, hair, build** | Section 1 | Everywhere |
| 4 | **House studio look** | Section 5 | Everywhere |
| 5 | **None of: jewellery, watch, glasses, beard, tattoo, visible hands** | Nothing is designed for these, so none may appear | Everywhere |
| 6 | **Added in post, never generated:** the badge (「AI 生成｜虛擬角色」 on any image that shows him; 「AI」 tag on avatars), any other Chinese text, date stamps | Section 7.1 | Every published image |

### 2.1 Headphones: detail

The headphones are the **only constant visible in every crop**, so they carry recognition. Photoreal failure modes: earbuds, gaming headset with boom mic, visible cable, glowing ring, brand mark on the cup, different shape from image to image, or cups that fuse into the ears or hair. The check list is in the pack, section 5. Running joke J2 (「耳機沒接線」) still fits: no cable is drawn, no cable may be rendered.

### 2.2 Patch: detail (this replaces bible 4.2 for rendering)

| Item | Spec |
|---|---|
| Object | A **small rectangular sewn woven patch**, about 4 cm wide (assumption), flat, matte, **not an app icon, not a logo** |
| Backing and edge | Bone `#EEECE7` backing with a thin **charcoal** stitched border. The charcoal edge is a small addition so the patch stays readable on the light fog jacket at small sizes (bone against fog is only about 13 apart, computed with the CIE76 formula in `personas/palette_check.py`). The wife may rule against it (section 10 item 5) |
| Design | A rising staircase of **six flat squares in three columns that share a bottom edge: one square, two squares, three squares, left to right as the viewer sees it**, so the shape rises to the right. Left column fog `#C9D1DA`, middle column dusk `#6F8197`, right column ink slate `#3B4A5C`. **Not a 2 by 2 grid, no digits, no letters, no QR look** (bible 4.2 cautions stay) |
| Where | Chest of the outermost layer, on the **wearer's left (the viewer's right when he faces the camera)**. If the chosen master shows it on the other side, the master wins and the side is recorded once; it never changes after that and no image is ever flipped (a flip moves the patch and the hair parting) |
| Fallback if a generator cannot hold six squares at patch size (hypothesis: small objects are unreliable) | The **three-bar version**: the same staircase outline built from three bottom-aligned bars of rising height in the same three colours, with no internal square lines. Using it needs the operator's log note and the wife's approval, and a fresh look-alike pass on the patch (logo check) |
| Alternative form | A small enamel pin instead of a sewn patch. **Not the default**: enamel adds shine and reflections that generators garble and that read as a brand pin. Allowed only if sewn patches fail three rounds; it is a change to log |
| Not a disclosure | In the stylised bible the patch was a visible "not a photo" tag. **In photoreal it is not.** Do not describe it as a disclosure anywhere |

---

## 3. Wardrobe lock

Only these IDs exist. A new outfit needs a revision of this file and the wife's approval. The headphones and the patch appear in **every** outfit. No real garment brand, no logo, no text, no stripes or ticks on any item. Wardrobe is modest, adult and practical. Fabrics are matte. The prompts name colours in words; hex is for the wife's and operator's colour checks (hex codes in a prompt tend to be printed into the image, and photographic lighting changes the colour anyway).

| ID | Outfit | Photoreal description | Use |
|---|---|---|---|
| **A** (default) | Workday | Boxy light cool-grey (fog) coach-style jacket in matte fabric, zipped about two thirds, over a plain crew-neck tee in muted ink-slate blue-grey; charcoal straight-leg trousers; plain low-top off-white (bone) sneakers with no stripes or marks. Patch on the jacket chest | PiP, avatar, thumbnails, most posts |
| **B** | Studio knit | Fine-gauge crew-neck knit in muted ink slate, no jacket; the same patch sewn on the chest; charcoal trousers | Close-ups, title cards, cool-season videos |
| **C** | Warm-day shirt | Short-sleeve collared shirt in muted dusk grey-blue in a matte lightweight cotton, **fastened so that at most the top button is open** (modest; no chest showing), one cuff fold on each sleeve; a small flat chest pocket on the wearer's left carrying the patch; charcoal trousers | Hot, humid weather |

| Seasonal variant (Taiwan climate; culture.md 7.4) | Change |
|---|---|
| Plum rain and rainy season (about May to June, and any rainy backdrop) | Outfit A plus a light matte hooded rain shell in dusk grey-blue, hood down, no reflective strips, no logos, patch on the shell chest. **No umbrella in the character's hands** (hands out of frame; an umbrella is also a parting symbol if shown as a gift, culture.md 5.3). If an umbrella is ever shown it is a separate still-life image, plain charcoal, closed |
| Hot, humid summer | Outfit C, no jacket. No sweat, no fabric-performance claims (排汗, 透氣, 抗UV) anywhere |
| Cool, damp season (northeast monsoon, roughly late October to early spring in the north) | Outfit B, or A plus a lightweight charcoal padded vest over the jacket with the patch on the vest. No heavy snow coat, no maple-leaf or Japanese-autumn styling (generators default to it) |
| 農曆新年 (2027-02-06) | No costume change. No all-black or all-white outfit (culture.md 5.5). No red clothing (it would collide with other characters' accents). A single small warm card or envelope may exist only as a separate graphic with the wife's approval, never held |

**Colour-read note for the wife.** The set is grey on grey (fog jacket, slate tee, charcoal trousers, grey backdrop). Check it does not read as 喪服 (mourning wear), a party colour (blue-and-white slogan layouts, green, or election blocking), or gloomy. Ink slate plus dusk stays at or below about 40% of the visible area (bible 4.4 rule, kept).

---

## 4. Framing and pose rules

### 4.1 Allowed framings (every one keeps hands out of frame or hidden)

| ID | Framing | Hands | Patch visible? |
|---|---|---|---|
| F1 | **Headshot**: just above the head to the top of the chest | Out of frame | Maybe (edge only) |
| F2 | **Half-body**: just above the head down to the belt line, arms relaxed at his sides with the frame ending above the hands | Below the frame edge | Yes |
| F3 | **Waist-up**: just above the head to the hips, **both hands inside the jacket or trouser pockets, thumbs not hooked out, no fingers visible** | Hidden in pockets | Yes |
| F4 | **Full-body standing**: front, three-quarter, side. Both hands in pockets, feet fully visible, plain sneakers | Hidden in pockets | Yes (front, three-quarter) |
| F5 | **PiP bust**: chest-up, turned slightly toward the content, figure about 80% of the frame height, inside the rounded-square bone frame | Out of frame | Yes |
| F6 | **Avatar crop**: tight head and shoulders, square, face inside the central 70% so a circular crop keeps it (assumption; check each platform's current crop guidance) | Out of frame | Not required |

The camera is at **eye level**. Standing or head-and-shoulders only. Seated and walking poses from the bible (P08, P12) are **dropped for the pilot weeks**: seated and walking add hands, knees and feet failures and invite a "daily life" read. They can return after the first approved set, one at a time.

### 4.2 Dropped from the bible (they need hands)

P09 holding the checklist card, P10 holding the date-stamp card, P11 pointing. The checklist card, the date stamp and any pointer are **graphics added beside or over the character in editing**, not held objects.

### 4.3 Never a candid "my life" frame (Ground rule 1 and 4)

No phone-photo look (no flash, no handheld blur, no wide-angle selfie distortion, no arm-length selfie perspective), no mirror selfie, no over-the-shoulder street shot, no table-top café shot, no "just woke up", "on my way", "my desk", "my setup", "today I" framing. No location tag on any post. No image is ever described, captioned or tagged as a place he visited. No time-of-day storytelling (no morning-light, no golden hour). The studio look is deliberately **composed and a bit formal** so that nobody mistakes it for a snapshot of a real person's day.

### 4.4 Backgrounds

| Type | Rule |
|---|---|
| **Default: neutral studio** | Seamless studio backdrop in mid-light neutral cool grey (5.2), soft falloff, nothing else in frame. Used for everything in the pilot weeks, including STOP 3 samples |
| **Generic 示意 sets (later, wife's sign-off first)** | Three at most to begin with: a plain desk corner, an office partition, a study room. Each is **generic and unnamed**: no real place, no real shop or brand, no signs, no screens, no menu, no plates. Each use carries the badge (「AI 生成｜示意圖」 on a plate without him, 「AI 生成｜虛擬角色」 on an image that places him in it) and a 「示意」 label (typeset in post). He stands near the set, hands in pockets, **touching nothing and using nothing** (the bible's rule that the character cannot operate a computer stands). The set is never called his desk, room or café |
| **Never** | Real, named or recognisable places; MRT stations or maps; temples; night markets; convenience stores; anything with legible text; food or drink; a place that implies "I was here" |
| Taiwan-ness of sets | Sockets (Type A and B), window grille (鐵窗), split air conditioner, shoes-off floor, right-hand traffic and helmets if scooters appear. Run the culture.md 7.6 checklist; the wife is the checker |

### 4.5 Hands: the rule in one line

**A hand that is not in the frame cannot be wrong.** Frame to cut them off or hide them in pockets. If a hand appears, the fix ladder (regenerate, targeted edit, crop, reject) is in the pack, section 10.2. Never repair a hand by compositing a photo of a real person's hand, and never hand-draw fingers.

---

## 5. Lighting and photographic style (the house look)

One look, used for every post, so he reads as one consistent produced character and not as a mix of random snapshots.

### 5.1 Parameters

| Parameter | Spec |
|---|---|
| Genre | Studio portrait photograph, composed and plain |
| Lens look | About 85 mm equivalent, moderate depth of field (an f/2.8 look), sharp on the eyes, no wide-angle distortion |
| Camera | Eye level, straight on or a slight turn of the body, face toward the camera |
| Key light | One large soft source from the front left (the viewer's left), roughly 45 degrees, slightly above eye level |
| Fill | Gentle, so shadows stay soft and readable. No hard rim light, no colour gels, no neon, no backlight glow |
| White balance | Neutral daylight (about 5200 to 5600 K; assumption) |
| Colour and grade | Muted natural colour, no filter, no teal-orange grade, no HDR, no lens flare, no heavy vignette, no heavy film grain |
| Retouching | **None implied.** Natural skin texture stays. Editing limited to crop, exposure and white balance, and removing a stray defect |
| Framing margin | Headroom about a tenth of the frame height in half-body; badge-safe corner left clear |
| Aspect ratios | 4:5 portrait for Instagram and Threads stills; 1:1 for avatars; 9:16 or 16:9 as the PiP source is cut for video (assumption; platform sizes unverified) |

### 5.2 Backdrop colour (adjusted from the bible)

The bible used bone `#EEECE7` as the neutral ground. In a photo the backdrop fills more than half the frame, so it now matters for telling the three pilots apart. **Studio grey `#A9B0B8`** (mid-light, cool-leaning, saturation about 10%, so it is a grey and not a blue; computed) replaces bone as the **photo backdrop**. Bone stays for the PiP frame, thumbnails, patch backing and sneakers.

| Studio grey `#A9B0B8` against | CIE76 distance (computed with the functions in `personas/palette_check.py`) |
|---|---|
| 方寸 off-white `#F5F0E6` (YouTube, shares a platform) | 25.6 |
| 色環 dusty-blush photo backdrop `#EBCFC6` (Threads, shares a platform) | 21.0 (the card ground `#F2DAD2` is 22.4) |
| 規格 paper `#DEE3E1` | 19.1 |
| 歸位 mist `#E7E5EB` | 20.0 |
| 里程 concrete `#CFD2D0` | 13.6 |
| Own jacket fog `#C9D1DA` | 12.0 (the jacket reads lighter than the backdrop; enough to separate it) |
| Bone, for comparison, against 方寸 off-white | 3.2 (the near pair the register accepted; this change removes it for photos) |

The other persona grounds not listed (接話, 轉乘, 歲歲, 等一下) are 20.5 to 29.1 away. Against other personas' **figure** colours, the register shows two close ones: 歸位 light steel `#A9A7B3` is 4.8 from the studio grey (both on YouTube; 歸位 is lawyer-gated, a later wave, and stylised, so the risk is low) and 規格 mist `#BFC4C2` is 9.0 (Instagram, not a platform 步驟 posts on). Both are computed with `personas/palette_check.py`; the 110 px test in section 9 covers them when those personas have images.

These are hex-level numbers. Real photos vary with lighting, so the working check is by eye plus an eyedropper on a flat area of backdrop: within about 15 on each of R, G and B of the target is a pass, up to 30 is "regrade", beyond that regenerate (assumption, borrowed from the stylised pack). `personas/palette_check.py` has not been edited; its `buzhou` entry still lists bone as the ground. Re-run it with the new ground when the wife accepts (section 11).

---

## 6. What NOT to render

Everything in bible 4.9 still applies. Additions and photoreal-specific items:

| Never render | Why |
|---|---|
| Any real person's face or a resemblance to one; any prompt that names a real person, performer, public figure, existing virtual character or the user's wife; any uploaded photo of a real person (even as a lighting, pose, hair or outfit reference) | BRIEF ground rule 2; likeness complaints (Life8, competitors.md section 5) |
| Visible hands, fingers, thumbs hooked from pockets; hands holding anything | The top photoreal failure (IKEA Taiwan hands, competitors.md S8). Design-out |
| Phone, laptop, keyboard, cup, food, drink, a named product held or used, a wearable-testing scene | Ground rule 4: no lived experience; the character cannot operate a computer |
| Candid or selfie framing; mirror shots; "day in my life" scenes; any location tag or real place | Ground rule 1 (must not pass as a real person's life) |
| Jewellery, watch, glasses, beard, tattoo, makeup emphasis | Not designed; consistency |
| Logos or brand marks on headphones, sneakers, zip pulls, tags; legible text; numerals on the patch; licence plates | Ground rule rules; garbling |
| Skin-care glow, "glass skin", before-and-after cues, scars or acne shown as a condition, gym or body imagery, scales, tape measures | Ground rule 6: no health, body, weight or skin-efficacy imagery |
| Money, coins, banknotes, trading charts, income screens, crypto symbols | Ground rule 6 |
| Flags, maps, party colours (blue-and-white slogan layouts, green), election imagery, red-star icons | Ground rule 6; elections recalled for 2026-11-28 (unverified) |
| Sexualised pose or styling, open shirt, bare skin below the collarbone, tight clothing, wet or glossy look | Ground rule 3 |
| School uniform, backpack, lanyard, lab coat, suit-and-badge or any expert costume; official, police, bank or agency styling | Adult read; implied credential; fraud association (competitors.md section 5) |
| Idol, anime, glamour, K-pop or "soft boy" template looks; caricatured East Asian features | Taiwan realism; stereotype |
| Cliché AI imagery: glowing brain, circuits, blue digital rain, robot or screen face | Assistant-mascot look; also pushes palette toward saturated blue |
| Other people in frame, crowds, partners, children | Not designed; likeness and consent exposure |
| Any image whose face visibly differs from the master | Treated as a new face: fails until it passes the full look-alike check (8.3) |

---

## 7. New risks of photoreal and their mitigations

The stylised choice was made partly to avoid these (DECISIONS STOP 2 decision 3). They are accepted now by the user's decision, so each needs a control. Evidence is from `research/` (dated 2026-10-10, mostly secondary and unverified).

| # | Risk | Evidence | Mitigation | Owner |
|---|---|---|---|---|
| 1 | **Uncanny valley and visible AI errors** draw ridicule | IKEA Taiwan AI hands, 2026-06-01; the 民視 AI anchor whose lips and eyes viewers found unnatural (culture.md 6.1) | Hands never shown; restrained expressions; teeth out of frame; eye, ear and skin checks; the uncanny test (8.4); reject, never retouch around; stills before any animation | Operator, wife |
| 2 | **Mistaken for a real person** | A 2025 AI influencer whose bio disclosure sat behind "Read More" caused mass confusion (competitors.md S45); the Guardian-reported brands using realistic AI "customers" (relayed by TVBS, S1 to S3) | The disclosure stack (7.1); no candid framing, no location tags, no daily-life posts (section 4); the disclosure-legibility test (8.4); reply R1 every time; tripwire below | Operator |
| 3 | **Likeness complaint** (a generator face can resemble a real person without anyone intending it) | Life8, July 2026: apology and withdrawal after a model said an AI image copied his features; Civil Code Art. 18 portrait right commentary (competitors.md S7, legal.md 8.3; recalled, unverified) | The stricter look-alike procedure (8.3); only the character's own images are ever uploaded; full provenance (prompt, tool, date) for every asset; take down within 24 hours of a credible claim (portfolio.md 6.2); lawyer question 20 (legal.md) | Operator, wife, lawyer |
| 4 | **Instagram "AI-generated profile" label and recommendation limit**; Taiwan scope unverified | Announced 2026-08-31 for accounts prominently featuring a photorealistic AI person; unlabelled accounts may lose recommendation eligibility (platforms.md 4.1, S27, S28) | Apply the label from day one if offered; test on a Taiwan test account first (HUMAN_TODO 10); label the Instagram account that Threads needs (bible 2.2). Plan as if it applies | User |
| 5 | **Platform AI labels on realistic people** | YouTube labels significant photorealistic AI use automatically from May 2026 and can add labels itself; Meta requires the disclosure tool for organic photorealistic video and uses C2PA/IPTC signals (platforms.md 4.1, 4.3) | Platform label **always ON** for photoreal (7.1); never strip metadata; dispute nothing | Operator |
| 6 | **Taiwan's AI-person ad disclosure duty** | Fraud Crime Hazard Prevention Act requires ad platforms to disclose AI-generated personal images; Meta reportedly fined NT$5 million (platforms.md S51; date and articles unverified) | No paid ads or boosted posts with the face until the AI-disclosure control and the lawyer's answers are in place; use the control on every boosted or partnership post | User, lawyer |
| 7 | **An AI face already carries fraud associations in Taiwan** | Deepfake investment ads using officials' faces, August 2026; deepfake doctors (competitors.md section 5) | Stay in the tools niche; no money, finance or health talk; no uniform, badge or credential look; the existing tripwire (asking viewers for personal data) is treated as higher severity with a face | Operator |
| 8 | **Synthetic voice or lip-sync on a photoreal face** is the closest thing to a deepfake | Same evidence; voice decision G5 is still open | **Stills and captions only in the pilot weeks.** No talking, lip-synced or voice-cloned video of the photoreal face until G5 is decided and a separate test passes; if ever used, the platform label is ON and the voice resembles no real person | User |
| 9 | **Demand and trust may be weaker than stylised** | Hypothesis H1 (stylised earns more saves than photoreal, culture.md 6.4); no Taiwan data on photoreal versus stylised (culture.md 6.2) | Treat the first 6 weeks as the test. Track 是真人嗎 comments, uncanny or "fake" comments, saves and shares per reach. Keep the code-drawn stylised art (`assets/buzhou/art/`, v0.1) as the fallback; **never mix both looks on one account** (they would read as two characters) | User |
| 10 | **Copyright and licence** | AI-only images may lack copyright in Taiwan (legal.md 8.2, unverified). Commercial terms of the user's plans not checked | Keep prompts, selection, edits and the log as the human-authorship record; read and record the terms before any commercial use (pack section 7) | Operator, lawyer |
| 11 | **Stereotype or default template face** | culture.md 7.4: generators default to an idol or foreign look | Neutral wording (1.7); the wife's blind check; no exaggerated feature wording | Wife |
| 12 | **Face drift across images** | Consistency is harder in photoreal than flat art (hypothesis) | One master as the reference; character lock; restart from the master, never from a drifted image; consistency test (8.5) | Operator |

### 7.1 Disclosure stack for photoreal (amends bible 8.3 and 8.4)

1. **Bio** (unchanged, bible 8.1): 「AI 虛擬角色」 and the studio name.
2. **First caption line (proposed v2, DRAFT for the wife):** 「【AI 虛擬角色】本篇由 AI 生成的虛擬角色「步驟」發布。圖像為 AI 生成，並非真人。」 (Gloss: AI virtual character; this post is by the AI-generated virtual character 步驟; the image is AI-generated and is not a real person.) This replaces 「圖為示意」 on photoreal posts, because "illustrative" no longer says what a photoreal image needs to say.
3. **On-screen badge:** 「AI 生成｜虛擬角色」 ("AI-generated | virtual character") on **every** image that shows him, and 「AI 生成｜示意圖」 on a plate without him, and on every frame of any video in which he appears (the bible's "first second only" option is dropped for photoreal). Typeset in post, never generated, in the same fixed corner every time, clear of platform controls. **Size and position now follow 方寸 and 色環 (aligned in the cross-pilot check of 2026-10-11):** text height at least about 3.5% of the image height (*assumption*), inset at least 11% of the height from the top and bottom edges and at least 8% of the width from the sides (so a centred square crop of a 4:5 picture cannot remove it; see pipeline/qa-checklist.md D3). (The earlier "about 12% of image width" rule and the shorter wording 「AI 生成」 are replaced: the longer wording says "virtual character" like the other two pilots, and the old size was smaller than theirs and had no crop-safe inset.) On avatars a small 「AI」 tag. The wife checks every character.
4. **Platform label:** the platform's AI-content label is **always ON** for photoreal images and video of him. The bible 8.4 allowance that a stylised animated character "may be exempt" no longer applies. Instagram: the "AI-generated profile" label if it exists for Taiwan accounts.
5. **Metadata:** keep it. Do not strip provenance data or visible tool marks (pack section 8).
6. **Never:** a location tag, a "candid" caption, or a claim of presence. Voice stays 「我」 for explaining, never for experience (bible 3.2).

### 7.2 Added tripwires (proposed; portfolio.md 6.2 stands as written)

| Event | Action |
|---|---|
| Three or more "是真人嗎" or "is this a real person" comments in the first two weeks, or five in any week (portfolio.md 6.2) | Strengthen the first-line and badge within 48 hours; consider enlarging the badge |
| A credible look-alike claim or a person who says it is their face | Take down within 24 hours, pause, re-run 8.3, log. An upheld complaint retires the face (portfolio.md 6.2) |
| An image published with a visible hand error, garbled text, a logo or a wrong patch | Same as portfolio.md 6.2 garbled-text rule: correct within 24 hours; two in six weeks pauses until the QA step is fixed |
| An image published without the badge or without the platform label | Disclosure failure: fix within 24 hours, log; a repeat in the same quarter pauses the persona (bible 7.3) |

---

## 8. Checks: adult reading, age guess, look-alike, uncanny and real-person read, consistency

All stricter than the stylised bible (4.7, 5.7). The pack, section 6, turns these into steps and logs.

| Check | Stylised bible | Photoreal (this file) |
|---|---|---|
| Age-guess pass | Wife guesses 25 or older, no "student" or "young" | **Same rule as 方寸 and 色環 (aligned in the cross-pilot check of 2026-10-11):** no single guess under 25; panel median 28 or older (28 is his stated age); no "student" or "young" word. Target median 28 to 33 |
| Panel size | Wife plus 2 or 3 trusted people | Wife plus **at least 5**, at least 3 living in Taiwan, mixed ages |
| Look-alike search | Reverse search on the master and 3 variants | **Face crops** (front, three-quarter, profile) as well as full images; three tools; logged out; plus a stock-look check |
| Wife's resemblance check | Not specified beyond the panel | **Wife looks for resemblance to any local public figure** (entertainment, news, sport, politics, online creators) and to anyone she knows |
| Resemblance to a politician | Not specified | Counts as a fail (Ground rule 6 and the election window) |
| Disclosure legibility | Not tested | New test: viewers shown the badge and first line must all understand it is AI |
| Uncanny read | Not tested | New test |
| Re-runs | Before launch, week 6, redesign, complaint | Same, plus any image whose face visibly drifts |

### 8.1 Adult-reading check (replaces bible 4.7)

Run on the master and on each new framing, at full size and at **64, 96 and 128 pixel head height**:

1. The age cues of 1.5 are present; the face has no baby softness, glassy skin, oversized eyes or rounded cheeks.
2. Neck, jaw, shoulders and hairline read adult.
3. Clothing is practical adult wear; no school or student cue.
4. Pose is neutral; no sexualised pose, no revealing or tight garment, no bare skin below the collarbone.
5. At 64 px he still does not read as a student or a teenager.
6. Fail any item: reject the image. **Do not retouch around it.** A mild adult-reading fail across several images is fixed in the prompt (pack section 10), not in the editor.

### 8.2 Age-guess test (stricter)

1. Ask the wife first, alone, before she knows the design age. Say only: "Write one number for how old you think this person is and one word for what he does. There are no right answers." Full size first, then the 96 px version.
2. Repeat with **5 or more others** (six or more in all), one at a time, same words; at least 3 living in Taiwan and at least two over 40.
3. **Hard fail:** any single guess (the wife's or the panel's) **under 25**, a median guess **under 28**, or the word student or young (學生, 年輕, 童顏). Reject the image and go back to the shortlist.
4. **Warn (hold):** a median of 28 or 29, or any single guess of 25 to 27. Do not approve. Regenerate with stronger age cues (pack section 10), retest with the same people plus two new ones.
5. **Pass:** none of the above. Target: median 28 to 33. (Before 2026-10-11 this file accepted a median of 27 and tolerated one guess under 25; that was looser than the other two pilots and Ground rule 3 asks for visible age about the stated age or older.)

### 8.3 Look-alike procedure (stricter; replaces the one inside bible 5.7)

Run on the master and again on any redesign. Log each run as `LA-PR-001`, `LA-PR-002` ... in `personas/buzhou/lookalike_log.md` (the file does not exist yet; the pack section 6.2 has the template). Only the studio's own images are ever uploaded anywhere.

1. **Reverse-image search by hand, with face crops.** Crop from the master and from three variants: a tight front face, a three-quarter face and a profile, plus the full half-body. Search each in **Google Lens, Bing Visual Search and TinEye**, one image at a time, in a logged-out private window, no scripts, no scraping, no login. Read at least the first two screens of visually similar results. Record date, tool, the page address and a one-line description of any close match. **These tools may return photos of real people: do not try to find out who anyone is, do not contact anyone, do not save or repost their photos.** A close match to a person is a stop-and-escalate event. These are unpublished drafts uploaded to third-party sites: check each site's current terms first (unverified)
2. **Stock-look check.** Search stock-photo and image sites in plain words that match the prompt (for example an East Asian man, short black hair, grey studio backdrop, over-ear headphones) and compare the first page by eye with the master. Generators sometimes reproduce a stock look
3. **The wife's local-public-figure check.** She sees the master, one face-sheet image and one expression image, at full size and on her phone. She writes down **in her own words** whether the face reminds her of any person from television, film, music, sport, news, politics or online video in Taiwan or elsewhere, and whether it reminds her of anyone she knows personally (initials only). We do not suggest names. She may look up a name she thinks of; she never uploads anything. **If she names a person: fail**
4. **Blind panel of at least 5**, at least 3 living in Taiwan, mixed ages, asked the open question "Does this remind you of any real person, anyone famous, or any character?" (no names offered). Ask them not to share or save the images. If one person names someone, the wife compares with that person's public photos by eye; if she or a second panel member sees it, fail. If two or more name the same person, fail
5. **Existing virtual humans.** Compare side by side with the photoreal virtual influencers listed in `research/competitors.md` sections 4 and 5 (by file, not repeated here) and with the headphone-wearing virtual singers and streamers that the bible 5.7 list covers. Same hair, headphones and jacket silhouette on a recognisable existing character is a fail
6. **Pass rule:** no unexplained close match in any search, no named person from the wife or the panel, no resemblance to a politician, no similarity to an existing virtual character. **Any doubt is a fail.** Fix by changing the offending feature through a revision of this file and the wife's re-approval, then re-run. Do not retouch
7. **Spot checks (assumption):** before launch, at the week-6 review, after any complaint, and on any later image whose face visibly differs from the master. Because every image comes from the one master, a drifted face is rejected rather than checked
8. **If a complaint arrives:** take the material down within 24 hours, pause, re-run, log, and ask the lawyer (legal.md question 20: does a claim need actual copying or only resemblance?). Keep the provenance rows ready as the record of origin

### 8.4 Uncanny read, real-person read and disclosure legibility (new)

Show five viewers (the same panel can be used) the master at full size and at phone size, one expression image with a smile and one with a slightly open mouth.

1. **Uncanny:** "Does anything look off, fake or creepy? Where?" (open answer), then "How natural, 1 to 5?" **Pass:** median 4 or more, and no more than one person flags the eyes or the mouth. Two flagging the same area: fail and fix that area (pack section 10)
2. **Real-person read (information, not pass or fail):** "Is this a photo of a real person?" Record the count. If four or five say yes, treat the disclosure risk as high: use the largest badge size and first-line wording in 7.1
3. **Disclosure legibility (strict):** show the image **with** the badge and the first caption line. "Is it clear whether this is a real person?" **Pass: all five say it is an AI character.** Any "not sure": enlarge or reposition the badge and strengthen the line, then retest. This is the check that Ground rule 1 depends on

### 8.5 Same-person test (new)

Show six images (the master, a face-sheet image, two expressions, one outfit B and one full-body) mixed in one row, with no labels. Ask "How many different people?" **Pass:** every viewer says one. A "two": find the drifting image and reject it.

---

## 9. Near-pair note: the three pilots must look like three different people

**Redone in the cross-pilot check of 2026-10-11**, when all three photoreal addenda existed (`personas/fangcun/photoreal-addendum.md` section 10 and `personas/sehuan/photoreal-addendum.md` section 10 carry the same table). The plain-language version for the operator is `pipeline/image-pack/README-photoreal.md` section 3. The earlier text of this section said 色環's photoreal design was undecided and listed 方寸 as a parallel draft; both are now settled.

| Axis | 步驟 (this file) | 色環 | 方寸 |
|---|---|---|---|
| Presentation and age | Man, 28, reads 28 to 33 | Woman-presenting, 30, reads 30 to 35 | Woman, 32, reads 30 to 36 |
| Face shape | Long oval, defined jaw, straight slightly square chin | Oval, widest at the cheekbones, narrow soft chin | Softly squared, rounded chin |
| Hair | Short black, side-parted | Shoulder-length blunt, worn down, left side tucked | Low ponytail, side-parted, no fringe |
| Face furniture | Matte charcoal over-ear headphones | Colour-wheel drop earrings | Thin walnut glasses |
| Skin undertone (by design, by eye) | Light-to-medium, neutral-to-warm | Medium, warm golden-beige | Light-to-medium, slightly warm |
| Signature | Rising six-square sewn patch | Persimmon accent, chip ring | Tick-mark belt |
| Palette | Cool greys, slate, charcoal; studio grey backdrop | Cream, warm stone, charcoal, persimmon; dusty blush backdrop | Oat, sage, walnut, cream belt; warm off-white backdrop |
| Key light and white balance | Front left, neutral daylight | Front right, neutral-warm | Front left, neutral-warm |
| Platforms | YouTube Shorts, Threads | Instagram, Threads | Instagram, YouTube Shorts |
| Shares a feed with 步驟 | n/a | **Threads** | **YouTube** |

**Six-axis rule (adopted for all three designs).** Each character differs from each other on at least four of: face shape; hair (length, colour, style); face furniture (glasses, earrings, headphones, facial hair); apparent age; skin undertone; backdrop and light. Apparent age is not counted for any pair (the visible bands overlap, generators cannot render a two-year gap, and under-reading is the main risk). 步驟 against 方寸: face shape, hair, face furniture, backdrop (studio grey 25.6 from off-white) and white balance differ, and so does presentation; skin undertone is the same. 步驟 against 色環: face shape (jaw and chin), hair, face furniture, backdrop (21.0 from the dusty-blush photo backdrop) differ; skin undertone is modest. Both are four or more. The largest pair in the set is 方寸 and 色環 (section 10 of the sibling addenda).

**Reserved for 步驟 (the siblings do not use these):** short black side-parted hair, over-ear headphones, a sewn patch, a cool grey studio backdrop, neutral daylight white balance, man-presenting. **Checked 2026-10-11:** neither sibling uses over-ear headphones, a patch, short hair or a grey or cool-grey backdrop. 色環's open blazer is a warm stone grey and is worn open; 步驟's coach jacket is a cool light grey and is zipped about two thirds; the two differ in hue (17.7 apart), cut and closure. **Never on 步驟:** glasses, earrings, a ponytail, hair worn down, oat, sage, walnut, persimmon, a blush or off-white backdrop.

**Tests (run when all three masters exist):**

1. The three headshots (or front waist-up images) in one row at about 110 px, on a laptop and on a phone, unlabelled. Can the wife tell them apart in two seconds with eyes half closed? (`pipeline/image-pack/README.md` section 8 has the stylised-era version; use `README-photoreal.md` section 3.)
2. Show the wife and at least four others (five viewers or more; the age-guess panel can be reused) the three and ask "How many different people? Do any two look related?" **Pass:** three people, nobody sees a family resemblance. Resemblance fails because it makes the set read as one operator's puppets (portfolio.md 3.3). **Fix by changing a design attribute of the character that fails, not by editing.**
3. Skin tone by eye on a shared Threads feed (步驟 and 色環): the flat-art skin swatches were 2.7 apart (computed); photoreal skin is not measured here, so the wife judges.
4. Generate each character in its own chat, and never upload one character's image as a reference for another.
5. Re-run `personas/palette_check.py` with the new ground and sampled photo values once accepted (`personas/README.md` section 8).

---

## 10. Changes the wife must rule on

Each is a change from the bible or an open wording question. I have not decided any of them. Until she rules, the pack runs the stated default.

| # | Question | Default used in the pack | Why it matters |
|---|---|---|---|
| 1 | **Man-presenting.** The bible was gender-neutral (bible open item 5). Does man-presenting feel natural? Keep **name-only** references and 這個角色, or allow 他? | Name-only copy; image shows a man | Pronouns appear in every caption. A male face with no pronoun may read stiff |
| 2 | **Region wording** in generator prompts: N (neutral, default), L ("plausibly local to Taiwan") or D (drop) | N | The same open item as the other pilots; stereotype risk if L |
| 3 | **Look and age.** Does the described face and the plain haircut read as an ordinary adult man in Taiwan in his late 20s, and not a template or a trend cut? Is "reads 28 to 33" right? | As written in 1.2 to 1.5 | Adult read, Taiwan realism |
| 4 | **Studio grey backdrop** replaces bone as the photo ground. Colour read: party colour, 喪服 (mourning) look, too cold or dull? Is the grey-on-grey wardrobe acceptable? | Studio grey `#A9B0B8` | It separates the pilots (5.2) but is a bible change |
| 5 | **The patch.** Sewn woven patch with a thin charcoal edge. Does it look like a logo of an app or a company? Keep six squares, or allow the three-bar fallback if generators cannot hold six? | Six squares, sewn, charcoal edge | Logo look is a look-alike risk; legibility at small size |
| 6 | **Headphones always on the head.** Natural for the persona, or should some images show them around the neck? | On the head; around the neck allowed in a few full-body shots | Ears are hidden when worn |
| 7 | **Disclosure wording for photoreal.** First line: 「圖像為 AI 生成，並非真人」 (replacing 「圖為示意」); badge 「AI 生成｜虛擬角色」 on every image that shows him (「AI 生成｜示意圖」 on a plate without him); 「AI」 tag on avatars. Natural, or too heavy and 工商味? | As in 7.1 | Ground rule 1; she is the only reader of the Chinese |
| 8 | **Running joke J2** (「耳機沒接線」): the headphones now look like real headphones. Does the joke still land? | Kept | Voice |
| 9 | **示意 sets.** Are a plain desk corner, an office partition and a study room acceptable, and do the Taiwan details look right? | Studio only until she signs off | "My life" read; Taiwan-ness |
| 10 | **Fallback.** If photoreal fails the uncanny, age or look-alike tests after three rounds, is the fallback the stylised art? (A decision for the user too.) | Stylised art (`assets/buzhou/art/`, v0.1, gender-neutral) is a different character; do not mix looks on one account | Planning |
| 11 | **Her time.** The photoreal checks add her local-public-figure check and the uncanny and legibility tests. Suggested: about 15 minutes per master check and 10 per re-run (assumption). Acceptable inside her 10 hours a week? | Yes, assumed | Capacity (DECISIONS Section 2 answers, #2) |

---

## 11. Other open items (operator and user)

1. **Licence terms.** Read and record the current commercial-use terms for the exact Gemini and ChatGPT plans before any publication (pack section 7). Not checked here.
2. **Voice and lip-sync.** Gate G5 stays open; this addendum assumes stills and captions only (risk 8).
3. **Instagram label.** Test on a Taiwan test account (HUMAN_TODO 10).
4. **Palette register.** `personas/README.md` section 8 (added 2026-10-11) says the near-pair checks must be re-run on photos. `personas/palette_check.py` is not edited: update it with the studio grey and sampled photo values when the wife accepts them.
5. **Records.** The photoreal tasks (wife's rulings, extra lawyer questions, the extra look-alike process) are in `HUMAN_TODO.md`, section "Photoreal switch" (added 2026-10-11). `DECISIONS.md` has the 2026-10-11 decision; an entry for this addendum is still to be added.
6. **Tool refusals and marks.** If a tool refuses a prompt or adds a visible or hidden mark (unverified), log it and do not reword to get round a refusal.
7. **Hand-finishing.** The stylised plan was to finish the master in a vector editor. For photoreal, keep an untouched original and a lightly edited copy (crop, exposure, white balance), logged, as the human-authorship record.
8. **Claude cannot do the look-alike check.** Claude does not identify real people from faces and must not be asked who the character resembles. Claude can give a first-pass checklist on a saved image; the wife's judgements cannot be replaced.

---

## Appendix: references

BRIEF.md section 3 (ground rules 1 to 6); DECISIONS.md 2026-10-11 entry; `personas/buzhou/bible.md` 2.4, 4.1 to 4.9, 5.1 to 5.9, 7.3, 8.1 to 8.4; `strategy/portfolio.md` 1.4, 2D, 2.6, 3.3, 6.2; `research/competitors.md` section 5 and S1 to S3, S7, S8, S45; `research/platforms.md` 4.1 to 4.3, S27, S28, S51; `research/culture.md` 5.3, 5.5, 6.1 to 6.4, 7.4, 7.6; `research/legal.md` 8.2, 8.3, question 20; `personas/palette_check.py`; `personas/README.md` section 5; `pipeline/image-pack/README.md`; `pipeline/image-pack/buzhou.md` (stylised pack, structure); `pipeline/image-pack/buzhou-photoreal.md` (the pack that implements this file).
