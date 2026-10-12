# 步驟 (buzhou): launch checklist, DRAFT v0.1 (2026-10-12)

**Status.** Pilot, slot 2, AI tools (N7). YouTube Shorts primary, Threads second, plus an Instagram account that Threads probably needs (unverified); first post is Thu 2026-11-19 in the calendar (assumption). No account exists, no handle has been checked, no avatar exists (PENDING), and nothing has been cleared. Every zh-TW string is an AI draft for the wife; the studio name 明說角色工作室 is provisional and unsearched. This file gives the *values* for 步驟; the *steps* for each platform are in [`../platform-checklists.md`](../platform-checklists.md) and the studio-level setup (mailbox, password manager, two-factor, recovery) is in [`../00-studio-setup.md`](../00-studio-setup.md). Nothing in this repo may hold a password, recovery code, two-factor secret, API key or phone number. File names without a folder (`README.md`, `schedule.md`, `00-studio-setup.md`, `platform-checklists.md`, `evidence-log.csv`) are in the parent folder `launch/`; `link-pages/` and `templates/` are also under `launch/`.

Sources: `strategy/portfolio.md` 1.4, 2B and 5.2; `personas/buzhou/bible.md` 2.2 and 8; `personas/buzhou/photoreal-addendum.md` 8.2; `research/platforms.md` 4; `pipeline/image-pack/buzhou-photoreal.md`. Platform limits and menu names are recalled and **unverified**: read the live field or menu and trust it over this file.

## 1. Accounts to create

| # | Platform | Role | Why | Notes |
|---|---|---|---|---|
| 1 | YouTube channel (a Brand Account) | Primary (Shorts with dated screen recordings) | `portfolio.md` 2B row 2 | Managed by two permissioned users, not a shared password (`00-studio-setup.md` section 9) |
| 2 | Threads account | Second (text takeaways and prompt templates) | Cheap secondary on the Meta stack | Same login as Instagram (unverified); the handle may follow the Instagram username (unverified) |
| 3 | Instagram account (technical prerequisite for Threads, **unverified**) | No posts at launch | `bible.md` 2.2: probably needed as the Threads login | Same name field, bio, avatar and AI-generated profile label as the others; do not post. Confirm in the Threads sign-up whether it is needed at all, and if it is not, do not create it |

**Not used in the pilot:** Facebook, TikTok, LINE. Three Instagram-login accounts exist across the pilots (方寸, 色環 and this prerequisite), inside the five-account switcher limit (`portfolio.md` 2.6).

## 2. Handles (availability UNCHECKED)

Rank order is the bible's (`personas/buzhou/bible.md` 2.2). Check logged out, as a public profile URL or by typing it into the sign-up field and stopping before you submit; **do not create accounts to test names, do not park placeholders, never buy or trade a handle** (`personas/README.md` section 2). Record every result. A free handle is not trademark clearance. Use the first free candidate in rank order on every platform if possible; if a platform forces a different one, write it in the last column.

| Rank | Handle | Chars | YouTube @handle | Threads | Instagram | Risk (from the bible) |
|---|---|---|---|---|---|---|
| 1 | `step0_ai` | 8 | UNCHECKED | UNCHECKED | UNCHECKED | generic; may be taken or look like a code term; echoes 第 0 步 |
| 2 | `stepwise_ai` | 11 | UNCHECKED | UNCHECKED | UNCHECKED | very generic; no link to the Chinese name |
| 3 | `buzhou_steps` | 12 | UNCHECKED | UNCHECKED | UNCHECKED | pinyin reads as 不周; do not use unless the wife says it is fine; if 驟 reads zòu, change to `buzou_steps` |

Search each string as a person's name too (Ground rule 2). The `_ai` suffix makes the handle itself a disclosure (rule H1). Threads handles may follow the Instagram username (unverified), so check Instagram first for the Threads and Instagram pair and YouTube separately.

Check log (fill in; one row per check):

| Date | Handle | Platform | Free / taken / similar taken | Similar account (describe, never contact) | Wife: confusable? | Decision |
|---|---|---|---|---|---|---|
| | | | | | | |

## 3. Text to paste (zh-TW DRAFTS for the wife)

Lengths are counted by `check_launch_docs.py` (characters, a line break counts as 1, the full-width bar ｜ counts as 1). Limits are recalled and unverified: Instagram and Threads bio about 150, name field about 30, YouTube channel description about 1,000, YouTube channel name about 50, handle 30 (`platform-checklists.md` section 0).

### 3.1 Name fields

| ID | Where | Text | chars | English gloss |
|---|---|---|---|---|
| N1 | Instagram name, Threads name, YouTube channel name | `步驟｜AI 虛擬角色` | 10 | 步驟 / AI virtual character |

The name field is searchable and is the only disclosure that shows in comments and search results, so it carries 「AI 虛擬角色」 itself.

### 3.2 Bios

| ID | Where | Text | chars | English gloss |
|---|---|---|---|---|
| B1 | Threads bio and Instagram bio, line 1 (the bible's line, unchanged) | `AI 虛擬角色｜步驟｜AI 工具功能對照與提示詞範本，附資料日期｜螢幕錄影由工作室真人操作｜明說角色工作室 創作與營運` | 59 | AI virtual character / 步驟 / AI tool feature comparisons and prompt templates, with data dates / screen recordings operated by a real person at the studio / created and run by 明說角色工作室 |
| B2 | Threads and Instagram bio, line 2 (recommended; added for photoreal) | `角色為 AI 生成，非真人。角色本身沒有使用過任何工具，不是工具廠商的官方帳號。` | 40 | The character is AI-generated, not a real person. The character itself has never used any tool and is not a tool vendor's official account. |
| B3 | Instagram prerequisite account, extra line (optional, wife rules) | `此帳號目前不發布內容，內容請見 Threads 與 YouTube。` | 34 | This account currently posts no content; see Threads and YouTube. |

* B1 + B2 (line break between): **100** characters in total (limit about 150, unverified).
* B1 + B2 + B3 (Instagram prerequisite account): **135** characters in total (limit about 150, unverified).

#### B4: YouTube channel description (the bible's text, unchanged)

```
【AI 虛擬角色】
步驟是由 AI 生成的虛擬角色，不是真人，由明說角色工作室創作與營運。
角色本身沒有使用過任何工具；影片中的螢幕錄影由工作室真人操作，並標示工具、版本、方案與錄製日期。
內容只說明、比較公開資訊，並附上資料來源與日期。工具更新很快，請以官方頁面為準。
本頻道與影片中提到的工具廠商無隸屬關係；若有業配、廠商提供的方案或分潤連結，會在影片與說明欄清楚標示。
不提供投資、醫療、法律或賺錢相關的建議。
```

Length: 208 characters.

English gloss: [AI virtual character] 步驟 is an AI-generated virtual character, not a real person, created and run by 明說角色工作室. The character itself has never used any tool; the screen recordings in the videos are operated by a real person at the studio and show the tool, version, plan and recording date. Content only explains and compares public information, with sources and dates; tools update quickly, so the official page prevails. This channel has no affiliation with the tool vendors mentioned in the videos; any sponsored post, vendor-supplied plan or affiliate link is clearly marked in the video and description. No investment, medical, legal or make-money advice.

### 3.3 Alt text (every image)

| ID | Text | chars | English gloss |
|---|---|---|---|
| T1 | `AI 生成的虛擬角色步驟，非真人。` | 17 | AI-generated virtual character 步驟, not a real person. (The bible gives no alt text for 步驟; this copies the 色環 form. The QA checklist form adds 「示意圖」.) |

### 3.4 Changes from the bible, and why

* B2 is new. The bible's bio had no 「非真人」 line; with a photoreal man-presenting avatar the addendum treats 'mistaken for a real person' as a risk (`photoreal-addendum.md` 7, risk 2), so the bio now says it in words. The wife rules; B1 alone satisfies the portfolio pattern.
* B3 is new and optional: a dormant Instagram account with no explanation would confuse people who find it. The wife rules.
* B4 is the bible's text. It says 「本頻道」 (this channel), which is right for YouTube; the link page uses 「步驟與影片、貼文中提到的工具廠商無隸屬關係」 because it covers Threads too.

## 4. Link page and pinned content

* **Link in bio (YouTube About, Threads, and the Instagram prerequisite if it exists):** the 步驟 link page, `<LINK-PAGE-HOST>/buzhou/` (URL **not chosen**). Do not put the link in until `check_pages.py --final` passes.
* **Pinned post (Threads):** the first Threads post, `pipeline/review-queue/buzhou/2026-11-19_01` (T1), if the app allows pinning (limit unverified). Draft only; not reviewed.
* **YouTube Shorts:** four Short drafts are in the review queue (`2026-11-19_02`, `2026-11-22_02`, `2026-11-26_02`, `2026-11-29_02`); none has a recording (media PENDING) and every Short is **on HOLD** until the user confirms that still images of the photoreal character inside a video are acceptable (`calendar-30d.md` section 9 item 1). Captions only, no synthetic voice (gate G5 open).
* **Highlights, Stories:** none.

## 5. Profile image (PENDING)

The avatar is the picture the Instagram AI-generated-profile label is about, so it is the most label-sensitive image of the persona. It is a tight head-and-shoulders crop of the approved master with the **AI** chip added by hand. No image exists. Nothing is generated here.

| Item | Rule |
|---|---|
| Source | R07: a crop of an approved image, or the AI route below, tight head and shoulders, face centred and filling about 60% of the image width, **headphones fully visible**, grey backdrop visible around the head, margin so a circular crop keeps the whole head and both headphone cups (`buzhou-photoreal.md` 4.5) |
| Size and format | Export 1080 x 1080, PNG or high-quality JPG; platform minimums and crop shapes are unverified, check each upload preview |
| Circle crop | Preview a circle over the square: both headphone cups, the whole head and the chin inside; face centre about 50% across and 45% down (assumption). The chip must be **inside the circle** |
| AI chip | Latin letters **AI**, typeset in a design tool, never generated. Style: bone fill `#EEECE7`, charcoal letters `#2B3038`, thin charcoal outline (the addendum's badge style, readable on the grey backdrop). Reference size 220 x 128 on 1080, lower right on the shoulder side, not over the chin or mouth. Legible at 110 px; not at 40 px, so the name field carries the disclosure |
| Thumbnail tell at 110 px | Over-ear matte charcoal headphones, short black hair with a side parting, the boxy light-grey jacket collar. The sewn six-square patch is a recognition mark only and no longer a disclosure (addendum 0.1) |
| Check at 40 and 96 px | Still reads as an adult; headphones still visible; tag still readable at 96 px (`pack` 4.5) |
| Never | A photo of any real person; generated text or numerals; hands; a logo; a beauty filter or skin smoothing; another persona's face or image as a reference |
| Tests before use | Adult-reading check, age-guess panel (no single guess under 25, median at least 28), look-alike procedure, three-pilot side-by-side test and the disclosure-legibility test (`photoreal-addendum.md` 8 and 9; `pipeline/qa-checklist.md` section 3) |
| Platform behaviour | Platforms may re-encode the file and drop generator markers (hypothesis). The on-image chip and the name field are the durable disclosure |

**Media record (PENDING until the file exists).**

| Field | Value |
|---|---|
| path | `PENDING` (will be `assets/buzhou/photoreal/R07_pr_avatar_v1.png`) |
| description | Square tight head-and-shoulders avatar of 步驟 (man-presenting, over-ear charcoal headphones), neutral calm expression, studio grey backdrop, AI chip at lower right inside the circular crop |
| shot_prompt | the AI route below, only if the crop route fails the checks |
| provenance | one `assets/provenance.csv` row for the file and one for its parent, same day (`pipeline/scripts/provenance.py`); the AI chip is a human edit, say so in the row |
| used on | YouTube channel avatar, Threads and Instagram avatar, link page (`avatar.webp`) |

Generation prompt carried from `pipeline/image-pack/buzhou-photoreal.md` section 4.5 (R07) (attach the persona's own approved R01 and its headshot only; never any photo of a real person, never another persona's image):

```
CHANGE ONLY: the framing. Avatar.
FRAMING: tight head and shoulders, front-on, face centred and filling about 60 percent of the image
width, headphones fully visible, neutral calm expression, lips closed, no hands visible, grey
backdrop visible around the head. Leave enough margin that a circular crop keeps the whole head and
both headphone cups.
OUTPUT: 1 image, square (1:1).
```

Finish in a design tool, never with the generator: crop the headshot to a square, add the **AI** chip as typeset Latin letters (style in the table), keep the whole head and chip inside the circular crop (use [`../templates/avatar-guide.svg`](../templates/avatar-guide.svg)), preview at 110 px and 40 px, export one copy, keep the untouched original and the layered file, log both.

## 6. Settings that are specific to 步驟

| Setting | Value | Why |
|---|---|---|
| Instagram account-level AI label (prerequisite account) | Switch on the 'AI-generated profile' label if offered (path and Taiwan availability unverified) | `bible.md` 2.2 and 8.4; addendum 7 risk 4 |
| Threads AI label | Find and record what Threads offers for AI content; use it on every post (unverified) | `platforms.md` 4.2: profile label on Threads not found |
| YouTube altered or synthetic content | Yes on every Short that shows the character, even if YouTube would exempt it; first description line 「【AI 虛擬角色】本片由 AI 生成的虛擬角色「步驟」說明；螢幕錄影由工作室真人操作。資料日期：{YYYY/MM/DD}。」 | Addendum 7.1: platform label always ON for photoreal; `bible.md` 8.2 |
| Paid partnership tools | Locate and screenshot on YouTube and Threads; **do not use** in the first 30 days | No sponsor, vendor-supplied plan or affiliate is possible before registration and the lawyer |
| Comments | Hold potentially inappropriate comments for review; reply only by the approved templates; never ask viewers for personal data | `bible.md` 3.5 and tripwires; the face makes the data-request tripwire higher severity (addendum 7 risk 7) |
| Voice | None. Captions only | Gate G5 is open and a synthetic voice on a photoreal face is out of scope (addendum 7 risk 8) |
| Location tags, following | No location tags. Follow no other persona; no follow-for-follow | `portfolio.md` 3.3 |

## 7. Gates

| # | Gate | Owner | Needed before | State (2026-10-12) |
|---|---|---|---|---|
| A1 | Wife's reading test of the studio name and 步驟 (`HUMAN_TODO.md` 18) | Wife | Account creation | OPEN |
| A2 | TIPO and 經濟部 searches for the studio name and 步驟, Chinese and romanised (`HUMAN_TODO.md` 20) | Operator, wife | Account creation | OPEN |
| A3 | Handle check on each platform in section 2 (`HUMAN_TODO.md` 21) | Operator | Account creation | OPEN, all UNCHECKED |
| A4 | Avatar approved: master set passes the adult-reading, age-guess, look-alike and near-pair tests (`personas/buzhou/photoreal-addendum.md`, `pipeline/qa-checklist.md` section 3) | Operator, wife | Account creation | OPEN, no image exists |
| A5 | Commercial-use terms of the exact image tool and plan read and recorded (`HUMAN_TODO.md` 33). Until then every image is internal design material: **no public account** | Operator | Account creation | OPEN |
| A6 | Studio mailbox, password manager and two-factor method decided (`00-studio-setup.md` sections 3 to 5) | Operator, wife | Account creation | OPEN |
| A7 | Wife has read and approved every string in section 3 and the link page text (`link-pages/README.md` section 4) | Wife | Account creation | OPEN, all DRAFT |
| A8 | Link page deployed and `check_pages.py --final` passes (`link-pages/README.md` section 6) | Operator | Putting the link in the bio | OPEN |
| A9 | Instagram "AI-generated profile" label checked on a Taiwan account (`HUMAN_TODO.md` 10 and 38; `README.md` section 5, decision D1) | Operator | First post | OPEN |
| A10 | Lawyer's launch-gate answers (`HUMAN_TODO.md` 9 and 37; `research/legal.md` 12) | User | First post | OPEN |
| A11 | Business registration started (`HUMAN_TODO.md` 4 and 7) | Wife (registrant, to be confirmed) | First post | OPEN |
| A12 | Wife's reviewer trial on about 10 sample posts passed (`HUMAN_TODO.md` 8) | Wife | First post | OPEN |
| A13 | STOP 3: sample posts approved (`BRIEF.md` section 6) | User | First post | OPEN |
| A14 | First batch approved in `pipeline/review-queue/` for the first two weeks (`schedule.md` section 2) | Wife, operator | Scheduling | OPEN, 0 of 8 drafts approved (4 Threads, 4 Shorts) |
| A15 | The user confirms still images of the photoreal character inside Shorts are acceptable (calendar section 9 item 1) | User | First Short | OPEN, every Short is on HOLD for it |
| A16 | Decide captions-only against a labelled synthetic voice (gate G5) | User | First Short | OPEN, calendar assumes captions only |

An account may be created only when A1 to A7 are all closed. A first post needs every row closed. Closing a row means a date, who closed it and where the evidence is (`evidence-log.csv`).

## 8. Who does what and in what order

| Step | What | Who | Estimate (assumption) |
|---|---|---|---|
| 1 | Close gates A1 to A7 (section 7) | Wife, operator | see `README.md` section 4 (launch/) |
| 2 | Confirm in the Threads sign-up whether an Instagram login is needed; if yes create the Instagram account first (`platform-checklists.md` A), then Threads (B) | Operator | about 70 min plus 25 min |
| 3 | Create the YouTube channel under the studio Google account, add the wife and operator, description B4, avatar, banner, defaults, 2FA (`platform-checklists.md` C) | Operator, with the wife adding herself | about 50 min |
| 4 | Run the label and scheduling dry run in the real accounts without publishing (`schedule.md` section 4) | Operator | about 20 min per platform |
| 5 | Screenshot the four disclosure places and the settings, log them | Operator | about 10 min |
| 6 | Read the live profiles aloud; check the name field, the chip and the link | Wife | about 20 min |

Estimates are *assumptions*. Setup is extra to the weekly hours in `strategy/portfolio.md` 5.3 and competes with the 6 hours a week; see `README.md` section 4 (launch/). The recording hygiene kit and the vendor-terms reading (calendar section 9 items 2 and 14) are content jobs, not account setup, and are not counted here.

## 9. Sign-off (fill in by hand)

| Item | Date | Done by | Evidence file name (kept outside the repo) |
|---|---|---|---|
| Threads sign-up checked: Instagram login needed? (yes or no, date) | | | |
| Instagram prerequisite account created (if needed) | | | |
| Threads account created | | | |
| Handles recorded (platform, date) | | | |
| Name field and bios pasted (B1, B2, optional B3) | | | |
| Avatar with AI chip uploaded | | | |
| Link added (after A8) | | | |
| AI-generated profile label: on, or NOT AVAILABLE (date) | | | |
| AI label options on Threads recorded | | | |
| Paid partnership toggles located, not used | | | |
| 2FA on, backup codes stored in the password manager | | | |
| Recovery email and phone set (both people can recover) | | | |
| YouTube channel created, permissions set for both people | | | |
| YouTube description (B4) and avatar set | | | |
| Dry-run scheduling check done on Threads and YouTube | | | |

## 10. For the wife: what to read

B1, B2, B3, B4, N1 and T1, then the whole link page. Rulings needed: 「非真人」 in the bio; whether B3 is wanted; whether 「步驟｜AI 虛擬角色」 reads naturally; how she pronounces 驟 (zòu or zhòu; `HUMAN_TODO.md` 18); whether the pinyin handle `buzhou_steps` reads as 不周; whether the avatar (when it exists) reads as an adult and as an AI character in two seconds.

