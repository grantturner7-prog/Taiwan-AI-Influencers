# Studio-level setup: do this once, before any persona account (DRAFT v0.1, 2026-10-12)

For the operator (English; every zh-TW term is for the wife). **Nothing here has been done.** Claude cannot create an account, pass a phone or ID check, hold a credential or press any button on any platform; every step below is a human step. Platform menus, limits and rules are recalled and **unverified** (`research/platforms.md` could not open a primary page); read the live screen and trust it over this file.

## 1. People and roles

| Who | Does | Must not |
|---|---|---|
| **Operator** (6 h a week) | Creates the accounts on his own phone, passes every phone and ID check, switches on every platform AI label by hand, publishes or schedules every post after approval, keeps the evidence log | Hand a password to anyone outside the two of you; use any tool that clones, emulates or automates the apps |
| **Wife** (10 h a week; native zh-TW reader; registrant to be confirmed) | Reads and approves every Chinese string, is the second person who can recover every account, holds the registrant role if the entity is in her name (`HUMAN_TODO.md` 7), owns the domain if it is registered in her name | Be the only holder of any credential (single point of failure) |
| **Claude** | Drafts text, builds the link pages and scripts, keeps the checklists current, flags problems | Log in to anything, hold or see a credential, approve a post, press publish, create or buy an account, contact a platform |
| **Lawyer, 記帳士** | Gates in `research/legal.md` 12; ownership of accounts and characters in writing | (day-to-day content) |

## 2. What may and may not be in this repository

| In the repo | Never in the repo, in chat, or in a screenshot that is saved in the repo |
|---|---|
| Public handles and URLs once chosen; the status of each step; the text of bios and pages; the evidence **log** (`evidence-log.csv`: date, what, result, file name) | Passwords; recovery or backup codes; two-factor secrets and QR codes; API keys; phone numbers; the studio mailbox's password; ID or business documents; screenshots of settings pages (they show the personal email or phone) |

Keep the evidence screenshots in a private folder **outside** this repository (a shared private drive both of you can open) and write only the file name in the log. If a secret ever lands in git, treat it as leaked: rotate it first, then clean the history. Claude does not commit anything in this project; check `git status` before you do.

## 3. The studio mailbox (the login identity of every account)

* **Why:** if every account logs in with one person's personal email, losing that person's mailbox loses the studio. A studio-owned mailbox that both of you can open is the account owner; personal addresses are only recovery contacts.
* **Requirements:** a real, long-lived address that neither of you uses for anything else; two-factor on the mailbox first (nothing else is safe if the mailbox is not); a name that is not a persona's name and does not claim to be official, a company or a bank (no 官方, 公司 or 銀行 wording; the studio is not registered yet).
* **Options (none created, no address chosen or claimed available):** (a) a new consumer mailbox now, which is also the Google account that owns the YouTube channels (section 9); (b) a mailbox on the studio's own domain once the domain exists (section 10). Moving every account's login email later costs about 5 minutes per account, so choose once; (a) is the practical start.
* **Registrant and ownership:** write one page, with the 記帳士 or the lawyer, that says who owns the accounts, the mailbox, the domain and the characters, and what happens if one of you stops (`strategy/portfolio.md` 2.6; `HUMAN_TODO.md` 7). Not legal advice.

## 4. The password manager

* One shared vault that both of you can open, with each person's own login and a long master passphrase, and its own two-factor. Examples, not endorsements (features and prices **not checked**): Bitwarden, 1Password. If the paid tier is needed for stored authenticator codes, it is not in `COSTS.md`: take it from the NT$900 contingency (`strategy/portfolio.md` 7) and log it in `COSTS.md`.
* Each account gets one entry: login (the studio mailbox), a generated password of at least 20 characters, the authenticator secret if the manager supports it, the backup codes, the date created, and the recovery contacts. Never reuse a password.
* Keep the manager's emergency kit (master-passphrase recovery) on paper, in two places, one with each of you.

## 5. Two-factor authentication on every account

| Rule | Detail |
|---|---|
| Every account, no exceptions | The studio mailbox, the registrar and host of the link page (section 10), each Instagram, Threads (through Instagram), YouTube (through the Google account), and later any Facebook Page or LINE Official Account |
| Method | Prefer a security key or passkey where the platform offers one, then an authenticator app (the code or secret stored in the shared vault so either of you can sign in), then SMS only as a fallback. Options differ by platform (**unverified**): use the strongest one the screen offers and write down which |
| Backup codes | Generate them at set-up, store them in the vault entry and print one copy per account for the wife's envelope or safe |
| Never | Approve a login prompt you did not start; give a code to anyone, including someone who claims to be the platform |
| Re-check | Quarterly and after any change of phone: open each account's security page and confirm the methods and recovery contacts are still yours |

## 6. Recovery contacts, and phone and ID verification

**Recovery: either of you can recover everything.**

* Each account's recovery email is the **other** person's personal mailbox or the studio mailbox, and the recovery phone is the number of whoever did not create it where the platform allows two (**unverified**).
* **Recovery test, once at set-up:** the person who did not create the account follows the recovery path from their own device using only the vault and their own phone, then signs out. Do not repeat it often; repeated logins from new devices can raise security flags (*inference*).
* Single point of failure to avoid: the wife is the registrant and the only Chinese reader; if she is unavailable, culture-heavy posting pauses (`strategy/portfolio.md` 2.6) and nothing may depend on only her phone.

**Phone and ID verification (humans only).**

* You pass every code, phone check or ID or selfie check yourselves, with your own real number, on your own phone. **Never** use a purchased or rented virtual number, an SMS-receiving service, a SIM farm, an emulator or an account-creation service, and never buy, sell or "snipe" an account or a handle (Instagram's terms bar buying and selling accounts, `research/platforms.md` 4.1).
* Whether one phone number may verify several Instagram, Threads or YouTube accounts is **unverified** (`research/platforms.md` 4.1: "multiple accounts need separate phone numbers: not found"). If a platform refuses a reused number, stop and tell Claude; do not look for a workaround.
* The date-of-birth field belongs to the human who creates the account. Enter that person's real date, never the character's stated age as a birth date (the platforms' terms govern; **unverified**).
* ID checks, if a platform asks for one, use the real person's own document and never a character's invented identity. Do not photograph documents into the repo.

## 7. Accounts to create, and accounts not to create

| Create (pilot) | Platform | Reference |
|---|---|---|
| 方寸 | Instagram professional account; YouTube channel | `personas/fangcun.md` |
| 步驟 | YouTube channel; Threads; an Instagram account only if Threads needs it (unverified) | `personas/buzhou.md` |
| 色環 | Instagram professional account; Threads | `personas/sehuan.md` |
| Studio | Mailbox, password manager, link-page host and domain; **no studio social account** (`DECISIONS.md` STOP 2 item 7) | sections 3, 4 and 10 |

| Do not create now | Why |
|---|---|
| Facebook Page | None of the three pilots uses Facebook (`portfolio.md` 2B). The template is kept for Wave 3 (歲歲, 里程, 等一下): `platform-checklists.md` D |
| LINE Official Account | Retention channel only, free 輕用量 plan, and not until an audience exists (`portfolio.md` 7); template in `platform-checklists.md` E |
| TikTok, X, Xiaohongshu, Dcard, PTT | No pilot uses them (TikTok is manual, wave 2 at the earliest; Xiaohongshu is blocked; Dcard and PTT are listening only) |
| A second or backup account for any persona, a parked handle, a test account that is not one of the real accounts | No replacement accounts ever (`portfolio.md` 6.2); no parked placeholders (`personas/README.md` section 2) |
| Accounts for the other seven characters | Designed only; they launch by wave and gate |

## 8. Meta (Instagram and Threads): structure, and decision D3

* **A Facebook profile for a character is forbidden.** Meta counts a personal profile created to represent a non-human entity as a fake account (`research/platforms.md` 4.1, S34). Each character is an Instagram **professional** account (and a Threads account on the same login). The only Facebook identities involved are your own real personal profiles, if you have them.
* **Option 1 (recommended default for the pilot): shared login in the vault.** Both of you sign in with the vault entry; the code comes from the vault. Simple, with unverified risks: sign-ins from a second device may trigger a security check, and Meta's view of shared logins is not read.
* **Option 2: a Meta business portfolio** owned by one of your real profiles, with the Instagram accounts added as assets and the other person given access under their own login. No shared password. Requirements are **unverified** (whether a Facebook Page is needed, what verification asks for with no registered business). Revisit before any contractor, agency or second operator needs access: then use roles, never passwords.
* **Accounts Center:** when the Instagram app offers to link an account to an Accounts Center, choose "not now" where it lets you, and write down what it offered. Do not link a persona to your own personal Instagram or Facebook profile, and do not link two different personas to each other (Ground rule 8; what a link does to enforcement is **unverified**). An Instagram and Threads pair for the same persona is linked by design.
* **Five-account switcher:** three Instagram-login accounts exist at launch (方寸, 色環 and, only if needed, the 步驟 prerequisite), inside the limit of five (`portfolio.md` 2.6). Use one phone, the app's own switcher and the vault; never an app cloner or dual-app tool (Ground rule 9).

## 9. Google and YouTube: structure

* Each persona channel is created as a **Brand Account** channel under the studio Google account (the studio mailbox, section 3), so the channel is not tied to anyone's personal Google identity (recalled, unverified: YouTube's "create a new channel" flow makes one).
* In YouTube Studio, add the operator and the wife as users with their **own** Google accounts and two-factor (role names recalled and unverified: Owner, Manager, Editor, Viewer). Nobody signs in as the studio account except to change permissions.
* Verify the channel by phone if asked (unlocks features, recalled), as a human, with a real number.
* Channel monetisation is not applied for in year 1 (`portfolio.md` 2C: platform payouts planned at NT$0) and the "inauthentic content" rule is a standing risk (`research/platforms.md` 4.3).

## 10. The link-page host and domain (decision D4)

* The four pages in `link-pages/` are static; any static host works (examples only, not checked: GitHub Pages, Cloudflare Pages, Netlify). Budget line: up to NT$300 a month for hosting and a domain (`portfolio.md` 7, assumption); free hosting may cover it.
* **Domain:** only after the TIPO and 經濟部 searches (`HUMAN_TODO.md` 20 and 21), candidate stems `plainspoken` and `mingshuo` under .tw, .com.tw and .com; registrant: the wife, to be confirmed. The registrar and the host need their own two-factor.
* **Cost of changing later:** the URL is in every bio, so a later change means editing up to seven profiles and re-checking the pages. If you start on a free host address, accept that. A domain you control first avoids it.
* Do not enable any analytics the host offers (the pages promise none), and read what the host logs and whether it sets cookies before you write the privacy note (`link-pages/README.md` section 6).

## 11. Rules for creating and running accounts

1. A human creates every account, by hand, one at a time, on a phone and network you normally use. No bulk creation, no scripts, no emulators, no cloned apps (Ground rule 9).
2. **Create each account only when it can be finished in one sitting and used within about a week:** avatar approved, bio approved, mailbox and vault ready. No parked or placeholder accounts.
3. Handle: the first free candidate in the bible's order (`personas/<slug>.md` section 2). If it is taken when you sit down, take the next candidate and record it. Never buy, trade or snipe one.
4. The first thing set on every account is the disclosure: name field, bio, avatar chip, then the AI label settings. Nothing is posted until the first-post gates in the persona file are closed.
5. Personas never follow, like, comment on, tag or reply to each other; you and your relatives never like, comment, share or follow persona posts to lift them (`portfolio.md` 3.3 items 1 and 8). No follow-for-follow, no pods, no bought followers.
6. No automated reply or DM in the first 30 days. If one is ever added it says it is automated (Ground rule 9).
7. Every post is approved by a human first, for at least 30 days (`schedule.md` section 2).

## 12. Evidence log

`evidence-log.csv` holds one row per check: date, platform, account (public handle), what was checked, result, file name of the screenshot (kept outside the repo), who. It is the proof that the AI-label settings, the paid-partnership toggle and the four disclosure places were seen, and it is where the Instagram label check (`HUMAN_TODO.md` 10 and 38) is recorded. It is empty today; no row has been invented.

## 13. If access is lost or an account is compromised (first hour)

1. Do not tap links in a message or DM about the account. Open the platform's login help by typing the address or from the app.
2. From the **other** person's device or a clean browser: change the password in the vault, sign out of all sessions, and confirm that the two-factor methods, recovery email and recovery phone are still yours.
3. Unschedule everything for that account (`schedule.md` section 6), so nothing publishes while access is uncertain.
4. If you are locked out, use only the platform's own recovery path. **Do not pay or hire anyone who offers to "recover" an account;** that is a common scam (recalled).
5. Delete any post you did not write; tell the other person; add a row to the evidence log; report it in the app.
6. A platform restriction or label dispute is a standing incident: pause that persona on that platform, write the root cause, create no replacement account (`portfolio.md` 6.2).

## 14. Spend

Nothing in this file requires money. Possible lines, none committed: password-manager paid tier (price **not checked**; from contingency), domain and host (inside the NT$300 line, prices **not checked**). Anything bought is logged in `COSTS.md` the same day.
