# Phase 4 tools: image, voice, video and lip-sync compared

Written 2026-10-12 for the operator (English; zh-TW terms beside Taiwan-specific words). Research, not legal advice.

**Status in one paragraph.** Nothing here has been tested. No image was generated through any API, no text-to-speech voice was heard, no licence page was read in full. Every price and every licence statement comes from **search-result summaries** read on 2026-10-12; the page-fetch tool failed (DNS error for `ai.google.dev` and `developers.openai.com`), so **no primary page was opened**. Labels: *secondary* = a third-party page that reports a primary fact; *unverified* = single mention, recalled, or sources disagree; *UNTESTED* = we have not tried it; *assumption* = a planning number of mine; *computed* = arithmetic done in this session. Prices are list prices in US$ and are converted at **NT$32 per US$ (assumption, check the day's rate)**. Model names change fast: a search summary of the Gemini release notes says two image preview models were deprecated with a shut-down date of 2026-06-25, and one aggregator says `gpt-image-1` retires on 2026-10-23 (both *secondary*, one source each). So **the scripts hard-code no model id**; you pass the id you copy from the provider's current model page.

---

## 1. What the pipeline needs

Scope today: **photoreal AI stills** for the three pilots 方寸, 步驟, 色環 (`DECISIONS.md` 2026-10-11 and 2026-10-12). Diagrams, badges and every Chinese character on an image are **human-built in a design tool**, never generated. Video, voice and lip-sync are out of scope for you ("everything except the videos") and `pipeline/image-pack/README-photoreal.md` section 1 says no voice, video or lip-sync on a photoreal face until a separate addendum and review exist, so section 4 is short on purpose.

A usable still tool must: hold one face across many images from a reference (R01); return text-free pictures; give us the file untouched (so provider marks stay); have terms that allow commercial use on the plan we use; and cost well inside NT$5,000 to 10,000 a month. The binding limit is **human QA time and licence certainty, not image price** (section 5).

---

## 2. Still-image tools

Consistency ratings are **hypotheses from documentation summaries, not results**. The only way to settle them is the bake-off in 3.3.

| Tool (official API?) | How it keeps a face (hypothesis) | Price per image, list (*secondary*, 2026-10-12) | Licence and terms found | Marks in the file | Fit |
|---|---|---|---|---|---|
| **Gemini API, "Nano Banana Pro" / Gemini 3 Pro Image class** (yes; REST `generateContent`) | Accepts reference images in the prompt. A search summary of the docs lists up to 6 object and 5 character references plus style references for this class; the same summary conflicts with the Gemini 3 developer guide, so *unverified* | US$0.134 at 1K or 2K, US$0.24 at 4K (about NT$4.3 and NT$7.7, *computed*); one source says uploaded reference images are charged on top (about US$0.067 each, one source, *unverified*) | Gemini API Additional Terms: Google does not claim ownership of generated content, may generate the same or similar content for others, and the content must comply with law (attribution may be required). Paid tier: prompts and responses not used to improve Google products; free tier: they may be (docs summaries) | Docs summary: every output carries a **SynthID** watermark. Not verified in a file | **Best first candidate** |
| **Gemini API, "Nano Banana 2" / Flash-class** (yes) | Same mechanism; a summary lists up to 10 object plus 4 character references | US$0.045 (0.5K), 0.067 (1K), 0.101 (2K), 0.151 (4K); older 2.5 Flash Image about US$0.039 (1,290 output tokens per image per the Vertex doc) | As above | As above | Cheap variants and drafts |
| **Imagen 4** (Gemini API and Vertex) | Text-to-image; no sign of reference conditioning in what I found (*unverified*), so weaker for one fixed face | Fast 0.02, Standard 0.04, Ultra 0.06 (a reseller blog, low confidence) | Not checked | Not checked | Not a consistency tool; skip |
| **OpenAI Images API, gpt-image-1.5** (yes; `/v1/images/generations` and `/v1/images/edits`) | The edits endpoint takes input images (recalled; `input_fidelity` option recalled, *unverified*) | OpenAI model page via search: 1024x1024 low 0.009, medium 0.034, high 0.133; 1024x1536 low 0.013, medium 0.05, high 0.20 | Summaries of OpenAI's terms: output rights assigned to you "to the extent permitted by law", commercial use allowed if you comply with the terms and usage policies; outputs may not be unique to you; the realistic-people rules were **not found** | OpenAI help page (via search): images from ChatGPT, Codex **and the API** carry C2PA metadata and SynthID, announced 2026-05-19 | **Best second candidate** |
| **OpenAI gpt-image-2** (reported released 2026-04-21) | Same family | Only third-party figures that disagree (about 0.006 / 0.053 / 0.211 at 1024x1024 in one place, 0.009 / 0.034 / 0.133 in another) | Not checked | Probably as above | Read the model page before choosing between 1.5 and 2 |
| **FLUX.2 (Black Forest Labs API)** (yes) | Multi-reference editing is advertised (*unverified*) | From about US$0.03 per megapixel for [pro], 0.06 [flex], 0.07 [max], [klein] 4B from 0.014 (BFL guide via search) | **Conflicting**: one source calls [dev] non-commercial, another lists it as free on the API. Read BFL's licence page first | Not checked | Possible third bake-off arm only if the licence is clear |
| **Midjourney** (**no official API** found as of mid-2026; vendor-written sources only) | Has reference features in the web app (recalled) | US$10 to 120 a month plans (vendor source) | Secondary sources say the terms bar automated access; unofficial wrappers exist | Not checked | **Not usable by Claude** (Ground rule 9: no ToS-breaking automation). Manual use by you is your choice |
| **Ideogram, Seedream (ByteDance), Stable Diffusion with a trained LoRA** | SD plus a LoRA trained on our own generated images is the strongest consistency method in principle, but needs a GPU, skills and hours we do not have | Not assessed | Per-model licences, not assessed | n/a | Not assessed. Seedream's vendor is mainland-linked: a data and reputation question for a Taiwan studio. Revisit only if both APIs fail the bake-off |

**What the table cannot tell us:** whether any of these keeps *our* faces consistent over 16 images, whether they print stray text, how they treat East Asian faces, or whether a photoreal 32-year-old woman comes out looking 22. Those are the questions the packs' 31-row checklist and the age-guess test answer, on real images.

### 2.1 Licence points to settle before any commercial use

From `README-photoreal.md` section 5.7, restated for the API path. **Until a human has read the current text and recorded it in `licence_notes`, every image is internal design material.** Read for the exact tool and plan: who owns the output; commercial use allowed on that plan; limits on using outputs as a recurring character; **what the terms say about realistic images of people and any disclosure duty**; what they say about visible marks, SynthID and C2PA metadata and about removing them (we never remove them); rules about uploaded reference images (we upload only the character's own images); last-changed date. Save a dated screenshot or PDF. Also a lawyer question (`research/legal.md` 8.2): purely AI-generated images may not be protected by copyright in Taiwan (recalled, *unverified*), which weakens licensing.

---

## 3. Claude running image generation itself

### 3.1 What it needs from you (Claude cannot do these)

1. **An API key, which is a different product from your app subscription.** Gemini and ChatGPT subscriptions are billed separately from the Gemini API and the OpenAI API (assumption: true for your plans; check your account pages). Create a key in Google AI Studio and/or the OpenAI developer console and **turn on billing**. For Gemini use a billing-enabled (paid-tier) project: the docs summaries say free-tier prompts and outputs may be used to improve Google products and paid-tier ones are not. OpenAI may require organisation verification for its image models (recalled for gpt-image-1, *unverified*).
2. **Put the key in the cloud environment, never in the chat.** In the environment settings (cloud environment menu in the session title bar, then Edit), add it under *Network secrets* (called *API credentials* in older apps) or as an environment variable. The variable names the scripts read are `GEMINI_API_KEY` and `OPENAI_API_KEY`. A new session picks them up. Never paste a key into chat, a file or a commit.
3. **Allow the two hosts.** On 2026-10-12 this session could not resolve `ai.google.dev` or `developers.openai.com`, so assume the API hosts are blocked until allowed. In the same settings screen, under Network access, add `generativelanguage.googleapis.com` and `api.openai.com` to *Allowed domains* (steps: https://code.claude.com/docs/en/cloud-environments#network-access). Whether that screen offers per-host rules on your plan is *unverified*.
4. **Set a hard monthly spend limit in each provider's console.** The scripts have a daily call cap (default 40, `GEN_IMAGE_MAX_PER_DAY`) but it is not a billing cap.
5. **Read and record the licence terms** (2.1).

### 3.2 What the scripts do (all UNTESTED against live APIs)

`pipeline/scripts/gen_image.py` builds the request for either provider, **sends nothing unless the key variable is set and `--dry-run` is off**, writes the returned bytes untouched, then appends a validated row to `assets/provenance.csv`. It refuses prompts that name real people or existing characters (a keyword list, not clearance), refuses `--reference` files outside `assets/<persona>/` (and anything in a `lookalike` folder), and never overwrites a file. Request shapes were written from memory of the public APIs and need a first-run check. Run `--dry-run` to see the exact request and the row it would write. Details: `pipeline/README.md`.

**What Claude still cannot do with a key:** judge a face for resemblance to a real person (Claude does not identify real people from faces and must not be asked), decide that a picture is on-voice or Taiwanese enough, or approve anything. Claude can read a saved image against the checklist for a first pass; your wife and you make the calls (`qa-checklist.md`).

### 3.3 Gemini image API vs OpenAI image API vs others, for photoreal consistent characters

Hypotheses only. "Test" is what the bake-off measures.

| # | Question | Hypothesis (unverified) | Test |
|---|---|---|---|
| H1 | Which holds one face better across 8 follow-ups with R01 attached? | Gemini's explicit "character reference" slots help; OpenAI's edits endpoint may drift more in face shape but follow clothing better. Either could be wrong | Same R01, same 8 follow-up prompts (angle, expression, outfit), blind to tool; count rows 2, 3 and 4 of the pack checklist failures |
| H2 | Which makes less plastic skin and fewer dead eyes (the user's own complaint)? | Higher-quality tiers help; Pro-class Gemini and OpenAI `high` may be closer than the cheap tiers | Checklist row 25 and the uncanny score at 100% and 200% |
| H3 | Which leaks text, numerals or hex codes into the picture? | Both sometimes; named colours in words reduce it | Rows 16 and 20 |
| H4 | Which gives the fewest hand and tooth defects when hands are kept out of frame? | Similar; framing rules matter more than the tool | Rows 8 and 10 |
| H5 | Which drifts toward a young or idol face? | Both; the age-cue phrases in the packs help | Age-guess panel (addendum 9.2) |
| H6 | Which respects aspect ratio 4:5? | Gemini has an aspect-ratio setting; OpenAI offers fixed sizes (recalled: 1024x1024, 1024x1536, 1536x1024) so 4:5 means a crop in post, logged as a human edit | Compare delivered sizes |
| H7 | Cost per **kept** image | Cheap tiers win per image, not necessarily per kept image | Total spend divided by images that pass all 31 rows |
| H8 | Terms | Unknown for realistic people on both | Read both texts (2.1) |

**Bake-off protocol (run once, per pilot, when a key exists):** 8 candidates of R01 per tool from the pack's own prompt; shortlist at most 3; run the full checklist and the reverse-image and age tests on the shortlist only; then 8 follow-ups (4 angles, 2 expressions, 2 outfits) from the winner's R01 in a fresh chat or call each; log time and spend per image. **Decision rule:** pick the tool with the lower failure rate on rows 2 to 4 and 25; break a tie on cost per kept image; if both fail the same way twice, stop and tell Claude (the design may need a change, not a better tool).

---

## 4. Voice, video and lip-sync (brief; out of scope for you)

Photoreal faces plus a synthetic voice or lip-sync come closest to a deepfake and each addendum bars them until a separate review. Nothing below is recommended for purchase now.

**Text-to-speech.** Every row **UNTESTED for a Taiwanese Mandarin accent.** Do not buy any until the wife has listened.

| Option | What was found (*secondary*) | Taiwan accent | Price | Licence |
|---|---|---|---|---|
| Azure AI Speech | zh-TW neural voices named HsiaoChen, HsiaoYu, YunJhe listed on a voice directory | **UNTESTED** | Billed per character; about US$16 per million characters for neural voices in one third-party source, *unverified* | Not checked |
| Google Cloud Text-to-Speech | Taiwan Mandarin (cmn-TW) voices recalled, not found in search | **UNTESTED** | About US$16 per million for premium neural voices (one comparison, *unverified*) | Not checked |
| ElevenLabs | A marketplace page lists 12 voices labelled "Taiwan Mandarin accent"; nobody rated their naturalness | **UNTESTED** | Starter about US$5 to 6 a month with a commercial licence, Creator about US$22 (blogs disagree) | Per plan; read before use |
| OpenAI TTS, Gemini TTS | Mandarin support recalled | **UNTESTED**, accent unknown | Not checked | Not checked |

*Accent test for your wife (a 5-minute script, per voice):* 6 sentences with Taiwan vocabulary (影片, 資訊, 軟體, 坪, 捷運), numbers and dates (二〇二六年十月十二日), 不 and 一 tone changes, neutral-tone words, and no rolled "兒" endings. She rules: Taiwanese accent yes or no, any mainland pronunciation, robotic rhythm. Any synthetic voice also needs the on-screen label 「AI 生成語音」 (bible 8.3).

**Video.** Per-second API prices reported by blogs, *secondary and inconsistent*: Veo 3.1 tiers about US$0.05 to 0.40 a second, Kling 3.0 about 0.09 to 0.16, Runway about 0.05 to 0.20. Character consistency across shots, Taiwan faces and licence terms are **all UNTESTED and unchecked**. Ten seconds at US$0.15 a second is about US$1.5, so cost is not the problem; consistency, the deepfake line and 30-day human approval are.

**Lip-sync and avatar tools.** HeyGen (API from US$5 pay-as-you-go; about 20 credits a minute for its newest avatar tier, per one comparison), Sync Labs (lip-sync API, entry price about US$5 a month plus per-second use), Hedra (no price found). Mandarin support and Taiwan accent: **not confirmed for any**. UNTESTED.

---

## 5. Recommended stack inside NT$5,000 to 10,000 a month

**Recommendation (a proposal for you to accept or change):**

1. **Stills, primary: Gemini API on a paid-tier project**, a Pro-class model for R01 masters and a Flash-class model for variants and drafts. **Secondary: OpenAI Images API** (`gpt-image-1.5` or `-2`, whichever the model page recommends) as the bake-off rival. Run the 3.3 bake-off on 方寸 first, then keep one primary and one fallback. This is a hypothesis-based pick; the bake-off can overturn it.
2. **Until a key exists, nothing is blocked:** you run the packs' prompts in the Gemini and ChatGPT apps as planned in `README-photoreal.md`, and log each file with `provenance.py`. The API path is faster for Claude, not required.
3. **Badges, diagrams and all Chinese text:** a design tool you already have or a free tier, with a Taiwan-glyph font (Noto Sans TC, free; licence recalled as the SIL Open Font License, *unverified*).
4. **Voice, video, lip-sync: buy nothing.** Reopen after the photoreal stills pass the age, look-alike and uncanny tests and a voice addendum exists.
5. **Posting:** native tools only (`COSTS.md`).

**Monthly cost model** (*computed*; volumes are *assumptions*: steady state 240 generations a month, about 60 kept images at 4 tries each; set-up of the three golden sets 300 generations; NT$32 per US$; reference inputs add cost I could not pin down):

| Tier | Per image (NT$) | Steady month (NT$) | Set-up month (NT$) |
|---|---|---|---|
| Gemini Flash-class 1K (0.067 USD) | 2.1 | 510 | 640 |
| Gemini Pro-class 1K or 2K (0.134 USD) | 4.3 | 1,030 | 1,290 |
| Gemini Pro-class with 2 paid reference inputs (about 0.268 USD, one-source guess) | 8.6 | 2,060 | 2,570 |
| OpenAI 1024x1536 medium (0.05 USD) | 1.6 | 380 | 480 |
| OpenAI 1024x1536 high (0.20 USD) | 6.4 | 1,540 | 1,920 |
| Five times the volume at Gemini Pro with references | | 10,290 | |

**Budget lines** (replaces the image and video allocations in `strategy/portfolio.md` section 7; base case NT$5,000):

| Line | NT$ a month | Note |
|---|---|---|
| Image API spend, hard-capped in the provider consoles | 2,500 | Covers every row above except the five-times case; the daily call cap protects against loops |
| Extra image credits or a second tool | 500 | Bake-off rival |
| Design and template tool | 500 | Badges, diagrams |
| Link page hosting and domain | 300 | Unchanged |
| Video, voice, lip-sync | **0** | Not bought; reopen only after a voice and video addendum |
| Contingency | 1,200 | The old video and voice allocation (2,800) is released into this and the image line |
| **Total** | **5,000** | NT$10,000 headroom only if a tool clearly earns it |

---

## 6. Open items for you

1. Decide whether to supply API keys (3.1). Without them Claude cannot generate images; the app route still works.
2. If yes: add the two hosts to the allowed domains, add the key as a secret, set provider spend limits, confirm billing is on.
3. Read and record the commercial-use terms for each tool and plan you use (2.1). Until then nothing leaves the studio.
4. Give your wife the voice test script only when voice is reopened.
5. Tell Claude your real monthly Claude, Gemini and ChatGPT costs for `COSTS.md`.
6. Check one current model id for each provider and pass it with `--model`.

---

## 7. Sources (all read as search-result summaries on 2026-10-12; none opened). Also in `SOURCES.md` section G

| ID | What it supports | URL | Confidence |
|---|---|---|---|
| PT1 | Gemini 2.5 Flash Image uses 1,290 tokens per image | https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash-image | medium |
| PT2 | Flash Image list price about US$0.039 to 0.04 | https://anotherwrapper.com/tools/llm-pricing/image-models/gemini-25-flash-image-nano-banana ; https://www.getmaxim.ai/bifrost/llm-cost-calculator/provider/gemini/model/gemini-2.5-flash-image | low (aggregators) |
| PT3 | Nano Banana Pro US$0.134 (1K/2K), 0.24 (4K); Nano Banana 2 tiers; reference input charge | https://benchlm.ai/md/media-pricing/nano-banana.md (says it read Google's pricing page 2026-09-11) ; https://www.myarchitectai.com/blog/nano-banana-api-pricing | low to medium |
| PT4 | Gemini image docs: reference-image limits, SynthID statement, preview-model deprecation (conflicting pages) | https://ai.google.dev/gemini-api/docs/image-generation ; https://ai.google.dev/gemini-api/docs/changelog | medium (summary) |
| PT5 | Gemini API Additional Terms: no ownership claim over generated content | https://ai.google.dev/gemini-api/terms | medium (summary) |
| PT6 | Paid tier data not used to improve products; free tier may be | https://ai.google.dev/gemini-api/docs/billing ; https://ai.google.dev/gemini-api/docs/pricing | medium (summary) |
| PT7 | gpt-image-1.5 per-image prices and token rates | https://developers.openai.com/api/docs/models/gpt-image-1.5 | medium (summary) |
| PT8 | gpt-image-2 release date and conflicting prices | https://pricepertoken.com/image/model/openai-gpt-image-2 ; https://aireiter.com/blog/gpt-image-2-api-pricing | low |
| PT9 | gpt-image-1 retirement 2026-10-23; gpt-image-1.5 and -mini listed | https://pricepertoken.com/gpt-image-pricing | low (one site) |
| PT10 | C2PA and SynthID in images from ChatGPT, Codex and the API (announced 2026-05-19) | https://help.openai.com/en/articles/8912793-c2pa-in-chatgpt | medium (summary) |
| PT11 | OpenAI output ownership and commercial use, as summarised by third parties | https://terms.law/ai-output-rights/chatgpt/ | low |
| PT12 | FLUX.2 per-megapixel prices; [dev] licence conflict | https://help.bfl.ai/articles/7686530342-flux-2-pricing-guide | medium (price), low (licence) |
| PT13 | Imagen 4 tier prices | https://blog.laozhang.ai/en/posts/ai-image-api-pricing-comparison | low (reseller) |
| PT14 | No official Midjourney API; plan range; terms bar automation | https://unifically.com/blogs/midjourney-api | low (vendor) |
| PT15 | Azure Speech billed per character; zh-TW voice names | https://azure.microsoft.com/zh-tw/pricing/details/speech/ ; https://json2video.com/ai-voices/azure/voices/zh-tw-hsiaochenneural/ | low to medium |
| PT16 | ElevenLabs Taiwan Mandarin voice listing; plan prices | https://www.famulor.io/voices/elevenlabs/languages/zh/accents/taiwan-mandarin ; https://www.aiworthit.com/blog/elevenlabs-review/ | low |
| PT17 | Video API per-second prices | https://rangy.ai/blog/veo-vs-kling-vs-runway ; https://modelslab.com/blog/api/veo-3-1-vs-kling-3-sora-2-ai-video-api-cost-2026 | low |
| PT18 | Lip-sync and avatar tool prices | https://dupple.com/learn/best-ai-lip-sync-tools ; https://creatify.ai/blog/heygen-vs-synthesia-(2026)-pricing-avatars-and-which-one-fits-your-team | low |
| PT19 | How to allow network hosts and add secrets in the cloud environment | https://code.claude.com/docs/en/cloud-environments#network-access | medium (given by the environment documentation) |
