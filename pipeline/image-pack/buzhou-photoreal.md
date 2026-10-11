# 步驟 (buzhou): PHOTOREAL image pack, version 1

Written 2026-10-11 from `personas/buzhou/photoreal-addendum.md` (the spec; it wins if this pack disagrees) and, where the addendum is silent, from `personas/buzhou/bible.md` and `BRIEF.md` section 3. This replaces the stylised pack `pipeline/image-pack/buzhou.md` for the look only (the stylised pack stays as a record). Nothing has been generated yet: no photoreal image exists.

**How to read this pack**

- Text inside a code block is for copy and paste. Everything else is for you to read.
- **Hypothesis** means I believe it but have not checked it. Image tools change their menus, model names, limits and rules often. **Check the current screen** before relying on any statement about what Gemini or ChatGPT can do, and copy model names exactly as the app shows them.
- The prompts describe a **fictional person** by attributes only. They name nobody. You must never add a real person's name, a public figure, a performer, an existing character or a photo to any prompt (section 1, bullet 3).
- This character is **openly AI**. Nothing made with this pack may be posted until the licence check (section 7), the human tests (section 6) and the labelling steps (section 8) are done, and the reading test, lawyer answers and STOP 3 are passed (`HUMAN_TODO.md`). Making test images today is fine.
- File names use short ID codes (R01, R02 ...) so nothing has to be renamed when the real handle is chosen. **This pack's file names carry a `_pr_` tag** (for example `R01_pr_master_v1.png`); the 方寸 and 色環 packs do not. Use each pack's own names exactly.
- **Start with `pipeline/image-pack/README-photoreal.md`** (which pilot first, time, how to log, what to send back, why the labels still apply).

---

## 0. One-screen summary

**Who the character is.** 步驟 (working name `buzhou`, Chinese for "steps") is an openly-AI character for a YouTube Shorts and Threads channel that explains AI tools in three steps or fewer. A real person at the studio makes the screen recordings; the character is a small picture in the corner. He is now a **photorealistic fictional man**, stated age 28, who looks about 28 to 33: ordinary East Asian adult features, long-oval face with a defined jaw, straight dark eyebrows, short black side-parted hair, clean-shaven, no glasses. Constants: **matte charcoal over-ear headphones with no logo** and a **small sewn patch with a rising staircase of six squares** on the chest. Default outfit: a boxy light cool-grey jacket over a muted slate tee, charcoal trousers. Photographed as a plain studio portrait against a mid-light grey backdrop, with **hands always out of frame or hidden in pockets**. He must read as clearly adult, ordinary, not uncanny, not like any real person, and unmistakably AI once the badge and caption are on.

**What the first session should achieve.** You leave with (1) one chosen master image, R01, that passes the checklist in section 5; (2) the quick tests started: the wife's age guess and the first reverse-image search of face crops; (3) the first lock-in images made from it: the face set R02, and the two corner busts R06; and (4) every image saved and logged in `assets/provenance.csv`. Expressions, outfits, framings and the avatar come in the next sitting.

**Time estimate (my estimate, an assumption, not measured).**

| Part | Who | Minutes |
|---|---|---|
| Set-up: folders, one new chat per tool, log sheet ready | You | 10 |
| STEP 1: R01, 4 runs in each tool, saved | You | 35 |
| Choose: shortlist, blind pick with the wife | You, wife | 20 |
| Test the winner: checklist, small-size test, quick age guess, first reverse-image search | You, wife | 45 |
| STEP 2: R02 face set (4 images), R06 corner busts (2 images), 4 runs of each (24 runs) | You | 60 |
| Logging while you go | You | 25 to 30 |
| **Today, total** | | **about 3.5 hours**, wife about 40 minutes |
| Next sitting: R03 expressions, R04 outfits | You | about 2 hours |
| Later: R05 framings, R07 avatar, the full human tests, the optional sets | You, wife, panel | about 3 hours plus the panel |

**Order of work**

1. Section 1, then set up the folders (2.1).
2. STEP 1: R01 in Gemini and in ChatGPT (section 2).
3. Choose the best, run the checklist (section 5) and the quick tests (section 6).
4. STEP 2: continue only in the tool that made the winner (section 3): R02, then R06.
5. Next sitting: R03 expressions, R04 outfits, R05 framings, R07 avatar (section 4).
6. Before anything is used for real: the full human tests (section 6), the licence record (section 7) and the labelling steps (section 8).

---

## 1. Before you start

1. **Which tool first, and why (hypothesis).** Start with **Gemini**, then run the same R01 in **ChatGPT** as a second opinion (about 15 extra minutes for 8 candidates instead of 4). The Gemini prompt is written as a conversation ("generate, then I will ask for one change at a time"), which is the easiest way to learn how this face behaves; the ChatGPT prompt is written as labelled fields. Both ideas are unverified; start with whichever app you find easier. Once a winner is chosen, do **all** the follow-up images in the tool that made it, each in a fresh chat, because mixing tools for one face is likely to cause drift. If you hit a usage limit, wait rather than switching tools in the middle of a set.
2. **Settings to look for, if available (check the current screen).** Aspect ratio: portrait 4:5 (or 3:4) for R01; square 1:1 for busts and avatars. Highest resolution or quality (if the app offers a number-of-images setting, leave it at its default). An attach or upload button, an edit or select-region mode, and the place where the model name is shown (you will copy it into the log). Every prompt ends with an `OUTPUT:` line asking for 1 image, so run the prompt again (or press regenerate) until you have 4 separate images. Do not ask for "four images in one picture".
3. **Never upload a photo of a real person, and never type one into a prompt.** Not yourself, not your wife, not a friend, not an actor, not a stock-photo person, not a screenshot from the internet, not "just for the lighting", "just for the hair" or "just for the pose". Never type a real person's name, a public figure, a performer, an influencer, an existing virtual character or a brand into any prompt, and never write "looks like" or "in the style of" with a name. **The only images you ever upload are the character's own generated images** (`R01_pr_master_v1.png` and later approved files). Never an image of 方寸 or 色環, and never the old code-drawn vector art of 步驟 (`assets/buzhou/art/`). **Use a separate chat for this character**: never continue a chat in which you made 方寸 or 色環, because a generator reuses its default face and a cross-contaminated chat is the commonest cause of "they look like sisters" (addendum 9). The look-alike search in section 6 uploads only those too.
4. **Save everything, log everything.** Use the tool's download button, not a screenshot (a screenshot loses quality and any embedded information). Do not convert, crop or strip metadata on the originals. If a tool adds a visible mark or an invisible one (unverified), leave it and note it in the log. Save every image you look at for more than a glance: keepers into `assets/buzhou/photoreal/`, everything else into `assets/buzhou/photoreal/candidates/`. Add one row per image to `assets/provenance.csv` (section 7). Copy the tool and model name from the screen, never from memory.
5. **Licence terms have NOT been checked.** Before any commercial use, read the **current** terms for the exact tool and plan you used and write the result into `licence_notes` (section 7). Commercial use means anything posted, published, shown to a client or sold. Until then every image is "for internal review only".
6. **Photoreal is not a way to look human.** Every image that is ever published carries the badge, the first-line caption, the bio and the platform AI label (section 8). Never ask for a "candid", "selfie", "phone photo" or "day in the life" look, never add a location, and never describe any image as a place he visited. The house look is a plain, slightly formal studio portrait on purpose.
7. **If a tool refuses, or answers only in words,** reply "Please generate the image now." If it refuses, read the reason, do not reword the prompt to get round it, log it and tell Claude. Tools may restrict realistic people in some ways (unverified).
8. **Claude cannot do your look-alike check.** Claude does not identify real people from faces and must not be asked who the character resembles. Claude can give a first-pass look at a saved file against the checklist; it cannot make the wife's judgements.

---

## 2. STEP 1: the master reference R01

R01 is **one half-body portrait**: just above the head down to the belt line, front-facing, in Outfit A, hands below the frame edge. Photoreal faces do not hold up in multi-view turnaround sheets (hypothesis), so the other angles are made one by one in STEP 2 from the chosen master.

### 2.1 Prepare

- Make the folders (in your file manager, or ask Claude in this project folder): `assets/buzhou/photoreal/` already exists with a `.gitkeep`. Inside it make `candidates/` and `lookalike/` (screenshots and notes from the searches in section 6; keep these private, never post them).
- In each tool open a **new chat** named "buzhou photoreal R01".
- Keep this file open next to the chat. Copy a block, paste, send.

### 2.2 Gemini prompt for R01

The wording "ordinary East Asian adult features" is the neutral option from addendum 1.7. If the wife later chooses another option, change those words in both prompts and in the lock (3.2), and log the changed prompt.

```
I'm designing a fictional adult character for a studio that publishes openly AI-generated
characters. Please generate a fictional person: one photorealistic studio portrait, using the
specification below. After I choose a result, I'll ask for edits. This person is original. He is
not based on, copied from or meant to resemble any real individual. Do not put any text, letters,
numbers, logos or watermarks anywhere in the image.

Person: an adult man, stated age 28, who looks about 28 to 33. Ordinary East Asian adult features,
everyday and unexaggerated: a plain, ordinary look, not a glamour or beauty-retouched look.

Face: long-oval face with a moderately defined jaw and a straight, slightly square chin; medium
forehead; straight, medium-thick, dark brown-black eyebrows that are natural and very slightly
uneven; medium-sized dark brown almond-shaped eyes with natural eyelids, a calm level gaze and
natural catchlights; medium nose with a moderate bridge; medium-full lips; clean-shaven; fine
natural lines at the outer corners of the eyes; a mature adult face, clearly not a teenager or a
student.

Skin: light-to-medium, neutral-to-warm beige, matte, with natural fine texture: visible pores on
the nose and cheeks, faint shading under the eyes, slight natural unevenness. No airbrushing, no
glow, no plastic smoothness.

Hair: short black hair, about five centimetres on top, neat side parting, tapered sides and back,
natural texture with a few loose strands, natural hairline, not dyed.

Expression: calm and relaxed, lips closed, a very slight asymmetric smile, looking at the camera.

Build: slim-to-average, natural shoulders, upright relaxed posture, natural adult proportions.

Headphones (always present): over-ear closed-back headphones in matte charcoal grey, worn on the
head with the cups over the ears. Thin padded band, plain round-oval cups, fabric ear pads. No
logo, no text, no cable, no microphone, no lights, no metallic shine.

Outfit: a boxy light cool-grey coach-style jacket in matte fabric, zipped about two thirds, over a
plain crew-neck t-shirt in muted dark blue-grey slate. No logos, no text, no stripes. On the
jacket chest, on the wearer's left (the viewer's right), a small rectangular sewn woven patch
about four centimetres wide: off-white background, thin charcoal stitched border. On the patch, a
rising staircase of six flat squares in three columns that share a bottom edge: one square, then
two squares, then three squares, from the viewer's left to right, so the shape rises to the right.
Left column pale grey, middle column grey-blue, right column dark slate blue-grey. Flat matte
fabric, no shine, no digits, no letters, not a two-by-two grid, not a logo.

Framing: half-body portrait from just above the head down to the belt line. The body is angled
slightly (about fifteen degrees, turned toward the left edge of the image) and the face turns to the
camera. Both arms hang relaxed at his sides. The frame ends at the belt line, so the hands are below
the bottom edge of the image: no hands or fingers visible anywhere.

Background: plain seamless studio backdrop in a mid-light neutral cool grey, soft light falloff,
nothing else in the scene.

Photographic style: studio portrait photograph, 85 mm lens look, eye-level camera, sharp focus on
the eyes. One large soft key light from the front left with gentle fill, neutral daylight white
balance, soft natural shadows, muted natural colour. No beauty retouching, no skin smoothing, no
HDR, no lens flare, no heavy vignette. A composed studio portrait, not a phone snapshot or selfie.

Avoid: visible hands or fingers; text, letters, numbers, logos, brand marks, watermarks; jewellery
of any kind (earrings, chains, rings, watches); glasses; beard or stubble; tattoos; phones, food,
drinks or other objects; other people; real places; glossy or plastic skin; oversized or glassy
eyes; doll-like, anime-like or airbrushed looks; glamour styling; teenage or student look; school
uniform, lab coat, suit and tie; bare skin below the collarbone; tight clothing; sexualised pose;
strong or saturated colours; flags; any resemblance to a real person.

Output: 1 image, portrait orientation (4:5).
```

### 2.3 ChatGPT prompt for R01

Same content, written as labelled fields, which the bible guesses suits ChatGPT better (hypothesis).

```
GOAL: Generate a fictional person: one photorealistic studio portrait of an original adult man, for a
studio that publishes openly AI-generated characters. He is not based on, copied from or meant to
resemble any real individual. No text, letters, numbers, logos or watermarks anywhere in the image.
PERSON: adult man, stated age 28, looks about 28 to 33. Ordinary East Asian adult features, everyday
and unexaggerated; a plain, ordinary look, not a glamour or beauty-retouched look.
FACE: long-oval face, moderately defined jaw, straight and slightly square chin, medium forehead.
Straight, medium-thick, dark brown-black eyebrows, natural and very slightly uneven. Medium-sized dark
brown almond-shaped eyes with natural eyelids, calm level gaze, natural catchlights. Medium nose with
a moderate bridge. Medium-full lips. Clean-shaven. Fine natural lines at the outer corners of the
eyes. A mature adult face, clearly not a teenager or a student.
SKIN: light-to-medium, neutral-to-warm beige, matte, natural fine texture (visible pores on nose and
cheeks, faint shading under the eyes, slight natural unevenness). No airbrushing, no glow, no plastic
smoothness.
HAIR: short black hair, about five centimetres on top, neat side parting, tapered sides and back,
natural texture with a few loose strands, natural hairline, not dyed.
EXPRESSION: calm, relaxed, lips closed, a very slight asymmetric smile, looking at the camera.
BUILD: slim-to-average, natural shoulders, upright relaxed posture, natural adult proportions.
HEADPHONES (always present): over-ear closed-back headphones, matte charcoal grey, worn on the head
with the cups over the ears; thin padded band, plain round-oval cups, fabric ear pads. No logo, no
text, no cable, no microphone, no lights, no metallic shine.
OUTFIT: boxy light cool-grey coach-style jacket in matte fabric, zipped about two thirds, over a
plain crew-neck t-shirt in muted dark blue-grey slate. No logos, no text, no stripes.
PATCH: on the jacket chest, on the wearer's left (the viewer's right), a small rectangular sewn
woven patch about four centimetres wide, off-white background, thin charcoal stitched border. On it, a
rising staircase of six flat squares in three columns sharing a bottom edge: one square, then two
squares, then three squares, from the viewer's left to right, so the shape rises to the right. Left
column pale grey, middle column grey-blue, right column dark slate blue-grey. Flat matte fabric, no
shine, no digits, no letters, not a two-by-two grid, not a logo.
FRAMING: half-body portrait from just above the head down to the belt line; body angled slightly
(about fifteen degrees, turned toward the left edge of the image), face turned to the camera; both
arms hanging relaxed at his sides. The frame ends at the belt line, so the hands are below the
bottom edge of the image and no hands or fingers are visible anywhere.
BACKGROUND: plain seamless studio backdrop, mid-light neutral cool grey, soft light falloff, nothing
else in the scene.
STYLE: studio portrait photograph, 85 mm lens look, eye-level camera, sharp focus on the eyes; one
large soft key light from the front left with gentle fill; neutral daylight white balance; soft natural
shadows; muted natural colour. No beauty retouching, no skin smoothing, no HDR, no lens flare, no heavy
vignette. A composed studio portrait, not a phone snapshot or selfie.
AVOID: visible hands or fingers; text, letters, numbers, logos, brand marks, watermarks; jewellery of
any kind (earrings, chains, rings, watches); glasses; beard or stubble; tattoos; phones, food, drinks
or other objects; other people; real places; glossy or plastic skin; oversized or glassy eyes;
doll-like, anime-like or airbrushed looks; glamour styling; teenage or student look; school uniform,
lab coat, suit and tie; bare skin below the collarbone; tight clothing; sexualised pose; strong or
saturated colours; flags; any resemblance to a real person.
OUTPUT: 1 image, portrait orientation (4:5).
```

### 2.4 The Avoid list on its own

Chat tools have no separate negative-prompt box (assumption), so the avoid list lives inside the prompt. This copy is for two uses: paste it into a negative-prompt field **if** your tool has one (check the current screen), and keep it as the master version when you add to it. Add to it when QA finds a new failure; never remove from it; tell Claude to log the new item in the addendum. Negative phrases can backfire in image tools (hypothesis); where a fix works better as a positive statement ("the frame ends at the belt line"), section 10 says so.

```
Avoid: visible hands or fingers; text, letters, numbers, logos, brand marks, watermarks; jewellery
of any kind (earrings, chains, rings, watches); glasses; beard or stubble; tattoos; phones, food,
drinks or other objects; other people; real places; glossy or plastic skin; oversized or glassy
eyes; doll-like, anime-like or airbrushed looks; glamour styling; teenage or student look; school
uniform, lab coat, suit and tie; bare skin below the collarbone; tight clothing; sexualised pose;
strong or saturated colours; flags; any resemblance to a real person.
```

### 2.5 What to generate

- **4 runs in each tool, so 8 images.** Run the same prompt four times. Do not edit the prompt between runs: the point is to see how much the face varies.
- Save each with the download button into `assets/buzhou/photoreal/candidates/` as `R01_pr_cand_gem1.png` to `R01_pr_cand_gem4.png` (Gemini) and `R01_pr_cand_gpt1.png` to `R01_pr_cand_gpt4.png` (ChatGPT). If the tool gives `.jpg` or `.webp`, keep that extension; do not convert.
- Write down the date, time, tool name and model name shown on screen now, while the chat is open.
- Expect that none is perfect. The patch and small defects can be fixed; the face, the age read and the hands cannot be rescued by editing.

### 2.6 How to choose

1. **Quick-kill (you, 5 minutes).** Remove any candidate with: any visible hand or finger; any text, number or logo; a teenage, student or baby-faced look; glassy or oversized eyes; plastic skin; glasses, beard, jewellery or tattoo; a candid, selfie or snapshot look; a wrong backdrop or props; a bare-chested, tight or open-collar look; a resemblance that makes you think of anyone. Log each removed candidate with one word of reason.
2. **Shortlist up to three**, in this priority: (a) reads as an ordinary adult man of about 28 to 33; (b) natural skin and calm eyes; (c) the written face (long oval, defined jaw, straight brows); (d) headphones and patch roughly right; (e) house look (grey seamless backdrop, soft light).
3. **Blind pick with the wife.** Rename copies of the shortlist `A`, `B`, `C` so neither of you knows which tool made which. Show them on a screen at full size, then on a phone. Each writes down a first choice and one sentence on why, separately, then compare. If you disagree, the wife's pick on age read, naturalness and Taiwan plausibility decides.
4. **Run section 5** on the winner. If it fails something that is a defect rather than a design problem (a wrong patch, a stray mark), fix it with a local edit or follow-up (section 10), save as a new file in `candidates/` (for example `R01_pr_cand_gem2_fix1.png`), log it and run section 5 on that file. If it fails the adult read, the uncanny look or resemblance, go back to the shortlist.
5. **Do the quick tests today** (section 6): the wife's age guess (6.1) and the first reverse-image search on the winner's face crops (6.2 part A). Do not spend more than about two hours on follow-ups before the full look-alike check passes; everything built after R01 is provisional until it does.
6. **Copy the final winner** to `assets/buzhou/photoreal/R01_pr_master_v1.png` (copy, do not rename; keep the original in `candidates/`). **Never edit or overwrite this file.** Every later change is a new file (v2, v3).
7. **Log** all 8 candidates and the master copy (section 7).

If all 8 fail, do not keep rerolling. Read section 10, add one corrective line to the prompt (and to the Avoid list if it is a "don't"), and run one more round of 4. After three rounds, or if the same defect appears in two rounds of four in both tools, stop and ask Claude for a revised prompt.

---

## 3. STEP 2: lock it

Goal: every later image shows the same man. The chosen master, not the words, carries the identity.

### 3.1 Rules for every follow-up image

1. **Always attach `R01_pr_master_v1.png`**, whether you continue in the same chat or start a new one. The tool does not reliably remember it (hypothesis). Attach at most three images, and only the character's own generated files. A second attachment is allowed only where a block says so.
2. **New chat or same chat?** A **new chat** for each new image type is the cleaner default, because long chats drift. Staying in the same chat is fine for a quick tweak to the image you just made, but attach the master again anyway. If a result drifts, restart from the master, never from the previous generated image.
3. **Message order:** attach the image(s), paste the **character lock** (3.2), then paste the block for the image you want.
4. **One change per image.** The block's `CHANGE ONLY` line is the one thing that may differ from the master.
5. **Generate 4, save all, check all** (section 5), keep the best, log everything.
6. **Three tries, then stop.** If one defect survives three rounds, change the framing so it cannot appear (hands are the usual case), or ask Claude for a better prompt.
7. **Which side is the patch on?** The prompts put it on the wearer's left (the viewer's right). Whatever side the chosen master shows is the rule for every image from now on. Write it at the top of your log notes. If a result has it on the other side, it fails; regenerate. **Never mirror or flip an image in an editor**: that moves the patch and the hair parting.
8. **Hands rule for every block:** hands out of frame, or fully inside pockets with no fingers or thumbs showing. No block ever asks for a gesture or a held object.

### 3.2 The character lock (paste at the start of every follow-up)

```
CHARACTER LOCK. The attached image is the studio's own generated image of one fictional man. It is
the source of truth for identity. Generate the SAME fictional person: same long-oval face, moderately
defined jaw, straight medium-thick dark eyebrows, dark brown almond eyes, medium nose, medium lips,
same natural skin tone and texture, same short black side-parted hair, same age (looks about 28 to
33), same slim-to-average build. He always wears the same matte charcoal over-ear headphones (no
logo, no cable) and the same small sewn patch on the chest of his outermost garment (off-white, thin
charcoal border, a rising staircase of six squares in three columns of one, two and three squares:
pale grey, grey-blue, dark slate; on the same side of the chest as in the attached image). Keep the
same studio look: mid-light neutral cool-grey seamless backdrop, one soft key light from the front
left, natural unretouched skin, muted colour. No hands or fingers visible. No text, numbers, logos,
watermark, jewellery, glasses or beard. He is a fictional person, not any real individual. If the
face changes in any way, say so and redo it.
```

### 3.3 Order of work and file names

Kept files go in `assets/buzhou/photoreal/`. Candidates go in `assets/buzhou/photoreal/candidates/` as `<ID>_pr_<name>_cand_gem1.png` (Gemini) or `_cand_gpt1.png` (ChatGPT). Version numbers go up (v1, v2); never overwrite. A kept file is a copy of the chosen candidate with `_v1`; the original stays in `candidates/`. Log the candidate rows and the keeper row.

| Order | ID | What | Kept file name | Where | When |
|---|---|---|---|---|---|
| 1 | R01 | Master half-body portrait | `R01_pr_master_v1.png` | section 2 | Today |
| 2 | R08 | Small-size test sheet (made by shrinking, not generated) | `R08_pr_small_test_v1.png` | 4.6 | Today |
| 3 | R02 | Face set: front, three-quarter left, three-quarter right, profile | `R02_pr_face_front_v1.png`, `..._3q_left_v1.png`, `..._3q_right_v1.png`, `..._profile_v1.png` | 3.4 | Today |
| 4 | R06 | Corner (PiP) busts, left and right | `R06_pr_pip_left_v1.png`, `R06_pr_pip_right_v1.png` | 4.4 | Today |
| 5 | R03 | Ten expressions E01 to E10 | `R03_pr_E01_v1.png` ... `R03_pr_E10_v1.png` | 4.1 | Next sitting |
| 6 | R04 | Outfits B, C, rain shell, vest | `R04_pr_outfitB_v1.png` ... | 4.2 | Next sitting |
| 7 | R05 | Framings: waist-up, full-body views | `R05_pr_waist_A_v1.png`, `R05_pr_full_front_A_v1.png` ... | 4.3 | Later |
| 8 | R07 | Avatar | `R07_pr_avatar_v1.png` | 4.5 | Later |
| 9 | R09, R10 | Generic 示意 set plates, and him placed in one | `R09_pr_set_desk_v1.png`, `R10_pr_inset_desk_v1.png` | 4.7 | Only after the wife signs off |

The stylised pack's pose sheet (P09 to P11) is **dropped**: those poses need hands. The checklist card, date stamp and any pointer are graphics added in editing.

### 3.4 R02: face set (four separate images)

Attach `R01_pr_master_v1.png`, paste the lock, then the template with one VIEW line. Four runs of the template, one VIEW each.

```
CHANGE ONLY: the camera angle and framing.
FRAMING: headshot from just above the head to the top of the chest, {VIEW}. Neutral calm
expression, lips closed. Same outfit, headphones, backdrop and lighting. No hands visible.
OUTPUT: 1 image, portrait (4:5).
```

The four VIEW lines (replace `{VIEW}` with one at a time):

```
face front-on to the camera
head and shoulders turned about 35 degrees toward the left edge of the image, eyes toward the camera
head and shoulders turned about 35 degrees toward the right edge of the image, eyes toward the camera
full profile facing the left edge of the image, so the headphone band and cup are seen from the side
```

These four plus R01 are the face references for the look-alike crops (6.2) and the same-person test (6.4).

---

## 4. Expressions, outfits, framings, corner busts, avatar

Every block here is used the same way: attach `R01_pr_master_v1.png`, paste the **character lock (3.2)**, then paste the block. "Left" means toward the left edge of the image.

### 4.1 R03: expression set (ten single images)

Source for the ten expressions: bible 5.4, adapted for photoreal: restrained, lips closed or barely parted, no teeth-baring grin, no laughing, no tears, no anger, no wink. Single images are more reliable than ten faces in one picture (hypothesis).

```
CHANGE ONLY: the expression.
EXPRESSION: {PASTE ONE LINE FROM THE LIST BELOW}
FRAMING: headshot from just above the head to the top of the chest, face toward the camera unless
the expression line says otherwise. Same outfit, headphones, backdrop and lighting. No hands
visible. Keep it restrained and natural: no wide smile, no laughing, no teeth-baring, no tears, no
anger, no wink.
OUTPUT: 1 image, portrait (4:5).
```

The ten lines, in order E01 to E10 (name files `R03_pr_E01_v1.png` ... `R03_pr_E10_v1.png`; the E-number stays out of the prompt):

```
Neutral, calm: relaxed face, lips closed, eyebrows level, steady gaze at the camera
Explaining: head tilted slightly, lips slightly parted as if mid-sentence with teeth barely visible, gaze at the camera
Pointing attention: eyebrows slightly raised, head turned a few degrees, eyes looking toward the right edge of the image
Checking: eyes slightly narrowed, looking down and a little to the side as if reading something just out of frame, lips closed
Mild smile: closed-lip smile with a slight lift in the cheeks, gaze at the camera
Uncertain: one eyebrow slightly higher than the other, lips pressed together, gaze at the camera
Caution: eyebrows drawn slightly together, mouth level, serious but not angry, gaze at the camera
Correcting: small bow of the head, soft eyebrows, lips closed, eyes lifted to the camera
Pleased, light: small closed-lip smile, eyes gently crinkled, gaze at the camera
Polite decline: head tilted slightly, lips pressed, soft eyebrows, a small apologetic look, gaze at the camera
```

Use in the channel (from the bible): E01 for most corner pictures and the avatar; E04 for 「第 0 步」 (step zero: check the date); E06 for "go by the official page"; E07 for privacy and risk points; E08 for corrections; E10 for questions he will not answer. Off-camera gaze (E03, E04) is where photoreal eyes go wrong most often: check the eye line carefully (section 5, check 8).

### 4.2 R04: outfits (Outfit A is the master)

Wardrobe lock: only A, B, C and the listed Taiwan seasonal variants (addendum 3). The headphones and the patch appear in every outfit. Use the half-body framing. The rain shell and the vest are shot dry in the studio: no rain, **no umbrella in the picture** (his hands are out of frame).

Outfit B, studio knit (close-ups, cool season):

```
CHANGE ONLY: the outfit. This is Outfit B, the studio knit.
OUTFIT: a fine-gauge crew-neck knit sweater in muted dark ink-slate blue-grey, no jacket. The same
small sewn patch on its chest, on the same side as in the attached image. Charcoal straight-leg
trousers. No logos, no text, no stripes.
FRAMING: half-body, from just above the head down to the belt line, body angled slightly, face to
the camera, arms hanging relaxed at his sides, the frame ending at the belt line so the hands are below it and no hands are visible. Same headphones, backdrop and lighting.
OUTPUT: 1 image, portrait (4:5).
```

Outfit C, warm-day shirt (hot, humid weather):

```
CHANGE ONLY: the outfit. This is Outfit C, the warm-day shirt.
OUTFIT: a short-sleeve collared shirt in muted dusk grey-blue, matte lightweight cotton, buttoned
so that at most the top button is open and no chest shows, one fold in each sleeve cuff, and a small flat
chest pocket on the wearer's left carrying the same small sewn patch. Charcoal straight-leg
trousers. Modest and plain. No logos, no text, no stripes.
FRAMING: half-body, from just above the head down to the belt line, body angled slightly, face to
the camera, arms hanging relaxed at his sides, the frame ending at the belt line so the hands are below it and no hands are visible. Same headphones, backdrop and lighting.
OUTPUT: 1 image, portrait (4:5).
```

Rain-season variant:

```
CHANGE ONLY: the outfit. This is the rain-season variant of Outfit A.
OUTFIT: Outfit A (the boxy light cool-grey coach jacket over the muted slate t-shirt) with a light
matte hooded rain shell in muted dusk grey-blue worn over it, hood down, plain, no reflective
strips, no logos. The same small sewn patch on the chest of the shell. It is a dry studio shot:
no rain, no umbrella, nothing else in the picture.
FRAMING: half-body, from just above the head down to the belt line, body angled slightly, face to
the camera, arms hanging relaxed at his sides, the frame ending at the belt line so the hands are below it and no hands are visible. Same headphones, backdrop and lighting.
OUTPUT: 1 image, portrait (4:5).
```

Cool-season variant:

```
CHANGE ONLY: the outfit. This is the cool-season variant of Outfit A.
OUTFIT: Outfit A plus a slim lightweight padded vest in charcoal worn over the jacket, plain, no
logos. The same small sewn patch on the chest of the vest. Not a heavy snow coat, no autumn-leaf
styling.
FRAMING: half-body, from just above the head down to the belt line, body angled slightly, face to
the camera, arms hanging relaxed at his sides, the frame ending at the belt line so the hands are below it and no hands are visible. Same headphones, backdrop and lighting.
OUTPUT: 1 image, portrait (4:5).
```

The hot-weather variant is Outfit C. 農曆新年 needs no costume change: no all-black or all-white, no red clothing.

### 4.3 R05: framings (waist-up and full-body)

The headshot is R02, the half-body is R01 and R04, the corner bust is 4.4 and the avatar is 4.5. These two blocks add the waist-up and the full-body shots. In both, **the hands are inside pockets**; thumbs hooked outside are the usual failure.

Waist-up (hands in the jacket pockets):

```
CHANGE ONLY: the framing and pose. Waist-up.
FRAMING: from just above the head down to the hips, standing relaxed, body turned slightly, face
toward the camera. Both hands are inside the jacket pockets: only the sleeves and the pocket
openings are visible, with no fingers and no thumbs hooked outside the pockets. Neutral calm
expression, lips closed. Same outfit (Outfit A), headphones, patch, backdrop and lighting.
OUTPUT: 1 image, portrait (4:5).
```

Full-body (replace `{VIEW}` with one of the four lines below):

```
CHANGE ONLY: the framing and pose. Full-body.
FRAMING: full-body standing view from head to feet, {VIEW}. Feet fully in frame on a plain seamless
floor of the same grey with a soft natural contact shadow. Both hands inside the jacket pockets, no
fingers and no thumbs visible. Plain off-white low-top sneakers with no stripes, marks or logos.
Neutral calm expression, lips closed. Camera at about chest height with a long lens look, no
wide-angle distortion. Same outfit (Outfit A), headphones, patch, backdrop and lighting.
OUTPUT: 1 image, portrait (2:3 or 3:4).
```

```
front-on to the camera
turned about 35 degrees toward the left edge of the image
turned about 35 degrees toward the right edge of the image, patch still visible on the chest
side view facing the left edge of the image
```

For Outfit B, Outfit C or a seasonal variant, change "Outfit A" to the outfit name and "jacket pockets" to "trouser pockets" in both blocks. Outfit C shows bare forearms: that is fine, but the hands must still be fully inside the pockets.

Optional, only if the wife approves headphones around the neck (addendum 10 item 6): add to the full-body block: `The headphones rest around his neck instead of on his head; both ears are fully visible and natural, with no earrings.` Check the ears hard (section 5).

### 4.4 R06: corner (PiP) busts, left and right

The corner picture sits beside the content and he faces toward it. Make left and right as **two separate runs**. Never flip one: a flip moves the patch and the parting. The rounded-square bone frame and the badge are added in editing, so the picture itself has no frame.

```
CHANGE ONLY: the framing. Picture-in-picture bust facing left.
FRAMING: chest-up, head and body turned a slight three-quarter turn toward the left edge of the
image (not a profile), face clearly visible, calm neutral expression, lips closed, headphones on,
the patch visible on the chest, no hands visible. The figure fills about 80 percent of the image
height, centred, with an even margin of grey backdrop all round. No frame, no border, no rounded
corners, no ground shadow.
OUTPUT: 1 image, square (1:1).
```

```
CHANGE ONLY: the framing. Picture-in-picture bust facing right.
FRAMING: chest-up, head and body turned a slight three-quarter turn toward the right edge of the
image (not a profile), face clearly visible, calm neutral expression, lips closed, headphones on,
no hands visible. The patch must stay visible on the same side of the chest as in the attached
image, so keep the turn small. The figure fills about 80 percent of the image height, centred, with
an even margin of grey backdrop all round. No frame, no border, no rounded corners, no ground
shadow.
OUTPUT: 1 image, square (1:1).
```

### 4.5 R07: profile avatar

The avatar is the image the Instagram AI-generated-profile label is about, so it is the most label-sensitive picture. Generate it, or crop it from an approved image (a crop is a human edit: log it with its parent file).

```
CHANGE ONLY: the framing. Avatar.
FRAMING: tight head and shoulders, front-on, face centred and filling about 60 percent of the image
width, headphones fully visible, neutral calm expression, lips closed, no hands visible, grey
backdrop visible around the head. Leave enough margin that a circular crop keeps the whole head and
both headphone cups.
OUTPUT: 1 image, square (1:1).
```

Crop and finish checklist (in an editor, on a copy):

1. Preview a circle over the square. Both headphone cups, the whole head and the chin sit inside the circle; the face centre is near the middle (about 50% across, 45% down; assumption). Platform crop shapes and sizes are unverified: check each platform's current guidance.
2. Add a small 「AI」 tag in editing (typeset, never generated): bone fill, charcoal letters, in a corner that survives the circle. The wife decides the final wording (addendum 10 item 7).
3. Check at 40 and 96 pixels: still reads as an adult, headphones still visible, tag still readable.
4. Export a copy; keep the untouched original. Log both.

### 4.6 R08: small-size test (no prompt; do this right after you pick the master)

It is a shrinking job, not a generating job. Log the result as an edited asset (tool "manual resize", prompt "none, derived from R01_pr_master_v1.png").

1. Crop the head and shoulders from the master into a copy. Do not touch the master.
2. In any basic image tool make copies about **64, 96 and 128 pixels** in head height. Put them on the studio grey backdrop, on bone `#EEECE7` and on a dark ground `#2B3038`. Save as one image, `R08_pr_small_test_v1.png`.
3. Look at it at normal viewing size, not zoomed. Can you still see the headphones? Does he still read as an adult man and not a student? Does he look like a plausible real person at this size, and is that why the badge must be added (section 8)?
4. This image is what the wife looks at for the small-size age guess.

### 4.7 Optional, later: generic 示意 set plates (R09) and him placed in one (R10)

**Only after the wife has signed off** (addendum 4.4 and 10 item 9). The first sittings and the STOP 3 samples use the plain studio backdrop only. Plates are generic and unnamed: no real place, no brand, no signs, no screens. They are illustrations of "a kind of place" and always carry the badge plus a 「示意」 label added in editing; no caption ever calls one his desk, room or café. The wife runs the Taiwan-ness check (`research/culture.md` 7.6).

Plate: desk corner (no people).

```
Generate an empty photorealistic interior with no people: a generic desk corner,
shown plainly. A plain small desk against a wall with nothing on it except a small desk fan; a
tiled or laminate floor edge with no shoes in view; a power strip with Taiwan-style Type A and
Type B sockets (two flat parallel slots, and a round ground pin on the B type); a split air
conditioner high on the wall; a window with a plain metal security grille; a round ceiling light. No
posters, no books with titles, no screens, no signs, no writing, no brands. Soft neutral daylight,
plain and slightly formal, not a lifestyle photo.
OUTPUT: 1 image, landscape (3:2).
```

Plate: office partition (no people).

```
Generate an empty photorealistic office interior with no people: a generic office partition desk
with fluorescent ceiling lights, low desk partitions, a document tray and a plain desk lamp. No
posters, no whiteboard writing, no laptops or screens, no branded items, no readable text. Soft
neutral light, plain and slightly formal, not a lifestyle photo.
OUTPUT: 1 image, landscape (3:2).
```

Plate: study room (no people).

```
Generate an empty photorealistic study room with no people: a partitioned desk with plain wood
dividers, a desk lamp, a quiet-room feel. Any sign is a blank panel with no writing. No school
uniforms, no posters, no books with titles, no screens. Soft neutral light, plain and slightly
formal, not a lifestyle photo.
OUTPUT: 1 image, landscape (3:2).
```

Place him (attach the master first and the chosen plate second; this block overrides the backdrop sentence of the character lock):

```
CHANGE ONLY: the background. The second attached image is a generic empty set: use it as the
background and keep its content unchanged.
FRAMING: waist-up, standing a little way from the desk at a respectful distance, not touching or
using anything, hands inside the jacket pockets, no fingers visible, neutral calm expression, lips
closed. Same outfit (Outfit A), headphones and patch. Light him to match the set naturally, keeping
the soft look.
OUTPUT: 1 image, landscape (3:2).
```

---

## 5. Pass/fail checklist (tick for every image you keep)

For plates with no person (R09) use checks 7, 12, 13 and the wife's Taiwan-ness check. Hand-made files (R08, badge artwork) get checks 7 and 12 only.

Copy this section once per kept image, or tick it in a note beside the file. For a discarded image, one word of reason in the log is enough. Optional: ask Claude (in Claude Code, in this folder) to look at a saved file and tick a first pass. It can miss details, it does not identify real people, and it cannot make the wife's judgements on age, naturalness, colour read or Taiwan details.

### 5.1 Main checks

| # | Check | How to check, in plain words | Pass | If it fails |
|---|---|---|---|---|
| 1 | **Adult read** | Look at full size and at 64, 96 and 128 px head height (4.6). Mature jaw, neck and shoulders; fine lines at the outer eye corners; adult haircut; practical adult clothes; no school cue; no baby softness. He should read about 28 to 33, never younger. The wife's blind age guess (section 6) | [ ] | **Reject, do not retouch.** Regenerate. If 2 of 4 look young, add the age-cue line from section 10 first |
| 2 | **Same face as the master** | Put the new image beside `R01_pr_master_v1.png`. Compare in order: jaw and chin; eyebrows; eye shape and spacing; nose; lips; hairline and parting; skin tone; neck. Any of them moved? | [ ] | Face moved: **regenerate in a fresh chat** with the master attached. Do not edit the face |
| 3 | **Hands** | No hand, finger or thumb visible anywhere. Zoom to 200 percent on the lower edge, sleeve ends and pocket openings. No thumbs hooked out of pockets. No hand-like shapes in cloth folds | [ ] | Hand procedure, section 10.2 |
| 4 | **Teeth** | Lips closed by default. If teeth show (E02 only), they are an even natural row, not too many, not fused, not bleached, no gap oddities | [ ] | Regenerate with "lips closed". If teeth keep appearing, drop the expression |
| 5 | **Ears and headphones** | Cups sit over the ears, same design as the master, band follows the head, hair around the cups looks natural, nothing fuses into skin. Around the neck: both ears visible, same shape, no earrings | [ ] | Regenerate. If one defect, a local edit of that area |
| 6 | **No jewellery, glasses, beard, tattoo, watch** | None designed, so none allowed. Look at ears, neck, chin, wrists, fingers | [ ] | Regenerate; if it persists, restate "no jewellery of any kind" as a follow-up |
| 7 | **Text, numbers, logos, garbled characters** | Look at the patch, zip pull, tags, sneakers, headphone cups, backdrop and every corner. No letters, digits, squiggles that imitate writing, brand marks or watermarks you did not expect. Any Chinese character at all is a fail (Chinese is added later in editing) | [ ] | **Regenerate.** One small mark: local edit. Never keep a generated character |
| 8 | **Uncanny eyes** | Both eyes look the same direction; same iris size and colour; catchlights in the same place in both eyes; round pupils; natural lids; eye whites not glowing; the gaze goes where the expression says. No dead stare | [ ] | Regenerate. If it keeps happening in one expression, drop that expression for now |
| 9 | **Skin too smooth or plastic** | At 100 percent: pores and fine texture on nose and cheeks; no waxy sheen; no repeated texture pattern; no HDR crispness. Not airbrushed | [ ] | Regenerate with "natural fine skin texture, visible pores, no smoothing". Do not smooth or sharpen in an editor |
| 10 | **Resemblance to real people** | Gut check first: does he remind you of anyone, any public figure, any existing character? Then the full look-alike check in section 6 | [ ] | **Any doubt: do not keep.** Change the offending feature through a revision of the addendum with the wife, not by retouching |
| 11 | **Clothing and patch consistent** | Exactly one of Outfit A, B, C or a listed variant. Patch: six squares in columns of one, two and three rising to the viewer's right; pale grey, grey-blue, dark slate; off-white backing and thin charcoal border; on the same side as the master; no digits; not a logo | [ ] | Patch only: local edit or follow-up, two rounds at most, then the three-bar fallback (addendum 2.2) with the wife's approval. Wrong outfit: regenerate with the OUTFIT line restated |
| 12 | **House look and framing** | Plain mid-light grey seamless backdrop; one soft key light from the front left; muted colour; allowed framing only (addendum 4.1); no props, people, phone, food, place; **not a candid or selfie look** | [ ] | Regenerate with the style paragraph restated |
| 13 | **No logos, brands, plates, flags, money, party colours, mourning look** | Squint: muted grey family, no saturated blue or green, no blue-and-white slogan look, no all-black or all-white outfit. The wife confirms the colour read | [ ] | Strong colour cast: regenerate. Mild cast: regrade a copy and log it |
| 14 | **Modest and neutral** | No open collar showing the chest, no tight cloth, no sexualised pose or look, no body or health imagery | [ ] | **Reject** |

### 5.2 Part B: locked features (tick each against the master)

| # | Locked feature | Pass |
|---|---|---|
| 1 | Long-oval face, moderately defined jaw, straight slightly square chin | [ ] |
| 2 | Straight, medium-thick, dark eyebrows | [ ] |
| 3 | Dark brown almond eyes, medium size, calm gaze, natural lids | [ ] |
| 4 | Medium nose, medium-full lips | [ ] |
| 5 | Light-to-medium neutral-to-warm skin with natural texture | [ ] |
| 6 | Short black side-parted hair, natural hairline | [ ] |
| 7 | Clean-shaven; no glasses; no marks | [ ] |
| 8 | Slim-to-average build, natural shoulders | [ ] |
| 9 | Matte charcoal over-ear headphones, no logo, no cable, no microphone, no lights | [ ] |
| 10 | Patch as in check 11, same side as the master | [ ] |
| 11 | Outfit is exactly A, B, C or a listed variant | [ ] |
| 12 | Studio grey backdrop and soft front-left light | [ ] |
| 13 | Allowed framing, hands out of frame or hidden | [ ] |
| 14 | No jewellery, text, logos | [ ] |
| 15 | Adult reading (check 1) and about 28 to 33 | [ ] |

### 5.3 Regenerate, edit the prompt, or edit the image?

| Situation | Do this |
|---|---|
| Whole-design problem (face, age read, uncanny look, resemblance) | **Regenerate** from the master in a fresh chat |
| The same defect in 2 or more of 4 runs | It is systematic. **Edit the prompt**: add one corrective line (section 10), then 4 more |
| One local defect in an otherwise good image (a stray mark, a wrong patch) | **Edit the image** with the tool's edit or select-region mode if it has one (hypothesis), or a follow-up such as "Change only the chest patch. Keep everything else identical." Two rounds at most |
| The face starts to move after several edits | Stop. Start a fresh chat from `R01_pr_master_v1.png` |
| The same defect survives three rounds | Stop. Change the framing so it cannot appear, or ask Claude for a revised prompt |
| The tool refuses or answers only in words | Reply "Please generate the image now." If it refuses, read the reason; do not reword to get round a refusal |

---

## 6. The human tests

Both of the first two are gates for approving the master (addendum 8). Do the quick version today; do the full version before the master is used for anything real. The wife's minutes are the scarce resource: do the tests in one sitting with her.

### 6.1 Test 1: the age-guess test (stricter than the stylised pack)

1. Prepare the winner at full size and `R08_pr_small_test_v1.png`.
2. Ask the **wife first, alone**, before she knows the design age. Do not say "28", "adult" or "check whether he looks young". Say only: "Please write one number for how old you think this man is, and one word for what he does. There are no right answers." Full size first, then the small version.
3. Repeat with **5 or more others** (six or more in all; at least 3 living in Taiwan, at least two over 40), one at a time, same words. Write each answer as given: initials, number, word.
4. **Hard fail:** any single guess (the wife's or the panel's) **under 25**, a median guess **under 28**, or the word student or young (學生, 年輕, 童顏). Reject the image and go back to the shortlist.
5. **Warn (hold):** a median of 28 or 29, or any single guess of 25 to 27. Do not approve. Regenerate with the age-cue line (section 10) and retest with the same people plus two new ones.
6. **Pass:** none of the above. **Target:** median 28 to 33. This is the same rule as the 方寸 and 色環 packs (aligned in the cross-pilot check of 2026-10-11; the first version of this pack accepted a median of 27 and one guess under 25).

### 6.2 Test 2: the look-alike check (stricter than the stylised pack)

**What it proves:** he does not resemble a real person, anyone famous, a politician, or an existing virtual character (Ground rule 2). Source: addendum 8.3.

**Part A: reverse-image search of face crops (about 40 minutes; by hand; no login scraping)**

1. Make the crops from the winner and from three variants (R02 front, three-quarter and profile are ideal): a **tight front face**, a **three-quarter face**, a **profile** and the **full half-body**. Save them in `assets/buzhou/photoreal/lookalike/`. These are the studio's own generated images. Never use a photo of a real person for any part of this. They are unpublished drafts and you upload them to third-party search sites: check each site's current terms on what it does with uploaded images (unverified) and use only sites you are comfortable with.
2. Open a **private, logged-out browser window**, not signed in to personal accounts.
3. Use at least three public reverse-image tools by hand, one image at a time: **Google Lens, Bing Visual Search and TinEye**. Names and addresses change, so use whatever is current. If a tool insists on an account, skip it. No scripts, no automated tools, nothing that logs in to someone else's account.
4. For each image and tool, read at least the first two screens of visually similar results. Write down the date, the tool, the page address of any close match and a one-line description (person, character, mascot, logo or stock photo).
5. **These tools may return photos of real people. Do not try to find out who anyone is, do not contact anyone, and do not save, share or repost their photos.** A close match to a real person is a stop: tell Claude and the wife, and do not keep that master.

**Part B: stock-look check (about 10 minutes)**

6. In an image search, type plain words that match the prompt (for example an East Asian man, short black hair, grey studio backdrop, over-ear headphones). Compare the first page by eye with the master. Generators sometimes reproduce a stock look. Note anything that looks too close.

**Part C: the wife's local-public-figure check (about 10 minutes)**

7. Show her the master, one face-set image and one expression image, at full size and on her phone. Ask the open question: "Does this face remind you of any person you have seen on television, in film, in music, in sport, in the news, in politics or in online video, in Taiwan or elsewhere? Does it remind you of anyone you know personally?" Write her answer **in her own words**. Do not suggest names. She may look up a name she thinks of; she never uploads anything.
8. **If she names a person, the master fails.** A politician or election candidate is also a Ground rule 6 problem (the local elections are recalled for 2026-11-28, unverified).

**Part D: blind panel (combine with Test 1, same sitting)**

9. Show the master to **at least 5 people, at least 3 of whom live in Taiwan**, mixed ages. After the age question ask: "Does this remind you of any real person, anyone famous, or any character?" Write every answer in their words. Do not prompt with names. Ask them not to save or share the images.
10. If one person names someone, the wife compares with that person's public photos by eye. If she or a second panel member sees it, fail. If two or more name the same person, fail.

**Part E: existing virtual humans (about 15 minutes)**

11. Compare side by side with the photoreal virtual influencers described in `research/competitors.md` sections 4 and 5 (look them up there; their names are not repeated here), and with the headphone-wearing virtual singers and streamers covered by bible 5.7. The same hair, headphones and jacket silhouette on a recognisable existing character is a fail.

**Result and what to do**

12. **Pass:** no unexplained close match in any search, no named person from the wife or the panel, no politician, no similarity to an existing virtual character. **Any doubt is a fail.** Fix through a revision of the addendum and the wife's re-approval, then re-run. Do not retouch.
13. Re-run before launch, at the week-6 review, after any redesign, after any complaint, and on any later image whose face visibly differs from the master (which you should have rejected anyway).
14. A credible look-alike claim means: take the material down within 24 hours, pause, re-run, log it, and ask the lawyer (`research/legal.md` question 20). Keep the provenance rows ready as the record of origin.
15. Log each run in `personas/buzhou/lookalike_log.md` (create it from this template) and write the ID into `licence_notes`:

```
LOOK-ALIKE LOG (PHOTOREAL)
LA-PR-001   date: ____-__-__   images: assets/buzhou/photoreal/R01_pr_master_v1.png + crops   checked by: ____

A. Reverse-image search of face crops (logged out, by hand)
 crop (front / 3-4 / profile / full) | tool | date | top matches (page address + one line) | person, character, mascot, logo or stock? | concern Y/N
 ____ | ____ | ____ | ____ | ____ | ____

B. Stock-look check: done Y/N     notes: ____

C. Wife's local-public-figure check (her own words; nothing suggested): ____
   Named a person?  Y / N       Reminds her of someone she knows?  Y / N

D. Blind panel (at least 5, at least 3 living in Taiwan)
 initials | age guess | one word | "reminds you of..." (their words) | concern Y/N
 ____ | ____ | ____ | ____ | ____

E. Existing virtual humans compared (competitors.md 4 and 5): done Y/N    notes: ____

Result: PASS / FAIL / HOLD      Decided by: ____   Date: ____
Re-run due: before launch / week-6 review / after any redesign or complaint
```

### 6.3 Test 3: uncanny read, real-person read, disclosure legibility (new)

Show five viewers (the same panel works) the master at full size and at phone size, one smiling expression (E05 or E09) and one with a slightly open mouth (E02).

1. **Uncanny.** Ask "Does anything look off, fake or creepy? Where?" (open answer), then "How natural, 1 to 5?" **Pass:** median 4 or more and no more than one person flags the eyes or the mouth. Two flagging the same area: fail; fix that area (section 10).
2. **Real-person read (information only).** Ask "Is this a photo of a real person?" Write down the count. If four or five say yes, the disclosure risk is high: use the largest badge and the first-line wording in section 8.
3. **Disclosure legibility (strict).** Show the image **with** the 「AI 生成｜虛擬角色」 badge and the first caption line added (section 8). Ask "Is it clear whether this is a real person?" **Pass: all five say it is an AI character.** Any "not sure": enlarge or reposition the badge and strengthen the line, then retest. Ground rule 1 depends on this test.

### 6.4 Test 4: same-person test (new)

Show six images in one unlabelled row: the master, a face-set image, two expressions, an Outfit B image and a full-body image. Ask "How many different people?" **Pass:** every viewer says one. If anyone says two, find the drifting image and reject it.

### 6.5 Later tests, not today

- The three pilots' headshots (or the three front waist-up images) in one row at about 110 px, once all three masters exist, on a laptop and on a phone, unlabelled. Ask the wife and at least four others (five viewers or more; the age-guess panel can be reused), two seconds each: "Same person, sisters, or different people?" Pass: all say different people. Fail: two or more say same person or sisters for any pair. Fix by changing a design attribute of the character that fails, not by editing (addendum 9; `README-photoreal.md` section 3). Also the stylised-era checks in `pipeline/image-pack/README.md` section 8.
- Re-run `personas/palette_check.py` with the studio grey ground when the wife accepts it (addendum 5.2).

---

## 7. Provenance and licence

Rule (BRIEF ground rule 2; bible 5.9): `assets/provenance.csv` gets **one row for every image you saved or considered, kept or discarded.** That means all 8 R01 candidates, every run of every later image, the copy that becomes `R01_pr_master_v1.png`, and every edited or derived file (a resize, a crop, a local edit, an avatar crop, a regrade). Download every image the tool gives you, even ones you reject on sight, and log it with one word of reason. Never delete a row; corrections go in a new row at the bottom.

Columns, already in the file: `timestamp,asset_path,persona,tool,model,prompt,licence_notes`.

- `timestamp`: ISO 8601 with the offset (Taiwan time is `+08:00`; if you are elsewhere write your real offset and keep it consistent).
- `asset_path`: path from the project folder, for example `assets/buzhou/photoreal/candidates/R01_pr_cand_gem1.png`.
- `persona`: `buzhou` (a placeholder until the handle is chosen).
- `tool` and `model`: copy exactly what the screen shows at the time, never from memory. If the screen shows no model name, write `not shown in UI` plus any mode or version you can see. Never guess.
- `prompt`: the **full text you pasted** (character lock plus block, or the whole R01 prompt), in double quotes, with every double quote inside it doubled. Start the cell with the attachments, for example `[REF: assets/buzhou/photoreal/R01_pr_master_v1.png]` or `[REF: none]`.
- `licence_notes`: the template below. Start it with `PHOTOREAL v2;` so the stylised rows and photoreal rows can be told apart.

**The easy way to fill it:** do not type CSV by hand. Paste into a spreadsheet app with these seven columns and save as CSV (UTF-8), or fill the batch card below after each batch and ask Claude: "Append these rows to assets/provenance.csv." Claude cannot see your screen, so it needs the model label and the time from you. Rows for the four runs of one prompt share the same prompt text.

```
BATCH CARD (fill in once per batch of images)
date and time, with offset: ____
tool, exactly as shown: ____          model, exactly as shown: ____
plan (from account settings): ____
reference image(s) attached: ____ (file name, or none)
prompt: (paste the full text)
files and what happened to each:
  assets/buzhou/photoreal/candidates/____ : kept / shortlisted / discarded because ____
  assets/buzhou/photoreal/candidates/____ : ____
edits made afterwards (app, what, new file): ____
visible or hidden mark or metadata from the tool, seen or not: ____
```

**Ready-to-fill CSV block** (header plus one example row; the braces show what to replace). The example is an illustration only: no such file exists yet.

```
timestamp,asset_path,persona,tool,model,prompt,licence_notes
2026-10-11T14:05:00+08:00,assets/buzhou/photoreal/candidates/R01_pr_cand_gem1.png,buzhou,"{tool name as shown}","{model name as shown, or: not shown in UI}","[REF: none] {full prompt text, every double quote doubled}","PHOTOREAL v2; STATUS: terms NOT YET CHECKED, do not publish or sell; plan {plan}; mark or metadata from tool: {seen / not seen, left untouched}; human edits: none; look-alike check: not yet run; age-guess: not yet run"
```

### 7.1 Licence reminder: terms have NOT been checked

Before any commercial use, open the **current** terms of use and any content or image policy for the tool and the exact plan you used (they can differ by plan and by country). Do not rely on the tool's description of itself. Answer from the text, not from memory:

1. Who owns, or what rights do you get in, the images you generate?
2. Is commercial use allowed on **this plan** (personal and business plans may differ)?
3. Does it limit how you can use outputs (for example advertising, representing a business, using a person-like character as a brand asset)?
4. Does it say anything about **realistic images of people**: restrictions, required labelling, or limits on a recurring fictional person?
5. Does it say similar outputs may be given to other users?
6. What does it say about visible marks, invisible watermarks or metadata, and about removing them?
7. Rules about reference images you upload (we upload only our own generated images): is an uploaded image stored, reviewed or used to train anything?
8. When were the terms last changed? If unclear, ask the lawyer before commercial use.

Save a dated screenshot or PDF of each terms page. Whether a purely AI-generated image is protected by copyright in Taiwan is an unverified recall (`research/legal.md` 8.2); that is why the log, the prompts, your selection and your edits are the human-authorship record. Keep it complete.

Filled-in `licence_notes` template:

```
PHOTOREAL v2; plan: ____; terms page: ____ (address); version or "last updated" date shown: ____; read by ____ on ____; commercial use of outputs on this plan: ALLOWED / NOT ALLOWED / UNCLEAR; realistic-people rules: ____; key sentence copied: "____"; restrictions noted: ____; mark or metadata from the tool: seen / not seen, left untouched; metadata kept after my edit: yes / no / not applicable; human edits: none / ____; look-alike check: LA-PR-____ (pending / pass / fail); age-guess: pending / pass / fail; STATUS: CLEARED FOR COMMERCIAL USE / NOT CLEARED
```

When you have read the terms once for a tool and plan, copy the same notes onto every row made with them, and redo it when the terms change.

---

## 8. Labelling reminder (nothing is posted without this)

Photoreal makes disclosure **more** important (addendum 7.1). The studio's four places are the bio, the first caption line, the on-screen badge and the platform's AI label. All four, on every post.

1. **Download the original; edit a copy.** Use the tool's download button, not a screenshot. Do not convert or strip anything on the original.
2. **Keep any provenance data the tool added. Do not strip metadata.** Some tools may add provenance data (for example content credentials) or an invisible watermark (hypothesis; unverified). Do not remove or try to defeat any of it. After editing, check whether your editing app kept the metadata (open the file's properties or info before and after). If an export dropped it, do not forge anything; make sure the visible badge and the platform label are on, and write "metadata not preserved after edit" in `licence_notes`.
3. **Leave any visible tool mark** until you have read what the terms say about it.
4. **Add the on-screen badge in editing.** 「AI 生成｜虛擬角色」 on **every** image that shows him (「AI 生成｜示意圖」 on a plate without him), typeset as real text in a Taiwan-glyph font such as Noto Sans TC with the language set to zh-TW. Never ask a generator to draw it. Bone `#EEECE7` fill, charcoal `#2B3038` letters, thin charcoal outline, in the same corner of every post (a corner clear of the platform buttons). Text height at least about 3.5% of the image height and inset at least 8% from every edge, so a square crop of a 4:5 picture cannot remove it (assumption; same rule as the other two pilots since the cross-pilot check of 2026-10-11, replacing "about 12 percent of the image width"). Never crop it out. On avatars a small 「AI」 tag. For video, the badge stays on for every frame in which he appears. The **wife checks every character** by eye.
5. **First caption line (proposed, AI draft for the wife):** 「【AI 虛擬角色】本篇由 AI 生成的虛擬角色「步驟」發布。圖像為 AI 生成，並非真人。」 (Gloss: AI virtual character; this post is by the AI-generated virtual character 步驟; the image is AI-generated and is not a real person.) It replaces 「圖為示意」 on photoreal posts. The bio keeps 「AI 虛擬角色」 and the studio name 明說角色工作室 (bible 8.1).
6. **Platform label always ON** for photoreal images and video of him: Instagram and Threads (the disclosure tool; the "AI-generated profile" label if it exists for Taiwan accounts, tested on a Taiwan test account first), YouTube (the altered or synthetic content question: yes). The old rule that a stylised character may be exempt no longer applies. Platform behaviour in Taiwan is unverified: look at the live app.
7. **No location tags, no "candid" captions, no "today" or "just now" wording, no claim that he was anywhere or used anything.**
8. **Keep evidence.** Save a screenshot of each published post showing the badge, the first line and the platform label.
9. **Five or more "是真人嗎" comments in a week** (or three in the first two weeks): strengthen the badge and first line within 48 hours (addendum 7.2). Reply with the bible's line R1 every time.

---

## 9. A short note for the wife

(Written in simple English. The Chinese terms are AI drafts: please correct any that sound wrong or too stiff, and tell us which are natural.)

You do not need to read the prompts or know the tools. Please look at the images the way a Taiwanese viewer would on a phone, and tell us for each image: **APPROVE (核准) / SMALL FIX (小修) / REJECT (退回)**, with a short reason. Use the project's reason codes where they fit (S text or fonts, X cultural or visual error, P politics or sensitive, D disclosure missing) plus three new ones for this pack: **A** age read, **L** look-alike, **U** uncanny.

1. **How old does he look? 看起來幾歲？** Write one number and one word (a job) before we tell you anything. Does he look like a student (像學生)? Too young or baby-faced (太年輕、童顏)? We need clearly adult, about 28 or older (成年人感).
2. **Does he remind you of anyone? 撞臉？** A person on TV, in film or music, an athlete, someone in the news, a politician (政治人物), an online creator (網紅), someone you know? Write the name in your own words. If you name a person, we change the face. Please do not search for a match for us; just tell us your first thought.
3. **Is the face natural and ordinary? 自然、像一般人？** Or does it look like a template: idol face (偶像臉), Korean-style (韓系), Japanese-style (日系), over-edited (修圖過度), plastic (塑膠感)? Could you meet a man like this in Taiwan?
4. **Wording decision.** For the prompts we used the neutral words "ordinary East Asian adult features". Do you want to keep that, add "plausibly local to Taiwan", or drop the region? (This is the same open item as for the other characters.)
5. **Does anything look fake or creepy? 恐怖谷：** the eyes (眼神), the smile (笑容), the skin (皮膚), the teeth (牙齒), the ears (耳朵)? Say where.
6. **Colours: 配色.** The set is grey on grey: grey jacket, slate shirt, charcoal trousers, grey backdrop. Does it look like a political party colour (政黨色), a campaign poster (競選感), mourning clothes (喪服感) or just gloomy (太悶)? Is the studio grey backdrop OK?
7. **The patch: 標誌感？** Does the small staircase patch look like a logo of some app or company? Can you see it at phone size?
8. **Headphones.** Natural? Do they look like a real brand (品牌感)? We want plain and logo-free.
9. **Clothes and haircut.** Practical, adult, modest, not a school uniform (制服) or a costume? The short-sleeve shirt (Outfit C) fine for hot weather? Is the haircut ordinary (not a trend cut)?
10. **Any text, hands or fingers? 圖上有沒有字、手指？** There should be none. If you see any character at all, tell us if it is garbled (亂碼), Simplified (簡體字), or a Japanese or Hong Kong form.
11. **Gender and pronouns: 性別感.** The bible was neutral (中性) on purpose. He is now man-presenting. Does that feel natural? Keep writing the character by name or as 這個角色, or is 他 fine? (Addendum section 10 item 1.)
12. **Is it clearly AI? 看得出是 AI 嗎？** When the badge 「AI 生成｜虛擬角色」 and the first line are added (the operator will show you), is it obvious to an ordinary viewer that this is not a real person? Is the wording natural, or too heavy and ad-like (工商味)? Is the first line 「圖像為 AI 生成，並非真人」 good?
13. **The 示意 set pictures, only if we get to them:** sockets (插座, Type A/B), window grille (鐵窗), split air conditioner (分離式冷氣), shoes off (脫鞋), no signs or brands. Does it feel like Taiwan or like Japan or Korea?
14. **The joke 「耳機沒接線」 (the headphones plug into nothing).** Now that they look like real headphones, does it still work?

If you are not sure, say "not sure" and why. Your gut reaction is useful information. The extra checks add some of your time (about 15 minutes per master check, 10 per re-run; our assumption): please tell us if that is too much.

---

## 10. Common failure modes for this character, and fixes

Source: the addendum's rules plus failures I would expect from photoreal generators (hypotheses). Each fix is a line to add to the prompt or send as a follow-up. If a fix is a "don't", also add it to the Avoid list in 2.4 and ask Claude to log the new item in the addendum. Positive phrasing ("the frame ends at the belt line") often works better than a negative ("no hands"); where both are given, try the positive first (hypothesis).

### 10.1 Table

| What you will see | Why it happens | Fix |
|---|---|---|
| **Hands or fingers appear**, or thumbs hooked out of pockets | Generators like hands; a half-body frame leaves room for them | Section 10.2. Positive line: `The frame ends at the belt line; both arms hang at his sides and the hands are below the bottom edge.` |
| **Skin plastic, airbrushed, glowing** | Generators default to beauty retouching | `Natural unretouched skin with visible pores and fine texture on the nose and cheeks, matte, no glow, no smoothing.` Do not smooth or sharpen afterwards |
| **Uncanny eyes**: dead stare, mismatched catchlights, uneven pupils, wandering gaze | Eyes are where photoreal fails first | `Both eyes look at the camera, the same size and brightness, natural catchlights in the same place in both eyes, natural eyelids.` If an off-camera expression keeps failing, drop it for now |
| **Teeth wrong** (too many, fused, too white) | Open mouths are hard | `Lips closed.` Keep E02 the only expression with parted lips and check it closely |
| **Looks too young, student-like, baby-faced** | "East Asian" plus "man" often pulls toward a smooth young face | Age-cue line: `A mature adult face about 30 years old: defined cheekbones and jaw, fine lines at the outer corners of the eyes, a faint line from nose to mouth corner when relaxed, adult neck and shoulders, no baby softness.` If the wife says young: reject, do not retouch |
| **Glamour or template face** (idol, "soft boy", over-symmetric, very pale, V-line jaw) | Training-data defaults | `Ordinary everyday face, natural asymmetry, a plain everyday look, not glamorous, not styled.` Add `no doll-like symmetry` |
| **Face drifts between images** | No seed control in chat tools (assumption); long chats drift | Always attach the master; restate the lock; restart from the master in a fresh chat; reject drifted images |
| **Headphones wrong**: earbuds, gaming headset with microphone, visible cable, glowing ring, brand mark, different shape | "Headphones" has many forms | `Matte charcoal closed-back over-ear headphones with a thin padded band and plain round-oval cups on the ears, no cable, no logo, no microphone, no lights, no shine, the same design as in the attached image.` |
| **Ears odd** (fused with the cups, mismatched, melting into hair) | Cups cover the ears; the model fills in | `The headphone cups sit cleanly over the ears; the band follows the head; hair falls naturally around the cups.` Local edit if one side only |
| **Patch wrong**: staircase falls to the right, 2 by 2 block, QR or barcode look, 5 or 7 squares, wrong colours, logo-like | Small objects and counts are hard | `Redraw only the chest patch: a small sewn woven patch, off-white with a thin charcoal border, six flat squares in three bottom-aligned columns of one, two and three squares rising to the viewer's right, colours pale grey, grey-blue and dark slate. Not a two-by-two grid. Change nothing else.` Then local edit, then the three-bar fallback with the wife's approval |
| **Digits or letters appear** on the patch, shirt or sneakers | The prompt mentions numbers | `The patch contains only coloured squares. No digits, no letters, no writing anywhere.` Regenerate; remove one small mark with a local edit |
| **Patch on the wrong side, or mirrored** | "Left" has two meanings; a flipped image moves it | Use the master's side as the rule. Follow-up: `Put the patch on the same side of the chest as in the attached image.` Never flip an image |
| **Jewellery, glasses, beard, tattoo appear** | Generators add accessories | `No jewellery of any kind, no glasses, clean-shaven, no tattoos, no watch.` |
| **Outfit drift**: hoodie, bomber, puffer, suit, stripes or ticks on sneakers, tight fit, open collar | Generators fill gaps with common clothes and brand styling | Restate the exact pieces in an `OUTFIT:` line (section 4.2). `Plain off-white sneakers, no stripes, no marks.` `Loose boxy fit, collar closed.` |
| **Logo or text on zips, tags, sneakers, headphone cups** | Generators imitate brands | `No logos, no brand marks, no text on any item.` Local edit to remove |
| **Lighting drift**: rim light, warm backlight, golden hour, neon, hard shadows | Dramatic lighting is a default | Restate: `One large soft key light from the front left, gentle fill, neutral daylight, soft shadows, no rim light, no coloured light.` |
| **Backdrop drift**: room, bokeh lights, window, props, textured wall | Generators add context | `Plain seamless mid-light neutral cool-grey studio backdrop, nothing else in the scene.` |
| **Candid or phone-snapshot look**, wide-angle selfie distortion, mirror shot | "Photoreal" pulls toward social-media photos | `A composed studio portrait with an 85 mm lens look at eye level; not a snapshot, not a selfie.` Reject any that look like a slice of someone's day |
| **Extra person, phone, cup, laptop, food appears** | Scene filler | Regenerate; add the object to Avoid. Ground rule 4: nothing in use |
| **Over-sharp, HDR crispness; colour cast** (orange or teal) | Default grading | `Muted natural colour, neutral white balance, no HDR, no filter.` Regrade a copy if the cast is mild; log it |
| **Sexualised or too open**: unbuttoned collar, wet look, tight cloth, bare skin | Photoreal portraits drift to glamour | `Loose, modest, collar closed, matte fabric.` **Reject** the image |
| **Looks like someone** (the wife or a panel member names a person, or a search shows a close match) | Generators reproduce faces from training data | **Do not retouch.** Reject. Redesign a feature through a revision of the addendum with the wife, then repeat 6.2 |
| **Drift after several edits** (the "telephone game") | Each edit starts from the previous output | Start a fresh chat from `R01_pr_master_v1.png` |
| **The tool refuses or answers in words** | Safety rules or ambiguity | Reply "Please generate the image now." If it refuses, log it; do not reword to get round it |

### 10.2 The hand fix procedure

Rule one: **a hand that is not in the frame cannot be wrong.** Every block is built to keep hands out of frame or inside pockets. If one appears anyway:

1. **Count and zoom.** At 200 percent, look at the lower edge, sleeve ends and pocket openings. Extra, missing or melted fingers, a thumb hooked out of a pocket, or a hand-shaped fold in cloth all count as a fail.
2. **Rung 1: regenerate** in a fresh chat with the master attached and the positive framing line: `The frame ends at the belt line; both arms hang at his sides and the hands are below the bottom edge of the image.` (for waist-up and full-body: `Both hands are fully inside the pockets, only the sleeve ends and the pocket openings are visible`). Four runs.
3. **Rung 2: targeted edit.** In the tool's edit or select-region mode if it has one (hypothesis), select only the hand area and send: `Change only this area: the hand is hidden inside the pocket, no fingers or thumbs visible. Keep everything else identical.` Two rounds at most. Save as a new file, log it.
4. **Rung 3: reframe or crop.** For a half-body or headshot, crop higher on a copy so the hands fall outside the frame. This is an allowed human edit: keep the aspect ratio you need, keep the patch and the badge-safe corner in frame, and log the crop with its parent file. Re-run the adult read at the new crop.
5. **Rung 4: reject the image** and switch to a framing that does not need hands (headshot, half-body). Three failed rounds means stop: ask Claude for a revised prompt.
6. **Never** repair a hand by pasting in a photo of a real person's hand, by compositing any real photo, or by drawing fingers. Never keep an image with a visible hand error because "it is only small": hands are the failure audiences notice first (the IKEA Taiwan case, `research/competitors.md` S8).

---

## 11. When you stop for the day, and what to send back

**Stop cleanly.**

1. Every image you looked at is downloaded and in `candidates/` or `assets/buzhou/photoreal/`. Delete nothing.
2. Every file has a row in `assets/provenance.csv`, or your batch cards are filled in for Claude to write.
3. `R01_pr_master_v1.png` is a copy of the winner and is never edited. Write down which side the patch is on.
4. Note the chat links and the minutes you spent.
5. If you only have 90 minutes, stop after STEP 1 and the choose step. That is a good stopping point.

**After each sitting, paste this into Claude Code in this folder**, filled in as far as you can (partial is fine):

```
PERSONA: buzhou (photoreal)        DATE:
TOOL(S) AND MODEL LABEL(S), exactly as shown: Gemini ___ / ChatGPT ___
PLAN NAME shown in my account: ___
MINUTES: set-up __  generating __  choosing __  logging __  wife __
CHOSEN MASTER (path): assets/buzhou/photoreal/R01_pr_master_v1.png   from candidate: assets/buzhou/photoreal/candidates/___
WHICH PROMPT WORKED: Gemini or ChatGPT version; rounds of 4 needed; any wording I changed or fix phrase I added (paste it)
SIDE THE PATCH IS ON in the master (viewer's left or right):
KEPT AND DISCARDED: file paths with one word of reason (or: all in candidates/, rows logged)
FOLLOW-UP IMAGES DONE (path each): R02 ... R07
CHECKLIST rows that failed most often:
HANDS: did any appear? how many rounds to fix?
TOOL BEHAVIOUR: refused anything? text or numbers appeared? visible mark or watermark or metadata seen? did the face drift between chats?
WIFE: APPROVE / SMALL FIX / REJECT per image, with reason code (S, X, P, D, A, L, U); her answers to the questions in section 9 (especially 2, 4, 11, 12)
TESTS: age guesses (initials, number, job word); "reminds me of" answers word for word; reverse-image searches (tool, date, any close match); uncanny scores; real-person read count; legibility result; or "not yet run"
PROVENANCE: rows written (yes/no), or my notes attached for Claude to write them
LICENCE: terms read? date, page, plan, the key sentence; or "not yet"
```

What Claude does with it: writes or checks the provenance rows, updates the addendum's status, records the tool test in `pipeline/tools.md` (the BRIEF's Phase 4 comparison), and, once the wife has ruled on addendum section 10, revises the prompts and the lock (2.2, 2.3, 3.2) where a ruling changes the wording.

**Where things are**

- Spec: `personas/buzhou/photoreal-addendum.md`. Voice, pillars, disclosure lines: `personas/buzhou/bible.md`.
- Stylised pack (record only): `pipeline/image-pack/buzhou.md`. Shared rules and the three-pilot colour table: `pipeline/image-pack/README.md`.
- Output folder: `assets/buzhou/photoreal/` (`candidates/` and `lookalike/` inside it).
- The log: `assets/provenance.csv`. Look-alike log: `personas/buzhou/lookalike_log.md` (create it from 6.2).
- Your jobs, in order: `HUMAN_TODO.md` (items 10, 18 and 26 matter here).
