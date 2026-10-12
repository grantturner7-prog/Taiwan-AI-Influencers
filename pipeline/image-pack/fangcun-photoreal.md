# 方寸 (fangcun) PHOTOREAL image pack: first reference images

**Pack v1 (photoreal), written 2026-10-11.** For the operator (English only) and the wife (language and culture review). Source of truth: `personas/fangcun/photoreal-addendum.md` ("the addendum"), then `personas/fangcun/bible.md` for everything the addendum leaves alone. If this pack and the addendum ever disagree, the addendum wins; tell Claude and the pack gets fixed.

**This pack replaces the clay-figure pack (`fangcun.md`) for 方寸.** The user rejected the stylised look ("looks so fake, I need real people", `DECISIONS.md` 2026-10-11). The decision is recorded as **photorealistic AI-generated characters that stay openly AI**. The old pack is kept for history; do not use its prompts. The other two pilots now have their own photoreal packs (`buzhou-photoreal.md`, `sehuan-photoreal.md`). **Start with `pipeline/image-pack/README-photoreal.md`** (which pilot first, time, how to log, what to send back, why the labels still apply).

**Status of everything you make with this pack: working references, not approved assets.** Nothing is cleared for public use until the master passes the checklist (section 5), all three human tests (section 6), light hand-finishing, and the wife and operator approve it. Nothing has been generated yet; no photoreal reference image exists.

**How to use it:** read sections 0 and 1, then do sections 2 and 3 in order. Keep section 5 (checklist) and section 7 (log) open while you work. Copy the contents of each code box exactly as written. Model names, buttons and features in Gemini and ChatGPT change often, so **every statement about them below is a hypothesis**: check the current screen.

---

## 0. One-screen summary

**Who.** 方寸 (Fāngcùn, roughly "fahng-tsun") is a fictional adult woman, stated age 32, shown in photorealistic studio portraits. She is an **AI character**, not a real person, and every image says so. Practical, calm and tidy. Softly squared face, dark brown-black hair pulled back in a low ponytail, thin walnut-brown glasses, a plain knit top with an open sage vest, walnut trousers, and a cream belt printed with fine tick marks like a tape measure (no numbers). She will explain small-flat and renting arithmetic to Taiwan audiences on Instagram and YouTube Shorts, usually beside a human-built diagram. She has never lived in a home or used a product, so her pictures are plain studio portraits: no rooms, no places, no props, no hands.

**Goal of the first session.**
1. Pick one master portrait (R01, waist-up, front) that passes the checklist.
2. Use it to make the next images: three-quarter left and right, side, back and headshot (R02 to R06).
3. In later sittings: the ten expressions, the framings, the outfits, the seasons, the scale reference and the avatar (section 4).
4. Log every file the same day. The tests with other people, light hand-finishing and the freeze of the set come after.

**Three things that matter most.**
- **Hands are the top failure.** Every prompt keeps them out of the frame or inside pockets. Section 9.1 is the fix procedure.
- **She must never look like anyone real.** You run a reverse-image search by hand and the wife looks for resemblance (section 6). A look-alike is a hard fail.
- **Every image is labelled.** Save files untouched, add the on-screen badge only in editing, switch on the platform's AI label (section 7.5).

**Time (my estimate, not measured).** Sitting 1 about 1.5 to 2 hours (set-up, R01 in both tools, choose a shortlist). Sitting 2 about 2 to 2.5 hours (R02 to R06). Sitting 3 about 2 to 3 hours (section 4). About 15 minutes of the wife's time on the shortlist. About 1.5 to 2 hours on another day for the tests (more than the clay pack: there are more searches and more people). Write down your real minutes; the studio's capacity plan needs them.

**Order of work.**

| Step | What | Where |
|---|---|---|
| 1 | Make the folders and open the log (5 to 10 min) | Section 1 |
| 2 | R01 prompt in Gemini (4 images) and in ChatGPT (4 images) | Section 2 |
| 3 | Reject pass, checklist, shortlist at most 3 | Sections 2.6, 5 |
| 4 | Wife looks at the shortlist; you run the reverse-image search | Sections 8, 6.3 |
| 5 | Choose a provisional master, save as `R01_master_v1` | Section 2.6 |
| 6 | R02 to R06 with R01 attached each time (sitting 2) | Section 3 |
| 7 | Expressions, framings, outfits, seasons, scale reference, avatar (sitting 3) | Section 4 |
| 8 | Log as you go, not at the end | Section 7 |
| 9 | Another day: age-guess test, blind test, near-pair test, light hand-finishing, freeze the set (with Claude) | Sections 6, 11 of the addendum |

---

## 1. Before you start

- **Tool: start with Gemini, then run the same prompt in ChatGPT (hypothesis, not a finding).** Gemini's conversational recipe is the simpler start; ChatGPT's recipe is the more structured one. Nobody has tested either on this character, which is what today finds out. Once R01 is chosen, stay in the tool that made it for the follow-ups (hypothesis: one tool keeps the face more consistent).
- **Settings to look for, only if available.** Image shape or aspect ratio (4:5 portrait for most images, 1:1 for headshots and the avatar; if there is no setting, each prompt's OUTPUT line asks for it). Number of images per request (set 4; if not offered, send the prompt again until you have 4 separate images). Highest quality or resolution. A model or version picker (pick one and keep it for the whole sitting; **copy its label exactly**). Style presets or filters: leave **off**, so only the prompt sets the look. Chat history: do not use a temporary or private mode, you need the conversation link for the log. Use the download button for the largest version; a screenshot is the last resort (it loses file markers, see 7.5) and must be noted in the log.
- **Uploads: the only image you may ever upload is this character's own generated image** (R01 and the other golden images from this pack), and a plain colour swatch. **Never** upload a photograph of any real person (family, friends, colleagues, models, public figures, yourself), never an image of **any other character, including 色環 and 步驟**, never a picture, screenshot or fan art of any existing character or virtual influencer, and never a photo of a real room. Not "just for the face shape", not "just for the pose", not "just for the lighting". Describe things in words, as the prompts do.
- **Use a separate chat for this character.** Never continue a chat in which you made 色環 or 步驟. A generator reuses its default face, and a cross-contaminated chat is the commonest cause of "they look like sisters" (addendum 10).
- **Never type into a prompt** a real person's name, a celebrity, influencer, model, actor, existing character, or the words "looks like" / "in the style of" followed by any of those. No real brand, logo or number plate. The look-alike tests in section 6 are done by eye on the finished picture; no name ever goes into a prompt.
- **Outfits are her fixed design.** She does not try, test or review clothes. Never ask her to hold, use, taste, try on or show any object, and never name a garment brand or product.
- **No text in the picture.** Any text in any script on a generated image fails it (the belt must show tick marks only). Chinese text and the badge are added later in a design tool, and the wife reads every character.
- **Save everything and log everything.** Download every image you look at for more than a glance into `assets/fangcun/photoreal/` (candidates go in its `candidates/` folder) with the file name from this pack. Do not edit or rename-over the original download. Delete nothing today. One row per file in `assets/provenance.csv` the same day (section 7).
- **Licence terms are NOT checked.** This pack does not know what Gemini or ChatGPT allow for commercial use on your plan, or what they say about realistic images of people. Before any commercial use, read the current terms for the exact tool and plan, and record the date and the key sentence in `licence_notes` (section 7.4). Until then every image is internal design material only: no client work, no sponsored post, no public account.
- **Do not strip or remove any mark** the tool adds (visible, or in the file). Note it in the log (section 7.5).

**Set-up (about 5 to 10 minutes).**
1. The folder `assets/fangcun/photoreal/` already exists (with a `.gitkeep`). Inside it make two folders: `candidates` (every image you considered but did not choose) and `lookalike` (screenshots from section 6).
2. A folder `assets/fangcun/candidates/` from the earlier stylised attempt may exist, with one stylised, rejected Gemini image already logged in `assets/provenance.csv`. It is unrelated to this pack: leave it and its row alone, and save photoreal files only under `assets/fangcun/photoreal/`. Open `assets/provenance.csv` in a spreadsheet app. The header must read `timestamp,asset_path,persona,tool,model,prompt,licence_notes`. Do not change it. Add rows at the bottom.
3. Copy the Character Lock (section 3.1) into a notes file so you can paste it quickly.
4. In the same notes file, start a line "minutes: " and add your times as you go.

---

## 2. STEP 1: the master portrait R01

**What you are making.** One picture: a waist-up front portrait of the fictional person, calm closed-mouth expression, outfit O1, plain warm off-white studio background, 4:5 portrait. The frame ends at the belt line so **both hands are outside the picture**. Everything later is built from this image, so spend the time here.

The two prompts below carry the same design. The Gemini one opens conversationally and ends with a "Please avoid" sentence; the ChatGPT one uses labelled blocks and an AVOID block. The wording that describes her is identical. The avoid list is photoreal-specific (it replaces the clay one).

**Wording decision for the wife (open).** The line `East Asian, with ordinary, natural, unexaggerated features, not an idol or model look` is the neutral default. If the wife wants a different wording, swap that exact phrase for one of these in both prompts and write the changed prompt in the log:
- Option B: `East Asian, with ordinary, natural, unexaggerated features that read as Taiwanese, not an idol or model look`
- Option C: `an ordinary adult you could plausibly see on an everyday street in a large East Asian city, with natural, unexaggerated features, not an idol or model look`
Option C describes the face only: if an app starts drawing a street or any background from it, go back to the default. Run today's prompts with the default unless she has already answered.

### 2.1 Gemini: paste this

```
Create a photorealistic image from this brief.

Generate a fictional person. She is an original character with no real-world counterpart and must not resemble any real individual.

SUBJECT: an adult woman in her early thirties (she looks about 32 to 35), East Asian, with ordinary, natural, unexaggerated features, not an idol or model look. Softly squared face with a rounded chin and moderate cheeks. Medium-sized dark-brown eyes with a natural eyelid line and a calm level gaze. Straight dark-brown eyebrows of natural thickness. Medium-width nose with a soft tip. Natural medium lips in a muted rose-brown, closed in a very slight calm smile, no teeth showing. Light-to-medium, slightly warm, even skin tone with natural skin texture: fine pores visible, faint fine lines at the outer corners of the eyes and faint lines from nose to mouth at rest, soft natural under-eye shadow. Minimal natural makeup, no gloss, no glow.

HAIR: dark brown-black, straight, side parting, pulled back into a neat low ponytail at the nape with a plain thin dark-brown hair tie, a few natural flyaways, no fringe over the forehead, both ears partly visible.

GLASSES: thin matte walnut-brown softly rounded-rectangle frames with clear lenses, no logo, no glare or reflection on the lenses, both eyes fully visible.

OUTFIT (O1 Everyday): a plain oat-coloured fine-knit crew-neck top with long sleeves, tucked in; over it an open, hip-length sleeveless vest in muted sage; straight walnut-brown trousers. At the waist, a cream woven fabric belt with fine charcoal tick marks along its edge like a tape measure (tick marks only, no numbers or letters) and a small walnut-brown buckle, worn loosely at the waist and not cinched. Relaxed modest fit, the neckline covers the collarbone. No logos, text or patterns on any clothing. No jewellery.

POSE AND FRAMING: waist-up portrait. The frame ends at the belt line, so both hands are outside the picture, below the frame. Arms relaxed at her sides, shoulders level and relaxed, upright calm posture. Body and head facing the camera, calm direct gaze at the lens. Eye-level camera.

STYLE: a polished studio character-reference portrait, not a phone snapshot and not a candid photo. 85 mm lens look, no wide-angle distortion. One large soft diffused light from the front left at about 45 degrees with gentle fill from the right, neutral-warm colour balance, soft natural shadows, matte skin without shine, one soft window-shaped catchlight in each eye. Muted, low-saturation colour grade. Plain warm off-white seamless studio background, evenly lit, no gradient. No filters, no film grain, no beauty retouching.

OUTPUT: 4:5 portrait, one image.

Please avoid: hands or fingers anywhere in the picture; any resemblance to a real person; an idol, model or beauty-filter look; airbrushed, plastic, waxy or over-smooth skin; glowing or glossy skin; enlarged doll-like eyes; heavy eye makeup, eyeliner wings, glossy lipstick; teeth showing; laughing or an open mouth; tears; a baby-faced or teenage look; a fringe over the forehead; hair worn down; earrings, necklaces, rings, watches or any jewellery; text, letters, numerals, hex codes, logos, brand marks, watermarks, signage; a selfie, phone-camera or candid snapshot look; a mirror; other people, children, pets; real places or landmarks; a tape measure held, pulled out or wrapped around the body; revealing, tight, sheer, low-cut or sleeveless-only clothing; a sexualised or glamour pose; a uniform, apron, lab coat, hard hat or high-visibility vest; a school uniform; saturated red, blue, green or yellow clothing; an all-black or all-white outfit; sunglasses, tinted lenses or glare on the lenses; asymmetrical or warped glasses; mismatched eyes or ears; extra or missing fingers.
```

### 2.2 ChatGPT: paste this

```
Generate one image from the brief below.

Generate a fictional person, photorealistic. She is an original character with no real-world counterpart and must not resemble any real individual.

SUBJECT: an adult woman in her early thirties (she looks about 32 to 35), East Asian, with ordinary, natural, unexaggerated features, not an idol or model look. Softly squared face with a rounded chin and moderate cheeks. Medium-sized dark-brown eyes with a natural eyelid line and a calm level gaze. Straight dark-brown eyebrows of natural thickness. Medium-width nose with a soft tip. Natural medium lips in a muted rose-brown, closed in a very slight calm smile, no teeth showing. Light-to-medium, slightly warm, even skin tone with natural skin texture: fine pores visible, faint fine lines at the outer corners of the eyes and faint lines from nose to mouth at rest, soft natural under-eye shadow. Minimal natural makeup, no gloss, no glow.

HAIR: dark brown-black, straight, side parting, pulled back into a neat low ponytail at the nape with a plain thin dark-brown hair tie, a few natural flyaways, no fringe over the forehead, both ears partly visible.

GLASSES: thin matte walnut-brown softly rounded-rectangle frames with clear lenses, no logo, no glare or reflection on the lenses, both eyes fully visible.

OUTFIT (O1 Everyday): a plain oat-coloured fine-knit crew-neck top with long sleeves, tucked in; over it an open, hip-length sleeveless vest in muted sage; straight walnut-brown trousers. At the waist, a cream woven fabric belt with fine charcoal tick marks along its edge like a tape measure (tick marks only, no numbers or letters) and a small walnut-brown buckle, worn loosely at the waist and not cinched. Relaxed modest fit, the neckline covers the collarbone. No logos, text or patterns on any clothing. No jewellery.

POSE AND FRAMING: waist-up portrait. The frame ends at the belt line, so both hands are outside the picture, below the frame. Arms relaxed at her sides, shoulders level and relaxed, upright calm posture. Body and head facing the camera, calm direct gaze at the lens. Eye-level camera.

STYLE: a polished studio character-reference portrait, not a phone snapshot and not a candid photo. 85 mm lens look, no wide-angle distortion. One large soft diffused light from the front left at about 45 degrees with gentle fill from the right, neutral-warm colour balance, soft natural shadows, matte skin without shine, one soft window-shaped catchlight in each eye. Muted, low-saturation colour grade. Plain warm off-white seamless studio background, evenly lit, no gradient. No filters, no film grain, no beauty retouching.

OUTPUT: 4:5 portrait; one image.

AVOID: hands or fingers anywhere in the picture; any resemblance to a real person; an idol, model or beauty-filter look; airbrushed, plastic, waxy or over-smooth skin; glowing or glossy skin; enlarged doll-like eyes; heavy eye makeup, eyeliner wings, glossy lipstick; teeth showing; laughing or an open mouth; tears; a baby-faced or teenage look; a fringe over the forehead; hair worn down; earrings, necklaces, rings, watches or any jewellery; text, letters, numerals, hex codes, logos, brand marks, watermarks, signage; a selfie, phone-camera or candid snapshot look; a mirror; other people, children, pets; real places or landmarks; a tape measure held, pulled out or wrapped around the body; revealing, tight, sheer, low-cut or sleeveless-only clothing; a sexualised or glamour pose; a uniform, apron, lab coat, hard hat or high-visibility vest; a school uniform; saturated red, blue, green or yellow clothing; an all-black or all-white outfit; sunglasses, tinted lenses or glare on the lenses; asymmetrical or warped glasses; mismatched eyes or ears; extra or missing fingers.
```

If an app answers with text instead of a picture, reply "Please generate the image now." If it refuses, **do not reword the prompt to get around the refusal**: log it and tell Claude.

### 2.3 The avoid list on its own, and a short fallback

Chat tools have no negative-prompt box, so the avoid list is a sentence at the end (done above). If the long list seems to make an app draw the things it names, use the short fallback in 9.3.

### 2.4 What to generate

- **4 images in Gemini and 4 in ChatGPT**, each a separate waist-up portrait.
- Save each at once as `assets/fangcun/photoreal/candidates/R01_cand_gemini_1.png` to `_4`, and `R01_cand_chatgpt_1.png` to `_4`. If the app gives another file type (`.jpg`, `.webp`), keep that type and use the real name in the log.
- Write down, for each: the tool, the model label **exactly as the app shows it today**, the time, the conversation link or ID, and a seed if one is shown.
- If nothing passes, change one thing (a fix phrase from 9.2), generate 4 more, and repeat. A planning figure is about 8 to 12 candidates per tool (*assumption*). If both tools fail the same way after two rounds, stop and tell Claude.

### 2.5 The inspection habit (do this on every image you keep)

Open it at **100%** and then at **200%**. Look in this order: hands (should be absent), eyes, glasses, ears, mouth and teeth, skin, hair edges, belt, background. Hands are the part that fails most, and a defect there is the one the public mocks fastest.

### 2.6 How to choose

1. **Thirty-second reject pass.** Throw out any image with a visible hand or finger, text or numerals, teeth, glare on the lenses, hair worn down, no glasses, jewellery, a fringe, a plastic or airbrushed look, a teenage look, a glamour or sexualised feel, a non-plain background, or a selfie or snapshot look. Do not delete the files; mark them "rejected" in your notes.
2. **Checklist.** Run section 5 on each survivor.
3. **Shortlist at most three.**
4. **Wife looks** at the shortlist, without being told which tool made which (section 8). **You run the reverse-image search** on each shortlisted image (section 6.3).
5. **Choose one** and copy it to `assets/fangcun/photoreal/R01_master_v1.png` (keep the original in `candidates`). Log it as "provisional master". It becomes the real master only after the tests in section 6 pass and it has had light hand-finishing in an image editor (crop, colour, stray marks; **no skin smoothing**).

---

## 3. STEP 2: lock it

### 3.1 The Character Lock (paste this at the start of every follow-up prompt)

Attach R01 first (it is "Image 1"). Do not use the Lock for R01 itself or for R12.

```
Image 1 is the approved master image of one fictional person, an original character with no real-world counterpart. Keep exactly the same person: the softly squared face with a rounded chin, the medium-sized dark-brown eyes with a natural eyelid line, the straight dark-brown eyebrows, the medium nose with a soft tip, the natural closed lips, the light-to-medium warm skin tone with natural skin texture and fine pores, the dark brown-black hair in a low ponytail with a side parting, no fringe and a plain dark-brown hair tie, and the thin matte walnut-brown rounded-rectangle glasses with clear lenses and no glare. She looks about 32 to 35. No jewellery. Do not change the face, do not make her younger, do not smooth the skin, do not add makeup or glamour. Only the single change named below is allowed.

DEFAULTS unless the change below says otherwise: calm closed-mouth expression; outfit O1 (oat knit top tucked in, open sage vest, walnut trousers, cream belt with fine charcoal tick marks only, no numbers, worn loosely and not cinched); arms relaxed; both hands outside the picture; polished studio portrait, soft diffused light from the front left, neutral-warm muted colour, plain warm off-white seamless background. No text, logos or watermarks. No other people.
```

### 3.2 How R01 is used as the reference

- **New chat with R01 re-uploaded (recommended).** Open a fresh chat, attach your saved `R01_master_v1` file (**her own generated image**; uploading it is fine), then send the Character Lock, a blank line, and the prompt for that image. The advice to restart rather than correct in a long thread is an *assumption*; today confirms or refutes it. Use "same chat" only to retry the same image with a small fix.
- Attach R01 every time, plus at most two other golden images. Never anchor to a freshly generated output alone.
- One change per picture. Make 4, choose the best, compare with R01 **at the same size** using section 5. Two failures in a row: new chat, R01 only.
- **If the tool changes its model label between two sittings**, treat the next images as a new design: log the label, and re-run the look-alike checks (addendum 11, item 7).

### 3.3 Per-image routine (about 10 to 15 minutes each; my estimate)

1. Open a new chat in the tool that made R01.
2. Attach the files on the "Attach" line. In ChatGPT use image edit mode with reference images if offered (hypothesis); otherwise attach to a normal message. In Gemini attach to the message.
3. Paste the Character Lock, a blank line, then the prompt for that image.
4. Get 4 images and save all 4 into `candidates` at once.
5. Inspect (2.5), run the checklist (section 5), choose one, copy it to its pack name.
6. Add the log rows (kept and discarded) before the next image.

### 3.4 Order of work, file names and what to attach

Save in `assets/fangcun/photoreal/`. A redo is `v2`. File types follow the app. Candidates go in `candidates/` as `<ID>_cand_<tool>_<n>`.

| Order | ID | Image | Attach | Save the chosen one as | When |
|---|---|---|---|---|---|
| 1 | R01 | Master: waist-up, front, O1, calm face | nothing | `R01_master_v1.png` | Sitting 1 |
| 2 | R02 | Three-quarter left, waist-up | R01 | `R02_three-quarter-left_v1.png` | Sitting 2 |
| 3 | R03 | Three-quarter right, waist-up | R01 | `R03_three-quarter-right_v1.png` | Sitting 2 |
| 4 | R04 | Side profile, waist-up | R01 | `R04_side_v1.png` | Sitting 2 |
| 5 | R05 | Back view, waist-up | R01 | `R05_back_v1.png` | Sitting 2 |
| 6 | R06 | Headshot, front, 1:1 (face lock) | R01 | `R06_headshot_v1.png` | Sitting 2 |
| 7 | R07 | Ten expressions, one image each | R01, R06 | `EXP_E01_neutral_v1.png` ... `EXP_E10_nod_v1.png` | Sitting 3 |
| 8 | R08a | Half-body framing | R01 | `R08a_half-body_v1.png` | Sitting 3 |
| 9 | R08b | Knees-up, hands in pockets | R01 | `R08b_knees-up_v1.png` | Sitting 3 |
| 10 | R08c | Full body, hands in pockets | R01 | `R08c_full-body_v1.png` | Sitting 3 |
| 11 | R09 | Outfits O2 and O3 (O1 is R01) | R01 | `R09_O2_v1.png`, `R09_O3_v1.png` | Sitting 3 |
| 12 | R10 | Seasons: summer, winter (rain is O3) | R01 | `R10_summer_v1.png`, `R10_winter_v1.png` | Sitting 3 |
| 13 | R11 | Scale reference beside a freestanding door frame | R01 | `R11_scale-door_v1.png` | Sitting 3 |
| 14 | R12 | Belt flat-lay (object only, no person) | nothing | `R12_belt_v1.png` | Sitting 3, optional |
| 15 | R13 | Glance toward the diagram, waist-up | R01 | `R13_glance_v1.png` | Sitting 3 |
| 16 | R14 | Avatar 1:1 and 110 px test | R06 | `R14_avatar-1x1_v1.png` | After the master is final |
| 17 | R15 | Palette card (made by hand) | none | `R15_palette-card_v1.png` | See 3.6 |
| 18 | R16 | Badge and "AI" chip templates (made by hand) | none | later | See 3.6 |

The addendum (section 11) lists R01 to R16 as the golden set. Renaming into the frozen naming scheme happens when the set is frozen (Claude can do the rename and update the log paths).

### 3.5 The prompts for R02 to R06 (send after the Character Lock)

**R02: three-quarter left.** Attach: R01.

```
CHANGE only: the angle. Show the same woman in a three-quarter view, her body and head turned about 40 degrees toward the viewer's left, eyes still looking at the camera. Waist-up: the frame ends at the belt line and both hands are outside the picture below the frame, arms relaxed. Same outfit (O1), same hair and glasses, same calm closed-mouth expression.
OUTPUT: 4:5 portrait; plain warm off-white seamless studio background; same soft studio light from the front left; one image.
```

**R03: three-quarter right.** Attach: R01.

```
CHANGE only: the angle. Show the same woman in a three-quarter view, her body and head turned about 40 degrees toward the viewer's right, eyes still looking at the camera. Waist-up: the frame ends at the belt line and both hands are outside the picture below the frame, arms relaxed. Same outfit (O1), same hair and glasses, same calm closed-mouth expression.
OUTPUT: 4:5 portrait; plain warm off-white seamless studio background; same soft studio light from the front left; one image.
```

**R04: side profile.** Attach: R01.

```
CHANGE only: the angle. Show the same woman in a side profile, seen exactly from the side, facing toward the viewer's left, eyes looking straight ahead. Show the profile of the softly squared face, one ear, the arm of the thin walnut glasses over the ear, the low ponytail at the nape, and the cream tick-mark belt seen edge-on. Waist-up: the frame ends at the belt line and both hands are outside the picture. Same outfit (O1).
OUTPUT: 4:5 portrait; plain warm off-white seamless studio background; same soft studio light; one image.
```

**R05: back view.** Attach: R01.

```
CHANGE only: the angle. Show the same woman from directly behind, head facing away from the camera: the low ponytail with its plain dark-brown hair tie, the back of the oat knit top and the open sage vest, and the back of the cream belt with its fine tick marks (tick marks only, no numbers). Waist-up: the frame ends at the belt line and both hands are outside the picture. Same outfit (O1).
OUTPUT: 4:5 portrait; plain warm off-white seamless studio background; same soft studio light; one image.
```

**R06: headshot (face lock).** Attach: R01.

```
CHANGE only: the framing. Headshot: head and shoulders, the frame ends at the upper chest below the collarbone, front view, calm closed-mouth expression, eye-level, 85 mm lens look. Centre the head with clear space above it so a circular crop will not cut the hair. No hands in the picture.
OUTPUT: 1:1 square; plain warm off-white seamless studio background; same soft studio light; one image.
```

### 3.6 Images that are not generated

- **R15 palette card.** Made by hand in any slides or design app: one square swatch per colour with its hex under it (colours and ranges in 5.3, plus the hair, near-black brown, by eye). Log it with tool "human-made in <app name>" and prompt "none (made by hand)".
- **R16 badge and "AI" chip templates.** They carry text (「AI 生成｜示意圖」, 「AI 生成｜虛擬角色」, and the Latin chip "AI"). Do **not** ask Gemini or ChatGPT to draw them. They are built in a design tool with a Taiwan-form font (Noto Sans TC), and the wife reads every character. Not part of this session.
- **R14 avatar crops** are cut from the final master, so they wait until it is hand-finished (4.5).

---

## 4. Expressions, outfits, framings, poses, avatar

All prompts below follow the Character Lock. Attach as stated.

### 4.1 R07: the ten expressions (one image each)

Attach: R01 and R06. Do **not** ask for several faces on one image; in photoreal they come out as different people. One image per expression, then check each is still her. Names and uses are the bible's (5.5); only brows, eyes and lips change; lips stay closed in every expression (no parted lips; the cross-pilot check of 2026-10-11 removed the E07 exception, as in the 色環 pack); no teeth, tears, wink, pout or laughing. Save as `EXP_E04_noticing_v1` and so on.

| ID | Name | Face |
|---|---|---|
| E01 | 平靜 neutral (default) | Calm, brows level, lips closed in a very slight smile |
| E02 | 滿意 pleased | Gentle closed-mouth smile, eyes slightly softened |
| E03 | 思考 thinking | One brow slightly raised, eyes up and to the viewer's left, lips closed and flat |
| E04 | 發現 noticing | Both brows slightly raised, eyes a little wider but natural, lips together |
| E05 | 不確定 hmm | Brows slightly inward and down, lips pressed lightly together |
| E06 | 更正 correcting | Head tilted about 5 degrees, inner brow ends slightly raised, lips closed and flat |
| E07 | 說明 explaining | Brows level, head tilted about 5 degrees, lips closed and relaxed with the faintest lift of the chin, as if about to speak; lips not parted, no teeth visible |
| E08 | 冷面 deadpan | Brows level and low, flat gaze, lips closed and flat |
| E09 | 微笑 soft smile | Soft closed-mouth smile, small smile lines at the eye corners |
| E10 | 點頭 calm nod | Head down 5 to 10 degrees, eyes still toward the camera, slight closed-mouth smile |

E01:
```
Image 2 is the headshot; use it for the face only.
CHANGE only: the expression (E01, neutral): calm, brows level, lips closed in a very slight smile. Headshot, head and shoulders, front view, no hands in the picture. Nothing else changes.
OUTPUT: 1:1 square; plain warm off-white seamless studio background; same soft studio light; one image.
```

E02:
```
Image 2 is the headshot; use it for the face only.
CHANGE only: the expression (E02, pleased): a gentle closed-mouth smile, the eyes slightly softened, brows relaxed. No teeth. Headshot, head and shoulders, front view, no hands in the picture. Nothing else changes.
OUTPUT: 1:1 square; plain warm off-white seamless studio background; same soft studio light; one image.
```

E03:
```
Image 2 is the headshot; use it for the face only.
CHANGE only: the expression (E03, thinking): one eyebrow slightly raised, eyes directed up and to the viewer's left, lips closed and flat. Headshot, head and shoulders, front view, no hands in the picture. Nothing else changes.
OUTPUT: 1:1 square; plain warm off-white seamless studio background; same soft studio light; one image.
```

E04:
```
Image 2 is the headshot; use it for the face only.
CHANGE only: the expression (E04, noticing): both eyebrows slightly raised, the eyes a little wider but natural, lips together and relaxed. No open mouth, no teeth. Headshot, head and shoulders, front view, no hands in the picture. Nothing else changes.
OUTPUT: 1:1 square; plain warm off-white seamless studio background; same soft studio light; one image.
```

E05:
```
Image 2 is the headshot; use it for the face only.
CHANGE only: the expression (E05, unsure): eyebrows drawn slightly inward and down, lips pressed lightly together. No teeth. Headshot, head and shoulders, front view, no hands in the picture. Nothing else changes.
OUTPUT: 1:1 square; plain warm off-white seamless studio background; same soft studio light; one image.
```

E06:
```
Image 2 is the headshot; use it for the face only.
CHANGE only: the expression and head position (E06, correcting): head tilted about 5 degrees, the inner ends of the eyebrows slightly raised, lips closed and flat. Headshot, head and shoulders, no hands in the picture. Nothing else changes.
OUTPUT: 1:1 square; plain warm off-white seamless studio background; same soft studio light; one image.
```

E07:
```
Image 2 is the headshot; use it for the face only.
CHANGE only: the expression (E07, explaining): eyebrows level, head tilted about 5 degrees, the lips closed and relaxed with the faintest lift of the chin, as if about to speak, lips not parted, no teeth visible. Headshot, head and shoulders, front view, no hands in the picture. Nothing else changes.
OUTPUT: 1:1 square; plain warm off-white seamless studio background; same soft studio light; one image.
```

E08:
```
Image 2 is the headshot; use it for the face only.
CHANGE only: the expression (E08, deadpan): eyebrows level and low, a flat gaze, lips closed and flat, no smile. Headshot, head and shoulders, front view, no hands in the picture. Nothing else changes.
OUTPUT: 1:1 square; plain warm off-white seamless studio background; same soft studio light; one image.
```

E09:
```
Image 2 is the headshot; use it for the face only.
CHANGE only: the expression (E09, soft smile): a soft closed-mouth smile with small smile lines at the corners of the eyes. No teeth. Headshot, head and shoulders, front view, no hands in the picture. Nothing else changes.
OUTPUT: 1:1 square; plain warm off-white seamless studio background; same soft studio light; one image.
```

E10:
```
Image 2 is the headshot; use it for the face only.
CHANGE only: the expression and head position (E10, calm nod): head tilted down about 5 to 10 degrees, eyes still toward the camera, a slight closed-mouth smile. Headshot, head and shoulders, no hands in the picture. Nothing else changes.
OUTPUT: 1:1 square; plain warm off-white seamless studio background; same soft studio light; one image.
```

### 4.2 R08: framings (half-body, knees-up, full body)

Headshot is R06 and waist-up is R01. Attach: R01.

**R08a: half-body** (top of head to the lower chest; the belt is not in this frame)

```
CHANGE only: the framing. Half-body: from the top of the head to the lower chest, front view, calm closed-mouth expression, arms relaxed and outside the picture. Outfit O1.
OUTPUT: 4:5 portrait; plain warm off-white seamless studio background; same soft studio light; one image.
```

**R08b: knees-up, hands in pockets**

```
CHANGE only: the framing and pose. Three-quarter length: from the top of the head to mid-thigh, front view, standing relaxed and upright, both hands fully inside her trouser pockets, the sleeves covering the forearms, so that no fingers, thumbs or bare hands are visible. The cream tick-mark belt is visible in the open front of the vest. Outfit O1, calm closed-mouth expression, direct gaze at the camera.
OUTPUT: 4:5 portrait; plain warm off-white seamless studio background; soft contact shadow; same soft studio light; one image.
```

**R08c: full body, hands in pockets**

```
CHANGE only: the framing and pose. Full body from the top of the head to the shoes, front view, standing relaxed and upright on the seamless studio floor, 50 mm lens look, eye-level camera, both hands fully inside her trouser pockets so that no fingers or thumbs are visible. Plain flat walnut-brown leather loafers with no logo, both shoes fully in the frame with correct feet. Outfit O1, calm closed-mouth expression, direct gaze at the camera. Natural proportions: the head is about one seventh of her standing height.
OUTPUT: 4:5 portrait; plain warm off-white seamless studio background; soft contact shadow on the floor; same soft studio light; one image.
```

### 4.3 R09 and R10: outfits and seasons

Hex values are hints; check colours by eye and with 5.3. Attach: R01. Outfit O1 is R01.

**R09: O2 diagram day**

```
CHANGE only: the outfit. She wears outfit O2 (diagram day): a deep-walnut chunky-knit crew-neck pullover that ends at the waist, loose and not fitted, over straight oat-coloured trousers; the cream tick-mark belt (tick marks only, no numbers) on the trousers just below the pullover hem. No vest. No logos, text or patterns. Waist-up, the frame ends at the belt line, both hands outside the picture. Same face, hair and glasses.
OUTPUT: 4:5 portrait; plain warm off-white seamless studio background; same soft studio light; one image.
```

**R09: O3 rain, out**

```
CHANGE only: the outfit. She wears outfit O3 (rain, out): a lightweight matte putty-coloured hooded shell jacket, hip-length, worn open at the front, with the hood down and resting at the back of her neck, over the oat knit top; straight walnut trousers; the cream tick-mark belt visible at the waist in the open front of the jacket (tick marks only, no numbers). No reflective strips, no logos, no visible brand tags, no drawcord ends in the face. Waist-up, the frame ends at the belt line, both hands outside the picture. Same face, hair and glasses.
OUTPUT: 4:5 portrait; plain warm off-white seamless studio background; same soft studio light; one image.
```

**R10: summer (hot and humid)**

```
CHANGE only: the outfit. Summer version of O1: no vest; a short-sleeve oat-coloured linen-look crew-neck top with sleeves ending above the elbow, tucked in; lightweight straight walnut-brown trousers; the cream tick-mark belt at the waist (tick marks only, no numbers). Modest relaxed fit, neckline covers the collarbone. Waist-up, the frame ends at the belt line, both hands outside the picture. Same face, hair and glasses.
OUTPUT: 4:5 portrait; plain warm off-white seamless studio background; same soft studio light; one image.
```

**R10: winter (damp cold)**

```
CHANGE only: the outfit. Winter version of O1: the oat knit top and walnut trousers with the cream tick-mark belt, plus a long chunky open cardigan in putty and a loose scarf in muted sage around the neck. No snow, no maple leaves, no puffer coat, no gloves. Modest relaxed fit. Waist-up, the frame ends at the belt line, both hands outside the picture. Same face, hair and glasses.
OUTPUT: 4:5 portrait; plain warm off-white seamless studio background; same soft studio light; one image.
```

### 4.4 R11, R12, R13: scale reference, belt, glance

**R11: scale reference beside a freestanding door frame.** Attach: R01. This is the adult-scale check. The door height (about 200 cm) and "80 to 85 percent" are design targets, recalled and unverified; judge by eye.

```
CHANGE only: the pose and setting. Full body, front view, standing upright and relaxed beside a plain flat putty-coloured door in a simple frame. The door frame stands alone on the seamless studio floor with no wall around it, so it is clearly a studio set piece. Plain handle, no signs, no numbers, no marks. The top of her head reaches about 80 to 85 percent of the door's height. Both her hands are fully inside her trouser pockets. Plain flat walnut-brown loafers with no logo. 50 mm lens look, eye-level camera, no wide-angle distortion. Nothing else in the picture.
OUTPUT: 4:5 portrait; plain warm off-white seamless studio background; soft contact shadows; the whole door and the full-body figure in frame; one image.
```

**R12: belt flat-lay (object only).** Attach: nothing. Do not paste the Character Lock. A reference for the tick marks.

```
Generate a photorealistic reference image of a single fabric belt laid flat and straight on a plain warm off-white seamless surface, seen from directly above. The belt is cream woven fabric about 3 cm wide, with fine charcoal tick marks printed along one edge at regular intervals like a tape measure: tick marks only, no numbers, no letters, no symbols. A small matte walnut-brown rectangular buckle at one end. Soft diffused light from the front left, soft shadow. Nothing else in the picture: no hands, no person, no text, no logo, no brand mark.
OUTPUT: 3:2 landscape; one image.
```

**R13: glance toward the diagram.** Attach: R01. The pointing pose: arrows are added later in post.

```
CHANGE only: the head position and gaze. Waist-up, the head turned about 20 degrees and the eyes directed to an empty space at the viewer's left, as if looking at something just outside the picture; calm closed-mouth expression. The frame ends at the belt line and both hands are outside the picture. Outfit O1, same face, hair and glasses.
OUTPUT: 4:5 portrait; plain warm off-white seamless studio background; same soft studio light; one image.
```

### 4.5 R14: profile avatar

Easiest route: crop the headshot (R06) or the best expression E01 to E02 in any image editor, square, with the head about 60 to 70% of the height and a little space around it so a circular crop will not cut the hair. Log it as a human edit of its parent. Then: (a) shrink it to about 110 px tall (about 3 cm on a laptop screen, or zoom the browser out) and check section 5 row 1 and the 110 px tell: glasses visible, hair pulled back with a side parting, and the sage vest edge if it is in the crop. (b) Add the small **"AI" chip** in a design tool later (R16); do not generate it.

Optional AI route (attach R01 and R06):

```
CHANGE only: the framing. Head and shoulders only, front view, calm closed-mouth expression, centred, with a little space around the head so a circular crop will not cut the hair. No hands in the picture.
OUTPUT: 1:1 square; plain warm off-white seamless studio background; same soft studio light; one image.
```

---

## 5. Pass/fail checklist

Run this on **every** image you keep, at 100% and 200%, side by side with R01 at the same size. Any single failure in any row (1 to 31) rejects the image; a plastic or airbrushed look (row 25) is the user's own complaint, so it is not optional. Copy the table into your notes once per image you take seriously and tick the boxes.

**Fail codes:** **R** = regenerate (press again, nothing else changes). **P** = edit the prompt (add the matching fix phrase from 9.2, then make 4 more). **E** = fix in an image editor (small and local; log it as a human edit, keep the untouched original; never for hands, faces, or skin). **X** = stop and tell Claude (design problem or a test failed; never "fix" by editing).

### 5.1 The checklist

| # | Check | How to check | Pass | If it fails |
|---|---|---|---|---|
| 1 | **Adult and visible age** | Looks about 30 to 36 at full size and still adult at 110 px tall. Defined cheeks, faint age lines, natural brows. Not a teenager, not in her twenties. The age-guess test in 6.1 settles it | [ ] | P (age fix); X if it persists |
| 2 | **Same face as R01** | Beside R01 at the same size: face shape (softly squared, rounded chin), eye size and spacing, brows, nose, lips, jaw all match. If you hesitate, it fails | [ ] | R; re-anchor if twice |
| 3 | **Skin tone matches R01** | Same light-to-medium warm tone; not whitened, not tanned | [ ] | P |
| 4 | **Hair** | Dark brown-black, side parting, low ponytail with a plain dark-brown tie (not visible from the front; the smooth pulled-back line is), no fringe, a few flyaways, not worn down | [ ] | R / P |
| 5 | **Glasses** | Thin matte walnut rounded-rectangle frames, symmetrical, clear lenses, no glare, both eyes fully visible, arms resting on the ears, no logo; same frame shape as R01 | [ ] | R once; P if 2 of 4 |
| 6 | **Ears** | Both present (or the near ear in profile), natural shape, same as R01, glasses arm sits on the ear, **no earrings** | [ ] | R / P |
| 7 | **Eyes (uncanny check)** | Same size, round natural pupils, both looking the same way, one soft catchlight in each eye in the same place, no glassy or dead stare, no mismatched lids, no extra lashes | [ ] | R; P if 2 of 4 |
| 8 | **Mouth and teeth** | Lips closed in every expression (no parted lips). **No teeth in any image of this pack**; if any show, they must be natural and separate (not one white block) | [ ] | R / P |
| 9 | **Expression matches the request, and she is still the same person** | Compare with the E-ID in 4.1; the face has not drifted | [ ] | R |
| 10 | **Hands** (the top failure) | Prefer none visible. If any hand, wrist or thumb shows, zoom to 200%: count fingers, check joints, nails, thumb side, wrist continuity, no merged or extra digits. A pocket pose must show no fingers or thumbs. Anything odd: fail | [ ] | Follow 9.1; never E |
| 11 | **Arms, shoulders, neck** | Natural anatomy, level shoulders, arm lengths equal, neck not stretched, sleeves end at the wrist | [ ] | R / P |
| 12 | **Build and proportions** | Average-to-slim, no waist, bust or hip shaping or emphasis, head about one seventh of height in full-body (**fail above one sixth**) | [ ] | P |
| 13 | **Feet and shoes** (full-body only) | Two plain flat walnut loafers, correct orientation, no logo, no extra toes | [ ] | R / P |
| 14 | **Outfit** | O1, O2, O3 or an approved variant (addendum 4). Pieces are right: vest only in O1/winter, belt visible where the waist is | [ ] | P |
| 15 | **Clothing consistency and colour** | Same garments and colours as R01. Sample a flat, evenly lit patch of fabric (5.3): inside range and the same colour by eye. No hood over the face; not all black or all white | [ ] | P; E if only a colour cast |
| 16 | **Belt** | Cream fabric belt, fine charcoal tick marks along the edge, **no numerals, letters or symbols**, small walnut buckle, same as R01. Not a real tape measure | [ ] | R; E if only stray numerals |
| 17 | **Jewellery and accessories** | None at all: no earrings, necklace, ring, watch, bracelet, bag, phone. Only glasses, hair tie, belt and buckle | [ ] | R / P |
| 18 | **Modesty and no sexualised cue** | Collarbone covered, relaxed fit, no tight or sheer clothing, no glamour light, no parted-lip pose, no over-shoulder glance, no low camera angle, no body emphasis | [ ] | P; X if it persists |
| 19 | **No logos, brands or plates** | None on clothes, shoes, glasses, buttons, zips, door or background | [ ] | R / P |
| 20 | **Text (garbled or Simplified Chinese included)** | **No text at all**, in any script, even if it looks correct. If Chinese characters do appear, ask the wife whether they are garbled or Simplified and note it in the log (it tells us how the tool behaves) | [ ] | R; E if one small mark |
| 21 | **Background** | Plain warm off-white seamless, even, no gradient, no objects, nothing readable (R11: only the freestanding door frame) | [ ] | P |
| 22 | **Framing and pose as asked** | Matches the prompt (F1 to F5); crop line where asked; arms relaxed | [ ] | R / P |
| 23 | **Studio Look consistent** | Same light direction (front left), neutral-warm muted colour, matte skin, same backdrop as R01 | [ ] | P |
| 24 | **No candid, selfie or "my life" look** | No phone, mirror, arm-length view, motion blur, snapshot crop, room, street, food or product | [ ] | P |
| 25 | **Skin too smooth or plastic** | At 100%, pores and fine texture visible; no waxy sheen, airbrushing or uniform blur; shadows not painted on. A face that is too perfect also fails | [ ] | P |
| 26 | **Edge artefacts** | Hair strands, glasses edges, ear and collar edges are clean; nothing melted or merged | [ ] | R / P |
| 27 | **Overall 100% look** | Does anything look wrong without your being able to say what? Ask the wife. If yes, it fails | [ ] | R; X if it persists |
| 28 | **Resemblance to a real person** | Do you or the wife instantly think of a real person, public or private, or an existing character? A quick look now; the real tests are in 6.2 and 6.3 | [ ] | X |
| 29 | **Colour and objects with political or taboo reading** | At thumbnail size nothing reads as a party-colour camp; no flags, charts, money, religious or mourning objects | [ ] | P; wife decides |
| 30 | **File untouched and markers intact** | The file is the original download, not a screenshot, not re-saved; any visible mark left alone and noted (7.5) | [ ] | Re-download |
| 31 | **Saved, named and logged** | In the right folder with the pack name; a row in the log with tool, model label, prompt, time and licence notes | [ ] | Do it now |

### 5.2 Regenerate, edit the prompt, edit the picture, or stop?

| Situation | Do this |
|---|---|
| One of the four has the defect and the others do not | **R**: it is random. Choose another |
| The same defect appears in 2 or more of 4 | **P**: add the matching fix phrase from 9.2 at the end and generate 4 more |
| Otherwise perfect image, one tiny local flaw (a stray mark, a few numerals on the belt, a slight colour cast) | **E**: fix in an image editor. Never use E for hands, face, skin, proportions or age. Log it as a human edit and keep the untouched file as the parent |
| A visible hand with any defect | Follow 9.1 |
| The same defect after two rounds (8 images) in one tool | Try the other tool with the same prompt. If both fail, **X** |
| Age guess fails, a look-alike is named, or a search shows a close match | **X**: stop and tell Claude; do not repair it by editing |

### 5.3 Colour check: hex, RGB and an allowed range

Hex values are for your colour check only. The prompts name colours in words, because a tool can print a hex code into the picture (*hypothesis*) and that would fail the no-text rule (changed in the cross-pilot check of 2026-10-11; the 步驟 and 色環 packs already worked this way). Image models follow named colours loosely and lighting shifts them. Sample a **flat, evenly lit patch** of fabric that faces the light (not a fold, not a shadow, not an edge) with any eyedropper tool and read the red, green and blue numbers. The "OK range" below is **my suggestion, not a bible rule** (*assumption*, to calibrate): within 16 on each channel, wider than the clay pack because knit texture and light fall-off vary fabric colour. Inside range **and** the same colour by eye as a swatch of the hex: pass. Off by a little more: fix the colour in post and note it in the log. Visibly a different colour (a yellow oat, an orange walnut, a vivid green sage): regenerate or edit the prompt. The eyes, hair and tick marks are too small or dark to sample: check by eye that hair is a dark brown-black (not pure black, not dyed) and the tick marks are dark warm grey.

| Used for | Colour | Hex | R, G, B | OK range red | OK range green | OK range blue |
|---|---|---|---|---|---|---|
| Oat top, O2 trousers | Oat 燕麥 | `#E4D9C3` | 228, 217, 195 | 212 to 244 | 201 to 233 | 179 to 211 |
| Trousers, shoes, glasses, buckle | Walnut 胡桃 | `#6E5440` | 110, 84, 64 | 94 to 126 | 68 to 100 | 48 to 80 |
| Vest, winter scarf | Sage 灰綠 | `#A9B5A0` | 169, 181, 160 | 153 to 185 | 165 to 197 | 144 to 176 |
| Background | Warm off-white 米白 | `#F5F0E6` | 245, 240, 230 | 229 to 255 | 224 to 255 | 214 to 246 |
| Belt | Cream 奶油 | `#EFE6CF` | 239, 230, 207 | 223 to 255 | 214 to 246 | 191 to 223 |
| O2 pullover | Deep walnut 深胡桃 | `#5C4636` | 92, 70, 54 | 76 to 108 | 54 to 86 | 38 to 70 |
| O3 shell, cardigan, door | Putty 灰米 | `#CFC6B4` | 207, 198, 180 | 191 to 223 | 182 to 214 | 164 to 196 |

---

## 6. The human tests, and the reverse-image search

The addendum (section 9) sets the rules and they are **stricter than the clay pack's**. They need other people, so they usually happen on a different day from the generating. The people are helping you test a design; they do not follow, like or comment on any account, and they should not share the pictures. Tell them afterwards what the pictures were for. **Never place a photograph of any real person beside the character to compare.**

### 6.1 Age-guess test (adult-reading check)

1. For each shortlisted image (up to three), make a clean copy with no file name visible, and a copy at about 110 pixels tall. Crops are human edits; log them if you keep them.
2. Find the wife plus **at least five others (six or more in all)**, a mix of ages including at least two over 40, none of whom has seen the pictures. Show each person the pictures **one at a time, in a different random order, with no context**: do not say AI, character, mascot or account.
3. Ask only: **"How old is this person?"** Write the number exactly. If they refuse, ask for a rough range.
4. Do the same with the 110 px copy and, later, the avatar crop. Repeat once for O2 and O3.
5. **Hard fail:** any single guess **under 25**, or a median guess **under 28**.
6. **Warn (use the age fix in 9.2 and retest):** a median of 28 or 29, or any single guess of 25 to 27. **Target:** median 30 to 36.
7. Record the answers in the language given; the wife adds an English gloss.

### 6.2 Blind look-alike test

1. Same people and set-up as 6.1, shown the picture the same way.
2. Ask only: **"Who does this remind you of?"** Write the answer word for word.
3. **Fail** if *any one* person names a real person (public or private) or a specific existing virtual character or influencer. "Someone, I can't say who" is recorded, not failed; two such answers mean you ask the wife a follow-up and run an extra search round.
4. A fail goes in the log. The image is not used. Do not try to "fix" a look-alike by editing; regenerate with a changed attribute (face shape, hair) or tell Claude.

### 6.3 Reverse-image search (manual, public tools only)

Do this for each shortlisted image, on your own computer, by hand.

1. Make working crops (temporary files, no log row needed): **(a) head and shoulders; (b) tight face, forehead to chin.** For the chosen final master add **(c) eyes to mouth; (d) the tight face mirrored left to right** (search engines can miss flipped matches).
2. Use **Google Lens, Bing Visual Search and TinEye** (the current "search by image" pages), uploading the crops yourself. Do not use scripts, bots or scraping; do not log in anywhere you would not normally; **do not use face-recognition people-search services**. Uploading sends the picture to that service, acceptable for a pre-launch design but worth noting in the log.
3. Look at the first two pages of visual matches in each tool, for each crop. Write down any result where **you or the wife think the character looks like a real person**, public or private, and any close match to an existing character or virtual influencer. Record tool, crop and date.
4. Screenshot the result pages into `assets/fangcun/photoreal/lookalike/` with names like `R01_cand_gemini_2_googlelens_crop-b_2026-10-11.png`. Screenshots are evidence, not generated assets: list their names in the log below; no provenance row. They may contain photographs of real people from the search results: keep that folder private, do not commit, post, share or reuse them, and delete them once the check is closed unless a complaint is open.
5. Also run text searches on generic terms (for example "woman glasses low ponytail studio portrait") in the same tools' image results and compare by eye.
6. **The wife's local-public-figure check.** She looks at each shortlisted image and says whether the face resembles any local public figure (news presenter, actress, singer, model, influencer, politician, athlete, TV host) or anyone she knows personally; she writes the name or "the type". Names stay in this internal log only and never go into a prompt. A resemblance to a politician is also a Ground rule 6 problem.
7. If a very close match turns up: do not use the image; tell Claude.
8. Repeat on the final master, on any new outfit family or hair or glasses change, on any model or tool change, on a monthly sample of finals, annually, and on any complaint (take down within 24 hours; pause until a documented check is done).

### 6.4 Near-pair test against the other two pilots

When R01 exists for 色環 and 步驟 as well: put the three front waist-up images in one row at about 110 px tall, on a laptop and on a phone. Ask the wife and at least four others (five viewers or more; the age-guess panel can be reused), two seconds each: "Same person, sisters, or different people?" **Pass:** all say different people. **Fail:** two or more say same person or sisters for any pair. Fix by changing a design attribute of the character that fails (for 方寸: shorter hair, a different frame shape, a different vest colour), not by editing. Detail: addendum 10 and `README-photoreal.md` section 3.

### 6.5 Mistaken-for-real check (informational, not pass/fail)

Show the chosen master to the same people **without** any badge and ask: "Is this a real photo or AI?" Write the answers. It calibrates how much the label must do: if most say "real photo", the badge, the first caption line and the avatar chip matter even more (they are already mandatory). Never use the result to make the picture look *more* real.

### 6.6 The log to keep

| Date | Candidate or asset | Tools, crops and searches | Search result | Wife's check | Blind-test answers | Age guesses | Verdict | Checked by |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

Age-guess tally (one row per person; "under 25?" is yes if the guess is below 25):

| Person (initials) | Full-size guess | Thumbnail guess | Under 25? | "Reminds me of" (verbatim) |
|---|---|---|---|---|
| Wife | | | | |
| | | | | |

---

## 7. Provenance, licence and labelling

### 7.1 Columns and a ready-to-fill example

The rule (Ground rule 2): **every kept file and every discarded-but-considered file gets one row in `assets/provenance.csv`, the same day.** "Considered" means you saved it, compared it, shortlisted it or used it as a reference. Edited versions are separate files with their own rows that name the parent.

Columns, in order: `timestamp,asset_path,persona,tool,model,prompt,licence_notes`.

- `timestamp`: Taiwan time with offset `+08:00` when you generated it.
- `asset_path`: from the project folder, for example `assets/fangcun/photoreal/candidates/R01_cand_gemini_1.png`.
- `persona`: `fangcun` until the real handle is chosen.
- `tool`: what you actually used, for example "Gemini (app)" or "ChatGPT (app)". For an edit, the editor's name; for a hand-made file, "human-made in <app>".
- `model`: the label **exactly as the app shows it that day**. If none is shown: "not shown in app, YYYY-MM-DD". Never guess. For an edit: n/a.
- `prompt`: the **full text you sent**, including the Character Lock, and a note of which files were attached (only R01 and other golden images; never any other picture). If you changed even one word (for example the wording option in section 2), log the changed text.
- `licence_notes`: the template in 7.3.

This is an **example only**. Do not paste it as it is. Replace every `<...>` with the real value, and add only the second line to the real file.

```
timestamp,asset_path,persona,tool,model,prompt,licence_notes
<YYYY-MM-DDTHH:MM:SS+08:00>,<assets/fangcun/photoreal/candidates/R01_cand_gemini_1.png>,fangcun,"Gemini (app)","<model label exactly as shown in the app today>","<PASTE THE FULL PROMPT EXACTLY AS SENT. Attached files: none.>","Status: <KEPT | KEPT (provisional master) | DISCARDED-CONSIDERED>; reason: <one word>; parent file: none (raw download); reference images attached: none; human edits: none (raw); prompt ID: R01-Gemini; tool plan: <plan name shown in my account>; terms read on <YYYY-MM-DD, or: not yet read> at <page name or link, or: none>; commercial use per those terms: NOT CONFIRMED; visible mark or label on file or in the app: <none seen | describe>; conversation link or ID: <link>; seed: <none shown | number>"
```

### 7.2 Rules that keep the file valid

- One row per file. Four images from one prompt are four rows with the prompt cell copied down. Rejected-on-sight images that you saved get a row with one word of reason.
- Edit the CSV in a spreadsheet app and paste each field into its own cell; the app adds the quotes and handles commas, line breaks and double quotes. If you edit it as plain text, put every field that contains a comma, a line break or a quote in double quotes, and double every quote mark inside it. Save as CSV (UTF-8 if offered).
- Do not edit or delete old rows. Corrections go in a new row. Add yours at the bottom (other characters' rows share the file).
- You can paste your notes (file names, tool, model label, time, which prompt, any wording you changed) to Claude Code and ask it to write the rows. Claude cannot see your screen, so it needs the model label and the time from you.
- Search crops used only for the reverse-image search are temporary and need no row (6.3).

### 7.3 `licence_notes` template (fill the blanks)

```
Status: ___ (KEPT | KEPT (provisional master) | DISCARDED-CONSIDERED); reason: ___; parent file: ___ (none (raw download) | file name); reference images attached: ___ (none | R01_master_v1.png ...); human edits: ___ (none (raw) | crop | colour fix | numerals erased | badge added | other); prompt ID: ___ (for example R02); tool plan: ___ (the plan name shown in my account); terms read on ___ (date) at ___ (page name or link); commercial use per those terms: ___ (CONFIRMED | NOT CONFIRMED | RESTRICTED: what); visible mark or label on file or in the app: ___ (none seen | describe); conversation link or ID: ___; seed: ___ (none shown | number); hand check at 200%: ___ (no hand visible | pocket pose, no digits visible | other)
```

### 7.4 Licence reminder

**The commercial-use terms of your Gemini and ChatGPT subscriptions have not been checked.** Before any commercial use (a public account, a sponsored post, a client sample), read the **current** terms for the exact tool and plan, and fill in "terms read" and "commercial use" from what they actually say. Questions to answer from the text, not from memory: who owns the images or what rights you get; whether commercial use is allowed **on your plan**; limits on using outputs as a recurring character or brand asset; **what the terms say about realistic images of people and any duty to disclose AI generation**; what they say about visible marks, invisible watermarks and removing them; rules about uploaded reference images (you upload only the character's own images); when the terms last changed. Terms can differ between tools, plans, and the app and a developer interface, and they change. Save a dated screenshot or PDF of the page. If anything is unclear, write NOT CONFIRMED. Until it is recorded, every image is **internal design material only**. Whether purely AI-generated images can be protected by copyright is an open question for the lawyer (`research/legal.md` 8.2); light human edits with the layered file kept are how the studio documents its own contribution (and **no skin smoothing**).

### 7.5 Labelling reminder (read before you export anything)

- **Save the file as the app downloads it. Do not strip metadata.** Use the download button, not a screenshot, not "save for web", not a converter. Some tools put an AI marker in the file or add an invisible or visible mark (*hypothesis, unverified*: for example Meta reads industry markers such as C2PA or IPTC to apply "AI info", and YouTube locks its label on content with generative markers; `research/platforms.md`). Whether Gemini or ChatGPT add such markers is checked in the app and the file properties and **noted in the log**. If you see a mark, leave it and note it; do not remove any mark until you have read what the terms say.
- **An editor may drop the markers on export.** When you add the badge, the chip or text in a design tool, check whether the exported file keeps its metadata (the editor's export or file-properties screen) and write the result in the log. Because auto-detection cannot be relied on, **always switch on the platform's AI label by hand**.
- **The on-screen badge is added in editing, never generated.** `AI 生成｜示意圖` on diagram and room slides, `AI 生成｜虛擬角色` on slides that show her (wife rules, addendum 12 item 7). Solid charcoal pill, off-white text, text height at least about 3.5% of the image height, inset at least 11% of the height from the top and bottom edges and at least 8% of the width from the sides (so a centred square crop of a 4:5 picture cannot remove it; see pipeline/qa-checklist.md D3), on **every** image and every video frame. The wife reads every character. The avatar gets a small corner chip reading `AI`.
- **Platform labels at posting time:** Instagram, the AI-generated profile label on the account (checked on a Taiwan test account first) and the content-level AI disclosure on every post; YouTube, the altered or synthetic content disclosure on every Short plus the description line; the AI-disclosure control on any boosted or partnership post. Bio and first caption line follow bible section 8.
- **Alt text** on every image (AI draft, the wife corrects): 「AI 生成的虛擬角色方寸，示意圖，非真人。」
- **No location tag, no map pin, ever.**
- Nothing made with this pack goes on any account yet: the reading test, lawyer answers, the Instagram label check, licence terms and STOP 3 come first.

---

## 8. A note for the wife

Thank you for looking at these. You are judging **language, culture and how it feels**, not the technology. The operator checks hands, anatomy and numbers. Please look at each picture the way a Taiwanese viewer scrolling Instagram would, and say **APPROVE**, **SMALL FIX** or **REJECT** with a short reason. If you are not sure, say "unsure" and why. Reason codes (from the bible, 10.1): **X** cultural or visual error, **S** script or font problem, **P** politics or sensitive colour, **H** hands, people or other AI defect, **T** tone. About 15 minutes for a shortlist of three is my estimate. The zh-TW terms are an AI draft; correct them freely. **Please do not compare the pictures with photos of any real person; judge from memory.** If a picture reminds you of someone you know personally, say "someone I know" and you need not give the name.

| # | Look at | zh-TW words to look for | Your answer |
|---|---|---|---|
| 1 | Does she look like a **grown-up in her early thirties**? Not a student, not much older? | 成熟、穩重、像三十出頭 (good) / 太年輕、像大學生、像高中生、童顏、太老 (not good) | |
| 2 | Is the face **natural and ordinary**, like a woman you could meet in Taiwan? Or a template? | 自然、像一般人 (good) / 偶像臉、網美臉、韓系或日系偶像感、過度精緻 (not good) | |
| 3 | Does the face look **real or strange**? Eyes, teeth, ears, skin, glasses | 自然 (good) / 詭異、空洞、不自然、塑膠感、蠟像感、恐怖谷 (not good) | |
| 4 | Does she **remind you of a real person**? A local public figure (presenter, actress, singer, model, influencer, politician, athlete), or someone you know | 像不像某位藝人、主播、模特兒、網紅、政治人物、運動員，或你認識的人？像誰？ | |
| 5 | **Styling:** glasses, low ponytail, sage vest, cream belt. Natural or costume? Does the belt look like a tape-measure motif, a tradesperson's belt, or silly? | 自然、日常 (good) / 像制服、像工人、像 cosplay、很刻意 (not good) | |
| 6 | **Modesty and tone.** Right for Taiwan? Any glamour or "sexy" impression? | 端莊、得體 (good) / 性感、勾人、太貼身、太拘謹 (not good) | |
| 7 | **Colour impression** at small size. Any political or camp impression? Any all-black or all-white look? | 有沒有藍、綠、白的政黨色聯想？全黑、全白 (喪事色) | |
| 8 | **Any writing at all** on the picture. There should be none. Numbers on the belt? | 文字、數字、簡體字、亂碼、日文或港式字形 | |
| 9 | **The plain studio background.** Fine, or does it feel lifeless or "fake"? | 乾淨、可以 / 空洞、假、沒生氣 | |
| 10 | **Would a Taiwanese viewer think this is a real person?** Is it clear it is AI? (informational) | 看起來像真人嗎？標示明不明顯？ | |
| 11 | **Taboo objects.** There should be none | 神明桌、香、紙錢、白菊花、數字 4 | |
| 12 | **Logos or brand marks** on clothes, glasses, shoes | 商標、品牌標誌、車牌 | |
| 13 | **Rulings the addendum asks of you** (pronouns, feature wording, badge wording, summer wardrobe, jokes, near-pair with 色環) | See addendum section 12 | |

Not needed from you: hands, anatomy, numbers, measurements, whether it is "good AI", the name 方寸 (a separate reading test, bible gate G2).

---

## 9. Common failure modes for this character, and fixes

### 9.1 Hand fix procedure

Prevention first: the master prompts keep hands out of the frame, and the standing prompts use trouser pockets. Run the 200% inspection (2.5) on every kept image.

**Finger check (when any hand, wrist or thumb is visible).** Count five fingers on each hand. Check there is one thumb, on the correct side. Check knuckles and joints bend naturally, no merged or doubled fingers, no extra joints, nails natural, the wrist joins the forearm, the cuff is continuous, the fingers are not melting into the pocket or sleeve. If you cannot tell, it fails.

**Ladder (stop at the first rung that gives a passing image):**

1. **Reframe.** If the rest of the image is perfect and the hand is at the edge, crop it out in an image editor, as long as the crop still matches the framing in the prompt (a waist-up with the belt visible). Log it as a human edit (crop) of its parent.
2. **Re-roll.** Send the same prompt again for 4 new images and choose one that passes.
3. **Prompt fix.** Add one line at the end: `Both hands are outside the picture; the frame ends at the belt line.` or, for standing poses, `Both hands are fully inside her trouser pockets; no fingers or thumbs are visible.` Make 4 more.
4. **One conversational edit.** In the same chat ask: `Same image, but hide both hands: put them fully inside the trouser pockets.` or `Same image, reframed so the frame ends at the belt line.` (*hypothesis*: the tool may support edits). One try only, then inspect again at 200%. Do not stack repeated edits: faces drift.
5. **Switch tool** and repeat 2 and 3.
6. **Stop.** Discard the image. **Never paint or redraw a hand by hand, never publish an image with a visible odd hand.** A published hand defect is an N9 tripwire (addendum 8.3). Tell Claude if both tools fail the same way after two rounds each; the pose may need to change.

### 9.2 Symptoms and fix phrases

To use a fix phrase: add it at the end of the prompt (after the Character Lock and the prompt), regenerate 4, and see whether 3 or more now pass. In the same chat you can instead say "Same image, but: <phrase>" for a small fix.

| Symptom | Likely cause (hypothesis) | Fix phrase |
|---|---|---|
| Plastic, waxy, airbrushed or glowing skin | Beauty-render default | `Natural skin texture with visible fine pores and subtle tonal variation; matte; no airbrushing, no beauty filter, no glow, no shine.` |
| Idol, model or influencer look; over-pretty | Portrait default | `An ordinary everyday face with natural mild asymmetry, not a beauty-campaign model, no glamour, no idol look.` |
| Looks too young or like a student | Generators drift young | `She looks clearly in her early-to-mid thirties: faint smile lines at the corners of the eyes, faint lines from the nose to the corners of the mouth, defined cheeks, a mature composed expression; not a teenager, not in her twenties.` |
| Looks too old or tired | Overcorrected | `Early thirties, not middle-aged: only faint fine lines, healthy even skin tone, no deep wrinkles, no grey hair.` |
| Hands or fingers appear | Generators love hands | Follow 9.1 |
| Teeth show, or look odd | Smile default | `Lips closed, no teeth visible.` |
| Glasses wrong: asymmetrical, tinted, glare, a different frame, no glasses, fused to the face | Eyewear is hard | `Thin matte walnut-brown rounded-rectangle glasses, symmetrical, clear lenses with no reflection or glare, both eyes fully visible through the lenses, the arms resting on the ears, no logo.` |
| Ears missing, odd, or earrings appear | Hair and jewellery defaults | `Both ears natural and visible at the sides, partly behind the glasses arms; no earrings, no jewellery.` |
| Uncanny eyes: different sizes, glassy, looking different ways, odd pupils | Eye detail | `Both eyes the same size with natural round pupils, both looking at the camera, one soft catchlight in each eye in the same place, no glassy stare.` |
| Hair worn down, or a fringe appears | Portrait default | `Hair pulled back into a low ponytail at the nape with a plain dark-brown tie, side parting, no fringe, forehead partly visible.` |
| Belt shows numbers or letters | Tape measures "should" have numbers | `The belt has fine charcoal tick marks only: no numbers, no letters, no symbols. No text anywhere in the picture.` If it persists, use a plain cream belt and add ticks by hand in post (log it) |
| Jewellery, watch or accessories appear | Portrait default | `No jewellery of any kind, no watch, no bag, no phone, nothing in her hands.` |
| Costume drift: apron, uniform, hood over the face, tight or revealing clothing, all-black or all-white | "Helper" association or glamour default | `Plain relaxed knitwear and simple layers only: no uniform, no apron, no logos or text on clothing, neckline covers the collarbone, hood down, nothing tight or revealing.` |
| Glamour or sexualised feel: parted lips, over-shoulder look, low angle, soft-focus glow | Female portrait default | `A neutral composed pose, eye-level camera, direct calm gaze, modest relaxed clothing, no glamour lighting, no parted lips, no body emphasis.` |
| Background becomes a room, office, street or gradient | Not told strongly enough | `Plain warm off-white seamless studio background, evenly lit, no gradient, nothing else in the picture.` |
| Looks like a phone selfie or a candid snapshot | Realism default | `A polished studio character-reference portrait, not a phone snapshot, not a selfie, not candid.` |
| Face drifts from R01 with each picture | Building on the last output | New chat, attach only R01, resend. Never use a new output as the only reference twice in a row |
| Skin tone lightens or darkens | Lighting default | `Exactly the same skin tone as the reference image: light-to-medium, slightly warm; do not lighten or darken.` |
| Features look stereotyped or not ordinary | Generator defaults | `Ordinary, natural, unexaggerated features, no stereotype, no exaggeration.` |
| Colours drift: yellow oat, orange walnut, vivid green sage | Colour words are only hints | `Use only the muted palette: oat knit top, muted sage vest, walnut trousers, shoes and glasses, cream belt, on a warm off-white background; no saturated blue, green, teal, red or yellow.` |
| Door picture (R11) becomes a room, or gets perspective or text | Scene default | `A freestanding door frame standing alone on the seamless studio floor, no wall, no room. Orthographic eye-level view, no wide-angle distortion, no signs, no numbers.` |
| Head too large in full-body | Portrait default | `Natural adult proportions: the head is about one seventh of her standing height.` |
| Feet or shoes odd (full-body) | Feet are hard | `Two plain flat walnut-brown loafers, correct orientation, no logo, both fully visible.` |
| A visible mark or watermark appears | Tool behaviour | Leave it, note it in the log (7.5), do not remove it |
| The long avoid list makes the app draw the things it names | Naming a thing can summon it (hypothesis) | Use the short fallback below |
| She reminds a tester of someone, or a search shows a close match | The face itself | **X**: tell Claude. Regenerate with a changed attribute; never edit |
| Thumbnail loses the glasses or looks like a teenager | The design or the prompt | Tell Claude. Do not edit around it |

### 9.3 Short avoid fallback (only if the long list backfires)

```
Avoid: hands, fingers; any resemblance to a real person; airbrushed or plastic skin; teeth showing; jewellery; text, letters, numerals, logos, watermarks; a selfie or snapshot look; revealing or tight clothing; other people.
```

---

## 10. When you stop for the day

Tell Claude: which tool made the chosen R01 and the exact model label; which images you kept and discarded; the minutes you spent; which checklist rows failed most often (row 10, hands, will be the one to watch); whether any tool refused a prompt, added a visible mark, or showed a seed; whether the face drifted between chats; the licence terms you read (date, page, plan, the key sentence) or "not yet"; and what the wife said, including her answers to the open items in the addendum (section 12). Claude can then update the bible's status, record the tool test in `pipeline/tools.md`, write the provenance rows from your notes, and set up the next sitting.

**Nothing from this pack is approved** until the age-guess test, the look-alike tests, the reverse-image search, the near-pair test, light hand-finishing (no skin smoothing) and the approvals by the wife and the operator are done. The name 方寸, the studio name and the handle are still unchecked and are not part of this session. No post, account or client work is made from these images.
