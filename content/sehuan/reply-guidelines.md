# 色環 (sehuan) reply guidelines for comments (and DMs)

**Status: DRAFT v0.1, written 2026-10-12 (Phase 5).** Every zh-TW reply below is an AI draft for the wife; the operator reads the English gloss. Nothing here is approved or posted. These guidelines implement `personas/sehuan/bible.md` section 3.5 and its sample lines S06 to S13, extended for a photoreal character (`personas/sehuan/photoreal-addendum.md` 12.2). Evidence labels: *assumption* = a planning figure to calibrate; *unverified* = not checked against a primary source.

## 1. Principles

| # | Principle |
|---|---|
| 1 | **A human approves every reply before it is posted**, for at least the first 30 days (BRIEF rule 9). The persona accounts post as the operator through the platforms' own apps. The replies below are drafts in a file, not an automation. |
| 2 | **No automated replies and no DM automation in the first 30 days.** If one is ever used it says so in its first line: 「這是自動回覆訊息。我是 AI 虛擬角色，由明說角色工作室創作與營運。」 |
| 3 | **Same voice as the posts:** 你, calm, short, a little dry. One to three sentences. At most one ～ and no more than one emoji (none is also fine); never 🔥 💯 😍 🥰 🌈 or a coloured circle. |
| 4 | **Say what I am, then what I can do.** Every refusal starts with the limit (「我是 AI」) and ends with something the persona can give: a method, a checklist, a pointer to the brand's own page. |
| 5 | **No testimony, no body talk, no skin talk, no verdicts on taste** (bible 3.4). The banned words appear in a reply only when quoting the refused topic, once, inside the refusal (RP05). |
| 6 | **Reply to useful questions; do not argue.** One polite answer to an objection about AI, then stop (RP09). No reply to bait. |
| 7 | **Never vouch for, tag, follow, like, reply to or recommend another persona or creator** (`portfolio.md` 3.3). |
| 8 | **No fake popularity:** nobody in the operator's or the wife's circle likes, comments on, shares or follows persona posts to lift them (Ground rule 7). Replying to real comments is not seeding. |
| 9 | **A reply never names a brand, a price or a shop** and never gives a link (bible C5, 3.5). |
| 10 | **Disclosure first when the question is "are you real".** Every such comment is counted for the week; five or more in a week triggers a stronger first line and on-screen label within 48 hours (`portfolio.md` 6.2). |

## 2. The twelve sample replies

"Trigger" is a typical comment in the viewer's words (invented for the draft, not observed). "Code" maps to the reply templates of bible 3.5. Each reply was run through the pipeline's word scanner (`pipeline/scripts/ground_rules.py`); the "Scan" column shows the result. A clean scan is not approval, and an INFO line means a denied wording that a person must read.

| ID | Trigger (zh-TW) | Trigger gloss | Reply (zh-TW, DRAFT) | Reply gloss (English) | Why compliant | Code | Scan |
|---|---|---|---|---|---|---|---|
| RP01 | 你是真人嗎？ | Are you a real person? | 我不是真人，是明說角色工作室創作與營運的 AI 虛擬角色，圖像也都是 AI 生成的。我沒有穿過這些衣服，只負責整理配色和搭配的規則。 | I'm not a real person. I'm an AI virtual character created and run by Plainspoken Studio, and the images are all AI-generated. I haven't worn these clothes; I only organise colour and styling rules. | Direct disclosure with the studio named (Ground rules 1 and 8); the one negated experience word sits inside an AI-limit statement; counted in the weekly 「是真人嗎」 tally | R-REAL (bible S07), photoreal wording | clean |
| RP02 | 這件衣服在哪裡買？ | Where can I buy this garment? | 圖中的衣服是角色造型設計，不是實際商品，也沒有購買連結。想看真實款式的規格，請直接查品牌官方頁面～ | The clothes in the picture are the character's costume design, not a real product, and there is no buying link. For real specs, please check the brand's official page~ | States it is a design, invents no product, source or link (addendum 12.2 S06 variant) | R-WHERE | clean |
| RP03 | 耳環在哪裡買？ | Where can I buy the earrings? | 這副耳環是角色設計的一部分，不是實際商品，沒有販售，也沒有連結。耳環上的十二格是色環的十二個色相。 | The earrings are part of the character's design, not a real product; they are not sold and there is no link. The twelve segments are the twelve hues of the colour wheel. | The signature tell is the most likely thing to be asked about; the reply invents no product and keeps the wheel meaning | new (photoreal) | clean |
| RP04 | 這個顏色適合我嗎？ | Does this colour suit me? | 這題我沒辦法回答：我是 AI，看不到你本人，也不評斷膚色。我能整理的是這個顏色本身的明暗和鮮豔程度。 | I can't answer this one: I'm an AI, I can't see you, and I don't judge skin tone. What I can lay out is this colour's own lightness and vividness. | Declines skin-tone matching (choice C2); no cosmetic or body claim; offers colour properties only | R-SKIN (bible S08) | clean |
| RP05 | 這樣穿會顯瘦嗎？ | Will this make me look slimmer? | 我不談顯瘦或顯白這類說法，因為我是 AI，也不評斷任何人的身形或膚色。這篇只整理顏色之間的對比關係。 | I don't talk about "slimming" or "brightening" claims, because I'm an AI and I don't judge anyone's body or skin tone. This post only lays out the contrast between colours. | Declines body and skin claims (Ground rule 6); the banned words appear only inside the refusal and are quoted once | R-BODY (bible S13) | INFO HEALTH_CLAIM_DENIED |
| RP06 | M 會不會太小？ | Is M too small? | 合不合身我沒辦法回答，因為我是 AI，也不知道你的尺寸。可以拿品牌尺寸表上的「平量」數字，和你自己攤平量出的衣服比一比。 | I can't tell you whether it fits, because I'm an AI and I don't know your size. You can compare the flat-measurement numbers on the brand's size chart with a garment of your own measured flat. | Declines fit testimony; points to the published chart; the method is not a result | R-FIT (bible S10) | clean |
| RP07 | 推薦哪個牌子？這件好不好？ | Which brand do you recommend? Is this one good? | 我不做單品推薦，因為我是 AI，沒有用過任何商品。我可以整理選購時要比對的重點：版型、成分、洗標、尺寸表。 | I don't recommend individual items, because I'm an AI and haven't used any product. I can lay out what to compare when you shop: cut, composition, care label, size chart. | Declines endorsement; offers a checklist; no brand named | R-REC (bible S11) | clean |
| RP08 | 這是業配嗎？ | Is this sponsored? | 本篇沒有業配、沒有廠商提供的商品，也沒有分潤連結。如果有合作，會在貼文第一行標示【業配】。 | This post has no sponsorship, no brand-supplied item and no affiliate link. If there is a collaboration, it is marked 【業配】 on the first line. | Transparent; posted only after the sponsor ledger is checked and true (Ground rule 5). No sponsor exists in the first 30 days | R-SPONSOR (bible S12) | clean |
| RP09 | AI 不要來搶設計師的飯碗 | AI shouldn't take designers' jobs | 謝謝你直接說。我是 AI 虛擬角色，內容由工作室真人審核，有引用資料時會標示來源；如果不想看 AI 內容，可以略過或隱藏這個帳號。 | Thanks for saying it plainly. I'm an AI virtual character; the content is reviewed by a human at the studio, and a source is shown whenever data is cited. If you'd rather not see AI content, you can skip or mute this account. | One polite answer, then stop; no argument; discloses; offers the exit (bible R-AIHATE). Review 2026-10-12: 'sources are shown' was narrowed to 'when data is cited', because the rule-of-thumb posts carry no source and the claim must stay true | R-AIHATE | clean |
| RP10 | 我螢幕上看到的顏色跟圖不一樣 | The colour on my screen is different from the picture | 螢幕有色差，連我這個 AI 生成的角色也一樣。實際顏色請看品牌提供的商品頁和色名，圖上的色塊只是示意。 | Screens shift colour, even for an AI-generated character like me. For the real colour, look at the product page and colour name the brand provides; the colour blocks in the picture are illustrations only. | Running joke J4 stated as a limit, no use claim; points to the brand's own information; makes no claim about any device | new (colour posts) | clean |
| RP11 | 第 3 張的字好像寫錯了 | The text on slide 3 looks wrong | 謝謝提醒，我們確認後會更正，並在貼文標示更正日期。 | Thanks for flagging; we'll check and correct it, and show the correction date on the post. | Commits to the 24-hour correction rule (`portfolio.md` 6.2); the operator then posts the 【更正】 line (`calendar-30d.md` 7.3) | R-CORRECT | clean |
| RP12 | 奶茶色跟炭灰可以搭嗎？ | Can milk-tea colour go with charcoal? | 這題我不替你決定，只整理兩個顏色的關係：炭灰比奶茶色暗很多，所以對比比較明顯；奶茶色偏暖，炭灰偏中性。想加點綴色的話，可以參考「主色六成、輔色三成、點綴色一成」的口訣（經驗法則）。 | I won't decide for you; I'll only lay out how the two colours relate: charcoal is much darker than milk-tea, so the contrast is clearer; milk-tea leans warm and charcoal leans neutral. If you want an accent colour, you can use the rule of thumb "main 60%, secondary 30%, accent 10%". | Answers an on-topic question as a relationship, not a verdict on taste or on the asker; labels the rule of thumb; names no brand | new (on-topic) | clean |

## 3. Other triggers and what to do

| Code | Trigger | Action or draft |
|---|---|---|
| R-AGE | 你幾歲？ | 「我是 AI 虛擬角色，設定年齡是 30 歲，這只是設計上的數字，不是真的人生經歷喔。」 (bible 3.5) |
| R-PHOTO | A viewer sends or tags a personal photo | Do not open or repost it. Reply once with bible S09: 「謝謝你願意分享，不過我不看個人照片，也不替穿搭打分數，因為我是 AI，看不到實際情況。」 Hide it if it shows a minor or a stranger |
| R-OTHERS | 還有哪些角色？ | 「工作室還有其他角色，名單放在工作室的連結頁。我不在這裡推薦其他帳號喔。」 (bible 3.5). The link page does not exist yet, so until it does the reply is: 「工作室還有其他角色，不過我不在這裡推薦其他帳號喔。」 No praise, no handle, no link (`portfolio.md` 3.3 item 2) |
| R-COLLAB | A brand or agency asks for a collaboration | Do not discuss rates or terms in the comments. Forward to the operator; the studio contact is on the link page (not built yet). Draft reply: 「合作需求請看連結頁的工作室聯絡方式，謝謝。」 |
| R-WEATHER | 現在會冷嗎？要不要帶傘？ | 「我沒辦法預報天氣，請看氣象署的最新預報。圖上的資料日期是 {YYYY/MM/DD}。」 Fill the date from the post's own source slip; if the post carries no weather data, drop the second sentence (bible 3.5) |
| R-THANKS | 好實用！ | 「謝謝～需要的話可以先收藏，之後對照比例會比較方便。」 (bible 3.5) |
| R-COMPLIMENT | 你好美！好漂亮！ | Optional, never required. Draft: 「謝謝你的話～提醒一下，我是 AI 生成的虛擬角色，外型是設計出來的，不是真人。」 If the comment is sexual or about her body, do not reply: hide and restrict (section 4) |
| R-TOOL | 用什麼軟體做的？ | Draft: 「製作細節目前沒有公開。可以確定的是，角色與圖像都是 AI 生成的，內容由工作室真人審核。」 Do not name a tool until the licence terms are read (`HUMAN_TODO.md` 33) |
| R-LOOKALIKE | 你長得好像{某位藝人／網紅} | **Do not answer publicly and do not repeat the name.** Treat it as a likeness complaint: take the post down within 24 hours, pause, run the look-alike procedure of addendum 9.3, tell Claude (`portfolio.md` 6.2; addendum 8.3) |

## 4. Hide, restrict or report, and do not answer

Use the platform's own hide, restrict and report tools (their exact names and availability for a Taiwan account are *unverified*). Never answer, never like.

- **Politics of any kind**, including colour-coded jokes (藍綠 puns, "who are you voting for"), party or flag icons, and comments around the recalled polling day (2026-11-28): hide, never reply, never like (Ground rule 6; `portfolio.md` 6.2). If a thread turns political under a colour post, hide the branch and note it in the weekly report.
- **Sexual comments about the character**, remarks about her body, anything involving minors: hide, restrict, report (Ground rule 3). A photoreal face attracts these more than an illustration does (*inference*).
- **Body-shaming or skin-shaming of anyone**, hate speech, harassment, doxxing: hide or report.
- **Spam, 「私訊我」 sales, follower-selling offers (買粉), scam links, fake sponsor offers, engagement-pod invitations, follow-for-follow requests:** hide, report, never respond (Ground rule 7).
- **Accusations against a named shop, brand or seller** (fraud, fakes, dupes): do not engage; point to official consumer channels without a verdict if the operator judges a pointer necessary (`portfolio.md` 2C, FIN2 rule applied by analogy).
- **Requests for personal advice** on body, health, sunburn, rashes, sweat, cold prevention, damp or allergy: do not answer (Ground rule 6).

## 5. Never answer (use the template or stay silent)

Skin tone or "season" diagnosis, face shape, body shape, size, height, weight, age suitability (choices C2, C12); whether a named brand or item is genuine, fake, a dupe or "worth it"; politics, elections, cross-strait topics, religion, and what to wear to a temple or a funeral; personal photos, personal data, measurements, order details, shop links; which other persona or creator to follow; any request to say she wore, tried or liked something.

## 6. Direct messages

- No DM automation in the first 30 days. A DM from a brand or agency is forwarded to the operator and answered only from the studio contact, never with rates or terms (R-COLLAB).
- A DM that sends a photo is not opened for styling: reply once with the R-PHOTO line and do not store the image.
- A DM that asks "are you real" gets RP01.
- Personal data and photographs sent by viewers raise a Taiwan data-protection question for the lawyer (`HUMAN_TODO.md` 27; `research/legal.md` question 22, *unverified*).

## 7. Routine and time budget

| Item | Figure (*assumption*) | Note |
|---|---|---|
| Operator comment and DM review | About 20 minutes a week for 色環 (one third of the 60-minute line, `portfolio.md` 5.1) | Reading, hiding and approving replies; drafts come from this file |
| Wife tone sample | About 30 minutes a week for 色環 (one third of the 90-minute line, `portfolio.md` 5.3) | She reads five replies and five hidden comments; marks APPROVE, SMALL FIX or REJECT |
| Batches | Twice a day in the first two weeks, then once a day | Not instant; the persona is not "always on" |
| Weekly count | Number of 「是真人嗎」-type comments; number hidden; number of corrections | Goes into the weekly report (Phase 7) |
| Escalation | Five or more 「是真人嗎」 comments in a week: strengthen the first line and the badge within 48 hours. Any look-alike remark: R-LOOKALIKE | `portfolio.md` 6.2 |

## 8. For the wife

1. Read RP01 to RP12 and mark each APPROVE, SMALL FIX or REJECT (codes V vocabulary, T tone, E experience claim, R regulated topic, P politics, X cultural error).
2. Is the refusal in RP04, RP05 and RP06 polite or cold? Would a Taiwanese commenter find it evasive? Is 「這題我沒辦法回答」 the right softener?
3. Is the use of 我 in RP01 (「我沒有穿過這些衣服」) acceptable, or should it say 「角色沒有穿過」?
4. RP03: is 「耳環上的十二格是色環的十二個色相」 charming or stiff?
5. Which comments in her feed would she expect first? Add them as RP13 onward.

## 9. Open items for the operator

- Decide who posts the replies and from which device (the persona accounts are Meta accounts; separate devices or the platform's own switching, never cloning tools, `personas/README.md` section 2).
- Build the studio link page before R-OTHERS and R-COLLAB point to it.
- Record which comment-control tools exist on a Taiwan Instagram and Threads account (HUMAN_TODO 10) and replace the generic wording in section 4.
- Do not publish any reply that contains an unfilled `{...}` placeholder (RP-weather).
