# Photoreal image packs: start here

Written 2026-10-11 for the operator (English only). Your wife reviews language and culture. **Nothing has been generated yet:** no photoreal reference image exists, and no pilot character is cleared for public use. Everything the packs say about what Gemini and ChatGPT can do is a **hypothesis**, so check the current screen and copy model names exactly as the app shows them. Claude cannot make photoreal images; you run the prompts. All zh-TW wording is an AI draft for your wife to correct. The studio name 明說角色工作室 and the three character names are provisional and uncleared.

Evidence labels used here: *assumption* (a planning figure), *unverified* (not checked against a primary source), *computed* (calculated from numbers in the files).

## 1. What happened, and what is superseded

You saw the stylised art and said it looked fake and that you need real people. `DECISIONS.md` (2026-10-11) records the reading: **photorealistic AI-generated characters that are still openly AI.** That is not a switch to human presenters. If you meant hiring real human creators, that is a different business: tell Claude before spending time on these packs.

What this changes:

* Each pilot now has a photoreal **addendum** (the spec) and a photoreal **pack** (copy-and-paste prompts and a checklist):

| Character | Spec | Pack |
|---|---|---|
| 方寸 (fangcun) | `personas/fangcun/photoreal-addendum.md` | `pipeline/image-pack/fangcun-photoreal.md` |
| 步驟 (buzhou) | `personas/buzhou/photoreal-addendum.md` | `pipeline/image-pack/buzhou-photoreal.md` |
| 色環 (sehuan) | `personas/sehuan/photoreal-addendum.md` | `pipeline/image-pack/sehuan-photoreal.md` |

* **Your earlier clay and vector images are superseded.** That means the first 方寸 clay candidate from Gemini (`assets/fangcun/candidates/R01_cand_gemini_1.jpg`, already logged as rejected) and the code-drawn 步驟 art (`assets/buzhou/art/`). Keep the files and their rows in `assets/provenance.csv`; do not delete or edit them. Do **not** upload them to a generator as a reference for a photoreal character. Never mix the two looks on one account: they would read as two different characters. The code-drawn 步驟 art stays on file only as a fallback if photoreal fails (the decision would be yours).
* The old stylised packs (`fangcun.md`, `buzhou.md`, `sehuan.md`) and the old `README.md` are kept as a record. Do not use their prompts.
* Waves 2 to 4 (the other seven characters) stay stylised until the pilots are settled.
* **Stills only.** No voice, video or lip-sync for a photoreal face until a separate addendum and review exist. A synthetic voice on a photoreal face is the closest thing to a deepfake (all three addenda).

## 2. Start here (six moves)

1. Read sections 4 and 5 of this page (which pilot first; the rules).
2. Open `pipeline/image-pack/fangcun-photoreal.md`. Read its sections 0 and 1.
3. Set up the folders and open the log (section 6, about 5 to 10 minutes).
4. Run the R01 prompt in Gemini to get four images, and again in ChatGPT to get four. Save and log as you go.
5. Reject pass, checklist, shortlist of three at most. **Ask yourself one question before anyone else looks: does it still look fake to me?** That was your complaint, and the checklist cannot answer it for you. Then your wife looks at the shortlist (without knowing which tool made which) and you run the reverse-image search (pack section 6: step 6.3 in the 方寸 and 色環 packs, 6.2 in the 步驟 pack).
6. Send Claude the report in section 9.

Nothing blocks making test images today. Your wife's rulings (the "Photoreal switch" section of `HUMAN_TODO.md`) block **approving** a master, not generating one. Run today's prompts with the default wording unless she has already answered.

## 3. The three characters, side by side

They must read as three different people, not one generator face in three outfits (`portfolio.md 3.3`, Ground rule 8). The cross-pilot check of 2026-10-11 compared them on six axes: face shape; hair; face furniture (glasses, earrings, headphones); apparent age; skin undertone; backdrop and light. **Every pair differs clearly on at least four.** Apparent age is not counted: the three visible-age bands overlap (28 to 33, 30 to 35, 30 to 36), generators cannot render a two-year gap, and under-reading is the main risk, so no design is pushed younger or older to separate it.

| | 方寸 (fangcun) | 步驟 (buzhou) | 色環 (sehuan) |
|---|---|---|---|
| Stated age; reads about | 32; 30 to 36 | 28; 28 to 33 | 30; 30 to 35 |
| Presentation | Woman | Man | Woman-presenting |
| Niche; platforms | Small-space and renting arithmetic; Instagram, then YouTube Shorts | AI tools in three steps; YouTube Shorts, then Threads | Outfit logic and colour; Instagram, then Threads |
| Face shape | Softly squared, rounded chin | Long oval, defined jaw, straight chin | Oval, widest at the cheekbones, narrow soft chin |
| Hair | Dark brown-black, low ponytail, side part | Short black, side-parted | Dark brown-black, shoulder-length blunt, worn down, left side tucked behind the ear |
| Signature | Thin walnut glasses; cream belt with tick marks | Matte charcoal over-ear headphones; small sewn patch of six squares | Twelve-segment colour-wheel earrings; one persimmon accent; ring of six blank colour cards (knees-up shots) |
| Palette | Oat, sage, walnut, cream | Cool greys, slate, charcoal | Cream, warm stone, charcoal, persimmon |
| Backdrop (photo) | Warm off-white | Studio grey | Dusty blush |
| Key light | Front left, warm | Front left, daylight | Front right, warm |
| Thumbnail tell (110 px) | Glasses, pulled-back hair, sage vest | Headphones, light-grey jacket | Coloured dot at the left ear, tucked hair, persimmon at the collar |
| Master image R01 | Waist-up front, outfit O1 | Half-body front, outfit A | Waist-up front, outfit A |
| Main traps | Glare on the glasses; numerals on the belt; hands | Wrong patch (counts and side); headphones fusing into ears; hands | Earring wedge count; chip cards; neckerchief reading as a uniform; tuck side flipping; looking like the other two |
| Checklist rows | 31 | 14 main checks plus 15 locked features | 36 (34 reject checks, 2 housekeeping) |
| File names | `R01_master_v1.png` | `R01_pr_master_v1.png` (note the `_pr_`) | `R01_master_v1.png` |

Row counts are *computed* by counting. Backdrop distances (CIE76, *computed* from the planned colours, not from photos): 方寸 and 色環 13.1, 方寸 and 步驟 25.6, 色環 and 步驟 21.0 (higher is more different; above 10 is clearly different). The weakest pair is **方寸 and 色環** (two women, near in age, both dark-haired, both on Instagram): four clear differences and no spare margin.

**The near-pair test (do it once an R01 exists for all three).** Put the three front images in one row at about 110 pixels tall (about 3 cm on a laptop screen; zoom the browser out), unlabelled, on a laptop and on your phone. Ask your wife and at least four others (five viewers or more; the age-guess panel can be reused), two seconds each: "Same person, sisters, or different people?" **Pass:** all say different people. **Fail:** two or more say same person or sisters for any pair. Fix a fail by changing a design attribute of the character that fails (face shape, hair length, frame shape), not by editing, and tell Claude. Two habits keep the faces apart: **one chat per character** (never continue a chat in which you made another pilot) and **never upload one character's image as a reference for another**. A cross-contaminated chat is the commonest cause of "they look like sisters".

## 4. Which one first, and how long it takes

Recommended order: **1. 方寸, 2. 步驟, 3. 色環.** This is my judgement from reading the packs, not a test result. The old reason (the clay figure had no human face) no longer applies: all three are human faces now. The new reasons:

* **Fewest fiddly details to hold.** 方寸 has glasses and a belt. 步驟 adds a six-square patch that must be counted and kept on the same side, plus headphones that can fuse into the ears. 色環 has twelve earring wedges to count, a ring of exactly six cards, a neckerchief that can read as a uniform, and a left/right hair tuck that generators flip. Checklist rows: 31, 29, 36 (*computed* by counting).
* **The first run is also the tool test.** Learn how Gemini and ChatGPT handle skin, eyes, teeth, hands and file marks on the simplest character before the harder ones.
* **色環 is judged against the other two** (her pack's checklist asks whether she looks like 方寸 or 步驟), so she goes last, when both exist.
* 方寸 is also the niche that scored highest in the research (home organisation, 3.85, `research/niches.md`), and you have already made one image of her.

Finding out on the first pilot is useful: a design change goes through the addendum. **Stop rules:** if R01 fails the same way after two rounds of four in both tools, stop, tell Claude, and move to 步驟 rather than burn the day. If the best image still looks fake to you (plastic skin, dead eyes), tell Claude before spending more time: a prompt change is cheaper than polishing.

Gemini first, then ChatGPT with the same prompt, is the packs' starting point. That is a tie-breaker, not evidence. Run both on every R01: eight candidates is cheap and doubles as the Phase 4 tool test. After you pick a winner, stay in that tool for that character's follow-up images, each in a fresh chat with R01 attached.

**How long** (the packs' own estimates, *assumption*, nothing measured; write down your real minutes):

| Pack | Sittings | Your hours | Your wife |
|---|---|---|---|
| 方寸 | 1: 1.5 to 2 h (set-up, R01 in both tools, shortlist). 2: 2 to 2.5 h (R02 to R06). 3: 2 to 3 h (expressions, framings, outfits, seasons, scale reference, belt, glance, avatar). Tests on another day: 1.5 to 2 h | 7 to 9.5 (*computed*) | about 15 min on the shortlist |
| 步驟 | Today about 3.5 h (R01, choose, quick tests, face set, corner busts). Next about 2 h. Later about 3 h | about 8.5 | about 40 min today |
| 色環 | 1: about 2 h. 2: 2 to 2.5 h. 3: 3 to 4 h. Tests: 1.5 to 2 h | 8.5 to 10.5 (*computed*; the pack's own total says 7 to 9) | 15 to 20 min on the shortlist |

All three: about 24 to 28 hours of your time (*computed*) and about 70 to 75 minutes of your wife's at the first stage of each pack (shortlist, blind pick, quick checks). The photoreal checks add her local-public-figure check and the uncanny and legibility tests, about 15 minutes per master check and 10 per re-run (the 步驟 addendum's *assumption*; she is asked whether that fits her 10 hours a week). Your budget is 6 hours a week (`DECISIONS.md`), shared with registration, the lawyer and everything else. Plan **one pilot per fortnight**, not three in a weekend. If you only have 90 minutes, stop after Sitting 1; that is a good stopping point.

**STOP 3** (BRIEF, Phase 4) needs five finished sample posts for **one** pilot, not all three. That pilot needs a master that passed both human tests, was lightly hand-finished (crop, colour and stray marks only, layered file kept, **no skin smoothing**) and was approved by you and your wife. Claude will propose which pilot to use, most likely the first to pass.

## 5. Rules for every prompt, in both tools

1. **Uploads.** The only pictures you may ever upload are that character's **own generated images** (for example `R01_master_v1`) and plain colour swatches. Never a photo of a real person: not yourself, **not your wife**, not a friend, a celebrity or a model, not "just for the face shape, the pose or the lighting". Never a photo of a real room. Never a picture, screenshot or fan art of any existing character, mascot or virtual influencer. Never another pilot's image. Your wife is a reviewer only: she judges the pictures, and no prompt describes anyone you know.
2. **Prompts.** Paste the pack's code box unchanged. Never type a real person's name, a celebrity, influencer, model, actor or existing character, and never "looks like" or "in the style of" followed by any of those. No real brands, logos or number plates. The look-alike checks name nobody in a prompt; they are done by eye on the finished picture.
3. **Wording of the face.** All three packs use the same neutral phrase: *"East Asian, with ordinary, natural, unexaggerated features, not an idol or model look"* (步驟: "ordinary East Asian adult features, everyday and unexaggerated"). Whether to add "that read as Taiwanese" is your wife's decision; two other neutral options are in each pack (section 2 of 方寸 and 色環, addendum 1.7 of 步驟). I recommend the neutral default: a generator cannot reliably produce "Taiwanese" and the phrase invites stereotype. If she chooses another wording it is one swap, in the same place in all three packs, and the changed prompt goes in the log.
4. **No text in the picture, in any script.** Generators garble Chinese or output Simplified forms, and they sometimes print a colour code. The prompts therefore name colours in words (this was fixed in the 方寸 pack on 2026-10-11; the hex codes in the packs are only for your colour check). Any letter, numeral or Chinese character on a generated image is a fail, even if it looks right; if Chinese appears, ask your wife whether it is garbled or Simplified and note it in the log, because that tells us how the tool behaves. Badges and Chinese text are added later in a design tool, and your wife reads every character.
5. **Adults only, modest, nothing sexualised.** Every checklist has an adult-read row at thumbnail size. If a result looks young, cute or child-like, reject it; do not retouch around it. Glamour lighting, parted lips, tight or low-cut clothes, low camera angles and over-the-shoulder looks are rejects.
6. **The pictures must show no lived experience** (Ground rule 4). The characters have never eaten, worn, used or tested anything and have never been anywhere. So: no phone, food, drink, bag, product or held object; no home, cafe, street, MRT or shop; no mirror, selfie or phone-snapshot look; no location tag or map pin; no money, charts, flags or party colours (Ground rule 6); no health, body, weight or skin-care look; no logos or real places. The studio look is deliberately composed and a little formal so nobody mistakes it for a slice of someone's day.
7. **Licence terms are not checked.** The packs do not know what Gemini or ChatGPT allow for commercial use on your plan, or what they say about realistic images of people. **Before any commercial use, read the current terms for the exact tool and plan you used and record the result** in `licence_notes` on every row. Answer from the text, not from memory: who owns the images or what rights you get; whether commercial use is allowed on **your plan**; limits on using outputs as a recurring character or brand asset; what the terms say about **realistic images of people** and any duty to disclose AI generation; what they say about visible marks, invisible watermarks and metadata, and about removing them; rules about uploaded reference images; when the terms last changed. Save a dated screenshot or PDF of each page. If anything is unclear, write NOT CONFIRMED. Until it is recorded, every image is **internal design material only**: no client work, no sponsored post, no public account.
8. **Do not strip or remove any mark** the tool adds, visible or in the file. Download with the app's button, not a screenshot, and note any mark in the log.
9. **If a tool refuses, or answers in words,** reply "Please generate the image now." If it still refuses, do not reword the prompt to get around the refusal: log it and tell Claude.

## 6. How to save and log

**Folders.** Each `photoreal` folder already exists with a `.gitkeep`. Make the two sub-folders yourself (or ask Claude in this project folder):

```
assets/
  provenance.csv                (already exists; never change the header)
  fangcun/photoreal/            kept files, for example R01_master_v1.png
    candidates/                 every image you considered but did not choose
    lookalike/                  screenshots of reverse-image searches (keep private)
  buzhou/photoreal/             same pattern (names carry _pr_, for example R01_pr_master_v1.png)
  sehuan/photoreal/             same pattern
```

Save photoreal files **only** under the `photoreal` folders. The older files in `assets/fangcun/candidates/` and `assets/buzhou/art/` belong to the superseded stylised work; leave them alone.

**File names.** Use the exact names in the order-of-work table in each pack (section 3.4 of 方寸, section 3.3 of 色環 and 步驟). Candidates go in `candidates/`: 方寸 and 色環 `R01_cand_gemini_1.png`, `R01_cand_chatgpt_1.png`; 步驟 `R01_pr_cand_gem1.png`, `R01_pr_cand_gpt1.png`. The kept copy of the chosen candidate is `R01_master_v1.png` (步驟: `R01_pr_master_v1.png`): copy it, never rename the original, never overwrite or edit a master. A redo is `v2`. Keep the file type the app gives you and do not convert, crop or strip the original.

**Saving.** Download the largest version with the app's button (a screenshot is the last resort and must be noted). Do not use a temporary or private chat mode: you need the conversation link for the log. Download every image you look at for more than a glance. **Delete nothing today.**

**Logging.** One row in `assets/provenance.csv` per file, the same day: `timestamp,asset_path,persona,tool,model,prompt,licence_notes`.

* `timestamp`: Taiwan time with offset `+08:00` (if you are elsewhere, your real offset, kept consistent).
* `asset_path`: path from the project folder.
* `persona`: `fangcun`, `buzhou` or `sehuan` (working names, not cleared handles).
* `tool` and `model`: what you actually used and the label **exactly as the app shows it that day**; if none is shown, write "not shown in app, YYYY-MM-DD". Never guess.
* `prompt`: the **full text you sent**, with a note of which files were attached. If you changed one word, log the changed text.
* `licence_notes`: use the template in section 7 of your pack. Start it with `PHOTOREAL v2;` in all three packs (the 步驟 pack requires it; it keeps these rows apart from the stylised ones). It records status, reason, parent file, references attached, human edits, plan name, terms read on (date and page) or "not yet read", **commercial use per those terms: NOT CONFIRMED** until you have read them, any visible mark, the conversation link, and the pack's extra fields (hand check at 200%, tucked side, patch side, look-alike check ID).

Rules that keep the file valid: **every image the tool hands you gets a row**, including ones you reject on sight (one word of reason); crops, resizes, colour fixes and the avatar are separate files with their own rows that name the parent; never edit or delete an old row (corrections go in a new row at the bottom); do not type CSV by hand, because prompts contain commas, line breaks and quotes, so paste each field into its own cell of a spreadsheet and save as CSV (UTF-8), or keep notes and ask Claude "Append these rows to assets/provenance.csv" (Claude cannot see your screen, so it needs the model label and the time from you; the 步驟 pack has a batch card for this). Expect 20 to 30 minutes of logging per sitting (*assumption*).

**Look-alike results** go in each pack's log table (方寸 and 色環: section 6.6; 步驟: `personas/buzhou/lookalike_log.md`, which you create from pack section 6.2; 色環 also keeps `personas/sehuan/lookalike_log.md`). Search-result screenshots may contain photographs of real people: keep that folder private, never post, share or reuse them, and delete them when the check is closed unless a complaint is open.

## 7. Why the labels and the four-place disclosure still apply

In plain language, because this is the part that is easiest to get wrong when the pictures start to look good.

**What you are making.** A character who looks like a real person and is openly an AI character from 明說角色工作室. The "openly" is the product. The research found that what audiences, platforms and regulators react against is not AI characters; it is AI characters people mistake for real people: a July 2025 AI influencer whose disclosure sat behind a "Read More" button caused mass confusion; the Guardian-reported brands using realistic AI "customers" (relayed by TVBS, UK data, second-hand); IKEA Taiwan's AI family image with distorted hands, ridiculed on Threads on 2026-06-01; and Life8's apology in July 2026 after a real model said an AI image copied his features (`research/competitors.md` section 5, `research/culture.md` 6.1; none re-verified).

**Why photoreal makes it more important, not less.** The clay and vector characters carried the disclosure in the picture itself: nobody thought they were photographs. A photoreal picture says nothing. Someone scrolling at speed cannot tell, so the words have to do the work. The chest patch on 步驟, once a visible "not a photo" tag, no longer counts as a disclosure. Nothing in the packs is designed to make a character pass as a real person: the studio look is composed and plain on purpose, the pictures are never candid, and the "is this a real photo?" test in the packs is information for calibrating the label, never a way to make a picture look more real.

**The four places, and what each one is for.** Every post of a photoreal character carries all four:

| Place | What it covers |
|---|---|
| 1. The bio (「AI 虛擬角色」 and the studio name) | People who visit the profile |
| 2. The first line of the caption (draft: 「【AI 虛擬角色】本篇由 AI 生成的虛擬角色「{name}」發布，圖像為 AI 生成，並非真人。」, "AI virtual character. This post is by the AI-generated virtual character {name}; the image is AI-generated and is not a real person.") | People who read the post before the "more" fold |
| 3. The on-screen badge on every image and every video frame (drafts: 「AI 生成｜虛擬角色」 on images that show a character, 「AI 生成｜示意圖」 or 「AI 生成」 on diagrams, lesson slides and empty sets; a small 「AI」 chip on avatars; the exact wording per character is in its addendum, section 8.2 or 7.1, and your wife rules) | The picture when it travels without its caption: screenshots, reposts, grid crops |
| 4. The platform's own AI label, switched on by hand | The platform, its ranking and the viewers who never open a caption |

Why not just one: each place fails alone. Captions get cut off, pictures get cropped and reposted, and platform labels can be missed or dropped by an editor's export, so the studio never relies on auto-detection. The badge is typeset in a design tool, never generated, with text at least about 3.5% of the image height (*assumption*) and inset at least 11% of the height from the top and bottom edges and at least 8% of the width from the sides (so a centred square crop of a 4:5 picture cannot remove it; see pipeline/qa-checklist.md D3). Your wife reads every character. Keep a screenshot of every published post showing all four.

**The platform and legal background (unverified).** TikTok, YouTube and Meta all require a label on realistic AI-generated people (BRIEF section 4). Instagram announced on 2026-08-31 an "AI-generated profile" label with recommendation limits for accounts that prominently feature a photorealistic AI person; whether it exists on a Taiwan account is still to be tested (`research/platforms.md`, `HUMAN_TODO.md` item 10). Taiwan's rules on AI-generated personal images in ads (the Fraud Crime Hazard Prevention Act ad chapter, the AI Basic Act and the Fair Trade Commission's endorsement rules) are recalled, not checked; no lawyer has been asked yet, which is why the questions are in `HUMAN_TODO.md`. So treat the four places as the minimum, not as legal clearance.

**What the labels do not do.** They do not excuse a candid-looking picture, a location tag, an "I tried it" line or a face that resembles a real person. Those are separate rules (section 5, items 1 and 6) and they still apply in full. A "是真人嗎" ("is this a real person?") comment is a signal: three in the first two weeks, or five in any week, means strengthen the badge and first line within 48 hours.

## 8. Hands, and what else fails in photoreal

**Hands are the top failure** (the IKEA Taiwan case). Every prompt keeps them out of the frame (the crop ends at the belt line or the waist) or fully inside pockets with no fingers or thumbs showing. Never ask for a gesture or a held object. Inspect every image you keep at 100% and then 200%, hands first. If one appears:

1. Reframe: crop it out of a copy if the framing still matches the prompt (and the crop does not cut off a tool's visible mark). Log the crop as a human edit.
2. Re-roll: send the prompt again for four new images.
3. Prompt fix: add the pack's positive framing line ("Both hands are outside the picture; the frame ends at the belt line").
4. One conversational edit in the same chat ("hide both hands in the pockets"). One try only; stacked edits make the face drift.
5. Switch tool and repeat 2 and 3.
6. Stop and discard. **Never** draw fingers, paint a hand, or paste in a photo of a real person's hand. A published image with a visible odd hand is a tripwire: correct or take it down within 24 hours, and two in six weeks pause the persona.

The full procedure is pack section 9.1 (方寸, 色環) and 10.2 (步驟). The other failures to expect, each with a fix phrase in the pack (section 9.2, or 10.1 for 步驟): plastic or airbrushed skin (your own complaint, so not optional), a young or student look, glare on the glasses, teeth, eyes that look in different directions, jewellery that appears, numerals on the belt or patch, a wrong earring wedge count, the tuck or patch on the wrong side, a candid or selfie look, and a face that drifts between chats. Reject, never repair, a face. **A look-alike is never repaired by editing**: regenerate with a changed attribute, or stop and tell Claude.

**Claude and faces.** Claude does not identify real people from faces and must not be asked who a character resembles. Claude can read a saved file against the checklist for a first pass, but it can miss details, and it cannot make your wife's judgements on age, colour read, Taiwan details or resemblance to a local public figure.

## 9. What to send back to Claude

After each sitting, paste this into Claude Code in this folder, filled in as far as you can. Partial is fine.

```
PERSONA (photoreal):     DATE:
TOOL(S) AND MODEL LABEL(S), exactly as shown: Gemini ___ / ChatGPT ___
PLAN NAME shown in my account: ___
MINUTES: set-up __  generating __  choosing __  logging __  wife __
CHOSEN MASTER (path): assets/<slug>/photoreal/R01_master_v1.png (buzhou: R01_pr_master_v1.png)   from candidate: ___
WHICH PROMPT WORKED: Gemini or ChatGPT version; rounds of 4 needed; any wording I changed or fix phrase I added (paste it)
SIDE: which side the hair is tucked on (sehuan) / which side the patch is on (buzhou), in the chosen master
KEPT AND DISCARDED: file paths with one word of reason (or: all in candidates/, rows logged)
FOLLOW-UP IMAGES DONE (path each): R02 ...
CHECKLIST rows that failed most often:
HANDS: did any appear? how many rounds to fix?
TOOL BEHAVIOUR: refused anything? text, numerals or colour codes appeared? visible mark, watermark or metadata seen? a seed shown? did the face drift between chats? did it start to look like another pilot?
MY OWN VERDICT: does it still look fake to me (yes / a bit / no), and where (skin, eyes, teeth, hair edges, hands)?
WIFE: APPROVE / SMALL FIX / REJECT per image, with the pack's reason code; her answers to this character's open questions
TESTS: age guesses (initials, number, job word); "reminds me of" answers word for word; reverse-image searches (tool, date, crop, any close match) or "not yet run"; uncanny score; "is it a real photo?" count; disclosure-legibility result
PROVENANCE: rows written (yes/no), or my notes attached for Claude to write them
LICENCE: terms read? date, page, plan, the key sentence; or "not yet"
```

Open questions to include, per character:

* **方寸:** do the glasses, low ponytail, sage vest and cream belt look natural or like a costume? Is the plain off-white studio "lifeless"? Pronoun and feature-wording rulings.
* **步驟:** which side the patch is on in the chosen master (then it is the rule for every image; never flip an image); does a man-presenting character feel natural with name-only copy; do the grey-on-grey clothes read as mourning or as a party colour; does the patch look like an app logo?
* **色環:** which side the tucked ear and earring show on in R01; does the muted disc read as a colour wheel, a rainbow flag or a costume; does the neckerchief read as airline-crew or shop-staff; does outfit B read as a school uniform; is the blush backdrop (淡蜜桃色) too pink or skin-coloured; does she accept the face-shape change from the bible's long oval to an oval with a narrow soft chin (made to separate 色環 from the other two)?

What Claude does with it: writes or checks the provenance rows, updates each addendum's status, records the tool test in `pipeline/tools.md` (the BRIEF's Phase 4 comparison covers consistency, API access, price and licence terms; your sessions supply the consistency and licence evidence), revises the prompts where a wife's ruling changes the wording, and renames the frozen set into the golden-set scheme.

## 10. If you get stuck

* One bad image in four: press regenerate. The same defect in two or more of four: add the matching fix phrase from the pack and make four more.
* Two rounds of four fail the same way in one tool: try the other tool. Both fail: stop and tell Claude.
* The age guess fails, a look-alike is named, a search shows a close match, or the thumbnail reads as young: stop and tell Claude. Do not repair these by editing. The design may need a change in the addendum.
* A tool refuses or answers only in words: see section 5, item 9.
* The face drifts between chats, or two characters start to look alike: new chat, attach only that character's R01, resend. Never continue a chat that made another pilot.

## 11. What the cross-pilot check of 2026-10-11 compared and changed

Compared: the three addenda and the three packs, on face, hair, face furniture, age cues, skin undertone, styling, palette, backdrop, lighting, platforms shared and test rules. The colour distances were recomputed with the functions in `personas/palette_check.py` (the script itself was not changed).

**Verdict.** The three characters are clearly different people on at least four of six axes for every pair; the weakest pair is 方寸 and 色環. Only the side-by-side test with real images can settle it.

**Changed (so the three files agree):**

1. The near-pair sections of the 方寸 addendum (section 10) and the 步驟 addendum (section 9) still compared against drafts of each other (stylised bibles, a bone backdrop, "not decided"). Both now carry the same settled three-way table. The 色環 addendum (section 10) was re-checked and its count corrected (it had counted age and skin as extra margin).
2. 方寸 pack: hex codes removed from every prompt (38 prompt lines and 2 fix phrases) and "hex codes" added to its avoid list, because the 步驟 and 色環 packs already used colour words and a code can be printed into the picture.
3. 方寸: expression E07 no longer allows parted lips (addendum and pack). Her own section 7 bans a parted-lip pose, and 色環 already kept lips closed in every expression.
4. 步驟: the age-guess rule now matches the other two (fail on any single guess under 25 or a median under 28; before, a median of 27 passed and one guess under 25 was tolerated). The panel size now agrees with its own table (five others, not "four or more").
5. 步驟: the badge is now 「AI 生成｜虛擬角色」 with the same size and crop-safe inset as the other two (it was 「AI 生成」, about 12% of the image width, with no inset, which a square crop of a 4:5 picture could remove).
6. 方寸 and 步驟 packs: the "one chat per character; never upload another pilot's image" rule (it existed only in the 色環 pack).
7. All packs and addenda: the near-pair test panel is the wife plus at least four others. 色環 pack: a note that rows 35 and 36 are housekeeping.
8. `pipeline/image-pack/README.md` now points here, and `personas/README.md` section 8 says the palette near-pair checks must be re-run on photos.

**Left alone on purpose:** 方寸 and 步驟 share a key-light side (they differ in backdrop, 25.6 apart, and in white balance); the `_pr_` file-name tag in the 步驟 pack only; each character's own badge colours; 步驟's E02 expression allows barely parted lips (a man; the checklist still checks the teeth); 步驟's optional empty 示意 rooms, which wait for your wife's sign-off.

**Not decided here (your wife's or yours):** the rulings listed in `HUMAN_TODO.md` ("Photoreal switch"), whether two woman-presenting photoreal pilots on Instagram are too alike, and the fallback if photoreal fails the uncanny, age or look-alike tests.

## 12. Where things are

* Packs: `pipeline/image-pack/fangcun-photoreal.md`, `buzhou-photoreal.md`, `sehuan-photoreal.md`
* Specs: `personas/<slug>/photoreal-addendum.md` (the addendum wins over the pack; the bible still holds voice, pillars, disclosure lines and monetisation; the addendum's section 0 lists exactly what it supersedes)
* Source of truth for everything the addendum leaves alone: `personas/<slug>/bible.md`
* Colour near-pair register: `personas/README.md` sections 5 and 8; script: `personas/palette_check.py`
* The log: `assets/provenance.csv`
* Your jobs, in order: `HUMAN_TODO.md` (the "Photoreal switch" section at the end, and items 10, 18 and 26)
* Rules and decisions: `BRIEF.md` section 3 (ground rules), `DECISIONS.md` (2026-10-11)
