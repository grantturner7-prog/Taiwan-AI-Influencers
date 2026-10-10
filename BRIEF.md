# Project brief: a studio of 10 AI influencers for Taiwan

**How to use this file:** save it as `BRIEF.md` in an empty project folder, open Claude Code in that folder, and say:
"Read BRIEF.md, ask me the Section 2 questions, then start Phase 0."

---

## 1. Mission

I am a solo operator. Build everything I need to design, launch, run and monetise ten virtual (AI-generated) influencers for audiences in Taiwan.

"Successful" means, in this order:

1. Accounts that stay in good standing on every platform.
2. Audiences that engage, measured by saves, shares, comments and link clicks, not follower count alone.
3. Revenue per persona that exceeds its running cost.

You (Claude Code) do the research, strategy, writing, tooling and analysis. I do what only a person can do: create accounts, pass phone and ID verification, pay for tools, approve posts, talk to brands, sign contracts. Keep a running list of my jobs in `HUMAN_TODO.md`, in the order I should do them.

## 2. Ask me these before you start

Record my answers in `DECISIONS.md`. Do not assume any of them.

1. Monthly budget in NT$ for tools, and separately for a native reviewer if one is needed.
2. Hours per week I can give this.
3. How well I read and write Traditional Chinese. If I am not fluent, plan for a native Taiwanese reviewer on every post and include the cost.
4. Which image, video and voice generation tools or API keys I already have.
5. Whether I have a registered business in Taiwan that can invoice brands.
6. Niches I know well or have contacts in.
7. Anything I refuse to promote.

## 3. Ground rules

These apply to every file, script and post. The accounts, the brand deals and my legal exposure all depend on them, so treat a conflict with any rule as a reason to stop and ask me.

1. **Openly virtual.** Every persona says it is an AI character in its bio (for example 「AI 虛擬角色」) and every realistic image, video or voice post carries the platform's AI label. Undisclosed AI personas are the thing platforms, regulators and audiences are reacting against. Disclosure is also the positioning: a character people know is virtual and follow anyway.
2. **Original likeness.** No face, body, voice or name modelled on a real person, a celebrity, or an existing fictional character. Keep the prompt, model and date for every asset in `assets/provenance.csv` so I can prove origin if challenged.
3. **Adults only.** Every persona is designed and written as clearly 25 or older. No sexualised content and no adult-content funnels.
4. **No invented experience.** A virtual character has not eaten, worn, used or tested anything. Scripts present, explain, compare and demonstrate. They never testify ("I tried this for a month"), and they never invent customers, reviews or results.
5. **Disclose paid relationships.** Sponsored and affiliate posts are marked in the caption and with the platform's paid-partnership tool.
6. **Stay out of regulated and sensitive territory.** No health, medical, weight-loss or cosmetic-efficacy claims. No investment or financial advice. No gambling. No politics, elections or cross-strait topics.
7. **No fake popularity.** No bought followers, likes or views, no bot comments, no engagement pods.
8. **One studio, in the open.** Every bio names the studio behind the character. Personas never vouch for each other as if they were independent voices.
9. **Platform rules.** Official APIs and approved scheduling tools only. No scraping behind logins and no automation that breaks terms of service. I approve every post for at least the first 30 days. Any automated reply or DM says it is automated.
10. **Evidence.** Every market, pricing or legal claim gets a source and a date in `SOURCES.md`. If you cannot verify something, label it "unverified". Never fill a gap with an invented number.

## 4. Starting facts (checked 10 October 2026)

Re-verify these in Phase 1 and replace anything out of date.

- **Platform reach.** Taiwan's NCC 2025 report puts account ownership at LINE 98.2%, Facebook 82.4%, YouTube 68.6%, Instagram 47.8% and TikTok 23.8%. TikTok content has been watched by 47.5% of people overall and 72.5% of those aged 16 to 25.
- **Young adults.** An MIC survey found people aged 18 to 24 favour Instagram (78%), Dcard (45.9%) and Threads (44%).
- **AI law.** Taiwan's AI Basic Act has been in force since 14 January 2026. It is a framework law and its principles include a bar on AI use for false advertising. Sector regulators are issuing their own guidance under it.
- **Ad disclosure.** The Fraud Crime Hazard Prevention Act (詐欺犯罪危害防制條例, 2024) requires online advertising platforms to disclose AI-generated personal images in ads.
- **Endorsements.** The Fair Trade Commission (公平會) treats sponsored posts as endorsement advertising (薦證廣告). Material connections must be disclosed, and endorsers can share the advertiser's liability. Confirm the current fine range.
- **Platform labels.** TikTok, YouTube and Meta all require a label on realistic AI-generated people, voices and scenes.
- **Market mood.** Signals are mixed. Kolr's 2026 report (iKala) says brands are prizing verifiable human creators, and press coverage of brands passing off AI personas as real customers has caused a trust backlash. Treat "is there real demand for disclosed virtual characters in Taiwan?" as an open question for Phase 1, not a given.

## 5. Language and culture

- Working documents: English, with the zh-TW term beside any Taiwan-specific concept.
- Everything the audience sees: Traditional Chinese as written in Taiwan. Avoid mainland vocabulary (影片 not 視頻, 品質 not 質量, 資訊 not 信息, 網紅 or 創作者 not 博主). Mainland phrasing gets called out fast and is hard to recover from.
- Voices: test every text-to-speech option for a Taiwanese Mandarin accent before recommending it.
- Images: check all on-image Chinese text by eye. Generators often garble characters or output Simplified forms.

## 6. Phases

Work in order. At each **STOP**, summarise what you found, give your recommendation, and wait for my decision.

### Phase 0: Setup
- Create the folder structure in Section 7, plus `DECISIONS.md`, `SOURCES.md`, `HUMAN_TODO.md` and `COSTS.md`.
- Ask the Section 2 questions.

### Phase 1: Market research → `research/`
- `platforms.md`: who uses what in Taiwan by age and interest, which formats each platform rewards, and each platform's current AI-content and branded-content rules.
- `competitors.md`: every virtual influencer, VTuber and AI character account you can find that is active in Taiwan, plus the strongest regional examples. For each: niche, follower count, engagement, posting rhythm, how it discloses, how it earns.
- `niches.md`: score at least 20 niches on audience size, advertiser spend, competition, fit for a virtual character, and compliance risk under Ground rule 6.
- `monetisation.md`: what is actually available to a Taiwan-based account, with terms and typical rates. Cover sponsored posts (業配) by follower tier, affiliate programmes, LINE stickers and LINE Official Accounts, licensing a character to a brand as its spokes-character, producing AI ad creative for brands as a service, and own digital products.
- `legal.md`: the Fair Trade Act endorsement rules, the AI Basic Act and any guidance issued under it, the anti-fraud ad disclosure duty, sector advertising rules (food, cosmetics, medical, finance), business registration and tax on creator income, and trademark protection for character names and likenesses. End with a list of questions for a Taiwanese lawyer. This file is research, not legal advice.
- `culture.md`: tone by platform, slang, meme habits, the commercial calendar (農曆新年, 中秋, 雙11, 週年慶 and others), and topics to avoid.

**STOP 1.** Tell me plainly whether the research supports the demand, and which niches and revenue routes look strongest.

### Phase 2: Portfolio strategy → `strategy/portfolio.md`
- Ten personas as a portfolio: each a distinct niche, audience and primary platform, with a map showing they do not compete with each other.
- Name the studio and write its one-paragraph public description.
- Pick three pilot personas and say why. Design all ten, launch three, and add the rest in waves. One person must approve every post, and ten accounts on two platforms at five posts a week is 100 posts a week.
- Set numeric scale, keep and retire thresholds from the Phase 1 benchmarks, to be applied six weeks after each launch.

**STOP 2.** I approve the ten concepts and the three pilots.

### Phase 3: Persona bibles → `personas/<handle>/bible.md` (×10)
For each persona:
- Chinese name and handle, with the handle's availability added to `HUMAN_TODO.md` for me to check.
- Stated age (25+), fictional background, personality, values, running jokes.
- Voice rules and 20 sample lines in zh-TW across captions, replies and video scripts.
- Visual identity: face and build description, styling, wardrobe, colour palette, and recurring Taiwan settings.
- Character consistency sheet: the reference prompts and reference images needed to reproduce the same face every time.
- Three or four content pillars, formats per platform, and a do and don't list.
- The exact disclosure line for the bio.
- Monetisation fit and brand-safety notes.

### Phase 4: Production pipeline → `pipeline/`
- `tools.md`: compare current image, video, voice and lip-sync tools on character consistency, zh-TW voice quality, API access, price, and commercial-use licence terms. Recommend a stack inside my budget.
- Scripts that wrap the chosen APIs: prompt in, asset out, provenance row written.
- A review queue: each draft post as a folder with media, caption, hashtags, AI-label flag, sponsorship flag, and an approve or reject field.
- `qa-checklist.md`: hands and faces, garbled or Simplified text, uncanny motion, off-voice captions, missing disclosure.

**STOP 3.** Show me five finished sample posts for one pilot persona before producing anything in bulk.

### Phase 5: Content system → `content/`
- A 30-day calendar for each pilot persona. Weeks 1 and 2 fully written (hooks, scripts, captions, shot prompts, hashtags). Weeks 3 and 4 outlined.
- A hook library and three repeatable series formats per persona.
- A weekly trend-check routine and reply guidelines for comments.

### Phase 6: Launch → `launch/`
- An account setup checklist per platform and persona: handle, bio with disclosure, profile image, link page.
- A link-in-bio page per persona, built as static HTML.
- The posting schedule and scheduler setup, using official APIs or an approved tool.

### Phase 7: Analytics → `analytics/`
- A tracker (SQLite or CSV) and a simple local dashboard: followers, reach, engagement rate, saves, shares, link clicks, cost and revenue per persona.
- A weekly report script that says what worked, what did not, and one experiment to run next.
- An experiments log.

### Phase 8: Monetisation kit → `monetisation/`
- A media kit per persona in zh-TW and English.
- A rate card built from the Phase 1 rate research.
- 50 Taiwan brands and agencies per pilot niche, with outreach emails in zh-TW for me to send.
- A one-page offer for the studio's B2B services.
- A sponsorship contract checklist.
- A revenue model with low, middle and high scenarios. State and source every assumption. Do not promise outcomes.

### Phase 9: Risk and operations → `ops/`
- A risk register: account bans, policy changes, audience backlash, tool price or licence changes, likeness complaints.
- A crisis playbook and the weekly operating routine for one person.

## 7. Folder structure

```
BRIEF.md
DECISIONS.md
SOURCES.md
HUMAN_TODO.md
COSTS.md
research/
strategy/
personas/<handle>/
pipeline/
assets/provenance.csv
content/<handle>/
launch/
analytics/
monetisation/
ops/
```

## 8. How to work

- Finish one phase before starting the next, and stop at every STOP.
- Record each decision and its reason in `DECISIONS.md`.
- Log every paid tool and its monthly cost in `COSTS.md`.
- When a task needs me, add it to `HUMAN_TODO.md` and carry on with whatever does not depend on it.
- If the research says a plan in this brief is wrong, say so and propose the change.

## 9. Done means

- Three pilot personas are live, each with 30 days of content planned and two weeks ready to post.
- The other seven have complete bibles and are ready to launch in waves.
- The pipeline produces a compliant, labelled, on-voice post from a one-line idea.
- The dashboard and weekly report run on real data.
- The media kits, rate card and outreach lists are ready to use.

## 10. Sources for Section 4

- [TikTok viewership surges in Taiwan, Focus Taiwan (CNA), 4 Jan 2026](https://focustaiwan.tw/culture/202601040012)
- [Over 70% favor YouTube and Facebook: poll, Taipei Times via LTN, 9 Dec 2025](https://news.ltn.com.tw/news/focus/breakingnews/5271932)
- [NCC guidelines under the AI Basic Act, Taiwan News](https://www.taiwannews.com.tw/en/news/6380429)
- [Taiwan's AI governance framework unveiled, IAPP](https://iapp.org/news/a/taiwan-s-ai-governance-framework-unveiled)
- [公平會發布對於薦證廣告之規範說明, Lee and Li](https://www.leeandli.com/TW/Newsletters/2501.htm)
- [網路業配文要先說清楚講明白嗎?, ETtoday](https://www.ettoday.net/news/20171012/1029965.htm)
- [How to Label AI-Generated Content on Social Media, Metricool](https://metricool.com/how-to-label-ai-content/)
- [AI disclosure rules by platform, Influencer Marketing Hub](https://influencermarketinghub.com/ai-disclosure-rules/)
- [Kolr 2026 AI 行銷趨勢報告書, 數位時代](https://www.bnext.com.tw/article/90807/ikala_kolr_2026_04)
- [虛擬網紅 coverage, TVBS](https://news.tvbs.com.tw/news/searchresult/虛擬網紅/news)
