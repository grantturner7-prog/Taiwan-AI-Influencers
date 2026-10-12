# Outreach playbook (Phase 8), DRAFT v0.1

Written 2026-10-12 for the operator (English) and the wife (who reads the zh-TW and is the likely sender). Studio name 明說角色工作室 / Plainspoken Studio is provisional and uncleared. **Nothing here has been used. No message has been sent, no contact has been verified, and nothing may be sent by Claude: outreach is sent by the two of you, by hand.** All Taiwan-law points are **unverified, lawyer question**. All minutes and volumes are **assumptions** to measure on the first five messages.

Files in this folder: [README.md](README.md) (index and counts) · target lists [fashion](target-list-fashion.md), [AI tools and SME services](target-list-ai-tools.md), [home](target-list-home.md) (each with a CSV) · [email-drafts.md](email-drafts.md) (T1 to T6) · [tracking-template.csv](tracking-template.csv) · [check_outreach.py](check_outreach.py).

## 0. Read this first

1. **What outreach is for in this project.** It serves the studio revenue checkpoint (`strategy/portfolio.md` 6.4 and hypothesis H5): by week 8 of the pilots, at least 5 warm fashion contacts approached, at least 1 free scoped sample delivered, at least 3 written rate quotes gathered from agencies or creators (monetisation gaps G1, G2, G11); within 6 months at least one written B2B quote or accepted free sample, otherwise B2B is treated as unproven and spend stays at NT$5,000 a month or below. "Week 8" counts from the pilots' first posts; W0 2026-11-16 is only a label (DECISIONS 2026-10-12), not a date to plan sending around.
2. **What it is not.** Not a mass campaign; not a growth hack; not a way to raise follower numbers (Ground rule 7); not a way to sell anything the persona bibles decline. Brand-paid work of any kind needs the registered business and the other gates in [rate-card.md](../rate-card.md) section 0.
3. **No result is assumed.** The project holds no Taiwan figure for how a disclosed-AI studio's cold outreach is answered (Phase 1: not found), and Phase 1 found that brands may prefer verifiable humans (Kolr 2026). So **no reply rate, no conversion rate and no revenue is forecast here.** Measure from the first five messages and report the real count.
4. **Most important honesty rule.** Every message says what the studio is: a very small studio of openly labelled AI characters, with no past work, no client and no audience figure. Nothing is implied that is not true.

## 1. Gates before the first message (all open on 2026-10-12)

| # | Gate | Why | Where it is tracked |
| :-- | :-- | :-- | :-- |
| G1 | A registered business exists (or the registrant question is settled) and the **legal name** is known | The signature cannot be filled without it, and only a registered business invoices. Until then the drafts contain `[STUDIO LEGAL NAME / REGISTRATION: TO FILL]` and cannot be sent | `HUMAN_TODO.md` 4, 7 |
| G2 | The studio name is cleared (wife's reading test, TIPO search, 經濟部 business-name search) | A recipient will search the name; a clash or a bad tone is hard to undo | `HUMAN_TODO.md` 18, 20 |
| G3 | A studio mailbox exists, separate from any personal address; the person named in the signature has agreed to be named | Recipients answer the mailbox; the signature must be real. Not yet created | studio kit section 10 |
| G4 | The lawyer has answered outreach questions **O1 to O3** (section 8), a new [Gate: outreach] | Whether a first B2B email needs more than an opt-out line is unverified | to add to the lawyer list (open item 1) |
| G5 | The wife has read every zh-TW string in [email-drafts.md](email-drafts.md) and the signature block | Ground rule 9 spirit and the whole project rule: no native-unreviewed zh-TW goes out | `HUMAN_TODO.md` 8, 35 |
| G6 | For any **free sample only:** the exact image tool's commercial-use terms are read and recorded | The studio must not make client work on unread terms | `HUMAN_TODO.md` 33 |
| G7 | For a **fashion virtual try-on** only: the lawyer has answered whether labelled 虛擬試穿示意 creative can mislead | On hold; face-free options need no answer | `HUMAN_TODO.md` 27, 37 |
| G8 | The do-not-contact sheet and the tracking sheet (working copy, outside git) exist | Section 5 and 6 cannot work without them | this folder |
| G9 | Per row: `verified_on` filled (existence, route, no "no unsolicited proposals" notice) | The lists are unverified | each CSV |

**Before G1 to G5 close, the only permitted outreach is the private, verbal version to the operator's warm fashion contacts** (`content/sehuan/b2b-pitch.md` A3): the studio is exploring disclosed virtual-presenter creative, nothing exists yet, a free scoped sample is being planned, no price, no character name or handle, no image. No email, no form, no direct message.

## 2. Who does what

| Person | Does | Does not |
| :-- | :-- | :-- |
| **Wife** | Reads and corrects every zh-TW draft; is the natural sender of record for zh-TW messages (from the studio mailbox); reads every Chinese reply; reads each recipient's inquiry page and any notice about unsolicited proposals; leads any call in Mandarin | Sends anything the operator has not seen the English gloss of; agrees to any term, price or exclusivity by message |
| **Operator** | Chooses rows, opens each recipient's page (a browser translation may help to find the form, but the wife reads any notice), fills the slots, keeps the tracking sheet and the do-not-contact sheet, logs `outreach_sent` and later signals in `analytics/templates/lead_signals.csv`, handles English-language recipients and the warm contacts, produces any sample with Claude's diagrams | Sends Chinese text the wife has not read; promises a price, date or outcome |
| **Claude** | Drafts and updates the lists and templates; on request drafts a reply for the wife's review from text the humans paste in; runs `check_outreach.py`; keeps the open items | Sends, posts, logs in, contacts any person, platform or company, approves anything, sees a credential, or sets a review field. Claude has no memory between sessions: paste the tracking row and the reply into a new session |

## 3. Order of work and weekly time

**Order.** Wave 0: the operator's warm contacts, verbally (before the gates; see section 1). Wave 1: the P1 rows of each list, fashion first, then AI tools (whose P1 rows include the three agencies to ask for rate sheets), then home. Wave 2: P2 rows after Wave 1 is answered or closed. P3 rows only if the first two waves leave capacity; they are large or multinational and unlikely to answer. HOLD and SKIP rows are never contacted. The fashion order follows the research (B2B fashion is the best-supported studio route); the AI-tools agencies are early because the checkpoint needs three written rate quotes.

**If fewer than 3 rate sheets or quotes have arrived by week 6,** widen the ask to the P2 agencies in the AI-tools list (台北數位集團, 藍眼科技, TenMax, AD2, CreatorDB; 貝立德 is reported to be a Dentsu group agency, so it shares one thread with 台灣電通 and is a weak candidate) and also record the **public** prices of 3 to 5 Taiwan AI-creative studios or freelancers (HUMAN_TODO 11), which need no outreach.

**Volume and time (assumptions, to be measured).**

| Item | Assumption | Basis |
| :-- | :-- | :-- |
| New first contacts a week | at most **3**; replies always come first | the weekly routine gives the operator about 30 minutes for B2B and registration admin and the wife about 60 minutes for B2B correspondence review (`ops/weekly-routine.md`, Reading A) |
| Open first contacts at one time | at most **10** (sent, not yet closed) | each reply costs about 20 to 30 minutes of the two of you |
| Minutes per new first contact | operator about 10 (verify route, fill slots, log), wife about 10 (read the page, read the zh-TW, the notice check) | assumption; replace after the first five |
| Minutes per reply | operator about 10, wife about 15 | assumption |

If replies pile up, stop sending new first contacts until they are answered. If hours slip, B2B outreach and admin is among the first things cut (`strategy/portfolio.md` 5.6 item 2: from 60 to 30 minutes; `ops/weekly-routine.md` section 12), before posting; the never-cut list (AI labels, the wife's review, disclosure, the 24-hour take-down rule) still applies. Do not trade review time for sending.

## 4. Cadence for each contact

| Day | Action | Template |
| :-- | :-- | :-- |
| 0 | Send first contact. Tuesday to Thursday, about 10:00 to 16:00 Taipei time; not on a public holiday or the day before or after | T1 (brand) or T2 (agency, platform, vendor) |
| 7 | If no reply, **one** follow-up in the same thread (or the same form) | T3 |
| 14 | If still no reply: set `closed_no_reply`. **No further contact on any channel for 90 days** | none |
| after 90 days | Contact again **once** only if something materially new exists (for example a brand-approved sample that may be named, or a real audience figure from the platform's own insights), never with the same text | new text, the wife's read |
| any reply | Answer within 2 business days (section 7) | T4, T5, T6 or a custom reply |

**Timing cautions (from `research/culture.md`, computed or recalled, unverified):** retail and e-commerce marketing teams are busiest around 雙11 (Wed 2026-11-11), the autumn 週年慶 and year-end, and again before 農曆新年 (初一 Sat 2027-02-06, 除夕 Fri 2027-02-05; check the official holiday calendar); expect slow answers in those weeks and do not chase. The 2027 ghost month (2027-08-02 to 2027-08-31) is a sensitive period; do not push new deals in it. Election week (polling day recalled as Sat 2026-11-28, unverified): media outlets will be busy, so do not chase them that week; the outreach messages themselves contain nothing political.

## 5. Do-not-contact rules

A row or a person goes on the do-not-contact sheet (and `do_not_contact = Y` in the tracking sheet) for any of these. **The sheet is checked before every send. Removing someone from it needs both of you.**

1. **Declined categories (Ground rule 6 and the persona decline lists).** Health, medical, weight-loss or cosmetic-efficacy products and services; supplements; investment or financial products and any referral or affiliate link for them (brokers, funds, ETFs, cards, loans, loan apps, buy-now-pay-later, insurance, crypto); gambling and lotteries; politics, elections and cross-strait topics; face-swap, voice-cloning and deepfake-capable tools; AI fortune-telling; counterfeit or "dupe" sellers; anything illegal. These appear in the lists as SKIP. The full list, with classes A (always decline) and B (decline unless a documented condition is met), is [decline-list.md](../decline-list.md) section 2; it summarises the per-persona lists in `personas/<slug>/bible.md` 9.2 (fangcun, buzhou, sehuan), and the bibles win if they ever differ.
2. **HOLD rows** (rental platforms) until the lawyer has cleared the category in writing.
3. **Anyone who said no, stop, 不需要, or asked not to be contacted, on any channel, to either of you.** Record it the same day, send T5, never write again. Never ask why.
4. **A recipient whose site says it does not accept unsolicited proposals** (for example 不接受業務開發、廠商推銷或自薦), or whose form says it is for customers only. Obey the notice; mark the row `do_not_contact` with the reason.
5. **Anything other than the recipient's own published business-inquiry route.** No personal email or personal social account of an employee; no guessed address (info@, pr@); no address bought, scraped or harvested by a tool; no address found on a third-party site; no direct message to a brand's or a person's social account; no phone call. (The operator's warm contacts are the exception: they are people he already knows.)
6. **One open thread per entity and per corporate group.** The lists mark sister companies in `group_note` (for example 特力屋 and HOLA; SOGO, 遠東百貨, 遠傳 and friDay; the Dentsu and Hakuhodo groups). Do not write to two units of the same group within 30 days unless the first has answered no or been closed. The same entity can appear in two lists (the `also` column); it still has one thread.
7. **No conflict hidden.** If the operator or the wife has a personal or financial tie to a recipient, say so in the message or do not send.
8. **Government agencies, public-interest bodies, schools and any recipient aimed at minors.** Public-sector work needs separate procurement and registration steps and is out of scope for now.
9. **Anyone who has made a public likeness, deception or AI-image complaint against a studio like ours.** Do not contact without both of you agreeing; never refer to another party's public mistake.
10. **A recipient in the first week of a crisis or incident of the studio's own** (`ops/crisis-playbook.md`): pause all outreach while any 24-hour clock is running.

## 6. Tracking sheet

The working copy is a private CSV kept **outside git** (copy [tracking-template.csv](tracking-template.csv) to `monetisation/outreach/filled/tracking_YYYY-MM.csv`; `filled/` is git-ignored). One row per entity thread. Dates are `YYYY-MM-DD`. `python3 -B monetisation/outreach/check_outreach.py --tracking FILE` validates the header, the allowed values, the one-thread rule and the do-not-contact rule, and prints the funnel counts.

| Column | Meaning |
| :-- | :-- |
| `contact_id` | a running id you choose, for example C001 |
| `list_id` | the row id in the target list (F03, A05, H02) or `warm` for the operator's own contact |
| `entity_name` | the entity's name (the organisation; for a warm contact the brand only) |
| `niche` | fashion, ai-tools or home |
| `entity_type` | brand, agency or platform |
| `priority` | P1, P2, P3, HOLD or SKIP, copied from the list |
| `route` | warm (operator knows them), cold (list only) or introduction (introduced by someone) |
| `group_note` | parent group if the list records one |
| `verified_on` | the date the five-minute check was done |
| `contact_source` | where the business-inquiry route was found (page title and date); **no personal data** |
| `channel` | web_form, business_email, in_person or phone |
| `recipient_role` | a role or team (合作窗口, 行銷部); a named person only if the page publishes them as the business contact |
| `template` | T1 to T6 or custom |
| `sender` | operator or wife |
| `wife_checked_zh` | Y, N or n/a |
| `compliance_checked` | Y or N: category, decline list and the notice check done |
| `first_sent_date` | the day T1 or T2 was sent |
| `follow_up_due` | first_sent_date plus 7 days |
| `follow_up_sent_date` | the day T3 was sent, or empty |
| `status` | one of the values below |
| `reply_date` / `reply_type` | when and what kind (below) |
| `do_not_contact` / `dnc_reason` / `dnc_date` | Y or empty; the reason; the day |
| `sample_offered` / `sample_scope` / `sample_delivered_date` | Y or N; one line; the day |
| `written_quote_received` / `quote_date` | Y or N (a written price from them or an agency, for rate-card calibration); the day |
| `lead_signal_kind` / `lead_signal_logged_on` | the kind logged in `analytics/templates/lead_signals.csv` and the date |
| `persona_tag` | the showroom persona: fashion = sehuan, ai-tools = buzhou, home = fangcun (tagging only; the income is the studio's) |
| `next_action` / `next_action_due` | one line and a date |
| `notes` | free text, **no personal data beyond a business role**, no pasted private messages |

**Status values:** `not_started`, `verified`, `ready_to_send`, `sent`, `follow_up_sent`, `replied`, `in_conversation`, `sample_scoped`, `sample_delivered`, `quote_pending`, `closed_no_reply`, `closed_declined_by_them`, `closed_declined_by_us`, `do_not_contact`, `on_hold`.

**Reply types:** `interested`, `more_info`, `not_now`, `no_thanks`, `opt_out`, `noncompliant_brief`, `bounce`, `auto_reply`, `rate_sheet`, `other`, `none`.

**Logging in analytics.** Every send adds one `outreach_sent` row to `analytics/templates/lead_signals.csv` (`ref,signal_date,persona,kind,notes`) tagged with the showroom persona; an enquiry adds `written_enquiry`; an accepted free sample adds `accepted_free_sample`; a written price tied to a real brief, in either direction, adds `written_quote`; an agency's reply about budgets or rate sheets adds `agency_budget_reply`. **`outreach_sent` is counted but is not a positive signal**, and the analytics watch list flags a persona with many outreach messages and no signal (`analytics/metrics.py`), so log sends honestly. (The analytics owner should confirm that `written_quote` covers both directions; open item 4.)

## 7. What to do when someone replies

| They say | You do |
| :-- | :-- |
| Interested, wants to know more | T4 within 2 business days, wife reads first. Log `written_enquiry`. Do not give a price. Check their category against the decline list |
| Asks for a price or rate card | "We quote after scoping a real brief." Do not quote from `rate-card.md`: it is an internal proposal not yet checked against any real quote, and the registration gate is open. If pressed, ask for the brief and the usage they have in mind |
| Asks for followers, reach, engagement or past clients | Say plainly there are none yet; creative only; offer the private sample (if the operator chose) or the media-kit paragraph in mode 1 (`monetisation/media-kits/README.md`: "no data yet" text). Never round up, estimate or imply |
| Asks to see past work | There is none to show. Offer the private sample, or a short written description of the process. Do not show an image that is not cleared and labelled |
| Asks for a first-hand review, unboxing, "I tried it", or wants the character to say it wore or liked the product | Decline (T6). The character has not used anything (Ground rule 4) |
| Asks to remove, hide or shrink the AI label or the 業配 label, or to post without the platform tool | Decline (T6). Non-negotiable (Ground rules 1 and 5) |
| Brief is in a declined category (health, finance, gambling, politics, supplements and others) | Decline (T6); add to do-not-contact if they push |
| Asks for exclusivity, a perpetual buy-out, model training on assets, or unlimited usage | Do not agree by message. These are red flags in the bibles (9.3). Say terms are set in a written contract; send to the contract checklist; lawyer Q24 |
| Asks "are you a real person?" or "how many people are you?" | Answer honestly: two people run a very small studio, and the characters are AI-generated. Do not claim a team (the studio kit leaves team size for you two to decide) |
| Wants a call | Propose a window; the wife leads in Mandarin; write a note of what was said the same day; no verbal commitments |
| Sends a rate sheet or budget information (agency) | Thank them; store it in the private quotes folder; log `agency_budget_reply` (and `written_quote` if it is a written price for a real brief); use for rate-card calibration (gaps G1, G11); it does not oblige you to work with them |
| "Not now" | Log `not_now`, close the thread, 90-day rest; do not chase |
| "No", "stop", 不需要 | T5 the same day; do-not-contact; never write again |
| Email bounces | Do not try another address; look up the official route again (it may be a form); if there is none, close it |
| An auto-reply | Wait for a human; do not resend |
| A legal threat, a complaint about likeness or deception, or an angry reply | Pause all outreach; follow `ops/crisis-playbook.md` (scenarios 7.2, 7.3, 7.8); lawyer the same day; no admissions |
| A link, attachment or request for payment, bank details or personal data | Do not click or pay; treat as suspicious; ask the lawyer or 記帳士 if unsure |

## 8. Consent and anti-spam note, and the lawyer question

**What this is, and what I do not know.** Everything below is **unverified, lawyer question**. No primary legal source was opened in this project (Phase 1). What `research/legal.md` recalls (section 9, U21): the Personal Data Protection Act (個人資料保護法) has a **marketing opt-out** (Art. 20, recalled) and notice duties (Art. 8, recalled); **no general anti-spam statute is recalled**, so marketing messages seem to rely on the PDPA plus platform terms. Whether a first-contact message to a company's published business-inquiry address needs prior consent, a particular sender identification, a physical address, or a particular opt-out method is **not known**. A name and role at a company can be personal data. Whether Taiwan has other rules for commercial email, SMS, LINE or telephone solicitation is not known to this project.

**Practices adopted regardless of what the law turns out to require** (they are cheap and honest):

1. One-to-one, personalised, reviewed and sent by a person; no mail-merge tool, no sequence software, no auto-reply, no scraping, no purchased list, no tracking pixel, no link shortener, no attachment in a first message.
2. Only the recipient's own **published business-inquiry route**; never a personal address; never a guessed address.
3. The sender and the studio are identified truthfully; the subject says what the message is; the message says how the address was found.
4. A **one-step, free opt-out in the first message** (reply 「不需要」), honoured at once, recorded on the do-not-contact sheet, confirmed by T5.
5. A fixed, small cadence: one first contact, one follow-up, then silence for 90 days (section 4).
6. Obey any "no solicitation" notice (section 5, item 4).
7. Minimal personal data (section 9).
8. No claim that is not true (no client, result or audience figure); no pressure.

**Questions for the Taiwanese lawyer (new; to be added to `research/legal.md` section 12 and `HUMAN_TODO.md`; numbered O1 to O7 here so they cannot be confused with the existing Q1 to Q25).**

| # | Question | Gate |
| :-- | :-- | :-- |
| O1 | Is a first-contact B2B email, or a web-form submission, to a company's published business-inquiry route lawful in Taiwan without prior consent? Beyond the PDPA marketing opt-out (recalled Art. 20), is there any statute or regulation on unsolicited commercial email, SMS, LINE messages or calls to businesses, and who can be fined? | [Gate: outreach] |
| O2 | What must a first marketing email contain to be safe (sender identity, registered name or address, the source of the address, an opt-out)? Is the sentence 「若不希望再收到來信，請回覆『不需要』」 an adequate opt-out method, and at whose cost must it be offered? | [Gate: outreach] |
| O3 | Are a business role mailbox and a named business contact "personal data" under the PDPA? May the studio keep a tracking sheet with roles, dates and replies, for how long, and must the recipient be told? What may a do-not-contact list keep? | [Gate: outreach] |
| O4 | Is using an address that a company publishes for business inquiries for a marketing message within the PDPA's purpose limits (Art. 19 and 20, recalled)? | [Gate: outreach] |
| O5 | Before registration, may the operator or the wife send first-contact messages in their own names, and which name must appear? What identification do commercial messages require once registered (商號 or company name, tax ID)? | [Gate: outreach] |
| O6 | Does offering a free private sample to a company's staff create any gift, benefit or tax consequence for either side? Does a free sample later shown publicly count as an advertisement (already `HUMAN_TODO.md` 27, 37)? | [Gate: paid] |
| O7 | Rental platforms: what wording about leases, guarantees, deposits or tenant rights would make a rental platform's sponsorship of a general move-in checklist a problem, and can the studio take such work at all? (Backs the HOLD rows in the home list; bible 9.2.) | [Later] |

## 9. Data handling

1. **The tracking sheet and the do-not-contact sheet hold only business roles, organisation names, dates and a one-line note.** No personal phone numbers, no personal addresses, no private message text, no health, family or financial details.
2. **Working copies live outside git** (`monetisation/outreach/filled/`, git-ignored). The repository holds only templates and lists.
3. **Retention (assumption, lawyer question O3):** delete a closed thread's role and notes 12 months after closing; keep only organisation name, date and reason on the do-not-contact sheet, indefinitely, because it must be honoured.
4. **When pasting a reply into a Claude session,** remove personal details first (names, numbers, signatures) and keep the substance.
5. **Samples and client material:** a brand's photographs and specifications are used only for the agreed sample, under the written licence, and are deleted when the thread closes unless the contract says otherwise.

## 10. How the counts will be read

The checkpoint counts are read from the tracking sheet by `check_outreach.py --tracking FILE`: contacts approached (`first_sent_date` filled, or a recorded warm conversation), replies, interested replies, samples scoped and delivered, written quotes received, do-not-contact. They are counts of what happened, not targets for the recipients. If the real numbers are small, say so in the week-8 review; do not widen the list with weak rows to raise the count.

## 11. Open items

1. **Add the outreach questions O1 to O7 to the lawyer list** (`research/legal.md` section 12 and `HUMAN_TODO.md`), with [Gate: outreach] on O1 to O5. Shared files, not edited here.
2. **Operator:** write the five warm fashion contacts into the warm-contact table of the fashion list (real names only), and say which would take a free private sample.
3. **Wife and operator:** do the five-minute verification of each P1 row before it is used; add small independent labels, studios and SaaS start-ups you know of (the lists cannot name them with confidence).
4. **Analytics owner:** confirm whether `written_quote` covers a quote the studio gives and a price the studio receives, or only one of them.
5. **Both:** decide who is named in the signature and which address the studio shows; set the response time you can actually keep (studio kit section 10).
6. **Operator:** decide, per recipient, whether to offer the free private sample (and, for fashion, keep it face-free until the lawyer answers the try-on questions, `HUMAN_TODO.md` 27 and 37).
7. **Sibling files (another Phase 8 stream, now present):** [studio-offer.md](../studio-offer.md) may be attached to a T4 reply only as a filled working copy after its own Part A gates close and the wife has read it; [sponsorship-contract-checklist.md](../sponsorship-contract-checklist.md) is where exclusivity, usage and liability questions from a reply go; [decline-list.md](../decline-list.md) has fuller decline wording than T6 (its template numbers are its own, not T1 to T6 of this folder).
