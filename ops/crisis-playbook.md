# Crisis playbook (Phase 9), DRAFT v0.1

Written 2026-10-12. For the operator (English) and the wife (the zh-TW statements, which are AI drafts for her to adapt). Companion to [risk-register.md](risk-register.md) (what can go wrong, and the early signals) and [weekly-routine.md](weekly-routine.md) (how the week is run, including the daily notice check that makes the 24-hour clocks possible).

**Nothing here has been used.** No account exists, no incident has happened, no lawyer is booked, and no platform appeal form has been seen. Every platform step is *recalled* or *unverified* ([platforms.md](../research/platforms.md) could not open a primary page); the live screen overrules this file. Every Taiwan-law statement is *unverified* and none of this is legal advice ([legal.md](../research/legal.md)). The take-down clocks come from [portfolio.md 6.2](../strategy/portfolio.md) and the pilot bibles and addenda; this file does not change them. Minutes are *assumptions*.

How to use it: read sections 0 to 6 once, now, together. In an incident, start at section 0, then go to your scenario in section 7. Fill the checklist in section 6 before the first post.

## 0. Quick start: if something is wrong right now

1. **Is a person at risk, or is it a letter or message from a lawyer, a court, the police or a government agency?** Then also follow section 5: contact the lawyer the same day. Do not reply to the sender on the spot.
2. **Pause.** Unschedule everything for the affected persona (everything for all three if you are unsure). Either of you may do this alone, without asking. Target: ten minutes ([schedule.md](../launch/schedule.md) section 6).
3. **Capture.** Screenshot what you see (post, notice, comment, email) with the date and time visible, into the private evidence folder (section 4). Sixty seconds, before anything is changed.
4. **Tell the other person now**, by phone if you can, not by a message you hope they read.
5. **If a post is the problem and a clock in section 2 says 24 hours, take it down now** (archive or hide it; delete only if the platform gives no other way).
6. **Open your scenario in section 7** and follow the first hour.
7. **Do not:** reply in public; argue; delete comments (except harassment, politics and personal data); open a new account; pay anyone to recover or fix anything; edit a face or picture to make a problem go away; admit fault, apologise or promise money before you have spoken to the lawyer.

| What happened | Scenario |
|---|---|
| A strike, warning, limit, removal, disabled account, or a notice about the AI label | 7.1 |
| Someone says a face looks like them or like a named real person | 7.2 |
| Someone says the studio is deceiving people (pretending to be real, hiding AI, fake reviews, a scam) | 7.3 |
| Many critical comments at once, or a post spreading for the wrong reasons | 7.4 |
| A number, step, date, definition or Chinese character in a published post is wrong | 7.5 |
| A published post (or a reply) contains health, finance, gambling, politics or an "I tried it" claim | 7.6 |
| Typhoon, earthquake, disaster, public tragedy or national mourning | 7.7 |
| A brand, sponsor, client or tool vendor is unhappy, or a brief asks for something not allowed | 7.8 |
| Unrecognised login, posts you did not write, locked out, lost phone | 7.9 |
| A fake account, stolen images, the face in a scam ad | 7.10 |
| A missing label, a visible defect, 「是真人嗎」 comments, a leaked notification in a recording | section 8 |

## 1. Rules that apply to every incident

1. **Pause first, understand second.** A pause costs a day of posts; a wrong post costs an account. Either of you may pause or take down; both must agree to resume.
2. **Removing needs one key. Adding needs two.** Taking something down needs nobody's permission. Anything new (a correction, a statement, a replacement post) goes through the same approval gate as every post: the wife approves the zh-TW wording, the operator approves facts, labels and flags, and a human sets `approved: true` ([schedule.md](../launch/schedule.md) section 2). A ten-minute expedited review is allowed; skipping it is not. Claude never sets a review field.
3. **The studio speaks, not the character.** A statement says 「工作室」 (the studio) and is about what the studio did. The character has no experience to report and nothing to apologise for ([portfolio.md 1.3, 3.3](../strategy/portfolio.md)). A statement published as a post on a persona account still begins with the AI line and carries the badge and the platform label; a pinned comment or a reply does not need to.
4. **Capture before you change, but never delay a take-down by more than a few minutes to do it.**
5. **No replacement accounts, ever.** No new account, no second handle, no "backup" persona, no paid recovery service, no workaround of a platform limit ([portfolio.md 6.2](../strategy/portfolio.md); [00-studio-setup.md](../launch/00-studio-setup.md) section 13).
6. **No argument in public.** Honest criticism is never deleted. Harassment, politics and personal data are hidden. Nobody replies to politics, and nothing is automated.
7. **No admissions, apologies, refunds, compensation or promises before the lawyer** where a person or company is claiming harm or rights (section 5). Whether an apology counts against the studio under Taiwan law is *unverified*. A plain correction of a fact is not an apology and is always allowed.
8. **Log the same day.** A standing event in the tracker (the `standing` import, [analytics README](../analytics/README.md) section 5), an incident note (section 10), and for label or setting checks a row in `launch/evidence-log.csv`. For every 6.2 event the root cause is written within 24 hours.
9. **No cross-help between personas.** An incident on one persona is never answered by another persona, and no persona is told to "support" another (Ground rule 8).
10. **Claude's part.** Claude drafts statements and incident notes for the wife's review, runs `queue.py validate` over the queue to find similar wording, re-dates the schedule with `schedule_check.py`, and keeps the register current. Claude never logs in, posts, contacts a platform, a brand or a person, approves anything, or sees a credential. Claude has no memory between sessions: paste the incident note into a new session.

## 2. The clock table

The clock starts when **either of you first sees the problem**, not when the post went live (*assumption*: 6.2 does not say; this is the only workable reading, and it is why the weekly routine has a daily notice check). Everything below is [portfolio.md 6.2](../strategy/portfolio.md) unless a source is named; it governs if this table is ever out of step.

| Event | Clock | Then | Scenario |
|---|---|---|---|
| Any platform strike, restriction, label dispute or AI-label violation | Pause that persona on that platform **immediately** | Root-cause note; no replacement accounts; **not cleared in 14 days: stop that persona on that platform** | 7.1 |
| A Ground rule 6 contact in a published post (health, finance, politics, gambling, testimony) | **Take down within 24 hours** | Pause the persona **7 days**; write the root cause; a **second event within 8 weeks retires** the persona or the pillar | 7.6 |
| Likeness complaint or credible look-alike claim (including a viewer naming a real person) | **Take down within 24 hours** | Pause until a **documented look-alike check**; an upheld complaint retires that face (addenda 8.3, 9.3) | 7.2 |
| Disclosure failure, or a missing sponsorship or gifted-goods disclosure | **Fix within 24 hours**; log | A repeat in the same quarter pauses the persona | section 8 |
| 5 or more 「是真人嗎」 comments in any week; the pilot addenda and reply guidelines also count 3 or more in the first two weeks | **Strengthen the first caption line and the on-screen badge within 48 hours** | Reconsider photoreal at the review if it happens twice in six weeks (H1, [portfolio.md 4.2](../strategy/portfolio.md)) | 7.3, section 8 |
| 3 or more of any 20 drafts caught with testimony, health, finance or income wording | Stop and **redesign the pillars** before continuing | | section 8 |
| Garbled or Simplified Chinese, or a wrong factual claim, reaches publication | **Correct within 24 hours** | **Two in six weeks pause the persona** until the QA step is fixed | 7.5 |
| A visible face, hand or earring defect reaches publication (photoreal addenda 8.3) | **Correct or take down within 24 hours** | Two in six weeks pause the persona until QA is fixed | 7.5, section 8 |
| An image shows a hand holding something, a location, a product, a mirror, or looks like a candid photo (addenda 8.3) | Treated as a Ground rule 1 or 4 contact: **take down within 24 hours** | Pause the persona 7 days | 7.6 |
| 步驟 only: a recording leaks personal data, a key, a notification or a private tab; or the persona asks viewers for personal data | **Take down within 24 hours**; rotate any key; log | A repeat in the same quarter pauses the persona ([步驟 bible 7.3](../personas/buzhou/bible.md)) | section 8 |
| 步驟 only: a vendor complaint, takedown or terms objection | **Pause that video**, read the vendor's terms | Answer through the operator, in writing ([步驟 bible 7.3](../personas/buzhou/bible.md)) | 7.8 |
| The model label changes between two generations of the same image set | **Stop** | Treat as a new design: re-run the age, look-alike and near-pair tests (addenda 8.3) | section 8 |
| Typhoon, disaster or public tragedy | **Unschedule today and tomorrow** before the first slot | Both agree to resume ([schedule.md](../launch/schedule.md) section 6) | 7.7 |

**Section numbers in the pilot addenda.** This file cites the 方寸 and 色環 addenda numbering (tripwires 8.3, look-alike procedure 9.3, three-pilot test 10). The 步驟 addendum is shifted by one: tripwires 7.2, look-alike procedure 8.3, near-pair note 9. The 步驟 tripwire list is marked "proposed" there and does not add a "hand holding something" row; the 方寸 and 色環 rows are applied to 步驟 by analogy.

## 3. Who decides

| Decision | Who | Notes |
|---|---|---|
| Pause a persona, a platform or everything | **Either of you, alone, at once** | Stop-the-line authority. Resuming needs both |
| Take a post or comment down (archive, hide) | **Either of you, alone, at once** | One key to remove |
| Publish anything new: a statement, correction, replacement post | **Both**: wife on the zh-TW wording and tone, operator on facts, labels and flags | Two keys to add. Expedited review is allowed |
| Resume after a pause | **Both**, after a written root cause | The 7-day pause, the 14-day platform clock and the look-alike check are minimums, not the end |
| Retire a persona, a pillar or a face | **Both**; the operator records it in [DECISIONS.md](../DECISIONS.md) | Only on the 6.2 triggers or a deliberate decision |
| A platform appeal or report | **Operator** (account holder) submits; **wife** reads and approves any Chinese text | The platform's own form only |
| A letter or call from a regulator, the police, a court, a lawyer or a tax office | **Whoever receives it** tells the other at once; the **wife signs as registrant** once registered; both with the lawyer | Do not reply substantively before the lawyer call |
| Any apology, admission, refund, compensation, settlement or promise | **Both, after the lawyer** | |
| A journalist or consumer-group enquiry | **Nobody answers on the spot**; the only reply is "the studio will respond" | Wording is agreed with the lawyer if it concerns deception, likeness or a law |
| Statement wording | **Wife** decides the Chinese and the tone; **operator** decides facts | If you disagree on wording, say nothing publicly until the next day |
| A disagreement about safety (pause or not, take down or not) | **The more cautious action wins** | Reverse it later, together |
| Money, a contract position, an invoice | **Wife** (registrant, to be confirmed) with the 記帳士 or lawyer; **operator** supplies the facts | |

## 4. Evidence to preserve

**Where.** A private shared folder **outside the repository** that both of you can open. One subfolder per incident, `E-YYYYMMDD-NN`, mirrored by an incident note in the repo that holds no personal data (section 10). Settings screenshots show your personal email or phone, and complainants' details are personal data, so none of this goes into git ([00-studio-setup.md](../launch/00-studio-setup.md) section 2; PDPA exposure *unverified*, [legal.md](../research/legal.md) section 9).

**Capture first, in this order, then act:**

1. The thing itself: the post or comment with the URL, post id, date and time (Taiwan time), the caption in full, the on-image badge, the platform's AI label, and the comments visible at that moment.
2. The notice, email or message in full (export an email as a file with its headers; screenshot a notice and copy its text, including any ticket number).
3. The account state: the account-status page, the label setting, the insights snapshot.
4. Your own records for that post: the folder in `pipeline/review-queue/<persona>/<date>_<NN>/` (`post.json` with its review fields and notes), the final media files, the rows in `assets/provenance.csv`, the row in `launch/schedule-log.csv` (the live check), and the dated screenshots in `launch/evidence-log.csv` that show the label was on.
5. For a likeness claim: the prompt history in the generation app and the look-alike log (addendum 9.3), never a photo of the person making the claim beside the character.

**Rules.** Never edit an original; work on copies. Do not delete a post to "start clean"; archive or hide it, because the platform's record and your capture are the evidence (platform archive options *unverified*). Optional but cheap: write a hash list of the folder (`sha256sum *` on Linux, `shasum -a 256 *` on a Mac) and save it next to the files, so you can show they were not changed. Note the Taiwan time of every action in the incident note. Keep every incident folder until the lawyer says otherwise; the retention period is a lawyer question (*unverified*). Do not try to identify, find or contact anyone you meet in search results or in a comment thread.

## 5. When to call the lawyer

No lawyer is booked yet ([HUMAN_TODO.md](../HUMAN_TODO.md) 9). When one is, ask for an after-hours contact and a fee for an urgent letter; the cost is outside the monthly cap and its amount is unconfirmed ([DECISIONS.md](../DECISIONS.md) STOP 2 item 6). **A 24-hour take-down never waits for the lawyer.**

**Call or email the same day (hard triggers):**

1. Any letter, email, call or message from a lawyer, court, police officer or government agency (the Fair Trade Commission, the NCC, the Ministry of Digital Affairs (數位發展部) or its Digital Industry Administration (數位產業署), a health bureau, the tax office).
2. A named real person says the character uses their face, name or voice, or a lawyer writes for them; any demand for money or for removal beyond the cited post.
3. A brand or vendor threatens legal action, or alleges false advertising, trademark or copyright infringement, or defamation, or claims money.
4. A platform notice that cites a Taiwan law or says it acts on a government order, rather than citing its own policy.
5. A leak of other people's personal data (a viewer's details, a recording).
6. Someone says they were harmed by following a post (a lease, an electrical or load question, a tool misuse).
7. A journalist or consumer group asks about the studio.
8. A second Ground rule 6 contact within 8 weeks, or a regulated claim that ran with sponsor or affiliate money.
9. Before any apology, compensation, settlement or signed undertaking.
10. A dispute over who owns the character or the images with a freelancer, client or between the two of you (see risk PPL-4).

**Collect for the next consult (soft triggers):** platform policy ambiguity; label wording; a new brief category; whether a free sample is an advertisement; anything in [legal.md](../research/legal.md) section 12 that an incident made urgent.

**Before you call, prepare one page** (template in section 10): what happened and when; what you have done and when; the evidence list; the question; any deadline. Ask the lawyer how to send the evidence securely before attaching it.

## 6. Before the first post: what must exist

None of this is ticked. It restates [risk-register.md](risk-register.md) section 4 as a checklist for this playbook.

- [ ] A lawyer booked, with an after-hours contact and a fee for urgent letters.
- [ ] The private evidence folder exists and both of you have opened it.
- [ ] The studio mailbox, vault and two-factor exist (launch L2); someone reads the mailbox daily.
- [ ] The wife has read and adapted every statement in section 9.
- [ ] The pause drill has been timed once on the real accounts (target ten minutes), and the real lists to unschedule from have been screenshotted.
- [ ] Appeal and report forms for impersonation, a label dispute and a restriction have been found in each app and screenshotted (the dry runs, `launch/schedule.md` section 4).
- [ ] The studio link page is live and lists the accounts (it is the answer to impersonation), with a contact line that works.
- [ ] The look-alike panel is lined up (HUMAN_TODO 36), with an agreement not to share pictures.
- [ ] The ownership memo is written (risk PPL-4).
- [ ] The incident note and lawyer one-pager templates (section 10) have been copied somewhere you can reach them in a hurry.
- [ ] You each know the daily notice check owner this week (weekly-routine section 8).

## 7. Scenarios

Each scenario gives the people who decide, then the first hour, the first day and the first week, the evidence to keep, when to call the lawyer, and what not to do. The statement numbers (ST1 to ST11) are in section 9.

### 7.1 Scenario 1: platform strike, restriction, label dispute or AI-label violation

Covers: a strike or warning; content removed; reduced distribution; a demand to apply or confirm the Instagram "AI-generated profile" label; an account disabled; a YouTube channel strike or an automatic label; a branded-content violation; a scheduler or API lock. Risks: ACC-1, ACC-2, PHO-2, PHO-5. Clock: pause at once; 14 days to clear.

**Decider:** the operator (account holder); the wife reads a Chinese notice. Pausing needs nobody's permission.

**First hour**

1. Unschedule everything for that persona **on that platform**. Stop posting, replying and editing on the account. If it is an Instagram login, look at the same persona's Threads and at any other account on the same phone for notices.
2. Screenshot the notice and the account-status or cited-content page (section 4). Copy the notice text word for word into the incident note; the wife reads the Chinese.
3. Read what it asks. If it names a missing label, switch the label on (that is compliance, not evasion) and screenshot before and after. Change nothing else. Do not delete the cited post.
4. Tell the other person. Log a standing event with gate `strike_restriction` and start the 14-day count (date plus 14).

**First day**

1. Write the root-cause note: which post or setting; was the label on (check `launch/schedule-log.csv` and the account-creation row in `launch/evidence-log.csv`); anything changed recently (bio, avatar, scheduler, tool).
2. Sweep that persona's posts from the last two weeks on that platform for the same defect: the four disclosure places, and `python3 pipeline/scripts/queue.py validate` over their folders.
3. Appeal through the platform's own form only, short and factual: an openly AI character; the studio named; the labels on; the item cited; a request to review. The wife approves any Chinese text; the operator submits. Record the ticket number and the time.
4. Decide scope. By default only that platform is paused. If the cause is common to both (the photoreal label, a shared login) pause the persona's other platform until you have checked.

**First week**

1. Follow up the appeal at day 3 and day 7, through the same channel. No duplicate appeals.
2. **Day 14 not cleared: stop that persona on that platform** (6.2). Keep the account; do not create another. Mark those weeks in the tracker so the week-6 window is extended, not scored.
3. If a policy change caused it, correct the checklist with the real wording and date and add the page to the monthly policy watch.
4. Review at the standup; re-score ACC-1, ACC-2, PHO-2 or PHO-5.

| Variant | First move |
|---|---|
| Instagram "AI-generated profile" label demanded, or a recommendation-limit notice | Apply or confirm the label; if it was already on, appeal; log in `launch/evidence-log.csv`; read that account's week-6 numbers with the caveat (risk PHO-2) |
| YouTube applies or locks an AI label itself | Do not dispute it (labels on content with strong AI markers can be locked, [platforms.md 4.3](../research/platforms.md)); confirm your own disclosure was on |
| Removed as a fake or inauthentic account | Appeal: openly AI, studio named, never a personal Facebook profile. Do not open a Page or a second account to get around it |
| YouTube "inauthentic content" or Instagram "unoriginal content" flag | No monetisation is applied for in year 1 (NT$0). Check that each script is original; record in the QA notes |
| A paid-partnership violation | No sponsored post is possible in the first 30 days; later, fix inside 24 hours (disclosure failure, section 8) |
| A scheduler or API lock | Publish by hand in the app; no third-party tool (Ground rule 9) |

**Evidence:** the notice (text and screenshot), the cited item, its `post.json` and final media, the provenance rows, the label-setting screenshot and live-check row, the appeal text and ticket numbers, the times.

**Lawyer:** only if the notice cites a Taiwan law or a government order, or, after registration, if an account that earns money is disabled. Otherwise no.

**Do not:** post "we were banned"; blame the platform or a rival; change the handle or bio in a hurry; hire a recovery service; appeal in anger.

**Statement:** ST1, only if followers are asking. Default is silence.

### 7.2 Scenario 2: likeness complaint or credible look-alike claim

Covers: a person says the face looks like them; a viewer names a real person (an actress, presenter, influencer, a politician) or an existing virtual character; a lawyer writes; a blind-test answer or a search hit names someone. Risks: PHO-4, PHO-3. Clock: take down within 24 hours; pause until a documented look-alike check; an upheld claim retires the face ([portfolio.md 6.2](../strategy/portfolio.md); addenda 8.3 and 9.3). A resemblance to a politician is also a Ground rule 6 problem.

**Decider:** both. The operator runs the evidence and the procedure; the wife does the local-public-figure check and any Chinese contact. The lawyer is called the same day for an identified claimant (section 5).

**Two tiers (a reading of 6.2, which says "take down" without saying which posts; decision OPS-D4):**

* **Tier A: an identified real person, or a lawyer, claims it.** Archive **every** image of that face on that persona, replace the avatar with a plain neutral tile, and pause the persona until the check is done.
* **Tier B: a viewer's comment names a person, with no contact from that person.** Archive the cited post within 24 hours, pause the persona, run the check, and leave the rest up unless the check finds a resemblance.

**First hour**

1. Do not reply in public. Do not deny, argue, ask "who?" or defend the character.
2. Capture the claim (screenshot, URL, time) and the claimant's public profile header only. Do not dig through their account.
3. Take down per tier now (there is no reason to wait for the 24th hour). Unschedule everything for the persona.
4. **Do not place any photo of the named or claiming person beside the character, download their photos, or run a face-matching or people-search service.** The wife looks at the character image alone and says whether it reminds her of anyone local, including the person named, from memory (addendum 9.3 item 3).
5. Tell the other person. Log a standing event with gate `likeness_complaint`.

**First day**

1. Pull the provenance: every `assets/provenance.csv` row for that face (tool, model, date, prompt), and screenshot the prompt history in the generation app. Confirm that no reference photo was ever uploaded and that no prompt names or describes a real person (`gen_image.py` refuses non-persona references; the apps rely on your records).
2. Re-run the look-alike procedure on R01, the avatar and the cited image (addendum 9.3): three public reverse-image tools by hand, logged out, no face-recognition services; text searches; the wife's check; the blind panel (this may take days; the persona stays paused). Log every result in the addendum's table.
3. Reply privately to a claimant who contacted you with ST2a, after the lawyer has read it if they are identified or have a lawyer. A casual commenter gets no reply, or ST2b only if the claim is already public.
4. Lawyer: same day for Tier A.

**First week**

1. Finish the documented check. **Not upheld** (the three tools, the wife and the panel find no resemblance, and the claimant's specific points were considered): resume, with both of you agreeing and the log written. **Upheld or doubtful:** retire the face (6.2). A new face is a new design with every test re-run; it is never an edit of the old one (addendum 9.3 item 6). Whether the persona continues under a new face or stops, and what existing followers are told, is a decision for both of you with the lawyer.
2. A claimant who asks for money, an apology or removal beyond the posts: the lawyer only.
3. Re-score PHO-4. Record what the process missed (which tool, which crop, which test) and add it to the procedure.

**Evidence:** the claim and the claimant's header; the prompt history; provenance rows; the look-alike log with dates, tools, crops and results; the wife's notes (names stay in the private log, never in a prompt); the blind-test sheets; the model labels and generation dates; the approval record of the images.

**Lawyer:** same day for Tier A, and before any apology wording.

**Do not:** edit the face to look less similar and keep publishing; say "it is not based on anyone" before the log supports it; contact anyone you found by search; share the claimant's details with Claude (describe the case without names).

**Statements:** ST2a (private), ST2b (public holding line).

### 7.3 Scenario 3: accusation of deception

Covers: "this is a fake person"; "you are hiding that it is AI"; fake reviews or fake customers; a scam association; "a network of fake accounts"; a journalist or consumer group. Risks: PHO-1, PHO-6, ACC-4. Clock: a missing label is fixed inside 24 hours; 5 or more 「是真人嗎」 in a week means strengthening the label inside 48 hours.

**Decider:** both. The operator checks the live post; the wife drafts the Chinese. A journalist or regulator enquiry goes to the lawyer (section 5).

**First hour**

1. On the live post, check the four places (bio, first caption line, on-image badge, platform label) and screenshot each with the date (the live check in [schedule.md](../launch/schedule.md) section 9).
2. If any place is missing or hidden behind "more", fix it now. That is a disclosure failure (6.2): log it, and use ST3b.
3. If all four are there, reply once with ST3a (a reply or a pinned comment). Tally every 「是真人嗎」 comment into the daily count.
4. Do not delete the accusing comments unless they are abusive or hold personal data.

**First day**

1. Sweep the last ten posts on that account for the four places and the badge crop test.
2. Check that no post contains an experience claim (a "fake review" accusation is usually a Ground rule 4 question): run `queue.py validate` over the persona's published folders.
3. If the accusation spreads, treat it as Scenario 4 as well.
4. A journalist, consumer group or regulator: do not answer; the lawyer first.

**First week**

1. If the tally reached the trigger, strengthen the first caption line and badge within 48 hours (a larger badge, the avatar chip, a pinned line that the images are AI-generated). Record the change and ask the wife whether the wording now reads as heavy or 工商味.
2. Post-mortem: why did a viewer not see the label? Record the answer for the register (PHO-1).
3. Twice in six weeks: the user reconsiders photoreal at the review (H1; decision OPS-D5).

**Evidence:** the live screenshots of the four places with times; the `launch/schedule-log.csv` live-check row for that post; the account-creation rows in `launch/evidence-log.csv`; `post.json`; the comment thread; the tally.

**Lawyer:** a journalist, a consumer group, a regulator, or an accusation of fraud with a named complainant.

**Do not:** argue that AI characters are good; claim the accuser is wrong without checking the live post first; hide or crop the label to look cleaner afterwards.

**Statements:** ST3a (labels present), ST3b (a label was missing), ST11 (a holding reply).

### 7.4 Scenario 4: viral negative comment wave

Covers: an anti-AI pile-on; an error pile-on; brigading or harassment; political drift; scam bots; a post shared for the wrong reasons. Risks: CON-1, CON-4, PHO-1. No 6.2 clock unless the wave contains a real incident (a label gap, an error, a Ground rule 6 contact): then run that scenario too.

**Trigger (*assumption*, to calibrate):** more than 20 critical comments on one post inside 24 hours, or a post quoted by an account you do not recognise with mostly hostile replies. At pilot size a wave will be small; the same steps apply.

**Decider:** the operator triages; the wife reads the tone. Either may hide comments or restrict who can comment.

**First hour**

1. Screenshot the thread and the top comments (handles stay in the private folder, never in the repo).
2. **Triage in five minutes:** is there a real error, a missing label or a Rule 6 problem in the post? If yes, switch to that scenario (7.5, 7.3 or 7.6). The most useful thing in a wave is usually to fix what is true in it.
3. Unschedule the persona's next 24 hours of posts, so nothing publishes into the storm.
4. Hide harassment, political comments and personal data; report and restrict repeat offenders. Do not delete honest criticism. If the platform offers limits on who may comment, use them rather than turning comments off; control names are *unverified*.
5. Do not reply one by one. Pin ST4 if the wave is about AI or disclosure.

**First day**

1. The wife reads all the comments for tone and meaning; the operator reads for facts and for personal data. Sort into: valid criticism, a question you can answer plainly (replies from [reply-guidelines.md](../content/fangcun/reply-guidelines.md)), abuse, politics, spam.
2. Correct anything true and wrong (Scenario 5). Answer genuine questions once, with the existing reply lines.
3. Resume with the next approved post, a calm one, after 24 hours. No "response" post, no video about the wave, no jokes about it.

**First week**

1. Watch the daily numbers, the count of 「是真人嗎」, and unfollows.
2. Log it in the weekly report. If the wave is about the photoreal look ("creepy", "fake"), record it as evidence for H1 and the photoreal decision; do not change the face in the middle of a wave.
3. Re-score CON-1.

**Evidence:** screenshots of the thread over time, comment counts, the insights snapshot, what was hidden and why (category only).

**Lawyer:** threats, doxxing, or a named person being defamed in the thread.

**Do not:** buy or arrange supportive engagement (Ground rule 7); ask friends or relatives to defend the account; delete criticism; reply to politics; let any persona respond for another.

**Statements:** ST4, ST11.

### 7.5 Scenario 5: a factual error reached publication

Covers: a wrong number, step, date, definition, price, timetable or colour fact; garbled or Simplified Chinese; a stale tool step in a 步驟 video; a wrong reply to a commenter. Risks: CON-2, PHO-7. Clock: correct within 24 hours; two in six weeks pause the persona until the QA step is fixed.

**Decider:** the operator decides whether it is wrong; the wife approves the wording of the correction. A safety error is not held for the wife: either of you takes the post down at once.

**Severity (*assumption*):**

* **A, harmful:** a safety, lease, electrical, load, money or health statement, or anything that could hurt someone who acts on it. Take the post down at once, do not wait 24 hours.
* **B, material:** a wrong number, step or date that changes what a viewer would do. Correct within 24 hours.
* **C, cosmetic:** a typo, one wrong character, a date format. Fix at the next convenient moment; add a note only if the meaning changed. A garbled or Simplified character is still B (6.2).

**First hour**

1. Open the source again yourself and compare with the source slip and `post.json` `sources`. Classify: our error; the source changed since (the 「資料日期」 on the post protects you); the commenter is wrong.
2. If A: archive the post now. If B: prepare the correction.
3. Tell the other person. Log a standing event with gate `garbled_or_wrong` once confirmed.

**First day**

1. Correct. An Instagram carousel cannot be re-edited slide by slide: edit the caption and add a pinned comment with ST5; for a serious error archive the post and publish a corrected one. A YouTube Short cannot be replaced: edit the title and description, pin ST5, and unlist and re-upload for a serious error. Editing rules per platform are *unverified*; find them in the dry run.
2. A corrected post is a new draft: `python3 pipeline/scripts/queue.py new-draft ...`, then `validate`, then the two keys in an expedited review. Take the old one down only when the new one is live, unless it is severity A.
3. If the error was in a reply to a commenter, correct the reply in the thread (ST5 style) and log it.
4. Write the root cause: which step failed (the source slip, the operator's check, the wife's read, the draft itself, a source that changed).

**First week**

1. Sweep every other post that used the same source or figure.
2. Update the re-check ledger (步驟) or the source slip template.
3. Count it: a second published error within six weeks pauses the persona until the QA step is fixed. For 步驟, a second error that survived the source slip kills hypothesis H4.
4. Re-score CON-2. Ask whether Claude's draft invented the figure; if so, say so in the note so the check is aimed at that.

**Evidence:** before and after screenshots; the source page reopened and screenshotted with the date; `post.json` sources; who approved and when; the time of the notice and of the correction.

**Lawyer:** only if someone says they were harmed by acting on it (section 5 item 6).

**Do not:** quietly swap the media and leave comments pointing at nothing; blame the viewer; explain at length why it happened.

**Statement:** ST5.

### 7.6 Scenario 6: a Ground rule 6 contact (or Rule 4 testimony) reached publication

Covers: a published post or reply with a health, weight-loss or cosmetic claim, an investment or financial-advice claim, gambling, politics or a cross-strait remark, or an "I tried it, wore it, used it" line; an image showing a hand holding a product, a location or a candid look (addenda 8.3); a sponsor brief that asks for one (not published, but a near-miss). Risks: CON-3, CON-4. Clock: take down within 24 hours; pause the persona 7 days; a second event within 8 weeks retires the persona or the pillar.

**Decider:** both. The operator takes the post down; the wife judges whether the wording is in fact testimony or a claim (she is the language judge); the lawyer is called if the claim was regulated and ran with sponsor or affiliate money, or a regulator writes.

**First hour**

1. Archive the post (capture first). Unschedule the persona.
2. Search for the same wording elsewhere: `python3 pipeline/scripts/queue.py validate` over all queued and published folders; look at the last two weeks of replies.
3. Note the category (health, finance, gambling, politics, testimony, image rule).
4. Tell the other person; log a standing event with gate `rule6_contact`.

**First day**

1. Write the root cause: how did it pass the draft scan, the wife and the operator? Which control was blind? (The keyword net is blunt; a rephrased claim can pass.)
2. Check whether anyone replied to it or the persona engaged with a politics thread; hide what must be hidden.
3. Statement: none by default. ST6 only if the post had real reach or was reported.
4. If a regulator, the platform or a sponsor writes about it: section 5.

**First week**

1. The persona stays paused for **7 days** from the take-down. Resume only when both agree and the root cause is written. The first post back is a low-risk pillar.
2. Add the wording to the wife's word lists (`pipeline/scripts/ground_rules.py`) and the QA checklist.
3. Count: a **second event within 8 weeks retires the persona or the pillar** (both decide; record in DECISIONS.md). Three or more of any 20 drafts caught means redesigning the pillars before continuing.
4. Re-score CON-3.

**Evidence:** the post, its approvals and notes, the scan output, the root-cause note, the thread.

**Lawyer:** a regulated claim with money behind it; any agency contact; a viewer who says they were harmed.

**Do not:** edit the post in place and leave it up; delete without capturing; repost the same idea reworded the next day.

**Statement:** ST6 (optional).

### 7.7 Scenario 7: typhoon, earthquake, disaster, public tragedy or national mourning

Covers: a typhoon warning or a work-and-school-closure announcement (停班停課) affecting where your audience lives; a major earthquake or accident; a public tragedy; an officially announced period of national mourning. Risks: CON-5. Typhoon season is recalled as about July to October ([culture.md](../research/culture.md) 4 and 5.2); the pause switch runs all year. Official warning names and announcement processes are *unverified*: use the weather agency's (中央氣象署) public pages and your local government's announcements.

**Decider:** either of you, alone and at once, for all three personas (tone is a studio matter). The wife decides when it is respectful to return.

**First hour**

1. Unschedule everything that publishes **today and tomorrow**, for all personas and platforms; count the items before and after; write it in `launch/schedule-log.csv`. The earliest scheduled slot is 08:15 (步驟 on Threads), so check at 07:30 on warning days ([schedule.md](../launch/schedule.md) section 6).
2. Do not post a "stay safe" message and do not give any safety, weather or health advice: a persona has no standing for it and Ground rule 6 bars it. Pointing to the official source is allowed (ST7a).
3. Hide any flippant or political comment under the persona's earlier posts; reply to nothing except an error report.
4. Screenshot the official warning page with the time, as the reason for the pause.

**First day**

1. Look through the next seven days of posts for a clash in tone: rain-day outfits during a flood (色環), damp, mould or move-house content (方寸), or any cheerful weather joke. Swap or hold them. Re-date by whole days only where the calendar rules allow, and re-run `python3 launch/schedule_check.py --w0 <date>` with any `--no-post` dates.
2. Check on each other. If either of you is affected, the daily notice check and the 24-hour clocks are suspended for that person and the other covers.
3. Silence is usually right. Use ST7a or ST7b only if the persona has an audience that expects a post, and only if the wife agrees.

**First week**

1. Resume when the official warning is lifted and life has resumed locally; after a mass-casualty event allow at least a day or two more (*assumption*; the wife decides). Both agree.
2. **Do not catch up.** Never publish the missed posts in a burst ([schedule.md](../launch/schedule.md) section 5). Skip them or fold the idea into a later week through the normal rhythm.
3. For national mourning: nothing celebratory, no red-and-festive colours, no jokes. Muted palettes are already the studio's default.

**Evidence:** the official page screenshot with the time; the schedule log; what was unscheduled and re-dated.

**Lawyer:** no.

**Do not:** post "we are paused" for a one-day event nobody noticed; post a charity or donation call (finance and fraud adjacency); keep a scheduled post because "it is approved".

**Statement:** ST7a (weather or disaster), ST7b (mourning), both optional.

### 7.8 Scenario 8: brand, sponsor, client or vendor dispute

Two kinds. **Kind A, unsolicited:** a named brand, shop or tool vendor complains about a post that mentions them (a 步驟 recording, a comparison, a mention in a caption) with no contract. **Kind B, contracted** (only after registration; no sponsored post is possible in the first 30 days): a client disputes a deliverable, wants a label removed, asks for testimony, does not pay, or a brief breaks the red-flag list. Risks: BIZ-3, LEG-2. No 6.2 clock unless the complaint is also a Scenario 5 or 6; the 步驟 vendor-complaint row says pause that video.

**Decider:** both. The wife, as registrant, holds the contract position with the 記帳士 or lawyer; the operator holds the facts and the content.

**First hour**

1. Do not reply in the comments or DMs, and do not negotiate there. Capture the message.
2. Establish the kind: is there a signed agreement, a brief or any money? Who asked for what, in writing?
3. Kind A: pause (unlist) that post or video while you read the source slip and, for a vendor, its published terms on public demonstration and logo use (logged at gate G7 in the 步驟 bible).
4. Tell the other person; if it reads like a letter, section 5.

**First day**

1. Reply in writing from the studio mailbox only, with ST8a (holding), never a verdict. For a contracted client, pull the contract, brief, approval records and any written instruction to remove disclosures.
2. Sort the demand, using the table below.
3. A factual complaint is checked against the source slip like any error: if the post is wrong, Scenario 5.

| Demand | Response |
|---|---|
| Remove the AI or 業配 label, or the "character has not used this" sentence | Refuse. These are the studio's content principles and a contract clause (bibles 9.4) |
| Say the character used it, add results or a testimonial | Refuse (Ground rule 4) |
| Correct a wrong fact | Verify; if wrong, correct inside 24 hours (7.5) |
| Take the post down | Kind A: take it down if the complaint alleges a factual error, a misused logo or image, or a legal claim, otherwise keep it and reply in writing. Kind B: follow the contract's approval and termination terms |
| An unpaid invoice | The 記帳士; no public mention; pause further work under the contract |
| A vendor objects to a recording or a mention | Pause that video; the operator reads the terms; answer in writing; keep it if the terms allow public demonstration, take it down if not (步驟 bible 7.3) |
| Exclusivity or a competitor conflict | The contract and the ISO-week brand ledger ([portfolio.md 3.3](../strategy/portfolio.md) item 4) |

**First week**

1. Written resolution through the studio mailbox; the wife signs if a position is taken.
2. Log the dispute in the incident note. Re-score BIZ-3 and LEG-2.
3. Decide whether to continue with this counterparty. A client who asks twice to drop a label is a red flag (bibles 9.3).

**Evidence:** every message in full with headers; the contract, brief and approvals; the source slip for each claim at issue; dated screenshots of the post; payment records.

**Lawyer:** at once for a threat, a money claim, or an allegation of false advertising, infringement or defamation (section 5 item 3). The studio may share liability for a client's false claim if it "knew or should have known" (*unverified*, [legal.md](../research/legal.md) 3.3).

**Do not:** discuss a dispute publicly; let a persona reply; remove a disclosure to keep a client; accept free goods that come with a posting obligation outside a contract.

**Statements:** ST8a (private holding email); ST8b only if the other side goes public.

### 7.9 Scenario 9: account compromise or lockout

Covers: an unrecognised login alert; a password-change email; posts or messages you did not write; being locked out; a lost or stolen phone; a phishing message that claims a violation. Risks: ACC-3. Full first-hour steps already exist in [00-studio-setup.md](../launch/00-studio-setup.md) section 13; this adds the day and the week.

**Decider:** both; either may start. Use the other person's device or a clean browser for the first steps.

**First hour**

1. Do not tap links in any message about the account. Open the platform's login help by typing the address or from the app.
2. Change the password in the vault; sign out of all sessions; confirm the two-factor methods, recovery email and recovery phone are still yours.
3. Unschedule everything for that account. Delete anything you did not write (capture it first). Report it in the app.
4. If locked out, use only the platform's own recovery path. **Never pay or hire anyone who offers to recover an account.**

**First day**

1. Check connected apps and permissions, logged-in devices, forwarding rules and recovery settings on the studio mailbox, and the other accounts that share the email or password.
2. If followers received scam messages, pin ST9. If nothing went out, say nothing.
3. Tell the registrant (the wife). Log a row in `launch/evidence-log.csv`.

**First week**

1. Root cause: phishing, a reused password, a lost device, a shared-login security flag. Rotate everything that could be affected. Re-run the recovery test.
2. If the account is still restricted after the owner has recovered it, that is Scenario 1.
3. Update [00-studio-setup.md](../launch/00-studio-setup.md) with what you learned. Re-score ACC-3.

**Evidence:** the alert emails with headers, the login history screenshots, what was posted or sent and when.

**Lawyer:** if money was lost or other people's personal data was exposed.

**Statement:** ST9.

### 7.10 Scenario 10: impersonation, stolen images or the face in a scam

Covers: an account using a persona's name or images; images re-posted without the label; the face used in a scam ad or a fake endorsement; a deepfake of the character. The face is synthetic and may have no copyright (*unverified*), so protection leans on the platform's impersonation rules and the name. Risks: PHO-3. Clock: report within 24 hours (*assumption*).

**Decider:** the operator reports; the wife reads Chinese reports and any scam messages.

**First hour**

1. Capture the account or ad: URL, name, images, date, and any message sent to people.
2. Report it through the platform's impersonation or scam-ad form (names *unverified*). Do not contact the account owner and do not reply to their messages.
3. Confirm the studio link page still lists the real accounts; it is the answer you point people to.

**First day**

1. If people have been asked for money or data, pin ST10. If not, do not draw attention to it.
2. For a scam using the face, report to the platform's ad team as well and, if money is involved, to the police anti-fraud channel (the 165 hotline is recalled and *unverified*; confirm before using it).
3. Check your own posts for the badge; an image re-posted without the badge is exactly the PHO-1 case.

**First week**

1. Follow up the reports at day 3 and day 7. Re-run the reverse search of the avatar and R01 (public tools, by hand).
2. Decide with the lawyer whether a notice or a trademark step is worth the cost; the legal route for a synthetic face is a lawyer question.
3. Re-score PHO-3.

**Evidence:** the captures, the report ticket numbers, the dates, the reverse-search results.

**Lawyer:** if money was lost, if a real person is being impersonated using the character, or if a company or ad network refuses to act.

**Statement:** ST10.

## 8. Minor incidents: a quick table

These need no scenario. Each still gets a log line (the tracker standing event where a gate exists) and a one-line root cause. Clocks are from [portfolio.md 6.2](../strategy/portfolio.md) and the addenda.

| Incident | Do | Clock and escalation |
|---|---|---|
| A label or badge is missing or cropped on a live post (disclosure failure) | Add or fix it; re-run the live check; sweep the last ten posts; gate `disclosure_failure` | Inside 24 hours. A repeat in the same quarter pauses the persona |
| 5 or more 「是真人嗎」 comments in a week (3 or more in the first two weeks, per the addenda) | Reply plainly every time (existing reply); strengthen the first line and badge; gate `real_person_comments` | Inside 48 hours |
| A visible face, hand, earring or text defect on a live image | Correct or take down; check the QA row that should have caught it | Inside 24 hours; two in six weeks pause the persona |
| Garbled or Simplified Chinese on a live post | Replace or archive; the wife reads every character of the fix | Inside 24 hours; two in six weeks pause |
| 3 or more of any 20 drafts caught with testimony, health, finance or income wording | Stop drafting; redesign the pillars with Claude and the wife; gate `near_miss_rate` | Before continuing |
| The persona asks viewers for personal data (步驟) | Fix the post or reply; log | Inside 24 hours; a repeat in the quarter pauses |
| A recording shows a notification, key, tab or personal data (步驟) | Take down; rotate any key; rebuild the recording hygiene kit | Inside 24 hours |
| An image shows a hand holding something, a location, a mirror or a candid look | Take down; treat as a Ground rule 1 or 4 contact (7.6) | Inside 24 hours; pause 7 days |
| The image tool's model label changes between two generations of one set | Stop; treat as a new design; re-run the age, look-alike and near-pair tests | Before the next image is used |
| A reply you sent gave a verdict, a safety or lease opinion, or testimony | Delete or correct the reply (capture first); log as a near-miss | Inside 24 hours |
| A viewer names a real person the character resembles | Scenario 7.2 | Inside 24 hours |

## 9. Statement bank (zh-TW DRAFTS for the wife)

**Everything here is an AI draft.** The wife adapts every line in her own voice, rules on every word, and strikes anything that sounds 工商味 (like an ad), stiff or translated. Rules for all of them:

* The speaker is the studio: 「工作室」, in the third person, even inside a post on a persona account. Public texts use 「你」; private emails to a person or company use 「您」 (the wife may prefer 「你」). No emoji. No 「官方」 and no 「公司」 (the studio is not a registered company and must not sound official; the name is provisional).
* State facts and what the studio did. No guesses about the cause, no blame, no promises of compensation, no "we guarantee".
* A statement published as a post begins with the AI line 「【AI 虛擬角色】…」 and carries the badge and the platform label like any post; a pinned comment or a reply does not need to.
* Fill every {placeholder} before use. {工作室信箱} is the studio mailbox, which does not exist yet.
* Nothing is posted until both keys are turned (section 3). Whether any of these lines creates a legal admission is a lawyer question.

| ID | Use when | zh-TW (DRAFT) | English gloss | Notes |
|---|---|---|---|---|
| ST1 | Scenario 1, only if followers ask why the account went quiet | 【說明】這個帳號目前有部分功能受到平台限制，工作室正在處理。處理期間暫停更新，有進展會再通知。 | [Notice] Some functions of this account are currently limited by the platform and the studio is dealing with it. Updates are paused meanwhile; we will let you know when there is news. | Default is silence. Never name the platform's reason; never blame anyone |
| ST2a | Scenario 2: private reply to a person who says the face resembles them | 您好，謝謝您來信告知。<br>我們已收到您對角色「{角色名}」外觀的意見，並已於 {日期時間} 先將相關貼文下架，同時暫停該角色的更新，進行比對檢查。<br>「{角色名}」是由 AI 生成的虛構角色。製作時沒有使用任何真人照片作為參考，也沒有以特定真人為藍本，製作紀錄由工作室留存。<br>為了讓我們核對，如果方便，請告訴我們您認為相似的地方。不需要提供身分證件或其他個人資料。<br>我們會在 {日期} 前回覆檢查結果。<br>明說角色工作室 敬上 | Hello, thank you for writing to let us know. We have received your comments on the appearance of the character "{name}", and at {date and time} we took the related posts down and paused the character's updates while we run a comparison check. "{name}" is a fictional character generated by AI. No photo of any real person was used as a reference in making it, and it is not modelled on any specific real person; the studio retains the production records. To help us check, if it is convenient, please tell us where you see the resemblance. Please do not provide ID documents or other personal data. We will reply with the result of the check by {date}. Plainspoken Studio | Delete the third paragraph unless the provenance log supports it at that moment. No apology, no admission, no offer of money. The lawyer reads this first if the person is identified or has a lawyer |
| ST2b | Scenario 2: public holding line, only if the claim is already public | 我們看到有人認為角色「{角色名}」的外觀與真人相似。相關貼文已先下架，工作室正在進行比對檢查，完成後會再說明。如果你是當事人，歡迎來信 {工作室信箱}。 | We have seen people say the character "{name}" looks like a real person. The related posts have been taken down for now and the studio is running a comparison check; we will explain when it is done. If you are the person concerned, you are welcome to write to {studio mailbox}. | Never name the person. Never say "it does not look like anyone" |
| ST3a | Scenario 3: accusation of deception, all four labels were present | {角色名}是 AI 生成的虛擬角色，不是真人。簡介、每則貼文的第一行、圖片角落的標示，以及平台的 AI 標示都有說明。如果你在某則貼文上沒有看到這些標示，請告訴我們是哪一則，工作室會立刻檢查。 | {name} is an AI-generated virtual character, not a real person. This is stated in the bio, in the first line of every post, in the label in the corner of the picture, and in the platform's AI label. If you did not see these labels on a post, please tell us which one and the studio will check at once. | Check the live post first. Reply once |
| ST3b | Scenario 3: a label was in fact missing | 謝謝提醒。這則貼文漏了 {標示名稱}，工作室已於 {日期時間} 補上。 | Thank you for the reminder. This post was missing {label name}, and the studio added it at {date and time}. | Default is this plain statement of fact, which section 1 rule 7 allows without the lawyer. The wife (with the lawyer, if the matter is already a claim or a press enquiry) decides whether to add an apology sentence such as 「這是工作室的疏失，造成誤會很抱歉。」 (This was the studio's oversight and we are sorry for the misunderstanding); an apology is not used before that |
| ST4 | Scenario 4: pinned note during a comment wave about AI or disclosure | 謝謝大家的意見，我們都有看到。這個帳號是 AI 虛擬角色，由明說角色工作室創作與營運，標示在簡介和每則貼文裡。內容如果有錯誤，歡迎留言指正，工作室會查證並更正。和貼文無關的留言（例如廣告、人身攻擊）可能會被隱藏。 | Thank you for your comments; we have seen them all. This account is an AI virtual character created and run by Plainspoken Studio, labelled in the bio and in every post. If anything in the content is wrong, please say so in a comment and the studio will check and correct it. Comments unrelated to the post (for example ads and personal attacks) may be hidden. | Pin it once; do not repeat it in replies. Politics is deliberately not named, so the note does not invite it |
| ST5 | Scenario 5: a correction (caption, pinned comment or reply) | 【更正】本篇{第 N 頁／影片 mm:ss}的「{原本內容}」有誤，正確資訊是「{更正內容}」（出處：{出處名稱}，資料日期 {YYYY/MM/DD}）。工作室已於 {YYYY/MM/DD} 更正，謝謝指正。 | [Correction] In this post, {page N / video mm:ss}, "{original text}" was wrong; the correct information is "{corrected text}" (source: {source name}, data date {date}). The studio corrected it on {date}; thank you for pointing it out. | Say what was wrong and what is right, nothing more. The operator has reopened the source before this goes out |
| ST6 | Scenario 6: take-down note, only if the post had real reach or was reported | 【下架說明】先前有一則貼文的內容不符合工作室的內容原則，已經下架。這個帳號是 AI 虛擬角色，沒有使用經驗，也不提供健康、投資或政治相關的建議。 | [Take-down note] An earlier post did not meet the studio's content principles and has been taken down. This account is an AI virtual character with no experience of using anything, and it does not give health, investment or political advice. | Default is silence. Do not repeat the problem wording. The project's word scanner FLAGS this line because it names the barred topics inside a denial; the studio already uses that disclaimer pattern |
| ST7a | Scenario 7: pause during a typhoon or disaster, only if followers expect a post | 因應{颱風／災害}，{角色名}今天暫停更新。相關資訊請以中央氣象署與各地政府公告為準。 | In view of {the typhoon / the disaster}, {name} is pausing updates today. For information please rely on the announcements of the weather agency (中央氣象署) and local governments. | Points to official sources only; gives no safety advice |
| ST7b | Scenario 7: pause during national mourning or a public tragedy | {角色名}今天暫停更新，向受影響的家庭致意。 | {name} is pausing updates today and sends respects to the affected families. | Silence is often better. The wife decides whether any line is right |
| ST8a | Scenario 8: private holding email to a brand, sponsor or vendor | 您好，已收到您的來信，謝謝。<br>工作室會先對照合約與貼文內容確認，預計於 {日期} 前以書面回覆。確認期間，相關貼文{維持現狀／先行下架}。<br>另外說明：工作室所有 AI 虛擬角色的貼文，依內容原則必須標示 AI 生成與合作關係。角色沒有使用過任何商品，因此無法提供使用心得或效果保證，也無法移除相關標示。<br>明說角色工作室 敬上 | Hello, we have received your message, thank you. The studio will first check the contract and the post and expects to reply in writing by {date}. While we check, the related post will {stay as it is / be taken down for now}. Please also note: every post by the studio's AI virtual characters must carry the AI-generated and collaboration labels under the studio's content principles. The character has not used any product, so it cannot give a usage review or a promise of results, and the labels cannot be removed. Plainspoken Studio | Choose one option in the second paragraph. Do not argue the merits here |
| ST8b | Scenario 8: only if a brand criticises the studio in public | 我們已看到{廠商}的說法。工作室正在核對資料，目前不便公開細節，會以書面方式與對方聯繫。 | We have seen {company}'s statement. The studio is checking the records, cannot give details publicly at present, and will contact them in writing. | Lawyer first |
| ST9 | Scenario 9: only if followers received scam messages from a compromised account | 【注意】這個帳號近期曾遭未經授權登入，工作室已處理，並刪除了非工作室發布的內容。{角色名}不會私訊要求你點連結、提供個人資料或匯款。收到這類訊息請不要理會，並向平台檢舉。 | [Notice] This account was recently logged into without authorisation. The studio has dealt with it and deleted content not posted by the studio. {name} will never message you asking you to click a link, give personal data or send money. If you receive such a message, please ignore it and report it to the platform. | Pin it; do not say how it happened |
| ST10 | Scenario 10: an impersonating account or scam use | 近期有帳號冒用角色「{角色名}」的名稱或圖像。{角色名}只有工作室連結頁（{網址}）上列出的帳號。工作室不會私訊要求提供個人資料或匯款，收到可疑訊息請不要理會，並向平台檢舉。 | Recently an account has used the name or images of the character "{name}". {name} has only the accounts listed on the studio link page ({URL}). The studio will never message you asking for personal data or money; if you receive a suspicious message, please ignore it and report it to the platform. | Avoid 「官方」. Do not name or link the impersonator |
| ST11 | Scenarios 3 and 4: a short holding reply to a comment that demands an answer | 謝謝你的意見，工作室已收到，會查證後再回覆。 | Thank you for your comment; the studio has received it and will check before replying. | Use only when a real answer will follow |

## 10. Templates

### 10.1 Incident note (create `ops/incidents/INC-YYYYMMDD-NN.md` when the first one is needed; no personal data)

```
INCIDENT  id: INC-YYYYMMDD-NN   scenario: __   persona / platform: __
Noticed: date and time (Taiwan) ____ by ____     Clock starts: ____     Clock ends: ____
Evidence folder code (private drive): E-YYYYMMDD-NN
What happened (facts only; no names of viewers or claimants):
Actions, with times and who:  paused ____ | taken down ____ | told the other ____ | appeal / report ____
Deciders: ____     Lawyer called: yes / no (time ____)
Standing event logged: gate ____   ref ____   (analytics standing import)
Root cause (within 24 hours for a 6.2 event): the control that failed ____ ; why ____
Fix: the control changed ____ ; who ____ ; by ____
Resumed: date ____   agreed by both: yes / no
Register rows to re-score: ____
```

### 10.2 Post-incident review (15 minutes at the next standup)

1. What was the first sign, and who saw it? How long until the other person knew?
2. Which clock applied, and was it met? If not, why not?
3. Which control should have caught it (the draft scan, the wife's read, the operator's check, the live check, the daily notice check)? Why did it not?
4. What changes: one control, one owner, one date. Add it to HUMAN_TODO or the QA checklist.
5. Which register rows change, and is any gate (6.2) now open?
6. What did it cost in minutes for each of you? Log it, because incidents are the part of the plan no hour is reserved for.

### 10.3 One page for the lawyer

```
Who we are (registrant / operator, studio name provisional), what the studio does (openly AI virtual characters).
What happened, with dates and times (Taiwan time).
What we have done so far, with times (paused, took down, did not reply).
What we hold as evidence (list, with file names; nothing attached until you tell us how).
The question we need answered: ____
The deadline, if any: ____
What we have NOT done: apologised, admitted, offered money, contacted the other side.
```

## 11. Open items and what was not checked

* **Every platform step is unverified.** Archive, hide, restrict and report controls, appeal forms, label menus and edit limits were never seen. Fill them in from the dry runs.
* **No Taiwan law was read.** Liability for an apology, the effect of a take-down on a claim, the portrait-right threshold, the PDPA treatment of evidence folders and the retention period are all lawyer questions (HUMAN_TODO 9, 27, 37).
* **The 24-hour clocks need a daily look at the studio mailbox and the accounts**, which is a new task (weekly-routine section 8); without it the clocks cannot be met.
* **The Tier A / Tier B reading of the likeness clock, the severity classes in Scenario 5, the 20-comment wave trigger and the two-day resume rule after a tragedy are the author's *assumptions*.** The portfolio gives none of them.
* **The statements are drafts.** The wife has not read them; the studio name is provisional; the studio mailbox and link page do not exist.
* **No incident has ever occurred.** Every time and step here is untested; run the pause drill and read this file aloud together once before the first post.
