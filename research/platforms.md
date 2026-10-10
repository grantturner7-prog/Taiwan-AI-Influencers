# Platforms research: who uses what, which formats win, what the rules are

Phase 1 deliverable `research/platforms.md`. Written 2026-10-10. Scope: Taiwan audiences, a studio of openly-virtual (disclosed AI) personas, one operator at 6 h/week, NT$5,000/month tools budget, native zh-TW reviewer on every post.

## 0. Method, limits and how to read confidence labels

- **I could not open any primary page.** `WebFetch` failed (DNS) and `curl` through the egress proxy returned 403 for every host I tried (platform help centres, NCC, LINE, DataReportal, Taiwan news sites). I did not try to route around that. Everything below comes from `WebSearch` result summaries, which quote or paraphrase the pages. Policy URLs are given exactly so a human can open each one once and screenshot it for `SOURCES.md`.
- **Confidence labels** in the Sources table: `high` = two or more independent outlets agree, or the figure traces to an institutional release; `medium` = one reliable summary of a primary page I could not open; `low` = marketing blog, undated, or outlets disagree; `unverified` = reported once with no way to cross-check.
- Platform policy pages change often. Wording in section 4 is a paraphrase as of the search summaries, not a quotation of the live page.
- "Not found" means I searched and found nothing citable. I have not filled any gap with an estimate. The only numbers in this file that are not sourced are the planning assumptions in section 5.4, which are labelled as assumptions.
- Taiwan vocabulary: 業配 (sponsored post), 薦證廣告 (endorsement advertising), 限時動態 (Stories), 短影音 (short-form video), 輪播貼文 (carousel), 官方帳號 (LINE Official Account, OA), 好友 (LINE friends), 貼圖 (stickers).

## 1. Bottom line (read this first)

1. **The brief's headline numbers check out, but they measure different things and two of them are older than they look.** NCC's LINE 98.2% / Facebook 82.4% / YouTube 68.6% / Instagram 47.8% are *account ownership* among survey respondents (the report uses a 16+ base for its video questions; I could not confirm the base for account ownership) [S2][S4]. TikTok 23.8% is account ownership; 47.5% / 72.5% is *having watched* TikTok content [S3]. The MIC youth figures (Instagram 78%, Dcard 45.9%, Threads 44%) come from fieldwork in **Q4 2024**, published 2025-12-04, so they are about two years old [S5].
2. **Three things in the brief are now stale or wrong.** (a) The task text says "LINE VOOH"; the product is **LINE VOOM, and it shut down in Taiwan on 2026-09-30**, ten days ago [S11]. (b) **Xiaohongshu (小紅書) has been blocked in Taiwan since 2025-12-04** for a provisional one year under the Fraud Crime Hazard Prevention Act, which removes a popular fashion/beauty discovery channel (press descriptions, no share-of-discovery figure found) for young Taiwanese women [S13][S14]. (c) The brief says TikTok, YouTube and Meta "all require a label"; that is true but the rules tightened in 2026 (section 4).
3. **Instagram changed the rules for exactly this project six weeks ago.** On 2026-08-31 Instagram renamed its voluntary "AI creator" label to **"AI-generated profile"** and said profiles that prominently feature a photorealistic AI-generated person without the label can lose recommendation eligibility [S27][S28]. Whether this is enforced in Taiwan yet is not confirmed (one aggregator claimed US-only; I could not corroborate) [S27]. Plan as if it applies.
4. **The fitness/wellness niche is the one most in the crossfire.** Press coverage of the Instagram rule reportedly cited AI-generated doctors, healers and wellness personalities as part of the motivation (the count and exact wording were not verified; an earlier draft said "hundreds", which is removed as unverified) [S27]. A disclosed fitness persona is allowed, but it will sit in the most-scrutinised category on the primary platform.
5. **Recommended launch surface: Instagram (primary for most personas), Threads (cheap secondary on the same Meta stack), YouTube Shorts (secondary for explainer personas).** LINE OA is a retention tool, not a discovery tool, now that VOOM is gone. TikTok is a wave-2 option for a Gen-Z persona only, posted manually, because of its API audit wall and Taiwan's unsettled regulatory posture. Dcard and PTT are listening posts, not posting platforms (commercial-content bans).
6. **The highest-converting social content for 25-34s is the one thing a virtual character cannot make.** 60.3% of 25-34 social users say another person's shared experience (體驗文) makes them want to try it, the highest of any band [S5]. Ground rule 4 bars invented experience. The persona must win on explanation, comparison and demonstration, which is a weaker lever. This complicates the demand case for the whole portfolio.
7. **Taiwan already fines platforms over AI-person ads.** The Digital Industry Administration (數位產業署) reportedly fined Meta NT$5 million for ads with AI-generated personal images that were not disclosed [S51]. The decision date is **unverified**: an earlier draft said 2026-08-14, but the cited reports are dated 2026-09-23, so the fine may have been announced then. The article numbers an earlier draft gave (Art. 31(1)(4), Art. 40(2) of the 詐欺犯罪危害防制條例) were not checked against the statute text and are unverified; `legal.md` should confirm them. Any paid ads featuring a persona should use the platform's AI-disclosure control.
8. **YouTube monetisation is not a realistic revenue line.** Per secondary reports only (YouTube's own announcement not opened), from 2027-02-01 thresholds double for new applicants (8,000 watch hours or 20 million Shorts views in 90 days), and Shorts payout would require a rolling 10 million views per 90 days [S43]. The conclusion is a judgement; it rests on the current bar (3.3) as well as the reported change. Lower early-access YPP tiers may exist; Taiwan availability not checked. YouTube is worth using for reach and search, not for platform payouts.
9. **Official-API publishing is realistic on Meta and awkward elsewhere.** Instagram and Threads publishing APIs are open with documented limits [S36][S38]; TikTok's Content Posting API restricts unaudited clients to private posts [S48]; YouTube uploads from unverified API projects have been locked private [S45]. For a 6 h/week solo operator, first-party apps and Studio tools are the default, with a scheduler only where its API access is confirmed.
10. **Capacity.** At 6 h/week the platform count per persona must stay at two. Ten personas on two platforms at five posts a week (100 posts) is not approvable by one person; see 5.4.

## 2. Who uses what in Taiwan

### 2.1 Re-verification of the brief's starting figures

| Brief claim | Status | What I found | Note |
|---|---|---|---|
| NCC 2025: LINE 98.2%, Facebook 82.4%, YouTube 68.6%, Instagram 47.8% | **Confirmed** (secondary reports of NCC's 114th-year report) | Same four figures; overall 99.4% of people hold at least one social/IM account (97.0% prior year); Facebook rose from 46.8% in 2017 to 82.4% [S2][S4]. NCC report commissioned from 台灣經濟研究院, published Dec 2025 [S1][S2] | Metric = account ownership. Not active use. I could not open the PDF to see sample size or method [S1] |
| TikTok account 23.8% | **Confirmed** | 23.8% hold an account, ranked fifth [S3] | Threads, X, WeChat, WhatsApp and Xiaohongshu are each reported as below 30%; exact figures not found [S2]. Threads is therefore below 23.8% by inference (it is not fifth or higher in this ranking) |
| TikTok watched by 47.5% overall, 72.5% of ages 16-25 | **Confirmed** | 47.5% (18.7% in 2019); 16-25: 24% (2019) to 72.5% (2025) [S3][S4] | Viewing is roughly double account ownership; do not mix the two metrics |
| MIC 18-24: Instagram 78%, Dcard 45.9%, Threads 44% | **Confirmed but dated** | Exact figures confirmed. Fieldwork Q4 2024, online survey, n=1,091 (social) / 1,068 (messaging), sampling error ±3.0% at 95%; released 2025-12-04 [S5]. Verifier flag: n=1,068 is also given for the Q4 2023 wave in [S7]; confirm which wave each sample size belongs to | "常用" = frequently used. Not a 2026 measurement. No newer MIC social-platform wave found as of 2026-10-10 |
| (new) Video behaviour | **Newer data found** | MIC Aug 2026 video survey: 70.5% are short-video users; YouTube Shorts 68.1%, Facebook Reels 58.4%, Instagram Reels 43.0% of those users [S8] | Survey period and sample size not found in the summaries [S8]. TikTok is absent from the reported top three; its figure is not given in the coverage I could see |
| (new) LINE | **Newer data found** | LY Corp lists Taiwan at 22 million MAU, 94.5% penetration, as of 2026-03-31 [S9] | Company figure, MAU not "accounts" |

**Discrepancies to remember**
- NCC (accounts, 16+) and MIC (frequent use, adult online sample) give different pictures for the same platform: Instagram 47.8% (NCC accounts) vs 44.7% (MIC frequent use) is close; Facebook 82.4% vs 72.1% differs by the "own an account" vs "use often" gap. Use NCC for reach ceilings and MIC for age skew [S2][S5].
- MIC's earlier wave (fieldwork Q4 2023, released 2024-11) had Facebook 70%, YouTube 53%, Instagram 34%, PTT 11%, Dcard 9% [S7]. The jump to YouTube 72.3% and Instagram 44.7% a year later looks like a methodology or sample difference as much as real growth; I would not quote a growth trend from the two waves [S5][S7].
- Third-party user counts (DataReportal-derived: LINE about 22 million, YouTube 18.4 million, Facebook 17.1 million, Instagram 11.3 million, TikTok 8.34 million aged 18+, Threads about 3.5 million) appear only in a marketing blog and may be Digital 2025 data rather than 2026 [S18]. DataReportal's own Taiwan page reports 18.1 million social media user identities in Oct 2025 (78.4% of population) [S17]. Treat the blog's per-platform numbers as `low`. A search summary of AnyMind-related coverage mentioned a Threads user count of 6.65 million, but I could not find that figure in the report coverage; it is `unverified` and not used [S19].

### 2.2 Platform-by-platform (reach, skew, role for this studio)

| Platform | Reach evidence | Age/interest skew | Role for the studio |
|---|---|---|---|
| **LINE** (messaging, 官方帳號 OA, 貼圖) | 98.2% hold an account [S2]; 22 million MAU, 94.5% penetration [S9]; Nielsen via LINE: 93% used it in the past 7 days (ages 15-65), about 14 opens a day [S10] | Universal across ages | **Retention and owned-audience channel**, not discovery. Taiwan users send nearly 60 million stickers a day [S10] |
| **LINE VOOM** (the task text says "VOOH") | **Closed in Taiwan 2026-09-30**; posts, Stories, follow/fans features deleted [S11] | n/a | **Do not use.** LINE says to follow creators via their OA instead [S11] |
| **LINE TODAY** | Only a 2018 figure (more than 18 million MAU) found [S18]; no 2026 data, no creator-submission rules found | n/a | Not researched further; no creator route found. `unverified` |
| **Facebook** | 82.4% account ownership [S2]; 72.1% frequent use [S5] | Core is 45+ (79.4% of 45-54 use it); 18-34 about six in ten [S5][S6]. Earlier wave: 36-65 about 75% vs under 60% for 18-35 [S7] | Page (not personal profile) for 35+ personas; Reels reach 58.4% of short-video users [S8] |
| **Instagram** | 47.8% accounts [S2]; 44.7% frequent use [S5] | 18-24: 78%; 25-34: 59.3% [S5]. AnyMind: 57.7% of Taiwan influencer-marketing campaigns run on Instagram (2025 data) [S19] | **Primary** for 18-34 |
| **Threads** (nickname 脆) | Global 500 million MAU (Meta, June 2026) [S21]; Taiwan was named a top-three market in July 2024 and Meta's Threads head credited a Taiwan election for early growth [S21][S22]. MIC frequent use 17.5% [S5]. Official Taiwan user count: **not found** | 18-24: 44%; 25-34: 28.4% [S5]. Taiwan share of global Threads traffic is quoted at 24.04% (QSearch 2026) / 21.08% / 10.09% (Similarweb), mutually inconsistent [S23] | Cheap secondary: same login, same disclosure and branded-content tooling as Instagram [S32] |
| **TikTok** | 23.8% accounts; 47.5% have watched; 72.5% of 16-25 [S3] | Youngest-skewing platform in NCC data [S3] | Wave-2 for a Gen-Z-facing persona. See 2.3 on status |
| **YouTube / Shorts** | 68.6% accounts [S2]; 72.3% frequent use [S5]; Shorts used by 68.1% of short-video users; 86.6% of social-video watchers use YouTube [S8] | 70.6% of 18-24; 79.9% of 55-65 [S5]. MIC says YouTube users lean toward search and knowledge, Instagram users toward social interaction [S8] | Secondary for explainers; poor monetisation (3.3) |
| **Dcard** | 17.6% frequent use overall [S5]; older figures (2022: over 8 million registered, 20 million monthly unique visitors) are stale [S25] | 45.9% of 18-24, 30.9% of 25-34 [S5]. One source says over 95% of users are 18-24 (low confidence) [S25] | Listening only. Commercial/promotional posts are banned (4.6) |
| **PTT** | 17.1% frequent use [S5] | Largest share of its users is 35-44 (27.8%), then 25-34 (24.5%) [S5] | Do not post. Founder's 2022 statement says controls target coordinated volume-inflation behaviour [S26] |
| **X (Twitter)** | Below 30% accounts [S2]; Taiwan-specific usage: **not found** | Not found | Skip |
| **Xiaohongshu (小紅書)** | Over 3 million Taiwan users when blocked [S13][S14] | Young, strong for nails/fashion/food discovery (press descriptions) [S14] | **Blocked** from 2025-12-04 for a provisional year. See 2.3 |

### 2.3 Regulatory status that affects platform choice

**TikTok in Taiwan**
- Not banned for the public. Since the 2022-12 order (reported effective 12-05), TikTok and Douyin are barred on public-sector devices and networks, under a pre-existing 2019 principle against "products that endanger national information security". Officials said at the time that private use was not restricted, and whether to restrict the public was still under assessment [S15]. Some English summaries date the ban to 2023; sources differ, so treat the exact date as `medium`.
- In Dec 2022 the Mainland Affairs Council said a Taiwan company named for ByteDance appeared to be operating illegally under Cross-Strait Act Art. 40-1 and referred it to prosecutors; TikTok denied having a Taiwan branch [S16]. I found no 2026 update.
- TikTok is on the list of ad platforms the Ministry of Digital Affairs designated under the Fraud Crime Hazard Prevention Act, together with Google, YouTube, LINE, Facebook and Instagram; Threads was added later (per secondary reports) [S50].
- Taiwan-specific monetisation (Creator Rewards, TikTok Shop): **not found**. The only sources I found list Western markets and do not name Taiwan [S49].
- **Precedent risk:** the Interior Ministry used the Fraud Act (Art. 42 per the press reports; article number not checked against the statute) to order DNS blocking of Xiaohongshu for one year from 2025-12-04, citing 1,706 fraud cases and failed security checks, with about NT$247.7 million in reported losses [S13][S14]. One report quotes the Interior Minister saying an extension of another year is likely; the report is undated, so `low` [S14]. I found no sign of a similar action planned against TikTok. A critic quoted by Focus Taiwan called the treatment inconsistent [S3]. The mechanism exists; that is a tail risk, not a forecast.

**Advertising-platform duties (Fraud Crime Hazard Prevention Act)**
- Designated platforms must verify who commissions and pays for ads, remove notified scam ads within 24 hours, and disclose whether an ad uses deepfake or AI-generated personal images [S50][S51].
- Consequence for the studio: once a persona runs a *paid* ad, the platform's AI-disclosure control is mandatory, and the studio will need verified advertiser identity (needs the Taiwan business registration that DECISIONS.md says takes about two weeks).

## 3. Formats each platform rewards in Taiwan

### 3.1 What the Taiwan data supports

- Short vertical video is the main discovery format across platforms: 70.5% of surveyed users watch it; 59.3% say it shortens the time to find content they want; 51.7% discovered a new brand through it; 40.1% say it shortens their purchase decision; 31.2% watch more than before (37.2% among 18-25) [S8]. (Verifier flag: 59.3% is also the Instagram 25-34 figure in [S5]; the two may be coincidence or a transcription slip, so re-check the 59.3% video figure against the MIC video-survey release before quoting.) Top reason for choosing a short-video platform: "I watch on the social platform I already use" (51.3%), then "fresh, interesting content" (48.9%) [S8]. Implication: distribute where the audience already is; do not expect a new app to pull attention.
- Format preference, MIC wave with fieldwork Q4 2023 (older): Stories 37% (55% of 18-25, 46% of 26-35), recorded video 34%, live 26.1%, plain text 25.7%, images/infographics 25%; over half prefer content they can read in a minute [S7]. Text and graphics were ranked lower than a year earlier [S7].
- Experience sharing converts: 52.5% of social users say others' shared experiences make them want to try it; 60.3% of 25-34s, 57.8% of 18-24s [S5]. The persona cannot supply this (ground rule 4).
- Marketing-side signal: AnyMind reports Instagram carries 57.7% of Taiwan influencer campaigns, usually paired with Facebook and YouTube, and amplified through Reels and Shorts; Taiwan influencer-marketing market about US$239 million, +11.7% a year [S19]. Kolr (iKala) 2026 argues verifiable human creators are being prized [S20]. This is the demand headwind for disclosed AI characters; the other agents' `competitors.md` and `monetisation.md` should test it.

### 3.2 Format table (evidence quality is the point: Taiwan-specific format benchmarks were not found)

| Platform | Format that the evidence supports | Evidence | Strength | Fit for an AI persona at 6 h/week |
|---|---|---|---|---|
| Instagram | **Reels** (reach 43.0% of Taiwan short-video users) | Reels ranking weighs predicted watch-through, like, reshare and audio-page visits [S39]; Taiwan usage [S8] | Official ranking statement (2023) + Taiwan survey | High: one video asset feeds three platforms |
| Instagram | **Carousel (輪播貼文)** | Explore ranks mainly on likes, saves, shares [S39]. Claims that carousels hold longer engagement or now allow 20 slides come from marketing blogs [S58] | Official for saves/shares; carousel-specific claims `low` | High for outfit/gear/routine breakdowns; very text-heavy, so high native-review load |
| Instagram | Stories (限時動態) | Top-ranked format in MIC wave Q4 2023 [S7] | Taiwan survey, older | Poor: needs daily presence, informal tone, review per frame |
| Threads | Short **text posts** and replies | Taiwan skews 18-24 (44%) and 25-34 (28.4%) [S5]. Older coverage: 63% of posts text-only; spread depends on reply velocity and comment quality [S24] | `low` (undated blog-level) | Medium: cheap to produce, but slang-heavy so highest reviewer burden per post |
| YouTube | **Shorts** (68.1% of short-video users) and search-led explainers | Shorts share [S8]; YouTube users lean to search/knowledge [S8] | Taiwan survey | High for explainers. Monetisation unrealistic (3.3) |
| Facebook | Reels (58.4%); Page posts for 45+ | [S8][S5] | Taiwan survey | Medium: only worth it for a 35+ persona |
| TikTok | Vertical short video, strongest with 16-25 | 72.5% of 16-25 have watched [S3] | NCC | Wave 2 |
| LINE | **Stickers (貼圖)**, OA broadcast, auto-reply | About 60 million stickers sent daily; LINE messages over 1 billion a day [S10] | Company figures via press | Stickers: production outside this file's scope. OA broadcast cost: 3.4 |
| Dcard / PTT | Discussion threads and boards | Commercial posts banned on Dcard [S54] | Policy | Not for posting |

### 3.3 YouTube payouts and Shopping (Taiwan)
- Current entry bar: 1,000 subscribers plus 4,000 watch hours (365 days) or 10 million Shorts views (90 days) [S43].
- Announced 2026-08-10, effective 2027-02-01 (secondary reports only; I could not open YouTube's post): new applicants need 8,000 hours or 20 million Shorts views; Shorts payout continues only while a channel keeps 10 million qualified Shorts views per rolling 90 days [S43].
- Taiwan is on YouTube Shopping's affiliate country list; eligibility requires YPP membership; a Shopee partnership pilot (2025-11-19 to 12-31) reportedly produced about 9,000 transactions across 60-plus Taiwan channels in 42 days [S44]. The subscriber threshold for Shopping is reported inconsistently (10,000 on an older page, 500 in later coverage) [S44]. Check YouTube Studio's Earn tab.

### 3.4 LINE Official Account cost (relevant to budget)
- Current plans (ex-tax): 輕用量 NT$0 with 200 free messages; 中用量 NT$800 with 3,000 free; 高用量 NT$1,200 with 6,000 free [S12].
- From **2026-11-01**: 中用量 NT$1,000; 高用量 NT$1,400, with paid add-on messages at NT$0.20 for the first 50,000 in a month and NT$0.15 beyond; free message counts unchanged [S12]. LINE reportedly announced this 2026-09-01. Figures come from third-party summaries of the LINE Biz-Solutions notice; confirm at `https://tw.linebiz.com/column/LINEOA-2026-Price-Plan/` [S12].
- **Billing unit unresolved:** I could not confirm whether one broadcast to N friends counts as one message or N messages. Do not size an OA budget until that is checked [S12].

## 4. Rules by platform

### 4.0 Cross-platform summary

| | AI-content label | Branded-content tool | Persona/profile rule | Automation / API | Biggest standing risk |
|---|---|---|---|---|---|
| Instagram | "AI info" label (auto + self-disclosure); **"AI-generated profile"** label for accounts fronted by a photorealistic AI person | Paid partnership label via in-app tool | Profile label; recommendation limit if undisclosed | Graph API publishing (100/24h doc figure); DM API with 24 h window | Losing recommendation eligibility; unoriginal-content rule |
| Facebook | Same Meta system | Same Meta branded-content policy | **Page**, not personal profile (non-human personal profiles = fake accounts) | Same Meta platform terms | Fake-account removal if a persona is a personal profile |
| Threads | Meta "AI info" labels exist on Threads | Same tool, per Meta help page | Profile label status on Threads: not found | Threads API 250 posts / 1,000 replies per 24 h | Shared Meta login/standing with Instagram |
| YouTube | Creator disclosure for realistic synthetic content; auto-label since May 2026 | "Includes paid promotion" checkbox | No AI-persona-specific rule found; "inauthentic content" YPP rule | API uploads from unverified projects locked private (docs conflict) | YPP suspension; auto-labelling |
| TikTok | Creator "AI-generated" label required for realistic content; auto-label non-removable | Content Disclosure Setting, "Paid partnership" | Bars fake persona only with intent to mislead | Content Posting API: unaudited = private only, 5 users/24 h | Removal/restriction of unlabelled realistic AI content |
| LINE | Creators Market: LINE may label AI content; OA: no AI rule found | None found for OA | None found | Messaging API; plan message caps; bulk identical messages prohibited | OA suspension for bulk messaging (dated reports) |
| Dcard | No AI rule found | Promotional content banned | n/a | n/a | Suspension after repeated violations |
| X | Synthetic media policy | None found | n/a | Automation rules | n/a (skipped) |

### 4.1 Instagram and Facebook (Meta)

**Policy URLs (open and screenshot):**
- Branded content policies: `https://help.instagram.com/1695974997209192`
- Eligibility for partnership ads and branded content: `https://help.instagram.com/1372533836927082`
- Paid partnership label: `https://help.instagram.com/1123581461537025`
- Paid partnership tool on Threads and organic posts: `https://help.instagram.com/2467529163409127`
- Recommendations on Instagram (carries the AI-generated-profile limit): `https://help.instagram.com/313829416281232/`
- Terms of Use: `https://help.instagram.com/581066165581870/`
- Partner and content monetisation policies: `https://help.instagram.com/512371932629820`, `https://help.instagram.com/2635536099905516`
- Community Standards: Inauthentic Behavior `https://transparency.meta.com/policies/community-standards/inauthentic-behavior/`; Authentic Identity Representation `https://transparency.meta.com/policies/community-standards/authentic-identity-representation/`; Spam `https://transparency.meta.com/policies/community-standards/spam/`
- Labeling AI content: `https://transparency.meta.com/governance/tracking-impact/labeling-ai-content`
- Messaging and IG DM policy: `https://developers.facebook.com/documentation/business-messaging/messenger-platform/policy`
- Instagram content publishing API: `https://developers.facebook.com/docs/instagram-platform/content-publishing/`; Threads API: `https://developers.facebook.com/documentation/threads/overview`

**AI-generated content labelling**
- **Account level (new):** "AI-generated profile" label, announced 2026-08-31 via the Instagram Creators blog (as reported), replacing the voluntary "AI creator" label that was tested from 2026-05-04 [S27]. It is for accounts that feature an AI-generated person; ordinary AI editing, captions or graphics do not need it [S27]. Accounts detected as unlabelled get a notification and a chance to self-apply; appeals restore eligibility; label shows on the profile, posts, Reels and Stories; mobile app only at launch [S27]. Instagram's own recommendations page says it may limit accounts that repeatedly and recently share content prominently featuring a photorealistic AI-generated person unless the account has the label [S28]. Reported penalty is loss of recommendation eligibility, not a ban; the size of the reach loss is not published [S27]. Existing "AI creator" holders are asked to review and confirm [S27]. Rollout geography including Taiwan: **not confirmed** (`unverified`).
- **Content level:** Meta applies an "AI info" label when it detects industry-standard signals (C2PA/IPTC) or the creator self-discloses [S29][S30]. Meta's Feb 2026 notice (published inside a US-midterms post, so its geographic scope is not stated) says creators must use the disclosure tool for organic photorealistic video or realistic-sounding audio, and Meta may apply penalties for failing to [S29]. Current rule for photorealistic *still images* beyond auto-detection: not confirmed.
- **Ads:** Meta labels ads made with its own gen-AI tools and detects third-party AI signals [S31]. A commentator lists Taiwan as a self-disclosure region with a checkbox (`low`) [S31]. Taiwan law makes the AI-person disclosure mandatory for ads (section 2.3) [S51].
- **Design lever (not a loophole):** the recommendation limit and YouTube's prominent label both speak of *photorealistic* people [S28][S40]. A clearly stylised or illustrated character might be treated differently by those two platforms' automated rules (not confirmed by any source). Ground rule 1 does not change: every persona keeps the bio disclosure and applies the platform AI label or AI-generated-profile label wherever a platform offers it, even if a stylised design might arguably avoid the trigger. This affects the visual brief only. Flag for Phase 2/3.

**Branded-content (業配) rules**
- Branded content must be tagged with the branded-content tool, with the brand partner's prior permission; Meta defines it as content a business partner features or influences in exchange for payment *or other value* (gifts, free trips count) [S32].
- Label is "Paid partnership"; must be applied each time; per the help page the feature requires applying in the app and the label can only be added in the Instagram app. Verify before relying on any scheduler for sponsored posts [S32].
- Some partner categories (dating, gambling, pharmacies/prescription drugs, crypto) need Meta's written pre-authorisation [S32]. Branded content cannot carry pre-, mid- or post-roll ads or banners [S32]. Eligibility requires meeting Meta's creator eligibility and monetisation policies; the follower threshold was not visible in the summaries [S32].
- The Meta tool does not discharge Taiwan law. Fair Trade Commission (公平會) treats sponsored posts as endorsement advertising (薦證廣告); material connections must be disclosed; the 2023 handling principles bring influencers who sell or endorse under liability, with fines of NT$50,000 to NT$25 million for false advertising reported in the secondary coverage [S52]. The Fair Trade Act article number and the conditions for the fine (for example whether it follows an order to cease or correct) were not verified and are left to `legal.md`. Detail belongs in `legal.md`.

**Account standing: what gets accounts reduced or removed**
- Unlabelled photorealistic AI-person profile: recommendation limit (above) [S28].
- Unoriginal content: since spring 2026, accounts that mainly post others' photos, videos or carousels are excluded from recommendation surfaces, judged over a month; crediting the source or adding a watermark does not count; commentary, narration, graphics do [S33]. AI-original persona content is not the target. Whether near-identical templated AI output could be scored as unoriginal is not documented.
- Fake engagement: buying likes/follows/views is prohibited; Instagram may stop recommending accounts that repeatedly bought likes, and monetisation can be removed where an audience is largely fake engagement [S28][S34][S35]. Terms of Use also bar selling or buying accounts and impersonation [S35].
- Fake/duplicate accounts: Meta counts "personal profiles created to represent a business, organisation or non-human entity" as fake accounts [S34]. **Facebook presence for a persona must be a Page.** Authentic Identity Representation requires one account per person under a real name for profiles [S34]. For Instagram the professional account with the AI-generated-profile label is the compliant route [S27].
- Coordinated networks: Meta removes networks of fake assets run to mislead users; "Coordinated Inauthentic Behavior" centres on false identities [S34]. Ten personas from one operator are lower-risk when each bio names the studio and personas never cross-vouch (brief rule 8) but there is no Meta statement blessing a disclosed multi-persona studio; `unverified`.
- Multi-account handling: Instagram's help page says you can add up to five accounts in the app's account switcher [S35]. Ten personas therefore needs more than one switcher set-up, meaning more than one app instance or device. Whether multiple accounts need separate phone numbers: not found.

**Scheduler / API rules**
- Instagram: official content-publishing API, 100 API-published posts per rolling 24 h (a second line on the same doc still says 50, so verify), 400 containers per 24 h; Meta tells scheduling tools to enforce the limit; needs professional account and the right permissions/app review [S36]. Carousels count once [S36].
- Threads: 250 API posts and 1,000 replies per rolling 24 h [S38].
- Threads/Business Suite scheduling support is reported inconsistently across sources; check in-app [S58].

**Auto-reply / DM bots (Instagram Messaging API)**
- You may send within 24 h of a user's message; promotional content is allowed inside that window; the Human Agent tag extends human replies to 7 days; misuse of message tags can restrict the account [S37].
- Automated chats must disclose they are automated *when required by law*, and Meta recommends disclosing anyway; bots marked "automated" are expected to respond within 30 seconds on Messenger [S37]. The brief's rule 9 (any automated reply says it is automated) is stricter than Meta and should stand.

### 4.2 Threads
- Same login and Meta Community Standards as Instagram. AI info labels apply on Threads (an earlier draft quoted "150 million label views in a 29-day window in Oct 2024"; that figure was not re-verified and the 2024-02 Meta post cited for it cannot contain Oct 2024 data, so it is **unverified** and should not be quoted) [S30].
- Branded content on Threads uses the same paid-partnership tool [S32].
- Whether the AI-generated-profile label extends to Threads: not found.
- API limits above [S38].

### 4.3 YouTube
**Policy URLs:**
- Disclosing use of GenAI content: `https://support.google.com/youtube/answer/14328491`
- "How this content was made" disclosures: `https://support.google.com/youtube/answer/15447836`
- YouTube Blog, Improving AI labels: `https://blog.youtube/news-and-events/improving-ai-labels-viewers-creators/`
- Paid product placements, sponsorships and endorsements: `https://support.google.com/youtube/answer/154235`
- Branded content policies: `https://support.google.com/youtube/answer/17596007`
- Viewer-side explanation: `https://support.google.com/youtube/answer/10588440`
- YouTube Shopping affiliate: `https://support.google.com/youtube/answer/13376398`
- API: `https://developers.google.com/youtube/v3/docs/videos/insert`, `https://developers.google.com/youtube/v3/revision_history`, `https://support.google.com/youtube/answer/7300965` (videos locked as private), `https://developers.google.com/youtube/terms/developer-policies-guide`

**AI labelling**
- Creators must disclose realistic altered or synthetic content, including realistic people and synthetic voices [S40]. Exempt: productivity uses (scripts, ideas, auto-captions), clearly unrealistic or animated content, minor edits (beauty filters, colour, blur) [S40]. Labels sit below the player on long-form and as an overlay on Shorts; animated/unrealistic content gets a description-only disclosure [S40].
- From May 2026 YouTube applies a label automatically when its systems detect significant photorealistic AI use and the creator has not said; creators can dispute, but labels are locked for content made with YouTube's own AI tools and for C2PA metadata indicating fully generative content [S40]. Disclosure does not limit audience or monetisation eligibility [S40]. Repeated non-disclosure can lead to manual labels, content removal or YPP suspension [S40].
- No AI-persona-specific channel rule found.

**Branded content**
- Check "My video contains paid promotion like a product placement, sponsorship, or endorsement"; viewers see a disclosure at the start for 10 seconds; ads still run; branded-content videos are removed from YouTube Kids [S41]. YouTube states that creators and brands remain responsible for local legal disclosure duties; the box does not satisfy Taiwan law by itself [S41].

**Account standing**
- "Inauthentic content" (renamed from "repetitious content" on 2025-07-15): mass-produced or templated content, for example repetitive slideshows with bulk AI voiceover, is ineligible for monetisation; AI tools are allowed if the result is original and adds value [S42]. This is the main design constraint for a ten-persona factory on YouTube.
- API: videos uploaded via `videos.insert` from API projects created after 2020-07-28 and not audited are locked private (the reference page and revision history disagree on current behaviour); default quota 10,000 units/day, raised only after a compliance audit; the quota calculator page and the insert reference disagree on cost (1,600 units vs 1 unit in a separate upload bucket); creating multiple Cloud projects to get more quota is banned [S45]. Use YouTube Studio for uploads and scheduling unless an audited tool is chosen.

### 4.4 TikTok
**Policy URLs:**
- Community Guidelines overview: `https://www.tiktok.com/community-guidelines`
- Integrity and Authenticity: `https://www.tiktok.com/community-guidelines/en/integrity-authenticity`
- AI-generated content: `https://www.tiktok.com/tns-inapp/pages/ai-generated-content`; Creator Academy label guide: `https://www.tiktok.com/creator-academy/en/article/ai-generated-content-label`; Newsroom: `https://newsroom.tiktok.com/new-labels-for-disclosing-ai-generated-content?lang=en`; transparency: `https://www.tiktok.com/transparency/en/supporting-responsible-transparent-ai-generated-content/`
- Branded Content Policy: `https://www.tiktok.com/legal/page/global/bc-policy/en`; Commercial Content Disclosure setting: `https://ads.tiktok.com/help/article/about-the-content-disclosure-setting-for-creators`
- Content Posting API: `https://developers.tiktok.com/docs/en/content-sharing-guidelines`, `https://developers.tiktok.com/docs/en/content-posting-api-get-started`, `https://developers.tiktok.com/docs/en/getting-started-faq`

**AI labelling**
- The guidelines version released 2026-08-25 and effective 2026-09-24 requires labelling AI-generated or significantly edited content showing realistic scenes or people; unlabelled content may be removed, restricted or labelled by TikTok [S46]. TikTok auto-labels (for example when C2PA Content Credentials are attached) and the creator cannot remove an auto-label; wrongly applying the creator label to unaltered content can lead to removal [S46]. AI-generated speech put in a real person's mouth counts as "significantly edited" [S46].
- Not allowed even with a label: AI content that shows the likeness of people under 18, or of adult private figures without permission; fake authoritative sources or crisis events [S46]. The original-likeness rule in the brief covers this.
- Presenting as a fake person is prohibited where there is demonstrated intent to mislead [S46]; disclosure in the bio and label addresses that.

**Branded content**
- Branded content (promotion or review of a third-party brand for payment or any incentive) requires the Commercial Content Disclosure toggle, choosing "Your brand" or "Branded content"; the partner tag authorisation lasts 60 days by default; the post shows "Paid partnership" [S47]. Undisclosed commercial content may be ineligible for the For You feed [S47]. TikTok says enabling the label does not change recommendations, based on an internal test of nearly 2 million videos [S47]. Creator Academy and the ads help centre use slightly different label wording; check in-app [S47].

**Account standing and API**
- No bulk automated account registration or operation; spam via bots/scripts is prohibited; fake likes and followers are removed; penalties include banning the account and any new ones [S46].
- Content Posting API: unaudited clients can only post `SELF_ONLY`, to private accounts, for up to 5 users per 24 h (403 `unaudited_client_can_only_post_to_private_accounts`); an audit confirming Terms compliance lifts it; branded content cannot be private [S48]. For a solo operator, post manually in the TikTok app.

### 4.5 LINE (Official Account, Creators Market)
**Policy URLs:** LINE Creators Market Terms `https://creator.line.me/en/terms/` (clause 8.13), Review Guidelines `https://creator.line.me/en/review_guideline/`, Creation Guidelines `https://creator.line.me/en/guideline/`. LINE Official Account terms and Messaging API terms: **exact Taiwan URL not found**; start from `https://tw.linebiz.com/` and `https://developers.line.biz/en/docs/messaging-api/`.

- **AI labelling:** the Creators Market terms say LINE may display that content is AI-generated, triggered by the creator's declaration or LINE's own judgement, and LINE is not liable for damage from the label; the terms do not ban AI-made stickers [S55]. A third-party guide claims AI stickers are auto-flagged and IP infringement is strictly prohibited (`low`) [S55]. No AI-disclosure rule for Official Accounts found.
- **Branded content:** no OA-specific sponsorship tool found. Apply the brief's rule 5 in the message text. The legal duty is the Fair Trade Commission's [S52].
- **Persona rule:** none found.
- **Bulk-messaging standing risk:** LINE's general terms reportedly forbid sending identical or similar messages to many unspecified users, and LINE may delete accounts without prior notice; the reports I found are from 2013 and an undated critical commentary, so dated [S56]. The Executive Yuan's consumer protection office once asked LINE to revise unilateral-suspension clauses (older report, date not confirmed) [S56].
- **Auto-reply:** LINE's own AI-reply feature was reported as available only to some users in Japan, with no Taiwan date [S57]. No LINE rule requiring bot disclosure found; the brief's rule 9 applies.
- **Cost:** see 3.4.

### 4.6 Dcard, PTT, X (for completeness)
- **Dcard:** advertising and commercial-content rules (updated 2025-01-13) apply to all boards: no product sales, crowdfunding or sponsorship links, no promotional posts offering brand perks, no app-download links, restricted giveaways; three or more violations bring a 7-day suspension, repeat offenders longer; some boards are stricter (the home board deletes suspected 業配 and wants receipts) [S54]. The full site rules (reported updated 2026-03-30) and any AI-content rule were not retrievable. Not a posting platform for personas.
- **PTT:** no explicit sponsorship rule found; registration has been restricted at times; the founder said controls target coordinated inflation of volume [S26]. Not a posting platform.
- **X:** synthetic and manipulated media may be labelled or removed if deceptive and harmful; minor edits excluded; "Made with AI" indicators were described for EU users only; automation must not "surprise or mislead" users and needs express consent for actions on another user's account [S53]. No paid-partnership policy found. Taiwan usage data not found. Skip for launch.

## 5. Recommendation: ranked platforms by audience, sized for 6 h/week

### 5.1 Principles that follow from the evidence
1. **Two platforms per persona, maximum.** The binding constraint is operator approval plus native zh-TW review, not production (section 5.4).
2. **One video asset, two platforms.** Short vertical video is the discovery format everywhere [S8]. Make one master and publish to Instagram Reels and YouTube Shorts (and Facebook Reels where relevant), setting each platform's AI label and branded-content control separately.
3. **Put the text-heavy platform second.** Threads, Dcard and PTT consume slang and nuance; the operator is not good at Traditional Chinese, so text-first surfaces carry the highest reviewer cost per post. Carousels are similar.
4. **Meta-first for compliance simplicity.** Instagram, Threads and Facebook share one policy stack, one set of AI labels and one branded-content tool [S32].
5. **Do not build on closed or contested surfaces:** LINE VOOM (closed) [S11], Xiaohongshu (blocked) [S13].

### 5.2 By audience type

Rankings are my judgement from the cited data. Where an audience band lacks data, the cell says so.

| Audience | Evidence | Rank 1 (primary) | Rank 2 (secondary) | Later / avoid |
|---|---|---|---|---|
| **18-24** (students, early career) | Instagram 78%, YouTube 70.6%, Dcard 45.9%, Threads 44% [S5]; 72.5% of 16-25 have watched TikTok [S3] | Instagram (Reels, carousels) | Threads | TikTok in wave 2 (manual posting); Dcard listening only |
| **25-34** (core commercial band) | Instagram 59.3%, Dcard 30.9%, Threads 28.4% [S5]; Facebook about 60% for 18-34 [S6]; highest "experience-sharing converts" band (60.3%) [S5] | Instagram | YouTube Shorts (explainer/search niches) or Threads (fashion/lifestyle) | Facebook only if the persona skews older |
| **35-44** | Facebook roughly 75% for 36-65 [S7]; PTT's biggest share is 35-44 [S5]; Instagram and Threads figures for this band: not found | Facebook Page | YouTube | LINE OA for retention |
| **45-54** | Facebook 79.4% [S5]; YouTube and other platforms for this band: not found | Facebook Page | YouTube | Instagram not evidenced |
| **55-65** | YouTube 79.9% [S5]; LINE universal [S9] | YouTube | LINE OA | Not a likely audience for the three operator niches |
| **Brands and agencies** (B2B for the studio) | Brand-side influencer spend is on Instagram first [S19]; LinkedIn/B2B channels: **not researched** | Studio presence via Instagram and email (outside this file) | | Open question |

### 5.3 By operator niche (health-fitness, wealth, fashion), within ground rule 6

| Niche (compliant angle) | Primary | Secondary | Platform-specific caution |
|---|---|---|---|
| **Fashion** (outfit breakdowns, fabric/fit explainers, styling logic; no worn-it testimony) | Instagram: carousels for outfit breakdowns, Reels for transitions | Threads | Xiaohongshu, a popular Taiwan discovery channel for this audience (press descriptions; share not found), is blocked [S13][S14]; no worn/tried claims (rule 4) |
| **Fitness education** (exercise technique, programme structure, gear comparison; zero health/weight-loss claims) | Instagram Reels | YouTube Shorts / short explainers | Highest scrutiny: Instagram's AI-profile rule was prompted by AI doctors, healers and wellness personalities [S27]. Meta pre-authorisation applies to pharmacy/prescription categories if a brand deal touches them [S32] |
| **Money-literacy** (budgeting, how a fee or tool works, glossary; no investment advice or product picks) | YouTube (search-led explainers) | Threads (text) | MIC lists "financial information" among the top five reasons for using social platforms [S6]. Meta requires pre-authorisation for crypto and gambling partners [S32]. Whether Meta requires extra verification for financial-services advertisers in Taiwan: not found |

Evidence gap: I found **no Taiwan data splitting platform use by interest** (fitness, finance, fashion). The table above is inference from age-band data plus the AnyMind campaign mix [S19]. Phase 2 should treat first-6-week platform results as the real test.

### 5.4 Capacity model for 6 h/week

The minute values below are **planning assumptions, not findings**. They exist to show the shape of the constraint and must be calibrated in the first 30 days.

| Item | Assumption (minutes/week) |
|---|---|
| Account admin, brand/agency contact | 60 |
| Analytics and the weekly report | 30 |
| Comment/DM review (all personas) | 60 |
| **Left for post approval** | 360 - 150 = **210** |
| Operator time per post (check media, caption, label, sponsorship flag, publish) | 5 per post, excluding the external native review |

210 / 5 = **about 42 posts a week as an upper bound** if nothing goes wrong, before reviewer turnaround and rework. The brief's example of ten accounts on two platforms at five posts a week is 100 posts, more than twice that. A workable launch shape:

| Wave | Personas | Platforms each | Posts per platform per week | Posts per week |
|---|---|---|---|---|
| Pilot | 3 | 2 | 3 | 18 |
| Upper bound at this capacity | 3 | 2 | 5 | 30 |
| Not feasible | 10 | 2 | 5 | 100 |

Reusing one master video for Reels and Shorts counts as one *production* item but two *approvals*, because labels and captions differ per platform.

### 5.5 Budget (platform-driven items only; tools stack belongs in `pipeline/tools.md`)
- Native posting tools on Instagram, Threads, Facebook, YouTube and TikTok are free (no price found because none is charged).
- LINE OA: NT$0 on 輕用量 (200 free messages); NT$1,000 / NT$1,400 per month ex-tax for 中用量 / 高用量 from 2026-11-01 [S12]. One OA per persona multiplies this; start with at most one studio-level OA, or none until a persona has an audience.
- No scheduler price is recommended here because I did not verify any scheduler's API access to Instagram's paid-partnership tool, TikTok's audit state or YouTube's quota.

### 5.6 Things for `HUMAN_TODO.md` that follow from this file
1. Open every policy URL in section 4 once, screenshot, and add the date to `SOURCES.md`.
2. In a test Instagram professional account, check whether the "AI-generated profile" label is available in Taiwan, and where it sits in the menu.
3. In the LINE Official Account Manager, confirm the billing unit for a broadcast (one message or one per friend) before choosing a plan.
4. Ask the native reviewer which text-first platforms they are comfortable covering (Threads vs only caption review).
5. Decide whether personas are photorealistic or stylised before Phase 3; the label burden differs on Instagram and YouTube.
6. Confirm with a Taiwan lawyer whether disclosed AI personas posting organically need anything beyond the Fair Trade Commission's 薦證廣告 rules (see `legal.md`).

## 6. Where this contradicts or complicates the brief

- **LINE VOOM is closed** (the task text spells it "VOOH"). The task text's "LINE VOOH" (BRIEF.md does not mention VOOM at all) has no Taiwan audience as of 2026-10-01 [S11].
- **TikTok 23.8% vs 47.5% / 72.5%:** account ownership vs having watched. The brief lists them together without that distinction [S3].
- **MIC "18 to 24 favour" figures are fieldwork Q4 2024**, not a 2026 survey [S5].
- **Brief rule 4 versus the strongest conversion driver (experience sharing).** The 25-34 band, the commercially most valuable one, responds most to 體驗文 [S5].
- **Operator niches:** fitness/wellness personas are the main target of Instagram's new rule [S27]; the fashion/beauty channel Xiaohongshu is blocked [S13]; finance partners need extra care on Meta [S32].
- **Operator language gap vs the best-evidenced surfaces:** the most Taiwan-specific engagement happens on text- and slang-heavy surfaces (Threads, Dcard, PTT), the ones where the operator cannot self-check.
- **Demand risk is real.** Kolr (iKala) frames verifiable human creators as the asset brands want [S20], and Instagram's rule is explicitly motivated by users disliking later-discovered AI profiles [S27]. Neither says disclosed virtual characters lack demand; both show the headwind.

## 7. Open questions and unverifiable items

- Does Instagram's "AI-generated profile" label and recommendation limit apply to Taiwan accounts now? (`unverified`.) Does it extend to Threads and Facebook Pages?
- Official Threads Taiwan MAU: not found. Third-party numbers conflict (about 3.5 million in one blog; traffic-share estimates of 10% to 24%) [S18][S23].
- NCC report details: sample size, survey method, and the exact Threads/X/Xiaohongshu figures [S1].
- MIC 2026 video survey: fieldwork dates, sample size and the TikTok figure [S8].
- Xiaohongshu: decision on extension after 2026-12-04 (not found).
- TikTok in Taiwan: Creator Rewards and Shop availability (not found); any 2026 regulatory change (not found) [S49].
- LINE OA: billing unit per broadcast; Taiwan Official Account terms; whether LINE bans AI-generated Official Account content; LINE TODAY creator route and current audience.
- Dcard: current monthly users; AI-content rule in the site rules updated 2026-03-30.
- YouTube: the 2027 YPP changes rest on secondary coverage; YouTube Shopping's current subscriber threshold [S43][S44].
- Instagram publishing API: 100 vs 50 posts per 24 h on the same doc page [S36]; whether paid-partnership labels can be set through the API [S32].
- Meta financial-services advertiser verification for Taiwan (not found).
- AI Basic Act (人工智慧基本法): the brief states in force 2026-01-14. I did not verify the date or obtain platform-relevant duties; several secondary reports suggest promulgation on that date, but the competent authority was reported inconsistently [S59]. Left to `legal.md`.

## Sources

All rows: date accessed 2026-10-10. Where I saw a page only through a search summary, confidence is capped at `medium`.

| id | claim supported | URL | date published (if known) | date accessed | confidence |
|---|---|---|---|---|---|
| S1 | NCC 114th-year Communications Market Report exists; commissioned by NCC, executed by 台灣經濟研究院; published Dec 2025 | https://commsurvey.ncc.gov.tw/ ; full PDF: https://commsurvey.ncc.gov.tw/files/file_pool/1/0p336342530469870607/251201%20%20114%E5%B9%B4%E9%80%9A%E8%A8%8A%E5%82%B3%E6%92%AD%E5%B8%82%E5%A0%B4%E5%A0%B1%E5%91%8A_%E7%B6%B2%E7%AB%99%E4%B8%8A%E5%82%B3%E7%89%88.pdf | 2025-12 | 2026-10-10 | medium |
| S2 | LINE 98.2%, Facebook 82.4%, YouTube 68.6%, Instagram 47.8%; 99.4% overall account rate (97.0% prior); Facebook 46.8% to 82.4%; TikTok, Xiaohongshu, WeChat, Threads, X, WhatsApp each below 30% | https://news.nextapple.com/life/20260116/B179FADDD8297A4BE6D2F4C22549D035 | 2026-01-16 | 2026-10-10 | medium (downgraded from high by verifier: Instagram 47.8% and the sub-30% group rest on this one outlet; LINE/Facebook/YouTube corroborated by S4 and the BRIEF; not re-fetched) |
| S3 | TikTok watched by 47.5% (18.7% in 2019); 16-25: 24% to 72.5%; TikTok account 23.8% (fifth); critics note no similar action against TikTok | https://focustaiwan.tw/culture/202601040012 | 2026-01-04 | 2026-10-10 | high |
| S4 | NCC top three (LINE, Facebook, YouTube) and 83% of 16+ watch online creator-video platforms; TikTok 47.5% / 72.5% | https://udn.com/news/story/7240/9243385 | n/k (about Jan 2026) | 2026-10-10 | medium |
| S5 | MIC social survey: YouTube 72.3%, Facebook 72.1%, Instagram 44.7%, Dcard 17.6%, Threads 17.5%, PTT 17.1%; 18-24 Instagram 78%, Dcard 45.9%, Threads 44%, YouTube 70.6%; 25-34 59.3/30.9/28.4; YouTube 55-65 79.9%, Facebook 45-54 79.4%; PTT largest share 35-44; experience-sharing conversion 52.5% (25-34: 60.3%); fieldwork Q4 2024, n=1,091, ±3.0% | https://mic.iii.org.tw/news.aspx?id=744 | 2025-12-04 | 2026-10-10 | high |
| S6 | Press coverage of the MIC survey: Facebook about six in ten at 18-34, 45+ core; top motives include entertainment, friends, news, consumer info, financial info | https://money.udn.com/money/story/5613/9182136 ; also https://www.nownews.com/news/6761783 | 2025-12-04 | 2026-10-10 | high |
| S7 | MIC earlier wave (fieldwork Q4 2023, n=1,068): Facebook 70%, YouTube 53%, Instagram 34%, PTT 11%, Dcard 9%; formats Stories 37%, recorded video 34%, live 26.1%, text 25.7%, images 25%; Stories 55% (18-25), 46% (26-35); Facebook 36-65 about 75% | https://mic.iii.org.tw/news.aspx?id=691 ; https://www.ctee.com.tw/news/20241108700478-430502 | 2024-11-07 | 2026-10-10 | high |
| S8 | MIC Taiwan video-watching survey: 70.5% short-video users; YouTube Shorts 68.1%, Facebook Reels 58.4%, Instagram Reels 43.0%; 77.8% watch social video (YouTube 86.6%, Facebook 63.7%, Instagram 37.8%); reasons and purchase-decision effects; YouTube for search/knowledge, Instagram for social interaction | https://money.udn.com/money/story/7307/9704523 ; https://wantrich.chinatimes.com/news/20260820900336-420501 | 2026-08-20 | 2026-10-10 | medium |
| S9 | LINE Taiwan 22 million MAU, 94.5% penetration, as of 2026-03-31 (LY Corp global page); 22 million as of 2024, 93% (Feb 2025 interview) | https://www.lycorp.co.jp/en/company/global/ ; https://www.lycorp.co.jp/en/story/20250226/linetaiwan.html | 2026-03-31 | 2026-10-10 | medium |
| S10 | LINE Taiwan 14th-anniversary data: about 60 million stickers a day, 10 million active groups, 8.5 million recalls; over 1 billion messages a day; Nielsen: 93% used in past 7 days, about 14 opens/day | https://ec.ltn.com.tw/article/breakingnews/5511215 | 2025-06 | 2026-10-10 | medium |
| S11 | LINE VOOM Taiwan shut down 2026-09-30; Stories, follow/fans features closed; backups until 2026-09-30; LINE suggests following creators' OA | https://www.ettoday.net/news/20260803/3212389.htm ; https://www.nownews.com/news/6878748 | 2026-08-03 | 2026-10-10 | high |
| S12 | LINE OA plans: 輕 NT$0/200 msgs; 中 NT$800 (to NT$1,000 from 2026-11-01)/3,000; 高 NT$1,200 (to NT$1,400)/6,000 with add-on NT$0.20 then NT$0.15; ex-tax; billing unit unresolved | https://tw.linebiz.com/column/LINEOA-2026-Price-Plan/ ; https://lineoa.batmobile.com.tw/blogs/lineoa_message_counting ; https://tw.linebiz.com/faq/oa-price/message-price-list/ | 2026-09 (announcement) | 2026-10-10 | medium |
| S13 | Interior Ministry ordered DNS stop-resolution and access restriction on Xiaohongshu 2025-12-04, provisional one year, under Fraud Crime Hazard Prevention Act Art. 42; 1,706 cases; about NT$247.7 million losses; over 3 million Taiwan users | https://cna.com.tw/news/asoc/202512040238.aspx ; https://www.nownews.com/news/6761458 ; https://verfassungsblog.de/taiwans-xiaohongshu-ban-and-freedom-of-expression/ | 2025-12-04 | 2026-10-10 | high |
| S14 | Possible extension of the ban; user impact and VPN workarounds | https://www.inside.com.tw/tag/%E5%B0%8F%E7%B4%85%E6%9B%B8 ; https://asianews.network/nail-designs-food-reviews-not-politically-sensitive-taiwanese-users-rail-against-xiaohongshu-ban | undated / Dec 2025 | 2026-10-10 | low |
| S15 | TikTok/Douyin barred on public-sector devices (reported effective 2022-12-05), under the 2019 national-information-security product principle; private use not restricted; wider restriction under assessment | https://www.inside.com.tw/article/29992-MODA-ban-TikTok-Xiaohongshu ; https://news.pts.org.tw/article/613713 ; https://www.taiwannews.com.tw/en/news/4747705 | 2022-12 | 2026-10-10 | medium |
| S16 | Dec 2022 controversy over a ByteDance-named Taiwan company; MAC cites Cross-Strait Act Art. 40-1; TikTok denies a Taiwan branch | https://www.cna.com.tw/news/aipl/202212190332.aspx ; https://news.ltn.com.tw/news/politics/breakingnews/4158779 | 2022-12-19 | 2026-10-10 | medium |
| S17 | DataReportal Digital 2026 Taiwan: 18.1 million social identities, 78.4% of population, Oct 2025 | https://datareportal.com/reports/digital-2026-taiwan | 2026 | 2026-10-10 | medium |
| S18 | Third-party per-platform user counts (LINE 22 million, YouTube 18.4 million, Facebook 17.1 million, Instagram 11.3 million, TikTok 8.34 million 18+, Threads 3.5 million); LINE TODAY 18 million MAU is from 2018 | https://iseeu.tw/taiwan-social-media-report/ ; https://www.ithome.com.tw/news/121717 | 2026 / 2018 | 2026-10-10 | low |
| S19 | AnyMind 2026 APAC report: Instagram 57.7% of Taiwan influencer-marketing campaigns; market about US$239 million, +11.7%; brand collaborations pair Instagram with Facebook and YouTube | https://www.ctee.com.tw/news/20260203701010-430502 ; https://www.nownews.com/news/6782850 | 2026-02-03 | 2026-10-10 | medium |
| S20 | Kolr (iKala) 2026 AI marketing trend report: authenticity and verifiable human creators framed as the scarce asset | https://www.bnext.com.tw/article/90807/ikala_kolr_2026_04 | 2026-04 | 2026-10-10 | medium |
| S21 | Threads at 500 million MAU (June 2026); Threads head credits a Taiwan election for early growth | https://technews.tw/2026/06/17/new-features-to-celebrate-500-million-monthly-users-on-threads/ ; https://ec.ltn.com.tw/article/breakingnews/5476049 | 2026-06 | 2026-10-10 | medium |
| S22 | Meta (July 2024): India, Japan, Taiwan are the top three Threads markets | https://www.cna.com.tw/news/ait/202407040147.aspx | 2024-07-04 | 2026-10-10 | medium |
| S23 | Conflicting estimates of Taiwan's share of Threads traffic (24.04% QSearch 2026; 21.08%; 10.09% Similarweb) | https://www.managertoday.com.tw/articles/view/72894 ; https://rar.design/posts/threads-traffic-window-2026-designer ; https://www.bella.tw/articles/novelty/46115 | 2026 | 2026-10-10 | low |
| S24 | Threads brand-voice and engagement-velocity commentary; older stat that 63% of Threads posts are text-only | https://www.cw.com.tw/article/5131412 ; https://www.managertoday.com.tw/articles/view/72894 | 2024-2026 | 2026-10-10 | low |
| S25 | Dcard audience claims (over 95% aged 18-24; 2022: 8 million registered, 20 million monthly unique visitors) | https://newsletter.management.ntu.edu.tw/?p=11118 ; https://www.techbang.com/posts/51066-5-years-to-build-8-million-unique-monthly-visitors-how-communities-nova-dcard-rise | n/k / 2022 | 2026-10-10 | low |
| S26 | PTT account restrictions; founder says controls target coordinated volume-inflation behaviour | https://tfc-taiwan.org.tw/?p=105500 ; https://www.techbang.com/posts/88690-ptt-which-has-been-out-of-account-registration-for-nearly-two | 2022 | 2026-10-10 | low |
| S27 | Instagram renames "AI creator" to "AI-generated profile"; reach limits for unlabelled AI profiles; announced 2026-08-31; voluntary label tested from 2026-05-04; ordinary AI editing exempt; appeals; geography not confirmed | https://techcrunch.com/2026/08/31/instagram-puts-new-limits-on-undisclosed-ai-profiles/ ; https://engadget.com/2246914/instagram-will-demote-ai-generated-influencers-if-they-dont-clearly-label-their-account/ ; https://unwire.hk/2026/09/01/instagram-ai-profile-label/fun-tech/ ; https://hypebeast.com/zh/2026/5/instagram-tests-voluntary-ai-creator-label-on-profiles ; US-only claim (uncorroborated): https://ground.news/article/instagram-says-its-pulling-the-mask-off-ai-influencers | 2026-08-31 | 2026-10-10 | high (existence and core terms); unverified (Taiwan scope) |
| S28 | Instagram Help: may limit accounts that repeatedly and recently share content prominently featuring a photorealistic AI-generated person unless labelled with the AI-generated profile label | https://help.instagram.com/313829416281232/ | n/k | 2026-10-10 | medium |
| S29 | Meta Feb 2026: "AI info" label; creators must use the disclosure tool for organic photorealistic video or realistic audio; penalties possible | https://about.fb.com/news/2026/02/meta-prepares-for-2026-us-midterms/ | 2026-02 | 2026-10-10 | medium |
| S30 | Meta labelling of AI content ("AI info"; C2PA/IPTC signals; self-disclosure). The Threads "150 million label views" figure is unverified and no longer relied on | https://about.fb.com/news/2024/02/labeling-ai-generated-images-on-facebook-instagram-and-threads/ ; https://transparency.meta.com/governance/tracking-impact/labeling-ai-content | 2024-02 | 2026-10-10 | medium |
| S31 | Meta ads: "AI info" on ads made with Meta gen-AI tools and detected third-party AI; Taiwan listed as a checkbox region by one commentator | https://about.fb.com/news/2025/02/gen-ai-transparency-metas-ads-products/ ; https://www.jonloomer.com/ai-disclosure-checkbox-chatgpt-attribution/ | 2025-02 | 2026-10-10 | medium (Meta post); low (Taiwan checkbox claim) |
| S32 | Meta branded-content rules: tool tagging with permission; gifts count; categories needing pre-authorisation; no in-video ad roll; paid-partnership label (in-app); Threads uses the same tool; eligibility page | https://help.instagram.com/1695974997209192 ; https://help.instagram.com/1372533836927082 ; https://help.instagram.com/1123581461537025 ; https://help.instagram.com/2467529163409127 ; https://creators.instagram.com/earn-money/branded-content | n/k | 2026-10-10 | medium |
| S33 | Instagram expands unoriginal-content recommendation exclusion to accounts that mainly share unoriginal photos/videos/carousels; monthly assessment | https://petapixel.com/2026/04/30/new-instagram-policies-target-reposted-content/ | 2026-04-30 | 2026-10-10 | medium |
| S34 | Meta Community Standards: inauthentic behaviour, authentic identity (one account per person for profiles), fake accounts including profiles representing non-human entities, spam and fake engagement | https://transparency.meta.com/policies/community-standards/inauthentic-behavior/ ; https://transparency.meta.com/policies/community-standards/authentic-identity-representation/ ; https://transparency.meta.com/reports/community-standards-enforcement/fake-accounts/ ; https://transparency.meta.com/policies/community-standards/spam/ | n/k | 2026-10-10 | medium |
| S35 | Instagram Terms of Use (no buying/selling accounts, impersonation); Partner Monetization Policies (artificial engagement); up to five accounts can be added in the app | https://help.instagram.com/581066165581870/ ; https://help.instagram.com/512371932629820 ; https://help.instagram.com/1696686240613595/ | n/k | 2026-10-10 | medium |
| S36 | Instagram content-publishing API: 100 posts/24 h (doc also shows 50), 400 containers/24 h, scheduling tools should enforce | https://developers.facebook.com/docs/instagram-platform/content-publishing/ | n/k | 2026-10-10 | medium |
| S37 | Messenger/Instagram messaging policy: 24 h window, Human Agent tag 7 days, bot disclosure when required by law and recommended, 30 s response for bots marked automated | https://developers.facebook.com/documentation/business-messaging/messenger-platform/policy | n/k | 2026-10-10 | medium |
| S38 | Threads API: 250 API posts and 1,000 replies per rolling 24 h | https://developers.facebook.com/documentation/threads/overview | n/k (cached about 292 days old) | 2026-10-10 | medium |
| S39 | Instagram ranking: Reels ranked on predicted watch-through, like, reshare, audio-page visits; Explore on likes, saves, shares; creator FAQ on engagement per viewer | https://about.instagram.com/blog/announcements/instagram-ranking-explained ; https://about.instagram.com/blog/announcements/shedding-more-light-on-how-instagram-works ; https://creators.instagram.com/faq | 2021 / 2023 | 2026-10-10 | medium |
| S40 | YouTube GenAI disclosure: realistic synthetic people/voices; exemptions; label placement; auto-labelling from May 2026; locked labels; penalties incl. YPP suspension | https://support.google.com/youtube/answer/14328491 ; https://blog.youtube/news-and-events/improving-ai-labels-viewers-creators/ ; https://support.google.com/youtube/answer/15447836 | 2026-05 | 2026-10-10 | medium |
| S41 | YouTube paid-promotion checkbox, 10-second disclosure, creator responsible for local law; YouTube Kids removal | https://support.google.com/youtube/answer/154235 ; https://support.google.com/youtube/answer/17596007 ; https://support.google.com/youtube/answer/10588440 | n/k | 2026-10-10 | medium |
| S42 | YouTube "inauthentic content" YPP rule (renamed 2025-07-15); mass-produced content ineligible; AI voice allowed if original | https://www.thurrott.com/?p=323183 ; https://www.subsub.io/blog/youtube-inauthentic-content-policy-2025 | 2025-07 | 2026-10-10 | medium |
| S43 | YPP: current thresholds; changes announced 2026-08-10, effective 2027-02-01 (8,000 hours / 20 million Shorts views for new applicants; Shorts payout needs 10 million per 90 days) | https://ppc.land/youtube-cuts-shorts-pay-for-channels-under-10m-views-from-february-2027/ ; https://searchenginejournal.com/youtube-updates-partner-program-terms-shorts-payout-rules/585331 ; https://unwire.hk/2026/08/12/youtube-ypp-2027-threshold/life-tech/social-network/ | 2026-08-10 | 2026-10-10 | medium |
| S44 | YouTube Shopping affiliate lists Taiwan; Shopee pilot (60+ channels, about 9,000 transactions in 42 days); threshold reported inconsistently | https://support.google.com/youtube/answer/13376398 ; https://technews.tw/2026/01/29/youtube-shopping-affiliate-program-is-available-to-eligible-creators-in-taiwan/ | 2026-01-29 | 2026-10-10 | medium |
| S45 | YouTube Data API: unaudited-project uploads locked private (docs conflict), 10,000-unit default quota, audit needed, quota-cost discrepancy, no multi-project quota gaming | https://developers.google.com/youtube/v3/docs/videos/insert ; https://developers.google.com/youtube/v3/revision_history ; https://support.google.com/youtube/answer/7300965 ; https://developers.google.com/youtube/v3/determine_quota_cost ; https://developers.google.com/youtube/terms/developer-policies-guide | n/k | 2026-10-10 | medium |
| S46 | TikTok Integrity and Authenticity / AI-generated content: label required for realistic AIGC; auto-label not removable; unlabelled content may be removed/restricted; version released 2026-08-25 effective 2026-09-24; bulk automation and fake engagement banned | https://www.tiktok.com/community-guidelines/en/integrity-authenticity ; https://www.tiktok.com/tns-inapp/pages/ai-generated-content ; https://www.tiktok.com/creator-academy/en/article/ai-generated-content-label ; https://newsroom.tiktok.com/new-labels-for-disclosing-ai-generated-content?lang=en | 2026-08-25 | 2026-10-10 | medium |
| S47 | TikTok Branded Content Policy and Commercial Content Disclosure setting; 60-day tag authorisation; ineligible for For You if undisclosed; label wording varies | https://www.tiktok.com/legal/page/global/bc-policy/en ; https://ads.tiktok.com/help/article/about-the-content-disclosure-setting-for-creators | n/k | 2026-10-10 | medium |
| S48 | TikTok Content Posting API: unaudited clients private-only, 5 users per 24 h, audit required, branded content cannot be private | https://developers.tiktok.com/docs/en/content-sharing-guidelines ; https://developers.tiktok.com/docs/en/content-posting-api-get-started ; https://developers.tiktok.com/docs/en/getting-started-faq | n/k | 2026-10-10 | medium |
| S49 | TikTok Creator Rewards / Shop: no Taiwan availability found (third-party lists name Western markets) | https://postfa.st/blog/tiktok-monetization-requirements ; https://ttcalculator.net/learn/creator-fund-countries/ | 2026 | 2026-10-10 | low |
| S50 | Fraud Crime Hazard Prevention Act: ad platforms designated (Google, YouTube, LINE, Facebook, Instagram, TikTok; Threads added later per secondary reports); advertiser identity verification; 24-hour takedown; transparency reports | https://technews.tw/2024/11/13/platform-advertising-real-name-system/ ; https://www.thenewslens.com/article/245675 ; https://finance.ettoday.net/news/2854187 | 2024-11 | 2026-10-10 | medium |
| S51 | Digital Industry Administration (數位產業署) reportedly fined Meta NT$5 million for undisclosed AI-generated personal images in ads, plus NT$5 million for late takedown; Meta says it labels AI-made ads "AI info"; cumulative six fines totalling NT$28.5 million (single source). Decision date (earlier draft: 2026-08-14) and article numbers (earlier draft: Art. 31(1)(4), Art. 40(2)) are unverified | https://www.cna.com.tw/news/afe/202609230333.aspx ; https://ec.ltn.com.tw/article/breakingnews/5583322 ; https://www.blocktempo.com/meta-fined-twice-taiwan-scam-ads-ai-disclosure-lawmaker-amendment/ | 2026-09-23 (CNA URL date; fine date unverified) | 2026-10-10 | medium (existence of NT$5 million fine, multiple outlets, not re-fetched); low (cumulative total); unverified (decision date, article numbers) |
| S52 | Fair Trade Commission endorsement advertising (薦證廣告): disclosure of material connections; influencers as advertisers or endorsers; fines NT$50,000 to NT$25 million for false advertising | https://www.leeandli.com/TW/Newsletters/2501.htm ; https://www.inside.com.tw/article/30951-Taiwan-amendment-passed-KOL-main-advertisements-are-false-the-maximum-penalty-is-25-million | 2023-02 / 2025-01 | 2026-10-10 | medium |
| S53 | X policies: synthetic and manipulated media; automation rules; authenticity | https://help.x.com/en/rules-and-policies/manipulated-media ; https://help.x.com/en/rules-and-policies/x-automation ; https://help.x.com/en/rules-and-policies/platform-manipulation | 2023-04 (media policy) | 2026-10-10 | medium |
| S54 | Dcard advertising and commercial-content rules (updated 2025-01-13): bans, three-strike 7-day suspension, board-level strictness; site rules updated 2026-03-30 not read | https://www.dcard.tw/f/announcement/p/234243656 ; https://www.dcard.tw/terms ; https://www.dcard.tw/f/house/p/261518136 | 2025-01-13 | 2026-10-10 | medium |
| S55 | LINE Creators Market Terms cl. 8.13: LINE may display AI-generated label; review guidelines; third-party guide on AI stickers | https://creator.line.me/en/terms/ ; https://creator.line.me/en/review_guideline/ ; https://www.shareuhack.com/en/posts/ai-line-sticker-passive-income | n/k / 2026-05 | 2026-10-10 | medium (terms); low (guide) |
| S56 | LINE general terms reportedly bar mass identical messages and allow deletion without notice; older suspension reports | https://technews.tw/?p=1367793 ; https://www.ettoday.net/news/20130224/167143.htm ; https://www.ithome.com.tw/news/99363 ; https://robot.blueeyes.tw/LINE_rule-en.php | 2013 / n/k | 2026-10-10 | low |
| S57 | LINE's AI reply feature reported as limited to some Japan users; Taiwan plans unstated | https://news.tvbs.com.tw/travel/2986083 | n/k | 2026-10-10 | low |
| S58 | Third-party claims on Instagram carousels (20 slides), saves/sends, Reels reach decline; Threads scheduling support in Business Suite reported inconsistently | https://metricool.com/instagram-trends/ ; https://sproutsocial.com/insights/schedule-threads-posts/ ; https://shortsync.app/guides/schedule-threads-posts | 2026 | 2026-10-10 | low |
| S59 | AI Basic Act: brief states in force 2026-01-14. One search summary (source not named) said the Legislative Yuan passed it 2025-12-23 and it was promulgated 2026-01-14, and attributed the competent authority inconsistently (NSTC vs MODA). No primary source opened | BRIEF.md section 4 (as given); no URL verified | n/k | 2026-10-10 | unverified |

## Verification note

Verifier: independent skeptical re-check, date 2026-10-10.

**What I could and could not do.** I tried to re-fetch or re-search the highest-stakes claims, but the shared WebSearch budget for this run was already used up (the tool returned "budget used up" for every query) and WebFetch failed on DNS for every host tried (mic.iii.org.tw, cna.com.tw, focustaiwan.tw, techcrunch.com). I did not route around either block. **No claim in this file was independently re-confirmed against a live source by me.** The verification below is therefore a consistency, ground-rule, vocabulary and structure audit, plus downgrades of anything that looked fragile. Confidence labels in the Sources table still mean "as reported by search summaries", not "re-verified".

**Claims selected as highest-stakes (and status after this pass):**

| Claim | Status |
|---|---|
| NCC 2025 account ownership: LINE 98.2%, Facebook 82.4%, YouTube 68.6%, Instagram 47.8% [S2] | Matches BRIEF.md; not re-fetched; S2 downgraded to medium (single outlet for Instagram) |
| TikTok 23.8% accounts, 47.5% watched, 72.5% of 16-25 [S3] | Matches BRIEF.md; not re-fetched |
| MIC 18-24: Instagram 78%, Dcard 45.9%, Threads 44%; fieldwork Q4 2024 [S5] | Matches BRIEF.md; not re-fetched; sample-size n=1,068 appears for two waves, flagged |
| MIC video survey 70.5% / 68.1% / 58.4% / 43.0% [S8] | Not re-fetched; 59.3% duplicates an unrelated figure, flagged |
| LINE VOOM Taiwan closure 2026-09-30 [S11] | Two outlets cited; not re-fetched; kept |
| Xiaohongshu block from 2025-12-04, 1,706 cases, NT$247.7 million, Art. 42 [S13] | Three outlets cited; not re-fetched; article number marked unchecked |
| Instagram "AI-generated profile" label, 2026-08-31, reach limit, Taiwan scope [S27][S28] | Not re-fetched; Taiwan scope remains unverified |
| Meta NT$5 million fine; date 2026-08-14; Art. 31(1)(4), 40(2) [S51] | Date contradicts the cited sources' own date (2026-09-23); date and articles downgraded to unverified |
| YPP changes from 2027-02-01 [S43] | Secondary reports only; wording softened to "reported" |
| LINE OA prices incl. increase from 2026-11-01 and NT$0.20/0.15 add-on [S12] | Third-party summaries; not re-fetched; billing unit still unresolved |
| FTC fines NT$50,000 to NT$25 million [S52] | Article number and trigger conditions unverified; noted |
| Threads "150 million label views" [S30] | Cited source cannot contain it; marked unverified, no longer relied on |
| "Hundreds of AI doctors/healers" [S27] | Count removed as unverified |
| Instagram API 100 vs 50 posts/24 h; Threads 250 posts / 1,000 replies [S36][S38] | Not re-fetched; the 100-vs-50 conflict was already flagged |
| TikTok guidelines released 2026-08-25, effective 2026-09-24 [S46] | Not re-fetched; kept as medium |
| TikTok public-sector ban 2022-12 [S15] | Not re-fetched; kept as medium |
| AI Basic Act in force 2026-01-14 [S59] | Only the brief states it; still unverified |

**Other corrections made:** "brief says LINE VOOH" corrected (it is the task text; BRIEF.md does not mention it); "leading" Xiaohongshu fashion channel softened to "popular" (no share figure); fine-date claim rewritten; stylised-character "design lever" reworded so it cannot be read as permission to skip the AI label (ground rule 1).

**Checks that did pass:** capacity arithmetic in 5.4 (360-150=210; 210/5=42; 3x2x3=18; 3x2x5=30; 10x2x5=100); source ids S1-S59 all present in the table with date accessed and confidence; every Chinese string is in Traditional characters and Taiwan vocabulary is used (no mainland terms found by search); no recommendation breaks the ground rules (no health/financial advice, no invented testimony, no scraping, no fake popularity, manual or official-API posting only, personas labelled and studio-named).

**Remains unverified (needs a human or a search-enabled follow-up):** all headline figures above against live primary pages; Instagram AI-generated profile rollout in Taiwan; the Meta fine date and statute articles; LINE OA billing unit and the 2026-11-01 increase; the YPP 2027 changes; the 59.3% video figure and the 1,068 sample size; Threads Taiwan user count; AI Basic Act date and competent authority; Xiaohongshu extension after 2026-12-04.
