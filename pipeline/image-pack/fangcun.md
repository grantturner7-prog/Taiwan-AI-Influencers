# 方寸 (fangcun) image pack: first reference images

**Pack v1, written 2026-10-11.** For the operator (English only) and the wife (language and culture review). Source of truth: `personas/fangcun/bible.md`, sections 4 and 5, plus its Review log and Phase 3 integration log, which override earlier text. If this pack and the bible ever disagree, the bible wins; tell Claude and the pack gets fixed.

**Status of everything you make with this pack: working references, not approved assets.** Nothing is cleared for public use until the master is hand-finished, both human tests in section 6 are passed, and the wife and operator approve it (bible gate G4). Nothing has been generated yet; no reference image exists.

**How to use it:** read sections 0 and 1, then do sections 2 and 3 in order. Keep section 5 (checklist) and section 7 (log) open while you work. Copy the contents of each code box exactly as written. Model names, buttons and features in Gemini and ChatGPT change often, so every statement about them below is a hypothesis: check the current screen.

---

## 0. One-screen summary

**Who.** 方寸 (Fāngcùn, roughly "fahng-tsun") is an AI character: a tall, slim, gender-neutral adult (stated age 32) built from stacked rounded clay blocks, with a cube-shaped head, two dot eyes, two thin brow bars, a line for a mouth, and no hands (the arms end in smooth mitten shapes). It wears muted oat, sage and walnut-brown clothes and a cream tape-measure strip as a belt, and always stands beside a floor plan, a scale bar or a door so the picture itself shows size. It will explain small-flat and renting arithmetic (will the wardrobe fit, how much floor does a door swing take) to Taiwan audiences on Instagram and YouTube Shorts. It is openly an AI character from the studio; it has never lived in a home or used a product, so its pictures are always labelled illustrations.

**Goal of the first session.**
1. Pick one master picture (R01, a four-view sheet) that passes the checklist.
2. Use it to make the next six reference images: three-quarter left, three-quarter right, side, back, head turnaround, and the ten-face expression sheet (R02 to R07).
3. Log every file the same day. The tests with other people, hand-finishing and the rest of the set (R08 to R16) come after.

**Time (my estimate, not measured).** About 3 to 4 hours hands-on for R01 to R07, best split into two sittings. About 15 minutes of the wife's time on the shortlist. About an hour on another day for the tests with other people. Write down your real minutes; the studio's capacity plan needs them.

**Order of work.**

| Step | What | Where in this pack |
|---|---|---|
| 1 | Make the folders and open the log (5 min) | Section 1 |
| 2 | R01 prompt in Gemini (4 images) and in ChatGPT (4 images) | Section 2 |
| 3 | Throw out obvious failures, run the checklist on the rest, shortlist at most 3 | Sections 2.5, 5 |
| 4 | Wife looks at the shortlist; you run the reverse-image search | Sections 8, 6.3 |
| 5 | Choose a provisional master and save it as `R01_master_v1` | Section 2.5 |
| 6 | R02 to R07, always with R01 attached | Sections 3, 4 |
| 7 | Log as you go, not at the end | Section 7 |
| 8 | Another day: age-guess test, look-alike blind test, R08 to R16, hand-finish, freeze the set (with Claude, Phase 4) | Sections 6, 3 |

---

## 1. Before you start

- **Tool: start with Gemini, then run the same prompt in ChatGPT (hypothesis, not a finding).** The bible's Gemini recipe is the simplest workflow (attach the reference picture, ask for one change), which makes it the easier start for a non-technical operator. That is the whole reason: a tie-breaker, not evidence. The bible's ChatGPT recipe is the more structured one (separate PRESERVE, CHANGE, OUTPUT and AVOID blocks). Nobody has tested either tool on this character; that is what today finds out. Once R01 is chosen, stay in the tool that made it for R02 to R07 (hypothesis: one tool keeps the set consistent). You may upload the chosen R01 into the other tool later.
- **Settings to look for, only if available in the current app.** Image shape or aspect ratio (wide for sheets, 4:5 portrait for single figures, 1:1 for faces; if there is no setting, the OUTPUT line in each prompt asks for it). Number of images per request (set 4; if not offered, press regenerate or send the prompt again until you have 4 separate images; do not ask for "a grid of 4 versions"). Highest quality or resolution. A model or version picker (pick one and keep it for the whole sitting; copy its label exactly). Style presets or filters (leave off, so only the prompt sets the look). Chat history (do not use a temporary or private chat mode: you need the conversation link for the log). Use the download button for the largest version; a screenshot is the last resort and must be noted in the log.
- **Never upload a photo of a real person, or a picture of any existing character, at any point, including "just to copy the pose".** Do not upload photos of real rooms either (bible 4.9). The only pictures you may upload are ones made with this pack (your own R01 and so on). Describe poses in words, as the prompts do. Never type the name of a living artist, a studio, a brand or an existing character into a prompt.
- **Save everything and log everything.** Download every image you look at for more than a glance, straight into `assets/fangcun/` (or its `candidates` folder) with the file name from this pack. Do not edit or rename-over the original download. Delete nothing today. Add a row to `assets/provenance.csv` the same day for every kept file and every discarded-but-considered file (section 7).
- **Licence terms have not been checked.** This pack does not know what Gemini or ChatGPT allow for commercial use on your plan. Before any commercial use, read the current terms for the exact tool and plan you used, and record what you found and the date in `licence_notes` on every row. Until that is done, treat every image as internal design material only.

**Set-up (about 5 minutes).**
1. In the project folder, open `assets/fangcun/` (it exists and is empty). Inside it, make two folders: `candidates` (every image you considered but did not choose) and `lookalike` (screenshots from section 6).
2. Open `assets/provenance.csv` in a spreadsheet app. The header must read `timestamp,asset_path,persona,tool,model,prompt,licence_notes`. Do not change it.
3. Copy the Character Lock (section 4.1) into a notes file so you can paste it quickly from Step 2 on.
4. In the same notes file, start a line "minutes: " and add your times as you go.

---

## 2. STEP 1: the master reference R01

**What you are making.** One picture that is a character sheet: the same figure shown four times (front, three-quarter left, side, back), full body, plain warm off-white background, neutral face, everyday outfit O1. The bible calls R01 the "front full-body master identity"; the front view on this sheet is that master, and R02 to R05 later give each view its own larger picture. Shape: wide, if the app offers it (my suggestion; the bible does not fix a shape for the sheet).

The two prompts below carry the same design. They differ only in the opening line and in how the Avoid list is attached (bible 5.3 describes Gemini as conversational and ChatGPT as structured). The body text is the bible's master prompt (5.2) and Avoid list (5.4), copied unchanged. The opening line is the only wording added.

### 2.1 Gemini: paste this

```
Create an image from this brief.

Character design reference sheet for an original, fictional, adult virtual character (working name "Fangcun").

MEDIUM: a hand-sculpted matte clay maquette look, photographed on a plain table. Soft diffused studio light, soft contact shadows, faint thumbprint micro-texture on the clay, no gloss, no plastic sheen. Plain warm off-white seamless background (#F5F0E6).

FIGURE: tall and slim, about seven head-heights tall, calm upright posture, relaxed shoulders. The body is made of stacked rounded rectangular clay blocks separated by thin hairline seams: a rounded-cube head, a chest block, a waist block, a hip block and two long leg blocks. Gender-neutral, no gendered cues. Clearly an adult in their early thirties: adult proportions, a small head relative to the body, long slender limbs.

HEAD: rounded cube with softly rounded corners, matte oat-coloured clay (#E4D9C3). Two small round matte charcoal dot eyes (#3B3631), no highlights, set wide apart at the upper-middle of the face. Two thin short charcoal brow bars above the eyes. One thin horizontal charcoal mouth line. No nose, no ears, no eyelashes, no blush, no teeth. A short flat hair slab in walnut brown (#6E5440) with a side parting, sitting like a cap.

ARMS AND FEET: slender rounded bars ending in simple rounded mitten-shaped paddles. No fingers, no thumbs, no hands. Simple rounded flat shoes in walnut brown, no logo.

OUTFIT (default "O1 Everyday"): oat knit-textured chest block with a rolled hem, an open sleeveless vest in muted sage (#A9B5A0), walnut-brown trouser blocks (#6E5440). A cream tape-measure strip (#EFE6CF) with fine charcoal tick marks and no numerals, worn as a belt at the waist seam, with a small walnut buckle.

COLOUR: mostly oat and walnut, sage only as a small accent. Muted, low-saturation palette only. No saturated blue, green, teal or yellow.

SHEET LAYOUT: four full-body views of the same figure at the same scale, evenly spaced on one sheet: front, three-quarter left, side, back. Eye-level camera, no perspective distortion.

TEXT: no text, letters, numerals, logos, labels or watermarks anywhere in the image.

Avoid: hands, fingers, thumbs; toy-brick studs, pegs or interlocking connectors; yellow skin; printed face; claw hands; pixelated or voxel cubes; cylinder head; large glossy eyes, sparkles, eyelashes, blush, tears; chibi, baby or child-like proportions, oversized head, rosy cheeks; pastel candy colours; school uniform; uniform or costume of any profession (hard hat, high-visibility vest, overalls, lab coat, logo apron); sexualised pose or clothing; any real person's face or likeness; any celebrity; any existing cartoon, game, mascot or toy character; any artist's, studio's or brand's style; text, letters, numerals, logos, brand marks, signage, watermark; other people, children, pets; saturated blue, green, teal or yellow dominant colours; party-colour combinations; glossy plastic finish, neon, lens flare; snow, maple leaves, carpet, kitchen island, dishwasher, clothes dryer, fireplace (for Taiwan flat scenes).
```

### 2.2 ChatGPT: paste this

```
Generate one image from the brief below.

Character design reference sheet for an original, fictional, adult virtual character (working name "Fangcun").

MEDIUM: a hand-sculpted matte clay maquette look, photographed on a plain table. Soft diffused studio light, soft contact shadows, faint thumbprint micro-texture on the clay, no gloss, no plastic sheen. Plain warm off-white seamless background (#F5F0E6).

FIGURE: tall and slim, about seven head-heights tall, calm upright posture, relaxed shoulders. The body is made of stacked rounded rectangular clay blocks separated by thin hairline seams: a rounded-cube head, a chest block, a waist block, a hip block and two long leg blocks. Gender-neutral, no gendered cues. Clearly an adult in their early thirties: adult proportions, a small head relative to the body, long slender limbs.

HEAD: rounded cube with softly rounded corners, matte oat-coloured clay (#E4D9C3). Two small round matte charcoal dot eyes (#3B3631), no highlights, set wide apart at the upper-middle of the face. Two thin short charcoal brow bars above the eyes. One thin horizontal charcoal mouth line. No nose, no ears, no eyelashes, no blush, no teeth. A short flat hair slab in walnut brown (#6E5440) with a side parting, sitting like a cap.

ARMS AND FEET: slender rounded bars ending in simple rounded mitten-shaped paddles. No fingers, no thumbs, no hands. Simple rounded flat shoes in walnut brown, no logo.

OUTFIT (default "O1 Everyday"): oat knit-textured chest block with a rolled hem, an open sleeveless vest in muted sage (#A9B5A0), walnut-brown trouser blocks (#6E5440). A cream tape-measure strip (#EFE6CF) with fine charcoal tick marks and no numerals, worn as a belt at the waist seam, with a small walnut buckle.

COLOUR: mostly oat and walnut, sage only as a small accent. Muted, low-saturation palette only. No saturated blue, green, teal or yellow.

SHEET LAYOUT: four full-body views of the same figure at the same scale, evenly spaced on one sheet: front, three-quarter left, side, back. Eye-level camera, no perspective distortion.

TEXT: no text, letters, numerals, logos, labels or watermarks anywhere in the image.

AVOID: hands, fingers, thumbs; toy-brick studs, pegs or interlocking connectors; yellow skin; printed face; claw hands; pixelated or voxel cubes; cylinder head; large glossy eyes, sparkles, eyelashes, blush, tears; chibi, baby or child-like proportions, oversized head, rosy cheeks; pastel candy colours; school uniform; uniform or costume of any profession (hard hat, high-visibility vest, overalls, lab coat, logo apron); sexualised pose or clothing; any real person's face or likeness; any celebrity; any existing cartoon, game, mascot or toy character; any artist's, studio's or brand's style; text, letters, numerals, logos, brand marks, signage, watermark; other people, children, pets; saturated blue, green, teal or yellow dominant colours; party-colour combinations; glossy plastic finish, neon, lens flare; snow, maple leaves, carpet, kitchen island, dishwasher, clothes dryer, fireplace (for Taiwan flat scenes).
```

If an app answers with text instead of a picture, reply "Please generate the image now." If the app has no shape setting and gives a square or tall picture, add this as a last line of the prompt (my addition): "Make it a wide landscape image."

### 2.3 The Avoid list on its own

Chat tools have no negative-prompt box, so the Avoid list is a sentence at the end of the prompt (already done in 2.1 and 2.2). Keep this copy for tools or modes that do have a separate negative field, and for adding to a retry. If the long list seems to make an app draw the things it names, use the short fallback in section 9.

```
Avoid: hands, fingers, thumbs; toy-brick studs, pegs or interlocking connectors; yellow skin; printed face; claw hands; pixelated or voxel cubes; cylinder head; large glossy eyes, sparkles, eyelashes, blush, tears; chibi, baby or child-like proportions, oversized head, rosy cheeks; pastel candy colours; school uniform; uniform or costume of any profession (hard hat, high-visibility vest, overalls, lab coat, logo apron); sexualised pose or clothing; any real person's face or likeness; any celebrity; any existing cartoon, game, mascot or toy character; any artist's, studio's or brand's style; text, letters, numerals, logos, brand marks, signage, watermark; other people, children, pets; saturated blue, green, teal or yellow dominant colours; party-colour combinations; glossy plastic finish, neon, lens flare; snow, maple leaves, carpet, kitchen island, dishwasher, clothes dryer, fireplace (for Taiwan flat scenes).
```

### 2.4 What to generate

- **4 images in Gemini and 4 in ChatGPT.** Each image is itself a four-view sheet. Four separate images per tool, not one image containing four sheets.
- Save each one at once as `assets/fangcun/candidates/R01_cand_gemini_1.png` to `_4`, and `R01_cand_chatgpt_1.png` to `_4`. If the app gives you another file type (`.jpg`, `.webp`), keep that type and use the real name in the log.
- Write down, for each: the tool, the model label exactly as the app shows it today, the time, and the conversation link or ID if the app gives one. If a seed number is shown, write it down.
- If nothing passes, change one thing (a fix phrase from section 9), generate 4 more, and repeat. The bible's planning figure is about 8 to 12 candidates per tool (an assumption). If both tools fail the same way after two rounds, stop and tell Claude: the design may need a change in the bible.

### 2.5 How to choose

1. **Thirty-second reject pass.** Throw out any sheet with any text or numerals, any fingers or hands, toy-brick studs or pegs, glossy plastic, an oversized head, or a figure that changes between the four views. Do not delete the files (they are already in `candidates`); mark them "rejected" in your notes.
2. **Checklist.** Run section 5 on each survivor, using the front view at full size and then shrunk to thumbnail size.
3. **Shortlist at most three.** Prefer the sheet where the four views clearly show the same character, the front view is cleanest, and the back view shows the tape-measure belt going round the waist.
4. **Wife looks** at the shortlist (section 8). **You run the reverse-image search** on each shortlisted image (section 6.3).
5. **Choose one** and copy it to `assets/fangcun/R01_master_v1.png` (keep the original in `candidates`). Log it as "provisional master". It becomes the real master only after the age-guess and look-alike blind tests (section 6) pass and the sheet has been hand-finished in an image editor (bible 5.8 steps 3 and 4).

---

## 3. STEP 2: lock it

### 3.1 How the master is used as the reference

Two ways, and a recommendation.
- **Same chat:** keep going in the chat that made R01, send a new prompt, and the app can see the earlier picture. Fast, but each new picture is built on the last one and the face can drift (assumption).
- **New chat with R01 re-uploaded (recommended).** Open a fresh chat, attach your saved `R01_master_v1` file (your own image; uploading it is fine), then send the Character Lock followed by the prompt for that image. The bible's advice is to restart and re-attach rather than correct in a long thread (assumption; this sitting confirms or refutes it). Use "same chat" only to retry the same image with a small fix.

Rules from the bible (5.8) that apply to every image below:
1. Attach R01 every time, plus at most two other references. Never anchor to a freshly generated output alone.
2. One change per picture (one angle, one outfit, one expression set).
3. Make 4, choose the best, and compare it with R01 **at the same size** using the checklist in section 5.
4. If two pictures in a row fail the locked features, stop and re-anchor: new chat, R01 attached, nothing else.
5. All pictures are text-free. Chinese text and numbers are added later, in a design tool, never by the generator.

### 3.2 What every message looks like

Message = **Character Lock** (section 4.1, pasted first) + **a blank line** + **the prompt for that image** (the code boxes below). Attach the files named on the "Attach" line before you send.

**Per-image routine (about 10 minutes each; my estimate).**
1. Open a new chat in the tool that made R01.
2. Attach the files on the "Attach" line. In ChatGPT the bible says to use its image edit mode with reference images if the app offers one; otherwise attach the images to a normal message. In Gemini, attach them to the message.
3. Paste the Character Lock, a blank line, then the prompt for that image.
4. Get 4 images (settings in section 1) and save all 4 into `candidates` at once.
5. Run the checklist (section 5) on each, choose one, and copy it to its pack name.
6. Add the log rows (kept and discarded) before you start the next image.

Where an image is attached as the second reference, the prompt says "Image 2 is ..."; "Image 1" always means the first file you attached, which is R01.

Each prompt below ends with an OUTPUT line (shape, plain warm off-white background #F5F0E6, soft contact shadow, full body with room around it so it can be cut out, one image). That wording comes from the bible's variants (5.3). The shapes are my suggestions: 4:5 portrait for single figures, 3:2 or 16:9 for sheets, 1:1 for faces. The bible allows 1:1, 4:5 or 9:16 for single images and does not fix a shape for sheets.

### 3.3 Order of work, file names and what to attach

Save files in `assets/fangcun/`. Version number `v1` goes up if you redo an image (`v2`). File types follow whatever the app gives you. Candidates you looked at but did not choose go in `assets/fangcun/candidates/` as `<ID>_cand_<tool>_<n>`.

| Order | ID | Image | Attach | Save the chosen one as | When |
|---|---|---|---|---|---|
| 1 | R01 | Master four-view sheet | nothing | `R01_master_v1.png` | Today, Step 1 |
| 2 | R02 | Three-quarter left, full body | R01 | `R02_three-quarter-left_v1.png` | Today |
| 3 | R03 | Three-quarter right, full body | R01 | `R03_three-quarter-right_v1.png` | Today |
| 4 | R04 | Side profile, full body | R01 | `R04_side_v1.png` | Today |
| 5 | R05 | Back view, full body | R01 | `R05_back_v1.png` | Today |
| 6 | R06 | Head turnaround (face lock) | R01 | `R06_head-turnaround_v1.png` | Today |
| 7 | R07 | Expression sheet E01 to E10 | R01, R06 | `R07_expressions_v1.png` | Today; prompt in section 4.2 |
| 8 | R09 | Outfit sheet O1, O2, O3 | R01 | `R09_outfits_v1.png` | Next sitting |
| 9 | R11 | Scale reference beside a door and a single bed | R01 | `R11_scale-door-bed_v1.png` | Next sitting |
| 10 | R13 | Detail close-ups | R01 | `R13_details_v1.png` | Next sitting |
| 11 | R08 | Pose sheets P01 to P12 | R01 | `R08_poses-P01-P06_v1.png`, `R08_poses-P07-P12_v1.png` | Next sitting; prompt in section 4.4 |
| 12 | R10 | Seasonal sheet: summer, winter, rain | R01, R09 | `R10_seasonal_v1.png` | Next sitting |
| 13 | R05b | Back view in the rain shell (O3) | R01, R09 | `R05b_back-rain-shell_v1.png` | Next sitting |
| 14 | R15 | Diagram style anchor (no character) | nothing | `R15_diagram-anchor_v1.png` | Next sitting, optional |
| 15 | R14 | Avatar 1:1 and 110 px test | R01, R06 | `R14_avatar-1x1_v1.png` | After the master is final |
| 16 | R12 | Palette card (made by hand) | none | `R12_palette-card_v1.png` | See 3.5 |
| 17 | R16 | Badge and slide templates (made by hand) | none | later | See 3.5 |

The bible's list uses the folder `assets/fangcun/ref/` and names like `fc_ref_R01_front_v1_YYYYMMDD.png` for the frozen golden set. The names above are the working names for today; renaming into the golden-set scheme happens when the set is frozen (bible 5.8 step 4 and 7), and Claude can do that rename and update the log paths.

### 3.4 The prompts (send after the Character Lock)

**R02: three-quarter left.** Attach: R01. (Which way R02 and R03 face matters less than their being opposites; the bible does not define "left" for this view, so the direction below is my reading.)

```
CHANGE only: the angle. Show the same character in a three-quarter view, the whole body turned about 45 degrees so that it faces toward the viewer's left. Keep the neutral face, outfit O1 and relaxed arms.
OUTPUT: 4:5 portrait; the character alone on a plain warm off-white background (#F5F0E6); soft contact shadow; full body in frame with clear space around it so it can be cut out; one image.
```

**R03: three-quarter right.** Attach: R01.

```
CHANGE only: the angle. Show the same character in a three-quarter view, the whole body turned about 45 degrees so that it faces toward the viewer's right. Keep the neutral face, outfit O1 and relaxed arms.
OUTPUT: 4:5 portrait; the character alone on a plain warm off-white background (#F5F0E6); soft contact shadow; full body in frame with clear space around it so it can be cut out; one image.
```

**R04: side profile.** Attach: R01.

```
CHANGE only: the angle. Show the same character in a side profile, the whole body seen exactly from the side, facing toward the viewer's left. The head stays a rounded cube; still no nose and no ear. Keep the neutral face, outfit O1 and relaxed arms.
OUTPUT: 4:5 portrait; the character alone on a plain warm off-white background (#F5F0E6); soft contact shadow; full body in frame with clear space around it so it can be cut out; one image.
```

**R05: back view.** Attach: R01.

```
CHANGE only: the angle. Show the same character from directly behind, the whole body seen from the back: the back of the walnut hair slab, the back of the open sage vest, and the cream tape-measure belt going round the waist seam. Relaxed arms, outfit O1.
OUTPUT: 4:5 portrait; the character alone on a plain warm off-white background (#F5F0E6); soft contact shadow; full body in frame with clear space around it so it can be cut out; one image.
```

**R06: head turnaround (face lock).** Attach: R01.

```
CHANGE only: the framing. Make a head turnaround close-up: three views of the head and shoulders only, same scale, evenly spaced on one sheet, in this order: front, three-quarter (turned toward the viewer's left), side. Eye-level camera, no perspective distortion. Neutral face in all three. Rounded-cube head with the same corner softness in every view.
OUTPUT: 3:2 landscape; plain warm off-white background (#F5F0E6); soft contact shadows; one image.
```

**R07: expression sheet.** Attach: R01, R06. The prompt is in section 4.2, with single-expression prompts in 4.3.

**R08: pose sheets.** Attach: R01. The prompts are in section 4.4.

**R09: outfit sheet (O1, O2, O3).** Attach: R01.

```
CHANGE only: the outfit, shown as three versions of the same figure side by side on one sheet, same scale, all in front view, neutral face, relaxed arms, left to right:
1. O1 Everyday: oat knit-textured chest block (#E4D9C3) with a rolled hem, open sleeveless vest in muted sage (#A9B5A0), walnut trouser blocks (#6E5440), cream tape-measure belt (#EFE6CF) at the waist seam.
2. O2 Diagram day: deep-walnut (#5C4636) chunky knit pullover over oat trouser blocks (#E4D9C3), cream tape-measure belt (#EFE6CF).
3. O3 Rain, out: putty-coloured (#CFC6B4) light hooded shell, hood down, over the oat chest block; walnut trousers (#6E5440); the cream tape-measure belt visible outside the shell. No reflective strips.
No logos, text or patterns on any clothing. Nothing else about the character changes.
OUTPUT: 3:2 landscape; plain warm off-white background (#F5F0E6); soft contact shadows; full bodies in frame; one image.
```

**R10: seasonal sheet (summer, winter, rain).** Attach: R01, R09. (The bible allows sage or putty for the winter scarf; I chose putty to keep sage a small accent.)

```
Image 2 is the outfit sheet; use it for outfit O3 (the rain shell) only.
CHANGE only: the outfit, shown as three versions of the same figure side by side on one sheet, same scale, all in front view, neutral face, relaxed arms, left to right:
1. Summer (hot and humid): outfit O1 without the vest; a short-sleeve linen-textured chest block; trousers ending above the knee; simple flat sandal blocks, no toes.
2. Winter (damp cold): outfit O1 plus a chunky knit cardigan block and a scarf block in putty (#CFC6B4). No snow, no maple leaves, no puffer coat.
3. Rain: outfit O3, a putty-coloured (#CFC6B4) light hooded shell with the hood down over the oat chest block, walnut trousers, the cream tape-measure belt visible outside the shell. No reflective strips.
No logos, text or patterns on any clothing. Nothing else about the character changes. Muted palette only.
OUTPUT: 3:2 landscape; plain warm off-white background (#F5F0E6); soft contact shadows; full bodies in frame; one image.
```

**R05b: back view in the rain shell (O3).** Attach: R01, R09. Image 2 is the outfit sheet; use it for the rain shell only.

```
Image 2 is the outfit sheet; use it for outfit O3 (the rain shell) only.
CHANGE only: the angle and outfit. Show the character from directly behind wearing outfit O3: the putty-coloured (#CFC6B4) light hooded shell with the hood down, the hood clearly visible from behind, over the oat chest block, walnut trousers, and the cream tape-measure belt visible outside the shell. No reflective strips. Relaxed arms.
OUTPUT: 4:5 portrait; the character alone on a plain warm off-white background (#F5F0E6); soft contact shadow; full body in frame with clear space around it so it can be cut out; one image.
```

**R11: scale reference beside a standard door and a single bed.** Attach: R01. This is the adult-scale check (bible 4.8). The door height of about 200 cm and the 85 percent figure are recalled design targets, unverified; judge by eye.

```
CHANGE only: the pose and setting. Show the character standing upright beside a plain flat door, front view, neutral face, relaxed arms. The door is a plain flat putty-coloured (#CFC6B4) door in a simple frame with a plain handle, no signs, no numbers, no marks. The top of the character's head reaches about 85 percent of the door height. To the right of the door, at the same ground line and the same scale, place a plain single bed with an oat-coloured (#E4D9C3) cover and a walnut-tint (#BBA48F) frame, no pattern, no print, no text. Eye-level camera, no perspective distortion, no wide-angle. Nothing else in the picture.
OUTPUT: 3:2 landscape; plain warm off-white background (#F5F0E6); soft contact shadows; the whole door, bed and full-body character in frame; one image.
```

**R13: detail close-ups.** Attach: R01.

```
CHANGE only: the framing. Make a detail sheet of four close-ups of the same character, in a 2 by 2 grid, same lighting, matte clay:
1. The cream tape-measure belt and its small walnut buckle at the waist seam, with fine charcoal tick marks and no numerals.
2. The hairline seams between two stacked blocks, shallow and clean.
3. One arm end: a smooth rounded mitten-shaped paddle. No fingers, no thumbs, no hand.
4. One simple rounded flat walnut shoe, no logo, no tread pattern.
No text, letters or numerals anywhere.
OUTPUT: 1:1 square; plain warm off-white background (#F5F0E6); soft contact shadows; one image.
```

**R14: avatar (optional AI route).** Attach: R01, R06. Easier route: crop the head and shoulders from R02 or R06 in any image editor, make it square, and log it as a human edit. Then do the 110 px test (section 5, check 9).

```
CHANGE only: the framing. Head and shoulders only, front view, neutral face, centred, with a little space around the head so a circular crop will not cut it.
OUTPUT: 1:1 square; plain warm off-white background (#F5F0E6); soft contact shadow; one image.
```

**R15: diagram style anchor (no character).** Attach: nothing. Do **not** paste the Character Lock here. This is the bible's scene-only template with its layout line filled in from the bible's own example. Human-built diagrams are preferred for real posts (numbers and text go in a design tool), so treat this as a look reference only. The wife checks the Taiwan details (section 8).

```
Flat isometric floor-plan style illustration of a small Taiwan rental studio flat, seen from above at 30 degrees, with thin charcoal (#3B3631) outlines and flat muted fills (oat #E4D9C3, putty #CFC6B4, sage tint #D6DCCF, walnut tint #BBA48F) on a warm off-white background (#F5F0E6).
Layout: single bed along the left wall, small desk under the window, wardrobe on the right wall, entrance with shoe cabinet, rear balcony with washing machine and drying pole.
Taiwan details: shoes-off entrance with a shoe cabinet, tile floor, aluminium sliding window with a metal window grille, a split-type air conditioner high on a wall, a rice cooker on the kitchen counter.
Leave every dimension label and text area as an empty rectangle.
No people, no hands, no pets. No text, numerals, logos or brand marks. No carpet, kitchen island, dishwasher, clothes dryer or fireplace. No blue, teal, bright green or yellow.
```

### 3.5 Images that are not generated

- **R12 palette card.** Made by hand in any slides or design app: one square swatch per colour with its hex written under it. The colours and checking ranges are in section 5.3. Log it with tool "human-made in <app name>" and prompt "none (made by hand)".
- **R16 badge and slide templates.** The badge carries Chinese text (「AI 生成｜示意圖」). Do **not** ask Gemini or ChatGPT to draw it. It is built later in a design tool with a Taiwan-form font (the bible names Noto Sans TC), and the wife reads every character. Not part of this session.
- **R14 avatar crops and the 110 px test** are cut from the final master, so they wait until it is hand-finished.

---

## 4. Expression sheet and pose prompts

### 4.1 The Character Lock (paste this at the start of every prompt in sections 3 and 4)

It is built from the bible's "Keep identical" (Gemini) and "PRESERVE exactly" (ChatGPT) lists in bible 5.3, with the colours from bible 4.5 and the default outfit from bible 4.4. Attach R01 first. Do not use it for R15 or R01 itself.

```
Image 1 is the chosen master reference sheet for the original, fictional, adult virtual character "Fangcun". Use it as the exact design. The character is a gender-neutral adult in their early thirties, about seven head-heights tall, slim, calm and upright, built from stacked rounded clay blocks with thin hairline seams.

PRESERVE exactly: the rounded-cube head with softly rounded corners; the two small round matte charcoal dot eyes (#3B3631), set wide apart, no highlights; the two thin short charcoal brow bars; the one thin horizontal charcoal mouth line; no nose, no ears, no eyelashes, no blush, no teeth; the short flat walnut hair slab (#6E5440) with a side parting, sitting like a cap; the stacked-block body with hairline seams; the slender arms ending in smooth rounded mitten-shaped paddles (no fingers, no thumbs, no hands); simple rounded flat walnut shoes with no logo; the matte hand-sculpted clay material with faint thumbprint texture, no gloss; the cream tape-measure belt (#EFE6CF) with fine charcoal tick marks, no numerals, and a small walnut buckle; the muted palette (oat #E4D9C3, walnut #6E5440, sage #A9B5A0 only as a small accent); proportions (about seven head-heights). Do not redesign, restyle, smooth, add detail or change proportions. The only exception is the single change asked for below (for example an outfit, a pose, an expression or an angle).

DEFAULTS unless the change below says otherwise: neutral face (brows level, mouth flat); outfit O1 Everyday (oat knit-textured chest block with a rolled hem, open sleeveless sage vest, walnut trouser blocks, the cream tape-measure belt); arms hanging relaxed. Soft diffused studio light.

AVOID: text of any kind, letters, numerals, logos, watermarks; hands, fingers; other people; props not listed; gloss or plastic sheen; tears, sparkles, an open laughing mouth, a tongue; any change to the design.
```

### 4.2 R07: expression sheet (all ten at once)

Attach: R01 and R06. No labels on the picture: the generator would garble them. You tell the faces apart by position: top row left to right is E01 to E05, bottom row is E06 to E10. Zh-TW names are for the wife and for your notes only; the prompt is English. Rules from the bible (5.5): expressions are made only with the brows, the mouth line and a small shift of the dots; the one allowed deformation is E09 (the dots become short upward arcs); never blush, tears, sparkles, an open laughing mouth or a tongue.

| ID | Name | Face |
|---|---|---|
| E01 | 平靜 neutral (default) | Brows level, mouth flat |
| E02 | 滿意 pleased | Brows relaxed and slightly raised, mouth with a slight upward curve |
| E03 | 思考 thinking | One brow raised, dots shifted up-left, mouth short and flat |
| E04 | 發現 noticing | Both brows raised, mouth a small round "o" |
| E05 | 不確定 hmm | Brows angled slightly inward and down, mouth a short wavy line |
| E06 | 更正 correcting | Inner brow ends raised, head tilted about 5 degrees, mouth flat |
| E07 | 說明 explaining | Brows level, mouth a thin open ellipse line |
| E08 | 冷面 deadpan | Brows level and low, a flat upper-lid line over each dot, mouth flat |
| E09 | 微笑 soft smile | Dots become short upward arcs, mouth gentle curve |
| E10 | 點頭 calm nod | Head tilted down 5 to 10 degrees, dots, slight mouth curve |

```
Image 2 is the head turnaround; use it for the face only.
CHANGE only: the expression, shown as an expression sheet of the same head and shoulders ten times, same scale, evenly spaced in two rows of five, no labels, no text. Top row left to right:
1. Brows level, mouth flat.
2. Brows relaxed and slightly raised, mouth with a slight upward curve.
3. One brow raised, dots shifted up-left, mouth short and flat.
4. Both brows raised, mouth a small round "o".
5. Brows angled slightly inward and down, mouth a short wavy line.
Bottom row left to right:
6. Inner brow ends raised, head tilted about 5 degrees, mouth flat.
7. Brows level, mouth a thin open ellipse line.
8. Brows level and low, a flat upper-lid line over each dot, mouth flat.
9. The dots become short upward arcs, mouth a gentle curve.
10. Head tilted down 5 to 10 degrees, the dots stay round, slight mouth curve.
Only the brows, the mouth line and a small shift of the dots change. Same head, same colours, same matte clay in all ten.
OUTPUT: 16:9 landscape; plain warm off-white background (#F5F0E6); soft contact shadows; one image.
```

If ten faces on one sheet come out wrong or merged, split it into two sheets of five (faces 1 to 5, then 6 to 10) by deleting the other row from the prompt, and save as `R07a_expressions-E01-E05_v1` and `R07b_expressions-E06-E10_v1`. If that still fails, use the single-expression prompts in 4.3.

### 4.3 Single-expression prompts (E01 to E10)

Attach: R01 and R06 (Image 2 is the head turnaround, used for the face only). Send the Character Lock, then one block below. Save as `EXP_E04_noticing_v1` and so on.

E01 neutral:
```
Image 2 is the head turnaround; use it for the face only.
CHANGE only: the expression (E01, neutral): brows level, mouth flat. Only the brows, the mouth line and a small shift of the dots can change.
OUTPUT: 1:1 square; head and shoulders only; plain warm off-white background (#F5F0E6); soft contact shadow; one image.
```

E02 pleased:
```
Image 2 is the head turnaround; use it for the face only.
CHANGE only: the expression (E02, pleased): brows relaxed and slightly raised, mouth with a slight upward curve. Only the brows, the mouth line and a small shift of the dots can change.
OUTPUT: 1:1 square; head and shoulders only; plain warm off-white background (#F5F0E6); soft contact shadow; one image.
```

E03 thinking:
```
Image 2 is the head turnaround; use it for the face only.
CHANGE only: the expression (E03, thinking): one brow raised, dots shifted up-left, mouth short and flat. Only the brows, the mouth line and a small shift of the dots can change.
OUTPUT: 1:1 square; head and shoulders only; plain warm off-white background (#F5F0E6); soft contact shadow; one image.
```

E04 noticing:
```
Image 2 is the head turnaround; use it for the face only.
CHANGE only: the expression (E04, noticing): both brows raised, mouth a small round "o" drawn with a thin line, not an open mouth with teeth. Only the brows, the mouth line and a small shift of the dots can change.
OUTPUT: 1:1 square; head and shoulders only; plain warm off-white background (#F5F0E6); soft contact shadow; one image.
```

E05 hmm:
```
Image 2 is the head turnaround; use it for the face only.
CHANGE only: the expression (E05, unsure): brows angled slightly inward and down, mouth a short wavy line. Only the brows, the mouth line and a small shift of the dots can change.
OUTPUT: 1:1 square; head and shoulders only; plain warm off-white background (#F5F0E6); soft contact shadow; one image.
```

E06 correcting:
```
Image 2 is the head turnaround; use it for the face only.
CHANGE only: the expression (E06, correcting): inner brow ends raised, head tilted about 5 degrees, mouth flat. Only the brows, the mouth line, the head tilt and a small shift of the dots can change.
OUTPUT: 1:1 square; head and shoulders only; plain warm off-white background (#F5F0E6); soft contact shadow; one image.
```

E07 explaining:
```
Image 2 is the head turnaround; use it for the face only.
CHANGE only: the expression (E07, explaining): brows level, mouth a thin open ellipse line, drawn as a line, with no teeth and no tongue. Only the brows, the mouth line and a small shift of the dots can change.
OUTPUT: 1:1 square; head and shoulders only; plain warm off-white background (#F5F0E6); soft contact shadow; one image.
```

E08 deadpan:
```
Image 2 is the head turnaround; use it for the face only.
CHANGE only: the expression (E08, deadpan): brows level and low, a flat upper-lid line over each dot, mouth flat. Only the brows, the mouth line and a small shift of the dots can change.
OUTPUT: 1:1 square; head and shoulders only; plain warm off-white background (#F5F0E6); soft contact shadow; one image.
```

E09 soft smile:
```
Image 2 is the head turnaround; use it for the face only.
CHANGE only: the expression (E09, soft smile): the dots become short upward arcs, mouth a gentle curve. This is the one allowed change to the dot shape. No teeth, no blush.
OUTPUT: 1:1 square; head and shoulders only; plain warm off-white background (#F5F0E6); soft contact shadow; one image.
```

E10 calm nod:
```
Image 2 is the head turnaround; use it for the face only.
CHANGE only: the expression (E10, calm nod): head tilted down 5 to 10 degrees, the dots stay round, a slight mouth curve. Only the brows, the mouth line, the head tilt and a small shift of the dots can change.
OUTPUT: 1:1 square; head and shoulders only; plain warm off-white background (#F5F0E6); soft contact shadow; one image.
```

### 4.4 Poses (R08 sheets and the key single poses)

Pose rules from the bible (5.6): no pose holds an object, because the character has no hands; objects sit beside it or are drawn in the diagram. Arrows are added later in the diagram, never in the picture. Forbidden: extreme low or high angles, wide-angle distortion, any glamour or body-emphasis framing. P01 to P05 are already R01 to R05, and P12 is covered by R11. Camera is eye level (A1). The pose names are the bible's.

**R08a: pose sheet P01 to P06.** Attach: R01. Save as `R08_poses-P01-P06_v1`.

```
CHANGE only: the pose, shown as six poses of the same figure on one sheet, same scale, evenly spaced in two rows of three, no labels, no text, full body, neutral face. Top row left to right:
1. Front standing, neutral, arms relaxed.
2. Three-quarter view facing the viewer's left, standing, arms relaxed.
3. Three-quarter view facing the viewer's right, standing, arms relaxed.
Bottom row left to right:
4. Side profile, standing, arms relaxed.
5. Back view, standing, arms relaxed.
6. Pointing with the right arm (mitten end) toward the viewer's left, the other arm relaxed. Nothing is held and no arrow is drawn.
Every arm ends in a smooth mitten-shaped paddle with no fingers, no thumbs and no hands, in every pose.
OUTPUT: 3:2 landscape; plain warm off-white background (#F5F0E6); soft contact shadows; full bodies in frame; one image.
```

**R08b: pose sheet P07 to P12.** Attach: R01. Save as `R08_poses-P07-P12_v1`. P12 needs a plain door; if the sheet fails, drop P12 (R11 covers it).

```
CHANGE only: the pose, shown as six poses of the same figure on one sheet, same scale, evenly spaced in two rows of three, no labels, no text, full body, neutral face. Top row left to right:
7. Pointing upward with one arm (mitten end), the other arm relaxed.
8. Both arms held out to the sides in a shrug, the arm ends smooth mitten paddles with no palms.
9. Seated on a plain putty-coloured (#CFC6B4) box stool, upright, arms resting on the thighs.
Bottom row left to right:
10. Walking, caught mid-step, arms swinging gently.
11. Leaning forward about 15 degrees toward an empty space at the viewer's left, as if inspecting something just outside the picture.
12. Standing beside a plain flat putty-coloured (#CFC6B4) door in a simple frame, no signs, no numbers.
Nothing is held in any pose. Every arm ends in a smooth mitten-shaped paddle with no fingers, no thumbs and no hands, in every pose.
OUTPUT: 3:2 landscape; plain warm off-white background (#F5F0E6); soft contact shadows; full bodies in frame; one image.
```

**Single key poses.** Attach: R01. Send the Character Lock, then one block. Save as `POSE_P06_point-left_v1` and so on.

P06 pointing (the main callout pose):
```
CHANGE only: the pose. The character points with the right arm (mitten end) toward the viewer's left, the other arm relaxed, standing, front-facing, neutral face. Nothing is held and no arrow is drawn. The arm ends in a smooth mitten-shaped paddle with no fingers, no thumbs and no hand.
OUTPUT: 4:5 portrait; the character alone on a plain warm off-white background (#F5F0E6); soft contact shadow; full body in frame with clear space around it so it can be cut out; one image.
```

P07 pointing upward:
```
CHANGE only: the pose. The character points upward with one arm (mitten end), the other arm relaxed, standing, front-facing, neutral face. Nothing is held. The arm ends in a smooth mitten-shaped paddle with no fingers, no thumbs and no hand.
OUTPUT: 4:5 portrait; the character alone on a plain warm off-white background (#F5F0E6); soft contact shadow; full body in frame with clear space around it so it can be cut out; one image.
```

P08 shrug:
```
CHANGE only: the pose. Both arms held out a little to the sides in a shrug, front-facing, neutral face. The arm ends are smooth mitten-shaped paddles with no palms, no fingers, no thumbs and no hands.
OUTPUT: 4:5 portrait; the character alone on a plain warm off-white background (#F5F0E6); soft contact shadow; full body in frame with clear space around it so it can be cut out; one image.
```

P09 seated:
```
CHANGE only: the pose. The character sits upright on a plain putty-coloured (#CFC6B4) box stool with no back, in three-quarter view, arms resting on the thighs, neutral face. Nothing else in the picture.
OUTPUT: 4:5 portrait; the character and stool alone on a plain warm off-white background (#F5F0E6); soft contact shadow; whole figure and stool in frame with clear space around them; one image.
```

P10 walking:
```
CHANGE only: the pose. The character walks, caught mid-step, in three-quarter view facing the viewer's right, arms swinging gently, neutral face, upright posture.
OUTPUT: 4:5 portrait; the character alone on a plain warm off-white background (#F5F0E6); soft contact shadow; full body in frame with clear space around it so it can be cut out; one image.
```

P11 leaning toward a diagram:
```
CHANGE only: the pose. The character leans forward about 15 degrees toward an empty space at the viewer's left, as if inspecting something just outside the picture, in three-quarter view, arms relaxed, neutral face. Nothing is held and nothing else is in the picture.
OUTPUT: 4:5 portrait; the character alone on a plain warm off-white background (#F5F0E6); soft contact shadow; full body in frame with clear space around it so it can be cut out; one image.
```

---

## 5. Pass/fail checklist

Run this on **every** image, kept or not, at the size shown in each row. Any single failure in rows 1 to 8 rejects the image (bible 5.7). Copy the table into your notes once per image you take seriously and tick the boxes. Mark the failure code in the last column.

**Fail codes:** **R** = regenerate (press again, nothing else changes). **P** = edit the prompt (add the matching fix phrase from section 9 to the end, then make 4 more). **E** = fix in an image editor (small, local; log it as a human edit, keep the untouched original). **X** = stop and tell Claude (design problem or a test failed; never "fix" by editing).

### 5.1 The checklist

| # | Check | How to check | Pass | If it fails |
|---|---|---|---|---|
| 1 | Head | A rounded cube with softly rounded corners, matte oat. No stud, peg, dome or cylinder. Same corner softness as R01 | [ ] | R once; P if 2 of 4 |
| 2 | Face | Two small round matte charcoal dot eyes set wide, no highlight. Two thin brow bars. One thin mouth line. No nose, ears, eyelashes, blush, teeth, tongue | [ ] | R once; P if 2 of 4 |
| 3 | Hair | A short flat walnut slab with a side parting, sitting like a cap. Not a ponytail, long hair or hat | [ ] | R / P |
| 4 | Body | About 7 head-heights, slim, upright. Stacked rounded blocks with hairline seams in the same places as R01 | [ ] | R / P |
| 5 | Arms and feet | Arms end in smooth mitten paddles. **No fingers, no thumbs, no hands.** Simple flat shoes, no logo. Zoom to 200 percent and look at both arm ends | [ ] | R once; P if 2 of 4 (never E) |
| 6 | Material | Matte hand-sculpted clay, faint thumbprint texture, no gloss or plastic sheen | [ ] | P |
| 7 | Belt | Cream tape-measure strip with fine charcoal ticks, **no numerals**, small walnut buckle | [ ] | R; E if only numerals are stray |
| 8 | Outfit | O1, O2, O3 or an approved seasonal variant. No logos, text, uniform, tradesperson kit (hard hat, high-visibility vest, overalls, lab coat, apron), school uniform, hood over the face. Not all black or all white | [ ] | P |
| 9 | Adult-read at thumbnail | Shrink the full figure to about 110 pixels tall (about 3 cm on a laptop screen, or zoom the browser out). Still reads as an adult-proportioned figure, not a toy. Head about one seventh of the height and **fail if it is larger than one sixth**. Long slender limbs; no stubby limbs; no big glossy eyes, blush or sparkle; upright posture; no pastel candy colours; no body shaping or glamour framing. For head-only pictures (R06, R07, R14, single expressions) the proportion part cannot be judged, so check the face items instead: brows present, thin mouth line, no blush, no glossy or big eyes, no sparkle, no tears; the age-guess test (section 6.1) uses full-body views only | [ ] | P (smaller head, longer limbs); X if it still reads as a toy |
| 10 | Hands and fingers, anywhere | No hand-like shape on the character, on objects or elsewhere. No extra people | [ ] | R / P |
| 11 | Text (garbled or Simplified Chinese included) | **No text at all**: no letters, numerals, labels, signs, watermarks, nothing on the tape. Any text, in any script, fails the image, even if it looks correct, because all text is added later in a design tool. If Chinese characters do appear, ask the wife whether they are garbled or Simplified and note it in the log; that tells us how this tool behaves | [ ] | R; E if one small mark |
| 12 | Party-colour read | At thumbnail size nothing reads as a blue, green, teal or yellow camp. Sage is only a small accent, about 12 percent of the figure or less (bible assumption). No blue-and-red or green-and-white pairing. The wife confirms | [ ] | P (colour phrase); wife decides |
| 13 | Resemblance | Do you or the wife instantly think of a real person or an existing character, mascot, toy or game avatar? Quick look now; the real tests are in section 6 | [ ] | X |
| 14 | Medium and palette | Looks like a clay maquette, not a flat vector or a plastic toy render. Sample the colours with a colour picker (section 5.3): within range, or fix in post and note it | [ ] | P if wrong family; E if near |
| 15 | No brand, logo or plate | No brand marks on clothing, shoes, props or background; no number plate; nothing readable | [ ] | R / P |
| 16 | Background and framing | Plain warm off-white, soft contact shadow, full body in frame with space around it, eye-level, no wide-angle distortion. On a sheet: every view is clearly the same character at the same scale | [ ] | R / P |
| 17 | Match to R01 | Put it beside R01 at the same size. Any locked feature differs, it is rejected. Two failures in a row: new chat, attach only R01 | [ ] | R, then re-anchor |
| 18 | Taiwan details (R11, R15 only) | Wife checks the room details listed in section 8, item 8 | [ ] | P; wife decides |
| 19 | Saved and logged | File is in the right folder with the pack name; row added to the log with tool, model label, prompt, time, licence notes | [ ] | Do it now |

### 5.2 Regenerate, edit the prompt, edit the picture, or stop?

| Situation | Do this |
|---|---|
| One of the four has the defect and the others do not | **R**: it is random. Choose another |
| The same defect appears in 2 or more of 4 | **P**: the prompt is not stopping it. Add the matching fix phrase from section 9 at the end and generate 4 more |
| Otherwise perfect image, one tiny local flaw (stray mark, a few numerals on the tape, slight colour cast) | **E**: fix in an image editor. Never use E for fingers, face shape or proportions. Log it as a human edit and keep the untouched file as the parent |
| The same defect after two rounds (8 images) in one tool | Try the other tool with the same prompt. If both fail, **X** |
| The thumbnail reads as a toy, the age guess fails, or a look-alike is named | **X**: stop and tell Claude; do not repair it with edits |

### 5.3 Colour check: hex, RGB, and an allowed range

The bible says hex values in prompts are hints that image models follow loosely, and that colour is checked with a colour picker and corrected in post. Sample a **flat, evenly lit patch** (not an edge, not a shadow; shaded clay is naturally darker) with any eyedropper tool and read the red, green and blue numbers. The "OK range" is **my suggestion, not a bible rule** (assumption, to calibrate after the first session): within 12 on each of red, green and blue. I computed (CIE76, the scale in `personas/README.md` section 5) that moving all three channels together by 12 (a lighter or darker version of the same colour) shifts these palette colours by about 4 to 5 (the "close" band), but moving the channels in different directions by 12 each (a colour tint, such as a yellower oat) can shift them by about 15 to 19, which is "clearly different". So the range only screens out big errors: inside range, **and** it still looks like the same colour as the palette card or the hex swatch beside it by eye: pass. Off by 13 to about 25 on any channel: fix the colour in post and note it in the log. Off by more than that, or visibly a different colour (a yellow oat, an orange walnut, a vivid green sage): regenerate or edit the prompt.

| Used for | Colour | Hex | R, G, B | OK range red | OK range green | OK range blue |
|---|---|---|---|---|---|---|
| Body and head (dominant) | Oat 燕麥 | `#E4D9C3` | 228, 217, 195 | 216 to 240 | 205 to 229 | 183 to 207 |
| Hair, trousers, shoes, buckle | Walnut 胡桃 | `#6E5440` | 110, 84, 64 | 98 to 122 | 72 to 96 | 52 to 76 |
| Vest, scarf accent (small) | Sage 灰綠 | `#A9B5A0` | 169, 181, 160 | 157 to 181 | 169 to 193 | 148 to 172 |
| Background | Warm off-white 米白 | `#F5F0E6` | 245, 240, 230 | 233 to 255 | 228 to 252 | 218 to 242 |
| Eyes, brows, mouth, ticks | Charcoal 炭灰 | `#3B3631` | 59, 54, 49 | 47 to 71 | 42 to 66 | 37 to 61 |
| Tape-measure belt | Cream 奶油 | `#EFE6CF` | 239, 230, 207 | 227 to 251 | 218 to 242 | 195 to 219 |
| O2 pullover only | Deep walnut 深胡桃 | `#5C4636` | 92, 70, 54 | 80 to 104 | 58 to 82 | 42 to 66 |
| O3 rain shell, door | Putty 灰米 | `#CFC6B4` | 207, 198, 180 | 195 to 219 | 186 to 210 | 168 to 192 |
| Diagram fill, scene only | Sage tint | `#D6DCCF` | 214, 220, 207 | 202 to 226 | 208 to 232 | 195 to 219 |
| Diagram fill, bed frame in R11 | Walnut tint | `#BBA48F` | 187, 164, 143 | 175 to 199 | 152 to 176 | 131 to 155 |

The eyes, brows, mouth line and tick marks are too small to sample reliably: just check by eye that they are a dark warm grey, not pure black. When the palette card R12 exists, hold the picture beside it and compare by eye as well.

---

## 6. The two human tests, and the reverse-image search

The bible requires both tests on the shortlist before the master is chosen for good (bible 4.8, 5.8 step 2, 5.10). They need other people, so they usually happen on a different day from the generating. The people are helping you test a design; they do not follow, like or comment on any account, and they should not share the pictures. Tell them afterwards what the pictures were for.

### 6.1 Age-guess test (adult-reading check)

1. For each shortlisted sheet (up to three), crop out the front full-body view as its own picture. Save the crop as a separate file in `candidates`, for example `R01_cand_gemini_2_front-crop`, and log it as a human edit (crop) of its parent. Show people a copy with no file name visible. Also make a thumbnail copy at about 110 pixels tall.
2. Find the wife plus 3 to 5 acquaintances (4 to 6 people in all). Show each person the pictures **one at a time, in a different random order for each person, with no context**: do not say it is an AI character, a mascot or a character for a social-media account.
3. Ask only: **"How old is this character?"** Write the number they say, exactly. If they refuse to guess, ask for a rough range and write that.
4. Do the same with the thumbnail copy.
5. **Fail** if more than one of the people guesses under 25 (a bible assumption, to be calibrated). A fail goes in the log; the image is not used.
6. Record answers in the language they were given; the wife adds an English gloss.

### 6.2 Look-alike blind test

1. Same people and same set-up as 6.1, shown the same way.
2. Ask only: **"What or who does this remind you of?"** Write the answer word for word.
3. **Fail** if two people independently name the same existing character, brand or person, or if anyone names a real person (bible threshold, an assumption).
4. A fail goes in the log. The image is not used. Do not try to "fix" a look-alike by editing; tell Claude.

### 6.3 Reverse-image search (manual, public tools only)

Do this for each shortlisted image, on your own computer, by hand.

1. Make a clean copy of the front view only (crop out the other views; no border, no text).
2. Use **at least two** public reverse-image search tools. Examples, whichever are currently available: the "search by image" function of a large web search engine, Google Lens, TinEye, Bing visual search. Open the tool's web page and upload the picture yourself. Do not use scripts, bots or scraping, and do not log in anywhere you would not normally log in; no scraping behind logins (Ground rule 9). Uploading sends the picture to that service, which is acceptable for a pre-launch design but worth noting in your log.
3. Look at the first one or two pages of visual matches. Write down anything that is a close match: a character, mascot, toy, game avatar, sticker character or logo. Screenshot the result pages into `assets/fangcun/lookalike/` with names like `R01_cand_gemini_2_tineye_2026-10-11.png`.
4. Then run **text** searches on these generic terms in the same tools' image results: "clay block character", "stacked block mascot", "brick figure", "voxel character", "clay mascot". Compare what you see with your image by eye.
5. Names to keep in mind while comparing. **These are for searching and comparing only. Never paste any of them into an image prompt, and never upload anything of theirs:** toy-brick figures (LEGO), voxel and block games (Minecraft, Roblox avatars), toy and character-goods mascots (Sanrio and similar), clay-animation characters, LINE sticker characters (LINE Friends), Doraemon and other well-known anime or cartoon figures, well-known VTubers, and Taiwan mascots (for example OPEN將 and other convenience-store and city mascots).
6. Record tool and date for each search. Ask the wife about anything you do not recognise (section 8, item 4).
7. If a very close match turns up: do not use the image; tell Claude.

### 6.4 The log to keep (the bible's table, ready to fill)

| Date | Candidate / asset | Tools and searches | Search result | Blind-test result | Age guesses | Verdict | Checked by |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Age-guess tally (one row per person; "under 25?" is yes if their guess is below 25):

| Person (initials) | Full-size guess | Thumbnail guess | Under 25? | "Reminds me of" (verbatim) |
|---|---|---|---|---|
| Wife | | | | |
| | | | | |

---

## 7. Provenance: log every asset

The rule (Ground rule 2, bible 5.8 and 5.11): **every kept file and every discarded-but-considered file gets one row in `assets/provenance.csv`, the same day.** "Considered" means you saved it, compared it, shortlisted it or used it as a reference. Obvious failures you did not save need no row, but save anything you looked at for more than a glance. Human-made files (palette card, crops, edited versions) get rows too, with tool "human-made" and the app name. Edited versions are separate files with their own rows, naming the parent file.

### 7.1 Columns and a ready-to-fill example

Columns, in order: `timestamp,asset_path,persona,tool,model,prompt,licence_notes`.

- `timestamp`: Taiwan time (+08:00), the time you generated the image.
- `asset_path`: path from the project folder, for example `assets/fangcun/R01_master_v1.png`.
- `persona`: `fangcun` until the real handle is chosen.
- `tool`: for example "Gemini (app)" or "ChatGPT (app)". Write what you actually used.
- `model`: the model or version label **exactly as the app shows it that day**. If the app shows none, write "not shown in app, YYYY-MM-DD". Do not guess one.
- `prompt`: the **full text you sent**, including the Character Lock if you used it, and a note of which files were attached. If you changed even one word, log the changed text.
- `licence_notes`: use the template in 7.3.

This is an **example only**. Copy only the second line into the real file, and only after replacing every `<...>` with the real value. The header line is already in the file.

```
timestamp,asset_path,persona,tool,model,prompt,licence_notes
2026-10-11T14:05:00+08:00,assets/fangcun/R01_master_v1.png,fangcun,"Gemini (app)","<model label exactly as shown in the app today>","<PASTE THE FULL PROMPT EXACTLY AS SENT. Attached files: none.>","Status: KEPT (provisional master); reason: best of 4, passed checklist; parent file: none (raw download); reference images attached: none; human edits: none (raw); prompt ID: R01-Gemini; tool plan: <plan name shown in my account>; terms read on <YYYY-MM-DD, or: not yet read> at <page name or link, or: none>; commercial use per those terms: NOT CONFIRMED (change only after reading the terms); watermark or label on file: <none seen | describe>; conversation link or ID: <link>; seed: none shown"
```

### 7.2 Rules that keep the file valid

- One row per file. A kept file and the candidates around it each get their own row.
- The easiest way to avoid broken quotes: edit the CSV in a spreadsheet app and paste each field into its own cell; the app adds the quotes and handles commas, line breaks and double quotes. If you edit it as plain text, put every field that contains a comma, a line break or a quote in double quotes, and double every quote mark inside it. Save as CSV (UTF-8 if offered).
- A long prompt in one cell is fine. For a batch of images made from the same prompt, copy the prompt cell down.
- Do not edit or delete old rows. Corrections go in a new row.
- You can also paste your notes (file names, tool, model label, time, which prompt, any wording you changed) to Claude Code and ask it to write the rows. Claude cannot see your screen, so it needs the model label and the time from you, and it must use the exact text you sent.

### 7.3 `licence_notes` template (fill the blanks)

```
Status: ___ (KEPT | KEPT (provisional master) | DISCARDED-CONSIDERED); reason: ___; parent file: ___ (none (raw download) | file name); reference images attached: ___ (none | R01_master_v1.png ...); human edits: ___ (none (raw) | crop | colour fix | numerals erased | other); prompt ID: ___ (for example R02); tool plan: ___ (the plan name shown in my account); terms read on ___ (date) at ___ (page name or link); commercial use per those terms: ___ (CONFIRMED | NOT CONFIRMED | RESTRICTED: what); watermark or label on file: ___ (none seen | describe); conversation link or ID: ___; seed: ___ (none shown | number)
```

Before any commercial use, read the **current** terms for the tool and plan used, for example the terms of service and any content or image policy the app links to, and fill in the "terms read" and "commercial use" blanks from what they actually say. Terms can differ between tools, between plans, and between the app and a developer interface; they change. Whether AI-generated images can be protected by copyright is an open question for the lawyer (`research/legal.md` section 8.2), and hand-finishing the master, with the layered file kept, is how the studio documents its own human contribution.

---

## 8. A note for the wife

Thank you for looking at these. You are judging **language and culture and how it feels**, not the technology. The operator checks hands, proportions and numbers. For each picture, please say **APPROVE**, **SMALL FIX** or **REJECT**, and give a short reason. Reason codes (from the bible, 10.1): **X** cultural or visual error, **S** script or font problem, **P** politics or sensitive colour, **H** hands, people or other AI defect, **T** tone. If you are not sure, say "unsure" and say why. About 15 minutes for a shortlist of three is my estimate. The zh-TW terms are an AI draft; correct them freely.

| # | Look at | zh-TW words to look for | Your answer |
|---|---|---|---|
| 1 | Does it look like a **grown-up**? The risk is that a block body with dot eyes looks like a toy or a child. | 成熟、穩重 (good) / 幼稚、像玩具、像小孩、太可愛、童趣 (not good) | |
| 2 | Is it **gender-neutral**? Not clearly male or female. | 中性、看不出明顯性別 (good) / 偏男、偏女 (not good) | |
| 3 | Does it feel **friendly and trustworthy**, or strange? The dot eyes can look empty. | 親切、可信 (good) / 詭異、空洞、不舒服 (not good) | |
| 4 | Does it **remind you of anything that already exists**? Write the name. | 像不像某個吉祥物、卡通角色、公仔、玩具、積木、遊戲角色？像什麼？ | |
| 5 | **Colour impression** at small size. Does it give any political or camp impression? Any all-black or all-white look? | 有沒有藍、綠、白的政黨色聯想？全黑、全白 (喪事色) | |
| 6 | **Any writing at all** on the picture. There should be none. | 文字、數字、簡體字、亂碼、日文或港式字形 | |
| 7 | **Taboo objects**. There should be none. | 神明桌、香、紙錢、白菊花、數字 4 | |
| 8 | **Taiwan room details** (only for R11 door and bed and R15 floor plan). | 磁磚地板、鋁門窗和鐵窗、分離式冷氣、玄關鞋櫃 (進門脫鞋)、後陽台洗衣機和曬衣桿、電鍋、扁形插座 | |
| 9 | **Logos or brand marks** on clothes, shoes or objects. | 商標、品牌標誌、車牌 | |

Not needed from you: numbers, measurements, whether it is "good AI", the name 方寸 (that is a separate reading test, bible gate G2).

---

## 9. Common failure modes for this character, and fixes

These come from the bible's spec, Avoid list, adult-reading check and review notes. The top risk named in the bible's review is the **cube head with dot eyes and no hands**: it can read as a toy or a child, and it can look like the block-figure characters of games. Only the age-guess and blind tests (section 6) clear that. To use a fix phrase: add it at the end of the prompt (after the Character Lock and the prompt), regenerate 4, and see whether 3 or more now pass (rule in 5.2). In the same chat you can instead say "Same image, but: <phrase>" for a small fix.

| Symptom | Likely cause (hypothesis) | Fix phrase |
|---|---|---|
| Toy-brick look: studs on top, pegs, connectors, pixel or voxel cubes | "Stacked blocks" pulls the generator toward brick toys | `The blocks are smooth hand-sculpted clay with softly rounded corners and thin hairline seams; no studs, no pegs, no interlocking connectors, not toy bricks, not pixelated.` |
| Child-like or chibi: big head, short limbs | Cute-character default | `Make the head smaller: the figure is about seven head-heights tall with long slender limbs and a small head relative to the body; an adult in their early thirties; not chibi, no child-like proportions.` |
| Fingers or a hand appear, often when pointing | Generators love hands | `The arms end in smooth rounded mitten-shaped paddles: no fingers, no thumbs, no hands, no knuckles.` |
| Glossy plastic or vinyl finish | Toy-render default | `Matte hand-sculpted clay with a faint thumbprint texture; no gloss, no plastic sheen, no highlights.` |
| Numbers or lines of text on the tape measure, or labels on a sheet | Tape measures "should" have numbers | `The tape-measure belt has fine charcoal tick marks only: no numbers, no letters. No text anywhere in the picture.` |
| Face extras: nose, ears, eyelashes, blush, shiny eyes, sparkles | Cute-face defaults | `The face has only two small round matte charcoal dot eyes, two thin brow bars and one thin mouth line: no nose, no ears, no eyelashes, no blush, no teeth, no highlights in the eyes.` |
| Expression mouths turn into lips, teeth or a tongue (E04 "o", E07 ellipse) | Open mouths are drawn realistically | `The mouth is only a thin drawn line or a small round line; no lips, no teeth, no tongue.` |
| Side profile grows a nose or an ear | Profiles imply them | `In profile the head stays a rounded cube: no nose, no ear.` |
| Seams vanish, or the body turns into jointed robot parts | Smoothing, or over-detailing | `Show shallow hairline seams between the stacked blocks, in the same places as the reference; no robot joints, no mechanical parts.` |
| Colours drift: yellow oat, orange walnut, vivid green sage, cold grey | Hex values are only hints | `Use only the muted palette: oat (#E4D9C3) head and body, walnut (#6E5440) hair, trousers and shoes, sage (#A9B5A0) only as a small accent on the vest, cream (#EFE6CF) belt, on a warm off-white (#F5F0E6) background; no saturated blue, green, teal or yellow.` |
| Costume drift: apron, hard hat, high-visibility vest, uniform, hood over the face, all-black or all-white outfit | "Helper" or "worker" association | `Plain knitwear and simple layers only: no uniform, no apron, no hard hat, no high-visibility vest, no logos or text on clothing, hood down.` |
| Gendered or sexualised shaping: waist, hip or chest shaping | Body-shape defaults | `Gender-neutral straight block body: no waist, hip or chest shaping.` |
| Background grey, white, black, a gradient, or a room appears | Not told strongly enough | `Plain warm off-white background (#F5F0E6), no gradient, no pure white, no pure black, nothing else in the picture.` |
| Sheet views do not match, or are cropped, or extra figures appear | Many views in one image is hard | Generate each view as its own image (R02 to R05) with R01 attached. Add: `All views show exactly the same single character at the same scale. Eye-level camera, no perspective distortion.` |
| Four-view sheet comes back as a single large figure | Prompt read loosely | `This is a character reference sheet showing four full-body views of the same figure side by side.` |
| Seasonal pictures bring in snow, maple leaves or a puffer coat | Four-season defaults | `Taiwan climate: no snow, no maple leaves, no puffer coat. Knit layers only.` |
| Door or bed pictures (R11) get perspective, extra furniture or text | Scene defaults | `Orthographic eye-level view, no wide-angle distortion. Only the door, the single bed and the character. No signs, no numbers, no pattern, no print.` |
| Room (R15) shows carpet, kitchen island, dishwasher, clothes dryer, fireplace, UK or EU sockets, blue glass windows | Western defaults | Add the bible's own line: `No carpet, kitchen island, dishwasher, clothes dryer or fireplace. No blue, teal, bright green or yellow. Windows are pale oat-grey outlines.` The wife checks the rest. |
| Character drifts further from R01 with each new picture | Building on the last output | New chat, attach only R01, resend. Never use a new output as the only reference twice in a row. |
| The long Avoid list makes the app draw the things it names | Naming a thing can summon it (hypothesis) | Use the short fallback below instead of the long list. |
| Thumbnail still reads as a toy, or an age guess fails | The design itself, not a prompt problem | Tell Claude. Do not edit around it. |

**Short Avoid fallback (only if the long list backfires).** Every item is taken from the bible's Avoid list.

```
Avoid: hands, fingers, thumbs; toy-brick studs, pegs or interlocking connectors; large glossy eyes, sparkles, eyelashes, blush, tears; chibi, baby or child-like proportions, oversized head; glossy plastic finish; text, letters, numerals, logos, watermark; other people.
```

---

## 10. When you stop for the day

Tell Claude: which tool made the chosen R01 and the model label shown; which images you kept and discarded; the minutes you spent; which checklist rows failed most often; and what the wife said. Claude can then update the bible's status table (5.9), record the tool test in `pipeline/tools.md`, and set up the next sitting. Nothing from this pack is approved until the age-guess test, the look-alike blind test, the hand-finishing and the approvals by the wife and operator are done. The name 方寸, the studio name and the handle are still unchecked and are not part of this session.
