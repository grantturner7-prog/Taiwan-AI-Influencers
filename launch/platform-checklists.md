# Platform checklists: Instagram, Threads, YouTube (and templates for Facebook Page and LINE) (DRAFT v0.1, 2026-10-12)

For the operator. **Every menu name, path, limit and rule below is recalled from background knowledge or taken from search summaries, and is UNVERIFIED** (`research/platforms.md` section 0: no primary page was opened). The live screen is the authority. Where this file says "find it", the job is to find the real control, screenshot it with the date, and write the real name in the evidence log. Persona values (handles, bios, avatars) are in `personas/<slug>.md`; studio-level set-up (mailbox, vault, two-factor, recovery, who may do what) is in `00-studio-setup.md`. A human does every step; Claude cannot create, verify, log in or publish.

Tick boxes are for you to fill in; none is ticked.

## 0. Facts and limits this file relies on

| Item | Value used | Status |
|---|---|---|
| Instagram username | Letters, numbers, periods, underscores; up to 30 characters | recalled, unverified (`personas/README.md` section 2) |
| Instagram name field | About 30 characters, searchable | recalled, unverified |
| Instagram and Threads bio | About 150 characters | recalled, unverified (the three bibles state it the same way) |
| Instagram links in the profile | Several are allowed (recalled: up to 5); use **one**, the link page | recalled, unverified |
| Instagram account switcher | Up to five accounts in the app | medium (S35, `research/platforms.md`) |
| YouTube handle | 3 to 30 characters; letters, numbers, underscores, hyphens, periods | recalled, unverified |
| YouTube channel name / description | About 50 / 1,000 characters | recalled, unverified (bibles: 1,000 for the description) |
| YouTube channel banner | 2560 x 1440 px with a safe area of about 1546 x 423 px; the upload dialog states the current numbers | recalled, unverified |
| Instagram "AI-generated profile" label | Announced 2026-08-31; accounts prominently featuring a photorealistic AI person without it may lose recommendation eligibility; **Taiwan scope not confirmed** | existence high, Taiwan scope unverified (S27, S28) |
| Meta "AI info" label on content | Applied from industry markers or self-disclosure; creators must use the disclosure tool for organic photorealistic video or realistic audio; stills not confirmed | medium (S29, S30) |
| YouTube altered or synthetic content | Creators disclose realistic synthetic people and voices; YouTube labels automatically from May 2026 when it detects significant photorealistic AI use | medium (S40) |
| Paid partnership label on Meta | Added in the Instagram app; with the brand's permission; gifts count; may not be settable through third-party schedulers | medium (S32); scheduler point unverified |
| YouTube paid promotion | "My video contains paid promotion..." box; viewers see a disclosure at the start; the box does not satisfy Taiwan disclosure law | medium (S41) |
| Taiwan law | Disclosure duties for endorsement ads (薦證廣告) and AI personal images in ads exist; wording, fines and articles are **unverified**; nothing here is legal advice | unverified (`research/legal.md`) |

## S1. AI-label settings: one table for every platform

All three platforms get the label **by hand on every post** (`ai_label_flag` is true on every draft in `pipeline/review-queue/`), even where a platform might auto-detect or exempt the content. Auto-detection depends on file markers that editing may drop (hypothesis), so never rely on it.

| Platform | Account-level setting | Content-level setting | Where the text disclosure sits | Check after publishing |
|---|---|---|---|---|
| Instagram | "AI-generated profile" label, on from day one if offered; if it is not offered or says it is unavailable in your region, screenshot that, keep the strongest manual disclosure, re-check weekly | The post flow's AI-content disclosure ("Advanced settings" or similar, name unverified), on for every post, carousel and Reel | Name field 「{名}｜AI 虛擬角色」; bio line 1; first caption line 「【AI 虛擬角色】…」; on-image badge 「AI 生成｜…」; avatar chip "AI" | The live post shows the platform's AI label; the four text places are visible without tapping "more" |
| Threads | Whether the profile label carries over from Instagram: not found; find and record | The disclosure tool for AI content on Threads, name unverified; on for every post that has an image or video | Same name field and bio; first line of every post | Same |
| YouTube | None found for channels | The upload form's altered or synthetic content question: **Yes** for every Short that shows the character | Channel name and description; first description line; on-screen badge | The Short shows the AI label below or over the player; YouTube may add or lock a label itself: do not dispute it |
| Facebook Page (not planned) | Same Meta system; a Page, never a profile | Same as Instagram | Same | Same |
| LINE Official Account (not planned) | None found | None found; LINE's own AI label applies to stickers | Account name and profile text; every automated message starts 「這是自動回覆訊息。我是 AI 虛擬角色…」 | n/a |

## S2. Paid-partnership tools: set up now, use later

No sponsored, gifted or affiliate post is possible in the first 30 days (business not registered, lawyer unanswered, `calendar-30d.md` of each pilot). Setting up now means **finding and screenshotting each tool**, so the sponsorship checklist is written from the real screens and not from memory.

| Platform | Tool | Set-up job now | When a paid post exists |
|---|---|---|---|
| Instagram | "Paid partnership" label in the post flow (path unverified); branded-content eligibility under the creator tools (`https://help.instagram.com/1372533836927082`) | Find the toggle in a draft post, screenshot it, delete the draft; read the eligibility page and write down any requirement | Publish **from the Instagram app, not a scheduler**, until a scheduler is shown to set the label; tag the brand with its permission; caption tag first; AI-disclosure control on |
| Threads | Same tool and same policy page (`https://help.instagram.com/2467529163409127`) | Find it, screenshot it | Same |
| YouTube | "Includes paid promotion" box in the upload form | Find it in the upload form of a private draft, screenshot | Tick it; say 「本片為業配內容。」 aloud or on screen in the first seconds; description tag first |
| All | Taiwan caption tags: 【業配】, 【合作內容】, 【廠商提供】, 【含分潤連結】 (`strategy/portfolio.md` 1.4) | None | Order of the AI line and the commercial tag **differs across the three bibles** (see `README.md` section 7, item 6): pick one studio rule before the first sponsored post |

Gifted items count as paid relationships on Meta (S32). Client creative or a free sample posted on a persona account is treated as 【合作內容】 (`portfolio.md` 1.4); whether a public free sample is an advertisement is a lawyer question.

---

## A. Instagram professional account (once per persona that uses Instagram: 方寸, 色環, and 步驟 only if Threads needs it)

**A.0 Before you sit down** (all must be true; otherwise stop)
- [ ] Gates A1 to A7 of the persona file are closed (`personas/<slug>.md` section 7).
- [ ] The avatar file exists, passed its tests and has the **AI** chip (`personas/<slug>.md` section 5).
- [ ] The strings N1 and B1 (+ B2) are approved by the wife.
- [ ] The vault entry for this account exists with a generated password; the studio mailbox is open on your computer; your phone is charged; a private evidence folder outside the repo is open.
- [ ] You can finish in one sitting (about 70 minutes, assumption).

**A.1 Create**
- [ ] Install or update Instagram from the phone's official store. No cloned, dual or emulated app.
- [ ] Sign up with the **studio mailbox** (not a personal address). Paste the vault password. Real date of birth of the person creating it (`00-studio-setup.md` section 6).
- [ ] Username: the first free candidate in the persona file's order. If taken, take the next and record it. Name field: N1.
- [ ] Do not sync contacts, do not follow any suggested account, skip "find friends".
- [ ] Pass any code, phone, ID or selfie check yourself. If the app suspends the sign-up, stop, tell Claude, and do **not** start another account.

**A.2 Professional account**
- [ ] Settings, account type and tools, switch to a professional account (path unverified). Creator or Business: decision D3 (`README.md` section 5). Whichever you choose must offer scheduling, the AI label settings and the paid-partnership tool; check, and note which you chose and why.
- [ ] Category: a plain one that claims no credential (never stylist, consultant, designer, 收納師 or tutor). Hide the category label if unsure.
- [ ] Contact options: the studio mailbox only. No phone number, no address, no personal email.
- [ ] Do not connect a Facebook Page or any Facebook profile; turn off sharing to Facebook and other apps.

**A.3 Profile**
- [ ] Avatar with chip uploaded; check the preview in the circular crop.
- [ ] Bio: B1 on line 1, B2 on line 2 (or the variant the wife chose). Pronouns field empty (the characters have no gendered pronouns in copy).
- [ ] Link: **leave empty** until the link page is live and `check_pages.py --final` passes (gate A8). Then the persona's page only.

**A.4 AI labels** (section S1)
- [ ] Find the account-level "AI-generated profile" label (menu name unverified). Switch it on. Screenshot the setting and the profile showing it. If it is not offered, screenshot the absence and the date, and write "NOT AVAILABLE" in the sign-off.
- [ ] Start a draft post (not published). Find the content-level AI disclosure in the post flow. Screenshot it. Check it stays set when you reopen the draft. Delete the draft.

**A.5 Paid partnership** (section S2)
- [ ] Find the paid partnership toggle in the draft and the branded-content settings. Screenshot. Do not use.

**A.6 Interaction settings** (names unverified; find the nearest control)
- [ ] Comments: turn on the offensive-comment filter and Hidden Words; keep comments open. Message requests: filter on. Tags and mentions: manual approval if offered.
- [ ] No auto-replies, no saved-reply automation beyond text you paste by hand, no chatbot (Ground rule 9).

**A.7 Security** (`00-studio-setup.md` sections 5 and 6)
- [ ] Two-factor on, by the strongest method offered; the code or secret is in the vault. Backup codes in the vault and one printed copy.
- [ ] Recovery email and phone set so that either of you can recover. Run the recovery test once.
- [ ] Sessions list shows only your devices; no connected apps.

**A.8 Follows**
- [ ] The account follows nobody on day one. Never follow another persona; never follow-for-follow; official sources only, if at all.

**A.9 Evidence and sign-off**
- [ ] Screenshots (kept outside the repo): profile with bio and avatar; AI label setting; post-flow AI disclosure; paid partnership toggle; two-factor screen; recovery screen. One row each in `evidence-log.csv`.
- [ ] Persona file section 9 filled in. The wife reads the live profile aloud.

**Done when:** the profile shows the name field, bio, avatar chip and (if offered) the AI-generated profile label; two-factor and recovery are on; nothing has been posted; the evidence is logged.

---

## B. Threads account (方寸: not used; 步驟 and 色環: yes)

**B.0 Before**
- [ ] The persona's Instagram account exists and its A checklist is done. Threads is believed to need an Instagram login (**unverified**): on the Threads sign-up screen read whether it does. For 步驟 this decides whether the Instagram prerequisite account is created at all. If Threads offers a sign-up without Instagram, tell Claude before choosing: the plan changes.

**B.1 Create**
- [ ] Install Threads. Choose "log in with Instagram" and select the **right persona's** account in the switcher (a wrong pick attaches the wrong identity; check the name field before confirming).
- [ ] Profile: import the name and bio from Instagram or type the persona file's text (B-strings). Public profile. Link empty until gate A8, then the persona's page.
- [ ] If an option to share posts to the fediverse or to another network is offered, leave it off (unverified; it would copy posts to places you cannot label or moderate).

**B.2 Labels and settings**
- [ ] Find what Threads offers for AI content (account-level, post-level). Screenshot, write the real name in the log. Use the post-level disclosure on every post with an image or video; the text first line covers text-only posts (the text-only wording is an open approval, `calendar-30d.md` of 步驟 and 色環).
- [ ] Hidden Words filter on; who can reply and mentions: choose deliberately and write the choice down; plan to hide political or off-topic replies, not to answer them.
- [ ] Paid partnership: find and screenshot (section S2). Do not use.

**B.3 Security and evidence**
- [ ] Security is Instagram's (the login is shared); confirm it in the Threads settings and screenshot.
- [ ] Evidence rows and persona sign-off as in A.9.

**Done when:** the Threads profile matches Instagram, the label options are recorded, nothing has been posted.

---

## C. YouTube channel (方寸: yes; 步驟: yes; 色環: not in the pilot)

**C.0 Before**
- [ ] The studio Google account exists with two-factor (the studio mailbox, `00-studio-setup.md` section 9).
- [ ] Persona gates A1 to A7 are closed; the avatar and the **banner** are ready; N1 and the channel description are approved.
- [ ] **Banner (PENDING, human-built):** a solid ground in the persona's backdrop colour with the line 「AI 虛擬角色｜{名}｜明說角色工作室」 typeset in a design tool in a Taiwan-glyph font, optionally with a cut-out of the approved headshot carrying the 「AI 生成｜虛擬角色」 badge. No generated text. No generation prompt is needed unless the cut-out is a new AI image, in which case use the persona's pack prompt and log it. Safe-area numbers are in section 0; the wife reads every character.

**C.1 Create**
- [ ] Sign in as the studio Google account. Create the channel as a **Brand Account** with the name N1 (flow and wording unverified).
- [ ] In YouTube Studio, customization, basic info: handle (first free candidate), description, links (the link page only, after gate A8), contact email (the studio mailbox, for business enquiries), country Taiwan.
- [ ] Avatar with the **AI** chip; banner.
- [ ] Verify by phone if asked, yourself.

**C.2 Permissions**
- [ ] Studio, settings, permissions: add the operator and the wife with their own Google accounts (role names recalled: Owner, Manager, Editor, Viewer; unverified). Both have two-factor. Nobody signs in as the studio account except to change permissions.

**C.3 Upload defaults and community**
- [ ] Upload defaults: visibility private by default; "not made for kids"; a description template whose first line is the persona's YouTube AI line (`personas/<slug>.md` section 6); standard licence; no ads settings.
- [ ] Community defaults: hold potentially inappropriate comments for review; add a blocked-words list reviewed by the wife (political party and candidate names, scam phrases, adult terms); no automated replies.

**C.4 Labels and paid promotion** (S1, S2)
- [ ] Open a private draft upload with a throwaway test file only if you must (no public upload, no unlisted test channel); find the **altered or synthetic content** question and the **paid promotion** box; screenshot both; delete the draft. If you cannot test without publishing, leave this to the first real upload (`schedule.md` section 4) and set it by hand then.
- [ ] Shorts: record the real maximum length, the safe zones and the caption fold from the app (`HUMAN_TODO.md` 25).

**C.5 Monetisation and standing**
- [ ] Do **not** apply to the partner programme (payouts are planned at NT$0 in year 1) and do not add AdSense now. The "inauthentic content" rule targets templated mass AI output; one original script per video (`research/platforms.md` 4.3).

**C.6 Evidence and sign-off**
- [ ] Screenshots: channel page, About, permissions, upload defaults, the two questions. Evidence rows; persona sign-off; the wife reads the live channel page aloud.

**Done when:** the channel shows the name field, description, avatar chip and banner; both humans can manage it with their own login and two-factor; nothing is uploaded.

---

## D. Facebook Page (template; NOT planned for any pilot, Wave 3 only: 歲歲, 里程, 等一下)

Do not create a Page now. If a later wave plans one:
- [ ] A **Page**, never a personal profile for a character (a non-human profile is a fake account, S34). Admins are your own real profiles, with two-factor.
- [ ] Page name 「{名}｜AI 虛擬角色」; username letters, numbers and periods only (no underscore, recalled, unverified) in the persona's period form (handle rule H3); About text from the persona's bio; category without a credential.
- [ ] Same Meta AI-label and paid-partnership steps as A.4 and A.5; Page roles for the two of you; comment filters; no auto-replies.

## E. LINE Official Account (template; studio level only; free plan; DEFERRED until an audience exists)

Do not create it now (`portfolio.md` 7 and 2B: retention channel, not discovery; LINE VOOM closed 2026-09-30). When the time comes:
- [ ] One studio-level account, name 「明說角色工作室」, no persona name. Free 輕用量 plan (200 free messages; prices rise 2026-11-01 for the paid tiers; the **billing unit of a broadcast is unresolved**, so send no broadcast until you have read it in the manager: `research/platforms.md` 3.4).
- [ ] Profile text states 「AI 虛擬角色」 characters are made and run by the studio.
- [ ] Greeting and auto-reply: **off**, or worded 「這是自動回覆訊息。我是 AI 虛擬角色，由明說角色工作室創作與營運。」 (Ground rule 9). No bulk identical messages (LINE's terms reportedly bar them; dated, low confidence).
- [ ] Two-factor and an admin role for each of you; any paid plan is logged in `COSTS.md` and needs a decision first.
