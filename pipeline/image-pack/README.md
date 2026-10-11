# Image packs: start here

Written 2026-10-11 for the operator (English only). Your wife reviews language and culture. Nothing has been generated yet: no reference image exists, and no pilot character is cleared for public use. Everything the packs say about what Gemini and ChatGPT can do is a **hypothesis**, so check the current screen and copy model names exactly as the app shows them. All zh-TW wording is an AI draft for the wife to correct.

## Start here (six moves)

1. Read sections 2 and 4 of this page (which pack first, and the rules).
2. Open `pipeline/image-pack/fangcun.md`. Read its sections 0 and 1.
3. Set up folders and open the log (section 5 of this page, about 5 minutes).
4. Run the R01 prompt in Gemini to get four images, and again in ChatGPT to get four. Save and log as you go.
5. Reject pass, checklist, shortlist of three at most. Then your wife looks (without knowing which tool made which) and you run the reverse-image search.
6. Send Claude the report in section 7.

## 1. What the packs are

Each pack is a step-by-step recipe for the first reference images of one pilot character: copy-and-paste prompts for Gemini and ChatGPT, a pass/fail checklist, the two human tests (age guess, look-alike), a note for your wife, a log template, and fixes for the failures to expect. They are built from the character bibles (`personas/<slug>/bible.md`, sections 4 and 5), and if a pack and its bible disagree, the bible wins.

| Pack | Character (stated age) | Niche and platforms | Look | Main trap |
|---|---|---|---|---|
| [fangcun.md](fangcun.md) | 方寸 (32) | Small-space and renting arithmetic; Instagram, then YouTube Shorts | Matte hand-sculpted clay look, stacked blocks, cube head, dot eyes, no hands | Reads as a toy or a child; fingers or numerals sneaking in |
| [buzhou.md](buzhou.md) | 步驟 (28) | AI tools in three steps; YouTube Shorts, then Threads | Flat vector, no outlines, blue-greys; headphones; a small picture beside real screen recordings | The chest patch (six squares in columns of 1, 2, 3, rising left to right) |
| [sehuan.md](sehuan.md) | 色環 (30) | Outfit logic and colour; Instagram, then Threads | Fashion illustration: flat colour fields, loose ink-brush line; woman-presenting | The 12-segment colour-wheel earring, exactly six chip cards, one small persimmon accent, outfit B looking like a school uniform |

The three packs share one layout, so once you know one you know all: section 0 summary, 1 before you start, 2 R01 prompts, 3 lock it (follow-up images), 4 expressions and poses, 5 checklist, 6 the human tests, 7 the log, 8 a note for your wife, 9 common failures and fixes (方寸 and 色環 add 10, when you stop for the day). You do not read them end to end: sections 0 and 1, then 2 and 3 in order, with 5 and 7 open beside you.

## 2. Which one first: 方寸 (fangcun)

Recommended order: **1. 方寸, 2. 步驟, 3. 色環.** This is my judgement from reading the packs, not a test result.

Why 方寸 is the easiest to judge:

* **Fewest things to get wrong.** Counting the rows in each pack's checklist: 方寸 has 19, 步驟 has 25 (9 main checks plus 16 locked features), 色環 has 33 (13 plus 20). (*computed* by counting.)
* **Crisp yes/no checks you can do without Chinese or art training.** The figure has no hands, so any finger is an instant fail. No nose, ears or lips. No numerals on the tape-measure belt. Matte, not glossy. Head about one seventh of the height and never more than one sixth.
* **No human face.** The hardest question for a non-expert ("does this face look like a real person or a known influencer?") hardly arises. The look-alike risk is toy and game block figures, which a picture search shows quickly (hypothesis).
* **Little that depends on left or right.** No chest patch, no tucked-back ear, no skin tone to keep consistent.

Easiest to judge is not the same as most likely to pass. The pack's own top risk is that a cube head with dot eyes and no hands reads as a toy or a child, and only the age-guess and look-alike tests (pack section 6) settle that. Finding out on the first pilot is useful, because a design change goes through the bible. If R01 fails the same way after two rounds of four in both tools, stop, tell Claude, and move on to 步驟 rather than burn the day.

Why 步驟 second: the shortest first session in the packs (R01, the quick tests, the face sheet and corner busts), and flat colour shapes whose one fiddly detail is the chest patch. Why 色環 last: the most details to check, a human face with a look-alike list of named virtual influencers, and three wording questions for your wife (the blush background name 淡蜜桃色, the accent name 柿子橘, and whether the prompt keeps "that read as Taiwanese"). By then you will also know how each tool behaves.

Gemini first, then ChatGPT with the same prompt, is the packs' starting point. That is a tie-breaker (Gemini's recipe is the plainer one), not evidence. Run both on every R01: eight candidates is cheap and doubles as the Phase 4 tool test. After you pick a winner, stay in that tool for that character's follow-up images, in a fresh chat each time, with R01 attached.

## 3. How long

The figures below are the packs' own estimates (*assumption*, nothing measured). Your real minutes are data: write them down.

| Pack | Today's scope | Hands-on | Your wife | Another day |
|---|---|---|---|---|
| 方寸 | R01, then R02 to R07 (views, head turnaround, expressions) | 3 to 4 h, in two sittings | about 15 min | about 1 h for the tests |
| 步驟 | R01, quick tests, R02, R07 | 2.5 to 3 h | 30 to 40 min | next sitting about 1.5 h (R03, R04) |
| 色環 | R01, R02, R03 | about 3 h, in two sittings | 15 to 20 min | about 1 h for the tests |

Scopes differ (步驟 includes its quick tests today, the others do not), so do not compare rows. Adding them up: about 8.5 to 10 hours for you and 60 to 75 minutes for your wife across all three (*computed*). Your stated budget is 6 hours a week (`DECISIONS.md`), so plan **one pilot per week**, not three in a weekend.

**First session, 方寸:**

* Sitting 1, about 1.5 h (my estimate, extrapolated from 步驟's table: set-up 10, generating 30, choosing 20, logging 20 to 30 minutes): set-up, R01 in both tools (8 images), save and log everything, reject pass, checklist, shortlist.
* Between sittings: your wife looks at the shortlist (pack section 8), and you run the reverse-image search (pack section 6.3).
* Sitting 2, about 2 to 2.5 h: choose a provisional master, then R02 to R07 with R01 attached, logging as you go.
* If you only have 90 minutes, stop after Sitting 1. That is a good stopping point.

## 4. Rules for every prompt, in both tools

1. **Uploads.** The only pictures you may ever upload are your own images made with these packs (for example `R01_master_v1`) and plain colour swatches. Never a photo of a real person (yourself, your wife, a friend, a celebrity, a model), never a photo of a real room, and never a picture, screenshot or fan art of any existing character, mascot or virtual influencer, not even "just for the pose". Describe poses in words, as the prompts do.
2. **Prompts.** Paste the pack's code box unchanged. Never type "in the style of" followed by a living artist, a studio, a brand or an existing character. No real brands, logos or number plates. The look-alike steps name well-known characters for you to **search for by eye**; those names never go into a prompt.
3. **No text in the picture.** Generators garble Chinese characters or output Simplified forms, so every pack treats any text in a generated image (letters, numerals, Chinese) as a fail, even if it looks right. If Chinese does appear, ask your wife whether it is garbled or Simplified and note it in the log: that tells us how the tool behaves. Chinese text and badges are added later in a design tool, and your wife reads every character.
4. **Adults only.** Each pack's checklist has an adult-read check at thumbnail size. If a result looks young, cute or child-like, reject it. Do not retouch around it.
5. **Licence terms are not checked.** The packs do not know what Gemini or ChatGPT allow for commercial use on your plan. Before any commercial use, read the **current** terms for the exact tool and plan you used and record the result in `licence_notes` on every row. Questions to answer from the text, not from memory: who owns the images or what rights you get; whether commercial use is allowed on **your plan**; limits on using outputs as a recurring character or brand asset; what it says about visible marks, invisible watermarks and removing them; rules about uploaded reference images; when the terms last changed. Save a dated screenshot or PDF of the page. If anything is unclear, write NOT CONFIRMED. Until it is recorded, every image is **internal design material only**.

## 5. How to save and log (the one-page version)

**Folders** (`fangcun`, `buzhou`, `sehuan` are working names, not cleared handles). Make the sub-folders yourself, or ask Claude in this project folder to do it:

```
assets/
  provenance.csv            (already exists; header only; never change the header)
  fangcun/                  kept files, for example R01_master_v1.png
    candidates/             every image you considered but did not choose
    lookalike/              screenshots of reverse-image searches
  buzhou/                   same pattern; the 步驟 pack keeps its look-alike log in personas/buzhou/lookalike_log.md (a file you create from its template)
  sehuan/                   same pattern
```

**File names.** Use the exact names in the order-of-work table in each pack's section 3. Pattern: image ID, short name, version. Candidates go in `candidates/` as `<ID>_cand_<tool>_<n>` (方寸 and 色環: `R01_cand_gemini_1.png`, `R01_cand_chatgpt_1.png`; 步驟: `R01_master_cand_gem1.png`, `R01_master_cand_gpt1.png`). The kept copy of the chosen candidate is `R01_master_v1.png` (copy it, never rename the original). A redo is `v2`; never overwrite. Keep the file type the app gives you (`.png`, `.jpg`, `.webp`) and do not convert, crop or strip anything.

**Saving.**

* Use the app's download button for the largest version. A screenshot is the last resort and must be noted in the log.
* Do not use a temporary or private chat mode: you need the conversation link for the log.
* Download every image you look at for more than a glance. **Delete nothing today.**
* If the tool adds a visible mark, leave it and note it. Do not remove any mark until you have read what the terms say.

**Logging.** One row in `assets/provenance.csv` per file, the same day, columns `timestamp,asset_path,persona,tool,model,prompt,licence_notes`.

| Column | What goes in |
|---|---|
| timestamp | Date and time you generated it, in Taiwan time with offset, `+08:00` (if you are in another time zone, write your real offset and keep it consistent) |
| asset_path | Path from the project folder, for example `assets/fangcun/candidates/R01_cand_gemini_1.png` |
| persona | `fangcun`, `buzhou` or `sehuan` |
| tool | What you actually used, for example "Gemini (app)". For an edit, the editor's name; for a hand-made file, "human-made in <app>" |
| model | The model or version label **exactly as the app shows it that day**. If none is shown: "not shown in app, YYYY-MM-DD". Never guess. For an edit: n/a |
| prompt | The **full text you sent**, with a note of which files were attached. If you changed one word, log the changed text. For an edit, one sentence saying what you did |
| licence_notes | The template in section 7 of your pack: status (kept, provisional master, or discarded-but-considered), reason, parent file, references attached, human edits, plan name shown in your account, terms read on (date and page) or "not yet read", and **commercial use per those terms: NOT CONFIRMED** until you have read them |

Example shape only. Do not paste this; replace every `<...>`:

```
timestamp,asset_path,persona,tool,model,prompt,licence_notes
<YYYY-MM-DDTHH:MM:SS+08:00>,<assets/fangcun/candidates/R01_cand_gemini_1.png>,fangcun,"Gemini (app)","<model label exactly as shown>","<full prompt exactly as sent. Attached files: none.>","Status: DISCARDED-CONSIDERED; reason: <one word>; parent file: none (raw download); human edits: none (raw); tool plan: <plan name in my account>; terms read: not yet read; commercial use per those terms: NOT CONFIRMED; watermark or label on file: <none seen | describe>; conversation link: <link>"
```

Rules that keep the file valid:

* **Every image the tool hands you gets a row**, including ones you reject on sight (one word of reason). Four images from one prompt are four rows with the prompt cell copied down. The 方寸 and 色環 packs say rows are optional for images you never saved; this page takes the stricter 步驟 rule, in line with BRIEF Ground rule 2. When in doubt, log it.
* Crops, resizes, colour fixes, flips and hand-finished versions are separate files with their own rows that name the parent.
* Never edit or delete an old row; corrections go in a new row. Add yours at the bottom (other characters' rows share the file).
* Prompts contain commas, line breaks and quotes, so do not type CSV by hand. Paste each field into its own cell in a spreadsheet app and save as CSV (UTF-8). Or keep notes (file names, tool, model label, time, which prompt ID, any changed wording) and ask Claude: "Append these rows to assets/provenance.csv." Claude cannot see your screen, so it needs the model label and the time from you. If you pasted the pack's prompt unchanged, say so and Claude will use the pack's exact text. The 步驟 pack has a batch card for this (its section 7).
* Expect 20 to 30 minutes of logging per sitting (the 步驟 pack's estimate, *assumption*).

## 6. Disclosure: stylised is not a loophole

These characters are drawings, and they are always openly AI. Every post that uses these images is disclosed as AI. The bible for each character (section 8, the exact disclosure lines, all AI drafts for your wife) puts it in four places: the bio (which names 明說角色工作室 and says 「AI 虛擬角色」), the first line of the caption, an on-image badge on every image (方寸's is 「AI 生成｜示意圖」), and the platform's own AI label wherever the platform offers one (whether Instagram offers one on a Taiwan account is still to be checked, `HUMAN_TODO.md` item 10). The badge is typeset by a person later, never drawn by the generator.

The pictures are illustrations, not evidence. These characters have never lived in a home, used an app or worn a garment, so no image should look like a photo, a real place or a customer's result (BRIEF Ground rule 4). Nothing made with these packs goes on any account yet: the reading test, lawyer answers and STOP 3 come first.

## 7. What to send back to Claude

After each sitting, paste this into Claude Code in this folder, filled in as far as you can. Partial is fine. Claude can also look at the saved files and give a first-pass checklist, but it can miss details and cannot make your wife's judgements on age, colour read or Taiwan details.

```
PERSONA:                 DATE:
TOOL(S) AND MODEL LABEL(S), exactly as shown: Gemini ___ / ChatGPT ___
PLAN NAME shown in my account: ___
MINUTES: set-up __  generating __  choosing __  logging __  wife __
CHOSEN MASTER (path): assets/<slug>/R01_master_v1.png   from candidate: assets/<slug>/candidates/___
WHICH PROMPT WORKED: Gemini or ChatGPT version; rounds of 4 needed; any wording I changed or fix phrase I added (paste it)
KEPT AND DISCARDED: file paths with one word of reason (or: all in candidates/, rows logged)
FOLLOW-UP IMAGES DONE (path each): R02 ... R07
CHECKLIST rows that failed most often:
TOOL BEHAVIOUR: refused anything? text or numerals appeared? visible mark or watermark? a seed shown? did the face drift between chats?
WIFE: APPROVE / SMALL FIX / REJECT per image, with reason code (X, S, P, H, T); her answers to this character's open questions
TESTS: age guesses (initials, number, job word); "reminds me of" answers word for word; reverse-image searches (tool, date, any close match), or "not yet run"
PROVENANCE: rows written (yes/no), or my notes attached for Claude to write them
LICENCE: terms read? date, page, plan, the key sentence; or "not yet"
```

Open questions to include, per character:

* **方寸:** does the cube head read as an adult or a toy? Anything it reminds anyone of? (pack sections 6 and 8)
* **步驟:** which side of the body the patch is on in the chosen master (then it is the rule for every image; never flip an image); does a gender-neutral character feel natural?
* **色環:** which side the tucked-back ear and earring show on in R01; your wife's answers on "that read as Taiwanese" and on the blush background (淡蜜桃色) and accent (柿子橘) names.

What Claude does with it: writes or checks the provenance rows, updates each bible's status, records the tool test in `pipeline/tools.md` (the BRIEF's Phase 4 comparison covers character consistency, API access, price and licence terms; your sessions supply the consistency and licence evidence), and renames the frozen set into the bible's golden-set scheme.

**STOP 3** (BRIEF, Phase 4) needs five finished sample posts for **one** pilot, not all three. That persona needs: a master that passed both tests, was hand-finished in an image editor with the layered file kept (the packs assume you do this; no time is estimated for it, so log your real minutes), and was approved by you and your wife. Claude will propose which pilot to use, most likely the first to pass. 方寸's bible already suggests a five-post sample set (`personas/fangcun/bible.md`, section 11, item 18). The reading test of the names (`HUMAN_TODO.md` item 18) is not needed to make test images, but masters cannot be approved until it passes (`HUMAN_TODO.md` item 26), so do it when your wife is already looking at the shortlist. The assumed first posts (Mon 2026-11-16, `personas/README.md`) are an *assumption* gated by much more than images.

## 8. Colours: look at the three side by side

The three pilot palettes were checked against each other when the personas were integrated (`personas/README.md` section 5, the near-pair register, computed with `personas/palette_check.py`). The aim: characters that meet on the same feed must be easy to tell apart. But that check used the **planned** hex values. Generators treat hex codes as hints, and no image exists yet, so the real test is your eyes.

Once each pilot has a chosen R01, put the three front views in one row on one screen (the packs use about 110 pixels tall, roughly 3 cm on a laptop screen; zoom the browser out), and again on your phone. 步驟 also needs a 64 px look (its pack, section 3.4). Ask yourself whether you can tell them apart in two seconds with eyes half closed, and ask your wife. If two read as the same character, tell Claude; do not fix it with editing.

| Pair | Where they meet | Planned distance (CIE76, higher is more different) | Note |
|---|---|---|---|
| 方寸 and 色環 backgrounds (`#F5F0E6` and `#F2DAD2`) | Instagram | 9.5, noticeable side by side | Fixed in the integration pass (it was 3.4 when 色環's ground was cream). Re-check at the new ground |
| 方寸 and 步驟 backgrounds (`#F5F0E6` and `#EEECE7`) | YouTube | 3.2, hard to tell apart | Accepted in the register because 步驟 uses bone only as a frame and thumbnail ground. **Both R01 sheets are a plain off-white, so the grounds will look the same; tell them apart by the figure** |
| 步驟 and 色環 backgrounds (`#EEECE7` and `#F2DAD2`) | Threads | 9.6 | Fine |
| 步驟 and 色環 skin (`#D8B190` and `#DDB38E`) | Threads | 2.7 (1.4 on CIEDE2000) | **My own calculation this session; not in the register**, which does not track skin. Close, but the medium differs (outline-free flat vector against brush line) and so does everything else. Look at it side by side and tell Claude what you see |

After the files exist, sample the real colours with a colour picker (each pack's checklist explains how and gives an allowed range, which is the pack author's suggestion, not a bible rule) and tell Claude if they drift; Claude can re-run `personas/palette_check.py` with the measured values.

## 9. If you get stuck

* One bad image in four: press regenerate. The same defect in two or more of four: add the matching fix phrase from the pack's section 9 and make four more.
* Two rounds of four fail the same way in one tool: try the other tool. Both fail: stop and tell Claude.
* The age guess fails, a look-alike is named, or the thumbnail reads as a toy or young: stop and tell Claude. Do not repair these with editing. The design may need a change in the bible.
* A tool refuses or answers only in words: reply "Please generate the image now." If it refuses, do not reword the prompt to get around it. Log it and tell Claude.

## Where things are

* Packs: `pipeline/image-pack/fangcun.md`, `buzhou.md`, `sehuan.md`
* Source of truth: `personas/<slug>/bible.md` (sections 4 and 5; the Review and integration logs override earlier text)
* Colour near-pair register: `personas/README.md` section 5; script: `personas/palette_check.py`
* The log: `assets/provenance.csv`
* Your jobs, in order: `HUMAN_TODO.md` (items 18 and 26 matter here)
