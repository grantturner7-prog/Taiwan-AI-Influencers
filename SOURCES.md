# SOURCES

Master source table, consolidated and de-duplicated from the six Phase 1 research files (2026-10-10). Every market, pricing or legal claim needs a source and a date. Unverifiable claims are labelled **unverified**.

## How to read this file

- **No page was opened.** In every Phase 1 file, WebFetch failed on DNS, curl through the egress proxy returned 403, and the shared WebSearch budget ran out. Every web row below was read only as a search-result summary. The same limit applied to the Phase 1 synthesis pass (a reviewer-rate search was refused: "budget used up"). Treat all confidence labels as "as reported by summaries", not "re-verified".
- **Confidence:** `high` = two or more outlets agree, or an institutional release (author rubric; still not opened). `medium` = one reliable summary of a page nobody opened. `low` = marketing blog, undated, tracker estimate, or outlets disagree. `unverified` = single mention or recalled from memory with no way to cross-check. Where files rated the same source differently, the **lower** rating is used here.
- **Date accessed** is 2026-10-10 for every row.
- **ID scheme:** an ID such as `PL27` means "platforms.md source S27". Prefix: PL = platforms, CP = competitors, NI = niches, MO = monetisation, LG = legal, CU = culture. When several files cite the same source, it appears once under the first file in that order, and the **File(s) and local ids** column lists the others (for example `comp S4, legal S2` means competitors.md S4 and legal.md S2). Research files are in `research/`.
- Currency and figures are as reported. NT$ unless stated.

## A. Brief section 4 starting facts: re-verification status (Phase 1)

| # | Brief claim | Status after Phase 1 | What changed or remains open | Source ids |
|---|---|---|---|---|
| 1 | NCC 2025: LINE 98.2%, Facebook 82.4%, YouTube 68.6%, Instagram 47.8% (account ownership) | **Confirmed in secondary reports** | These measure account ownership, not active use. Instagram 47.8% rests on a single outlet. NCC PDF (sample size, method) not opened | PL1, PL2, PL4 |
| 2 | TikTok 23.8% accounts; 47.5% watched; 72.5% of 16-25 watched | **Confirmed in secondary reports** | Two different metrics (account vs having watched); the brief lists them together | PL3 |
| 3 | MIC: 18-24 favour Instagram 78%, Dcard 45.9%, Threads 44% | **Figures confirmed; dated** | Fieldwork Q4 2024, released 2025-12-04, so about two years old, not a 2026 measurement. n=1,091 vs 1,068 ambiguous across waves | PL5, PL6, PL7 |
| 4 | AI Basic Act in force 2026-01-14; principles bar AI use for false advertising | **Unverified** | Only the brief and one unnamed summary give the date (passed 2025-12-23, promulgated 2026-01-14); it may be a promulgation date, not an effective date. The "false advertising bar" and any labelling duty are not confirmed. Competent authority reported inconsistently (NSTC vs MODA) | PL59, LG-U5, LG-U6 |
| 5 | Fraud Crime Hazard Prevention Act requires ad platforms to disclose AI-generated personal images | **Partly confirmed** | Platform duty and a reported NT$5 million fine on Meta are in the press (reports dated 2026-09-23). The fine's decision date (an earlier draft said 2026-08-14) and article numbers (Art. 31(1)(4), 40(2)) are unverified. Whether advertisers or organic posts have their own duty: not found | PL50, PL51 |
| 6 | Fair Trade Commission treats sponsored posts as 薦證廣告; confirm current fine range | **Partly confirmed; fine range NOT confirmed** | Disclosure of material connections and endorser liability are in secondary sources. NT$50,000 to NT$25 million is reported by secondary sources only; Art. 21 / Art. 42 are recalled, statute text unseen | PL52, LG-U1, LG-U2 |
| 7 | TikTok, YouTube and Meta all require a label on realistic AI people | **Confirmed, and tighter than the brief says** | Instagram added an "AI-generated profile" label with recommendation limits (2026-08-31, Taiwan scope unconfirmed); YouTube auto-labels since May 2026; TikTok guidelines effective 2026-09-24, auto-labels non-removable | PL27, PL28, PL40, PL46 |
| 8 | Kolr 2026 (iKala): brands prize verifiable human creators | **Confirmed in summaries; report not read** | Direction matches; the full report was not opened | PL20 |
| 9 | Press coverage of brands passing off AI personas as real customers caused a trust backlash | **Corrected** | The TVBS/UDN items relay a UK Guardian investigation (2026-06-21), not a Taiwan brand case. The TVBS URL in the brief is a site-search page. No Taiwan regulator action on this found | CP1, CP2, CP3 |
| 10 | (New, not in brief) LINE VOOM, Xiaohongshu | **Changed** | LINE VOOM closed in Taiwan 2026-09-30. Xiaohongshu blocked since 2025-12-04 for a provisional year | PL11, PL13 |

## B. Platforms, audiences and platform rules (from platforms.md)

| ID | File(s) and local ids | Claim | URL | Confidence |
|---|---|---|---|---|
| PL1 | platforms S1 | NCC 114th-year Communications Market Report exists (commissioned by NCC, executed by 台灣經濟研究院, Dec 2025); PDF not opened | https://commsurvey.ncc.gov.tw/ | medium |
| PL2 | platforms S2; culture S2 | NCC: LINE 98.2%, Facebook 82.4%, YouTube 68.6%, Instagram 47.8%; 99.4% hold at least one account; TikTok, Xiaohongshu, WeChat, Threads, X, WhatsApp each below 30% | https://news.nextapple.com/life/20260116/B179FADDD8297A4BE6D2F4C22549D035 | medium (single outlet for Instagram) |
| PL3 | platforms S3; culture S3 | TikTok watched by 47.5% (18.7% in 2019); 16-25: 72.5%; account ownership 23.8% (fifth) | https://focustaiwan.tw/culture/202601040012 | medium |
| PL4 | platforms S4 | NCC top three platforms; 83% of 16+ watch online creator video | https://udn.com/news/story/7240/9243385 | medium |
| PL5 | platforms S5; culture S1; monetisation S10; niches S22 | MIC social survey: YouTube 72.3%, Facebook 72.1%, Instagram 44.7%, Dcard 17.6%, Threads 17.5%, PTT 17.1%; 18-24 Instagram 78%, Dcard 45.9%, Threads 44%; 25-34 Instagram 59.3%, Dcard 30.9%, Threads 28.4%; experience sharing (體驗文) makes 52.5% want to try (60.3% of 25-34); fieldwork Q4 2024, n=1,091, ±3.0%; released 2025-12-04 | https://mic.iii.org.tw/news.aspx?id=744 | medium (rated high by author; not re-opened; sample-size mapping unconfirmed) |
| PL6 | platforms S6; culture S34 | Press coverage of MIC survey: Facebook about six in ten of 18-34; 45+ core; motives incl. consumer and financial information | https://money.udn.com/money/story/5613/9182136 | medium |
| PL7 | platforms S7 | MIC earlier wave (fieldwork Q4 2023): Facebook 70%, YouTube 53%, Instagram 34%, PTT 11%, Dcard 9%; formats Stories 37%, video 34% | https://mic.iii.org.tw/news.aspx?id=691 | medium (rated high by author) |
| PL8 | platforms S8; culture S4 | MIC video survey (Aug 2026): 70.5% short-video users; Shorts 68.1%, Facebook Reels 58.4%, Instagram Reels 43.0%; 51.3% pick the platform they already use; a 59.3% sub-figure may duplicate another number | https://money.udn.com/money/story/7307/9704523 | medium |
| PL9 | platforms S9 | LINE Taiwan 22 million MAU, 94.5% penetration, as of 2026-03-31 | https://www.lycorp.co.jp/en/company/global/ | medium |
| PL10 | platforms S10; culture S5; monetisation S22 | LINE Taiwan: about 60 million stickers a day; over 1 billion messages a day; Nielsen 93% weekly use, about 14 opens a day | https://ec.ltn.com.tw/article/breakingnews/5511215 | medium |
| PL11 | platforms S11; monetisation S38; culture S6 | LINE VOOM Taiwan shut down 2026-09-30; Stories, follow/fans features closed; LINE suggests following creators via Official Account | https://www.ettoday.net/news/20260803/3212389.htm ; https://www.nownews.com/news/6878748 | medium-high (two outlets) |
| PL12 | platforms S12; monetisation S24 | LINE Official Account plans (ex-tax): 輕用量 NT$0 / 200 free messages; 中用量 NT$800 to NT$1,000 from 2026-11-01 / 3,000; 高用量 NT$1,200 to NT$1,400 / 6,000; add-on NT$0.20 then NT$0.15; billing unit per broadcast unresolved | https://tw.linebiz.com/column/LINEOA-2026-Price-Plan/ | medium (third-party summaries) |
| PL13 | platforms S13; legal S6; culture S7 | Interior Ministry DNS block of Xiaohongshu from 2025-12-04 for a provisional year; 1,706 cases; about NT$247.7 million losses; over 3 million Taiwan users; "Art. 42" is press-reported, not checked | https://cna.com.tw/news/asoc/202512040238.aspx ; https://www.nownews.com/news/6761458 | medium |
| PL14 | platforms S14 | Possible extension of the Xiaohongshu ban (undated report) | https://www.inside.com.tw/tag/%E5%B0%8F%E7%B4%85%E6%9B%B8 | low |
| PL15 | platforms S15 | TikTok/Douyin barred on public-sector devices (reported effective 2022-12-05); private use not restricted | https://www.inside.com.tw/article/29992-MODA-ban-TikTok-Xiaohongshu | medium |
| PL16 | platforms S16 | Dec 2022 controversy over a ByteDance-named Taiwan company; MAC cites Cross-Strait Act Art. 40-1 | https://www.cna.com.tw/news/aipl/202212190332.aspx | medium |
| PL17 | platforms S17 | DataReportal Digital 2026 Taiwan: 18.1 million social identities, 78.4% of population (Oct 2025) | https://datareportal.com/reports/digital-2026-taiwan | medium |
| PL18 | platforms S18 | Third-party per-platform user counts (marketing blog); LINE TODAY 18 million MAU is a 2018 figure | https://iseeu.tw/taiwan-social-media-report/ | low |
| PL19 | platforms S19; monetisation S1 | AnyMind 2026 APAC report: Instagram carries 57.7% of Taiwan influencer campaigns; market about US$239 million, +11.7% | https://www.ctee.com.tw/news/20260203701010-430502 | medium |
| PL20 | platforms S20; competitors S51; niches S23; monetisation S2; culture S23 | Kolr (iKala) 2026 AI marketing report: authenticity; verifiable human creators framed as the scarce asset; AI the dominant theme (report not read) | https://www.bnext.com.tw/article/90807/ikala_kolr_2026_04 | medium |
| PL21 | platforms S21 | Threads 500 million MAU globally (June 2026); Threads head credits a Taiwan election for early growth | https://technews.tw/2026/06/17/new-features-to-celebrate-500-million-monthly-users-on-threads/ | medium |
| PL22 | platforms S22 | Meta (July 2024): India, Japan, Taiwan top three Threads markets | https://www.cna.com.tw/news/ait/202407040147.aspx | medium |
| PL23 | platforms S23 | Conflicting estimates of Taiwan's share of Threads traffic (10% to 24%) | https://www.managertoday.com.tw/articles/view/72894 | low |
| PL24 | platforms S24; culture S13 | Threads brand-voice commentary; older stat that 63% of Threads posts are text-only | https://www.cw.com.tw/article/5131412 | low |
| PL25 | platforms S25 | Dcard audience claims (over 95% aged 18-24; 2022 registered users) | https://newsletter.management.ntu.edu.tw/?p=11118 | low |
| PL26 | platforms S26; culture S12 | PTT account restrictions; founder says controls target coordinated volume inflation | https://tfc-taiwan.org.tw/?p=105500 | low |
| PL27 | platforms S27; monetisation S39; culture S8 | Instagram renamed "AI creator" label to "AI-generated profile" (2026-08-31); reach limits for unlabelled photorealistic AI profiles; Taiwan scope unconfirmed (one uncorroborated aggregator says US-only) | https://techcrunch.com/2026/08/31/instagram-puts-new-limits-on-undisclosed-ai-profiles/ | high (existence and core terms); unverified (Taiwan scope) |
| PL28 | platforms S28 | Instagram Help: may limit accounts repeatedly sharing content prominently featuring a photorealistic AI-generated person unless labelled | https://help.instagram.com/313829416281232/ | medium |
| PL29 | platforms S29 | Meta Feb 2026 notice: disclosure tool required for organic photorealistic video / realistic audio; penalties possible (geographic scope not stated) | https://about.fb.com/news/2026/02/meta-prepares-for-2026-us-midterms/ | medium |
| PL30 | platforms S30 | Meta "AI info" labelling via C2PA/IPTC or self-disclosure. The "150 million Threads label views" figure is unverified and not relied on | https://about.fb.com/news/2024/02/labeling-ai-generated-images-on-facebook-instagram-and-threads/ | medium |
| PL31 | platforms S31 | Meta ads AI labels; one commentator lists Taiwan as a checkbox region | https://about.fb.com/news/2025/02/gen-ai-transparency-metas-ads-products/ | medium (Meta post); low (Taiwan checkbox) |
| PL32 | platforms S32; monetisation S15; legal S13 | Meta branded-content rules: tag with brand permission; gifts count; pre-authorisation for dating, gambling, pharmacies/prescription drugs, crypto; paid-partnership label in-app; same tool on Threads; does not discharge Taiwan law | https://help.instagram.com/1695974997209192 | medium |
| PL33 | platforms S33 | Instagram unoriginal-content recommendation exclusion (spring 2026) | https://petapixel.com/2026/04/30/new-instagram-policies-target-reposted-content/ | medium |
| PL34 | platforms S34; monetisation S16; culture S14 | Meta Community Standards: personal profiles for non-human entities are fake accounts (a persona on Facebook must be a Page); fake engagement barred | https://transparency.meta.com/policies/community-standards/inauthentic-behavior/ | medium |
| PL35 | platforms S35 | Instagram Terms of Use (no buying/selling accounts, impersonation); up to five accounts in the app switcher | https://help.instagram.com/581066165581870/ | medium |
| PL36 | platforms S36 | Instagram content-publishing API: 100 posts/24 h (same doc also shows 50); 400 containers | https://developers.facebook.com/docs/instagram-platform/content-publishing/ | medium |
| PL37 | platforms S37 | Messaging policy: 24 h window, Human Agent tag 7 days, bot disclosure when required by law | https://developers.facebook.com/documentation/business-messaging/messenger-platform/policy | medium |
| PL38 | platforms S38 | Threads API: 250 posts and 1,000 replies per rolling 24 h | https://developers.facebook.com/documentation/threads/overview | medium |
| PL39 | platforms S39 | Instagram ranking: Reels on watch-through, likes, reshares; Explore on likes, saves, shares | https://about.instagram.com/blog/announcements/instagram-ranking-explained | medium |
| PL40 | platforms S40; monetisation S40; culture S10 | YouTube GenAI disclosure: realistic synthetic people/voices; auto-labels since May 2026; repeated non-disclosure can lead to YPP suspension; disclosure does not limit monetisation eligibility | https://support.google.com/youtube/answer/14328491 | medium |
| PL41 | platforms S41 | YouTube paid-promotion checkbox; creator responsible for local law | https://support.google.com/youtube/answer/154235 | medium |
| PL42 | platforms S42; monetisation S18 | YouTube "inauthentic content" YPP rule (renamed 2025-07-15); mass-produced/templated content ineligible | https://www.thurrott.com/?p=323183 | medium |
| PL43 | platforms S43; monetisation S17 | YPP thresholds; reported changes announced 2026-08-10, effective 2027-02-01 (8,000 hours or 20 million Shorts views for new applicants; Shorts payout needs 10 million per 90 days). Secondary reports only | https://ppc.land/youtube-cuts-shorts-pay-for-channels-under-10m-views-from-february-2027/ | medium (secondary only) |
| PL44 | platforms S44; monetisation S19 | YouTube Shopping affiliate lists Taiwan; Shopee pilot 2025-11-19 to 12-31 (60+ channels, about 9,000 transactions in 42 days); threshold reported inconsistently | https://support.google.com/youtube/answer/13376398 ; https://technews.tw/2026/01/29/youtube-shopping-affiliate-program-is-available-to-eligible-creators-in-taiwan/ | medium |
| PL45 | platforms S45 | YouTube Data API: unaudited uploads locked private (docs conflict), quota, audit | https://developers.google.com/youtube/v3/docs/videos/insert | medium |
| PL46 | platforms S46; culture S9 | TikTok AI-content labels; guidelines released 2026-08-25, effective 2026-09-24; auto-labels non-removable; bulk automation banned | https://www.tiktok.com/community-guidelines/en/integrity-authenticity | medium |
| PL47 | platforms S47 | TikTok Branded Content Policy and disclosure setting | https://www.tiktok.com/legal/page/global/bc-policy/en | medium |
| PL48 | platforms S48 | TikTok Content Posting API: unaudited clients private-only, 5 users per 24 h | https://developers.tiktok.com/docs/en/content-sharing-guidelines | medium |
| PL49 | platforms S49; monetisation S20 | TikTok Creator Rewards / Shop Taiwan availability: not found (third-party lists name Western markets) | https://postfa.st/blog/tiktok-monetization-requirements | low |
| PL50 | platforms S50; legal S4; monetisation S14 | Fraud Crime Hazard Prevention Act: designated ad platforms (Google, YouTube, LINE, Facebook, Instagram, TikTok; Threads later); advertiser identity verification; 24 h takedown | https://technews.tw/2024/11/13/platform-advertising-real-name-system/ | medium |
| PL51 | platforms S51; legal S5; monetisation S13; culture S33 | Digital Industry Administration (數位產業署) reportedly fined Meta NT$5 million for undisclosed AI-generated personal images in ads (plus NT$5 million for late takedown). Reports dated 2026-09-23; decision date (earlier draft 2026-08-14) and article numbers unverified; NT$28.5 million cumulative is single-source | https://www.cna.com.tw/news/afe/202609230333.aspx | medium (existence); low (cumulative); unverified (date, articles) |
| PL52 | platforms S52; competitors S6; niches S24; monetisation S11; legal S1; culture S15 | FTC 薦證廣告: disclosure of material connections; endorser liability; false-advertising fines NT$50,000 to NT$25 million (secondary only; article numbers and trigger conditions unverified; inside.com.tw page may predate the 2023 amendment) | https://www.leeandli.com/TW/Newsletters/2501.htm ; https://www.inside.com.tw/article/30951-Taiwan-amendment-passed-KOL-main-advertisements-are-false-the-maximum-penalty-is-25-million | low-medium |
| PL53 | platforms S53 | X synthetic media, automation and platform manipulation policies | https://help.x.com/en/rules-and-policies/manipulated-media | medium |
| PL54 | platforms S54; culture S11 | Dcard advertising rules (updated 2025-01-13): promotion banned; three violations bring a 7-day suspension | https://www.dcard.tw/f/announcement/p/234243656 | medium |
| PL55 | platforms S55; monetisation S21; legal S14 | LINE Creators Market terms (cl. 8.13, number unconfirmed): LINE may display an AI-generated label; terms do not ban AI stickers; third-party guide claims auto-flagging | https://creator.line.me/en/terms/ | medium (terms); low (guide) |
| PL56 | platforms S56; monetisation S25 | LINE general terms reportedly bar mass identical messages; reports old (2013) or undated | https://technews.tw/?p=1367793 | low |
| PL57 | platforms S57; monetisation S26 | LINE AI reply feature limited to some Japan users | https://news.tvbs.com.tw/travel/2986083 | low |
| PL58 | platforms S58 | Third-party claims on carousels, saves/sends, Threads scheduling support | https://metricool.com/instagram-trends/ | low |
| PL59 | platforms S59; legal S7 | AI Basic Act: passed 2025-12-23, promulgated 2026-01-14 per one unnamed summary; authority inconsistent; no primary source opened | https://www.taiwannews.com.tw/en/news/6380429 ; https://iapp.org/news/a/taiwan-s-ai-governance-framework-unveiled | unverified |

## C. Competitors, trust incidents and virtual-character benchmarks (from competitors.md)

| ID | File(s) and local ids | Claim | URL | Confidence |
|---|---|---|---|---|
| CP1 | competitors S1; legal S9; culture S16 | TVBS headline (2026-06-23): AI virtual influencers posing as real customers, "7成大眾真假分不清". The URL is a TVBS site-search page, not the article | https://news.tvbs.com.tw/news/searchresult/虛擬網紅/news | low |
| CP2 | competitors S2 | UDN report on the same story; consumer groups call for mandatory AI labels | https://udn.com/news/story/6812/9583886 | low-medium |
| CP3 | competitors S3; legal S9 | Guardian investigation (2026-06-21) via secondary coverage: NDAs, Which? 70% figure; brands Once, Maket, Ashle named in secondary coverage | https://techstrong.ai/articles/brands-secretly-deploy-ai-influencers-to-mimic-authentic-reviews-report/ | medium |
| CP4 | competitors S4; legal S2; niches S10; monetisation S12; culture S31 | FTC (2026-04-23): AI-using ads in monitoring scope; illegal cases found; mandatory AI disclosure under evaluation. Speaker title unverified; single outlet | https://technews.tw/2026/04/23/ftc-to-assess-mandatory-disclosure-rules-for-ai-ads/ | medium (single outlet) |
| CP5 | competitors S5; legal S3 | FTC generative-AI competition policy statement 2026-03-18; AI can enable false marketing | https://www.cna.com.tw/news/afe/202603180299.aspx | medium |
| CP6 | competitors S7; legal S8; niches S12; monetisation S31; culture S18 | Life8 AI model likeness dispute (about 2026-07-17/18); brand apologised and withdrew; Civil Code Art. 18 portrait-right commentary | https://oecd.ai/en/incidents/2026-07-18-2fa7 | medium |
| CP7 | competitors S8; niches S13; monetisation S32; culture S19 | IKEA Taiwan AI family image with distorted hands (2026-06-01) | https://unwire.hk/2026/06/01/ikea-taiwan-ai-image-zombie-hand-controversy/ai/ | medium |
| CP8 | competitors S9; culture S20 | ALT lucky-bag "mouse" AI image case (May 2026), NT$10 million claim | https://www.ettoday.net/news/20260511/3164208.htm | medium |
| CP9 | competitors S10; niches S28 | AI celebrity-lookalike real-estate ad (OECD record only) | https://oecd.ai/en/incidents/2026-04-25-07a8 | low |
| CP10 | competitors S11; niches S14; legal S12 | AI deepfake doctors in Taiwan medical ads (2026-06-15 record) | https://oecd.ai/en/incidents/2026-06-15-3c15 | medium |
| CP11 | competitors S12 | Taiwan FactCheck Center on AI-generated YouTube personas (political; context only) | https://en.tfc-taiwan.org.tw/ai-generated-youtube-videos-promote-taiwan-false-claims/ | medium |
| CP12 | competitors S13; niches S31 | AI "perfect double" fake travel persona ran for about 3 years | https://www.peoplenews.tw/?p=1828 | low |
| CP13 | competitors S14; legal S10; culture S21 | Taiwan AI news presenters (2023); NCC letter to 民視; principle: disclose clearly, humans write and check scripts | https://news.pts.org.tw/article/648630 | medium |
| CP14 | competitors S15; niches S19; monetisation S28 | 虎妮 and 杏仁咪嚕 (Yahoo TV): history, audience, earnings model; Kaohsiung tourism ambassador | https://www.bnext.com.tw/article/51705/oath-yahoo-tv-vtuber-hoonie-friends | medium |
| CP15 | competitors S16; niches S15; monetisation S7 | Taiwan VTuber industry (Mirror Media, 2024-09): income order donations/memberships, merch, then 業配; corporate collaborations budgeted case by case; 100 to 200 stream hours a month expected by one agency | https://www.mirrormedia.mg/story/20240912insight004 | medium |
| CP16 | competitors S17 | 杏仁咪嚕 about 300,000 subscribers (undated) | https://news.tvbs.com.tw/life/1467071 | low |
| CP17 | competitors S18; niches S18; monetisation S29; culture S29 | Springfish (春魚創意): company-stated 1.8 million combined subscribers, 100 million views, 280+ collaborations (mid-2025) | https://www.4gamers.com.tw/news/detail/72720/springfish-studio-vtuber-3d-live-concert-nexus | medium (company-stated) |
| CP18 | competitors S19 | Universal Music and Springfish partnership for 極深空計畫, announced 2026-01-16 | https://www.setn.com/klist/352443 | medium |
| CP19 | competitors S20 | 極深空計畫 first member about 26,000 subscribers within a month | https://www.techbang.com/posts/100320-springfish-studio-unveils-new-vtuber-xtreme-deep-field-project | medium |
| CP20 | competitors S21 | Springfish 2022: 270,000 combined subscribers, Xbox Taiwan/Gamania partners | https://www.bnext.com.tw/article/71165/2022-taicca-2-springfish | medium |
| CP21 | competitors S22 | TAIPEI12elve (So-net with PANDOLOR), debut June 2024 | https://www.4gamers.com.tw/news/detail/65400/so-net-x-pandolor-super-virtual-idol-project | medium |
| CP22 | competitors S23; niches S20 | 宮祈緣 (Gamania G Studio with 霹靂): AI-driven "無中之人" host; 《結緣金》 from 2025-11-01; 健身 among about 20 themes; no audience data | https://www.ctee.com.tw/news/20251029700852-430201 | medium |
| CP23 | competitors S24 | Lady LayLa 萊拉 UE5 virtual singer | https://www.techbang.com/posts/101261-metaverse-idol-lady-layla-single-mv-is-online | low |
| CP24 | competitors S25; niches S25; monetisation S27 | 中華電信 HiNet virtual idol contest 2019 (745 entries) and 光音凱伶; "Lumina" identity unverified | https://www.cna.com.tw/news/afe/201911050200.aspx | medium (contest); low (Lumina) |
| CP25 | competitors S26 | JJ avatar of 解婕翎; 蝦拉拉 about 4,000 subscribers; Rui (Korea) | https://www.bnext.com.tw/article/74241/virtual-kol-rui-youtuber | medium |
| CP26 | competitors S27; niches S25; monetisation S23; culture S30 | 7-ELEVEN OPEN將: 8 LINE sticker rounds since 2020, over 10 million cumulative downloads (company statement, date not shown) | https://www.setn.com/news/1594957 | medium (company-stated) |
| CP27 | competitors S28; niches S16; monetisation S30; legal S15; culture S28 | About 2,595 Taiwan VTubers counted (2024); Taiwan has no law specific to virtual personas (academic, 2025) | https://www.airitilibrary.com/Article/Detail/U0020-1101202518053100 | medium (academic) |
| CP28 | competitors S28b | Forum-reposted 2026 comment on VTuber commercial disputes | https://www.ptt.cc/bbs/C_Chat/M.1779337364.A.589.html | unverified |
| CP29 | competitors S29 | Over 40% of Taiwan's top 100 live-stream earners in 2023 were virtual idols (single magazine) | https://www.gvm.com.tw/article/108762 | low |
| CP30 | competitors S30; monetisation S9 | ANYCOLOR revenue mix merch 44% / live 31% / ads 14%; Yano 2022 merch about 51.3% | https://www.nownews.com/news/6095525 | low |
| CP31 | competitors S31; monetisation S8 | Taiwan VTuber start-up costs (2D NT$100,000 to 200,000; 3D NT$150,000 to 500,000); most earn a few thousand NT$ a month; about 6-month average career | https://news.pts.org.tw/article/777069 | medium |
| CP32 | competitors S32; niches S26; culture S17 | Mainland China e-commerce report: AI product imagery can add details a real product lacks | https://www.worldjournal.com/wj/amp/story/121617/9062017 | low |
| CP33 | competitors S33 | Momosuze Nene MRT ads (May 2022); fan donation anecdote | https://www.rfa.org/english/news/china/taiwan-vtuber-08062022083451.html | medium |
| CP34 | competitors S34 | 茸茸鼠 passed 100,000 subscribers in under 3 months | https://www.4gamers.com.tw/news/detail/50396/youtuber-mchikomame-subscriber-reaching-100k | low |
| CP35 | competitors S35 | 22 Taiwanese VTubers at a Taipei anime festival (about 2025-02) | https://www.taiwanplus.com/news/taiwan-news/arts-and-entertainment/250207025/taiwanese-vtubers-take-center-stage-at-taipeis-biggest-anime-festival | medium |
| CP36 | competitors S36; niches S27 | Spicy AI companion app names Taiwan its first APAC market (2025-01-13) | https://www.ctee.com.tw/news/20250113701625-431202 | medium |
| CP37 | competitors S37; monetisation S34; culture S25 | 遠見 2026-01-30: "艾塔娜" over 110,000 Instagram followers (almost certainly Spain's Aitana López; unverified); Hootsuite 2026 "one third say AI-made brand ads lower purchase intent" quoted second-hand | https://www.gvm.com.tw/article/127642 | low (艾塔娜); unverified (Hootsuite) |
| CP38 | competitors S38; monetisation S6 | Aitana López: follower history; agency founder self-reports average EUR 3,000 a month, peaks over EUR 10,000 (2023, unaudited) | https://www.businessinsider.nl/an-agency-created-an-ai-model-who-earns-up-to-11000-a-month-because-it-was-tired-of-influencers-who-have-egos | medium (existence); low (earnings) |
| CP39 | competitors S39; monetisation S4 | Imma: about 378,656 Instagram followers (CreatorDB 2026-08-23); engagement 0.2% to 0.3% | https://creatordb.app/creatorstats/immagram/ | medium (tracker estimate) |
| CP40 | competitors S40 | Ria: about 31,000 followers (CreatorDB 2026-09-27) | https://creatordb.app/creatorstats/ria_ria_tokyo/ | low |
| CP41 | competitors S41; monetisation S5; niches S32 | Rozy: about 160,651 followers (CreatorDB 2026-09-25); engagement 1.9%; two Shinhan Life TV spots 17.2 million views combined | https://www.koreajoongangdaily.com/business/virtual-influencers-kept-busy-as-jobs-keep-coming-in/11903999 | medium |
| CP42 | competitors S42; monetisation S3 | Lil Miquela: about 2,261,877 followers (CreatorDB 2026-08-26); CreatorIQ BMW posts 0.6% vs 3.6% for human creators (May 2023 to Apr 2024, vendor press release); revenue claims range widely | https://www.creatoriq.com/press/releases/amid-rise-of-ai-influencers-human-creators-still-drive-higher-instagram-engagement-rates/ | medium (counts); low (BMW comparison); unverified (revenue) |
| CP43 | competitors S43 | Noonoouri: about 458,975 followers (CreatorDB 2026-08-23); Dior, Valentino, MiuMiu work | https://creatordb.app/creatorstats/noonoouri/ | medium |
| CP44 | competitors S44 | Lu do Magalu counts (inconsistent), awards | https://creatordb.app/creatorstats/magalu/ | low |
| CP45 | competitors S45; niches S30; culture S22 | Mia Zelu fake Wimbledon posts (July 2025); AI disclosure hidden behind "Read More" | https://www.tennis.com/news/articles/ai-influencer-mia-zelu-went-viral-wimbledon-artificial-intelligence-social-media | medium |
| CP46 | competitors S46; culture S26 | Thalasya, Maya (PUMA), Southeast Asia six-market perception survey (N=6,000) | https://www.tatlerasia.com/power-purpose/innovation/asian-ai-influencers | low |
| CP47 | competitors S47 | Ayayi and Liu Yexi history and counts (reports vary) | https://global.chinadaily.com.cn/a/202209/21/WS632a74b6a310fd2b29e78e30.html | low |
| CP48 | competitors S48 | PLAVE stadium sell-out; Asia virtual-idol acceptance (LBB 2026-03-24); Taiwan tour dates unverified | https://lbbonline.com/news/What-Can-Brands-Learn-From-Asias-Leading-AI-Idols | medium (LBB); low (dates) |
| CP49 | competitors S49 | Kizuna AI hiatus 2022-02-26, return 2025-02-26 | https://www.anitrendz.com/news/2025/02/26/kizuna-ai-makes-her-return-after-three-year-long-hiatus | medium |
| CP50 | competitors S50; niches S9; monetisation S36; legal S16 | TechNews 2026-03-30: AI creators succeed in entertainment, fashion, gaming; health, family, finance, wellness suffer an authenticity gap; "viral but can't close the sale" (page not read) | https://finance.technews.tw/2026/03/30/ai-creators-can-go-viral-they-just-cant-close-the-sale/ | low |
| CP52 | competitors S52; monetisation S33; culture S24 | NielsenIQ study (Dec 2024): AI ads rated more annoying, boring, confusing (vendor-run) | https://nielseniq.com/global/en/news-center/2024/niq-research-uncovers-hidden-consumer-attitudes-toward-ai-generated-ads/ | medium (vendor study) |
| CP55 | competitors S55; niches S11; legal S11; culture S32 | Deepfake investment fraud impersonating exchange officials (Aug 2026); fraud statistics (41.09% loss share; 107,000+ ads removed) second-hand | https://www.cna.com.tw/news/afe/202608050308.aspx | medium (events); low (statistics) |
| CP56 | competitors S56; niches S17 | Taiwan human fitness YouTubers, about 150,000 to 1.7 million subscribers (tracker snapshots, mid-2026) | https://www.heepsy.com/top-youtube/fitness/taiwan | low |
| CP59 | competitors S59; culture S27 | KOL Radar article citing a 2022 survey: 58% follow at least one AI virtual influencer (origin unspecified) | https://www.kolr.ai/en/?p=19757 | low |

## D. Niches and advertiser spend (from niches.md)

| ID | File(s) and local ids | Claim | URL | Confidence |
|---|---|---|---|---|
| NI1 | niches S1 | DMA 2025 total digital ad volume 661.77億 (NT$66.18bn, +3.92%); video 199.64億 (30.17%) above display; growth slowed in 2025 vs 2024 | https://udn.com/news/story/7241/9684687 | medium |
| NI2 | niches S2 | DMA 2025 by industry: e-commerce 110.79億 (+6.9%); apps/games 74.75億; finance-insurance 62.04億 (+5.69%); leisure/entertainment +18.8%; health-care and beauty +11.4% (26.6% digital); FMCG +5.91% (50.7% digital) | https://iaataipei.org.tw/news/article/386 | medium (e-commerce, leisure, health-beauty, FMCG); low-medium (apps/games, finance amounts: one summary each) |
| NI3 | niches S3 | DMA 2024: total 636.83億 (+4.32%); e-commerce 103.67億; leisure +11.88%; fashion-luxury +10.34% | https://www.dma.org.tw/newsPost/2559 | medium |
| NI4 | niches S4 | DMA 2023: total 610.46億 (+3.5%); FMCG 47.01億; e-commerce 98.28億, apps/games 73.25億, finance 57.38億, beauty 54.94億 (one TenMax summary) | https://www.tenmax.io/tw/archives/83448 | medium (total, FMCG); low-medium (rest) |
| NI5 | niches S5 | Kolr Brand Aura Index Q1 2026 (YSL Beauty, Tod's); Kolr 2025 travel YouTuber ranking (滴妹 1.44 million) | https://n.yam.com/Article/20250702127716 | medium (Brand Aura); low (travel ranking) |
| NI6 | niches S6 | Game-software industry revenue NT$71.0bn in 2025, under NT$50bn in 2020 (industry revenue, not ad spend) | https://blog.104.com.tw/taiwan-game-industry-growth/ | medium |
| NI7 | niches S7 | Food Safety and Sanitation Act Art. 28/45: false/exaggerated claims NT$40,000 to 4,000,000; medical-effect claims NT$600,000 to 5,000,000; Tainan notice on AI-synthesised people claiming weight loss; no creator-specific ruling | https://udn.com/news/story/7326/9335678 | medium (tiers); single-summary (Tainan notice) |
| NI8 | niches S8 | Cosmetic Hygiene and Safety Act Art. 10: medical-effect tier NT$600,000 to 5,000,000 (unverified); exaggeration tier disputed (first draft NT$40,000 to 200,000, verifier recalls NT$40,000 to 2,000,000); criteria in force 2019-07-01 | https://www.mohw.gov.tw/cp-16-58777-1.html | low-medium |

## E. Recalled and computed items (no URL opened; verify before use)

| ID | File | Claim | Where to verify | Confidence |
|---|---|---|---|---|
| LG-U1 to U4 | legal U1-U4 | Fair Trade Act Art. 21 (false/misleading representations; joint liability for agency, medium and endorser when they knew or should have known; ordinary-consumer exception); Art. 42 fine tier; civil remedies; FTC 薦證廣告規範說明 detail (genuine experience, conspicuous disclosure, substantiation) | https://law.moj.gov.tw ; https://www.ftc.gov.tw | unverified |
| LG-U5, U6 | legal U5-U6 | AI Basic Act effect date rule (中央法規標準法 Art. 13) and content (framework; NSTC authority; MODA risk framework; no direct private-sector penalty) | https://law.moj.gov.tw | unverified |
| LG-U7 | legal U7 | Fraud Act article detail beyond what the press reports | https://law.moj.gov.tw | unverified |
| LG-U8 to U11 | legal U8-U11; niches [U] | Food Act Art. 28 認定準則; Health Food Control Act Art. 14; Cosmetics Act Art. 10 and TFDA claim lists; Medical Care Act ad articles, Pharmaceutical Affairs Act, Medical Devices Act | https://law.moj.gov.tw ; https://www.fda.gov.tw ; https://www.mohw.gov.tw | unverified |
| LG-U12, U13 | legal U12-U13; niches [U] | Securities Investment Trust and Consulting Act (Art. 4, 16, 107; unlicensed advice may carry imprisonment); banking, insurance, virtual-asset rules | https://law.moj.gov.tw ; https://www.fsc.gov.tw ; https://www.sfb.gov.tw | unverified |
| LG-U14 to U17 | legal U14-U17; monetisation G12 | Income Tax Act Art. 14 categories; 183-day residency and non-resident withholding; business tax (recalled 5% / 1%) and 統一發票; 商號 vs 有限公司 registration. No fee, timeline or rate found | https://law.moj.gov.tw ; https://www.mof.gov.tw ; https://gcis.nat.gov.tw | unverified |
| LG-U18, U19 | legal U18-U19; monetisation U2 | Trademark Act (first-to-file, 10-year term, agent for foreign applicants); copyright requires human authorship, TIPO view that purely AI output is not a work | https://www.tipo.gov.tw ; https://law.moj.gov.tw | unverified |
| LG-U20 to U22 | legal U20-U22 | Civil Code Art. 18 and 195; Personal Data Protection Act duties; Consumer Protection Act Art. 22 and distance-selling rules | https://law.moj.gov.tw | unverified |
| MO-U1 | monetisation U1 | LINE Creators Market creator share about half of net sales | https://creator.line.me/en/terms/ | unverified |
| MO-U3 to U6 | monetisation U3-U6 | AppWorks is an accelerator, not an affiliate network; Meta payout programmes launch in the US first; Pinkoi, Vocus, PressPlay, ECPay exist; Amazon has no Taiwan storefront | none opened | unverified |
| CU-U1 to U16 | culture U1-U16 | Vocabulary pairs (110), particles, 台語/客語, 注音文, slang watchlist, converter traps, platform tone, public-holiday rules incl. 2025 amendment, retail calendar, tax calendar, folk beliefs, Indigenous/LGBTQ+ terms, sensitive dates incl. local elections 2026-11-28, visual details, neighbourhoods, age of majority, climate | native reviewer sign-off; https://www.dgpa.gov.tw ; https://www.mof.gov.tw ; Central Election Commission | unverified |
| CU-C1 to C6 | culture C1-C6 | Lunar-calendar dates 2026-2027 (除夕 2027-02-05; 初一 2027-02-06; ghost month 2027-08-02 to 08-31; etc.) computed with lunardate 0.3.0 and cross-checked with ephem 4.2.1 (UTC+8); weekdays and day counts; solar-term times; sexagenary years. 初一 2027 new moon is at 23:56, a 4-minute margin | local computation; confirm with the Taiwan government almanac | high (arithmetic); medium until matched to the almanac |
| BR-1 | BRIEF.md, DECISIONS.md | Ground rules, language rules and operator constraints | /home/user/Taiwan-AI-Influencers/BRIEF.md ; DECISIONS.md | operator-provided |
| SY-1 | SUMMARY.md | Native zh-TW reviewer cost per post/hour: **not found**. Planning range in SUMMARY.md is an assumption, not a sourced figure. A search for freelance proofreading rates was refused (search budget used up) | n/a | unverified (assumption) |

## F. Items to open first (to turn "medium" into "verified")

1. Fair Trade Act (公平交易法) text and FTC 薦證廣告規範說明, law.moj.gov.tw and ftc.gov.tw.
2. AI Basic Act (人工智慧基本法): promulgation vs effective date, authority, any labelling duty.
3. Fraud Crime Hazard Prevention Act (詐欺犯罪危害防制條例) ad chapter; the Meta fine report (decision date, articles).
4. Instagram Help "recommendations" page and a test professional account (is the "AI-generated profile" label available in Taiwan?).
5. LINE OA Manager (billing unit per broadcast) and the LINE Biz price notice; LINE Creators Market terms.
6. NCC report PDF; MIC release id=744 and the Aug 2026 video survey.
7. YouTube Studio Earn tab; YPP announcement of 2026-08-10.

## G. Phase 4 pipeline tools (added 2026-10-12, from pipeline/tools.md)

All rows were read as web-search result summaries on 2026-10-12 (the page-fetch tool failed with DNS errors for ai.google.dev and developers.openai.com). **No page was opened.** Prices are list prices reported by the source, not checked against an invoice; model names and prices change often. Currency US$ unless stated. Date accessed: 2026-10-12.

| ID | File(s) and local ids | Claim | URL | Confidence |
|---|---|---|---|---|
| PT1 | tools.md PT1 | Gemini 2.5 Flash Image uses 1,290 tokens per image | https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash-image | medium |
| PT2 | tools.md PT2 | Flash Image list price about US$0.039 to 0.04 | https://anotherwrapper.com/tools/llm-pricing/image-models/gemini-25-flash-image-nano-banana ; https://www.getmaxim.ai/bifrost/llm-cost-calculator/provider/gemini/model/gemini-2.5-flash-image | low (aggregators) |
| PT3 | tools.md PT3 | Nano Banana Pro US$0.134 (1K/2K), 0.24 (4K); Nano Banana 2 tiers; reference input charge | https://benchlm.ai/md/media-pricing/nano-banana.md (says it read Google's pricing page 2026-09-11) ; https://www.myarchitectai.com/blog/nano-banana-api-pricing | low to medium |
| PT4 | tools.md PT4 | Gemini image docs: reference-image limits, SynthID statement, preview-model deprecation (conflicting pages) | https://ai.google.dev/gemini-api/docs/image-generation ; https://ai.google.dev/gemini-api/docs/changelog | medium (summary) |
| PT5 | tools.md PT5 | Gemini API Additional Terms: no ownership claim over generated content | https://ai.google.dev/gemini-api/terms | medium (summary) |
| PT6 | tools.md PT6 | Paid tier data not used to improve products; free tier may be | https://ai.google.dev/gemini-api/docs/billing ; https://ai.google.dev/gemini-api/docs/pricing | medium (summary) |
| PT7 | tools.md PT7 | gpt-image-1.5 per-image prices and token rates | https://developers.openai.com/api/docs/models/gpt-image-1.5 | medium (summary) |
| PT8 | tools.md PT8 | gpt-image-2 release date and conflicting prices | https://pricepertoken.com/image/model/openai-gpt-image-2 ; https://aireiter.com/blog/gpt-image-2-api-pricing | low |
| PT9 | tools.md PT9 | gpt-image-1 retirement 2026-10-23; gpt-image-1.5 and -mini listed | https://pricepertoken.com/gpt-image-pricing | low (one site) |
| PT10 | tools.md PT10 | C2PA and SynthID in images from ChatGPT, Codex and the API (announced 2026-05-19) | https://help.openai.com/en/articles/8912793-c2pa-in-chatgpt | medium (summary) |
| PT11 | tools.md PT11 | OpenAI output ownership and commercial use, as summarised by third parties | https://terms.law/ai-output-rights/chatgpt/ | low |
| PT12 | tools.md PT12 | FLUX.2 per-megapixel prices; [dev] licence conflict | https://help.bfl.ai/articles/7686530342-flux-2-pricing-guide | medium (price), low (licence) |
| PT13 | tools.md PT13 | Imagen 4 tier prices | https://blog.laozhang.ai/en/posts/ai-image-api-pricing-comparison | low (reseller) |
| PT14 | tools.md PT14 | No official Midjourney API; plan range; terms bar automation | https://unifically.com/blogs/midjourney-api | low (vendor) |
| PT15 | tools.md PT15 | Azure Speech billed per character; zh-TW voice names | https://azure.microsoft.com/zh-tw/pricing/details/speech/ ; https://json2video.com/ai-voices/azure/voices/zh-tw-hsiaochenneural/ | low to medium |
| PT16 | tools.md PT16 | ElevenLabs Taiwan Mandarin voice listing; plan prices | https://www.famulor.io/voices/elevenlabs/languages/zh/accents/taiwan-mandarin ; https://www.aiworthit.com/blog/elevenlabs-review/ | low |
| PT17 | tools.md PT17 | Video API per-second prices | https://rangy.ai/blog/veo-vs-kling-vs-runway ; https://modelslab.com/blog/api/veo-3-1-vs-kling-3-sora-2-ai-video-api-cost-2026 | low |
| PT18 | tools.md PT18 | Lip-sync and avatar tool prices | https://dupple.com/learn/best-ai-lip-sync-tools ; https://creatify.ai/blog/heygen-vs-synthesia-(2026)-pricing-avatars-and-which-one-fits-your-team | low |
| PT19 | tools.md PT19 | How to allow network hosts and add secrets in the cloud environment | https://code.claude.com/docs/en/cloud-environments#network-access | medium (given by the environment documentation) |

