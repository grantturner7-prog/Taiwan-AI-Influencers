# 色環 (sehuan) image pack: first reference images

**Pack v1, written 2026-10-11.** For the operator (English only) and the wife (language and culture review). Source of truth: `personas/sehuan/bible.md`, sections 4 and 5, plus its Review log and Phase 3 integration log, which override earlier text (that is why the background colour is pale blush `#F2DAD2` and not cream). If this pack and the bible ever disagree, the bible wins; tell Claude and the pack gets fixed.

**Status of everything you make with this pack: working references, not approved assets.** Nothing is cleared for public use until the master has been hand-finished, both human tests in section 6 are passed, and the wife and operator approve it (bible gate G4). Nothing has been generated yet; no reference image exists. The name 色環, its handle and the studio name are also still unchecked and are not part of this session.

**How to use it:** read sections 0 and 1, then do sections 2 and 3 in order. Keep section 5 (checklist) and section 7 (log) open while you work. Copy the contents of each code box exactly as written. Model names, buttons and features in Gemini and ChatGPT change often, so every statement about them below is a hypothesis: check the current screen. The few places where this pack adds wording that is not in the bible are listed in 3.2, so you can always tell bible from pack.

---

## 0. One-screen summary

**Who.** 色環 (the word means "colour wheel"; how to say it is the wife's call, so do not worry about pronouncing it) is an AI character for a studio's Instagram and Threads accounts. She is a calm adult woman-presenting character with a design age of 30 who explains colour and outfit logic to Taiwan audiences: which colours go together, and how to layer for Taiwan's damp-cold, rainy and hot-humid weather. She is drawn as a fashion illustration, not a photo: flat blocks of muted colour with a loose, hand-drawn-looking brush outline. You can recognise her by three things. First, a round drop earring drawn as a colour wheel of twelve muted segments. Second, shoulder-length dark hair tucked behind one ear so that earring shows. Third, one small accent of persimmon (a soft terracotta orange) in every outfit, such as a neckerchief, never more than about a tenth of the picture. Her default outfit is a relaxed stone-grey blazer worn open over a cream knit top, charcoal trousers and flat loafers, with a ring of six blank colour-chip cards clipped to her belt loop. She is openly an AI character from the studio. She has never worn, bought or tested anything, so in lessons she stands beside the outfit being taught and never wears it, and her pictures are always labelled illustrations.

**Goal of the first session.**
1. Pick one master picture (R01, a character sheet with five views) that passes the checklist.
2. Use it to make the face sheet (R02) and the ten-face expression sheet (R03).
3. Log every file the same day. If energy is left, start the outfit sheets (R05). The tests with other people, hand-finishing and the rest of the set come after.

**Time (my estimate, not measured).** About 3 hours hands-on for R01 to R03, best split into two sittings. About 15 to 20 minutes of the wife's time on the shortlist. About an hour on another day for the tests with other people. Another 3 to 4 hours for the next sitting (outfits, seasons, poses, props, library). Write down your real minutes; the studio's capacity plan needs them.

**Order of work.**

| Step | What | Where in this pack |
|---|---|---|
| 1 | Make the folders and open the log (5 min) | Section 1 |
| 2 | R01 prompt in Gemini (4 images) and in ChatGPT (4 images) | Section 2 |
| 3 | Throw out obvious failures, run the checklist on the rest, shortlist at most 3 | Sections 2.5, 5 |
| 4 | Wife looks at the shortlist without knowing which tool made which; you run the reverse-image search | Sections 8, 6.3 |
| 5 | Choose a provisional master and save it as `R01_master_v1` | Section 2.5 |
| 6 | R02 face sheet, then R03 expression sheet, always with R01 attached | Sections 3, 4 |
| 7 | Log as you go, not at the end | Section 7 |
| 8 | Another day: age-guess test and look-alike blind test, outfits (R05), seasons (R06), poses (R04), props (R07), library (R10, R11, R13), then hand-finish and freeze the set (with Claude, Phase 4) | Sections 6, 3, 4 |

---

## 1. Before you start

- **Tool: start with Gemini, then run the same prompt in ChatGPT (a hypothesis, not a finding).** The bible's Gemini recipe is the plainer workflow (attach the reference picture, ask for one change), which makes it the easier first tool for a non-technical operator. The bible's ChatGPT recipe is more structured and mentions a local-edit mode (if the app has one), which may matter later for fixing a wrong earring without redrawing the whole picture. Nobody has tested either tool on this character; today finds out. Once R01 is chosen, stay in the tool that made it for the follow-up images (hypothesis: one tool keeps the set consistent). You can upload the chosen R01 into the other tool later.
- **Settings to look for, only if the current app offers them.** Image shape or aspect ratio (wide landscape for sheets, 4:5 portrait for single figures, 1:1 for the avatar; if there is no setting, the OUTPUT line in each prompt asks for it). Number of images per request (set 4; if not offered, send the prompt again until you have 4 separate images, and do not ask for "a grid of 4 versions"). Highest quality or resolution. A model or version picker (pick one, keep it for the whole sitting, copy its label exactly). Style presets or filters (leave off, so only the prompt sets the look). Chat history (if the app has a temporary or private chat mode, do not use it: you need the conversation link for the log). Download the largest version the app offers; a screenshot is the last resort and must be noted in the log.
- **Never upload a photo of a real person, or a picture of any existing character, at any point, including "just to copy the pose" or the look.** That includes fashion photos, models, "outfit inspiration" and screenshots of other virtual influencers. The only pictures you may upload are ones made with this pack (your own R01 and the images made from it). Describe poses and clothes in words, as the prompts do. Never type the name of a living artist, a studio, a brand or an existing character into a prompt.
- **Save everything and log everything.** Download every image you look at for more than a glance, straight into `assets/sehuan/` (or its `candidates` folder) with the file name from this pack. Do not edit or rename-over the original download. Delete nothing today. Do not strip any watermark, label or metadata the tool adds; note it in the log (bible 5.7 step 13). Add a row to `assets/provenance.csv` the same day for every kept file and every discarded-but-considered file (section 7).
- **Licence terms have not been checked.** This pack does not know what Gemini or ChatGPT allow for commercial use on your plan. Before any commercial use, read the current terms for the exact tool and plan you used, and record what you found and the date in `licence_notes` on every row. Until that is done, treat every image as internal design material only.

**Set-up (about 5 minutes).**
1. In the project folder, open `assets/sehuan/` (it exists and is empty apart from a `.gitkeep` placeholder). Inside it make two folders: `candidates` (every image you considered but did not choose) and `lookalike` (screenshots from section 6).
2. Open `assets/provenance.csv` in a spreadsheet app. The header must read `timestamp,asset_path,persona,tool,model,prompt,licence_notes`. Do not change it.
3. Copy the Character Lock (section 4.1) into a notes file so you can paste it quickly from Step 2 on.
4. In the same notes file start a line "minutes: " and add your times as you go.

---

## 2. STEP 1: the master reference R01

**What you are making.** One picture that is a character sheet: the same woman shown five times at the same scale and eye-line on a plain pale-blush background: four full-body views in a row (front, three-quarter left, side, back) plus one large head-and-shoulders view. Outfit A, neutral calm expression, hands in the blazer pockets or drawn as simple flat mitten shapes. Shape: wide landscape, if the app offers it (my suggestion; the bible leaves the sheet shape open). Full-body figures on a wide sheet are small, so the faces will be soft; that is expected, and R02 is the face lock.

Both prompts below carry the same design. The body text is the bible's master prompt (5.1) copied unchanged (I only joined its hard line breaks into single lines so it pastes cleanly). The Gemini prompt uses the bible's Gemini first-turn wrapper (5.2). The ChatGPT prompt uses the bible's labelled-block layout (5.3), filled from the same 5.1 text, because 5.3's KEEP IDENTICAL and REFERENCE lines need an image that does not exist yet; those lines appear from Step 2 onward, inside the Character Lock.

**One wording decision for the wife.** The Character paragraph says "ordinary East Asian features that read as Taiwanese". The bible leaves open whether to keep "that read as Taiwanese" in a generator prompt (bible open item 5). Run today's prompts as written. If the wife wants those four words removed, remove them from both prompts and note the changed prompt in the log (the Character Lock in 4.1 does not contain them).

### 2.1 Gemini: paste this

```
I'm designing an original, clearly adult virtual character for a studio. Please generate one reference sheet image using the specification below. After I choose a result, I'll ask for edits. Keep every locked feature identical unless I say otherwise. Do not put any text, letters, numbers or logos anywhere in the image, and do not copy any existing character or any real person.

Style: contemporary fashion illustration made of flat colour fields with a loose ink-brush line. The line weight varies from thin to thick and has small gaps and overshoots, as if drawn quickly with a brush pen. Colour fills are flat and sit very slightly off the line. No gradients, no airbrushing, no soft shadows, no photographic skin or fabric texture, no 3D, no glow. Adult fashion-illustration proportions, about seven and a half heads tall, with natural (not elongated) legs.

Character: a clearly adult woman-presenting character, stated age 30, ordinary East Asian features that read as Taiwanese, not an idol or anime template. Average-to-slim build, natural soft shoulders, relaxed upright posture, no exaggerated waist, bust or hips. Hands hidden in jacket pockets (or drawn as simple flat mitten shapes with a separate thumb).

Face: long-oval face, softly defined cheekbones and jaw shadow, straight dark eyebrows of medium thickness, almond eyes of modest size (each about one fifth of the face width) filled charcoal #3A3735 with one small cream #F4E8DF highlight, brows filled #2F2A28, a nose drawn as one short brush stroke with a small shadow shape, a calm closed mouth in flat muted terracotta-brown #B27A6C with a very slight asymmetric smile. No blush marks, no freckles, no eye makeup, no gloss, no sparkle.

Hair: natural dark brown-black #2F2A28, shoulder-length blunt cut, side parting, tucked behind the left ear so the earring is visible. Flat colour plus one lighter highlight shape.

Skin: flat warm medium tone #DDB38E with one shadow shape #C4946C.

Signature details (always present): (1) round drop earrings shaped like a colour wheel: twelve equal wedge segments in the twelve muted wheel colours #C27F80, #C58479, #CD8B6A, #D2AE72, #CCC07F, #A9B27F, #8DA68C, #7EA3A0, #7C95AA, #8A8DB0, #9F8AAB, #B58AA0 in that order, diameter about one quarter of the face width, no numbers or letters; (2) one persimmon accent #CD8B6A covering about one tenth of the visible clothing: a small knotted neckerchief at the collar; (3) a ring of six blank colour-chip cards in muted tints (#E6BBA3, #E4D6CB, #B8AEA2, #D2AE72, #C27F80, #9F8AAB), clipped to a belt loop, no text on the cards.

Outfit A: relaxed single-breasted blazer in warm stone grey #B8AEA2, worn open, over a cream #F4E8DF fine-knit crew-neck top; charcoal #3A3735 straight wide trousers ending at the ankle; flat charcoal loafers. No logos, no text, no tags, no labels, no patterns.

Layout: plain pale-blush #F2DAD2 background. Four full-body views in a row at identical scale and eye-line (front, three-quarter left, side, back), plus one large head-and-shoulders view. Neutral calm expression. Even flat lighting.

Avoid: text, letters, numerals, logos, monograms, watermarks, signatures, brand patterns, photorealism, 3D render, anime, chibi or kawaii proportions, large glossy eyes, blush, child-like features, school uniform, short skirt, cleavage, swimwear, lingerie, sexualised pose, exaggerated or idealised body, elongated legs, detailed fingers, gradients, airbrush, soft shadow, skin pores, fabric texture, glitter, dyed hair, makeup emphasis, tattoos, saturated blue, saturated green, saturated teal, saturated yellow, rainbow stripes, flags, party colours, red-star symbols, Indigenous patterns, traditional costume, any resemblance to a real person or an existing character.
```

### 2.2 ChatGPT: paste this

```
GOAL: One image: a character reference sheet of an ORIGINAL virtual character for a studio. She is not based on any real person, celebrity, model, influencer, illustrator's character or existing fictional character.
REFERENCE: None. This is the first image; nothing is attached.

Style: contemporary fashion illustration made of flat colour fields with a loose ink-brush line. The line weight varies from thin to thick and has small gaps and overshoots, as if drawn quickly with a brush pen. Colour fills are flat and sit very slightly off the line. No gradients, no airbrushing, no soft shadows, no photographic skin or fabric texture, no 3D, no glow. Adult fashion-illustration proportions, about seven and a half heads tall, with natural (not elongated) legs.

Character: a clearly adult woman-presenting character, stated age 30, ordinary East Asian features that read as Taiwanese, not an idol or anime template. Average-to-slim build, natural soft shoulders, relaxed upright posture, no exaggerated waist, bust or hips. Hands hidden in jacket pockets (or drawn as simple flat mitten shapes with a separate thumb).

Face: long-oval face, softly defined cheekbones and jaw shadow, straight dark eyebrows of medium thickness, almond eyes of modest size (each about one fifth of the face width) filled charcoal #3A3735 with one small cream #F4E8DF highlight, brows filled #2F2A28, a nose drawn as one short brush stroke with a small shadow shape, a calm closed mouth in flat muted terracotta-brown #B27A6C with a very slight asymmetric smile. No blush marks, no freckles, no eye makeup, no gloss, no sparkle.

Hair: natural dark brown-black #2F2A28, shoulder-length blunt cut, side parting, tucked behind the left ear so the earring is visible. Flat colour plus one lighter highlight shape.

Skin: flat warm medium tone #DDB38E with one shadow shape #C4946C.

Signature details (always present): (1) round drop earrings shaped like a colour wheel: twelve equal wedge segments in the twelve muted wheel colours #C27F80, #C58479, #CD8B6A, #D2AE72, #CCC07F, #A9B27F, #8DA68C, #7EA3A0, #7C95AA, #8A8DB0, #9F8AAB, #B58AA0 in that order, diameter about one quarter of the face width, no numbers or letters; (2) one persimmon accent #CD8B6A covering about one tenth of the visible clothing: a small knotted neckerchief at the collar; (3) a ring of six blank colour-chip cards in muted tints (#E6BBA3, #E4D6CB, #B8AEA2, #D2AE72, #C27F80, #9F8AAB), clipped to a belt loop, no text on the cards.

Outfit A: relaxed single-breasted blazer in warm stone grey #B8AEA2, worn open, over a cream #F4E8DF fine-knit crew-neck top; charcoal #3A3735 straight wide trousers ending at the ankle; flat charcoal loafers. No logos, no text, no tags, no labels, no patterns.

Layout: plain pale-blush #F2DAD2 background. Four full-body views in a row at identical scale and eye-line (front, three-quarter left, side, back), plus one large head-and-shoulders view. Neutral calm expression. Even flat lighting.

CONSTRAINTS: no text, no letters, no numerals, no logos, no watermark; hands hidden or simple flat mitten shape; plain background; clearly adult; not any real person or existing character.

Avoid: text, letters, numerals, logos, monograms, watermarks, signatures, brand patterns, photorealism, 3D render, anime, chibi or kawaii proportions, large glossy eyes, blush, child-like features, school uniform, short skirt, cleavage, swimwear, lingerie, sexualised pose, exaggerated or idealised body, elongated legs, detailed fingers, gradients, airbrush, soft shadow, skin pores, fabric texture, glitter, dyed hair, makeup emphasis, tattoos, saturated blue, saturated green, saturated teal, saturated yellow, rainbow stripes, flags, party colours, red-star symbols, Indigenous patterns, traditional costume, any resemblance to a real person or an existing character.

OUTPUT: 1 image, wide landscape.
```

If an app answers with text instead of a picture, reply "Please generate the image now." If the app has no shape setting and gives a square or tall picture, add this as a last line (my addition): "Make it a wide landscape image."

### 2.3 The Avoid list on its own

Chat tools have no negative-prompt box, so the Avoid list is a sentence at the end of the prompt (already done in 2.1 and 2.2). Keep this copy for tools or modes that do have a separate negative field, and for adding to a retry. Add to it, never remove from it, when you find a new failure (bible 5.1 notes), and tell Claude so the bible gets the new item. If the long list seems to make an app draw the things it names, use the short fallback at the end of section 9.

```
Avoid: text, letters, numerals, logos, monograms, watermarks, signatures, brand patterns, photorealism, 3D render, anime, chibi or kawaii proportions, large glossy eyes, blush, child-like features, school uniform, short skirt, cleavage, swimwear, lingerie, sexualised pose, exaggerated or idealised body, elongated legs, detailed fingers, gradients, airbrush, soft shadow, skin pores, fabric texture, glitter, dyed hair, makeup emphasis, tattoos, saturated blue, saturated green, saturated teal, saturated yellow, rainbow stripes, flags, party colours, red-star symbols, Indigenous patterns, traditional costume, any resemblance to a real person or an existing character.
```

### 2.4 What to generate

- **4 images in Gemini and 4 in ChatGPT.** Each image is itself a five-view sheet. Four separate images per tool, not one image containing four sheets.
- Save each one at once as `assets/sehuan/candidates/R01_cand_gemini_1.png` to `_4`, and `R01_cand_chatgpt_1.png` to `_4`. If the app gives you another file type (`.jpg`, `.webp`), keep that type and use the real name in the log.
- Write down, for each: the tool, the model label exactly as the app shows it today, the time, and the conversation link or ID if the app gives one. If a seed number is shown, write it down (the bible assumes these apps probably show none, 5.7 step 9).
- If nothing passes, change one thing (a fix phrase from section 9), generate 4 more, and repeat. The bible asks for "many candidates" on both tools and gives no number, so plan on a few rounds of 4. If both tools fail the same way after two rounds, stop and tell Claude: the design may need a change in the bible.

### 2.5 How to choose

1. **Thirty-second reject pass.** Throw out any sheet with any text or numerals (including fake Chinese), a photographic, 3D or airbrushed look, large glossy eyes or blush or a child-like face, detailed fingers, a school-uniform look or a short skirt, an exaggerated or elongated body, no earring or a saturated-rainbow earring, or views that look like different people. Do not delete the files (they are already in `candidates`); mark them "rejected" in your notes. A wrong background colour alone is not a reject: it can be fixed in an editor, but note it.
2. **Check which ear.** The bible says the hair is tucked behind "the left ear" and does not say whose left. This pack reads it as her own left ear, which sits on the right-hand side of the picture in a front view. Write down which side R01 shows. If an otherwise excellent sheet has it on the other side, flip the whole sheet left-to-right in an image editor and log it as a human edit (a mirror image is the same design). Tell Claude, so the bible can say it in words.
3. **Checklist.** Run section 5 on each survivor, using the large head-and-shoulders view at full size and the front full-body view shrunk to thumbnail size.
4. **Shortlist at most three.** Prefer the sheet where all five views clearly show the same woman, the earring reads as a muted colour wheel on the tucked-back ear, the face is calm and plainly adult, and the persimmon neckerchief is small.
5. **Blind look by the wife, and your reverse-image search.** Copy the shortlist to a separate folder under neutral names (S1, S2, S3, in random order, with the key written on paper) so the wife sees the pictures without knowing which tool made them (bible 5.7 step 1 asks for a blind shortlist). She uses section 8. You run the reverse-image search on each shortlisted image (section 6.3).
6. **Choose one** and copy it to `assets/sehuan/R01_master_v1.png` (keep the original in `candidates`). Log it as "provisional master". It becomes the real master only after the age-guess and look-alike tests (section 6) pass and the operator has hand-finished it in an image editor: fix proportions, hair and brush line, redraw the earring wheel with exact hex values, redraw the chip ring, and create the fixed mitten-hand asset (bible 5.7 step 2).

---

## 3. STEP 2: lock it

### 3.1 How the master is used as the reference

Two ways, and a recommendation.
- **Same chat:** keep going in the chat that made R01, send a new prompt, and the app can see the earlier picture. Fast, but each new picture is built on the last one and the face can drift (assumption).
- **New chat with R01 re-uploaded (recommended).** Open a fresh chat, attach your saved `R01_master_v1` file (your own image made with this pack; uploading it is fine; use the attach or upload button, wording varies by app), then send the Character Lock followed by the prompt for that image. The bible's advice is to restart from the master rather than correct a drifted thread (5.2 notes, 5.7 step 7); this sitting confirms or refutes it. Use "same chat" only to retry the same image with a small fix.

Rules from the bible (5.7) that apply to every image below:
1. Attach R01 every time, plus at most two other references (the bible says attach the master and the closest-angle approved image, three references at most). Never anchor to a freshly generated picture alone.
2. Change one thing per picture (one angle, one outfit, one expression set).
3. Make 4, choose the best, and compare it with R01 **at the same size**, using the checklist in section 5. If you have an editor with layers, put the new image over R01 at about 50 percent opacity and look for drift in the jaw, eyes, hairline and earring (the bible calls this onion-skinning).
4. If two pictures in a row fail the locked features, stop and re-anchor: new chat, R01 attached, nothing else.
5. All pictures are text-free. Chinese text and numbers are added later, in a design tool, never by the generator.
6. References are only your own approved pictures or plain colour swatches. Nothing else, ever (bible 5.7 step 10; BRIEF Ground rule 2).
7. If a tool refuses or returns a blocked message, do not reword the prompt to get around it. Log it and tell Claude.

### 3.2 What every message looks like

Message = **Character Lock** (section 4.1, pasted first) + **a blank line** + **the prompt for that image** (the code boxes below). Attach the files named on the "Attach" line before you send. Do **not** use the Character Lock for the items with no character in them (R07b, R07c, R10, R11, R13); they say so and carry their own style words.

**Per-image routine (about 10 minutes each; my estimate).**
1. Open a new chat in the tool that made R01.
2. Attach the files on the "Attach" line, using the attach or upload button of the current app (the wording and the number of files allowed vary, and I have not verified either; if the app takes fewer files than the line asks for, attach R01 first and tell Claude). The bible only suggests that ChatGPT may have an edit mode that works with reference images (a hypothesis); a normal message with the images attached is enough for today.
3. Paste the Character Lock, a blank line, then the prompt for that image.
4. Get 4 images (settings in section 1) and save all 4 into `candidates` at once.
5. Run the checklist (section 5) on each, choose one, and copy it to its pack name.
6. Add the log rows (kept and discarded) before you start the next image.

"Image 1" always means the first file you attached, which is R01. Where a second file is attached, the prompt says "Image 2 is ...".

**Wording this pack adds to the bible** (so you can tell bible from pack; Claude or the wife can veto any of it):
- Every OUTPUT line: the shapes (4:5 portrait for single figures, 3:2 or 16:9 for sheets, 1:1 for the avatar), "full body in frame with clear space around it so it can be cut out", and "no cast shadow" (the bible says only "plain background", "even flat lighting" and "no soft shadows"). The bible leaves `{aspect ratio}` open.
- Direction words. "Left" in a view name means turned toward the viewer's left, which shows her own left side, where the tucked-back ear and the earring are. This is my reading of the bible's "left ear" (see 2.5 step 2).
- The bible says "earrings" (plural) and "visible on the right when the head turns", so this pack reads it as one wheel earring on each ear, with the left ear always visible because the hair is tucked behind it.
- Outfit B gets adult-cut words (collar open, no tie, no bow, no pleats) because a collared shirt, a vest and a skirt can read as a school uniform (bible 4.7 item 3 bans that look).
- V1 and V2 mention a "strap" in the bible without saying what it belongs to; the prompts add a small plain bag and give the folded umbrella a charcoal colour. V1 uses the trousers option, not the shorts option.
- The two expressions that the bible describes almost identically (E06 and E10) are told apart by the brows. The look directions in E03 and E04, "no teeth" in E02, and "closed-mouth" in E05 are my wording of the bible's short descriptions. The four hand gestures in R07c are my suggestion; the bible says "four gestures" without naming them. "3 sizes" for P06 and P07 is read as three crops made later in an editor. The tote, sneakers, parasol, umbrella and rain-boot colours in R07b follow the outfit table; the umbrella colour is my choice.

### 3.3 Order of work, file names and what to attach

Save files in `assets/sehuan/`. Version number `v1` goes up if you redo an image (`v2`). File types follow whatever the app gives you. Candidates you looked at but did not choose go in `assets/sehuan/candidates/` as `<ID>_cand_<tool>_<n>` (for example `R02_cand_gemini_1.png`). Where one ID covers several separate pictures (the single expressions of R03, the poses of R04, and the flats, dress-form views and plates of R10, R11 and R13), put the item name before `cand` so two candidates never share a file name: `R03_E02_cand_gemini_1.png`, `R04_P01_cand_chatgpt_2.png`, `R10_flat_blazer_cand_gemini_1.png`, `R13_plate_bus-shelter_cand_chatgpt_1.png`.

| Order | ID | Image | Attach | Save the chosen one as | When |
|---|---|---|---|---|---|
| 1 | R01 | Master sheet: front, three-quarter left, side, back + large head-and-shoulders, outfit A | nothing | `R01_master_v1.png` | Today, Step 1 |
| 2 | R02 | Face sheet: front, three-quarter, profile, ear close-up | R01 | `R02_face-sheet_v1.png` | Today |
| 3 | R03 | Expression sheet E01 to E10, bust | R01, R02 | `R03_expressions_v1.png` | Today; prompt in 4.2 (singles in 4.3) |
| 4 | R05b | Outfit B, front and back | R01 | `R05b_outfit-B_v1.png` | Next sitting (or today if time) |
| 5 | R05c | Outfit C, front and back | R01 | `R05c_outfit-C_v1.png` | Next sitting |
| 6 | R05a | Outfit A, front and back (optional: R01 already shows A) | R01 | `R05a_outfit-A_v1.png` | Only if R01's back view is weak |
| 7 | R06a | Variant V1 hot and humid, front and back | R01 | `R06a_V1-hot-humid_v1.png` | Next sitting |
| 8 | R06b | Variant V2 rain, front and back | R01 | `R06b_V2-rain_v1.png` | Next sitting |
| 9 | R06c | Variant V3 damp cold, front and back | R01 | `R06c_V3-damp-cold_v1.png` | Next sitting |
| 10 | R04 | Poses P01 to P12, one image each | R01 (plus the outfit sheet where stated) | `R04_P01_front-pockets_v1.png` and so on | Next sitting; prompts in 4.4 |
| 11 | R07a | Signature-details sheet (earring, chip ring, neckerchief) | R01, R02 | `R07a_signature-details_v1.png` | Next sitting |
| 11b | R07b, R07c | Props sheet; mitten-hand guide (no person in either) | nothing | `R07b_props_v1.png`, `R07c_mitten-hand_v1.png` | Next sitting; no Character Lock |
| 12 | R10 | Garment flats (about ten, then shoes and tote) | nothing | `R10_flat_<garment>_v1.png` | Next sitting, library; no Character Lock |
| 13 | R11 | Dress form (front, three-quarter, back) | nothing | `R11_dress-form_<view>_v1.png` | Next sitting, library; no Character Lock |
| 14 | R13 | Empty setting plates (ten) | nothing | `R13_plate_<setting>_v1.png` | Next sitting, library; no Character Lock |
| 15 | R08, R09, R12, R14 to R18 | Not generated | none | See 3.5 | Later |

The bible's list uses the layout `assets/sehuan/ref/` and names like `sehuan_ref_v01_front_E01_A_20261015.png` for the frozen golden set. The names above are working names for today; renaming into the golden-set scheme happens when the set is frozen (bible 5.7 step 5), and Claude can do that rename and update the log paths.

Why this order: face, then expressions, locks the identity before anything with more detail is tried; outfits and seasons come before poses because P10 and P11 need the outfit B sheet and the V2 sheet as second references.

### 3.4 The prompts (send after the Character Lock)

**R02: face sheet.** Attach: R01.

```
CHANGE ONLY: the framing. Make a face sheet of the same character: head and shoulders only, four panels on one sheet at the same eye-line, calm neutral expression in all of them. Panels, left to right: (1) front view; (2) three-quarter view turned toward the viewer's left; (3) profile view facing the viewer's left; (4) a larger close-up of her left ear with the colour-wheel earring: the hair tucked behind the ear, a little of the jaw and neck, and the earring big enough that its twelve muted wedge segments can be counted, no numbers or letters. Same face in every panel: same long-oval shape, jaw shadow, almond eyes, brows, nose stroke, mouth and ears.
OUTPUT: 1 image, 3:2 landscape; plain pale-blush #F2DAD2 background; no labels, no text; no cast shadow.
```

**R03: expression sheet.** Attach: R01 and R02. The prompt is in section 4.2, with single-expression prompts in 4.3.

**R05b: outfit B, front and back.** Attach: R01.

```
CHANGE ONLY: the outfit, shown as two full-body views of the same character side by side at the same scale and eye-line: front and back. Calm neutral expression.
Outfit B: a cream (#F4E8DF) long-sleeve collared shirt with the sleeves rolled to the elbow, collar open at the neck, no tie, no bow; a charcoal (#3A3735) sleeveless knit vest; a warm stone grey (#B8AEA2) midi skirt ending below the knee, no pleats; charcoal (#3A3735) ankle boots. A plain persimmon (#CD8B6A) canvas tote on the shoulder with the ring of six blank colour-chip cards clipped to its strap. The tote is the only persimmon item, so no neckerchief in this outfit. Hands as simple flat mitten shapes with a separate thumb, no detailed fingers.
No logos, text, tags, labels or patterns on any clothing or on the tote. Nothing else about the character changes.
OUTPUT: 1 image, 3:2 landscape; plain pale-blush #F2DAD2 background; both full bodies in frame; no cast shadow.
```

**R05c: outfit C, front and back.** Attach: R01.

```
CHANGE ONLY: the outfit, shown as two full-body views of the same character side by side at the same scale and eye-line: front and back. Calm neutral expression.
Outfit C: a long open knit coat in charcoal (#3A3735) over a cream (#F4E8DF) tee; warm stone grey (#B8AEA2) straight trousers; persimmon (#CD8B6A) flat canvas sneakers with cream laces, no logos. The sneakers are the only persimmon item, so no neckerchief in this outfit. The hair stays tucked behind the left ear with the earring visible. The ring of six blank colour-chip cards is clipped to a belt loop and visible at the waist where the coat is open. Hands as simple flat mitten shapes with a separate thumb, no detailed fingers.
No logos, text, tags, labels or patterns on any clothing. Nothing else about the character changes.
OUTPUT: 1 image, 3:2 landscape; plain pale-blush #F2DAD2 background; both full bodies in frame; no cast shadow.
```

**R05a: outfit A, front and back (optional).** Attach: R01. Only if R01's back view is weak.

```
CHANGE ONLY: the view, shown as two full-body views of the same character side by side at the same scale and eye-line: front and back. Calm neutral expression.
Outfit A exactly as in Image 1: relaxed single-breasted blazer in warm stone grey (#B8AEA2), worn open, over a cream (#F4E8DF) fine-knit crew-neck top; charcoal (#3A3735) straight wide trousers ending at the ankle; flat charcoal loafers; a small persimmon (#CD8B6A) neckerchief knotted at the collar; the ring of six blank colour-chip cards clipped to a belt loop. In the back view the hair is tucked behind the left ear with the earring visible, and the neckerchief knot shows at the collar. Hands hidden in the blazer pockets.
No logos, text, tags, labels or patterns on any clothing.
OUTPUT: 1 image, 3:2 landscape; plain pale-blush #F2DAD2 background; both full bodies in frame; no cast shadow.
```

**R06a: variant V1, hot and humid, front and back.** Attach: R01. (The bible says "bag strap" without describing the bag; the small plain bag is my addition. The bible allows trousers or knee-length shorts; this uses trousers.)

```
CHANGE ONLY: the outfit, shown as two full-body views of the same character side by side at the same scale and eye-line: front and back. Calm neutral expression.
Variant V1, hot and humid: a short-sleeve cream (#F4E8DF) shirt worn untucked; warm stone grey (#B8AEA2) wide trousers cropped at the ankle; simple flat sandals, feet drawn as simple shapes without detailed toes; a small plain bag in warm stone grey (#B8AEA2) on the shoulder, with the ring of six blank colour-chip cards clipped to its strap; a closed compact cream (#F4E8DF) parasol with persimmon (#CD8B6A) trim hooked over the bag strap. The parasol trim is the only persimmon item. Hands as simple flat mitten shapes with a separate thumb, no detailed fingers.
No logos, text, tags, labels or patterns. Nothing else about the character changes.
OUTPUT: 1 image, 3:2 landscape; plain pale-blush #F2DAD2 background; both full bodies in frame; no cast shadow.
```

**R06b: variant V2, rain, front and back.** Attach: R01.

```
CHANGE ONLY: the outfit, shown as two full-body views of the same character side by side at the same scale and eye-line: front and back. Calm neutral expression.
Variant V2, rain: a short warm stone grey (#B8AEA2) rain jacket with the hood down; cropped charcoal (#3A3735) trousers; charcoal (#3A3735) ankle-high rain boots; a small persimmon (#CD8B6A) neckerchief at the collar; a small plain bag in warm stone grey with the ring of six blank colour-chip cards clipped to its strap and a plain folded charcoal umbrella hooked on the strap. The neckerchief is the only persimmon item. Hands as simple flat mitten shapes with a separate thumb, no detailed fingers.
No logos, text, tags, labels or patterns. Nothing else about the character changes.
OUTPUT: 1 image, 3:2 landscape; plain pale-blush #F2DAD2 background; both full bodies in frame; no cast shadow.
```

**R06c: variant V3, damp cold, front and back.** Attach: R01.

```
CHANGE ONLY: the outfit, shown as two full-body views of the same character side by side at the same scale and eye-line: front and back. Calm neutral expression.
Variant V3, damp cold: a long charcoal (#3A3735) coat worn open over a cream (#F4E8DF) knit; warm stone grey (#B8AEA2) trousers; a cream (#F4E8DF) scarf with a persimmon (#CD8B6A) stripe at each end; charcoal (#3A3735) ankle boots. The ring of six blank colour-chip cards is clipped to a belt loop and visible where the coat is open. The scarf's end stripes are the only persimmon item. Hands as simple flat mitten shapes with a separate thumb, no detailed fingers. Taiwan climate: damp, overcast, mild cold; no snow, no puffer coat.
No logos, text, tags, labels or patterns. Nothing else about the character changes.
OUTPUT: 1 image, 3:2 landscape; plain pale-blush #F2DAD2 background; both full bodies in frame; no cast shadow.
```

**R04: poses P01 to P12.** Attach: R01, plus the outfit sheet named in each prompt. The prompts are in section 4.4.

**R07a: signature-details sheet.** Attach: R01 and R02. Think of this as the guide for the hand-drawn earring and chip-ring layers, which the bible says are redrawn by hand on every cut-out (5.7 step 3). Do not trust its details; count the segments.

```
CHANGE ONLY: the framing. Make a detail sheet of the character's signature details, large and clear, in a 2 by 2 grid on one sheet:
1. The colour-wheel earring shown flat three times at three sizes (small, medium, large): a round drop earring made of twelve equal wedge segments in muted colours in this order: #C27F80, #C58479, #CD8B6A, #D2AE72, #CCC07F, #A9B27F, #8DA68C, #7EA3A0, #7C95AA, #8A8DB0, #9F8AAB, #B58AA0. No numbers or letters.
2. The same earring on her left ear, close-up, with the hair tucked behind the ear.
3. The ring of six blank colour-chip cards in muted tints (#E6BBA3, #E4D6CB, #B8AEA2, #D2AE72, #C27F80, #9F8AAB) shown three ways: flat, clipped to a bag strap, hanging from a belt loop. No text, no numbers, no codes on the cards.
4. The small persimmon (#CD8B6A) neckerchief, knotted at a cream collar.
OUTPUT: 1 image, 1:1 square; plain pale-blush #F2DAD2 background; no labels, no text; no cast shadow.
```

**R07b: props sheet.** Attach: nothing. No Character Lock (there is no person in the picture, so the prompt carries its own style words). These are generic items that copy no brand; the operator checks each one for logos and invented details afterwards.

```
No person in this picture. A props sheet of five separate generic items laid out apart from each other on one sheet, plain pale-blush #F2DAD2 background: (1) a plain persimmon (#CD8B6A) canvas tote bag; (2) persimmon (#CD8B6A) flat canvas sneakers with cream (#F4E8DF) laces; (3) a closed compact cream (#F4E8DF) parasol with persimmon (#CD8B6A) trim; (4) a plain folded charcoal (#3A3735) umbrella; (5) charcoal (#3A3735) ankle-high rain boots. Each item is a flat illustration: flat colour fields with a loose charcoal (#3A3735) ink-brush outline whose weight varies from thin to thick, no gradients, no airbrushing, no soft shadows, no fabric texture, no 3D. Original generic designs that copy no brand. No logos, no tags, no labels, no text, no letters, no numerals, no pattern, no embossing, no brand-like details.
OUTPUT: 1 image, 3:2 landscape; no labels; no cast shadow.
```

**R07c: mitten-hand guide.** Attach: nothing. No Character Lock. The approved hand asset is drawn by hand (bible 5.7 step 2); this only gives you a shape to trace. If the tool draws detailed fingers, stop and draw the hand yourself instead of regenerating again and again.

```
No face and no other part of a person in this picture. A sheet of four versions of one hand and wrist, each drawn as a simple flat mitten shape with a separate thumb, in a flat warm medium skin tone (#DDB38E) with one shadow shape (#C4946C), on a plain pale-blush #F2DAD2 background. Style: flat colour fields with a loose charcoal (#3A3735) ink-brush outline whose weight varies from thin to thick, no gradients, no airbrushing, no soft shadows, no skin pores, no 3D. Gestures, left to right: (1) relaxed, hanging down; (2) presenting, the forearm held out sideways with the mitten open and tilted slightly up; (3) pointing, the front edge of the mitten extended toward the right; (4) resting, turned palm-down. No fingers, no knuckles, no fingernails, no rings, no raised open palm. No text, no letters, no numerals.
OUTPUT: 1 image, 3:2 landscape; no labels; no cast shadow.
```

**Library items: no character, no Character Lock.** These come from the bible's companion prompts (5.3). Generated flats and plates are never trusted: the operator checks each for logos, invented details and brand-like patterns, and recolours by hex in an editor (bible G9). A flat that resembles a recognisable branded design is discarded.

**R10: garment flat.** Attach: nothing. Make one flat per request. Fill `{GARMENT}` and `{HEX}` from the table below the box.

```
GARMENT FLAT: A generic garment flat of {GARMENT}, front view only, centred on a plain pale-blush #F2DAD2 background. Original generic design that copies no brand. Single flat fill {HEX} with a loose charcoal ink-brush outline, simple seams only. Symmetrical, no wrinkles, no body, no hanger. No logos, no tags, no labels, no text, no pattern, no embossing, no brand-like details.
```

| # | `{GARMENT}` | Starting `{HEX}` (my suggestion from the outfit table 4.3; the final fill is set by hand) |
|---|---|---|
| 1 | a relaxed single-breasted blazer | `#B8AEA2` |
| 2 | a long open knit coat | `#3A3735` |
| 3 | a sleeveless knit vest | `#3A3735` |
| 4 | a long-sleeve collared shirt | `#F4E8DF` |
| 5 | a fine-knit crew-neck top | `#F4E8DF` |
| 6 | straight wide trousers ending at the ankle | `#3A3735` |
| 7 | straight trousers | `#B8AEA2` |
| 8 | a midi skirt ending below the knee | `#B8AEA2` |
| 9 | a short rain jacket with the hood down | `#B8AEA2` |
| 10 | a long coat | `#3A3735` |
| later | flat loafers `#3A3735`; ankle boots `#3A3735`; flat canvas sneakers `#CD8B6A`; ankle-high rain boots `#3A3735`; a plain canvas tote `#CD8B6A` | for shoes and the tote, change "front view only" to "side view only" |

**R11: dress form.** Attach: nothing. Make three requests, changing "front view" to "three-quarter view" and "back view".

```
DRESS FORM: A faceless dress form (tailor's mannequin) on a simple stand, front view, plain pale-blush #F2DAD2 background. No face, no head detail, simple neck cap. Flat cream and warm-stone fills with a loose charcoal ink-brush outline. No text, no logo, no measuring tape.
```

**R13: setting plate.** Attach: nothing. Ten plates. The box shows the first one, filled in, as a worked example; for each other plate, replace the setting name, the Taiwan details and the season-and-weather sentence in the box with the matching row of the table below it. Plates are labelled 示意圖 in post and are never described as places the character visited.

```
SETTING PLATE: An empty background plate of an arcade walkway in rain, no people, no text. All signs, banners and screens are left blank. No logos, no legible numbers, no legible plates. Flat colour fields with a loose charcoal ink-brush line, muted palette (pale blush, cream, charcoal, warm stone). Taiwan details: a continuous ground-floor covered walkway along shophouses, square pillars, tiled floor, scooters parked at an angle along the pillars with blank number plates, goods spilling from shops, vertical shop signs left blank, roll-up shutters, wet street edge, folded umbrellas. Season and weather: damp overcast November, wet pavement, no snow, no autumn leaves.
```

The prompt stays in English on purpose: 騎樓 (the arcade walkway) is a word for you and the wife, and a Chinese word inside a prompt can tempt a tool to draw Chinese characters on the signs. Fill-in table (the details are from bible 4.8; the wife checks the results against her own eye):

| # | Setting | Taiwan details to paste after "Taiwan details:" | Season and weather |
|---|---|---|---|
| 1 | Arcade walkway in rain | See the box above | damp overcast November, wet pavement |
| 2 | Bus shelter in rain | Right-hand traffic, bus doors on the right, a shelter with a bench, a blank route-number panel and a blank arrival board, scooters waiting at the stop line, wet road | damp overcast November, wet road |
| 3 | MRT exit or platform, generic | Escalator and stair exit with a canopy, platform screen doors, yellow tactile paving, anonymous station, bilingual signs left blank, priority seats. No map, no station name, no line colours | indoor, even light |
| 4 | Department-store atrium | Atrium with crossing escalators, a blank floor directory, blank promotional banners, generic paper shopping bags without logos, queue lines | indoor, even light |
| 5 | Air-conditioned office | Open-plan desks with low partitions, ceiling air-conditioner units, a cardigan hung on a chair back as set dressing only, Type A sockets, a window with city haze | indoor, hazy window light |
| 6 | Convenience-store door, rainy day | Sliding door, an umbrella stand beside it, a seating area inside, a ticket-kiosk machine, a hot-food counter, no logos | damp overcast November, wet pavement |
| 7 | Home entrance and balcony | Shoes off, a shoe cabinet, tiled floor, a balcony with a drying rack and window grilles, air-conditioner outdoor units, a dehumidifier | soft indoor light |
| 8 | Banquet hall | Round tables for about ten with a turntable, a red backdrop panel left blank, a stage screen left blank | indoor, even light |
| 9 | Shopping district street | Dense scooters, hazy light, wet pavement, blank vertical signs | damp overcast November, no clear sky |
| 10 | Residential alley | Overhead cables, iron window grilles, rooftop water tanks, air-conditioner units, laundry poles | hazy, evergreen vegetation, no snow, no autumn leaves |

For the indoor plates (3, 4, 5, 7, 8) the weather sentence can be shortened to just the light. Every plate keeps the sentence "All signs, banners and screens are left blank". No plate shows a person, a rider or a helmet (bible choice C8: no scooter riding in the pilot; parked scooters are fine). Plate 7 (home entrance and balcony) is only for shoe or rain-gear scenes, because laundry and storage topics belong to another character in the studio (bible 4.8). Nothing on any plate may be worn or handled by the character: plates are empty backgrounds.

### 3.5 Images that are not generated

- **R08 cut-out library.** Made by hand in an editor from approved pictures (remove the background to a transparent PNG, then replace the earring and the chip ring with the hand-drawn layers). Generators do not reliably give true transparency, and the bible plans the cut-outs as human-checked and hand-finished (5.7 step 3). Done after the master is final.
- **R09 thumbnail test sheet.** Made from the final master by shrinking it in an editor: the figure at 64, 96 and 128 pixels on the pale-blush ground and on a dark background. It is also the stimulus for the age-guess panel.
- **R12 colour-wheel master diagram.** A vector drawing built by hand with the twelve hex values (ring only, numbered, tone-named variants; chip-card template; a lightness strip). Do not ask a generator to draw it (bible 4.4).
- **R14 carousel and Reel templates, R15 avatar, highlight covers and the 「關於色環」 pinned-post image, R16 badge and label artwork.** All carry Chinese text (for example 「AI 生成」, 「搭配示意」, 「示意圖」). Do **not** ask Gemini or ChatGPT to draw any of it. It is typeset later in a design tool with a Taiwan-glyph (TC) font whose licence the operator has read (bible G14), and the wife reads every character. The avatar is a head-and-shoulders crop of the final master, tested at 64, 96 and 128 pixels.
- **R17 palette swatch chart.** Made by hand: one square per colour with its hex under it (the table in 5.4 is the data). The wife uses it for her colour read and the side-by-side check.
- **R18 look-alike log.** A file `personas/sehuan/lookalike_log.md`, created in Phase 4. Use the table in 6.4 meanwhile; Claude can turn it into the file.

---

## 4. Expression sheet and pose prompts

### 4.1 The Character Lock (paste this at the start of every prompt in sections 3 and 4)

It is built from the bible's later-turn sentence (5.2) and its KEEP IDENTICAL, STYLE, CONSTRAINTS and AVOID blocks (5.3), with the colours from bible sections 4.1 to 4.4. It is long on purpose: you paste it, you do not read it every time. Attach R01 first. Do **not** use it for R01 itself, nor for R07b, R07c, R10, R11 and R13 (no character).

```
The attached Image 1 is the chosen master reference sheet for an ORIGINAL, fictional, clearly adult virtual character: a woman-presenting character, stated age 30. She is not based on any real person, celebrity, model, influencer or existing character. Use Image 1 as the identity reference. This is the same character: same face, jaw, eyes, eyebrows, nose stroke, mouth, ears, hair, skin tone, proportions, colour-wheel earrings and chip ring (and the persimmon neckerchief only where the outfit below includes it). Keep every locked feature identical. Do not redesign, restyle or add detail.

KEEP IDENTICAL: long-oval face with softly defined cheekbones and jaw shadow; almond eyes of modest size (each about one fifth of the face width) filled charcoal #3A3735 with one small cream #F4E8DF highlight; straight dark eyebrows of medium thickness filled #2F2A28; a nose drawn as one short brush stroke with a small shadow shape; a calm mouth in flat muted terracotta-brown #B27A6C; both ears and the neck visible; natural dark brown-black #2F2A28 shoulder-length blunt hair with a side parting, tucked behind the left ear so the earring is visible, flat colour plus one lighter highlight shape; flat warm medium skin #DDB38E with one shadow shape #C4946C; about seven and a half heads tall, average-to-slim, natural (not elongated) legs, soft shoulders; round drop earrings shaped like a colour wheel of twelve equal wedge segments in the muted colours #C27F80, #C58479, #CD8B6A, #D2AE72, #CCC07F, #A9B27F, #8DA68C, #7EA3A0, #7C95AA, #8A8DB0, #9F8AAB, #B58AA0 in that order, about one quarter of the face width, no numbers or letters; one persimmon accent #CD8B6A covering about one tenth of the visible clothing; a ring of six blank colour-chip cards (#E6BBA3, #E4D6CB, #B8AEA2, #D2AE72, #C27F80, #9F8AAB), clipped and never held, no text on the cards.

STYLE: contemporary fashion illustration, flat colour fields, a loose ink-brush line whose weight varies from thin to thick with small gaps and overshoots, fills sitting very slightly off the line. No gradients, no airbrushing, no soft shadows, no photographic skin or fabric texture, no 3D, no glow.

DEFAULTS, unless the change below says otherwise: calm neutral expression (brows level, mouth closed with a very slight asymmetric smile); outfit A (relaxed single-breasted warm stone grey #B8AEA2 blazer worn open over a cream #F4E8DF fine-knit crew-neck top, charcoal #3A3735 straight wide trousers ending at the ankle, flat charcoal loafers, a small persimmon #CD8B6A neckerchief at the collar); hands hidden in the blazer pockets or drawn as simple flat mitten shapes with a separate thumb, never detailed fingers; plain pale-blush #F2DAD2 background; even flat lighting. No logos, text, tags, labels or patterns on any clothing.

Avoid: text, letters, numerals, logos, monograms, watermarks, signatures, brand patterns, photorealism, 3D render, anime, chibi or kawaii proportions, large glossy eyes, blush, child-like features, school uniform, short skirt, cleavage, swimwear, lingerie, sexualised pose, exaggerated or idealised body, elongated legs, detailed fingers, gradients, airbrush, soft shadow, skin pores, fabric texture, glitter, dyed hair, makeup emphasis, tattoos, saturated blue, saturated green, saturated teal, saturated yellow, rainbow stripes, flags, party colours, red-star symbols, Indigenous patterns, traditional costume, any resemblance to a real person or an existing character.

If anything about the face changes, tell me and redo it.
```

### 4.2 R03: expression sheet (all ten at once)

Attach: R01 and R02. No labels on the picture: the generator would garble them. You tell the faces apart by position: top row left to right is E01 to E05, bottom row is E06 to E10. The zh-TW names are an AI draft for the wife and for your notes only; the prompt is English. Bible rules (5.4): no wide grin, tears, anger, wink, pout or tongue, and no raised-palm "stop" gesture (it can read as protest or traffic police). She is a calm explainer, so expressions are small.

| ID | Name (zh-TW is an AI draft) | Face | Bible use |
|---|---|---|---|
| E01 | Neutral, calm 平靜 | Default: brows level, mouth closed | Avatar, most cut-outs |
| E02 | Explaining 說明 | Slight head tilt, mouth slightly open | Rule slides |
| E03 | Pointing attention 提醒注意 | Eyebrows slightly raised, eyes toward the diagram | "Look here" moments |
| E04 | Comparing 比較 | Eyes move toward one side, brows very slightly asymmetric | A-versus-B and "轉一格" slides |
| E05 | Mild smile 微笑 | Small, closed-mouth smile | Intros, thanks |
| E06 | Uncertain 不確定 | Small tilt, lips pressed | "Go by the brand's page" |
| E07 | Careful 謹慎 | Brows drawn slightly in, level mouth | Size-chart numbers, label warnings |
| E08 | Correcting 更正 | Small head bow, soft brows | Corrections |
| E09 | Pleased, light 輕鬆愉快 | Small smile, eyes crease slightly | A new hue revealed at "轉一格" |
| E10 | Polite decline 婉拒 | Slight tilt, lips pressed, soft brows | Questions she will not answer |

```
Image 2 is the face sheet; use it for the face only.
CHANGE ONLY: the expression, shown as an expression sheet of the same head and shoulders ten times, same scale and eye-line, evenly spaced in two rows of five, no labels, no text. The hair is tucked behind the left ear and the colour-wheel earring is visible in every one. Top row, left to right:
1. Neutral and calm: brows level, mouth closed with a very slight asymmetric smile.
2. Explaining: a slight head tilt, the mouth slightly open as if speaking, no teeth.
3. Pointing attention: eyebrows slightly raised, the eyes looking toward the viewer's left at something just outside the picture.
4. Comparing: the eyes glancing to one side, the brows very slightly asymmetric.
5. Mild smile: a small closed-mouth smile.
Bottom row, left to right:
6. Uncertain: a small head tilt, lips pressed together, brows level.
7. Careful: brows drawn slightly inward, mouth level.
8. Correcting: a small bow of the head, soft brows.
9. Pleased, light: a small smile, the eyes creasing slightly.
10. Polite decline: a slight head tilt, lips pressed together, soft brows raised slightly at the inner ends.
Only the brows, eyes, mouth and a small head tilt change. Same face, hair, earring, neckerchief and colours in all ten. No wide grin, no teeth, no tears, no anger, no wink, no pout, no tongue, no raised open palm.
OUTPUT: 1 image, 16:9 landscape; plain pale-blush #F2DAD2 background; no cast shadow.
```

Ten faces on one sheet are small, so expect some drift. If the faces do not match each other and R01 (check A11 in section 5), use the single-expression prompts in 4.3 instead. Pick the final ten from whichever route works, and keep them in the set as `R03_E01_neutral_v1.png` to `R03_E10_polite-decline_v1.png`.

### 4.3 Single-expression prompts (E01 to E10)

Attach: R01 and R02. One image per prompt, head and shoulders, front view.

**E01: neutral, calm**

```
CHANGE ONLY: the framing and expression. Head and shoulders only, front view, centred, with a little space around the head. Expression: neutral and calm, brows level, mouth closed with a very slight asymmetric smile. Nothing else changes.
OUTPUT: 1 image, 1:1 square; plain pale-blush #F2DAD2 background; no cast shadow.
```

**E02: explaining**

```
CHANGE ONLY: the framing and expression. Head and shoulders only, front view, centred, with a little space around the head. Expression: a slight head tilt, the mouth slightly open as if speaking, no teeth. Nothing else changes.
OUTPUT: 1 image, 1:1 square; plain pale-blush #F2DAD2 background; no cast shadow.
```

**E03: pointing attention**

```
CHANGE ONLY: the framing and expression. Head and shoulders only, front view, centred, with a little space around the head. Expression: eyebrows slightly raised, the eyes looking toward the viewer's left at something just outside the picture. Nothing else changes.
OUTPUT: 1 image, 1:1 square; plain pale-blush #F2DAD2 background; no cast shadow.
```

**E04: comparing**

```
CHANGE ONLY: the framing and expression. Head and shoulders only, front view, centred, with a little space around the head. Expression: the eyes glancing toward the viewer's right, the brows very slightly asymmetric, mouth level. Nothing else changes.
OUTPUT: 1 image, 1:1 square; plain pale-blush #F2DAD2 background; no cast shadow.
```

**E05: mild smile**

```
CHANGE ONLY: the framing and expression. Head and shoulders only, front view, centred, with a little space around the head. Expression: a mild, small, closed-mouth smile, not a grin. Nothing else changes.
OUTPUT: 1 image, 1:1 square; plain pale-blush #F2DAD2 background; no cast shadow.
```

**E06: uncertain**

```
CHANGE ONLY: the framing and expression. Head and shoulders only, front view, centred, with a little space around the head. Expression: a small head tilt, lips pressed together, brows level. Nothing else changes.
OUTPUT: 1 image, 1:1 square; plain pale-blush #F2DAD2 background; no cast shadow.
```

**E07: careful**

```
CHANGE ONLY: the framing and expression. Head and shoulders only, front view, centred, with a little space around the head. Expression: brows drawn slightly inward, mouth level. Nothing else changes.
OUTPUT: 1 image, 1:1 square; plain pale-blush #F2DAD2 background; no cast shadow.
```

**E08: correcting**

```
CHANGE ONLY: the framing and expression. Head and shoulders only, front view, centred, with a little space around the head. Expression: a small bow of the head, soft brows, mouth level. Nothing else changes.
OUTPUT: 1 image, 1:1 square; plain pale-blush #F2DAD2 background; no cast shadow.
```

**E09: pleased, light**

```
CHANGE ONLY: the framing and expression. Head and shoulders only, front view, centred, with a little space around the head. Expression: a small smile with the eyes creasing slightly, not a grin. Nothing else changes.
OUTPUT: 1 image, 1:1 square; plain pale-blush #F2DAD2 background; no cast shadow.
```

**E10: polite decline**

```
CHANGE ONLY: the framing and expression. Head and shoulders only, front view, centred, with a little space around the head. Expression: a slight head tilt, lips pressed together, soft brows raised slightly at the inner ends. Nothing else changes.
OUTPUT: 1 image, 1:1 square; plain pale-blush #F2DAD2 background; no cast shadow.
```

### 4.4 Poses (R04, P01 to P12)

One image per prompt, saved as `R04_P01_front-pockets_v1.png` and so on (names in each heading). Attach: R01 unless the line says more. Bible rule (5.5): no pose involves a scooter, a seat, lying down, a crouch, a hand in the hair, a kiss, a "model" pose with hips thrown out, or a body-emphasising angle. She is a presenter beside a lesson, so nothing here shows her "trying on" or "wearing for the lesson" anything: poses use her own fixed outfits only. P01 and P06 to P10 in outfits A, B and C are what the later cut-out library needs (bible 5.7 step 3). The prompts below use outfit A. To make B or C, replace the words "Outfit A" with the outfit B or C description from section 3.4, replace "hands in the blazer pockets" with "hands as simple flat mitten shapes with a separate thumb, relaxed at her sides", add "The tote is the only persimmon item, so no neckerchief" (outfit B) or "The sneakers are the only persimmon item, so no neckerchief" (outfit C), take out any neckerchief mention (P05 names one), and attach that outfit sheet as Image 2. Since the Character Lock describes outfit A as the default, always say clearly in the prompt which outfit it is. Hands are the risk in this section: if two of four have detailed fingers, use the fix phrase in section 9 before anything else.

**P01: front, neutral, hands in pockets** (`R04_P01_front-pockets_v1.png`)

```
CHANGE ONLY: the pose. Front view, standing relaxed and upright, hands in the blazer pockets, calm neutral expression. Outfit A.
OUTPUT: 1 image, 4:5 portrait; the character alone on a plain pale-blush #F2DAD2 background; full body in frame with clear space around it so it can be cut out; no cast shadow.
```

**P02: three-quarter left** (`R04_P02_three-quarter-left_v1.png`)

```
CHANGE ONLY: the angle. Standing relaxed and upright, the whole body turned about 45 degrees toward the viewer's left, hands in the blazer pockets, calm neutral expression, the left ear and the earring visible. Outfit A.
OUTPUT: 1 image, 4:5 portrait; the character alone on a plain pale-blush #F2DAD2 background; full body in frame with clear space around it so it can be cut out; no cast shadow.
```

**P03: three-quarter right** (`R04_P03_three-quarter-right_v1.png`)

```
CHANGE ONLY: the angle. Standing relaxed and upright, the whole body turned about 45 degrees toward the viewer's right, hands in the blazer pockets, calm neutral expression, the earring on the right ear visible as the head turns. Outfit A.
OUTPUT: 1 image, 4:5 portrait; the character alone on a plain pale-blush #F2DAD2 background; full body in frame with clear space around it so it can be cut out; no cast shadow.
```

**P04: side profile** (`R04_P04_side_v1.png`)

```
CHANGE ONLY: the angle. The whole body seen exactly from the side, facing the viewer's left, standing relaxed and upright, hands in the blazer pockets, calm neutral expression, the hair tucked behind the left ear with the earring visible. Outfit A.
OUTPUT: 1 image, 4:5 portrait; the character alone on a plain pale-blush #F2DAD2 background; full body in frame with clear space around it so it can be cut out; no cast shadow.
```

**P05: back view** (`R04_P05_back_v1.png`)

```
CHANGE ONLY: the angle. The whole body seen from directly behind, standing relaxed and upright, hands in the blazer pockets: the back of the shoulder-length hair, the hair tucked behind the left ear with the ear and the earring visible from behind, the knot of the neckerchief at the collar, the back of the blazer. Outfit A.
OUTPUT: 1 image, 4:5 portrait; the character alone on a plain pale-blush #F2DAD2 background; full body in frame with clear space around it so it can be cut out; no cast shadow.
```

**P06: bust facing left toward the lesson** (`R04_P06_bust-left_v1.png`). The bible asks for three sizes; make one image and crop it to three sizes later in an editor.

```
CHANGE ONLY: the framing and pose. Chest-up (head, shoulders and upper chest), the head and shoulders turned about 45 degrees toward the viewer's left, as if looking at a diagram just outside the picture, calm neutral expression, the left ear and the earring visible. No hands in frame. Outfit A.
OUTPUT: 1 image, 4:5 portrait; the character alone on a plain pale-blush #F2DAD2 background; clear space around the head and shoulders so it can be cut out; no cast shadow.
```

**P07: bust facing right** (`R04_P07_bust-right_v1.png`)

```
CHANGE ONLY: the framing and pose. Chest-up (head, shoulders and upper chest), the head and shoulders turned about 45 degrees toward the viewer's right, as if looking at a diagram just outside the picture, calm neutral expression, the earring on the right ear visible. No hands in frame. Outfit A.
OUTPUT: 1 image, 4:5 portrait; the character alone on a plain pale-blush #F2DAD2 background; clear space around the head and shoulders so it can be cut out; no cast shadow.
```

**P08: beside a dress form, presenting with the whole forearm** (`R04_P08_dress-form_v1.png`)

```
CHANGE ONLY: the pose and setting. She stands to the left of a faceless dress form and presents it, her forearm held out sideways toward it with a simple flat mitten shape, palm up and tilted slightly up, not a raised palm; she looks toward the dress form, calm neutral expression. The dress form stands on a simple stand: no face, no head detail, simple neck cap, flat cream (#F4E8DF) and warm stone grey (#B8AEA2) fills with a loose charcoal ink-brush outline, no garment on it, no text, no logo, no measuring tape. Both full height in frame on the same ground line. Outfit A.
OUTPUT: 1 image, 3:2 landscape; plain pale-blush #F2DAD2 background; both in frame with clear space around them; no cast shadow.
```

**P09: beside a flat-lay panel, looking at it** (`R04_P09_flat-lay_v1.png`)

```
CHANGE ONLY: the pose and setting. She stands to the left of a tall plain rectangular panel on a stand, turned toward it and looking at it, hands in the blazer pockets, calm neutral expression. The panel is cream (#F4E8DF) with a loose charcoal ink-brush outline and shows three simple generic garment silhouettes (a top, a pair of trousers, a skirt) in flat cream, charcoal and warm stone grey fills with no details, no text, no logos. Both full height in frame on the same ground line. Outfit A.
OUTPUT: 1 image, 3:2 landscape; plain pale-blush #F2DAD2 background; both in frame with clear space around them; no cast shadow.
```

**P10: chest-up with the chip ring clipped at the strap in frame** (`R04_P10_chip-ring_v1.png`). Attach: R01 and `R05b_outfit-B_v1`.

```
Image 2 is the outfit B sheet; use it for the outfit and the tote only.
CHANGE ONLY: the framing and outfit. Chest-up, front view, wearing outfit B (cream collared shirt with sleeves rolled to the elbow and the collar open, charcoal sleeveless knit vest), the plain persimmon (#CD8B6A) canvas tote strap across the shoulder, and the ring of six blank colour-chip cards clipped to the strap, clearly in frame at chest height, no text on the cards. The tote is the only persimmon item, so no neckerchief. No hands in frame. Calm neutral expression.
OUTPUT: 1 image, 4:5 portrait; plain pale-blush #F2DAD2 background; clear space around the head and shoulders so it can be cut out; no cast shadow.
```

**P11: chest-up with a closed umbrella hooked on the strap (variant V2)** (`R04_P11_umbrella_v1.png`). Attach: R01 and `R06b_V2-rain_v1`.

```
Image 2 is the variant V2 (rain) sheet; use it for the outfit and the umbrella only.
CHANGE ONLY: the framing and outfit. Chest-up, front view, wearing variant V2: the short warm stone grey rain jacket with the hood down and the small persimmon (#CD8B6A) neckerchief, a plain folded charcoal umbrella hooked on the bag strap, clearly in frame. No hands in frame. Calm neutral expression.
OUTPUT: 1 image, 4:5 portrait; plain pale-blush #F2DAD2 background; clear space around the head and shoulders so it can be cut out; no cast shadow.
```

**P12: walking, side** (`R04_P12_walking_v1.png`)

```
CHANGE ONLY: the pose. Walking, seen exactly from the side, facing the viewer's left, a relaxed natural stride, upright, hands in the blazer pockets, calm neutral expression. Outfit A. Nothing else in the picture.
OUTPUT: 1 image, 3:2 landscape; the character alone on a plain pale-blush #F2DAD2 background; full body in frame with clear space around it; no cast shadow.
```

---

## 5. Pass/fail checklist

Run this on **every** image you take seriously, at the size shown in each row. Table A applies to everything. Table B is the bible's locked-features list (5.6); any single locked-feature failure rejects the image (bible 5.7 step 8). Copy the two tables into your notes once per image and tick the boxes. Mark the failure code in the last column.

**Fail codes:** **R** = regenerate (press again, change nothing). **P** = edit the prompt (add the matching fix phrase from section 9 to the end, then make 4 more). **E** = fix in an image editor (small, local; log it as a human edit and keep the untouched original). **X** = stop and tell Claude (a design problem or a test failed; never repair it with editing).

### 5.1 Table A: checks for every image

| # | Check | How to check | Pass | If it fails |
|---|---|---|---|---|
| A1 | **Adult-read at thumbnail size** | Shrink the full figure to about 110 pixels tall (about 3 cm on a laptop screen, or zoom the browser out) and the head-and-shoulders view to 64, 96 and 128 pixels. Passes only if all hold (bible 4.7): the face reads 25 or older (defined cheekbone and jaw shadow, medium-thickness brows, modest eyes, no round baby cheeks, no blush marks, no large glossy eyes); the proportions read as an adult (about seven and a half heads tall, shoulders wider than the head, natural legs; **fail if the head is larger than about one sixth of the height**, my suggested limit); the clothes read as adult workwear or casual wear (no school uniform, pleated mini skirt, knee socks, school-style collar and bow, backpack with charms, pastel kawaii palette, pigtails, character hair clips, stuffed toys); no sexualised pose, cleavage, bare midriff, swimwear or lingerie | [ ] | R once; P if 2 of 4; X if it still reads young |
| A2 | **Hands and fingers** | Zoom to 200 percent. Hands are hidden in pockets, or are simple flat mitten shapes with a separate thumb. No detailed fingers, no extra or missing fingers, no hand in the hair, no extra hands | [ ] | R once; P if 2 of 4; never E for fingers |
| A3 | **Text, garbled or Simplified Chinese included** | **No text at all**: no letters, numerals, labels, signs, signatures, watermarks. Look at the chip cards, collars and necklines, shoe soles, the corners of the sheet and the background. Any text in any script fails the image, even if it looks right, because all text is added later in a design tool. If Chinese characters do appear, ask the wife whether they are garbled, Simplified, Japanese or Hong Kong forms and note it in the log: that tells us how the tool behaves | [ ] | R; E if one small mark |
| A4 | **Party-colour read** | At thumbnail size nothing reads as a blue, green, teal or yellow camp: no dominant saturated blue, green, teal or yellow, and no main look built on blue with green, blue with white, or green with white. The persimmon is small and muted, not a dominant orange. The wife confirms (section 8) | [ ] | P (colour phrase); the wife decides |
| A5 | **Rainbow and mourning read** | The wheel earring is a small, muted circle: not a rainbow flag, no horizontal bar of six or more saturated stripes. No head-to-toe white, no head-to-toe black, nothing all red | [ ] | P; E for the earring |
| A6 | **Resemblance to real people or existing characters** | Do you or the wife instantly think of a real person, model, singer, creator, VTuber, mascot, fashion-brand character or cartoon character? A quick look now; the real tests are in section 6 | [ ] | X |
| A7 | **Medium** | Flat colour fields under a loose ink-brush line whose weight varies from thin to thick, with small gaps and overshoots; the fills sit very slightly off the line. No gradient, airbrush, soft shadow, skin pores, fabric texture, glow, 3D or photographic look | [ ] | P |
| A8 | **Palette and hex match** | Sample flat patches with a colour picker and compare with the table in 5.4 (allowed range: within 10 on each of red, green and blue, my suggestion). The ground is pale blush, not cream, white or grey | [ ] | P if the wrong colour family; E if near |
| A9 | **No brand, logo or plate** | Nothing on clothes, bag, shoes, props or background resembles a brand mark, monogram, signature stripe or check, tag, label or number plate. No bag or shoe shape that resembles a recognisable branded design | [ ] | R; P if 2 of 4 |
| A10 | **Background and framing** | Plain flat pale blush `#F2DAD2`: no gradient, texture or scene (except the library plates). No cast shadow. Full body in frame with clear space around it. Eye-level view. On a sheet: every view is clearly the same woman at the same scale and eye-line, and the right number of views is there | [ ] | R / P; E for the background colour |
| A11 | **Match to R01** (from R02 onward) | Put it beside R01 at the same size, or over it at about 50 percent opacity. Any locked feature that differs rejects it. Two failures in a row: new chat, attach only R01 | [ ] | R, then re-anchor |
| A12 | **Taiwan details** (R13 plates, and any picture with a setting) | The wife checks the list in section 8, item 8 | [ ] | P; the wife decides |
| A13 | **Saved and logged** | The file is in the right folder with the pack name; a row is in `assets/provenance.csv` with tool, model label, full prompt, time and licence notes | [ ] | Do it now |

### 5.2 Table B: locked features (bible 5.6; tick each on every approved image)

| # | Locked feature | Note for these first images | Pass |
|---|---|---|---|
| L1 | Long-oval face, softly defined cheekbone and jaw shadow | | [ ] |
| L2 | Almond eyes of modest size, one small highlight | | [ ] |
| L3 | Straight dark brows of medium thickness | | [ ] |
| L4 | Nose as one brush stroke; calm mouth in muted terracotta-brown (expression may change) | | [ ] |
| L5 | Both ears and the neck visible | In a back view the left ear and earring show from behind | [ ] |
| L6 | Shoulder-length blunt hair, side parting, tucked behind the left ear | Her own left (right-hand side of a front view); same side as R01 | [ ] |
| L7 | Skin tone `#DDB38E` family, one shadow shape | The same in every image: not lighter, not darker | [ ] |
| L8 | About seven and a half heads tall; average-to-slim; natural legs; soft shoulders | Model-style long legs fail | [ ] |
| L9 | Colour-wheel earrings: twelve muted segments, about a quarter of the face width, no text | Count the wedges at 200 percent. A muted wheel with the wrong count is an **E** (the hand-finishing redraws it anyway); missing, a saturated rainbow, or letters on it is a reject | [ ] |
| L10 | One persimmon accent per outfit, about one tenth of the frame | One item only (neckerchief in A and V2, tote in B, sneakers in C, parasol trim in V1, scarf end stripes in V3). Fail if clearly more than about a fifth of the clothing, or if a second orange item appears. The six muted chip cards and the earring wheel are not counted as orange items | [ ] |
| L11 | Chip ring of six blank cards, clipped, not held | Exactly six; no text or codes on the cards | [ ] |
| L12 | Variable-weight brush line over flat fills; no gradient, texture, glow or 3D | | [ ] |
| L13 | Palette only from bible 4.4 | See 5.4 | [ ] |
| L14 | No text, logo, tag, brand pattern or readable label anywhere | | [ ] |
| L15 | Hands hidden, or the fixed mitten-hand asset; no detailed fingers | | [ ] |
| L16 | Adult reading (bible 4.7) | Same as A1 | [ ] |
| L17 | **Wardrobe lock:** the outfit is exactly one of A, B, C, V1, V2, V3 as listed in bible 4.3 | No new outfit without a bible revision | [ ] |
| L18 | No head-to-toe white or black; no all-red | | [ ] |
| L19 | Not wearing the lesson outfit: lesson garments are flats or on the dress form | Not applicable to reference images (tick N/A); it matters when lessons are built | [ ] |
| L20 | Provenance row written and look-alike check ID logged | The ID stays "pending" until section 6 is done | [ ] |

### 5.3 Regenerate, edit the prompt, edit the picture, or stop?

| Situation | Do this |
|---|---|
| One of the four has the defect and the others do not | **R**: it is random. Choose another |
| The same defect appears in 2 or more of 4 | **P**: the prompt is not stopping it. Add the matching fix phrase from section 9 at the end and generate 4 more |
| An otherwise perfect image has one small local flaw (a stray mark, a wrong segment count in the earring, a slight colour cast, the wrong background shade, the tucked-back ear on the wrong side) | **E**: fix in an image editor (for the ear side, flip the whole image left-to-right). Never use E for fingers, face shape, age read or proportions. Log it as a human edit and keep the untouched file as its parent |
| The same defect after two rounds (8 images) in one tool | Try the other tool with the same prompt. If both fail, **X** |
| The thumbnail reads young, the age guess fails, or a look-alike is named | **X**: stop and tell Claude. Do not repair it with edits |

### 5.4 Colour check: hex, RGB and an allowed range

The bible says hex values in prompts are guidance and that generators drift (4.4, 5.7 step 12): a generator's hue is never trusted, exact fills are set by hex in the editor, and the result is viewed on two screens. Sample a **flat patch** (not an edge, not the one shadow shape) from the downloaded file with any colour picker and read the red, green and blue numbers. The "OK range" is **my suggestion, not a bible rule** (assumption, to calibrate after the first session): within 10 on each of red, green and blue. A same-direction shift of 10 on all three channels (a little lighter or darker) is a colour distance of about 4 to 5 on the scale in `personas/README.md` section 5, which is hard to see; a mixed shift (red up, blue down) at the edge of the range can reach about 13 to 17, a visible change of hue. So the range is a first filter, and your eye beside the swatch is the second. Inside range: pass. Off by 11 to about 25 on any channel: fix the colour in post and note it. Off by more, or visibly a different colour (a red or yellow-orange persimmon, a grey blush): regenerate or edit the prompt.

| Used for | Colour | Hex | R, G, B | OK red | OK green | OK blue |
|---|---|---|---|---|---|---|
| Ground (backgrounds) | Pale peach-blush 淡蜜桃色 | `#F2DAD2` | 242, 218, 210 | 232 to 252 | 208 to 228 | 200 to 220 |
| Tops, shirts, tee, scarf, eye highlight | Cream 奶油白 | `#F4E8DF` | 244, 232, 223 | 234 to 254 | 222 to 242 | 213 to 233 |
| Line, trousers, shoes, vest, coat, type | Charcoal 炭灰 | `#3A3735` | 58, 55, 53 | 48 to 68 | 45 to 65 | 43 to 63 |
| Blazer, skirt, trousers, jacket | Warm stone 暖灰 | `#B8AEA2` | 184, 174, 162 | 174 to 194 | 164 to 184 | 152 to 172 |
| The one accent | Persimmon 柿子橘 | `#CD8B6A` | 205, 139, 106 | 195 to 215 | 129 to 149 | 96 to 116 |
| Chip-card tint | Persimmon tint | `#E6BBA3` | 230, 187, 163 | 220 to 240 | 177 to 197 | 153 to 173 |
| Chip-card tint | Mist | `#E4D6CB` | 228, 214, 203 | 218 to 238 | 204 to 224 | 193 to 213 |
| Hair, brows | Dark umber | `#2F2A28` | 47, 42, 40 | 37 to 57 | 32 to 52 | 30 to 50 |
| Skin | Warm medium | `#DDB38E` | 221, 179, 142 | 211 to 231 | 169 to 189 | 132 to 152 |
| Skin, one shadow shape | Skin shadow | `#C4946C` | 196, 148, 108 | 186 to 206 | 138 to 158 | 98 to 118 |
| Mouth | Muted terracotta-brown | `#B27A6C` | 178, 122, 108 | 168 to 188 | 112 to 132 | 98 to 118 |

- The ground `#F2DAD2` and the garment cream `#F4E8DF` are only about 6 apart, so their ranges overlap a little. A background whose green is above about 225 and blue above about 216 is the old cream ground: fix it in post. The ground is the pinker of the two.
- The twelve wheel colours are too small to sample. Check the earring by eye against the order in the prompt: red, red-orange, orange (the persimmon), yellow-orange, yellow, yellow-green, green, blue-green, blue, blue-violet, violet, red-violet, all dusty and muted, none a saturated spectrum.
- The eyes, brows and mouth are too small to sample reliably: check by eye that they are a dark warm grey, not pure black.
- When the swatch chart (R17) exists, hold the picture beside it as well.

---

## 6. The two human tests, and the reverse-image search

The bible requires both tests on the master before it is final (adult-reading panel, 4.7 item 5; look-alike check, 5.7). They need other people, so they usually happen on a different day from the generating. The people are helping you test a design; they do not follow, like, comment on or share anything, and they should not pass the pictures on. Tell them afterwards what the pictures were for.

### 6.1 Age-guess test (adult-reading check)

1. For each shortlisted sheet (up to three), crop the front full-body view and the large head-and-shoulders view as separate files. Save them in `candidates` (for example `R01_cand_gemini_2_front-crop.png`) and log each as a human edit (crop) of its parent. Make a thumbnail copy of each: the figure about 110 pixels tall, the head-and-shoulders view about 96 pixels. Hide or remove file names.
2. Find the wife plus 2 or 3 trusted people (3 or 4 in all). Show each person the pictures **alone, one at a time, in a different random order for each person, with no context**: do not say it is an AI character, a mascot, an illustration for a studio or a character for a social-media account. The wife already knows what it is; ask her anyway, first, without discussion, and record it.
3. Ask only: **"How old would you say she is, and what might she do for a living?"** Write down the number they say, exactly. If they refuse to guess, ask for a range and write that. Write down any word like "student" or "teenager".
4. Do the same with the thumbnail copies, at the end.
5. **Pass** only if nobody guesses under 25 and nobody says "student" or "teenager" (bible 4.7 item 5; the pass rule is the bible's assumption). **Fail** otherwise: the image is not used. Write it in the log.
6. If every shortlisted image fails, or the common comment is "young" or "cute", do not fix it by editing: tell Claude (a design change goes through a bible revision and the wife's re-approval, bible 5.7 step 11).
7. Record answers in the language they were given; the wife adds an English gloss.

### 6.2 Look-alike blind test

1. Same people and same set-up as 6.1, shown the same way (the full-size images, one at a time).
2. Ask only the bible's question: **"Does this remind you of any real person (a model, actress, singer or online creator), a virtual streamer, a mascot or a cartoon character?"** Write the answer word for word. If the answer is yes, ask who or which, and write the name.
3. **Pass** if nobody names a real person or an existing character. Words like "a fashion illustration" or "anime in general" are notes, not names; write them down anyway. **Fail** if anyone names a specific real person or a specific existing character.
4. A named person or character: do not argue with it and do not "fix" it by editing. Search that name yourself in a normal image search, compare it with your picture by eye at the same size, write what you see, and tell Claude. The bible's remedy is to redesign the feature, or to document why it is coincidence and ask the lawyer (bible 5.7 step 4; legal.md question 20).

### 6.3 Reverse-image search (manual, public tools only)

Do this for each shortlisted image, on your own computer, by hand, logged out of any personal accounts.

1. Make clean copies: the whole sheet, the front full-body view, the head-and-shoulders view, and a crop of the ear with the earring (the signature tell). No borders, no text. The bible says to search the master and three variants.
2. Use **at least two** public reverse-image search tools. Examples, whichever are currently available: Google Lens, Bing Visual Search, TinEye. Open each tool's web page and upload the picture yourself. Do not use scripts, bots or scraping, and do not log in anywhere just for this; no scraping behind logins (Ground rule 9). Uploading sends your picture to that service, which is acceptable for a design that has not launched but worth a note in your log.
3. Look at the first one or two pages of visual matches. Write down anything that is a close match: an illustrated character, a fashion-illustration avatar, a brand or shop mascot, a LINE sticker character, a logo, an influencer's illustration. Screenshot the result pages into `assets/sehuan/lookalike/` with names like `R01_cand_gemini_2_tineye_2026-10-11.png`. Record date, tool and top matches.
4. Then run **text searches** in the same tools' image results for the signature combination, to see whether another character or brand already uses a colour-wheel earring on an illustrated woman. English: "colour wheel earrings illustrated woman", "colour wheel earring character", "fashion illustration character colour wheel earrings". Ask the wife to run the Chinese ones (an AI draft, she adjusts): 「色環 耳環 插畫」, 「色環耳環 虛擬角色」, 「配色 穿搭 插畫角色」. Compare what you see with your picture by eye.
5. **Named-comparison list** (bible 5.7 step 3). Search each name in a normal image search, look at the first page of results, and compare with your shortlist at the same size. The virtual fashion characters named in `research/competitors.md`: Imma, Ria, Noonoouri, Lil Miquela, Aitana, Thalasya, 柳夜熙 (Liu Yexi). The Taiwan characters named in the research: OPEN將, 虎妮, 光音凱伶, 杏仁咪嚕. Also LINE sticker characters, and any fashion-brand mascot your searches turn up. **These names are for searching and comparing by eye only. Never paste any of them into an image prompt, and never upload anything of theirs to Gemini or ChatGPT.** The studio's other nine concepts (portfolio.md 2D) are also on the bible's list, but no reference images exist for them yet, so compare only their written looks for now and repeat this step when images exist. Ask the wife about any name or account you do not recognise.
6. **Pass** if search and panel report no match and the named comparison shows no similarity. If a very close match turns up: do not use the image and tell Claude.
7. Re-run before launch, at the week-6 review and after any complaint (bible 5.7). A credible look-alike claim after launch means take the post down within 24 hours (portfolio.md 6.2).

Searching the name 色環 itself (existing shops, accounts and trademarks) is a different gate (bible G3: the wife's reading test and the TIPO and business-name searches) and is not part of this test.

### 6.4 The log to keep (ready to fill)

Bible 5.7 puts this in `personas/sehuan/lookalike_log.md`, created in Phase 4. Until then keep it in your notes and give it to Claude. Use one check ID per candidate set: LA-001 for the first, LA-002 for the next. Write that ID in `licence_notes` for the files it covers.

| Check ID | Date | Candidate or asset | Tools and searches (tool, date, queries) | Search result | Blind-test result (verbatim) | Age guesses | Verdict | Checked by |
|---|---|---|---|---|---|---|---|---|
| LA-001 | | | | | | | | |

Age-guess tally (one row per person; "Under 25 or student?" is yes if the guess is below 25 or the word student or teenager was used):

| Person (initials) | Full-size guess | Thumbnail guess | Job guess | Under 25 or student? | "Reminds me of" (verbatim) |
|---|---|---|---|---|---|
| Wife | | | | | |
| | | | | | |
| | | | | | |

---

## 7. Provenance: log every asset

The rule (BRIEF Ground rule 2; bible 5.7 and 5.9): **every kept file and every discarded-but-considered file gets one row in `assets/provenance.csv`, the same day.** "Considered" means you saved it, compared it, shortlisted it or used it as a reference. Obvious failures you did not save need no row, but save anything you looked at for more than a glance. Human-made files (crops, flipped or colour-fixed versions, hand-finished masters, the swatch chart) get rows too, naming their parent file. A copy of a candidate saved under its pack name (for example `R01_master_v1.png`) is its own row, with the candidate as its parent.

### 7.1 Columns and a ready-to-fill example

Columns, in order: `timestamp,asset_path,persona,tool,model,prompt,licence_notes`.

- `timestamp`: Taiwan time (+08:00), the time you generated the image.
- `asset_path`: path from the project folder, for example `assets/sehuan/R01_master_v1.png`.
- `persona`: `sehuan` (the bible's placeholder slug until the real handle is chosen).
- `tool`: for example "Gemini (app)" or "ChatGPT (app)". Write what you actually used.
- `model`: the model or version label **exactly as the app shows it that day**. If the app shows none, write "not shown in app, YYYY-MM-DD". Do not guess one.
- `prompt`: the **full text you sent**, including the Character Lock if you used it, and a note of which files were attached. If you changed even one word, log the changed text.
- `licence_notes`: use the template in 7.3.

For a manual step in an editor (a crop, a flip, a colour fix, the hand-finishing), `tool` is the editor's name as shown, `model` is `n/a`, `prompt` describes the edit in a sentence, and `licence_notes` names the parent file and says "human edit".

This is an **example only**. Copy only the second line into the real file, and only after replacing every `<...>` with the real value. The header line is already in the file.

```
timestamp,asset_path,persona,tool,model,prompt,licence_notes
2026-10-11T14:05:00+08:00,assets/sehuan/R01_master_v1.png,sehuan,"Gemini (app)","<model label exactly as shown in the app today>","<PASTE THE FULL PROMPT EXACTLY AS SENT. Attached files: none.>","Status: KEPT (provisional master); reason: best of 4, passed checklist; parent file: assets/sehuan/candidates/R01_cand_gemini_2.png; reference images attached: none; human edits: none (raw); prompt ID: R01-Gemini; tool plan: <plan name shown in my account>; terms read on <YYYY-MM-DD> at <page name or link>; commercial use per those terms: NOT YET CHECKED; watermark or label on file: <none seen | describe>; conversation link or ID: <link>; seed: none shown; look-alike check LA-001 pending"
```

### 7.2 Rules that keep the file valid

- One row per file. A kept file and the candidates around it each get their own row.
- The easiest way to avoid broken quotes: edit the CSV in a spreadsheet app and paste each field into its own cell; the app adds the quotes and handles commas, line breaks and double quotes. If you edit it as plain text, put every field that contains a comma, a line break or a quote in double quotes, and double every quote mark inside it. Save as CSV (UTF-8 if offered).
- A long prompt in one cell is fine. For a batch of images made from the same prompt, copy the prompt cell down.
- Do not edit or delete old rows. Corrections go in a new row.
- Other people may be adding rows to the same file for other characters. Add yours at the bottom and do not change theirs.
- You can also paste your notes (file names, tool, model label, time, which prompt, any wording you changed) to Claude Code and ask it to write the rows. Claude cannot see your screen, so it needs the model label and the time from you, and it must use the exact text you sent.

### 7.3 `licence_notes` template (fill the blanks)

```
Status: ___ (KEPT | KEPT (provisional master) | DISCARDED-CONSIDERED); reason: ___; parent file: ___ (none (raw download) | file name); reference images attached: ___ (none | R01_master_v1.png ...); human edits: ___ (none (raw) | crop | flip | colour fix | earring or ring redrawn | other); prompt ID: ___ (for example R02); tool plan: ___ (the plan name shown in my account); terms read on ___ (date) at ___ (page name or link); commercial use per those terms: ___ (CONFIRMED | NOT CONFIRMED | RESTRICTED: what); watermark or label on file: ___ (none seen | describe); conversation link or ID: ___; seed: ___ (none shown | number); look-alike check: ___ (LA-00x pending | LA-00x passed on date | LA-00x failed)
```

Before any commercial use, read the **current** terms for the tool and plan used (the terms of service and any content or image policy the app links to) and fill in the "terms read" and "commercial use" blanks from what they actually say. Questions worth looking for in them: whether images made on your plan may be used commercially; whether any credit, label or watermark is required; any limits on using the output as a recurring character or brand asset; and whether the answer is different for the app and for a developer interface. Terms differ between tools, between plans and over time. If anything is unclear, write NOT CONFIRMED and keep the image internal. Whether AI-generated images can be protected by copyright is an open question for the lawyer (`research/legal.md` section 8.2); hand-finishing the master, with the layered file kept, is how the studio documents its own human contribution.

---

## 8. A note for the wife

Thank you for looking at these. You are judging **language, culture and how it feels**, not the technology. The operator checks hands, proportions and numbers. Please look at each picture the way a Taiwanese viewer scrolling Instagram would, and say **APPROVE**, **SMALL FIX** or **REJECT** with a short reason. If you are not sure, say "unsure" and why. Reason codes (from the bible, 10.1): **X** cultural or visual error, **S** script or font problem, **P** politics or sensitive colour, **T** tone. Allow about 15 to 20 minutes for a shortlist of three. The zh-TW words below are an AI draft; please correct them freely.

You do not need any fashion knowledge (the bible says so). The operator's fashion contacts, not you, are the check on fashion facts.

| # | Look at | zh-TW words to look for | Your answer |
|---|---|---|---|
| 1 | Does she look like a **grown-up**, about 30? The risk is that a cute illustration looks like a student or a younger girl | 成熟、穩重、三十歲左右 (good) / 孩子氣、像學生、童顏、太年輕、太可愛 (not good) | |
| 2 | Is the face **natural and ordinary**, like a woman you could meet in Taiwan? Or does it look like a template? Also: should the words "that read as Taiwanese" stay in the prompt, or be dropped? (bible open item 5) | 自然、像一般人 (good) / 偶像臉、韓系偶像感、日系動漫感、網美臉、過度精緻 (not good) | |
| 3 | Does she **remind you of anyone or anything that already exists**? Please write the name. | 像哪個明星、模特兒、網紅、虛擬網紅、吉祥物、卡通角色、LINE 貼圖？ | |
| 4 | **Colour impression** at small size. Any political or party feeling? Does the earring look like a rainbow flag? Anything all black or all white? | 藍綠、藍白、綠白、黃色的政黨聯想；橘色會不會像政黨色；彩虹旗聯想；全黑、全白 (喪事色) | |
| 5 | The **pale blush background** `#F2DAD2`. Too pink or childish? Does it look like skin colour? Is 淡蜜桃色 a natural name? For the accent, which sounds natural: 柿子橘、柿橘 or 柿色? | 太粉、幼稚、少女感、像膚色 (not good) / 柔和、自然 (good) | |
| 6 | **Clothes.** Do they look like adult everyday or work clothes? Does the shirt, vest and skirt (outfit B) feel like a school uniform? Too short or too revealing? | 上班穿搭、日常穿搭 (good) / 制服感、學生裝、太短、太露 (not good) | |
| 7 | **Any writing** on the picture. There should be none. Also any logo or brand mark on clothes, bags or shoes | 文字、數字、簡體字、亂碼、日文或港式字形；商標、品牌標誌、車牌 | |
| 8 | **Taiwan details** (only for the library pictures R13) | 騎樓 (連續的騎樓、方形柱子、磁磚地板、停放的機車、鐵捲門)；公車候車亭 (右側行駛、車門在右邊)；捷運出口 (沒有路線圖和站名)；百貨公司；辦公室冷氣房 (扁形插座)；便利商店 (有座位區、不像日本)；玄關和陽台 (脫鞋、鞋櫃、鐵窗、冷氣室外機、除濕機)；喜宴廳 (圓桌、轉盤、紅色背板)；商圈街景；住宅巷弄 (電線、鐵窗、水塔)。季節感：濕冷、梅雨、悶熱、常綠，不要楓葉、雪、羽絨外套 | |
| 9 | **Expressions** (R03). Do the ten faces feel natural, calm and adult, not cute, flirty or over-acted? Is the polite decline polite, and not cold or angry? | 平靜、說明、提醒注意、比較、微笑、不確定、謹慎、更正、輕鬆愉快、婉拒 / 撒嬌、嫵媚、冷淡、生氣 (not good) | |
| 10 | **Poses** (R04). Anything that feels sexy, stiff or odd for this kind of account? | 姿勢自然、站姿端正 (good) / 擺姿勢、刻意、性感 (not good) | |
| 11 | **Skin tone.** Only tell us if it looks different from one picture to the next. (The studio never talks about skin tone in public posts.) | 膚色一致 / 忽深忽淺 | |
| 12 | Anything else that feels **wrong for a Taiwan audience** | 文化上怪怪的、不適合台灣觀眾 | |

Not needed from you: hex numbers, finger counts, proportions, whether it is "good AI", or the name 色環 (that is a separate reading test, bible gate G3; the questions are in the bible, section 10.2).

---

## 9. Common failure modes for this character, and fixes

These come from the bible's spec, Avoid list, adult-reading check and review notes. The top risks for this character are: (1) a generic, pretty illustration that reads younger than 25 or like an idol or anime heroine; (2) the signature earring and chip ring coming out wrong or turning into a rainbow; (3) outfit B reading as a school uniform; (4) drift in skin tone, hair side and the single persimmon accent. Only the age-guess and blind tests (section 6) clear the first one. To use a fix phrase: add it at the end of the prompt (after the Character Lock and the prompt), generate 4, and see whether the defect is gone from at least 3 of them. In the same chat you can instead say "Same image, but: <phrase>" for a small fix.

| Symptom | Likely cause (hypothesis) | Fix phrase |
|---|---|---|
| Photo-like, glossy, 3D or airbrushed; soft shading; fabric or skin texture | Generators default to polished renders | `Flat illustration only: flat colour fields with a loose ink-brush outline whose weight varies from thin to thick, fills sitting very slightly off the line. No gradients, no airbrushing, no soft shadows, no skin pores, no fabric texture, no 3D, no glow, not a photograph.` |
| Looks young, cute, idol-like or anime: big glossy eyes, blush, small chin, round cheeks | Cute-character default | `An adult woman of about thirty: long-oval face with softly defined cheekbones and a jaw shadow, almond eyes of modest size (each about one fifth of the face width), straight medium-thickness brows, no blush marks, no freckles, no eye makeup, no gloss, no sparkle. Not anime, not chibi, not an idol template.` |
| Model proportions: very long legs, tiny waist, exaggerated hips or bust | Fashion-illustration default (the bible's reason for natural legs: a long croquis signals an idealised body) | `About seven and a half heads tall with natural, not elongated, legs; average-to-slim build; natural soft shoulders; relaxed upright posture; no exaggerated waist, bust or hips.` |
| Earring wrong: rainbow or saturated stripes, a plain disc, letters or numbers, too small, one colour, missing on the visible ear | "Colour wheel" pulls toward a rainbow spectrum | `Round drop earrings shaped like a colour wheel: twelve equal wedge segments in dusty, muted colours, not a saturated rainbow, about one quarter of the face width, no numbers, no letters, no stripes. The earring on the left ear is fully visible with the hair tucked behind the ear.` Count the wedges; if only the count is off, fix in the editor (E). |
| Chip ring wrong: more or fewer than six cards, held in a hand, text or codes on the cards | An unusual prop | `A ring of exactly six blank rectangular colour-chip cards in muted tints, clipped to the belt loop (or the bag strap), never held in a hand. No text, no numbers and no codes on the cards.` |
| Too much orange, a second orange item, or the accent turns bright orange or red | The accent is over-applied | `Exactly one persimmon accent (#CD8B6A, a soft muted terracotta-orange) covering about one tenth of the visible clothing; every other garment is cream, warm stone grey or charcoal.` |
| Hair wrong: dyed or colour-block, ponytail, bangs, curls, covers the ear, tucked behind the wrong ear | "Tucked behind the left ear" read loosely | `Natural dark brown-black shoulder-length blunt-cut hair with a side parting, tucked behind the left ear so the ear and the earring are visible. Flat colour plus one lighter highlight shape. No dyed or colour-block hair, no ponytail, no braids, no hair clips.` |
| Hands: detailed fingers, a hand in the hair, hands holding things | Generators love hands | `Hands hidden in the blazer pockets, or drawn as simple flat mitten shapes with a separate thumb: no detailed fingers, no knuckles, no fingernails.` |
| Logos, tags, monograms, stripes, checks or patterns on clothes or props; a bag or shoe that resembles a real brand | Fashion prompts attract branding | `Plain clothing with no logos, no monograms, no tags, no labels, no text, no stripes, no checks, no patterns, no brand-like details; simple seams only. Generic design that copies no brand.` |
| School-uniform read in outfit B (collared shirt, vest, skirt): a tie or bow, pleats, knee socks, a short skirt | Shirt plus vest plus skirt is a uniform cue | `Relaxed adult workwear cut: shirt collar open at the neck, sleeves rolled to the elbow, no tie, no bow, no pleats; the midi skirt ends below the knee; no knee socks; not a school uniform.` If the age panel still says "student", tell Claude (X). |
| Expert costume or props: tape measure, scissors, clipboard, lanyard, badge, apron, stylist or tailor look | A "colour expert" association (the tape measure belongs to another character) | `No tape measure, no scissors, no clipboard, no lanyard, no badge, no apron, no professional uniform. Her only extras are the earrings, the persimmon accent and the ring of blank colour-chip cards.` |
| Background not pale blush: white, cream, grey, gradient, a studio shadow, a scene | Not forced strongly enough | `Plain flat pale-blush background (#F2DAD2): not white, not cream, not grey, no gradient, no texture, no cast shadow, nothing else in the picture.` |
| Colours drift: a saturated blue, green, teal or yellow; neon; the persimmon turns red | Hex values are only hints | `Muted palette only: pale blush #F2DAD2, cream #F4E8DF, charcoal #3A3735, warm stone grey #B8AEA2 and one persimmon #CD8B6A accent. No saturated blue, green, teal or yellow, nothing neon.` |
| Skin tone changes between images (paler, tanned) or gets blush | Drift | `Skin is one flat warm medium tone (#DDB38E) with one shadow shape (#C4946C), identical to Image 1: not lightened, not darkened, no blush.` |
| Text appears: "FRONT" and "BACK" labels, captions, invented Chinese, a signature, numbers on the chip cards | Sheets tempt labelling | `The picture contains no text of any kind: no labels, no captions, no letters, no numerals, no Chinese characters, no signature, no watermark.` Any text fails the image even if it looks right. |
| Sheet problems: views do not match, a view is missing, feet cropped, extra figures, one big figure instead of a sheet | Many views in one image is hard | Generate each view as its own image (R02, then R04) with R01 attached. Add `All views show exactly the same single woman at the same scale and eye-line.` For the sheet itself add: `This is a character reference sheet with four full-body views side by side and one large head-and-shoulders view.` |
| Expressions over-acted: a grin, teeth, a wink, tears, a pout, a tongue; E10 looks cold or angry | Expression words get over-acted | `Expressions are small and calm: only the brows, eyes and the mouth line change slightly. No wide grin, no teeth, no tears, no anger, no wink, no pout, no tongue.` |
| Poses: hips thrown out, a hand in the hair, a body-emphasising angle, a raised open palm | Fashion-pose default | `A natural, relaxed, upright pose; no model pose with hips thrown out, no hand in the hair, no raised open palm, nothing that emphasises the body.` |
| Seasonal sheets: snow, autumn leaves, a puffer coat in V3; V1 looks like beachwear; V2 hood up | Four-season defaults | V3: `Taiwan climate: damp, overcast, mild cold; no snow, no autumn leaves, no puffer coat.` V1: `Light everyday summer clothing, not beachwear.` V2: `The hood is down.` |
| The earring side or the tucked-back ear flips between images | Left and right are weak instructions | New chat, attach only R01, add `The earring and the tucked-back ear are on the same side as in Image 1.` Or flip the picture in the editor (E). |
| Library pictures: a dress form with a face or head, flats with logos, tags or wrinkles; plates with riders, legible plates, signs with text, MRT maps, left-hand traffic, Western arcades | Scene defaults | Dress form: `No face, no hair, no head detail, simple neck cap.` Flats: `No logos, tags, labels, text, pattern or embossing.` Plates: `All signs, banners and screens are left blank; no people, no riders, no helmets, no legible numbers or plates; right-hand traffic.` |
| The face drifts further from R01 with each new picture | Building on the last output | New chat, attach only R01, resend. Never use a new output as the only reference twice in a row. |
| The long Avoid list makes the app draw the things it names (a flag, a rainbow, a logo) | Naming a thing can summon it (hypothesis) | Use the short fallback below instead of the long list. |
| She reminds someone of a real person or a known character, or the thumbnail reads young, or the age guess fails | The design itself, not a prompt problem | **X**: tell Claude. Do not edit around it. |

**Short Avoid fallback (only if the long list backfires).** Every item is taken from the bible's Avoid list.

```
Avoid: text, letters, numerals, logos, watermarks; photorealism, 3D render, anime, chibi or kawaii proportions, large glossy eyes, blush, child-like features; school uniform, short skirt, sexualised pose, exaggerated or idealised body, elongated legs, detailed fingers; gradients, airbrush, soft shadow; saturated blue, saturated green, saturated teal, saturated yellow, rainbow stripes, flags; any resemblance to a real person or an existing character.
```

---

## 10. When you stop for the day

Tell Claude: which tool made the chosen R01 and the model label shown; which side R01 shows the tucked-back ear on; which images you kept and discarded; the minutes you spent; which checklist rows failed most often; whether any tool refused a prompt; and what the wife said (including her answer on "that read as Taiwanese" and on the blush background). Claude can then update the bible's status and provenance notes, record the tool test in `pipeline/tools.md` (Phase 4), write the `licence_notes`-ready rows from your notes, and set up the next sitting.

Nothing from this pack is approved until the age-guess test, the look-alike blind test and reverse-image search, the hand-finishing of the master (earring wheel and chip ring redrawn by hand, the fixed mitten-hand asset, a layered file kept) and the approvals by the wife and operator are done. The name 色環, the handle and the studio name are still unchecked and are not part of this session. Do not post any of these pictures anywhere before the gates in the bible (section 1.2) are met.
