# pipeline/: from a one-line idea to a labelled, compliant post

Written 2026-10-12 (Phase 4). For the operator (English; every zh-TW string is an AI draft for the wife). **Nothing in this folder has produced a public post.** No image-generation API key exists, no live API has ever been called, and the two image adapters are **UNTESTED**.

## 1. What is here

| Path | What it is |
|---|---|
| `tools.md` | Image, voice, video and lip-sync tools compared; what Claude-run generation needs from you; the recommended stack and monthly cost model. Prices are secondary, licence terms are not yet read |
| `qa-checklist.md` | The checks every draft passes before a human approves it: disclosure, faces, hands, text, motion, voice, lived-experience wording, look-alike, Taiwan details, timing |
| `scripts/` | Three command-line tools, standard library only: `provenance.py`, `gen_image.py`, `queue.py` (logic in `reviewqueue.py`, word lists in `ground_rules.py`), plus tests |
| `review-queue/<persona>/<YYYY-MM-DD>_<NN>/` | One folder per draft post: `post.json` and `media/` (with `.gitkeep`) |
| `image-pack/` | Copy-and-paste prompt packs for you to run in the Gemini and ChatGPT apps (start at `image-pack/README-photoreal.md`) |
| `art/` | The superseded code-drawn 步驟 art script (kept as a record) |
| `../assets/provenance.csv` | The log of every asset: `timestamp,asset_path,persona,tool,model,prompt,licence_notes` |

## 2. How a one-line idea becomes a compliant labelled post

Example idea (not a real post): 「一句話：房門打開時會佔掉多少地板？」 for 方寸 on Instagram.

| Step | Who | What happens | Command or place |
|---|---|---|---|
| 1 | You | Give Claude the idea, the persona and the date | Chat |
| 2 | Claude | Picks the pillar and format from the bible, checks the date against the calendar rules (228, ghost month, election day, typhoon pause) | `personas/<slug>/bible.md` section 6 |
| 3 | Claude | Scaffolds the draft | `python3 pipeline/scripts/queue.py new-draft --persona fangcun --platform instagram --format carousel --date 2026-11-24 --pillar "尺寸算給你看"` |
| 4 | Claude | Fills `hook_zh`, the caption body, `caption_gloss_en` (English for you), hashtags, `sources` (claim, URL, date; arithmetic-only posts say so), and each media entry as `PENDING` with a `shot_prompt`. The scaffold already starts the caption with the AI disclosure line, sets the label 「AI 生成｜虛擬角色」, `ai_label_flag` true, and review `pending / pending / false` | `post.json` |
| 5 | Claude | Pre-screens | `python3 pipeline/scripts/queue.py validate <draft folder>` (fix every ERROR and FLAG; read every WARN and INFO) |
| 6 | You, or Claude with a key | Makes the pictures. **No key:** you run the shot prompt in the Gemini or ChatGPT app (packs in `image-pack/`), download with the app's button, save under `assets/<persona>/photoreal/`. **With a key:** `gen_image.py` (section 4) | App, or script |
| 7 | You, or Claude | Logs every file the same day | `python3 pipeline/scripts/provenance.py add --asset ... --persona ... --tool ... --model ... --prompt-file ... --licence-notes ...` (`gen_image.py` does this itself) |
| 8 | You | Runs the image checks: 31-row pack checklist at 100% and 200%, hands first; age-guess and look-alike tests on a master | `qa-checklist.md` sections 3 to 5, 9 |
| 9 | You | Adds the badge 「AI 生成｜虛擬角色」 or 「AI 生成｜示意圖」, all Chinese text and diagrams in a design tool (never generated); sets each `media[].path` to the final file | Design tool |
| 10 | Your wife | Reads everything on the post: Traditional Chinese, Taiwan vocabulary, tone, culture, taboos. Sets `review.wife_language` to `approved` or `changes`, reason codes in `review.notes` | Edit `post.json` |
| 11 | You | Checks facts against `sources`, sets `review.operator_facts` | Edit `post.json` |
| 12 | You | If both are `approved`, you set `review.approved` to `true`. **Only a human does this**, for every post in at least the first 30 days | Edit `post.json` |
| 13 | You | Schedules with the platform's own tool; switches on the platform AI label by hand (and the paid-partnership tool if sponsored); screenshots the four disclosure places | `python3 pipeline/scripts/queue.py approve <draft folder>` shows what is still open |

`queue.py list` shows every draft with its status: `incomplete` (scaffold not filled), `invalid` (errors), `flagged` (banned wording to edit), `awaiting-both`, `awaiting-wife`, `awaiting-operator`, `changes-requested`, `ready-for-final-approval`, `approved`.

## 3. What runs without a key

Everything except actually calling an image API. No script in this folder makes a network call unless a key variable is set **and** `--dry-run` is off.

| Works today with no key and no network | Needs a key |
|---|---|
| `queue.py` new-draft, validate, list, approve (report only) | `gen_image.py` without `--dry-run` |
| `provenance.py` add and check | |
| `gen_image.py --dry-run` (prints the exact request, key masked, and the provenance row; needs no key) | |
| The prompt blocklist, the reference-folder rule and the output-path rule (run before anything else) | |
| All tests | |
| The image-pack route: you generate in the apps and log with `provenance.py` | |

## 4. gen_image.py (UNTESTED against live APIs)

```
python3 pipeline/scripts/gen_image.py --provider gemini --persona fangcun \
    --out assets/fangcun/photoreal/R01_cand_gemini_api_1.png --model <exact model id> \
    --prompt-file prompt.txt [--reference assets/fangcun/photoreal/R01_master_v1.png] \
    [--aspect-ratio 4:5] [--dry-run]
```

* The key comes **only** from `GEMINI_API_KEY` or `OPENAI_API_KEY` in the environment. It is never accepted as an argument, never printed, never written to the log, and is scrubbed from error text. Without it the script exits with code 3 and says why.
* `--model` (or `GEMINI_IMAGE_MODEL` / `OPENAI_IMAGE_MODEL`) is required for a real run and has **no default**: copy the id from the provider's current model page. Request shapes, endpoints and response fields were written from memory and search summaries; expect to fix them on the first real run.
* It **refuses** (exit 4, before any spend): a prompt that names a real person, celebrity, existing character or franchise (seed list plus `scripts/blocklist_extra.txt`) or uses "looks like" or "in the style of" with a name; a `--reference` that is not under `assets/<persona>/` (so no photo of a real person, no other persona's image, nothing from a `lookalike` folder); more than 3 references; an output path outside `assets/<persona>/` or one that already exists; and, past the daily call cap (default 40, `GEN_IMAGE_MAX_PER_DAY`), any further call. The blocklist is a keyword check, **not** clearance: look-alike tests are still required on every face.
* It writes the returned bytes **exactly as received** (nothing re-encoded, nothing stripped, so any SynthID or C2PA mark stays), warns if the file type does not match the name, and appends a validated provenance row. The row is checked before the call, so a spend is never followed by a refused log. If the image is written but the log fails, it exits 6 and tells you to log it by hand today.
* It never works around a provider refusal: a blocked prompt is reported and you tell Claude.
* Exit codes: 0 ok or dry-run; 2 bad arguments; 3 inert (no key); 4 refused; 5 provider or network failure; 6 written but not logged.

**DEMO output** (a dry run with a placeholder model id; nothing sent, no file written, abbreviated):

```
DRY RUN: nothing sent, nothing written. UNTESTED request shape.
POST https://generativelanguage.googleapis.com/v1beta/models/MODEL-ID-HERE:generateContent
  header x-goog-api-key: ***(from env, not printed)
  body: { "contents": [{"role": "user", "parts": [{"text": "An original adult woman, ..."}]}],
          "generationConfig": {"responseModalities": ["TEXT","IMAGE"], "imageConfig": {"aspectRatio": "4:5"}} }
provenance row that would be appended after a successful write:
  asset_path: assets/fangcun/photoreal/DEMO_not_generated.png   persona: fangcun
  tool: Gemini API (generateContent, image output)   model: MODEL-ID-HERE
  licence_notes: PHOTOREAL v2; Status: UNREVIEWED ...; commercial use per those terms: NOT CONFIRMED ...
key variable GEMINI_API_KEY: NOT set (value never printed)
```

To switch it on (your jobs, `tools.md` 3.1): create a billing-enabled API key, add it as a secret or environment variable in the cloud environment settings (never in chat), allow `generativelanguage.googleapis.com` and `api.openai.com`, set a monthly spend limit in each provider console, and read the commercial-use terms.

## 5. The review-queue format (`post.json`)

| Field | Type | Rule enforced by `queue.py validate` |
|---|---|---|
| `id` | string | `<persona>-<YYYY-MM-DD>-<NN>`, equal to the folder (`<date>_<NN>`) and its parent |
| `persona` | slug | one of the ten slugs (`fangcun, buzhou, sehuan, jiehua, zhuancheng, suisui, licheng, guige, dengyixia, guiwei`); non-pilot and lawyer-gated personas produce a WARN |
| `platform` | `instagram`, `threads`, `youtube_shorts`, `facebook` | WARN if not in the persona's planned platforms |
| `format` | `carousel`, `reel`, `short`, `text`, `image` | WARN for unusual platform pairs |
| `scheduled_date` | `YYYY-MM-DD` | WARN for 228, the recalled election date, the 2027 ghost month, before the assumed first-post date 2026-11-16 |
| `pillar`, `hook_zh`, `caption_zh`, `caption_gloss_en` | strings | not empty; the caption **starts with 【AI 虛擬角色】** and has a body |
| `hashtags` | list of `#` strings | no spaces; no follow-for-follow tags (ERROR); scanned like the caption |
| `on_screen_label_zh` | string | present and contains 「AI 生成」 |
| `ai_label_flag` | boolean | **must be true** (the studio switches the platform label on for every post) |
| `sponsorship_flag`, `sponsorship_type` | boolean, `none/paid/gifted/affiliate` | flag and type agree; the matching tag (【業配】 or 【合作內容】, 【廠商提供】, 【含分潤連結】) is in the first lines; a tag without the flag is an ERROR |
| `sources` | list of `{claim, url, date}` | required when the text makes source-dependent claims; empty `url` only for entries that begin `ARITHMETIC ONLY` or `NO FACTUAL CLAIM`; placeholders warn and block approval |
| `media` | list of `{path, description, shot_prompt}` | `path` is `PENDING` until generated (then a `shot_prompt` is required and is checked against the blocklist); a real path must exist and should have a provenance row |
| `review` | `{wife_language, operator_facts, approved, notes}` | states `pending/approved/changes`; `approved: true` is an ERROR unless both are `approved`, no media is PENDING, and no ERROR or FLAG remains |

**Banned-term scan** (`hook_zh`, `caption_zh`, hashtags, label): lived-experience words and patterns, mainland vocabulary, Simplified characters, health and weight-loss claims, investment and finance words, gambling, politics, wording that denies the AI disclosure, one persona naming or tagging another (a WARN when another persona's name is quoted, @-tagged or followed by 角色), sponsor wording while `sponsorship_type` is `none` (WARN), and unsourced superlatives. Hits are **flagged and never fixed**. A hit inside a denial sentence ("not measured by me") is downgraded to INFO so a human reads it. The lists are blunt: they miss things and flag harmless things (`ground_rules.py` documents their sources). The wife's reading is the real check.

## 6. Tests

```
python3 -m unittest discover -s pipeline/scripts -v        # from the project folder
cd pipeline/scripts && python3 -m unittest                  # or from the scripts folder
```

130 tests at the time of writing (119 by the author plus 11 added in the review); they use temporary folders, a fake transport and no network. They do not and cannot test the live APIs.

## 7. Cautions

* **`queue.py` shares its name with a standard-library module.** With this folder first on the Python path, any library that does `import queue` would get our file. `queue.py` therefore re-exports the real standard-library module when imported, and is only a command line when run (the logic is in `reviewqueue.py`). A test covers this.
* **Model ids and prices change.** Re-read `tools.md` section 2 before relying on a price.
* **The queue is shared.** Other work (content drafts) already writes drafts into `review-queue/`; `queue.py validate` reads them and never edits them.
* **Provenance is append-only.** Never edit or delete an old row; corrections are new rows at the bottom.
* **Not legal advice.** The scans enforce the project's rules as drafted; Taiwan-law statements remain unverified (`research/legal.md`).

## 8. Open items for you

1. Decide whether to supply API keys and network access (`tools.md` 3.1). Until then use the app route.
2. Read and record the commercial-use terms of each tool and plan (`tools.md` 2.1). Until then every image is internal design material.
3. Ask your wife to review the word lists in `scripts/ground_rules.py` (mainland and lived-experience terms, the Simplified-character list) and add local presenters and other public figures to `scripts/blocklist_extra.txt`.
4. Confirm the badge and first-line wording (`qa-checklist.md` section 2 repeats the drafts) and the studio rule that `ai_label_flag` is true on every post.
5. Run the bake-off in `tools.md` 3.3 once a key exists, and the first real `gen_image.py --dry-run` against the provider's current documentation.

## 9. Review log (independent skeptical review, 2026-10-12)

Reviewer read every file of the stream, ran all tests (119 passed before changes, 130 after), ran every script by hand (dry run, inert run, refusals, bad input), and checked all 17 drafts in `review-queue/` with an independent format script (fields, types, id and folder, `ai_label_flag`, pending review fields, empty `media/` with `.gitkeep`): 17 of 17 pass; no draft was edited. No API key was present in the environment and no network call was made.

**Fixed in place**
1. `queue.py list` crashed (`TypeError`) on a `post.json` whose `id` or `scheduled_date` was not a string; `queue.py approve` crashed (`AttributeError`) when `review` was not an object. Both now degrade to a table row or a "NOT APPROVED" report. Tested.
2. `provenance.py add` and `gen_image.py` printed a traceback for a missing or non-UTF-8 `--prompt-file` or `--licence-notes-file`. They now refuse with a one-line message (exit 2). Tested.
3. Scanner misses that let Ground rule 4 and 6 wording through (probed with 50 phrases): 「我昨天試了」, 「我每天都用」, 「我之前買過」, 「我一直在穿」, 「我在用」, 「我的衣櫃」, 「親自體驗」, 「這個角色用過」 (WARN), 「非 AI」/「不是 AI」/「真人拍攝」, 「改善睡眠」, 「買了會瘦」. Added, with tests.
4. A bare 「沒」 downgraded a claim to INFO: 「沒想到我親測有效」 counted as a denial. Now only a negator glued to the term, or a listed denial phrase such as 「沒有」, counts.
5. Mainland vocabulary list lacked the AI-tools and home topics the pilots write about (硬盤, 插件, 不銹鋼, 用戶, 代碼, 文檔, 界面, 裝修, 租房 and others). Added (HIGH where Taiwan has one clear form, WARN where both are heard). Two candidates were dropped because they match inside correct Taiwan words (算法 inside 演算法, 手機號 inside 手機號碼).
6. New advisory checks: another persona's name used like a name (Ground rule 8), and 業配 / 分潤 / 折扣碼 wording while `sponsorship_type` is `none` (Ground rule 5).
7. `qa-checklist.md` D3 and D4: the badge inset of "8% from every edge so a square crop of a 4:5 picture cannot remove it" is wrong vertically. A centred 1:1 crop of 4:5 removes 10% of the height at the top and at the bottom (1,350 px becomes 1,080 px). The checklist now says 11% top and bottom, 8% at the sides, and to test with a real crop.

**Not fixed here (other streams' files)**
* The same "8% from every edge" sentence was in `image-pack/README-photoreal.md`, the three `*-photoreal.md` packs, the three `personas/*/photoreal-addendum.md` files, `content/sehuan/calendar-30d.md` and two sehuan post.json files. Fixed by the integrator on 2026-10-12 to the D3 wording (11% top/bottom, 8% sides). `content/fangcun/calendar-30d.md` was already fixed. `launch/` and `content/buzhou` were not affected.
* The scanner is still a keyword net. It cannot see a lived-experience claim phrased in a way nobody listed, or a false statement. The wife's reading and the operator's fact check remain the controls.
* Every price, model id and licence statement in `tools.md` is still search-summary level; nothing was verified against a primary page in this review either (no key, no verified web access).
* The real Gemini and OpenAI request shapes are still untested; expect to fix them on the first live run.
* `ground_rules.py` word lists are unreviewed by a native speaker (HUMAN_TODO 41).
