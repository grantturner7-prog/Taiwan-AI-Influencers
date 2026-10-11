# 步驟 (buzhou): image pack, version 1

Written 2026-10-11 from `personas/buzhou/bible.md` (v0.1 DRAFT: sections 4, 5, 7, the review log and the integration log) and `BRIEF.md` section 3. Nothing has been generated yet: no reference image exists.

**How to read this pack**

- Text inside a grey code block is for copy and paste. Everything else is for you to read.
- Each prompt says where it came from. **Bible, verbatim** means copied from the bible without change. **Pack wording** means I wrote it from the bible's specification (hex colours, outfit pieces, pose and expression lists) so it is ready to use. If the bible and this pack ever disagree, the bible wins.
- **Hypothesis** means I believe it but have not checked it. Image tools change their menus, model names and limits often. **Check the current UI** before relying on any statement about what a tool can do.
- The character's name and the working folder name `buzhou` are placeholders until the handle check is done (bible 2.2). File names in this pack therefore use short ID codes (R01, R02 ...) so nothing has to be renamed later.
- **Nothing made with this pack may be published, posted or sold until the licence check in section 1 and section 7 is done and written down.** Making test images today is fine.

---

## 0. One-screen summary

**Who the character is.** 步驟 (working name `buzhou`, Chinese for "steps") is an openly-AI character for a YouTube Shorts and Threads channel that explains AI tools in three steps or fewer. It stands as a small picture in the corner of screen recordings that a real person at the studio makes, so it has to be flat, simple and readable even when tiny. It is drawn as a calm adult (design age 28, gender not stated): long oval head with a defined angular jaw, short neat dark side-parted hair, matte charcoal over-ear headphones with no cable, a boxy light-grey jacket over a dark blue-grey tee, charcoal trousers, and a small patch on the left chest showing a staircase of six squares that rises to the right. The whole look is flat colour shapes with no outlines in muted blue-greys. It must read as clearly adult, clearly a drawing (not a photo), and not like any real person or existing character.

**What the first session should achieve.** You leave with (1) one chosen master image, R01, that passes the checklist in section 5; (2) a first age-guess and look-alike check on it, started with the wife; (3) the first "lock-in" images made from it (face sheet R02 and the two small corner busts R07); and (4) every image saved and logged in `assets/provenance.csv`. Expressions, poses, outfits and props come in the next sittings.

**Time estimate (my estimate, an assumption, not measured).**

| Part | Who | Minutes |
|---|---|---|
| Set-up: folders, one new chat per tool, log sheet ready | You | 10 |
| STEP 1: R01, 4 variations in each tool, saved | You | 30 |
| Choose: shortlist, blind pick with the wife | You, wife | 20 |
| Test the winner: checklist, shrink test (R08), age-guess, quick reverse-image search | You, wife | 40 |
| STEP 2: R02 face sheet, R07 corner busts | You | 30 to 40 |
| Logging while you go | You | 20 to 30 |
| **Today, total** | | **about 2.5 to 3 hours**, wife about 30 to 40 minutes |
| Next sitting: R03 expressions, R04 poses | You | about 1.5 hours |
| Later sittings: R05 outfits, R06 props, R10 settings, R11 avatar and banner, R12 and R13 by hand | You | about 2 hours |

**Order of work**

1. Section 1, then set up folders (section 2.1).
2. STEP 1: generate R01 in Gemini and in ChatGPT (section 2).
3. Choose the best, run the checklist (section 5) and the quick tests (section 6).
4. STEP 2: continue only in the tool that made the winner (section 3): R02, then R07.
5. Next sitting: R03 expressions and R04 poses (section 4).
6. Later: R05, R06, R10, R11, R12, R13 (section 3). R09 only if the studio decides to use a voice.
7. Before anything is used for real: the full panel and named-comparison look-alike check (section 6), the hand-finish of the master (bible 5.7 step 2), and the licence record (section 7).

---

## 1. Before you start (5 bullets)

1. **Which tool to start with, and why (hypothesis).** Start with **Gemini**, then run the same R01 in **ChatGPT** as a second opinion (about 10 extra minutes for 8 candidates instead of 4). Why Gemini first: the bible's Gemini prompt is written for a conversational "generate, then ask for one change at a time" flow (bible 5.2), which is the easiest way to learn how this character behaves. The bible's guess for ChatGPT is structured prompts, reference images and a region-edit mode for fixing one wrong detail (bible 5.3). Both guesses are unverified; if ChatGPT is the one you find easier, start there. Once you pick a winner, do **all** the follow-up images in the tool that made it, in a fresh chat for each, because mixing tools for one character is likely to cause drift (also a hypothesis). If you hit a usage limit, wait rather than switching tools in the middle of a set.
2. **Settings to look for, if available (check the current UI).** Aspect ratio: wide landscape (3:2 or 16:9) for sheets, square (1:1) for single busts and the avatar. Number of images per request: set it to 4. If neither is offered, the prompts end with an `OUTPUT:` line that asks in words, and you press "regenerate" or send the same prompt again until you have 4 separate images (do not ask for "four images in one picture"). Also look for: highest resolution or quality, an attach or upload button, an edit or select-region mode, and where the model name is shown (you will copy it into the log).
3. **Never upload a photo of a real person.** Not yourself, not your wife, not a friend, not a celebrity, not a stock photo, and not a screenshot or fan art of any existing character or mascot. The only images you may ever upload are the studio's own generated character images (R01_master_v1.png and later approved files) and plain colour swatches. Never type "in the style of" followed by a living artist, studio or character into any prompt; describe the look in plain words instead (flat, geometric, outline-free).
4. **Save everything, log everything.** Use the tool's download button, not a screenshot (a screenshot loses quality and any embedded information). Do not convert, crop or strip metadata; if a tool adds a visible or invisible mark, leave it and note it in the log (unverified whether any is added; bible 5.2). Save every image you generate, kept or not, into `assets/buzhou/` (keepers) or `assets/buzhou/candidates/` (everything else; create this folder), and add one row per image to `assets/provenance.csv` (section 7). Copy the tool name and model name from the screen, never from memory.
5. **Licence terms have NOT been checked.** Before any commercial use, read the **current** terms for the exact tool and plan you used (Gemini and/or ChatGPT, on your plan) and write the result into the `licence_notes` column (template in section 7). Commercial use means anything posted, published, shown to a client or sold. Until that is recorded, treat every image as "for internal review only". Do not crop out or remove a tool's own mark or watermark until you have read what its terms say about that.

---

## 2. STEP 1: the master reference R01

### 2.1 Prepare

- Make a sub-folder `assets/buzhou/candidates/` (in your file manager: open `assets/buzhou`, right-click, New Folder, name it `candidates`; or ask Claude in this project folder to create it).
- In each tool, open a **new chat** and give it a name you will recognise, for example "buzhou R01".
- Keep this file open next to the chat. You copy a block, paste it, and press send.

### 2.2 Gemini prompt for R01

Source: **bible 5.2 first turn, followed by the Style, Character, Face, Skin, Hair, Outfit A, Signature details, Layout and Avoid paragraphs of bible 5.1, verbatim** (the bible says to paste exactly those paragraphs; the opening paragraph of 5.1 is not included for Gemini because the first lines already say "original").

```
I'm designing an original, clearly adult virtual character for a studio. Please generate one
reference sheet image using the specification below. After I choose a result, I'll ask for edits.
Keep every locked feature identical unless I say otherwise. Do not put any text, letters or logos
anywhere in the image.

Style: flat vector illustration, outline-free, built from clean geometric planes. Every form is one
flat colour plus at most one flat shadow shape. No gradients, no textures, no outlines, no glow, no
3D, no photographic detail. Crisp edges. Adult proportions, about seven heads tall.

Character: a clearly adult person-like character, stated age 28, gender not specified (neutral
presentation, can be read either way). Tall, slim-to-average build, slightly broad shoulders,
rectangular torso, upright relaxed posture. Hands hidden in jacket pockets.

Face: long oval head, defined angular jaw, visible neck and ears, high straight eyebrows,
almond-shaped dark eyes of modest size (each about one fifth of the face width) in flat #2B3038
with one small highlight, eyebrows flat #2B3038, a simple wedge-shaped nose shadow in #BE9371, a
calm closed mouth (flat #BE9371 shape) with a very slight asymmetric smile. No blush marks, no
freckles, no makeup emphasis.

Skin: flat warm medium beige #D8B190 with shadow shapes #BE9371.
Hair: short, neat, side-parted, flat charcoal #2B3038 with one lighter highlight shape #4A515B.

Outfit A: boxy light-grey coach jacket #C9D1DA over an ink-slate crew-neck tee #3B4A5C; charcoal
straight trousers #2B3038; plain bone sneakers #EEECE7. No logos, no text.

Signature details (always present): (1) matte charcoal over-ear headphones, generic shape, no logo,
no cable, worn on the ears; (2) a small rectangular patch on the jacket's left chest: bone #EEECE7
backing with a rising staircase of six flat squares: three bottom-aligned columns of 1, 2 and 3
squares, left to right (left column #C9D1DA, middle column #6F8197, right column #3B4A5C). The
staircase rises left to right. No 2x2 grid.

Layout: plain bone #EEECE7 background. Four full-body views in a row at identical scale and
eye-line (front, three-quarter left, side, back), plus one large head-and-shoulders view.
Neutral expression. Even flat lighting.

Avoid: text, letters, numerals, logos, watermarks, signatures, readable interface or keyboard
legends, photorealism, 3D render, anime or chibi proportions, large eyes, child-like features,
school uniform, robot or screen face, glowing circuits, lab coat, beard-and-glasses expert look,
detailed fingers, gradients, outlines, texture, sexualised pose or clothing, saturated blue,
saturated green, yellow, flag or party colours, any real person or existing character resemblance.
```

If you can set an aspect ratio, choose wide landscape (3:2 or 16:9). If not, add one more line at the end: `OUTPUT: 1 image, wide landscape (3:2).` (bible 5.3 uses the same kind of line).

### 2.3 ChatGPT prompt for R01

Source: **bible 5.1, the tool-agnostic master prompt, verbatim.** The structured ChatGPT wording in bible 5.3 needs an attached reference image, which does not exist yet, so it is used from the follow-up images onward (section 3.2). If ChatGPT answers in words instead of drawing, reply "Please generate the image now."

```
Create a character reference sheet for an ORIGINAL virtual character. It is not based on any real
person, celebrity or existing character.

Style: flat vector illustration, outline-free, built from clean geometric planes. Every form is one
flat colour plus at most one flat shadow shape. No gradients, no textures, no outlines, no glow, no
3D, no photographic detail. Crisp edges. Adult proportions, about seven heads tall.

Character: a clearly adult person-like character, stated age 28, gender not specified (neutral
presentation, can be read either way). Tall, slim-to-average build, slightly broad shoulders,
rectangular torso, upright relaxed posture. Hands hidden in jacket pockets.

Face: long oval head, defined angular jaw, visible neck and ears, high straight eyebrows,
almond-shaped dark eyes of modest size (each about one fifth of the face width) in flat #2B3038
with one small highlight, eyebrows flat #2B3038, a simple wedge-shaped nose shadow in #BE9371, a
calm closed mouth (flat #BE9371 shape) with a very slight asymmetric smile. No blush marks, no
freckles, no makeup emphasis.

Skin: flat warm medium beige #D8B190 with shadow shapes #BE9371.
Hair: short, neat, side-parted, flat charcoal #2B3038 with one lighter highlight shape #4A515B.

Outfit A: boxy light-grey coach jacket #C9D1DA over an ink-slate crew-neck tee #3B4A5C; charcoal
straight trousers #2B3038; plain bone sneakers #EEECE7. No logos, no text.

Signature details (always present): (1) matte charcoal over-ear headphones, generic shape, no logo,
no cable, worn on the ears; (2) a small rectangular patch on the jacket's left chest: bone #EEECE7
backing with a rising staircase of six flat squares: three bottom-aligned columns of 1, 2 and 3
squares, left to right (left column #C9D1DA, middle column #6F8197, right column #3B4A5C). The
staircase rises left to right. No 2x2 grid.

Layout: plain bone #EEECE7 background. Four full-body views in a row at identical scale and
eye-line (front, three-quarter left, side, back), plus one large head-and-shoulders view.
Neutral expression. Even flat lighting.

Avoid: text, letters, numerals, logos, watermarks, signatures, readable interface or keyboard
legends, photorealism, 3D render, anime or chibi proportions, large eyes, child-like features,
school uniform, robot or screen face, glowing circuits, lab coat, beard-and-glasses expert look,
detailed fingers, gradients, outlines, texture, sexualised pose or clothing, saturated blue,
saturated green, yellow, flag or party colours, any real person or existing character resemblance.
```

Same ratio rule as above: use the ratio setting if there is one, otherwise add `OUTPUT: 1 image, wide landscape (3:2).` as a last line.

### 2.4 The Avoid list on its own

Chat tools have no separate "negative prompt" box (assumption), so the avoid list lives inside the prompt as an "Avoid:" sentence, as above. This stand-alone copy is for two uses: paste it into a negative-prompt field **if** your tool happens to have one (check the current UI), and keep it as the master version when you add to it. Source: **bible 5.1, verbatim.** The rule from the bible: add to this list when QA finds a new failure, never remove from it, and tell Claude to log the new item in the bible.

```
Avoid: text, letters, numerals, logos, watermarks, signatures, readable interface or keyboard
legends, photorealism, 3D render, anime or chibi proportions, large eyes, child-like features,
school uniform, robot or screen face, glowing circuits, lab coat, beard-and-glasses expert look,
detailed fingers, gradients, outlines, texture, sexualised pose or clothing, saturated blue,
saturated green, yellow, flag or party colours, any real person or existing character resemblance.
```

### 2.5 What to generate

- **4 variations in each tool, so 8 images**, each one a full sheet (four full-body views plus one large head-and-shoulders view). The four views are inside each image; the four variations are four separate runs of the same prompt.
- Do not edit the prompt between runs. The point is to see how much the result varies.
- Save each with the tool's download button into `assets/buzhou/candidates/` as:
  `R01_master_cand_gem1.png` to `R01_master_cand_gem4.png` (Gemini) and `R01_master_cand_gpt1.png` to `R01_master_cand_gpt4.png` (ChatGPT). If the tool gives you .jpg or .webp, keep that extension; do not convert.
- Write down the date, time, tool name and model name shown on screen now, while the chat is open (you need them for the log).
- Expect that none is perfect. Gender may differ from run to run because the prompt leaves it open (bible 5.1 notes); the approved master, not the prompt, fixes the identity.

### 2.6 How to choose

Do this in order. Perfect is not required: the patch and colours can be fixed later by hand; the face, proportions and adult read cannot.

1. **Quick-kill (you, 5 minutes).** Remove any candidate that has any of: visible text or numbers anywhere; a logo or brand-like mark; a child-like or "student" look; large eyes, rounded cheeks or blush; outlines, gradients, glow or 3D shading; a robot or screen face; saturated blue, green or yellow dominating; a real-person look; fewer than four full-body views. Log each removed candidate with a one-word reason.
2. **Shortlist up to three** from what is left, using this priority: (a) reads clearly adult and calm; (b) face and angular jaw match the written description; (c) flat, outline-free medium; (d) headphones and patch roughly right; (e) four views at the same scale.
3. **Blind pick with the wife.** Rename copies of the shortlist `A`, `B`, `C` (so neither of you knows which tool or prompt made which). Show them on a screen at full size. Each of you writes down your first choice and one sentence on why, separately, then compare. If you disagree, the wife's pick on adult reading and colour read decides (bible gate G4).
4. **Run section 5** on the winner (the checklist). If it fails something that is a defect rather than a design problem, fix it with a local edit or a follow-up (section 9), save the result as a new file in `candidates/` (for example `R01_master_cand_gem2_fix1.png`), log it, and run section 5 on that file instead; if it fails the adult read or resemblance, go back to the shortlist.
5. **Copy the final winner** (the original candidate, or its fixed version from step 4) to `assets/buzhou/R01_master_v1.png` (copy, do not rename; keep the original in `candidates/`). **Never edit or overwrite this file.** Every later change gets a new file name (v2, v3).
6. **Log** all 8 candidates and the master copy (section 7).
7. **Later, not today:** the operator traces or cleans the approved master in a vector editor to fix proportions and the patch, and exports the identity source plus a transparent PNG (bible 5.7 step 2). That file becomes `R01_master_v2` and, from then on, replaces v1 as the reference you upload.

If all 8 fail, do not keep rerolling. Read section 9, add one corrective line to the prompt (and to the Avoid list if it is a "don't"), and run one more round of 4. After three rounds, stop and ask Claude for a revised prompt.

---

## 3. STEP 2: lock it

Goal: every later image looks like the same person. The chosen master, not the words, carries the identity.

### 3.1 Rules for every follow-up image

1. **Always attach `R01_master_v1.png`** to the message, whether you continue in the same chat or start a new one. The tool does not reliably remember it (hypothesis), and the bible says "always with the approved master attached" (5.2). A second attachment is allowed only where a block below says so (for example the approved hand image). Never attach more than three images, and never anything but our own generated files.
2. **Same chat or a new chat?** Re-uploading in a **new chat** for each new image type is the cleaner default, because long chats drift (bible 5.7, "no telephone game"). Staying in the **same chat** is fine for a quick tweak to the image you just made, but attach the master again anyway. If a result drifts, restart from the master, never from the previous generated image.
3. **Message order:** attach the image(s), paste the **character lock** (3.2), then paste the block for the image you want.
4. **One change per image** (bible 5.2): the block's `CHANGE ONLY` line is the one thing that is allowed to differ from the master.
5. **Generate 4, save all, check all** (section 5), keep the best, log everything.
6. **Three tries, then stop.** If one defect survives three rounds, fix it by hand or ask Claude for a better prompt. Do not burn an afternoon.
7. If the tool changes the face, it should say so (the lock asks it to). If it does not and the face moved, treat that as a fail.
8. **Which side is "left chest"?** The bible does not say whether "left" is the character's own left or the viewer's left. Once the master is chosen, the side its patch is on is the rule for every image. Wherever a block below says "left chest", it means "the same side as in the attached master". If a result has the patch on the opposite side, treat it as a fail and regenerate. Never mirror or flip an image in an editor. Write the side you chose (for example "patch is on the viewer's right in the front view") at the top of your log notes.
9. **Exception to rule 1:** the setting plates (R10) contain no character, so they use the style-only lock and attach nothing. The prop sheet (R06) attaches the master only to copy the headphones and patch design.

### 3.2 The character lock (paste at the start of every follow-up)

Source: **pack wording**, merged from the bible's follow-up prompts (5.2 later turns and 5.3 structured form), the locked features in 4.1, 4.2 and 5.6, and the palette in 4.4. It is long on purpose: you paste it, you do not retype it. The same labelled layout should work in both tools (hypothesis); if Gemini does better with plain sentences, delete the labels.

If you add an item to the Avoid line later, change it here and in 2.4, and ask Claude to log it in the bible.

```
REFERENCE: The attached image is the source of truth for identity. This is the same ORIGINAL,
clearly adult virtual character (stated age 28, gender not specified). Do not redesign it.
KEEP IDENTICAL: face shape, long oval head, defined angular jaw, almond dark eyes of modest size
with one small highlight, high straight eyebrows, wedge-shaped nose shadow, calm mouth, visible
ears and neck, short neat side-parted charcoal hair with one lighter highlight shape, flat warm
beige skin, about seven heads tall, slim-to-average build with slightly broad shoulders, matte
charcoal over-ear headphones (no logo, no cable), and the small rectangular patch on the left
chest (bone backing, rising staircase of six flat squares: three bottom-aligned columns of 1, 2
and 3 squares, left to right, colours #C9D1DA, #6F8197, #3B4A5C; on the same side of the chest as
in the attached image; no 2x2 grid).
STYLE: flat vector, outline-free, one flat colour plus at most one flat shadow shape per form, no
gradients, no texture, no glow, no 3D. Palette only: #3B4A5C, #6F8197, #C9D1DA, #EEECE7, #2B3038,
#4A515B, #D8B190, #BE9371.
CONSTRAINTS: no text, no letters, no numerals, no logos, no watermark; hands hidden or simplified;
plain flat bone #EEECE7 background unless told otherwise; not any real person or existing
character. If anything about the face changes, say so and redo it.
AVOID: text, letters, numerals, logos, watermarks, signatures, readable interface or keyboard
legends, photorealism, 3D render, anime or chibi proportions, large eyes, child-like features,
school uniform, robot or screen face, glowing circuits, lab coat, beard-and-glasses expert look,
detailed fingers, gradients, outlines, texture, sexualised pose or clothing, saturated blue,
saturated green, yellow, flag or party colours, any real person or existing character resemblance.
```

**Style-only lock** (use this one instead for images that contain no character: props R06 and settings R10). Source: pack wording, from bible 4.4, 4.8 and 4.9.

```
STYLE: flat vector, outline-free, built from clean geometric planes; one flat colour plus at most
one flat shadow shape per form; no gradients, no texture, no glow, no 3D; crisp edges. Palette
only: #3B4A5C, #6F8197, #C9D1DA, #EEECE7, #2B3038, #4A515B, #D8B190, #BE9371. Muted overall, no
saturated blue, green, teal or yellow, no red.
CONSTRAINTS: no text, no letters, no numerals, no logos, no brand marks, no watermark, no licence
plates, no readable signs, interface or keyboard legends, no flags or party colours, no people
unless stated.
AVOID: photorealism, 3D render, gradients, outlines, texture, glow, glowing circuits, blue digital
rain, robot or screen faces, money, charts, maps, anything resembling a real brand or product, any
real person or existing character resemblance.
```

### 3.3 Order of work and file names

Kept files go in `assets/buzhou/`. Candidates go in `assets/buzhou/candidates/` as `<ID>_<name>_cand_gem1.png` (Gemini) or `_cand_gpt1.png` (ChatGPT). Version numbers go up (v1, v2); never overwrite. The short names below replace the long pattern in bible 5.7 step 3 on purpose, so nothing has to be renamed when the handle is chosen; the bible calls that layout a proposal.

| Order | ID | What | Kept file name | Where the prompt is | When |
|---|---|---|---|---|---|
| 1 | R01 | Master turnaround sheet | `assets/buzhou/R01_master_v1.png` | section 2 | Today |
| 2 | R08 | Thumbnail-size test sheet (made by shrinking, not generated) | `assets/buzhou/R08_thumb_test_v1.png` | 3.4 | Today |
| 3 | R02 | Face sheet | `assets/buzhou/R02_face_sheet_v1.png` | 3.5 | Today |
| 4 | R07 | Corner (PiP) busts, left and right | `assets/buzhou/R07_pip_left_v1.png`, `R07_pip_right_v1.png` | 3.6 | Today |
| 5 | R03 | Expression sheet E01 to E10 | `assets/buzhou/R03_expressions_v1.png` (or `R03_E01_v1.png` ...) | section 4.2 | Next sitting |
| 6 | R04 | Pose set | `assets/buzhou/R04_P03_v1.png` ... | section 4.3 | Next sitting |
| 7 | R05 | Outfit sheets | `assets/buzhou/R05_outfitA_v1.png` ... | 3.7 | Later |
| 8 | R06 | Prop sheet | `assets/buzhou/R06_props_v1.png` | 3.8 | Later |
| 9 | R10 | Empty setting plates | `assets/buzhou/R10_plate_desk_v1.png` ... | 3.9 | Later |
| 10 | R11 | Avatar and banner | `assets/buzhou/R11_avatar_v1.png`, `R11_banner_v1.png` | 3.10 | Later |
| 11 | R12 | Badge and label artwork (made by hand) | `assets/buzhou/R12_badges_v1.png` | 3.11 | Later |
| 12 | R13 | Palette swatch chart (made by hand) | `assets/buzhou/R13_palette_v1.png` | 3.12 | Later |
| 13 | R09 | Mouth-shape set | `assets/buzhou/R09_mouths_v1.png` | 3.13 | Only if a voice is used |

Keeper rule: a kept file is a copy of the chosen candidate, saved in `assets/buzhou/` under the short name in the table with `_v1`; the original stays in `candidates/`. Log the candidate rows and the keeper row.

The bible's R04 is "pose sheet P01 to P12". Single poses are more reliable than twelve in one image (hypothesis), so each pose is its own file and the folder is the sheet.

### 3.4 R08: thumbnail-size test (no prompt; do this right after you pick the master)

This is the adult-read test at small size (bible 4.7, 4.6). It is a shrinking job, not a generation job, but log the result file as an edited asset (tool "manual resize", prompt "none, derived from R01_master_v1.png").

1. Crop one full-body front view from `R01_master_v1.png` into a copy. Do not touch the master.
2. In any basic image tool (Preview on a Mac, Paint or Photos on Windows, or a slide app), make three copies of the figure about **64, 96 and 128 pixels tall** (roughly the size of a phone app icon at the small end). Put them on a bone background (`#EEECE7`) and again on a dark one (`#2B3038`). Save as one image, `R08_thumb_test_v1.png`.
3. Look at it at normal viewing size, not zoomed in. Can you still see the headphones and the staircase patch? Does it still read as an adult? Does it look like a different person from a cartoon child, a mascot or a robot?
4. This image is what the wife looks at for the age-guess test (section 6).

### 3.5 R02: face sheet

Source: pack wording, from bible 5.8 R02 ("front, three-quarter, profile, neutral") and the 5.5 conventions. Attach `R01_master_v1.png`. "Left" always means toward the left edge of the image.

```
CHANGE ONLY: the view. Make a face sheet.
LAYOUT: three chest-up views of this character in one row at identical scale and eye-line: front,
three-quarter left, side profile. Include head, neck, ears, shoulders and upper chest, so the chest
patch is visible where the angle allows. Neutral calm expression in all three. Headphones on the
ears in all three. Plain bone background. Even flat lighting.
OUTPUT: 1 image, wide landscape (3:2).
```

### 3.6 R07: corner (PiP) busts, left and right

Source: pack wording, from bible 4.6, 5.5 (P06, P07) and 5.8 (R07). The corner picture sits beside the content and the character faces toward it. Generate left and right as **two separate runs**. Do not flip one in an editor: flipping moves the patch to the wrong side of the body.

The bible asks for a transparent background and 3 sizes. Ask for a plain flat bone background (a transparent background is a later cut-out in the vector editor; if the tool offers a transparent option, check the current UI and inspect the edges). The 3 sizes are made by resizing a copy later, not generated.

```
CHANGE ONLY: the framing. Make a picture-in-picture bust facing left.
LAYOUT: one chest-up bust of this character in Outfit A, head and body turned a slight
three-quarter turn toward the left edge of the image (not a full profile), face clearly visible,
neutral calm expression, headphones on, chest patch visible, hands out of frame. The figure fills
about 80 percent of the image height, centred, with an even margin of plain flat bone background
all round so it can be cut out later. No frame, no ground shadow, no checkerboard pattern.
OUTPUT: 1 image, square (1:1).
```

```
CHANGE ONLY: the framing. Make a picture-in-picture bust facing right.
LAYOUT: one chest-up bust of this character in Outfit A, head and body turned a slight
three-quarter turn toward the right edge of the image (not a full profile), face clearly visible,
neutral calm expression, headphones on, hands out of frame. The chest patch must stay visible, on
the same side of the body as in the attached image; keep the turn small enough for that. The figure fills about 80
percent of the image height, centred, with an even margin of plain flat bone background all round
so it can be cut out later. No frame, no ground shadow, no checkerboard pattern.
OUTPUT: 1 image, square (1:1).
```

### 3.7 R05: outfit sheets (later)

Source: pack wording, from bible 4.3 and the wardrobe lock: only outfits A, B, C and the listed seasonal variants exist; the patch and headphones appear in **every** outfit; no real garment brand. Attach `R01_master_v1.png`. Clarifications I had to make because the bible is silent (the wife can overrule): shoes for B and C reuse outfit A's plain bone sneakers so the tool does not invent a pair; in the rain and cool-season variants the patch sits on the outermost layer so it stays visible, as the wardrobe lock requires; the vest goes over the jacket.

Outfit A, workday (default):

```
CHANGE ONLY: nothing about the character. This is the outfit reference sheet for Outfit A.
LAYOUT: two full-body views side by side at identical scale and eye-line: front, then back.
Neutral expression, hands in jacket pockets, headphones on the ears, plain bone background, even
flat lighting.
OUTFIT A: boxy light-grey coach jacket #C9D1DA over an ink-slate crew-neck tee #3B4A5C; charcoal
straight trousers #2B3038; plain bone sneakers #EEECE7; the staircase patch on the jacket's left
chest (not visible from behind). No logos, no text.
OUTPUT: 1 image, wide landscape (3:2).
```

Outfit B, studio knit (close-ups, title cards, cool-season videos):

```
CHANGE ONLY: the outfit. This is the outfit reference sheet for Outfit B.
LAYOUT: two full-body views side by side at identical scale and eye-line: front, then back.
Neutral expression, hands in trouser pockets, headphones on the ears, plain bone background, even
flat lighting.
OUTFIT B: thin ink-slate #3B4A5C knit crew-neck, no jacket, with the staircase patch embroidered on
the left chest; charcoal straight trousers #2B3038; plain bone sneakers #EEECE7. No logos, no text.
OUTPUT: 1 image, wide landscape (3:2).
```

Outfit C, warm-day shirt (hot, humid weather):

```
CHANGE ONLY: the outfit. This is the outfit reference sheet for Outfit C.
LAYOUT: two full-body views side by side at identical scale and eye-line: front, then back.
Neutral expression, hands in trouser pockets, headphones on the ears, plain bone background, even
flat lighting.
OUTFIT C: short-sleeve open-collar shirt in dusk grey-blue #6F8197, sleeves rolled once, modest
and not revealing, no jacket, with the staircase patch on a small chest tab on the left chest;
charcoal straight trousers #2B3038; plain bone sneakers #EEECE7. No logos, no text.
OUTPUT: 1 image, wide landscape (3:2).
```

Rain-season variant (Outfit A plus a light hooded rain shell and a compact folding umbrella):

```
CHANGE ONLY: the outfit. This is the rain-season variant of Outfit A.
LAYOUT: two full-body views side by side at identical scale and eye-line: front, then back.
Neutral expression, hands in pockets, headphones on the ears, plain bone background, even flat
lighting. Next to the figure, drawn as a separate prop and not held by anyone: one compact folding
umbrella, closed, plain charcoal #2B3038.
OUTFIT: the Outfit A pieces plus a light hooded rain shell in dusk grey-blue #6F8197 worn over the
jacket, hood down, plain, with the staircase patch visible on the left chest of the shell. No
logos, no text, no reflective strips.
OUTPUT: 1 image, wide landscape (3:2).
```

Cool-season variant (Outfit A plus a lightweight charcoal padded vest; Outfit B is the other cool-season option and is already sheet B):

```
CHANGE ONLY: the outfit. This is the cool-season variant of Outfit A.
LAYOUT: two full-body views side by side at identical scale and eye-line: front, then back.
Neutral expression, hands in pockets, headphones on the ears, plain bone background, even flat
lighting.
OUTFIT: the Outfit A pieces plus a lightweight padded vest in charcoal #2B3038 worn over the
jacket, slim and plain, with the staircase patch visible on the left chest of the vest. Not a
heavy snow coat, no autumn-leaf styling. No logos, no text.
OUTPUT: 1 image, wide landscape (3:2).
```

The hot-weather variant is simply Outfit C with no jacket, so it needs no extra sheet.

### 3.8 R06: prop sheet (later)

Source: pack wording, from bible 5.8 R06 and 4.2. Use the **style-only lock** (3.2), not the character lock, and attach `R01_master_v1.png`. All card text, numbers and dates are added later in post and checked by the wife.

```
Use the attached image only to copy the design of the headphones and the chest patch. Do not draw
the character.
LAYOUT: a prop sheet on a plain bone background, objects well spaced and not touching, no labels.
In reading order:
- the headphones: matte charcoal closed-back over-ear shape, generic, no logo, no cable, three
  views (front, side, three-quarter);
- the chest patch alone, flat: bone backing with a rising staircase of six flat squares, three
  bottom-aligned columns of 1, 2 and 3 squares, left to right (#C9D1DA, #6F8197, #3B4A5C), no 2x2
  grid, shown at three sizes (large, medium, small);
- a blank checklist card in fog #C9D1DA with three empty small squares down the left side, each
  followed by a short plain ink-slate bar; no digits, no letters;
- a blank date-stamp card in fog #C9D1DA with one empty rounded slot at the top right; no digits,
  no letters;
- a compact folding umbrella, closed, plain charcoal, no logo;
- a generic laptop, open, with a plain blank light-grey screen, blank keycaps, and a plain lid with
  no logo.
OUTPUT: 1 image, wide landscape (3:2).
```

### 3.9 R10: empty setting plates (later)

Source: pack wording, from bible 4.8 (details and the "what generators get wrong" column). Style-only lock, no attachment, no characters, no text. These are illustrated scenery and are always labelled 示意 (illustration only) later, typeset in post; no caption ever calls a scene the character's own room, desk or café (bible 4.8). Wood and tile are shown in the palette's greys so the character sits on them without clashing; if the wife finds them too cold she can ask for one or two muted warm neutrals, which is a bible change (4.4).

Run the Taiwan-ness check from `research/culture.md` 7.6 on every plate (the wife does this; section 8).

Rented-room desk corner (check: sockets, grille, no shoes on the floor):

```
LAYOUT: an empty illustrated rented-room desk corner, no people, no characters, desk corner only
(no storage furniture, no room layout). Details: a shoes-off tile or laminate floor edge with no
shoes in view; a plain small desk with a small desk fan on it; a power strip with Taiwan Type A/B
sockets drawn simply (two flat parallel slots, plus a round ground pin on the B type); a split air
conditioner high on the wall; a window with a plain metal security grille; a round ceiling light
or a tube lamp. No posters, no books with titles, no screen content.
OUTPUT: 1 image, wide landscape (16:9).
```

Old-house café (check: blank menu, no logos):

```
LAYOUT: an empty illustrated renovated old-house cafe, no people, no characters. Wood and old
patterned floor tile shown in the palette's greys, a hand-drip coffee counter in the background,
plain mugs without logos, and a laptop with a blank screen on a table. The menu board is a blank
panel with no writing and no marks that look like writing.
OUTPUT: 1 image, wide landscape (16:9).
```

Study room or library seat (check: signs blank, no uniforms):

```
LAYOUT: an empty illustrated study room or library seat, no people, no characters: a partitioned
desk with wood dividers shown in the palette's greys, a desk lamp, a quiet-room feel. Any sign is a
blank panel with no writing. No school uniforms, no posters.
OUTPUT: 1 image, wide landscape (16:9).
```

Office cubicle (check: no readable text or logos):

```
LAYOUT: an empty illustrated office cubicle, no people, no characters: fluorescent ceiling lights,
desk partitions, a document tray, a plain laptop with a blank screen. No posters, no whiteboard
writing, no branded items, no readable text.
OUTPUT: 1 image, wide landscape (16:9).
```

Rainy window (check: helmets, no legible plate, right-hand traffic):

```
LAYOUT: an illustrated rainy window, no people in the room: rain on the glass and condensation, a
closed plain charcoal umbrella by the door, blurred scooters outside with riders in rain ponchos,
every rider wearing a helmet, right-hand traffic, no licence plate visible, no readable signs.
Greyed muted palette only. No snow, no autumn leaves.
OUTPUT: 1 image, wide landscape (16:9).
```

MRT platform, minor use (check: neutral grey only, no map text):

```
LAYOUT: an illustrated Taiwan-style MRT platform, no people: platform screen doors, a row of seats
with one section in a slightly different grey tone to suggest priority seating, plain ceiling
lights. Neutral grey only: no line colours, no station names, no signs, no maps, no route text.
OUTPUT: 1 image, wide landscape (16:9).
```

### 3.10 R11: avatar and channel banner (later)

Source: pack wording, from bible 5.8 R11 and 5.4 (E01 neutral is "most PiP and avatar"). Character lock, attach the master. The avatar keeps the headphones and the patch in frame because the patch is the "not a photo" tell. Platform banner sizes and safe zones are unverified: check the platform's current help page before cropping. All text is added in post.

```
CHANGE ONLY: the framing. Make a square avatar.
LAYOUT: one chest-up view of this character in Outfit A, front-facing, centred, neutral calm
expression, headphones on, chest patch clearly visible, hands out of frame. The figure fills about
70 percent of the image height. Plain flat bone background.
OUTPUT: 1 image, square (1:1).
```

```
CHANGE ONLY: the framing. Make a wide channel banner background.
LAYOUT: one chest-up view of this character in Outfit A, three-quarter view facing toward the
centre, placed in the right-hand third of a very wide image, neutral calm expression, headphones
on, chest patch visible, hands out of frame. The rest of the image is empty plain flat bone
background, kept clear for text that will be added later. No text of any kind.
OUTPUT: 1 image, very wide landscape (16:9, or wider if the tool offers it).
```

### 3.11 R12: badge and label artwork (make by hand, no prompt)

The bible lists this as artwork with text typeset in post. A drawing tool does flat rectangles better than an image generator, and the Chinese text must never be generated (bible 4.5, BRIEF section 5). Make the frames in a slide or design app. Source: bible 4.4, 4.6, 5.8 R12, 8.2, 8.3. **The Chinese strings below go into the design app as typed text, in a Taiwan-glyph font such as Noto Sans TC with the language set to zh-TW. Never paste them into an image generator.** The wife checks every character by eye.

```
Callout style (bible 4.4): bone #EEECE7 fill, charcoal #2B3038 text, thin charcoal outer line.
Make four frames:
1. Corner badge, small:        text  AI 生成
2. Recording label bar, wide:  text  錄製條件：{工具}｜{版本}｜{方案}｜{YYYY/MM/DD}　由工作室真人操作錄製
3. Operator label bar, short:  text  由工作室真人操作錄製
4. Sponsored badge, small:     text  業配
Placeholders in {braces} are filled per video from the source slip.
The recording-label wording (錄製條件 versus 測試條件) is still an open decision for the wife and
operator (bible 8.2, open item 6). Use 錄製條件 until they decide.
```

### 3.12 R13: palette swatch chart (make by hand, no prompt)

A generator drifts hex colours, so a generated swatch chart would be wrong by design. Make it in a slide app: eight equal squares, each filled with the exact hex, with its name and hex typed underneath. The wife uses it for the colour read and the side-by-side check against the other nine concepts. Source: bible 4.4.

```
Ink slate        #3B4A5C
Dusk grey-blue   #6F8197
Fog grey         #C9D1DA
Bone             #EEECE7
Charcoal         #2B3038
Charcoal light   #4A515B
Warm beige (skin)   #D8B190
Beige shadow        #BE9371
```

### 3.13 R09: mouth-shape set (only if a voice is used)

Skip this until the voice decision (bible G5) is made. If the studio goes with captions only, R09 is never needed. Source: pack wording, from bible 5.8 R09 ("6 to 8 shapes"). Character lock, attach the master.

```
CHANGE ONLY: the mouth, one shape per head.
LAYOUT: a mouth-shape sheet for simple lip-sync: eight front-facing head-and-neck views of this
character in two rows of four, identical scale, headphones on, the same neutral eyes and eyebrows
in every cell, each with a different simple flat mouth shape: closed and relaxed; slightly open;
mid open; wide open oval; wide and flat; small and round; lips pressed together; closed with a
slight smile. Mouths are flat #BE9371 shapes, with a flat #2B3038 shape inside when open; no teeth
detail, no tongue detail. Plain bone background, no labels, no numbers.
OUTPUT: 1 image, wide landscape (3:2).
```

---

## 4. Expression sheet and pose prompts

Every block here is used the same way: attach `R01_master_v1.png`, paste the **character lock from 3.2**, then paste the block. All prompts avoid numbers and letters on purpose, so the tool does not draw them. "Left" means toward the left edge of the image.

### 4.1 Which poses come free

R01 already gives P01 front, P02 three-quarter left, P04 side and P05 back (hands in pockets, full body, outfit A). Pose P06 and P07 are the corner busts, R07 (section 3.6). The rest are below. If R01's own views are weak, use the optional turnaround row in 4.3.

### 4.2 R03: expression sheet (10 expressions)

Source for the ten expressions: **bible 5.4, copied**. Source of the prompt: pack wording. In two places I added a plain-words clarification in brackets because the bible mentions a card that is not in the picture. The bible's limits are included: no wide grin, no tears, no anger, no exaggerated emotion, and no raised-palm "stop" gesture.

All ten on one sheet:

```
CHANGE ONLY: the expression, one per head. Keep the same head, hair, headphones and collar in
every cell.
LAYOUT: an expression sheet: ten chest-up busts of this character in two rows of five, identical
scale and eye-line, front-facing unless the expression says otherwise, plain bone background, no
borders, no labels, no numbers, no text of any kind, no hands.
Top row, left to right:
- Neutral, calm (the default).
- Explaining: slight head tilt, mouth slightly open.
- Pointing attention: eyebrows slightly raised, eyes looking toward the right edge of the image
  (toward where a screen would be).
- Checking: eyes narrowed a little, looking to the side as if at a small card just out of frame.
- Mild smile.
Bottom row, left to right:
- Uncertain: eyebrows slightly asymmetric, lips pressed.
- Caution: eyebrows drawn in, level mouth.
- Correcting: small head bow, soft brows.
- Pleased, light: small smile, eyes crease slightly.
- Polite decline: slight head tilt, lips pressed, soft brows.
Keep every expression restrained: no wide grin, no tears, no anger, no exaggerated emotion.
OUTPUT: 1 image, wide landscape (3:2).
```

If the faces drift or two expressions look the same (hypothesis: ten in one image is hard), use one expression per image. This template takes one line from the list below it:

```
CHANGE ONLY: the expression. Expression: {PASTE ONE LINE FROM THE LIST BELOW}.
LAYOUT: one chest-up bust, front-facing unless the line says otherwise, centred, no hands, plain
flat bone background, no text.
OUTPUT: 1 image, square (1:1).
```

The ten lines, in order E01 to E10 (name the files `R03_E01_v1.png` ... `R03_E10_v1.png`; the E-number stays out of the prompt):

```
Neutral, calm (the default)
Explaining: slight head tilt, mouth slightly open
Pointing attention: eyebrows slightly raised, eyes looking toward the right edge of the image
Checking: eyes narrowed a little, looking to the side as if at a small card just out of frame
Mild smile
Uncertain: eyebrows slightly asymmetric, lips pressed
Caution: eyebrows drawn in, level mouth
Correcting: small head bow, soft brows
Pleased, light: small smile, eyes crease slightly
Polite decline: slight head tilt, lips pressed, soft brows
```

Use in the channel: E01 for most corner pictures and the avatar; E04 for "step zero: check the date"; E06 for "go by the official page"; E07 for privacy and risk points; E08 for corrections; E10 for questions it will not answer.

### 4.3 R04: poses

Source of the pose list: **bible 5.5**. Source of the prompts: pack wording. Hands are the main risk: the bible says never ask a generator for detailed fingers, and use one fixed simplified hand ("capsule-and-thumb") drawn once and reused (4.1). So **do P11 first**, approve its hand, then attach that approved P11 image as a second reference for P09 and P10.

P03, three-quarter right, full body (the one view R01 does not include):

```
CHANGE ONLY: the pose. Three-quarter right view, full body.
LAYOUT: one full-body view of this character in Outfit A, turned three-quarters toward the right
edge of the image, hands in jacket pockets, neutral calm expression, headphones on, feet fully
visible, plain bone background, no ground shadow.
OUTPUT: 1 image, portrait (2:3 or 3:4).
```

P11, pointing with the fixed simplified hand (do this one first):

```
CHANGE ONLY: the pose. Pointing.
LAYOUT: one chest-up view of this character in Outfit A, three-quarter view facing the left edge
of the image, one arm raised in front of the chest and pointing toward the left edge of the image
with a single simplified hand: one rounded capsule shape pointing outward plus a separate thumb
shape, no individual fingers, flat #D8B190 with one #BE9371 shadow shape. The other hand stays in
the jacket pocket. Eyes look the way the hand points. Neutral expression with eyebrows slightly
raised. The chest patch stays visible. Plain bone background. Do not raise an open palm.
OUTPUT: 1 image, square (1:1).
```

P09, holding the checklist card (attach the master, then the approved `R04_P11_v1.png`; numbers are added later, so the card stays blank):

```
CHANGE ONLY: the pose. Holding a blank checklist card.
SECOND ATTACHED IMAGE: it shows the approved simplified hand. Copy that hand style exactly
(capsule shape plus separate thumb, no individual fingers).
LAYOUT: one chest-up view of this character in Outfit A, front-facing, holding a blank rectangular
checklist card in front of the chest with both simplified hands. The card is fog #C9D1DA with
three empty small squares down the left side, each followed by a short plain ink-slate bar. No
digits, no letters, no writing on the card. Neutral calm expression. Plain bone background.
OUTPUT: 1 image, square (1:1).
```

P10, holding the date-stamp card (same two attachments):

```
CHANGE ONLY: the pose. Holding a blank date-stamp card.
SECOND ATTACHED IMAGE: it shows the approved simplified hand. Copy that hand style exactly
(capsule shape plus separate thumb, no individual fingers).
LAYOUT: one chest-up view of this character in Outfit A, front-facing, holding a blank rectangular
card in front of the chest with both simplified hands. The card is fog #C9D1DA with one empty
rounded slot in its top right corner. No digits, no letters, no writing on the card. Neutral calm
expression. Plain bone background.
OUTPUT: 1 image, square (1:1).
```

P12, walking, side view:

```
CHANGE ONLY: the pose. Walking.
LAYOUT: one full-body side view of this character in Outfit A, facing the left edge of the image,
mid-stride, relaxed upright posture, hands in jacket pockets, neutral calm expression, headphones
on, feet fully visible, plain bone background, no ground shadow.
OUTPUT: 1 image, wide landscape (3:2).
```

P08, seated at a desk, waist-up. By design the character cannot operate a computer or press a key (bible 2.4), so it must not be shown typing or touching a device:

```
CHANGE ONLY: the pose. Seated at a desk, waist-up.
LAYOUT: one waist-up view of this character in Outfit A, seated behind a plain flat desk drawn as a
simple flat shape, three-quarter view facing slightly toward the right edge of the image, upright
relaxed posture, both hands resting out of sight below the desk edge. Nothing on the desk: no
laptop, no screen, no keyboard, no cup. Neutral calm expression, headphones on. Plain bone
background, no room.
OUTPUT: 1 image, wide landscape (3:2).
```

Optional: the five full-body turnaround views (P01 to P05) in one row, only if R01's own views are not good enough:

```
CHANGE ONLY: the layout. Make a turnaround row.
LAYOUT: five full-body views of this character in Outfit A in one row at identical scale and
eye-line: front, three-quarter left, three-quarter right, side, back. Hands in jacket pockets,
neutral calm expression, headphones on, plain bone background, no labels. The chest patch is not
visible from behind; the headphones must be clearly visible from behind.
OUTPUT: 1 image, very wide landscape (16:9, or wider if the tool offers it).
```

---

## 5. Pass/fail checklist (tick for every image you keep)

For images with no character (props R06, setting plates R10), skip part B rows 1 to 10, 14 and 16 and use main checks 4, 5, 7, 8 and 9, plus the wife's Taiwan-details check (section 8, item 7) for R10. Hand-made files (R08, R12, R13) get checks 4 and 5 only.

Copy this section once per kept image, or tick it in a note beside the file. For a discarded image, one word of reason in the log is enough. Optional help: you can ask Claude (in Claude Code, in this folder) to look at a saved file and tick part B as a first pass. Treat its answer as a first pass only: it can miss details, and it cannot make the wife's judgements on age, colour read and Taiwan details.

### 5.1 Main checks

| # | Check | How to check, in plain words | Pass | If it fails: what to do |
|---|---|---|---|---|
| 1 | **Locked features** | Tick every row of part B below, against `R01_master_v1.png` side by side | [ ] | Face, jaw, eyes or proportions changed: **regenerate** from the master in a fresh chat. One small wrong item (patch, headphones, stray mark): **local edit** or a one-line follow-up (section 9), at most two rounds |
| 2 | **Adult read at thumbnail size** | Shrink to 64, 96 and 128 px tall (3.4). Seven-head proportions, head not oversized, limbs not shortened, jaw, neck and ears visible, eyes not large, no blush or freckles, practical adult clothes, neutral pose. The wife's blind age guess (section 6) | [ ] | Any item fails: **reject the image, do not retouch around it** (bible 4.7). Regenerate. If 2 or more of 4 look young, add the corrective line from section 9 to the prompt first |
| 3 | **Hands and fingers** | Count them. Hands should be hidden in pockets, or the one simplified capsule-and-thumb hand. No individual fingers, no extra or missing fingers | [ ] | One bad hand in a good image: **local edit** to "hide the hands in the pockets". Repeats: **edit the prompt** to hide hands, or hand-fix |
| 4 | **Text, numbers, garbled or Simplified Chinese** | Look at the patch, shirt, shoes, headphones, cards, laptop, menu boards and every corner. No letters, no numbers, no squiggles that imitate writing. Any Chinese character at all is a fail (Chinese is added later in post, bible 4.5) | [ ] | **Regenerate**. If it is one small mark, **local edit** to remove it. Never keep a generated Chinese character: it is wrong until proven otherwise |
| 5 | **Party-colour read** | Squint. Is it a muted blue-grey family, or does it look like a campaign poster? Ink slate and dusk together should look like well under half the image (bible: about 40 percent, an assumption). No saturated blue, green, teal or yellow; no red or burgundy; no blue-and-white slogan look; no all-black or all-white outfit. The wife confirms | [ ] | Colour drift only: note "colour-correct in the vector editor" and keep. Strong saturated cast or wrong colour family: **edit the prompt** (restate the palette) and regenerate |
| 6 | **Resemblance to real people or existing characters** | Gut check first: does it remind you of anyone or any character, mascot, singer, VTuber or logo? Then the full look-alike check in section 6 | [ ] | Any doubt: do not keep it as master. Change the offending feature through a bible revision (the wife re-approves), not by retouching |
| 7 | **Medium and palette match, with hex tolerance** | Flat vector, outline-free. No gradient, texture, glow, 3D or soft shading. Pick colours with any eyedropper tool that shows hex codes and compare with the swatches (3.12). My working tolerance (an assumption, not from the bible): each of R, G and B within 15 of the target is a pass; 16 to 30 is "colour-correct later"; more than 30, or a different hue family, is a fail | [ ] | Style fail (outlines, gradients): **regenerate**. Colour a little off: keep and correct in the vector editor (the bible plans this). Style fail in 2 of 4: **edit the prompt** |
| 8 | **No brand, logo or plate** | Check headphones, sneakers (stripes, ticks), jacket, laptop, mugs, scooters and the background. No logos, brand-like marks, vendor icons, licence plates or station names | [ ] | **Regenerate**; if one small mark, **local edit** |
| 9 | **Layout as asked** | The right views, number of figures, same scale and eye-line, plain bone ground, no labels or titles | [ ] | **Edit the prompt** (state the count and layout again) and regenerate |

### 5.2 Part B: locked features (bible 5.6, tick each on every approved image)

| # | Locked feature | Pass |
|---|---|---|
| 1 | Long oval head, defined angular jaw | [ ] |
| 2 | Almond dark eyes (flat `#2B3038`), modest size, one highlight; eyebrows `#2B3038` | [ ] |
| 3 | High straight eyebrows | [ ] |
| 4 | Wedge nose shadow; calm mouth (expression may change) | [ ] |
| 5 | Visible ears and neck | [ ] |
| 6 | Short side-parted charcoal hair | [ ] |
| 7 | Skin tone `#D8B190` family, one shadow shape | [ ] |
| 8 | About seven heads tall; slim-to-average; slightly broad shoulders | [ ] |
| 9 | Matte charcoal over-ear headphones, no logo, no cable | [ ] |
| 10 | Staircase patch: six squares, bottom-aligned columns of 1, 2 and 3 rising left to right, colours fog, dusk, ink slate, on the left chest, on the same side as in the master | [ ] |
| 11 | Palette only from the eight colours (3.12) | [ ] |
| 12 | Outline-free flat vector; no gradient, texture or glow | [ ] |
| 13 | No text, logo or readable interface | [ ] |
| 14 | Adult reading (check 2 above) | [ ] |
| 15 | No hand detail beyond the fixed simplified hand | [ ] |
| 16 | Outfit is exactly one of A, B, C or a listed seasonal variant | [ ] |

### 5.3 Regenerate, edit the prompt, or edit the image?

| Situation | Do this |
|---|---|
| Whole-design problem (face, proportions, age read, wrong style, resemblance) | **Regenerate**: press regenerate or send the same prompt again, from the master in a fresh chat |
| The same defect appears in 2 or more of 4 variations | It is systematic. **Edit the prompt**: add one specific corrective line (section 9), or an item to the Avoid list, and run 4 more |
| One local defect in an otherwise good image (patch, stray mark, extra finger) | **Edit the image**: use the tool's edit or select-region mode if it has one (hypothesis), or a follow-up such as "Change only the chest patch. Keep everything else identical." Two rounds at most |
| The face starts to move after several edits | Stop. Start a fresh chat from `R01_master_v1.png` |
| The same defect survives three rounds | Stop. Fix by hand in a vector editor, or ask Claude for a revised prompt, and write the failure in section 9's list |
| The tool refuses or answers only in words | Reply "Please generate the image now." If it refuses, read the reason; do not reword to get round a safety refusal |

---

## 6. The two human tests the bible requires

Both are gates for approving the master (bible G4, 4.7 and 5.7; HUMAN_TODO item 26). Do a quick version today on the winner; do the full version before the master is used for anything real. Anything built after R01 is provisional until the full look-alike check passes, so do not spend more than about two hours on follow-ups before that.

### 6.1 Test 1: the age-guess test

**What it proves:** the character reads as 25 or older (BRIEF ground rule 3), including when tiny.

1. Prepare two things: the winner at full size, and `R08_thumb_test_v1.png` (3.4).
2. Ask the **wife first, alone**, before she knows the design age. Do not say "28", "adult" or "check whether it looks young". Say only: "Please write one number for how old you think this character is, and one word for what they do (for example student, office worker, designer). There are no right answers." Show full size first, then the small version.
3. Repeat with **3 to 5 other people**, one at a time, same words. The bible requires only the wife's read; the other bibles in this project and HUMAN_TODO 26 use a small panel as well, and the blind age test is the stricter of the two approvals, so a panel is recommended.
4. Write each answer as it is given: initials, number, word.
5. **Pass:** the wife's number is 25 or more and she does not say "student" or "young" (bible 4.7 item 5). For the panel, my suggested rule (an assumption): no more than one guess under 25.
6. **Fail:** the wife says "student" or "young", or two or more panel guesses are under 25. Reject the image and go back to the shortlist; do not retouch around it.

### 6.2 Test 2: the look-alike check

**What it proves:** the character does not resemble a real person, a celebrity or an existing character (BRIEF ground rule 2). Source: bible 5.7, "Look-alike check procedure".

**Part A: reverse-image search (about 30 minutes; manual, no login scraping)**

1. Save the master and three variants (the shortlist) in one folder. These are the studio's own generated images. Never use a photo of a real person for any part of this. These are unpublished drafts and you will upload them to third-party search sites; check each site's current terms on what it does with uploaded images (unverified; I have not checked) and use only sites you are comfortable with.
2. Open a private or logged-out browser window, not signed in to personal accounts.
3. Use several public reverse-image search tools, by hand, one image at a time. Examples: Google Lens, Bing Visual Search, TinEye. Names and web addresses change, so use whatever public reverse-image search is current. If a tool insists on creating an account, skip it and use another one. No scripts, no automated tools, nothing that logs in to someone else's account.
4. For each image and tool, look at the first screen or two of "visually similar" results. Write down the date, the tool and the top matches, and whether any is a character, mascot, virtual singer, VTuber, logo or person.
5. Also run plain word searches in an image search and look for lookalikes in the results: for example "flat vector character with over-ear headphones", "staircase logo", "stair step pixel logo", "grey coach jacket character mascot". The patch must not resemble a logo (bible 4.2: no 2x2 grid, no QR-code look).

**Part B: named comparisons (about 20 minutes; wife helps with the Chinese names)**

6. For each name or group below, run an image search and look at the results beside the master on one screen. You do not need to read the Chinese: copy and paste the names. Nothing is uploaded.
   - The Taiwan characters named in the research files: 光音凱伶, 宮祈緣, OPEN將, 虎妮, and any competitor named in `research/competitors.md`.
   - Common AI-assistant and robot mascots.
   - Well-known headphone-wearing virtual singers and VTubers.
   - LINE Friends, Doraemon, Sanrio characters, and brand mascots.
   - The other nine concepts in `strategy/portfolio.md` 2D (their images do not exist yet; compare again as they appear).
   - Any logo with stair or pixel motifs.

**Part C: blind panel (combine with test 1, same sitting)**

7. Show the master to you, the wife and 2 to 3 trusted people. After the age question, ask: "Does this remind you of any real person, celebrity, VTuber, mascot or cartoon character?" Write down every answer in their own words. No one is being asked to like, follow or share anything. Do not prompt them with names.

**Result and what to do**

8. **Pass:** no match from the search, no match from the panel, and no similarity in the named comparisons. **Any match:** redesign the feature, or document why it is a coincidence and take it to the lawyer (`research/legal.md`, question 20). Do not keep a master with an unexplained match.
9. Re-run the whole check before launch, at the week-6 review, after any redesign, and after any complaint. A credible look-alike claim means taking the material down within 24 hours and pausing (bible 5.7, 7.3).
10. Log the result with an ID (LA-001, LA-002 ...) in `personas/buzhou/lookalike_log.md`. That file does not exist yet; create it with this template and write the ID into `licence_notes`:

```
LOOK-ALIKE LOG
LA-001   date: ____-__-__   image: assets/buzhou/R01_master_v1.png   checked by: ____

A. Reverse-image search (logged out, by hand)
 tool | date | top matches (character / mascot / logo / person?) | concern Y/N
 ____ | ____ | ____ | ____

B. Named comparisons done (tick): [ ] Taiwan characters  [ ] assistant/robot mascots
   [ ] headphone virtual singers and VTubers  [ ] LINE Friends, Doraemon, Sanrio, brand mascots
   [ ] other nine concepts  [ ] logos with stair or pixel motifs      notes: ____

C. Blind panel and age guesses
 initials | age guess | one word | "reminds you of..." (their words) | concern Y/N
 ____ | ____ | ____ | ____ | ____

Result: PASS / FAIL / PASS with note      Decided by: ____   Date: ____
Re-run due: before launch / week-6 review / after any redesign or complaint
```

**Later tests, not today:** the master at 64 px beside 里程's master, and at 110 px beside 歸位's, once those exist (`personas/README.md` section 5; HUMAN_TODO 26).

---

## 7. Provenance

Rule (BRIEF ground rule 2; bible 5.9): `assets/provenance.csv` gets **one row for every image you saved or considered, kept or discarded**. That means all 8 R01 candidates, every variation of every later image, the copy that becomes `R01_master_v1.png`, and every edited or derived file (a resized R08, a local edit, a cut-out). So do not discard anything unsaved: download every image the tool gives you, even the ones you reject on sight, and log it with a one-word reason. Nothing generated goes unlogged. Never delete a row.

Columns, already in the file: `timestamp,asset_path,persona,tool,model,prompt,licence_notes`.

- `timestamp`: ISO 8601 with the offset. The bible uses Taiwan time, `+08:00`. If you are elsewhere, convert, or write your real offset and keep it consistent.
- `asset_path`: the path from the project folder, for example `assets/buzhou/candidates/R01_master_cand_gem1.png`.
- `persona`: `buzhou` for now (it is a placeholder).
- `tool` and `model`: copy exactly what the screen shows at the time, never from memory. If the screen shows no model name, write `not shown in UI` plus the mode or version you can see. Never guess.
- `prompt`: the **full text you pasted** (character lock plus block, or the whole R01 prompt), in double quotes, with every double quote inside it doubled. At the very start of the cell write the attachments, for example `[REF: assets/buzhou/R01_master_v1.png]` or `[REF: none]`. The edit or follow-up text goes in too.
- `licence_notes`: the template below.

**The easy way to fill it:** do not type CSV by hand. Either paste into a spreadsheet app with these seven columns and save as CSV (UTF-8) so it handles the quotes, or fill the batch card below after each batch and ask Claude: "Append these rows to assets/provenance.csv." Rows for the four variations of one prompt share the same prompt text.

```
BATCH CARD (fill in once per batch of images)
date and time, with offset: ____
tool, exactly as shown: ____          model, exactly as shown: ____
plan (from account settings): ____
reference image(s) attached: ____ (file name, or none)
prompt: (paste the full text)
files and what happened to each:
  assets/buzhou/candidates/____ : kept / shortlisted / discarded because ____
  assets/buzhou/candidates/____ : ____
edits made afterwards (tool, what, new file): ____
visible or hidden mark from the tool seen or not: ____
```

**Ready-to-fill CSV block** (header plus one example row; the braces show what to replace). The example is only an illustration: no such file exists yet.

```
timestamp,asset_path,persona,tool,model,prompt,licence_notes
2026-10-11T14:05:00+08:00,assets/buzhou/candidates/R01_master_cand_gem1.png,buzhou,"{tool name as shown}","{model name as shown, or: not shown in UI}","[REF: none] {full prompt text, every double quote doubled}","STATUS: terms NOT YET CHECKED, do not publish or sell; plan {plan}; metadata or mark from tool: {seen / not seen, left untouched}; human edits: none; look-alike check: not yet run; age-guess: not yet run"
```

**Licence terms to read, and what to write.** Before any commercial use, open the **current** terms of use and any content or image policy for the tool and the exact plan you used (these differ by plan and may differ by country). Do not rely on the tool's own description of itself. Questions to answer from the text, not from memory:

1. Who owns, or what rights do you get in, the images you generate?
2. Is commercial use allowed on **this plan** (personal versus business plans may differ)?
3. Does it limit how you can use outputs (for example advertising, representing a business, using a character as a brand)?
4. Does it say similar outputs may be given to other users?
5. What does it say about visible marks, invisible watermarks or metadata, and about removing them?
6. Are there rules about the reference images you upload (we upload only our own generated images)?
7. When were the terms last changed? If it is unclear, ask the lawyer before commercial use.

Save a dated screenshot or PDF of the terms page somewhere you will find it. Then write the answer in `licence_notes`. A note on copyright: whether a purely AI-generated image is protected by copyright in Taiwan is an unverified recall (`research/legal.md` 8.2). That is why the bible keeps every prompt, edit and the hand-finished vector master as the human-authorship record, so keep this log complete.

**Filled-in licence_notes template, with blanks:**

```
plan: ____; terms page: ____ (address); version or "last updated" date shown: ____; read by ____ on ____; commercial use of outputs on this plan: ALLOWED / NOT ALLOWED / UNCLEAR; key sentence copied: "____"; restrictions noted: ____; mark or watermark from the tool: seen / not seen, left untouched; human edits: none / ____; look-alike check: LA-____ (pending / pass / fail); age-guess: pending / pass / fail; STATUS: CLEARED FOR COMMERCIAL USE / NOT CLEARED
```

When you have read the terms once for a tool and plan, copy the same notes onto every row made with them, and redo it when the terms change.

---

## 8. A short note for the wife

(Written in simple English. The Chinese terms are AI drafts: please correct any that sound wrong or too stiff, and tell us which are natural.)

You do not need to check the prompts or the tools. Please look at the images the way a Taiwanese viewer would on a phone, and tell us, for each image, **APPROVE (核准) / SMALL FIX (小修) / REJECT (退回)**, with a short reason. Use the project's reason codes where they fit: S for text or fonts, X for a cultural or visual error.

1. **How old does it look? 看起來幾歲？** Write one number and one word before we tell you anything. Does it look like a student (像學生)? Too young or baby-faced (太年輕、童顏)? We need it to read clearly adult, 25 or older (成年人感).
2. **Does it remind you of anyone? 撞臉？** A real person, an idol, a VTuber, a mascot, a cartoon character, a brand logo (標誌)? Does the staircase patch look like a logo of some app or company?
3. **Colours: 配色.** Does it look like a political party colour (政黨色), a campaign poster (競選感), or a blue-and-white slogan? Do the greys look like funeral or mourning clothes (喪服感)? Is the colour too cold or too dull (太冷、太悶)? The colours are meant to be quiet blue-greys.
4. **Does it look like a robot or a customer-service mascot? 像機器人或客服吉祥物？** It should not.
5. **Any text on the image? 圖上有沒有字？** There should be none. If you see any character at all, tell us whether it is garbled (亂碼、鬼畫符), Simplified (簡體字), or a Japanese or Hong Kong form (日式、港式字形).
6. **Gender: 性別感.** The design is neutral (中性) on purpose. Does it feel natural, or does it feel odd that we do not say he or she (他或她)? (This is bible open item 5.)
7. **Taiwan details, for the setting pictures only (R10):** the sockets (插座, Type A/B), the window grille (鐵窗), the air conditioner (分離式冷氣), scooters with helmets (機車、安全帽), no licence plate (車牌), no MRT line colours or names (捷運). Does it feel like Taiwan or like Japan or Korea?
8. **Hands: 手指.** Any extra or missing fingers?
9. **Does the outfit look practical and adult, not a school uniform (制服) or a costume?**

10. **Badge and label frames (R12), once the operator has typeset them.** Check every character by eye: are they Traditional (繁體) as written in Taiwan, in a Taiwan-style font, with no Simplified, Japanese or Hong Kong forms, and does the wording sound natural? The wording is an AI draft; please correct it.

If you are not sure about something, say "not sure" and why. Your gut reaction is useful information.

---

## 9. Common failure modes for this character, and fixes

Source: the bible's rules (4.1, 4.2, 4.4, 4.8, 4.9, 5.7) plus failures I would expect from the prompt text (hypotheses). Each fix is a line to add to the prompt or send as a follow-up. If a fix is a "don't", also add it to the Avoid list in 2.4 and 3.2, and ask Claude to log the new item in the bible.

| What you will see | Why it happens | Fix |
|---|---|---|
| **Patch is wrong**: staircase falls to the right, 2x2 block, QR or barcode look, 5 or 7 squares, wrong colours | "Rows" versus "columns" is easy to misread (the bible rewrote this once, review log) | `Redraw only the chest patch: six flat squares in three bottom-aligned columns of 1, 2 and 3, rising from left to right, colours #C9D1DA, #6F8197, #3B4A5C, on a bone #EEECE7 backing. Not a 2x2 grid. Change nothing else.` If it still fails, try plain words (hypothesis): `three bars of increasing height, built from stacked squares`. Then local edit, then hand-fix |
| **Digits or letters appear** on the patch, shirt or card | The prompt itself contains the digits 1, 2, 3 and "numerals" | `The patch contains only coloured squares. No digits, no letters, no writing anywhere.` Regenerate; remove in the editor if it is one small mark |
| **Patch on the wrong side, or mirrored** | The bible says "left chest" without saying whose left; flipping an image in an editor moves it | Use the side the master shows as the rule and keep it for every image (record the decision). Never flip an image. Follow-up: `Put the patch on the same side of the body as in the attached image.` |
| **Looks young, cute or student-like**: big eyes, rounded cheeks, blush, short body | Generators drift toward cute for "character"; the prompt's "virtual character" can pull toward anime or VTuber looks | `Adult proportions, about seven heads tall, angular jaw, small calm eyes, no blush, no rounded cheeks, practical adult clothes.` If the wife says "young": reject, do not retouch |
| **Robot, screen face, glowing AI imagery, saturated blue** | "AI" imagery defaults (bible 4.9) | Already in Avoid. Add: `Muted greyed blue-greys only; a plain human-like face; no glowing lines.` Check the 40 percent rule |
| **Outlines, gradients, soft shading, texture, glow creep in** | Generators prefer polished, shaded art | `Flat colour shapes only. No outlines, no gradients, no soft shading, no glow.` After 3 rounds, hand-finish |
| **Headphones wrong**: earbuds, gaming headset with a boom mic, visible cable, logo, glowing ring; missing from the back view | Generic "headphones" has many forms | `Matte charcoal closed-back over-ear headphones on the ears, no cable, no logo, no microphone, no lights. Visible from behind.` |
| **Gender, beard, glasses or makeup change between runs** | The prompt leaves gender open (bible 5.1 note) | Always attach the master. `Same gender presentation, face and hair as the attached image. No beard, no glasses, no makeup.` |
| **Hands**: fingers, hands out of the pockets | Hands are the classic generator weakness (bible 4.1) | `Hands hidden in the jacket pockets.` For pointing and card poses use the simplified hand from the approved P11. Local edit or hand-fix otherwise |
| **Outfit drift**: hoodie, bomber, puffer or heavy snow coat, white jacket, stripes or ticks on sneakers, lab coat, suit-and-badge look | Generators fill gaps with common clothes and brand styling | Restate the exact pieces and hex values in an `OUTFIT:` line (section 3.7). `Plain sneakers, no stripes, no logos.` No lab coat, no expert costume |
| **Hex codes or colour names printed in the picture, or colour swatches drawn** | The prompt contains many hex codes | `Do not write any hex codes, colour names or swatches in the image.` (A new Avoid item: tell Claude to log it in the bible.) |
| **Layout wrong**: different scales, views merged, only 3 views, labels or titles added, a face on the back view | Multi-view sheets are hard for generators | State the count and order again: `Exactly four full-body views of the same size in one row: front, three-quarter left, side, back, plus one large head-and-shoulders view. No labels.` Or make the sheet from single views |
| **Fake transparency**: a grey-and-white checkerboard drawn into the picture | The tool "draws" transparency | `Plain flat bone #EEECE7 background, no checkerboard.` Cut out later in the editor |
| **Pseudo-writing** on cards, laptop screens, menu boards, keyboard keys | Generators imitate text | `All cards, screens, boards and keys are blank, with no marks that look like writing.` Regenerate or erase |
| **Seated pose shows typing or a laptop** | Natural for "desk" prompts, but the character cannot operate a computer (bible 2.4) | The P08 block already says hands out of sight and nothing on the desk. If it still adds a laptop: `Remove the laptop and keyboard. Hands out of sight.` |
| **Setting plate does not look like Taiwan**: wrong sockets, no window grille, shoes on, left-hand traffic, no helmets, visible plates, MRT line colours or names, branded cups | The bible's "what generators often get wrong" column (4.8) | Add the specific detail from the R10 block as a follow-up, for example `Add a plain metal security grille on the window. Remove the shoes.` The wife runs the Taiwan-ness check (8) |
| **Looks like an existing character or logo**: a headphone-wearing virtual singer or VTuber, an assistant mascot, a software or pixel logo | The headphones and the patch are the two most "borrowable" features | Do not retouch. Redesign the feature through a bible revision with the wife, then repeat the look-alike check (6.2) |
| **Drift after several edits** (the "telephone game") | Each edit starts from the previous output | Start a fresh chat from `R01_master_v1.png` (bible 5.7 step 5) |
