# 色環 (sehuan) PHOTOREAL image pack: first reference images

**Pack v1 (photoreal), written 2026-10-11.** For the operator (English only) and the wife (language and culture review). Source of truth: `personas/sehuan/photoreal-addendum.md` ("the addendum"), then `personas/sehuan/bible.md` for everything the addendum leaves alone. If this pack and the addendum ever disagree, the addendum wins; tell Claude and the pack gets fixed.

**This pack replaces the illustration pack (`sehuan.md`) for 色環.** The user rejected the stylised look ("looks so fake, I need real people", `DECISIONS.md` 2026-10-11). The decision is recorded as **photorealistic AI-generated characters that stay openly AI**. The old pack is kept for history; do not use its prompts.

**Start with `pipeline/image-pack/README-photoreal.md`** (which pilot first, time, how to log, what to send back, why the labels still apply). **Status of everything you make with this pack: working references, not approved assets.** Nothing is cleared for public use until the master passes the checklist (section 5), all the human tests (section 6), light hand-finishing, and the wife and operator approve it. Nothing has been generated yet; no photoreal reference image exists. The name 色環, its handle and the studio name are also unchecked and are not part of this session.

**Save everything here:** `/home/user/Taiwan-AI-Influencers/assets/sehuan/photoreal/` (from the project folder: `assets/sehuan/photoreal/`). The folder already exists with a `.gitkeep` placeholder. The older folder `assets/sehuan/` belongs to the illustration pack; do not mix the two.

**How to use it:** read sections 0 and 1, then do sections 2 and 3 in order. Keep section 5 (checklist) and section 7 (log) open while you work. Copy the contents of each code box exactly as written. Model names, buttons and features in Gemini and ChatGPT change often, so **every statement about them below is a hypothesis**: check the current screen.

---

## 0. One-screen summary

**Who.** 色環 (the word means "colour wheel"; how to say it is the wife's call) is a fictional adult woman, stated age 30, shown in photorealistic studio portraits. She is an **AI character**, not a real person, and every image says so. She will explain colour and outfit logic to Taiwan audiences on Instagram and Threads. You can recognise her by four things. First, matching round drop earrings that look like a colour wheel of twelve muted segments. Second, shoulder-length dark hair with a side parting, one side tucked behind the ear so the earring shows. Third, one small persimmon accent (a soft terracotta orange), never more than about a tenth of the picture. Fourth, a ring of exactly six blank colour-chip cards clipped at her hip or bag strap, visible from the knees up. Her default outfit is a relaxed warm stone-grey blazer worn open over a cream knit top, with a small persimmon neckerchief, charcoal trousers and flat loafers. She is **a presenter, not a wearer**: she has never worn, bought or tested anything, her three outfits are her fixed design, and her pictures are plain studio portraits. No rooms, no places, no props in her hands, no hands at all.

**Goal of the first session.**
1. Pick one master portrait (R01, waist-up, front, outfit A) that passes the checklist.
2. Use it to make the next images: three-quarter left and right, side, back and headshot (R02 to R06).
3. In later sittings: the ten expressions, the framings, the outfits, the seasons, the earring and chip-ring stills, the glance and the avatar (section 4).
4. Log every file the same day. The tests with other people, light hand-finishing and the freeze of the set come after.

**Three things that matter most.**
- **Hands are the top failure.** Every prompt keeps them out of the frame or inside pockets. Section 9.1 is the fix procedure.
- **She must never look like anyone real, and must not look like 方寸 or 步驟.** You run a reverse-image search by hand and the wife looks for resemblance (section 6). A look-alike is a hard fail.
- **Every image is labelled.** Save files untouched, add the on-screen badge only in editing, switch on the platform's AI label (section 7.5).

**Time (my estimate, not measured).** Sitting 1 about 2 hours (set-up, R01 in both tools, shortlist). Sitting 2 about 2 to 2.5 hours (R02 to R06). Sitting 3 about 3 to 4 hours (section 4). About 15 to 20 minutes of the wife's time on the shortlist. About 1.5 to 2 hours on another day for the tests. That is roughly 7 to 9 hours of your time against a 6-hour weekly budget, so plan two weeks. Write down your real minutes; the studio's capacity plan needs them.

**Order of work.**

| Step | What | Where |
|---|---|---|
| 1 | Make the sub-folders and open the log (5 to 10 min) | Section 1 |
| 2 | R01 prompt in Gemini (4 images) and in ChatGPT (4 images) | Section 2 |
| 3 | Reject pass, checklist, shortlist at most 3 | Sections 2.6, 5 |
| 4 | Wife looks at the shortlist without knowing which tool made which; you run the reverse-image search | Sections 8, 6.3 |
| 5 | Choose a provisional master, save as `R01_master_v1` | Section 2.6 |
| 6 | R02 to R06 with R01 attached each time (sitting 2) | Section 3 |
| 7 | Earring and chip-ring stills, expressions, framings, outfits, seasons, glance, avatar (sitting 3) | Section 4 |
| 8 | Log as you go, not at the end | Section 7 |
| 9 | Another day: age-guess test, blind test, near-pair test, light hand-finishing, freeze the set (with Claude) | Section 6, addendum 9 to 11 |

---

## 1. Before you start

- **Tool: start with Gemini, then run the same prompt in ChatGPT (hypothesis, not a finding).** Gemini's conversational recipe is the simpler start; ChatGPT's labelled-block recipe is more structured. Nobody has tested either on this character, which is what today finds out. Once R01 is chosen, stay in the tool that made it for the follow-ups (hypothesis: one tool keeps the face more consistent).
- **Settings to look for, only if available.** Image shape or aspect ratio (4:5 portrait for most images, 1:1 for headshots and the avatar; if there is no setting, each prompt's OUTPUT line asks for it). Number of images per request (set 4; if not offered, send the prompt again until you have 4 separate images, and do not ask for "a grid of 4"). Highest quality or resolution. A model or version picker (pick one and keep it for the whole sitting; **copy its label exactly**). Style presets or filters: leave **off**, so only the prompt sets the look. Chat history: do not use a temporary or private mode, you need the conversation link for the log. Use the download button for the largest version; a screenshot is the last resort (it loses file markers, see 7.5) and must be noted in the log.
- **Uploads: the only image you may ever upload is this character's own generated image** (R01 and the other golden images from this pack), and a plain colour swatch. **Never** upload a photograph of any real person (family, friends, colleagues, models, public figures, yourself), never an image of **any other character, including 方寸 and 步驟**, never a picture, screenshot or fan art of any existing character or virtual influencer, and never a photo of a real room or garment. Not "just for the face shape", not "just for the pose", not "just for the lighting". Describe things in words, as the prompts do.
- **Never type into a prompt** a real person's name, a celebrity, influencer, model, actor, existing character, or the words "looks like" or "in the style of" followed by any of those. No real brand, logo or number plate. The look-alike tests in section 6 are done by eye on the finished picture; no name ever goes into a prompt.
- **Colours are written as words, not hex codes.** Tools sometimes print a hex code into the picture, and photographic light changes the colour anyway (hypothesis). The hex values appear only in the colour check (5.3).
- **Outfits are her fixed design.** She does not try, test or review clothes. Never ask her to hold, use, taste, try on or show any object, never name a garment brand or product, and never ask for a mirror, fitting room or "outfit of the day" look.
- **No text in the picture.** Any text in any script on a generated image fails it (the chip cards and the earring must carry none). Chinese text and the badge are added later in a design tool, and the wife reads every character.
- **Save everything and log everything.** Download every image you look at for more than a glance into `assets/sehuan/photoreal/` (candidates go in its `candidates` folder) with the file name from this pack. Do not edit or rename-over the original download. Delete nothing today. One row per file in `assets/provenance.csv` the same day (section 7).
- **Licence terms are NOT checked.** This pack does not know what Gemini or ChatGPT allow for commercial use on your plan, or what they say about realistic images of people. Before any commercial use, read the current terms for the exact tool and plan, and record the date and the key sentence in `licence_notes` (7.4). Until then every image is internal design material only: no client work, no sponsored post, no public account.
- **Do not strip or remove any mark** the tool adds (visible, or in the file). Note it in the log (7.5).
- **Use a separate chat for this character.** Never continue a chat in which you made 方寸 or 步驟. A generator reuses its default face, and a cross-contaminated chat is the commonest cause of "they look like sisters" (addendum 10).

**Set-up (about 5 to 10 minutes).**
1. The folder `/home/user/Taiwan-AI-Influencers/assets/sehuan/photoreal/` already exists (with a `.gitkeep`). Inside it make two folders: `candidates` (every image you considered but did not choose) and `lookalike` (screenshots from section 6).
2. Open `assets/provenance.csv` in a spreadsheet app. The header must read `timestamp,asset_path,persona,tool,model,prompt,licence_notes`. Do not change it. Add rows at the bottom.
3. Copy the Character Lock (2.7) into a notes file so you can paste it quickly.
4. In the same notes file, start a line "minutes: " and add your times as you go.

---

## 2. STEP 1: the master portrait R01

**What you are making.** One picture: a waist-up (half-body) front portrait of the fictional person, calm closed-mouth expression, outfit A, plain dusty-blush studio background, 4:5 portrait. The frame ends at the waist, just below the lowest blazer button, so **both hands are outside the picture**. The chip ring is clipped at the hip and is therefore out of frame in this image; it enters at the knees-up shots. Everything later is built from this image, so spend the time here.

The two prompts below carry the same design. The Gemini one opens conversationally and ends with a "Please avoid" sentence; the ChatGPT one uses labelled blocks and an AVOID block. The wording that describes her is identical.

**Wording decision for the wife (open).** The line `East Asian, with ordinary, natural, unexaggerated features, not an idol or model look` is the neutral default. If the wife wants different wording, swap that exact phrase for one of these in both prompts and write the changed prompt in the log:
- Option B: `East Asian, with ordinary, natural, unexaggerated features that read as Taiwanese, not an idol or model look`
- Option C: `an ordinary adult you could plausibly see on an everyday street in a large East Asian city, with natural, unexaggerated features, not an idol or model look`
- Option D (features only, no region): delete the words `East Asian, ` and keep `with ordinary, natural, unexaggerated features, not an idol or model look`. The wife then judges whether the result looks plausible for Taiwan. A generator may drift to a different default face, so expect more rejects (hypothesis).

Run today's prompts with the default unless she has already answered.

### 2.1 Gemini: paste this

```
Create a photorealistic image from this brief.

Generate a fictional person. She is an original character with no real-world counterpart and must not resemble any real individual.

SUBJECT: an adult woman of about thirty (she looks about 30 to 35), East Asian, with ordinary, natural, unexaggerated features, not an idol or model look. An oval face of medium length, widest at the cheekbones, tapering to a narrow, softly rounded chin, with softly defined cheekbones and a gentle jaw shadow. Almond-shaped dark-brown eyes of modest size with slightly upturned outer corners and a natural eyelid fold, a calm level gaze. Straight dark brown-black eyebrows of medium thickness. A small-to-medium nose with a soft tip. Natural medium lips in a muted terracotta-brown, closed in a very slight, calm, faintly asymmetric smile, no teeth showing. Medium, warm golden-beige skin tone, even, with natural skin texture: fine pores visible, faint fine lines at the outer corners of the eyes and faint lines from nose to mouth at rest, soft natural under-eye shadow. Minimal natural makeup: no blush, no eye makeup emphasis, no gloss, no glow.

HAIR: natural dark brown-black, shoulder-length with a blunt-cut line, straight with very slight natural movement, a deep side parting on her right (the viewer's left), no fringe over the forehead. The hair on her left side (the viewer's right) is tucked behind her left ear so that the ear and the earring are fully visible; the hair on her right side falls forward past the cheek to the shoulder and mostly covers her right ear. A few natural flyaways. Not dyed, no highlights, not glossy, no clips or hair accessories.

EARRINGS: a matching pair of round drop earrings. Each is a flat, matte, enamel-look disc about 2.5 to 3 cm across, hanging from a small plain hook, divided into twelve equal wedge segments like a colour wheel in dusty, muted colours, going round in this order: dusty red, red-orange, soft orange, golden yellow-orange, muted yellow, yellow-green, sage green, blue-green, dusty blue, blue-violet, soft violet, red-violet. No gloss, no gems, no metal rim detail, no numbers, no letters. The left earring is clearly visible.

OUTFIT (A): a relaxed, unstructured single-breasted blazer in warm stone grey (a soft grey-beige), worn open, with plain buttons; under it a cream fine-knit crew-neck top (cream with a faint peach-pink cast, not yellow) whose neckline covers the collarbone; at the collar, a small neckerchief in persimmon (a soft, muted terracotta-orange, not bright orange, not red) made of matte cotton-linen, folded into a narrow band and loosely knotted at the front, not shiny, not satin, not tight at the throat. Relaxed modest fit. No logos, text, tags, labels or patterns on any clothing. No other jewellery.

POSE AND FRAMING: waist-up portrait. The frame ends at the waist, just below the lowest blazer button, so both hands are outside the picture, below the frame. Arms relaxed at her sides, shoulders level and relaxed, upright calm posture. Body and head facing the camera, calm direct gaze at the lens. Eye-level camera.

STYLE: a polished studio character-reference portrait, not a phone snapshot and not a candid photo. 85 mm lens look, no wide-angle distortion. One large soft diffused light from the front right at about 40 degrees, slightly above eye level, with gentle fill from the left. Neutral-warm colour balance, soft natural shadows, matte skin without shine, fabric weave visible and matte, one soft window-shaped catchlight in each eye at the upper right. Muted, low-saturation colour grade. Plain dusty-blush seamless studio background (a muted pinkish-peach, not bright pink, not white, not cream, not grey), evenly lit, no gradient, no vignette. No filters, no film grain, no beauty retouching.

OUTPUT: 4:5 portrait, one image.

Please avoid: hands or fingers anywhere in the picture; any resemblance to a real person; an idol, model or beauty-filter look; airbrushed, plastic, waxy or over-smooth skin; glowing, glossy, whitened or brightened skin; enlarged doll-like eyes; heavy eye makeup, eyeliner wings, blush, glossy lipstick; teeth showing; laughing or an open mouth; tears; a baby-faced or teenage look; a fringe over the forehead; hair tied back, a ponytail or pigtails; dyed or highlighted hair; hair clips or accessories; glasses; necklaces, rings, watches, bracelets or any jewellery other than the two colour-wheel earrings; text, letters, numerals, hex codes, logos, brand marks, watermarks, signage; a selfie, phone-camera, mirror or candid snapshot look; a fitting room, wardrobe, hanger or shopping bag; other people, children, pets; real places or landmarks; a colour swatch or fabric held near her face; revealing, tight, sheer, low-cut or sleeveless clothing; a sexualised or glamour pose; a uniform, an airline-crew or shop-staff look, a satin or shiny neckerchief; a school uniform; saturated red, blue, green or yellow clothing; an all-black or all-white outfit; rainbow stripes or flags; mismatched eyes or ears; extra or missing fingers.
```

### 2.2 ChatGPT: paste this

```
Generate one image from the brief below.

Generate a fictional person, photorealistic. She is an original character with no real-world counterpart and must not resemble any real individual.

SUBJECT: an adult woman of about thirty (she looks about 30 to 35), East Asian, with ordinary, natural, unexaggerated features, not an idol or model look. An oval face of medium length, widest at the cheekbones, tapering to a narrow, softly rounded chin, with softly defined cheekbones and a gentle jaw shadow. Almond-shaped dark-brown eyes of modest size with slightly upturned outer corners and a natural eyelid fold, a calm level gaze. Straight dark brown-black eyebrows of medium thickness. A small-to-medium nose with a soft tip. Natural medium lips in a muted terracotta-brown, closed in a very slight, calm, faintly asymmetric smile, no teeth showing. Medium, warm golden-beige skin tone, even, with natural skin texture: fine pores visible, faint fine lines at the outer corners of the eyes and faint lines from nose to mouth at rest, soft natural under-eye shadow. Minimal natural makeup: no blush, no eye makeup emphasis, no gloss, no glow.

HAIR: natural dark brown-black, shoulder-length with a blunt-cut line, straight with very slight natural movement, a deep side parting on her right (the viewer's left), no fringe over the forehead. The hair on her left side (the viewer's right) is tucked behind her left ear so that the ear and the earring are fully visible; the hair on her right side falls forward past the cheek to the shoulder and mostly covers her right ear. A few natural flyaways. Not dyed, no highlights, not glossy, no clips or hair accessories.

EARRINGS: a matching pair of round drop earrings. Each is a flat, matte, enamel-look disc about 2.5 to 3 cm across, hanging from a small plain hook, divided into twelve equal wedge segments like a colour wheel in dusty, muted colours, going round in this order: dusty red, red-orange, soft orange, golden yellow-orange, muted yellow, yellow-green, sage green, blue-green, dusty blue, blue-violet, soft violet, red-violet. No gloss, no gems, no metal rim detail, no numbers, no letters. The left earring is clearly visible.

OUTFIT (A): a relaxed, unstructured single-breasted blazer in warm stone grey (a soft grey-beige), worn open, with plain buttons; under it a cream fine-knit crew-neck top (cream with a faint peach-pink cast, not yellow) whose neckline covers the collarbone; at the collar, a small neckerchief in persimmon (a soft, muted terracotta-orange, not bright orange, not red) made of matte cotton-linen, folded into a narrow band and loosely knotted at the front, not shiny, not satin, not tight at the throat. Relaxed modest fit. No logos, text, tags, labels or patterns on any clothing. No other jewellery.

POSE AND FRAMING: waist-up portrait. The frame ends at the waist, just below the lowest blazer button, so both hands are outside the picture, below the frame. Arms relaxed at her sides, shoulders level and relaxed, upright calm posture. Body and head facing the camera, calm direct gaze at the lens. Eye-level camera.

STYLE: a polished studio character-reference portrait, not a phone snapshot and not a candid photo. 85 mm lens look, no wide-angle distortion. One large soft diffused light from the front right at about 40 degrees, slightly above eye level, with gentle fill from the left. Neutral-warm colour balance, soft natural shadows, matte skin without shine, fabric weave visible and matte, one soft window-shaped catchlight in each eye at the upper right. Muted, low-saturation colour grade. Plain dusty-blush seamless studio background (a muted pinkish-peach, not bright pink, not white, not cream, not grey), evenly lit, no gradient, no vignette. No filters, no film grain, no beauty retouching.

OUTPUT: 4:5 portrait; one image.

AVOID: hands or fingers anywhere in the picture; any resemblance to a real person; an idol, model or beauty-filter look; airbrushed, plastic, waxy or over-smooth skin; glowing, glossy, whitened or brightened skin; enlarged doll-like eyes; heavy eye makeup, eyeliner wings, blush, glossy lipstick; teeth showing; laughing or an open mouth; tears; a baby-faced or teenage look; a fringe over the forehead; hair tied back, a ponytail or pigtails; dyed or highlighted hair; hair clips or accessories; glasses; necklaces, rings, watches, bracelets or any jewellery other than the two colour-wheel earrings; text, letters, numerals, hex codes, logos, brand marks, watermarks, signage; a selfie, phone-camera, mirror or candid snapshot look; a fitting room, wardrobe, hanger or shopping bag; other people, children, pets; real places or landmarks; a colour swatch or fabric held near her face; revealing, tight, sheer, low-cut or sleeveless clothing; a sexualised or glamour pose; a uniform, an airline-crew or shop-staff look, a satin or shiny neckerchief; a school uniform; saturated red, blue, green or yellow clothing; an all-black or all-white outfit; rainbow stripes or flags; mismatched eyes or ears; extra or missing fingers.
```

If an app answers with text instead of a picture, reply "Please generate the image now." If it refuses, **do not reword the prompt to get around the refusal**: log it and tell Claude.

### 2.3 The avoid list on its own, and a short fallback

The chat apps may have no separate negative-prompt box (hypothesis; check the screen), so the avoid list is a sentence at the end (done above). If the long list seems to make an app draw the things it names (a flag, a rainbow, a logo, a hand), use the short fallback in 9.3.

### 2.4 What to generate

- **4 images in Gemini and 4 in ChatGPT**, each a separate waist-up portrait. The prompt says "one image" on purpose: do not change it. If the app has an images-per-request setting, use it; otherwise send the same prompt four times in a row (section 1).
- Save each at once as `assets/sehuan/photoreal/candidates/R01_cand_gemini_1.png` to `_4`, and `R01_cand_chatgpt_1.png` to `_4`. If the app gives another file type (`.jpg`, `.webp`), keep that type and use the real name in the log.
- Write down, for each: the tool, the model label **exactly as the app shows it today**, the time, the conversation link or ID, and a seed if one is shown.
- If nothing passes, change one thing (a fix phrase from 9.2), generate 4 more, and repeat. A planning figure is about 8 to 12 candidates per tool (*assumption*). If both tools fail the same way after two rounds, stop and tell Claude.

### 2.5 The inspection habit (do this on every image you keep)

Open it at **100%** and then at **200%**. Look in this order: hands (should be absent), eyes, **earrings (count the wedges on each one)**, ears, mouth and teeth, skin, hair edges and the tuck, neckerchief, blazer buttons, seams and collar, background. Hands, then earrings, fail most often, and a defect there is the one the public mocks fastest.

### 2.6 How to choose

1. **Thirty-second reject pass.** Throw out any image with a visible hand or finger, text or numerals, teeth, hair tied back, both ears covered or both tucked, no earring, a fringe, glasses or other jewellery, a plastic or airbrushed look, a teenage look, a glamour or sexualised feel, a non-blush background, or a selfie or snapshot look. Do not delete the files; mark them "rejected" in your notes.
2. **Checklist.** Run section 5 on each survivor.
3. **Shortlist at most three.**
4. **Wife looks** at the shortlist, without being told which tool made which (section 8). **You run the reverse-image search** on each shortlisted image (6.3).
5. **Choose one** and copy it to `assets/sehuan/photoreal/R01_master_v1.png` (keep the original in `candidates`). Log it as "provisional master", and **write down which side the hair is tucked on** (the addendum's side rule: the master fixes the tuck and the earring side for every later image; no image is ever flipped). It becomes the real master only after the tests in section 6 pass and it has had light hand-finishing in an image editor (crop, colour, stray marks; **no skin smoothing or brightening**).

### 2.7 The Character Lock (short paragraph)

Paste this at the start of every follow-up prompt in sections 3 and 4, after attaching R01 (it is "Image 1"). Do not use it for R01 itself or for the object stills R11 and R12.

```
Image 1 is the approved master image of one fictional person, an original character with no real-world counterpart. Keep exactly the same person: the oval face tapering to a narrow, softly rounded chin, the almond dark-brown eyes of modest size, the straight dark brown-black eyebrows, the small-to-medium nose with a soft tip, the natural closed lips in muted terracotta-brown, the medium warm golden-beige skin tone with natural skin texture and fine pores, the shoulder-length blunt-cut dark brown-black hair with a deep side parting, one side tucked behind the ear and the other side falling forward, no fringe, and the matching round twelve-segment colour-wheel drop earrings. The tucked side and the earring side are exactly as in Image 1. She looks about 30 to 35. No glasses, no other jewellery. Do not change the face, do not make her younger, do not smooth or brighten the skin, do not add makeup or glamour. Only the single change named below is allowed.

DEFAULTS unless the change below says otherwise: calm closed-mouth expression; outfit A (relaxed warm stone grey blazer worn open, cream fine-knit crew-neck top, small matte persimmon neckerchief at the collar, charcoal straight wide trousers, no logos or text); arms relaxed; both hands outside the picture; polished studio portrait, soft diffused light from the front right, neutral-warm muted colour, plain dusty-blush seamless background (a muted pinkish-peach, not bright pink, not white, not cream, not grey). No text, logos or watermarks. No other people.
```

---

## 3. STEP 2: lock it (the same person in more shots)

### 3.1 How R01 is used as the reference

- **New chat with R01 re-uploaded (recommended).** Open a fresh chat, attach your saved `R01_master_v1` file (**her own generated image**; uploading it is fine), then send the Character Lock (2.7), a blank line, and the prompt for that image. The advice to restart rather than correct in a long thread is an *assumption*; today confirms or refutes it. Use "same chat" only to retry the same image with a small fix.
- Attach R01 every time, plus at most two other golden images named on the "Attach" line. Never anchor to a freshly generated output alone.
- One change per picture. Make 4, choose the best, compare with R01 **at the same size** using section 5. Two failures in a row: new chat, R01 only.
- **If the tool changes its model label between two sittings**, treat the next images as a new design: log the label, and re-run the look-alike checks (addendum 11, item 8).
- **Never flip an image** and never use another character's image as a reference.

### 3.2 Per-image routine (about 10 to 15 minutes each; my estimate)

1. Open a new chat in the tool that made R01.
2. Attach the files on the "Attach" line. In ChatGPT use image edit mode with reference images if offered (hypothesis); otherwise attach to a normal message. In Gemini attach to the message.
3. Paste the Character Lock, a blank line, then the prompt for that image.
4. Get 4 images and save all 4 into `candidates` at once.
5. Inspect (2.5), run the checklist (section 5), choose one, copy it to its pack name.
6. Add the log rows (kept and discarded) before the next image.

### 3.3 Order of work, file names and what to attach

Save in `assets/sehuan/photoreal/`. A redo is `v2`. File types follow the app. Candidates go in `candidates/` as `<ID>_cand_<tool>_<n>`.

| Order | ID | Image | Attach | Save the chosen one as | When |
|---|---|---|---|---|---|
| 1 | R01 | Master: waist-up, front, outfit A, calm face | nothing | `R01_master_v1.png` | Sitting 1 |
| 2 | R02 | Three-quarter toward the viewer's left (shows the tucked ear and earring) | R01 | `R02_three-quarter-left_v1.png` | Sitting 2 |
| 3 | R03 | Three-quarter toward the viewer's right (hair side) | R01 | `R03_three-quarter-right_v1.png` | Sitting 2 |
| 4 | R04 | Side profile facing the viewer's left | R01 | `R04_side_v1.png` | Sitting 2 |
| 5 | R05 | Back view | R01 | `R05_back_v1.png` | Sitting 2 |
| 6 | R06 | Headshot, front, 1:1 (face lock) | R01 | `R06_headshot_v1.png` | Sitting 2 |
| 7 | R11 | Earring pair, object only | nothing (no Lock) | `R11_earrings_v1.png` | Sitting 3, first |
| 8 | R12 | Chip ring, object only | nothing (no Lock) | `R12_chip-ring_v1.png` | Sitting 3, first |
| 9 | R07 | Ten expressions, one image each | R01, R06 | `EXP_E01_neutral_v1.png` ... `EXP_E10_decline_v1.png` | Sitting 3 |
| 10 | R08a | Half-body framing | R01 | `R08a_half-body_v1.png` | Sitting 3 |
| 11 | R08b | Knees-up, hands in pockets, chip ring | R01, R12 | `R08b_knees-up_v1.png` | Sitting 3 |
| 12 | R08c | Full body, hands in pockets | R01, R12 | `R08c_full-body_v1.png` | Sitting 3 |
| 13 | R09 | Outfits B and C (A is R01) | R01 (B also R12) | `R09_B_v1.png`, `R09_C_v1.png` | Sitting 3 |
| 14 | R10 | Seasons V1, V2, V3 | R01 | `R10_V1_v1.png`, `R10_V2_v1.png`, `R10_V3_v1.png` | Sitting 3 |
| 15 | R13 | Glance toward the lesson | R01 | `R13_glance_v1.png` | Sitting 3 |
| 16 | R14 | Avatar 1:1 and 110 px test | R06 | `R14_avatar-1x1_v1.png` | After the master is final |
| 17 | R15 | Palette card (made by hand) | none | `R15_palette-card_v1.png` | See 3.5 |
| 18 | R16 | Badge and "AI" chip templates (made by hand) | none | later | See 3.5 |

The addendum (section 11) lists R01 to R16 as the golden set. Renaming into the frozen scheme happens when the set is frozen (Claude can do the rename and update the log paths).

### 3.4 The prompts for R02 to R06 (send after the Character Lock)

**R02: three-quarter toward the viewer's left.** Attach: R01.

```
CHANGE only: the angle. Show the same woman in a three-quarter view, her body and head turned about 40 degrees toward the viewer's left, eyes still looking at the camera. The tucked ear and its colour-wheel earring are clearly visible. Waist-up: the frame ends at the waist and both hands are outside the picture below the frame, arms relaxed. Same outfit (A), same hair, same calm closed-mouth expression.
OUTPUT: 4:5 portrait; plain dusty-blush seamless studio background; same soft studio light from the front right; one image.
```

**R03: three-quarter toward the viewer's right.** Attach: R01.

```
CHANGE only: the angle. Show the same woman in a three-quarter view, her body and head turned about 40 degrees toward the viewer's right, eyes still looking at the camera. The hair on this side falls forward and mostly covers the ear on this side; if the second earring shows below the hair it is identical to the first. Waist-up: the frame ends at the waist and both hands are outside the picture below the frame, arms relaxed. Same outfit (A), same hair, same calm closed-mouth expression.
OUTPUT: 4:5 portrait; plain dusty-blush seamless studio background; same soft studio light from the front right; one image.
```

**R04: side profile.** Attach: R01.

```
CHANGE only: the angle. Show the same woman in a side profile, seen exactly from the side, facing toward the viewer's left, eyes looking straight ahead. Show the profile of the oval face and narrow soft chin, the ear that is tucked behind the hair with the colour-wheel earring hanging from it, the blunt-cut hair falling forward on the far side, and the neckerchief knot from the side. Waist-up: the frame ends at the waist and both hands are outside the picture. Same outfit (A).
OUTPUT: 4:5 portrait; plain dusty-blush seamless studio background; same soft studio light; one image.
```

**R05: back view.** Attach: R01.

```
CHANGE only: the angle. Show the same woman from directly behind, head facing away from the camera: the shoulder-length blunt-cut hair with the parting visible at the crown, the side that is tucked behind the ear with its colour-wheel earring visible from behind, the back of the relaxed blazer and the back of the cream knit collar. Waist-up: the frame ends at the waist and both hands are outside the picture. Same outfit (A).
OUTPUT: 4:5 portrait; plain dusty-blush seamless studio background; same soft studio light; one image.
```

**R06: headshot (face lock).** Attach: R01.

```
CHANGE only: the framing. Headshot: head and shoulders, the frame ends at the upper chest below the collarbone, front view, calm closed-mouth expression, eye-level, 85 mm lens look. Centre the head with clear space around it so a circular crop will not cut the hair or the earring. The tucked-side earring, the neckerchief knot and the tuck remain visible as in Image 1; the other ear stays mostly covered by the hair, as in Image 1. No hands in the picture.
OUTPUT: 1:1 square; plain dusty-blush seamless studio background; same soft studio light; one image.
```

### 3.5 Images that are not generated

- **R15 palette card.** Made by hand in any slides or design app: one square swatch per colour with its hex under it (cream, warm stone, charcoal, persimmon, the backdrop; ranges in 5.3), plus the twelve wheel hues in order and the six chip tints. Log it with tool "human-made in <app name>" and prompt "none (made by hand)".
- **R16 badge and "AI" chip templates.** They carry text (「AI 生成｜虛擬角色」, 「AI 生成」 and the Latin chip "AI"). Do **not** ask Gemini or ChatGPT to draw them. They are built in a design tool with a Taiwan-form font (Noto Sans TC), and the wife reads every character. Not part of this session.
- **R14 avatar crops** are cut from the final master, so they wait until it is hand-finished (4.5).
- **The hand-built colour-wheel layer.** If you later need to repair an earring (addendum 11 item 6), the wheel is built by hand in an editor from the twelve hues in the Character Lock order. It is not asked of a generator.

---

## 4. Object stills, expressions, outfits, framings, poses, avatar

All person prompts below follow the Character Lock. Attach as stated.

### 4.1 R11 and R12: object stills (do these first in sitting 3)

These are references for the two details generators get wrong most. They show **no person**. Do not paste the Character Lock. Check them with rows 7 and 20 of the checklist before you use them as references.

**R11: earring pair.**

```
Generate a photorealistic reference image of a pair of round drop earrings laid flat on a plain dusty-blush seamless surface (a muted pinkish-peach, not bright pink), seen from directly above. Each earring is a flat, matte, enamel-look disc about 2.5 to 3 cm across hanging from a small plain hook, divided into twelve equal wedge segments like a colour wheel in dusty, muted colours, going round in this order: dusty red, red-orange, soft orange, golden yellow-orange, muted yellow, yellow-green, sage green, blue-green, dusty blue, blue-violet, soft violet, red-violet. Both earrings are identical. No gloss, no gems, no metal rim detail, no numbers, no letters, no text. Soft diffused light from the front right, soft shadow. Nothing else in the picture: no hands, no person, no logo, no brand mark.
OUTPUT: 3:2 landscape; one image.
```

**R12: chip ring.**

```
Generate a photorealistic reference image of a ring of exactly six blank rectangular colour-chip cards fanned on a thin charcoal binder ring, laid on a plain dusty-blush seamless surface (a muted pinkish-peach, not bright pink), seen from above at a slight angle. The six cards are matte card stock in muted tints: pale peach, light mist beige, warm stone grey, golden ochre, dusty rose, soft violet. The cards are completely blank: no text, no numbers, no codes, no labels, no logos. A small plain clip on the ring. Soft diffused light from the front right, soft shadow. Nothing else in the picture: no hands, no person.
OUTPUT: 3:2 landscape; one image.
```

### 4.2 R07: the ten expressions (one image each)

Attach: R01 and R06. Do **not** ask for several faces on one image; in photoreal they come out as different people. One image per expression, then check each is still her. Names and uses are the bible's (5.4); only brows, eyes and lips change; lips stay closed in every expression (no parted lips); no teeth, tears, wink, pout or laughing. Save as `EXP_E04_comparing_v1` and so on.

| ID | Name | Face |
|---|---|---|
| E01 | 平靜 neutral (default) | Calm, brows level, lips closed in a very slight smile |
| E02 | 說明 explaining | Head tilted about 5 degrees, lips closed and relaxed, as if about to speak; no parted lips, no teeth |
| E03 | 注意 pointing attention | Eyebrows slightly raised, eyes toward an empty space at the viewer's right |
| E04 | 比較 comparing | Eyes move to one side, brows very slightly asymmetric, lips flat |
| E05 | 微笑 mild smile | Soft closed-mouth smile, small smile lines at the eye corners |
| E06 | 不確定 uncertain | Small head tilt, lips pressed lightly together |
| E07 | 謹慎 careful | Brows drawn slightly inward, mouth level and closed |
| E08 | 更正 correcting | Small head bow, soft brows, lips closed |
| E09 | 輕鬆愉快 pleased, light | Small closed-mouth smile, eyes creasing slightly |
| E10 | 婉拒 polite decline | Slight tilt, lips pressed, soft brows; polite, not cold or angry |

E01:
```
Image 2 is the headshot; use it for the face only.
CHANGE only: the expression (E01, neutral): calm, brows level, lips closed in a very slight smile. Headshot, head and shoulders, front view, no hands in the picture. Nothing else changes.
OUTPUT: 1:1 square; plain dusty-blush seamless studio background; same soft studio light; one image.
```

E02:
```
Image 2 is the headshot; use it for the face only.
CHANGE only: the expression and head position (E02, explaining): head tilted about 5 degrees, the lips closed and relaxed with the faintest lift of the chin, as if about to speak, lips not parted, no teeth visible, brows level. Headshot, head and shoulders, no hands in the picture. Nothing else changes.
OUTPUT: 1:1 square; plain dusty-blush seamless studio background; same soft studio light; one image.
```

E03:
```
Image 2 is the headshot; use it for the face only.
CHANGE only: the expression (E03, pointing attention): the eyebrows slightly raised, the eyes directed to an empty space at the viewer's right, lips closed. Headshot, head and shoulders, no hands in the picture. Nothing else changes.
OUTPUT: 1:1 square; plain dusty-blush seamless studio background; same soft studio light; one image.
```

E04:
```
Image 2 is the headshot; use it for the face only.
CHANGE only: the expression (E04, comparing): the eyes move toward one side, the brows very slightly asymmetric, lips closed and flat. Headshot, head and shoulders, no hands in the picture. Nothing else changes.
OUTPUT: 1:1 square; plain dusty-blush seamless studio background; same soft studio light; one image.
```

E05:
```
Image 2 is the headshot; use it for the face only.
CHANGE only: the expression (E05, mild smile): a soft closed-mouth smile with small smile lines at the corners of the eyes. No teeth. Headshot, head and shoulders, front view, no hands in the picture. Nothing else changes.
OUTPUT: 1:1 square; plain dusty-blush seamless studio background; same soft studio light; one image.
```

E06:
```
Image 2 is the headshot; use it for the face only.
CHANGE only: the expression and head position (E06, uncertain): a small head tilt, the lips pressed lightly together, the eyebrows drawn slightly in. No teeth. Headshot, head and shoulders, no hands in the picture. Nothing else changes.
OUTPUT: 1:1 square; plain dusty-blush seamless studio background; same soft studio light; one image.
```

E07:
```
Image 2 is the headshot; use it for the face only.
CHANGE only: the expression (E07, careful): the eyebrows drawn slightly inward, the mouth level and closed. Headshot, head and shoulders, front view, no hands in the picture. Nothing else changes.
OUTPUT: 1:1 square; plain dusty-blush seamless studio background; same soft studio light; one image.
```

E08:
```
Image 2 is the headshot; use it for the face only.
CHANGE only: the expression and head position (E08, correcting): a small head bow of about 5 degrees, soft eyebrows, lips closed. Headshot, head and shoulders, no hands in the picture. Nothing else changes.
OUTPUT: 1:1 square; plain dusty-blush seamless studio background; same soft studio light; one image.
```

E09:
```
Image 2 is the headshot; use it for the face only.
CHANGE only: the expression (E09, pleased, light): a small closed-mouth smile with the eyes creasing slightly. No teeth. Headshot, head and shoulders, front view, no hands in the picture. Nothing else changes.
OUTPUT: 1:1 square; plain dusty-blush seamless studio background; same soft studio light; one image.
```

E10:
```
Image 2 is the headshot; use it for the face only.
CHANGE only: the expression and head position (E10, polite decline): a slight head tilt, the lips pressed together, soft eyebrows; polite, not cold and not angry. Headshot, head and shoulders, no hands in the picture. Nothing else changes.
OUTPUT: 1:1 square; plain dusty-blush seamless studio background; same soft studio light; one image.
```

### 4.3 R08: framings (half-body, knees-up, full body)

Headshot is R06 and waist-up is R01. 

**R08a: half-body** (top of head to the lower chest; the waist is not in this frame). Attach: R01.

```
CHANGE only: the framing. Half-body: from the top of the head to the lower chest, front view, calm closed-mouth expression, arms relaxed and outside the picture. Outfit A.
OUTPUT: 4:5 portrait; plain dusty-blush seamless studio background; same soft studio light; one image.
```

**R08b: knees-up, hands in pockets, chip ring.** Attach: R01 and R12. 

```
Image 2 is a reference for one object only: the ring of six blank colour-chip cards. Copy that object; do not copy anything else from Image 2.
CHANGE only: the framing and pose. Three-quarter length: from the top of the head to mid-thigh, front view, standing relaxed and upright, both hands fully inside her trouser pockets under the open blazer, so that only the blazer sleeves show and no fingers or thumbs are visible. At her left hip, the ring of exactly six blank colour-chip cards is clipped to the belt loop of the trousers, hanging against the trouser leg; the cards carry no text, numbers or codes. Outfit A, calm closed-mouth expression, direct gaze at the camera.
OUTPUT: 4:5 portrait; plain dusty-blush seamless studio background; soft contact shadow; same soft studio light; one image.
```

**R08c: full body, hands in pockets.** Attach: R01 and R12.

```
Image 2 is a reference for one object only: the ring of six blank colour-chip cards. Copy that object; do not copy anything else from Image 2.
CHANGE only: the framing and pose. Full body from the top of the head to the shoes, front view, standing relaxed and upright on the seamless studio floor, 50 mm lens look, eye-level camera, both hands fully inside her trouser pockets so that no fingers or thumbs are visible. The ring of exactly six blank colour-chip cards is clipped to the belt loop at her left hip. Plain flat charcoal leather loafers with no logo, both shoes fully in the frame with correct feet. Outfit A, calm closed-mouth expression, direct gaze at the camera. Natural proportions: the head is about one seventh of her standing height.
OUTPUT: 4:5 portrait; plain dusty-blush seamless studio background; soft contact shadow on the floor; same soft studio light; one image.
```

### 4.4 R09 and R10: outfits and seasons; R13: glance

Colours are words; check them with 5.3. Attach: R01 (and R12 for outfit B).

**R09: outfit B (背心裙裝組).** Attach: R01 and R12.

```
Image 2 is a reference for one object only: the ring of six blank colour-chip cards. Copy that object; do not copy anything else from Image 2.
CHANGE only: the outfit. She wears outfit B: a cream long-sleeve collared shirt with the collar open at the top button only, no tie, no bow, sleeves rolled to the elbow, under a charcoal sleeveless knit vest; a plain canvas tote bag in persimmon (a soft, muted terracotta-orange, not bright orange, not red) on her right shoulder (the viewer's left), its wide flat strap crossing the shoulder, with the ring of exactly six blank colour-chip cards clipped to the strap at chest height. Her arm hangs relaxed; no hand touches the strap or the bag. No neckerchief. Relaxed adult workwear cut, neckline covers the collarbone, not a school uniform. No logos, text or patterns. Waist-up: the frame ends at the waist and both hands are outside the picture. Same face, hair and earrings.
OUTPUT: 4:5 portrait; plain dusty-blush seamless studio background; same soft studio light; one image.
```

**R09: outfit C (長版針織組).** Attach: R01.

```
CHANGE only: the outfit. She wears outfit C: a plain long open knit coat in charcoal, hip-to-thigh length, worn open over a cream crew-neck tee whose neckline covers the collarbone; at the neck the small persimmon (a soft, muted terracotta-orange, not bright orange, not red) matte cotton-linen neckerchief, folded into a narrow band and loosely knotted, not shiny. Relaxed modest fit. No logos, text or patterns. Waist-up: the frame ends at the waist and both hands are outside the picture. Same face, hair and earrings.
OUTPUT: 4:5 portrait; plain dusty-blush seamless studio background; same soft studio light; one image.
```

**R10: V1 hot and humid.** Attach: R01.

```
CHANGE only: the outfit. Hot-humid version: a short-sleeve cream shirt worn untucked, sleeves ending above the elbow, neckline covers the collarbone, no blazer; the small persimmon matte neckerchief at the collar. Modest relaxed fit, nothing sleeveless, nothing tight. No logos, text or patterns. Waist-up: the frame ends at the waist and both hands are outside the picture. Same face, hair and earrings.
OUTPUT: 4:5 portrait; plain dusty-blush seamless studio background; same soft studio light; one image.
```

**R10: V2 rain (jacket only; no umbrella, no rain).** Attach: R01.

```
CHANGE only: the outfit. Rain version: a short stone-grey rain jacket in a plain matte fabric, zipped about halfway, with the hood down and resting at the back of the neck; the small persimmon matte neckerchief at the collar. No reflective strips, no logos, no visible brand tags, no drawcord ends near the face. No rain, no umbrella. Waist-up: the frame ends at the waist and both hands are outside the picture. Same face, hair and earrings.
OUTPUT: 4:5 portrait; plain dusty-blush seamless studio background; same soft studio light; one image.
```

**R10: V3 damp cold.** Attach: R01.

```
CHANGE only: the outfit. Damp-cold version: a long charcoal coat worn open over a cream knit; a cream scarf with one persimmon (a soft, muted terracotta-orange) stripe at each end, draped round the neck with both ends hanging down the front. No snow, no maple leaves, no puffer coat, no gloves. Modest relaxed fit. No logos, text or patterns. Waist-up: the frame ends at the waist and both hands are outside the picture. Same face, hair and earrings.
OUTPUT: 4:5 portrait; plain dusty-blush seamless studio background; same soft studio light; one image.
```

**R13: glance toward the lesson.** Attach: R01. The "pointing" pose: arrows are added later in post.

```
CHANGE only: the head position and gaze. Waist-up, the head turned no more than about 15 degrees toward the viewer's right and the eyes directed to an empty space at the viewer's right, as if looking at something just outside the picture; calm closed-mouth expression. The tucked ear and its earring remain visible. The frame ends at the waist and both hands are outside the picture. Outfit A, same face, hair and earrings.
OUTPUT: 4:5 portrait; plain dusty-blush seamless studio background; same soft studio light; one image.
```

### 4.5 R14: profile avatar

Easiest route: crop the headshot (R06) or the best of E01 and E05 in any image editor, square, with the head about 60 to 70% of the height, the face inside the central 70%, and a little space around it so a circular crop will not cut the hair or the earring. Log it as a human edit of its parent. Then: (a) shrink it to about 110 px tall (about 3 cm on a laptop screen, or zoom the browser out) and check the thumbnail tell: shoulder-length hair with one side tucked, a coloured dot at the left ear, and a persimmon patch at the collar, if the crop includes it; (b) add the small **"AI" chip** in a design tool later (R16); do not generate it.

Optional AI route (attach R01 and R06):

```
CHANGE only: the framing. Head and shoulders only, front view, calm closed-mouth expression, centred, with a little space around the head so a circular crop will not cut the hair or the earring. The tucked-side earring and the neckerchief knot stay visible as in Image 1; the other ear stays mostly covered by the hair. No hands in the picture.
OUTPUT: 1:1 square; plain dusty-blush seamless studio background; same soft studio light; one image.
```

---

## 5. Pass/fail checklist

Run this on **every** image you keep, at 100% and 200%, side by side with R01 at the same size. Any single failure in rows 1 to 34 rejects the image (rows 35 and 36 are housekeeping: fix them, do not reject). Copy the table into your notes once per image you take seriously and tick the boxes.

**Fail codes:** **R** = regenerate (press again, change nothing). **P** = edit the prompt (add the matching fix phrase from 9.2, then make 4 more). **E** = fix in an image editor (small and local; log it as a human edit, keep the untouched original; **never for hands, face, skin, proportions or age**). **X** = stop and tell Claude (a design problem or a test failed; never "fix" it by editing).

### 5.1 The checklist

| # | Check | How to check | Pass | If it fails |
|---|---|---|---|---|
| 1 | **Adult and visible age** | Looks about 30 to 35 at full size and still adult at 64 px tall. Defined cheeks, faint age lines, natural brows. Not a teenager, not in her early twenties. The age-guess test in 6.1 settles it | [ ] | P (age fix); X if it persists |
| 2 | **Same face as R01** | Beside R01 at the same size: face shape (oval tapering to a narrow soft chin), eye size and spacing, brows, nose, lips, jaw all match. If you hesitate, it fails | [ ] | R; re-anchor if twice |
| 3 | **Skin tone matches R01 and is not brightened** | Same medium warm golden-beige. Sample a flat cheek patch in R01 and write down the red, green and blue numbers; a later image should be within 12 on each channel in similar light. Not whitened, not tanned, no pink cast | [ ] | P |
| 4 | **Hair** | Dark brown-black, shoulder-length, blunt-cut, deep side parting, one side tucked behind the ear and the other falling forward, no fringe, not tied back, not dyed, no clips, a few flyaways | [ ] | R / P |
| 5 | **Tuck and earring side match R01** | Same side as the master (the side rule, addendum 11 item 5). Not flipped | [ ] | R; P if 2 of 4 |
| 6 | **Ears** | Tucked-side ear fully visible, natural shape, pierced lobe, same as R01. The other ear mostly covered. No extra piercings or studs | [ ] | R / P |
| 7 | **Earrings** | Matching pair of flat round matte discs hanging from small hooks. **Count the wedges at 200%: twelve.** Muted colours in the Lock order, not a saturated rainbow, no letters or numbers. Same as R11 | [ ] | R; E for a wrong count if all else is perfect (object-only) |
| 8 | **Eyes (uncanny check)** | Same size, round natural pupils, both looking the same way, one soft catchlight in each eye in the same place, no glassy or dead stare, no mismatched lids | [ ] | R; P if 2 of 4 |
| 9 | **Mouth and teeth** | Lips closed in every expression (no parted lips, a banned sexualised cue). **No teeth in any image of this pack**; if any show, the image fails (and a defect like one white block is the worst case) | [ ] | R / P |
| 10 | **Expression matches the request and she is still the same person** | Compare with the E-ID in 4.2; the face has not drifted | [ ] | R |
| 11 | **Hands (the top failure)** | Prefer none visible. If any hand, wrist or thumb shows, zoom to 200%: count fingers, check joints, nails, thumb side, wrist continuity, no merged or extra digits. A pocket pose must show no fingers or thumbs. Anything odd: fail | [ ] | Follow 9.1; never E |
| 12 | **Arms, shoulders, neck** | Natural anatomy, level shoulders, equal arm lengths, neck not stretched, sleeves end at the wrist (B: rolled to the elbow; V1: short sleeves ending above the elbow, with no hand in frame) | [ ] | R / P |
| 13 | **Build and proportions** | Average-to-slim, no waist, bust or hip shaping or emphasis. Head about one seventh of height in full body (**fail above one sixth**) | [ ] | P |
| 14 | **Feet and shoes** (full body only) | Two plain flat shoes, correct orientation, no logo, no extra toes | [ ] | R / P |
| 15 | **Outfit** | Exactly one of A, B, C, V1, V2, V3 (addendum 4). Pieces are right for that outfit | [ ] | P |
| 16 | **Garment realism** | Collar symmetrical, buttons round and aligned, seams straight, pocket and cuff edges clean, nothing melted, doubled or merged, no invented tag, label, trim or pattern (a standing tripwire) | [ ] | R / P |
| 17 | **Clothing consistency and colour** | Same garments and colours as R01. Sample a flat, evenly lit patch (5.3): inside range and the same colour by eye. No head-to-toe white or black | [ ] | P; E if only a colour cast |
| 18 | **Persimmon accent** | Exactly one persimmon item (neckerchief in A, C, V1, V2; tote in B; scarf stripes in V3), a soft muted terracotta-orange, never bright orange or red, at most about a tenth of the figure, readable against cream or charcoal and not lost in the skin | [ ] | P |
| 19 | **Neckerchief** (A, C, V1, V2) | Matte, folded narrow, loosely knotted, ends tucked, not tight, not satin. Does not read as an airline-crew or shop-staff scarf or a tie | [ ] | P; wife decides |
| 20 | **Chip ring** (when the hip or strap is in frame) | **Exactly six** blank cards on a thin charcoal ring, clipped (not held), no text, numbers or codes; same as R12 | [ ] | R; E if only stray marks on a card (object-only) |
| 21 | **Other jewellery and accessories** | None: no glasses, necklace, ring, watch, bracelet, hair accessory, phone. Outfit B's tote is the only bag | [ ] | R / P |
| 22 | **Modesty and no sexualised cue** | Collarbone covered, relaxed fit, no tight or sheer clothing, no glamour light, no parted-lip pose, no over-shoulder glance, no low camera angle, no body emphasis | [ ] | P; X if it persists |
| 23 | **No wearing, testing or "life" cue** | No mirror, fitting room, hanger, wardrobe, shopping bag, product, swatch or fabric near the face, phone, food or drink | [ ] | P |
| 24 | **No logos, brands or plates** | None on clothes, shoes, tote, buttons, zips or background; no garment that resembles a recognisable branded piece | [ ] | R / P |
| 25 | **Text, hex codes, numerals (garbled or Simplified Chinese included)** | **No text at all**, in any script, even if it looks correct. If Chinese characters do appear, ask the wife whether they are garbled or Simplified and note it in the log (it tells us how the tool behaves) | [ ] | R; E if one small mark |
| 26 | **Background** | Plain dusty-blush seamless (a muted pinkish-peach), even, no gradient, no objects, nothing readable. Not white, cream, grey or bright pink | [ ] | P; E for the shade if near |
| 27 | **Framing and pose as asked** | Matches the prompt (F1 to F6); crop line where asked; arms relaxed | [ ] | R / P |
| 28 | **Studio Look consistent** | Light from the front right, neutral-warm muted colour, matte skin, same backdrop and catchlight position as R01 | [ ] | P |
| 29 | **No candid, selfie or "my life" look** | No phone, mirror, arm-length view, motion blur, snapshot crop, room, street, food or product | [ ] | P |
| 30 | **Skin too smooth or plastic** | At 100%, pores and fine texture visible; no waxy sheen, airbrushing or uniform blur. A face that is too perfect also fails | [ ] | P |
| 31 | **Edge artefacts** | Hair strands, ear edges, earring hooks, collar and neckerchief edges are clean; nothing melted or merged | [ ] | R / P |
| 32 | **Overall 100% look** | Does anything look wrong without your being able to say what? Ask the wife. If yes, it fails | [ ] | R; X if it persists |
| 33 | **Resemblance to a real person, or to 方寸 or 步驟** | Do you or the wife instantly think of a real person, public or private, or an existing character, or of the other two pilots? A quick look now; the real tests are in section 6 | [ ] | X |
| 34 | **Colour with a political or taboo reading** | At thumbnail size nothing reads as a party-colour camp; no flags, rainbow flag read, charts, money, religious or mourning objects | [ ] | P; wife decides |
| 35 | **File untouched and markers intact** | The file is the original download, not a screenshot, not re-saved; any visible mark left alone and noted (7.5) | [ ] | Re-download |
| 36 | **Saved, named and logged** | In the right folder with the pack name; a row in the log with tool, model label, prompt, time and licence notes | [ ] | Do it now |

### 5.2 Regenerate, edit the prompt, edit the picture, or stop?

| Situation | Do this |
|---|---|
| One of the four has the defect and the others do not | **R**: it is random. Choose another |
| The same defect appears in 2 or more of 4 | **P**: add the matching fix phrase from 9.2 at the end and generate 4 more |
| Otherwise perfect image, one tiny local flaw (a stray mark, a wrong wedge count on an earring, a mark on a chip card, a slight colour cast) | **E**: fix in an image editor. Allowed: crop, colour correction, stray-mark removal, and an **object-only** repair of the earring disc or a chip card. Never for hands, face, skin, proportions or age. A "stray mark" is never the tool's own visible mark or watermark, and a crop is never used to cut one out. Log it as a human edit and keep the untouched file as its parent |
| A visible hand with any defect | Follow 9.1 |
| The same defect after two rounds (8 images) in one tool | Try the other tool with the same prompt. If both fail, **X** |
| Age guess fails, a look-alike is named, or a search shows a close match | **X**: stop and tell Claude; do not repair it by editing |

### 5.3 Colour check: hex, RGB and an allowed range

Hex values are hints for you; they are not in the prompts. Image models follow named colours loosely and lighting shifts them. Sample a **flat, evenly lit patch** that faces the light (not a fold, a shadow or an edge) with any eyedropper tool and read the red, green and blue numbers. The "OK range" is **my suggestion, not a bible rule** (*assumption*, to calibrate): within 16 on each channel, wider than the illustration pack because fabric weave and light fall-off vary photographic colour. Inside range **and** the same colour by eye as a swatch of the hex: pass. Off by a little more: fix the colour in post and note it in the log. Visibly a different colour (a yellow cream, a bright orange or red persimmon, a hot-pink or white backdrop): regenerate or edit the prompt.

| Used for | Colour | Hex | R, G, B | OK red | OK green | OK blue |
|---|---|---|---|---|---|---|
| Backdrop | Dusty blush 淡蜜桃色 (photo backdrop) | `#EBCFC6` | 235, 207, 198 | 219 to 251 | 191 to 223 | 182 to 214 |
| Knit top, shirt, tee, scarf | Cream 奶油白 | `#F4E8DF` | 244, 232, 223 | 228 to 255 | 216 to 248 | 207 to 239 |
| Blazer, skirt, trousers, rain jacket | Warm stone 暖灰 | `#B8AEA2` | 184, 174, 162 | 168 to 200 | 158 to 190 | 146 to 178 |
| Trousers, vest, coat, shoes | Charcoal 炭灰 | `#3A3735` | 58, 55, 53 | 42 to 74 | 39 to 71 | 37 to 69 |
| The one accent | Persimmon 柿子橘 | `#CD8B6A` | 205, 139, 106 | 189 to 221 | 123 to 155 | 90 to 122 |

- The bible's card ground `#F2DAD2` is for cards and lesson graphics, not for these photos. A photo backdrop whose red, green and blue are all above about 238, 213 and 205 is closer to the card ground and washes out the cream top: edit the prompt or fix it in post.
- The twelve wheel colours and the six chip tints are too small to sample. Check the earring and the ring by eye against the Lock order: all dusty and muted, none a saturated spectrum.
- Hair, eyes, lips and skin: check by eye against R01 (hair a dark brown-black, not pure black; skin by the cheek-patch rule in checklist row 3).
- When the palette card (R15) exists, hold the picture beside it as well.

---

## 6. The human tests, and the reverse-image search

The addendum (section 9) sets the rules and they are **stricter than the illustration pack's**. They need other people, so they usually happen on a different day from the generating. The people are helping you test a design; they do not follow, like or comment on any account, and they should not share the pictures. These tests are the only place an unlabelled working image is shown to anyone: never post, send or leave one with a tester, and do not use test results to make a picture look more real. Tell them afterwards what the pictures were for. **Never place a photograph of any real person beside the character to compare.**

### 6.1 Age-guess test (adult-reading check)

1. For each shortlisted image (up to three), make a clean copy with no file name visible, a copy at about 110 pixels tall, and a headshot at 64 pixels. Crops are human edits; log them if you keep them.
2. Find the wife plus **at least five others (six or more in all)**, a mix of ages including at least two over 40 and at least three living in Taiwan, none of whom has seen the pictures. Show each person the pictures **one at a time, in a different random order, with no context**: do not say AI, character, mascot or account.
3. Ask only: **"How old is this person, and what might she do for a living?"** Write the number and the job word exactly. If they refuse to guess, ask for a range.
4. Do the same with the 110 px copy and, later, the avatar crop. Repeat once for outfits B and C.
5. **Hard fail:** any single guess **under 25**, a median guess **under 28**, or the word student (學生) or teenager.
6. **Warn (use the age fix in 9.2 and retest):** a median of 28 or 29, or any single guess of 25 to 27. **Target:** median 30 to 35.
7. Record the answers in the language given; the wife adds an English gloss.

### 6.2 Blind look-alike test

1. Same people and set-up as 6.1, shown the picture the same way.
2. Ask only: **"Who does this remind you of?"** Write the answer word for word. Do not offer names.
3. **Fail** if *any one* person names a real person (public or private) or a specific existing virtual character or influencer. "Someone, I can't say who" is recorded, not failed; two such answers mean you ask the wife a follow-up and run an extra search round.
4. A fail goes in the log. The image is not used. Do not try to "fix" a look-alike by editing; regenerate with a changed attribute (face shape, hair length, parting side) or tell Claude.

### 6.3 Reverse-image search (manual, public tools only)

Do this for each shortlisted image, on your own computer, by hand, logged out of personal accounts, in a private window.

1. Make working crops (temporary files, no log row needed): **(a) head and shoulders; (b) tight face, forehead to chin; (c) eyes to mouth; (d) a three-quarter face from R02 if it exists.** For the chosen final master add **(e) the tight face mirrored left to right** (search engines can miss flipped matches) and **(f) the tucked ear with the earring**.
2. Use **Google Lens, Bing Visual Search and TinEye** (the current "search by image" pages), uploading the crops yourself. Do not use scripts, bots or scraping; do not log in anywhere you would not normally; **do not use face-recognition people-search services**. Uploading sends the picture to that service, acceptable for a pre-launch design but worth noting in the log.
3. Look at the first two pages of visual matches in each tool, for each crop. Write down any result where **you or the wife think the character looks like a real person**, public or private, and any close match to an existing character or virtual influencer. Record tool, crop and date. **These tools may return photos of real people: do not try to find out who anyone is, do not contact anyone, do not save or repost their photos.** A close match to a person means stop and tell Claude.
4. Screenshot the result pages into `assets/sehuan/photoreal/lookalike/` with names like `R01_cand_gemini_2_googlelens_crop-b_2026-10-11.png`. Screenshots are evidence, not generated assets: list their names in the log below; no provenance row.
5. Also run text searches on generic terms in the same tools' image results and compare by eye: for example "woman shoulder-length black hair blazer studio portrait pink backdrop", "colour wheel earrings woman portrait", "segmented disc earrings", "persimmon neckerchief blazer". The wife runs Chinese equivalents (an AI draft, she adjusts): 「色環 耳環 人物」, 「虛擬角色 色環耳環」, 「柿子橘 領巾 外套 人物」. The signature combination (a wheel earring plus a persimmon neckerchief) may already belong to another character or brand.
6. **Fashion-niche check.** Compare by eye with the AI-generated "model" images that apparel sellers use, in the first page of image results for generic descriptions of her. A look-alike dispute over an apparel brand's AI model image has already forced an apology in Taiwan (addendum 8.1 row C).
7. **The wife's local-public-figure check.** She looks at each shortlisted image and says whether the face resembles any local public figure (news presenter, actress, singer, model, influencer, politician, athlete, TV host) or anyone she knows personally; she writes the name or "the type". Names stay in this internal log only and never go into a prompt. A resemblance to a politician is also a Ground rule 6 problem.
8. **Existing virtual humans.** Compare by eye with the photoreal virtual influencers and the Taiwan characters listed in `research/competitors.md` sections 3 and 4. Read the names from that file; they never go into a prompt and nothing of theirs is ever uploaded.
9. If a very close match turns up: do not use the image; tell Claude.
10. Repeat on the final master, on any new outfit family or hair or earring change, on any model or tool change, on a monthly sample of finals, annually, and on any complaint (take down within 24 hours; pause until a documented check is done).

### 6.4 Near-pair test against the other two pilots

When R01 exists for 方寸 and 步驟 as well: put the three front waist-up images in one row at about 110 px tall, on a laptop and on a phone, unlabelled. Ask the wife and at least four others (five viewers or more; the age-guess panel can be reused), two seconds each: "Same person, sisters, or different people?" **Pass:** all say different people. **Fail:** two or more say same person or sisters for any pair. Fix by changing a design attribute of the character that fails (face shape, hair length, parting side), not by editing. Detail: addendum 10 and `README-photoreal.md` section 3.

### 6.5 Uncanny read, disclosure legibility and mistaken-for-real check

Show five viewers the master at full size and at phone size, plus two closed-mouth smiling expressions (E05 and E09; no open-mouth or teeth-showing image is made). (a) **Uncanny:** "Does anything look off, fake or creepy? Where?", then "How natural, 1 to 5?" Pass: median 4 or more and no more than one person flags the eyes or the mouth. (b) **Mistaken for real (information, not pass or fail):** without any badge, "Is this a real photo or AI?" It calibrates how much the label must do: if most say "real photo", the badge, the first caption line and the avatar chip matter even more (they are already mandatory). Never use the result to make the picture look *more* real. (c) **Disclosure legibility (strict):** show the image **with** a mock badge and first caption line (addendum 8.2) and ask "Is it clear whether this is a real person?" Pass: everyone says it is an AI character. Any "not sure": enlarge or move the badge and retest.

### 6.6 The log to keep

| Check ID | Date | Candidate or asset | Tools, crops and searches | Search result | Wife's check | Blind-test answers | Age guesses | Verdict | Checked by |
|---|---|---|---|---|---|---|---|---|---|
| LA-PR-001 | | | | | | | | | |

Age-guess tally (one row per person; "Under 25 or student?" is yes if the guess is below 25 or the word student or teenager was used):

| Person (initials) | Full-size guess | Thumbnail guess | Job guess | Under 25 or student? | "Reminds me of" (verbatim) |
|---|---|---|---|---|---|
| Wife | | | | | |
| | | | | | |

---

## 7. Provenance, licence and labelling

### 7.1 Columns and a ready-to-fill example

The rule (Ground rule 2): **every kept file and every discarded-but-considered file gets one row in `assets/provenance.csv`, the same day.** "Considered" means you saved it, compared it, shortlisted it or used it as a reference. Edited versions and hand-made files are separate files with their own rows that name the parent.

Columns, in order: `timestamp,asset_path,persona,tool,model,prompt,licence_notes`.

- `timestamp`: Taiwan time with offset `+08:00` when you generated it.
- `asset_path`: from the project folder, for example `assets/sehuan/photoreal/candidates/R01_cand_gemini_1.png`.
- `persona`: `sehuan` until the real handle is chosen.
- `tool`: what you actually used, for example "Gemini (app)" or "ChatGPT (app)". For an edit, the editor's name; for a hand-made file, "human-made in <app>".
- `model`: the label **exactly as the app shows it that day**. If none is shown: "not shown in app, YYYY-MM-DD". Never guess. For an edit: n/a.
- `prompt`: the **full text you sent**, including the Character Lock, and a note of which files were attached (only R01 and other golden images; never any other picture). If you changed even one word (for example the wording option in section 2), log the changed text.
- `licence_notes`: the template in 7.3.

This is an **example only**. Do not paste it as it is. Replace every `<...>` with the real value, and add only the second line to the real file.

```
timestamp,asset_path,persona,tool,model,prompt,licence_notes
<YYYY-MM-DDTHH:MM:SS+08:00>,<assets/sehuan/photoreal/candidates/R01_cand_gemini_1.png>,sehuan,"Gemini (app)","<model label exactly as shown in the app today>","<PASTE THE FULL PROMPT EXACTLY AS SENT. Attached files: none.>","Status: <KEPT | KEPT (provisional master) | DISCARDED-CONSIDERED>; reason: <one word>; parent file: none (raw download); reference images attached: none; human edits: none (raw); prompt ID: R01-Gemini; tool plan: <plan name shown in my account>; terms read on <YYYY-MM-DD, or: not yet read> at <page name or link, or: none>; commercial use per those terms: NOT CONFIRMED; visible mark or label on file or in the app: <none seen | describe>; conversation link or ID: <link>; seed: <none shown | number>; hand check at 200%: no hand visible; tucked side: <viewer's left | viewer's right>; look-alike check: LA-PR-001 pending"
```

A human edit (an avatar crop, a colour fix, an earring repair) looks like this; the same rule applies (replace every `<...>`):

```
<YYYY-MM-DDTHH:MM:SS+08:00>,<assets/sehuan/photoreal/R14_avatar-1x1_v1.png>,sehuan,"<editor name as shown>","n/a","Square crop of R06_headshot_v1, head about 65% of the height, face inside the central 70%; no other change","Status: KEPT; parent file: assets/sehuan/photoreal/R06_headshot_v1.png; human edits: crop; no skin smoothing or brightening; untouched parent kept; look-alike check: <LA-PR-00x status>"
```

### 7.2 Rules that keep the file valid

- One row per file. Four images from one prompt are four rows with the prompt cell copied down. Rejected-on-sight images that you saved get a row with one word of reason.
- Edit the CSV in a spreadsheet app and paste each field into its own cell; the app adds the quotes and handles commas, line breaks and double quotes. If you edit it as plain text, put every field that contains a comma, a line break or a quote in double quotes, and double every quote mark inside it. Save as CSV (UTF-8 if offered).
- Do not edit or delete old rows. Corrections go in a new row. Add yours at the bottom (other characters' rows share the file).
- You can paste your notes (file names, tool, model label, time, which prompt, any wording you changed) to Claude Code and ask it to write the rows. Claude cannot see your screen, so it needs the model label and the time from you.
- Search crops used only for the reverse-image search are temporary and need no row (6.3).

### 7.3 `licence_notes` template (fill the blanks)

```
Status: ___ (KEPT | KEPT (provisional master) | DISCARDED-CONSIDERED); reason: ___; parent file: ___ (none (raw download) | file name); reference images attached: ___ (none | R01_master_v1.png ...); human edits: ___ (none (raw) | crop | colour fix | stray mark | earring repair | chip-card repair | badge added | other); prompt ID: ___ (for example R02); tool plan: ___ (the plan name shown in my account); terms read on ___ (date) at ___ (page name or link); commercial use per those terms: ___ (CONFIRMED | NOT CONFIRMED | RESTRICTED: what); visible mark or label on file or in the app: ___ (none seen | describe); conversation link or ID: ___; seed: ___ (none shown | number); hand check at 200%: ___ (no hand visible | pocket pose, no digits visible | other); tucked side: ___; look-alike check: ___ (LA-PR-00x pending | passed on date | failed)
```

### 7.4 Licence reminder

**The commercial-use terms of your Gemini and ChatGPT subscriptions have not been checked.** Before any commercial use (a public account, a sponsored post, a client sample), read the **current** terms for the exact tool and plan, and fill in "terms read" and "commercial use" from what they actually say. Questions to answer from the text, not from memory: who owns the images or what rights you get; whether commercial use is allowed **on your plan**; limits on using outputs as a recurring character or brand asset; **what the terms say about realistic images of people and any duty to disclose AI generation**; what they say about visible marks, invisible watermarks and removing them; rules about uploaded reference images (you upload only the character's own images); when the terms last changed. Terms can differ between tools, plans, and the app and a developer interface, and they change. Save a dated screenshot or PDF of the page. If anything is unclear, write NOT CONFIRMED. Until it is recorded, every image is **internal design material only**. Whether purely AI-generated images can be protected by copyright in Taiwan is an open question for the lawyer (`research/legal.md` 8.2); light human edits with the layered file kept are how the studio documents its own contribution (and **no skin smoothing or brightening**).

### 7.5 Labelling reminder (read before you export anything)

- **Save the file with the platform's AI marker intact. Do not strip metadata.** Use the download button, not a screenshot, not "save for web", not a converter. Some tools put an AI marker in the file or add an invisible or visible mark (*hypothesis, unverified*: for example Meta reads industry markers such as C2PA or IPTC to apply "AI info", and YouTube locks its label on content with generative markers; `research/platforms.md` 4.1). Whether Gemini or ChatGPT add such markers is checked in the app and the file properties and **noted in the log**. If you see a mark, leave it and note it. Do not remove, crop out, paint over or cover any mark, and do not re-save or convert a file in order to lose its markers; the terms of use may also restrict removing them. Crops for the avatar and reframing follow the same rule: keep the mark in frame or re-roll.
- **An editor may drop the markers on export.** When you add the badge, the chip or text in a design tool, check whether the exported file keeps its metadata (the editor's export or file-properties screen) and write the result in the log. Because auto-detection cannot be relied on, **always switch on the platform's AI label by hand**.
- **The on-screen badge is added in editing, never generated.** Add the 「AI 生成」 badge to every published image: `AI 生成｜虛擬角色` on any image that shows her, `AI 生成` on lesson slides without her (the wife rules on the wording, addendum 12.1 item 8). Solid charcoal pill, cream text, text height at least about 3.5% of the image height, inset at least 11% of the height from the top and bottom edges and at least 8% of the width from the sides (so a centred square crop of a 4:5 picture cannot remove it; see pipeline/qa-checklist.md D3), in the same corner every time, on **every** image and every video frame. The wife reads every character. The avatar gets a small corner chip reading `AI`.
- **Platform labels at posting time:** Instagram, the AI-generated profile label on the account (checked on a Taiwan test account first) and the content-level AI disclosure on every post; Threads, the same disclosure; the AI-disclosure control on any boosted or partnership post. Bio and first caption line follow bible section 8 and addendum 8.2.
- **Alt text** on every image (AI draft, the wife corrects): 「AI 生成的虛擬角色色環，非真人。」
- **No location tag, no map pin, ever.**
- Nothing made with this pack goes on any account yet: the reading test, lawyer answers, the Instagram label check, licence terms and STOP 3 come first.

---

## 8. A note for the wife

Thank you for looking at these. You are judging **language, culture and how it feels**, not the technology. The operator checks hands, anatomy and numbers. Please look at each picture the way a Taiwanese viewer scrolling Instagram would, and say **APPROVE**, **SMALL FIX** or **REJECT** with a short reason. If you are not sure, say "unsure" and why. Reason codes (from the bible, 10.1): **X** cultural or visual error, **S** script or font problem, **P** politics or sensitive colour, **H** hands, people or other AI defect, **T** tone. About 15 to 20 minutes for a shortlist of three is my estimate. The zh-TW terms are an AI draft; correct them freely. **Please do not compare the pictures with photos of any real person; judge from memory.** If a picture reminds you of someone you know personally, say "someone I know" and you need not give the name. You do not need any fashion knowledge.

| # | Look at | zh-TW words to look for | Your answer |
|---|---|---|---|
| 1 | Does she look like a **grown-up of about thirty**? Not a student, not much older? | 成熟、穩重、像三十歲左右 (good) / 太年輕、像大學生、像高中生、童顏、太老 (not good) | |
| 2 | Is the face **natural and ordinary**, like a woman you could meet in Taiwan? Or a template? Should "that read as Taiwanese" be added to or kept out of the prompt? (addendum 12.1 item 2) | 自然、像一般人 (good) / 偶像臉、網美臉、韓系或日系偶像感、過度精緻 (not good) | |
| 3 | Does the face look **real or strange**? Eyes, teeth, ears, skin, the earring | 自然 (good) / 詭異、空洞、不自然、塑膠感、蠟像感、恐怖谷 (not good) | |
| 4 | Does she **remind you of a real person**? A local public figure (presenter, actress, singer, model, influencer, politician, athlete), or someone you know. Does she remind you of the other two characters? | 像不像某位藝人、主播、模特兒、網紅、政治人物、運動員，或你認識的人？像誰？跟另外兩個角色像嗎？ | |
| 5 | **Styling.** Blazer, cream top, persimmon neckerchief. Natural, or does the neckerchief look like an airline-crew or shop-staff scarf? Does outfit B (shirt, vest, midi skirt, tote) feel like a school uniform? | 上班穿搭、日常穿搭 (good) / 空服員感、店員感、制服感、學生裝、像 cosplay、很刻意 (not good) | |
| 6 | **The earring.** Does it read as a colour wheel? Does it look like a rainbow flag? Too big, or costume-like? | 色環、自然 (good) / 彩虹旗聯想、像道具、太大、太花 (not good) | |
| 7 | **Modesty and tone.** Right for Taiwan? Any glamour or "sexy" impression? | 端莊、得體 (good) / 性感、勾人、太貼身、太拘謹 (not good) | |
| 8 | **Colour impression** at small size. Any political or camp impression? Any all-black or all-white look? | 有沒有藍、綠、白、黃的政黨色聯想？全黑、全白 (喪事色) | |
| 9 | **The blush background.** Too pink or childish? Does it look like skin colour? Is 淡蜜桃色 a natural name? For the accent, which sounds natural: 柿子橘、柿橘 or 柿色? | 太粉、幼稚、少女感、像膚色 (not good) / 柔和、自然 (good) | |
| 10 | **Skin tone.** Only tell us if it looks different from one picture to the next, or if it looks whitened or tanned. (The studio never talks about skin tone in public posts.) | 膚色一致 / 忽深忽淺、修得太白 | |
| 11 | **Any writing** on the picture. There should be none. Numbers or letters on the chip cards or the earring? | 文字、數字、簡體字、亂碼、日文或港式字形 | |
| 12 | **The plain studio background.** Fine, or does it feel lifeless or "fake" to a Taiwanese viewer, given the user's complaint? | 乾淨、可以 / 空洞、假、沒生氣 | |
| 13 | **Would a Taiwanese viewer think this is a real person?** Is it clear it is AI? (informational) | 看起來像真人嗎？標示明不明顯？ | |
| 14 | **Taboo objects and brand marks.** There should be none | 神明桌、香、紙錢、白菊花、數字 4；商標、品牌標誌、車牌 | |
| 15 | **Rulings the addendum asks of you** (pronouns, face shape, wording, badge, jokes, two woman-presenting pilots on Instagram) | See addendum section 12 | |

Not needed from you: hands, anatomy, numbers, measurements, whether it is "good AI", or the name 色環 (a separate reading test, bible gate G3).

---

## 9. Common failure modes for this character, and fixes

### 9.1 Hand fix procedure

Prevention first: the master prompts keep hands out of the frame, and the standing prompts use trouser pockets. Run the 200% inspection (2.5) on every kept image.

**Finger check (when any hand, wrist or thumb is visible).** Count five fingers on each hand. Check there is one thumb, on the correct side. Check knuckles and joints bend naturally, no merged or doubled fingers, no extra joints, nails natural, the wrist joins the forearm, the cuff is continuous, the fingers are not melting into the pocket, the sleeve, the coat or the bag strap. If you cannot tell, it fails.

**Ladder (stop at the first rung that gives a passing image):**

1. **Reframe.** If the rest of the image is perfect and the hand is at the edge, crop it out in an image editor, as long as the crop still matches the framing in the prompt (a waist-up that ends at the waist) and does not cut off a visible mark or watermark that the tool added (if it would, re-roll instead). Log it as a human edit (crop) of its parent.
2. **Re-roll.** Send the same prompt again for 4 new images and choose one that passes.
3. **Prompt fix.** Add one line at the end: `Both hands are outside the picture; the frame ends at the waist.` or, for standing poses, `Both hands are fully inside her trouser pockets; no fingers or thumbs are visible.` Make 4 more.
4. **One conversational edit.** In the same chat ask: `Same image, but hide both hands: put them fully inside the trouser pockets.` or `Same image, reframed so the frame ends at the waist.` (*hypothesis*: the tool may support edits). One try only, then inspect again at 200%. Do not stack repeated edits: faces drift.
5. **Switch tool** and repeat 2 and 3.
6. **Stop.** Discard the image. **Never paint or redraw a hand by hand, never composite a photo of a real person's hand, never publish an image with a visible odd hand.** A published hand defect is a tripwire (addendum 8.3). Tell Claude if both tools fail the same way after two rounds each; the pose may need to change.

### 9.2 Symptoms and fix phrases

To use a fix phrase: add it at the end of the prompt (after the Character Lock and the prompt), regenerate 4, and see whether 3 or more now pass. In the same chat you can instead say "Same image, but: <phrase>" for a small fix.

| Symptom | Likely cause (hypothesis) | Fix phrase |
|---|---|---|
| Plastic, waxy, airbrushed or glowing skin | Beauty-render default | `Natural skin texture with visible fine pores and subtle tonal variation; matte; no airbrushing, no beauty filter, no glow, no shine.` |
| Idol, model or influencer look; over-pretty | Portrait default | `An ordinary everyday face with natural mild asymmetry, not a beauty-campaign model, no glamour, no idol look.` |
| Looks too young or like a student | Generators drift young | `She looks clearly about thirty to thirty-five: faint smile lines at the corners of the eyes, faint lines from the nose to the corners of the mouth, defined cheeks, a mature composed expression; not a teenager, not in her twenties.` |
| Looks too old or tired | Overcorrected | `About thirty, not middle-aged: only faint fine lines, even skin tone, no deep wrinkles, no grey hair.` |
| Skin looks lightened, whitened or pink; or tanned | Lighting or beauty default | `Exactly the same skin tone as the reference image: medium, warm golden-beige; do not lighten, brighten, whiten, tan or darken it.` |
| Hands or fingers appear | Generators love hands | Follow 9.1 |
| Teeth show, or look odd | Smile default | `Lips closed, no teeth visible.` |
| Uncanny eyes: different sizes, glassy, looking different ways, odd pupils | Eye detail | `Both eyes the same size with natural round pupils, both looking at the camera, one soft catchlight in each eye in the same place, no glassy stare.` |
| Hair tied back, fringe, both sides tucked, both sides forward, dyed, too long or too short | "Tucked behind one ear" read loosely | `Natural dark brown-black shoulder-length blunt-cut hair with a deep side parting, no fringe; one side tucked behind the ear so the ear and earring show, the other side falling forward past the cheek; not tied back, not dyed, no clips.` |
| The tucked side or the earring side flips between images | Left and right are weak instructions | New chat, attach only R01, add `The tucked ear and the earring are on exactly the same side as in Image 1.` Do not flip the picture |
| Earring wrong: rainbow, hoop, stud, one colour, wrong wedge count, too small or too large, letters | "Colour wheel" pulls toward a rainbow | `A matching pair of round drop earrings, each a flat matte enamel-look disc about 2.5 to 3 cm across, divided into twelve equal wedge segments in dusty, muted colours, not a saturated rainbow, no numbers, no letters, no gems. The tucked-side earring is fully visible.` Count the wedges; if only the count is off, fix in the editor (E) |
| Chip ring wrong: more or fewer than six cards, held in a hand, text or codes on the cards | An unusual prop | `A ring of exactly six blank rectangular colour-chip cards in muted tints, clipped to the belt loop, never held in a hand. No text, no numbers and no codes on the cards.` Attach R12 |
| Persimmon: too much, a second orange item, bright orange or red, or lost against the skin | The accent is over-applied or the colour drifts | `Exactly one persimmon accent (a soft, muted terracotta-orange, not bright orange, not red), a small matte item covering a small part of the picture; every other garment is cream, warm stone grey or charcoal.` |
| Neckerchief shiny, tight, a tie, a bow, or an airline-crew look | Scarf defaults | `A small neckerchief in matte cotton-linen, folded into a narrow band and loosely knotted at the front, ends tucked in; not satin, not shiny, not a tie, not a bow, not tight at the throat.` |
| Blazer drift: structured, double-breasted, a logo, odd buttons or collar | Fashion defaults | `An unstructured single-breasted blazer in warm stone grey, worn open, plain round buttons, plain notch collar, symmetrical, no logos, no text, no tags.` |
| School-uniform read in outfit B | Shirt plus vest plus skirt is a uniform cue | `Relaxed adult workwear cut: shirt collar open at the top button only, sleeves rolled to the elbow, no tie, no bow, no pleats; the midi skirt ends below the knee; no knee socks; not a school uniform.` If the age panel still says "student", tell Claude (X) |
| Costume or accessories: stylist, apron, lanyard, badge, glasses, necklace, watch | A "colour expert" association | `No stylist or professional uniform, no apron, no lanyard, no badge, no glasses, no necklace, no watch. Her only extras are the two colour-wheel earrings, one persimmon accent and, below the waist, the ring of blank colour-chip cards.` |
| Glamour or sexualised feel: parted lips, over-shoulder look, low angle, soft-focus glow, tight clothing | Female portrait default | `A neutral composed pose, eye-level camera, direct calm gaze, modest relaxed clothing, no glamour lighting, no parted lips, no body emphasis, collarbone covered.` |
| A swatch, fabric or colour card held near her face; a mirror, hanger or shopping bag appears | Fashion-photo defaults | `Nothing in her hands and nothing near her face: no swatch, no fabric sample, no mirror, no hanger, no shopping bag, no phone.` |
| Background not dusty blush: white, bright pink, cream, grey, gradient, a room | Not forced strongly enough | `Plain dusty-blush seamless studio background, a muted pinkish-peach, not bright pink, not white, not cream, not grey, evenly lit, no gradient, nothing else in the picture.` |
| Looks like a phone selfie or a candid snapshot | Realism default | `A polished studio character-reference portrait, not a phone snapshot, not a selfie, not candid.` |
| Face drifts from R01 with each picture | Building on the last output | New chat, attach only R01, resend. Never use a new output as the only reference twice in a row |
| She looks like 方寸 or 步驟 (the same default face) | Generator default; chat contamination | New chat for this character only; change one attribute in the prompt: `an oval face widest at the cheekbones tapering to a narrow, softly rounded chin; shoulder-length hair worn down.` Never upload the other character's image |
| Features look stereotyped or not ordinary | Generator defaults | `Ordinary, natural, unexaggerated features, no stereotype, no exaggeration.` |
| Colours drift: a saturated blue, green, teal or yellow garment; neon | Colour words are only hints | `Use only a muted palette: cream, warm stone grey, charcoal, and one persimmon accent (a soft, muted terracotta-orange), on a dusty-blush background. No saturated blue, green, teal or yellow, nothing neon.` |
| Text, hex codes or numerals appear (on a chip card, the earring, a tag) | Tools print what they are told | `The picture contains no text of any kind: no letters, no numerals, no codes, no Chinese characters, no logo, no watermark.` Any text fails the image even if it looks right |
| Head too large in full body | Portrait default | `Natural adult proportions: the head is about one seventh of her standing height.` |
| Feet or shoes odd (full body) | Feet are hard | `Two plain flat charcoal loafers, correct orientation, no logo, both fully visible.` |
| A visible mark or watermark appears | Tool behaviour | Leave it, note it in the log (7.5), do not remove it |
| The long avoid list makes the app draw the things it names | Naming a thing can summon it (hypothesis) | Use the short fallback below |
| She reminds a tester of someone, or a search shows a close match | The face itself | **X**: tell Claude. Regenerate with a changed attribute; never edit |
| Thumbnail loses the earring dot or looks like a teenager | The design or the prompt | Tell Claude. Do not edit around it |

### 9.3 Short avoid fallback (only if the long list backfires)

```
Avoid: hands, fingers; any resemblance to a real person; airbrushed or plastic skin; teeth showing; glasses; jewellery other than the two colour-wheel earrings; text, letters, numerals, logos, watermarks; a selfie or snapshot look; revealing or tight clothing; other people.
```

---

## 10. When you stop for the day

Tell Claude: which tool made the chosen R01 and the exact model label; **which side the hair is tucked on in the chosen R01**; which images you kept and discarded; the minutes you spent; which checklist rows failed most often (row 11, hands, and row 7, the earring wedges, will be the ones to watch); whether any tool refused a prompt, added a visible mark, or showed a seed; whether the face drifted between chats or began to look like 方寸 or 步驟; the licence terms you read (date, page, plan, the key sentence) or "not yet"; and what the wife said, including her answers to the open items in the addendum (section 12). Claude can then update the bible's status, record the tool test in `pipeline/tools.md`, write the provenance rows from your notes, and set up the next sitting.

**Nothing from this pack is approved** until the age-guess test, the look-alike tests, the reverse-image search, the near-pair test, light hand-finishing (no skin smoothing or brightening) and the approvals by the wife and the operator are done. The name 色環, the studio name and the handle are still unchecked and are not part of this session. No post, account or client work is made from these images.
