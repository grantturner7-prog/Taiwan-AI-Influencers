# QA checklist: run on every draft before a human approves it

Written 2026-10-12 (Phase 4). It merges `research/culture.md` 7.6 (Taiwan-ness list) and 8 (reviewer brief), the 31-row image checklist and tests in `pipeline/image-pack/*-photoreal.md`, the disclosure rules of the three photoreal addenda, `strategy/portfolio.md` 1.4, 3.3 and 6.2, and `BRIEF.md` section 3. Every zh-TW string is an AI draft for the wife. Nothing here has been run on a real image yet.

## 0. How to use it

* **One run per draft**, before `review.wife_language` and `review.operator_facts` are set. The draft is the folder `pipeline/review-queue/<persona>/<date>_<NN>/`.
* **Who:** **C** = `python3 pipeline/scripts/queue.py validate <folder>` (Claude runs it first; a keyword net only). **O** = operator (hands, anatomy, numbers, sources, labels, files). **W** = wife (Traditional Chinese, Taiwan vocabulary, tone, culture, taboos, how it feels to a Taiwanese viewer). A row marked O+W needs both.
* **How:** look at every image at 100% and then 200%, hands first, beside the character's R01 master at the same size. Read every Chinese character on the image one by one. Read the caption aloud.
* **One failure anywhere stops the draft.** Fix code: **R** regenerate; **P** change the prompt (add the pack's fix phrase) and regenerate; **E** small local edit in a design tool (stray mark, colour cast, text, badge; log it as a human edit, keep the untouched original; **never** for hands, faces, skin, proportions or age); **X** stop and tell Claude (design problem or failed test; never repaired by editing).
* **Reason codes the wife writes** (from the reviewer brief): **V** vocabulary, **T** tone, **S** script or font, **E** experience claim, **R** regulated topic, **P** politics or sensitive, **D** disclosure missing, **X** cultural or visual error, **C** timing, **H** hands, people or other AI defect. She answers APPROVE, SMALL FIX or REJECT. Record the codes in `review.notes`.
* **Only humans set review fields.** `queue.py` never approves; a clean validate run is not approval.

## 1. What the automatic pre-screen (C) does and does not catch

`queue.py validate` checks: all `post.json` fields and types; id, folder, persona, platform, format, date; first caption line is 【AI 虛擬角色】; `ai_label_flag` true; on-screen label contains 「AI 生成」; hashtags are `#` strings and not follow-for-follow tags; sponsorship flag, type and caption tag agree; sources exist when the text makes claims; shot prompts name no real person or character; no media path marked approved while PENDING; and a **keyword net** over `hook_zh`, `caption_zh` and hashtags for lived-experience words, mainland vocabulary, Simplified characters, health, finance, gambling and politics wording, and one persona naming another. It **flags and never rewrites**. It cannot see images, judge tone, know whether a sentence is true, or tell a denial from a claim with certainty (denial sentences are shown as INFO so a human reads them). **A draft that passes C can still fail every row below.**

## 2. Disclosure and labels (Ground rule 1, 5, 8): O, with W on wording

Four places on every post: bio, first caption line, on-screen badge, platform label. Check them on the **published or scheduled preview**, not on the draft.

| # | Check | Pass | Who |
|---|---|---|---|
| D1 | Bio names 「AI 虛擬角色」 and 「明說角色工作室」 (studio name provisional) | Yes, on every platform account | O |
| D2 | First caption line is the AI line, before any hook or tag: 「【AI 虛擬角色】本篇由 AI 生成的虛擬角色「{名}」發布，圖像為 AI 生成，並非真人。」 (YouTube: 「本影片…畫面為 AI 生成，並非真人」) | Verbatim pattern, name correct | O+W |
| D3 | On-screen badge on **every** image and every video frame: 「AI 生成｜虛擬角色」 on images that show the character, 「AI 生成｜示意圖」 on diagrams or empty sets | Present, typeset in post (never generated), text at least about 3.5% of image height (assumption). **Inset: at least 11% of the image height from the top and bottom edges and at least 8% of the width from the sides.** A centred square crop of a 4:5 picture removes 10% of the height at the top and again at the bottom (1,350 px tall becomes 1,080 px: computed), so the packs' and addenda's "8% from every edge" is not enough vertically (review fix, 2026-10-12; the packs still say 8%) | O+W |
| D4 | Badge survives a centred 1:1 crop and the profile-grid crop (the grid crop ratio is recalled, unverified: check it on the live profile); not hidden behind platform buttons. Test it: crop a copy to 1:1 and look | Yes | O |
| D5 | Platform AI label switched on **by hand** (Instagram content-level disclosure and the account's AI-generated profile label; YouTube altered or synthetic content box plus description line) | On, and a screenshot of the post kept | O |
| D6 | Sponsored, client, gifted or affiliate content: tag directly under the AI line (【業配】 or 【合作內容】, 【廠商提供】, 【含分潤連結】), the "character has not used this product" sentence, the platform paid-partnership tool and the AI-disclosure control | All present; `sponsorship_flag` and `sponsorship_type` match | O+W |
| D7 | Avatar has the small 「AI」 chip; name field reads 「{名}｜AI 虛擬角色」 | Yes | O |
| D8 | Alt text on every image (draft: 「AI 生成的虛擬角色{名}，示意圖，非真人。」) | Present | W |
| D9 | No location tag, map pin or geotag | None | O |
| D10 | The disclosure is not buried: nothing hides it behind "more" and no wording claims "real person", "真人實拍", "非 AI" | Clean | W |
| D11 | Weekly count of 「是真人嗎」 comments | Under 3 in the first two weeks and under 5 in any week; otherwise strengthen the badge and first line within 48 hours (`portfolio.md` 6.2) | O |

## 3. Faces and bodies in photoreal stills (Ground rules 2, 3): O first, W second

Run the pilot's own 31-row (方寸, 色環) or 29-row (步驟) table in `pipeline/image-pack/<slug>-photoreal.md` section 5. Its locked features are the source of truth (glasses, hair, belt, earrings, headphones, patch, tuck side). The rows that apply to **every** pilot:

| # | Check | Pass | Who |
|---|---|---|---|
| F1 | **Same face as R01** at the same size: face shape, eye size and spacing, brows, nose, lips, jaw. If you hesitate, it fails | Same person | O+W |
| F2 | **Adult and visible age**: reads at least the stated age band at full size and still adult at 110 px tall; defined cheeks, faint age lines | Age-guess panel: no single guess under 25, median at least 28 | O+W |
| F3 | **Skin**: pores and fine texture visible at 100%; no airbrushed, waxy or too-perfect look; skin tone matches R01 | Natural | O+W |
| F4 | **Eyes (uncanny)**: same size, round pupils, both looking the same way, one soft catchlight each in the same place, no glassy stare, no mismatched lids | Natural | O+W |
| F5 | **Mouth and teeth**: lips closed per the pack; if teeth ever show they are separate and natural, not one white block | Clean | O |
| F6 | **Ears, hair, edges**: both ears natural (no stray earrings), hair edges and strands clean, nothing melted or merged | Clean | O |
| F7 | **Locked features present** and on the right side (earring wedge count, tuck side, patch side, belt ticks, glasses frame, headphones) | All present | O |
| F8 | **Outfit** is one of the approved outfits; colours inside the allowed range when sampled; no logos or text on clothes | Yes | O |
| F9 | **Modesty and no sexualised cue**: collarbone covered, relaxed fit, no glamour light, no parted-lip pose, no low angle, no body emphasis | Clean | O+W |
| F10 | **No candid or "my life" look** (Ground rule 4): no phone, mirror, selfie, food, drink, bag, product, home, street, shop, MRT; no motion blur; plain studio only | Clean | O |
| F11 | **Background and light** match the character's Studio Look (backdrop, key-light side, colour grade) | Same | O |
| F12 | **Not another pilot**: beside the other two pilots at about 110 px, unlabelled, five viewers say "different people" | Pass (repeat after any redesign or tool change) | O+W |
| F13 | **No political or taboo colour read** at thumbnail size: no party-colour camp, flags, red-and-blue or green-and-white pairs, no all-white or all-black outfit | Clean | W |
| F14 | **Files untouched**: the original download, not a screenshot or a re-save; any visible mark noted and left alone | Yes | O |
| F15 | **Overall 100% look**: does anything look wrong without your being able to say what? | Nothing | W |

## 4. Hands (the top failure: IKEA Taiwan, 2026-06-01)

| # | Check | Pass | Who |
|---|---|---|---|
| H1 | Prefer no hand in the picture: framing ends at the waist, or hands are fully inside pockets with no fingers or thumbs visible | Yes | O |
| H2 | If any hand, wrist or thumb shows: zoom to 200%; count fingers; check joints, nails, thumb side, wrist; no merged, extra or missing digits | Perfect, or the image fails | O |
| H3 | No pointing, holding, gesturing, waving, clasping or hand-to-face (arrows added in post do the pointing) | None | O |
| H4 | A hand defect is never painted over, redrawn or replaced with a real person's hand; follow the pack's hand fix procedure (reframe, re-roll, prompt fix, one edit, switch tool, stop) | Followed | O |
| H5 | A hand or face defect that reached publication is an incident | Correct or take down within 24 hours; two in 6 weeks pause the persona | O |

## 5. Text on images: garbled, Simplified or wrong (BRIEF section 5)

Generators garble Chinese or output Simplified forms, so **no generated text at all**; every character is added in post.

| # | Check | Pass | Who |
|---|---|---|---|
| T1 | The picture itself contains **no letters, numerals or Chinese characters** from the generator (including on belts, patches, signs, screens, labels), even if they look right | None. If Chinese appears, note it in the log and ask W whether it is garbled or Simplified (it tells us how the tool behaves) | O |
| T2 | Every character added in post is Traditional, in a Taiwan-glyph form (a TC font such as Noto Sans TC), legible at phone size | Read character by character | W |
| T3 | No Simplified, Japanese or Hong Kong forms; no mirrored or pseudo-characters | None | W |
| T4 | Numbers match the source slip digit for digit; units are 公分, 公尺, 坪, 平方公尺; dates read 資料日期：YYYY/MM/DD | Yes | O |
| T5 | Numbers that are not sourced carry 「示意數字」; fit or clearance slides carry 「請以現場丈量為準」 | Yes | O+W |
| T6 | Punctuation is full-width in Chinese lines; no stray ASCII quotes or bracket emoji such as [微笑] (mainland chat style) | Clean | W |
| T7 | Text is not cut off by the crop, the badge or the platform's UI | Clean at 4:5, 1:1 and 9:16 | O |
| T8 | Text on screen recordings (步驟): the recording is a dated, human-run capture; tool, version and plan are visible; no personal data on screen | Yes | O |

## 6. Motion and eyes (for any video or animation; none is produced yet)

Video, voice and lip-sync for a photoreal face are barred until a separate addendum exists. This section is here so it is not forgotten.

| # | Check | Pass |
|---|---|---|
| M1 | Blink rate and gaze look human; eyes never drift or cross; no dead stare | W+O |
| M2 | No face morphing, melting, flicker or identity drift between frames; same person as R01 on every frame | O |
| M3 | Lips match any audio; teeth stay stable; no "uncanny" mouth | W |
| M4 | Hands out of frame or fully hidden for the whole clip | O |
| M5 | Hair, glasses and jewellery stay put; locked features never change | O |
| M6 | Voice is labelled 「AI 生成語音」, passes the wife's Taiwan-accent listen, and is not a clone of a real person | W |
| M7 | Badge on every frame; platform label on | O |

## 7. Captions, hooks and voice (zh-TW): W, with O on facts

| # | Check | Pass | Who |
|---|---|---|---|
| V1 | **Taiwan vocabulary**: 影片 not 視頻, 資訊 not 信息, 品質 not 質量, 軟體 not 軟件, 儲存 not 保存, 創作者 or 網紅 not 博主 (full table: `research/culture.md` 3.1) | None of the mainland forms; C flags the clear ones | W (C first) |
| V2 | **Traditional characters only**; no 简体 | None | W (C first) |
| V3 | **Reads like a Taiwanese person**, not a translation; particles (喔, 啦, 耶) light and in character; no Taobao-style 親 or 寶子, no 絕絕子 | Natural | W |
| V4 | **On-voice** for this character: register, humour, "I" rules and running jokes follow the bible (`personas/<slug>/bible.md` section 3 and the sample lines) | A reader can tell this persona from the others in a blind read of three lines (week-6 test) | W |
| V5 | **Studio method phrase** 「先看 X」 used at most once in four posts; the intro 「我是{名}，AI 虛擬角色。」 only on the pinned post and first lines, not every post; the "I have no X, I only Y" frame used once in the persona's own words; only 方寸 uses 蓋 (蓋章) | Within limits (`personas/README.md` section 6) | W |
| V6 | **Pronouns**: 方寸 uses the name, 「這個角色」 or 「我」, never 他 or 她, unless the wife has ruled otherwise | Yes | W |
| V7 | **Hook** answers itself in the post, makes no result promise ("in N days"), and is not a fear hook about money, health or the law | Yes | W |
| V8 | **Facts**: every number, price, date, spec, rule or timetable matches a source in `sources` (claim, URL or file, date); no placeholder such as {廠商} or UNVERIFIED left in a post | Matches | O |
| V9 | **No unsourced superlative** (最好, 第一名, 最划算, 保證); comparisons are dated tables | None | W |
| V10 | **Hashtags**: relevant, Traditional, no follow-for-follow or like-for-like tags, no health, finance, gambling or political tags | Clean | W (C first) |
| V11 | **Length** fits the platform (Instagram about 2,200 characters, Threads about 500; both limits recalled, unverified) | Fits | O |
| V12 | **Replies** (when drafted): start 「這是自動回覆訊息。」 if automated; Mandarin only; never mention or tag another persona; politics is hidden, never bot-replied | Yes | O+W |

## 8. Lived-experience wording and imagery (Ground rule 4)

The character has never eaten, worn, used, tested or visited anything. It presents, explains, compares and demonstrates, with dated sources.

| # | Check | Pass | Who |
|---|---|---|---|
| L1 | No testimony words: 愛用, 回購, 開箱, 實測, 親測, 試用, 試穿, 心得, 踩雷, 避雷, 神器, 必買, 上身, 穿起來, 用起來, 住起來, 我今天…, 我試了, 我用過, 我去了, 打卡, GRWM, day-in-my-life, "I tried", "I wore" | None (C flags them; a denial such as 「不是我量出來的」 is allowed only when the wife agrees it denies) | W (C first) |
| L2 | No invented customers, reviews, results, before-and-after, "my flat", "my room", "my wardrobe" | None | W |
| L3 | A paid or gifted post says the character has not used the product; the room or product placement is labelled AI 生成示意, not a real scene | Yes | O+W |
| L4 | Scenes are labelled as AI-generated, not places the character visited (「AI 生成場景，非實際到訪」) | Yes | W |
| L5 | Demos are dated human recordings (步驟) or published specs, never "I tested" | Yes | O |
| L6 | Image shows no holding, wearing-as-product, eating or using (a brand garment on the character only as labelled 虛擬試穿示意 client work, lawyer question) | Clean | O+W |
| L7 | Regulated territory absent (Ground rule 6): no health, medical, weight-loss or cosmetic-efficacy claim; no investment or financial advice; no gambling; no politics, elections or cross-strait content; fabric-performance words only as the brand's quoted, dated spec | Clean | W+O |
| L8 | A published testimony, health, finance or politics line is an incident | Take down within 24 hours; pause 7 days; root-cause note (`portfolio.md` 6.2) | O |

## 9. Look-alike and originality (Ground rule 2): O+W, before first use and again on any change

| # | Check | Pass |
|---|---|---|
| O1 | No prompt names a real person, celebrity, influencer, model, actor or existing character; no "looks like" or "in the style of" followed by a name (`gen_image.py` also refuses these) | Yes |
| O2 | Only the character's **own** generated images were uploaded as references; no photo of any real person (not you, not your wife, not a friend), no screenshot, no fan art, no other pilot's image | Yes |
| O3 | Reverse-image search by hand (Google Lens, Bing Visual Search, TinEye; head-and-shoulders and tight-face crops; plus eyes-to-mouth and mirrored for the final master); no close match; no face-recognition people-search services | Pass; screenshots kept private in `lookalike/`, deleted when the check closes |
| O4 | The wife's local-public-figure check (news presenter, actress, singer, model, influencer, politician, athlete, host, anyone she knows) | No resemblance. Names stay in the internal log, never in a prompt |
| O5 | Blind test: 「Who does this remind you of?」 to the age-guess panel | Nobody names a real person or existing character |
| O6 | Never repair a look-alike by editing; regenerate with a changed attribute or stop and tell Claude | Followed |
| O7 | Every asset has a row in `assets/provenance.csv` the same day (prompt, tool, model label as shown, licence notes); `queue.py validate` warns when a media file has none | Yes |
| O8 | Re-run O3 to O5 on any new outfit family, hair or glasses change, model or tool change, a monthly sample of finals, annually, and on any complaint (take down within 24 hours; pause until a documented check) | Scheduled |

## 10. Taiwan-ness (merged from `research/culture.md` 7.6)

| # | Check | Who |
|---|---|---|
| X1 | Every character on the image is Traditional, in a Taiwan-glyph form, legible; no garbled strokes | W |
| X2 | No real brand logos used as an implied endorsement; background presence only | O |
| X3 | No legible real licence plate; plate side correct (scooters: rear only); right-hand traffic, steering wheel on the left; riders wear helmets | O+W |
| X4 | MRT line colours match their names; no invented station maps or timetables | W |
| X5 | Convenience stores look like 7-ELEVEN or 全家 (seating, hot-food counter); bubble-tea cups are film-sealed, not dome-lidded | W |
| X6 | Temple scenes accurate and respectful; nothing mixed with Japanese shrines; no deity jokes | W |
| X7 | Homes: shoes off, tiled floor, Type A or B sockets, window grilles; no Western carpeted house | W |
| X8 | Weather and clothing suit the season (no maple leaves in Taipei in November, no puffer coats in summer) | W |
| X9 | People look locally plausible and ordinary, not a default K-pop or Japanese idol template; adult appearance | W |
| X10 | No red star, PRC flag or political symbols; no party colours | W |
| X11 | No funeral objects, white-and-black pairing, or the number four in celebration imagery; gifting taboos respected | W |
| X12 | Scenes labelled AI-generated, never "a place I visited" | W |

## 11. Timing and taboos (reason code C)

| # | Check | Who |
|---|---|---|
| C1 | Not 228 (2027-02-28) and not an election day (recalled as 2026-11-28, unverified); no election hooks or party colours in the first weeks | O+W |
| C2 | Not in the 2027 ghost month (2027-08-02 to 08-31, computed) for launches; neutral explanation only | W |
| C3 | Not during a disaster or typhoon pause; the pause switch overrides the schedule | O |
| C4 | Commercial calendar fits (農曆新年 2027-02-06, 元宵 2027-02-20, computed); no brand-paid 雙11 content this year | O |
| C5 | The first post of a persona is not on the same day as another persona's first post (no coordinated launches); no two personas promote the same brand in the same week (`portfolio.md` 3.3) | O |
| C6 | Weekly approvals stay at or under the planning ceiling of 22 (`queue.py validate` warns) | O |

## 12. Sign-off and incidents

1. C: `validate` shows no ERROR and no FLAG for the draft.
2. O: sections 2 to 5, 7 (V8, V11), 8 (L3, L5, L7), 9, 10 (X2, X3) and the file checks done; the operator sets `review.operator_facts` to `approved` or `changes`.
3. W: sections 2 (D2, D3, D6, D8), 3, 5, 7, 8, 9 (O4, O5), 10 and 11 done; she sets `review.wife_language` to `approved` or `changes` with reason codes in `review.notes`.
4. Both set: media generated and logged (no PENDING left), badges on, platform labels on, screenshots kept. Then **a human** sets `review.approved` to true by editing `post.json`. Run `queue.py approve <folder>` to see what still blocks it. This holds for every post for at least the first 30 days.
5. After publishing: screenshot the four disclosure places; log minutes spent by each person (it feeds the capacity gates in `portfolio.md` 5 and 6).

Standing incidents from `portfolio.md` 6.2, in short: a platform strike or label dispute pauses that persona on that platform; a Ground-rule-6 or testimony line in a published post is taken down within 24 hours and the persona paused 7 days; a likeness complaint is taken down within 24 hours and paused until a documented check; a missing disclosure is fixed within 24 hours; garbled or Simplified Chinese or a wrong fact that reached publication is corrected within 24 hours, and two in six weeks pause the persona until this step is fixed.
