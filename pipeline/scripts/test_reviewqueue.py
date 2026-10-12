import copy
import datetime as dt
import hashlib
import json
import unittest
from pathlib import Path

import reviewqueue as rq
import testutil
from testutil import good_post


def codes(findings, level=None):
    return sorted({(f.level, f.code) for f in findings if level is None or f.level == level})


def has(findings, code, level=None):
    return any(f.code == code and (level is None or f.level == level) for f in findings)


class Scaffold(unittest.TestCase):
    def setUp(self):
        self.tmp, self.root = testutil.make_root()
        self.addCleanup(self.tmp.cleanup)

    def test_new_draft_follows_the_documented_format(self):
        folder = rq.new_draft(self.root, "fangcun", "instagram", "carousel", "2026-11-16", "尺寸算給你看")
        self.assertEqual(self.root / "pipeline/review-queue/fangcun/2026-11-16_01", folder)
        self.assertTrue((folder / "media" / ".gitkeep").is_file())
        self.assertEqual([".gitkeep"], [p.name for p in (folder / "media").iterdir()])
        post = json.loads((folder / "post.json").read_text(encoding="utf-8"))
        self.assertEqual("fangcun-2026-11-16-01", post["id"])
        self.assertEqual(set(rq.REQUIRED_STR) | set(rq.REQUIRED_OTHER), set(post))
        self.assertEqual("PENDING", post["media"][0]["path"])
        self.assertTrue(post["caption_zh"].startswith("【AI 虛擬角色】"))
        self.assertTrue(post["ai_label_flag"])
        self.assertEqual({"wife_language": "pending", "operator_facts": "pending", "approved": False, "notes": ""}, post["review"])

    def test_numbers_increment_per_persona_and_date(self):
        a = rq.new_draft(self.root, "fangcun", "instagram", "carousel", "2026-11-16")
        b = rq.new_draft(self.root, "fangcun", "youtube_shorts", "short", "2026-11-16")
        c = rq.new_draft(self.root, "fangcun", "instagram", "carousel", "2026-11-17")
        self.assertEqual(["2026-11-16_01", "2026-11-16_02", "2026-11-17_01"], [a.name, b.name, c.name])

    def test_youtube_and_text_variants_of_the_first_line(self):
        f = rq.new_draft(self.root, "buzhou", "youtube_shorts", "short", "2026-11-16")
        self.assertIn("本影片", json.loads((f / "post.json").read_text(encoding="utf-8"))["caption_zh"])
        f = rq.new_draft(self.root, "buzhou", "threads", "text", "2026-11-17")
        post = json.loads((f / "post.json").read_text(encoding="utf-8"))
        self.assertEqual([], post["media"])
        self.assertTrue(post["caption_zh"].startswith("【AI 虛擬角色】"))

    def test_refuses_bad_input_and_existing_drafts(self):
        for args in [("nobody", "instagram", "carousel", "2026-11-16"), ("fangcun", "tiktok", "carousel", "2026-11-16"),
                     ("fangcun", "instagram", "video", "2026-11-16"), ("fangcun", "instagram", "carousel", "2026-02-30"),
                     ("fangcun", "instagram", "carousel", "16/11/2026"), ("fangcun", "instagram", "carousel", "2026-1-5")]:
            with self.subTest(args=args):
                with self.assertRaises(rq.QueueError):
                    rq.new_draft(self.root, *args)
        rq.new_draft(self.root, "fangcun", "instagram", "carousel", "2026-11-16", number=3)
        with self.assertRaises(rq.QueueError):
            rq.new_draft(self.root, "fangcun", "instagram", "carousel", "2026-11-16", number=3)

    def test_a_fresh_scaffold_is_incomplete_not_valid(self):
        rq.new_draft(self.root, "fangcun", "instagram", "carousel", "2026-11-16")
        res = rq.validate_all(self.root)
        self.assertEqual("incomplete", res[0]["status"])
        self.assertTrue(has(res[0]["findings"], "EMPTY", "ERROR"))

    def test_the_scaffold_never_approves(self):
        for plat, fmt in (("instagram", "carousel"), ("youtube_shorts", "short"), ("threads", "text")):
            f = rq.new_draft(self.root, "fangcun", plat, fmt, "2026-11-20")
            self.assertIs(False, json.loads((f / "post.json").read_text(encoding="utf-8"))["review"]["approved"])


class GoodPost(unittest.TestCase):
    def setUp(self):
        self.tmp, self.root = testutil.make_root()
        self.addCleanup(self.tmp.cleanup)

    def test_a_clean_draft_has_no_error_or_flag(self):
        folder = testutil.write_draft(self.root)
        res = rq.validate_all(self.root)[0]
        self.assertEqual([], [f.render() for f in res["findings"] if f.level in ("ERROR", "FLAG")])
        self.assertEqual("awaiting-both", res["status"])
        self.assertEqual(folder, res["folder"])


class RuleChecks(unittest.TestCase):
    def setUp(self):
        self.tmp, self.root = testutil.make_root()
        self.addCleanup(self.tmp.cleanup)
        self.folder = testutil.write_draft(self.root)

    def v(self, **over):
        post = good_post(**over)
        return rq.validate_post(post, self.folder, self.root, prov_paths=set())

    def test_ai_label_flag_must_be_true(self):
        self.assertTrue(has(self.v(ai_label_flag=False), "AI_LABEL", "ERROR"))

    def test_on_screen_label_required(self):
        self.assertTrue(has(self.v(on_screen_label_zh=""), "NO_ONSCREEN_LABEL", "ERROR"))
        self.assertTrue(has(self.v(on_screen_label_zh="示意圖"), "NO_ONSCREEN_LABEL", "ERROR"))
        p = good_post()
        del p["on_screen_label_zh"]
        self.assertTrue(has(rq.validate_post(p, self.folder, self.root), "MISSING_FIELD", "ERROR"))

    def test_first_caption_line_must_be_the_ai_disclosure(self):
        self.assertTrue(has(self.v(caption_zh="床、衣櫃、門\n【AI 虛擬角色】本篇由 AI 生成"), "NO_DISCLOSURE_LINE", "ERROR"))

    def test_hashtags_must_be_a_list_of_hash_strings(self):
        self.assertTrue(has(self.v(hashtags="#收納"), "BAD_TYPE", "ERROR"))
        self.assertTrue(has(self.v(hashtags=["收納"]), "BAD_HASHTAG", "ERROR"))
        self.assertTrue(has(self.v(hashtags=["#收納 小宅"]), "BAD_HASHTAG", "ERROR"))
        self.assertTrue(has(self.v(hashtags=[5]), "BAD_HASHTAG", "ERROR"))
        self.assertTrue(has(self.v(hashtags=["#f4f"]), "FAKE_POPULARITY", "ERROR"))

    def test_sponsorship_consistency(self):
        self.assertTrue(has(self.v(sponsorship_flag=True), "SPONSORSHIP_MISMATCH", "ERROR"))
        self.assertTrue(has(self.v(sponsorship_type="paid"), "SPONSORSHIP_MISMATCH", "ERROR"))
        self.assertTrue(has(self.v(sponsorship_flag=True, sponsorship_type="paid"), "SPONSOR_TAG_MISSING", "ERROR"))
        self.assertTrue(has(self.v(sponsorship_type="mystery"), "BAD_ENUM", "ERROR"))

    def test_sponsorship_tags_in_caption(self):
        cap = good_post()["caption_zh"].replace("\n", "\n【業配】本篇為與{廠商}的合作內容。角色沒有使用過此商品，內容僅就公開規格與資料說明。\n", 1)
        ok = self.v(caption_zh=cap, sponsorship_flag=True, sponsorship_type="paid",
                    sources=[{"claim": "spec", "url": "https://example.invalid/spec", "date": "2026-10-12"}])
        self.assertFalse(has(ok, "SPONSOR_TAG_MISSING"))
        self.assertFalse(has(ok, "SPONSORSHIP_MISMATCH"))
        self.assertTrue(has(ok, "PLATFORM_TOOLS", "INFO"))
        unflagged = self.v(caption_zh=cap)
        self.assertTrue(has(unflagged, "SPONSOR_UNFLAGGED", "ERROR"))
        gifted = good_post()["caption_zh"].replace("\n", "\n【廠商提供】商品由{廠商}提供。\n", 1)
        self.assertTrue(has(self.v(caption_zh=gifted, sponsorship_flag=True, sponsorship_type="paid"), "SPONSOR_TAG_MISSING", "ERROR"))
        aff = good_post()["caption_zh"].replace("\n", "\n【含分潤連結】透過連結購買，工作室可能獲得分潤。\n", 1)
        self.assertFalse(has(self.v(caption_zh=aff, sponsorship_flag=True, sponsorship_type="affiliate"), "SPONSOR_TAG_MISSING"))

    def test_sources_required_when_claims_exist(self):
        cap = good_post()["caption_zh"] + "\n依官方公告，1 坪約 3.3 平方公尺。"
        self.assertTrue(has(self.v(caption_zh=cap), "NO_SOURCES", "ERROR"))
        good_src = [{"claim": "1 坪 = 3.3 m2", "url": "https://example.invalid/a", "date": "2026-10-12"}]
        self.assertFalse(has(self.v(caption_zh=cap, sources=good_src), "NO_SOURCES"))
        empty_url = [{"claim": "1 坪 = 3.3 m2", "url": "", "date": "2026-10-12"}]
        self.assertTrue(has(self.v(caption_zh=cap, sources=empty_url), "SOURCE_NO_URL", "ERROR"))
        # no factual claim: an empty url is tolerated
        self.assertFalse(has(self.v(sources=empty_url), "SOURCE_NO_URL"))
        self.assertTrue(has(self.v(caption_zh=cap, sources=[{"claim": "x"}]), "BAD_SOURCE", "ERROR"))

    def test_source_conventions_and_placeholders(self):
        arith = [{"claim": "ARITHMETIC ONLY: 300 - 150 = 150, example values", "url": "", "date": ""}]
        nofact = [{"claim": "NO FACTUAL CLAIM: a general checklist", "url": "", "date": ""}]
        self.assertEqual([], [x for x in self.v(sources=arith) if x.level in ("ERROR", "FLAG", "WARN")])
        self.assertEqual([], [x for x in self.v(sources=nofact) if x.level in ("ERROR", "FLAG", "WARN")])
        cap = good_post()["caption_zh"] + "\n依官方公告，1 坪約 3.3 平方公尺。"
        self.assertTrue(has(self.v(caption_zh=cap, sources=arith), "NO_REAL_SOURCE", "ERROR"))
        # a denied claim word is not a claim
        deny = good_post()["caption_zh"] + "\n數字皆為示意，沒有外部出處。"
        self.assertFalse(has(self.v(caption_zh=deny, sources=arith), "NO_REAL_SOURCE"))
        ph = [{"claim": "1 坪", "url": "UNVERIFIED-OPERATOR-TO-FILL", "date": "UNVERIFIED-OPERATOR-TO-FILL"}]
        f = self.v(caption_zh=cap, sources=ph)
        self.assertTrue(has(f, "PLACEHOLDER", "WARN"))
        self.assertFalse(has(f, "SOURCE_NO_URL"))
        f = self.v(caption_zh=good_post()["caption_zh"] + "\n{廠商}提供")
        self.assertTrue(has(f, "PLACEHOLDER", "WARN"))

    def test_approval_blocked_by_placeholder(self):
        done = [{"path": "media/s1.png", "description": "d", "shot_prompt": "p"}]
        (self.folder / "media" / "s1.png").write_bytes(b"x")
        both = {"wife_language": "approved", "operator_facts": "approved", "approved": True, "notes": ""}
        f = rq.validate_post(good_post(media=done, review=both, hook_zh="{標題}"), self.folder, self.root, prov_paths={"media/s1.png"})
        self.assertTrue(has(f, "APPROVAL_INCONSISTENT", "ERROR"))

    def test_bare_numbers_without_sources_warn_and_illustrative_numbers_are_info(self):
        first = good_post()["caption_zh"].split("\n")[0]
        cap = first + "\n門寬 80 公分，櫃子寬 60 公分。"
        self.assertTrue(has(self.v(caption_zh=cap), "NUMBERS_NO_SOURCE", "WARN"))
        cap2 = first + "\n示意數字：門寬 80 公分，櫃子寬 60 公分。"
        self.assertTrue(has(self.v(caption_zh=cap2), "NUMBERS_NO_SOURCE", "INFO"))

    def test_banned_terms_are_flagged_not_fixed(self):
        original = good_post()["caption_zh"] + "\n我試了一個月，這支視頻的質量很好，還能瘦身。"
        f = self.v(caption_zh=original)
        got = {c for lvl, c in codes(f, "FLAG")}
        self.assertTrue({"LIVED_EXPERIENCE", "MAINLAND_VOCAB", "HEALTH_CLAIM"} <= got, got)
        # the post object is not modified by validation
        post = good_post(caption_zh=original)
        before = copy.deepcopy(post)
        rq.validate_post(post, self.folder, self.root)
        self.assertEqual(before, post)

    def test_banned_terms_in_hook_and_hashtags_are_scanned(self):
        self.assertTrue(has(self.v(hook_zh="開箱最好用的收納"), "LIVED_EXPERIENCE", "FLAG"))
        self.assertTrue(has(self.v(hashtags=["#實測"]), "LIVED_EXPERIENCE", "FLAG"))
        self.assertTrue(has(self.v(hook_zh="这个视频"), "SIMPLIFIED_CHARS", "FLAG"))

    def test_denial_sentences_are_info_not_flag(self):
        cap = good_post()["caption_zh"] + "\n腰上的捲尺只是造型，不是我量出來的。"
        f = self.v(caption_zh=cap)
        self.assertFalse(has(f, "LIVED_EXPERIENCE", "FLAG"))
        self.assertTrue(has(f, "LIVED_EXPERIENCE_DENIED", "INFO"))

    def test_persona_cross_mentions_are_flagged(self):
        f = self.v(caption_zh=good_post()["caption_zh"] + "\n也看看 buzhou 的教學")
        self.assertTrue(has(f, "PERSONA_CROSS_MENTION", "FLAG"))
        f = self.v(caption_zh=good_post()["caption_zh"] + "\nstep0_ai 很棒")
        self.assertTrue(has(f, "PERSONA_CROSS_MENTION", "FLAG"))
        self.assertTrue(has(self.v(caption_zh=good_post()["caption_zh"] + "\n@someone"), "MENTION", "WARN"))
        # a persona's own handle is not another persona
        self.assertFalse(has(self.v(caption_zh=good_post()["caption_zh"] + "\nfangcun_ai"), "PERSONA_CROSS_MENTION"))

    def test_id_and_folder_must_agree(self):
        self.assertTrue(has(self.v(id="fangcun-2026-11-17-01"), "ID_MISMATCH", "ERROR"))
        self.assertTrue(has(self.v(id="buzhou-2026-11-16-01"), "ID_MISMATCH", "ERROR"))
        self.assertTrue(has(self.v(id="fangcun-2026-11-16-02"), "ID_MISMATCH", "ERROR"))
        self.assertTrue(has(self.v(id="bad id"), "ID_FORMAT", "ERROR"))

    def test_enums_and_dates(self):
        self.assertTrue(has(self.v(platform="tiktok"), "BAD_ENUM", "ERROR"))
        self.assertTrue(has(self.v(format="video"), "BAD_ENUM", "ERROR"))
        self.assertTrue(has(self.v(persona="nobody"), "UNKNOWN_PERSONA", "ERROR"))
        self.assertTrue(has(self.v(scheduled_date="2026-02-30"), "BAD_DATE", "ERROR"))
        self.assertTrue(has(self.v(scheduled_date="2027-02-28", id="fangcun-2027-02-28-01"), "CALENDAR", "WARN"))

    def test_calendar_warnings(self):
        f = rq.validate_post(good_post(scheduled_date="2026-11-10", id="fangcun-2026-11-10-01"), None, self.root)
        self.assertTrue(has(f, "CALENDAR", "WARN"))  # before assumed W0
        f = rq.validate_post(good_post(scheduled_date="2027-08-10", id="fangcun-2027-08-10-01"), None, self.root)
        self.assertTrue(any("ghost month" in x.message for x in f))

    def test_persona_status_and_platform_plan_warnings(self):
        self.assertTrue(has(self.v(platform="threads"), "PLATFORM_PLAN", "WARN"))
        p = good_post(persona="dengyixia", platform="facebook", id="dengyixia-2026-11-16-01")
        self.assertTrue(has(rq.validate_post(p, None, self.root), "PERSONA_STATUS", "WARN"))

    def test_media_rules(self):
        self.assertTrue(has(self.v(media=[]), "NO_MEDIA", "ERROR"))
        self.assertTrue(has(self.v(media=[{"path": "PENDING", "description": "d", "shot_prompt": ""}]), "EMPTY", "ERROR"))
        self.assertTrue(has(self.v(media=[{"path": "PENDING", "description": "d"}]), "BAD_MEDIA", "ERROR"))
        self.assertTrue(has(self.v(media=[{"path": "media/missing.png", "description": "d", "shot_prompt": "p"}]), "MEDIA_MISSING_FILE", "ERROR"))
        blocked = [{"path": "PENDING", "description": "d", "shot_prompt": "portrait of Taylor Swift"}]
        self.assertTrue(has(self.v(media=blocked), "PROMPT_BLOCKED", "ERROR"))
        self.assertFalse(has(self.v(format="text", platform="threads", media=[]), "NO_MEDIA"))

    def test_existing_media_needs_a_provenance_row_warning(self):
        (self.folder / "media" / "s1.png").write_bytes(b"x")
        media = [{"path": "media/s1.png", "description": "d", "shot_prompt": "p"}]
        f = rq.validate_post(good_post(media=media), self.folder, self.root, prov_paths=set())
        self.assertFalse(has(f, "MEDIA_MISSING_FILE"))
        self.assertTrue(has(f, "NO_PROVENANCE", "WARN"))
        rel = (self.folder / "media" / "s1.png").relative_to(self.root).as_posix()
        f = rq.validate_post(good_post(media=media), self.folder, self.root, prov_paths={rel})
        self.assertFalse(has(f, "NO_PROVENANCE"))

    def test_review_block(self):
        r = good_post()["review"]
        self.assertTrue(has(self.v(review={**r, "wife_language": "ok"}), "BAD_REVIEW", "ERROR"))
        self.assertTrue(has(self.v(review={**r, "approved": "yes"}), "BAD_REVIEW", "ERROR"))
        self.assertTrue(has(self.v(review={**r, "approved": True}), "APPROVAL_INCONSISTENT", "ERROR"))
        both = {**r, "wife_language": "approved", "operator_facts": "approved", "approved": True}
        f = self.v(review=both)
        self.assertTrue(has(f, "APPROVAL_INCONSISTENT", "ERROR"))  # media still PENDING
        done = [{"path": "media/s1.png", "description": "d", "shot_prompt": "p"}]
        (self.folder / "media" / "s1.png").write_bytes(b"x")
        f = rq.validate_post(good_post(media=done, review=both), self.folder, self.root, prov_paths={"media/s1.png"})
        self.assertEqual([], [x.render() for x in f if x.level in ("ERROR", "FLAG")])
        self.assertTrue(has(f, "HUMAN_FIELD", "INFO"))
        flagged = good_post(media=done, review=both, hook_zh="開箱")
        f = rq.validate_post(flagged, self.folder, self.root, prov_paths={"media/s1.png"})
        self.assertTrue(has(f, "APPROVED_WITH_OPEN_ISSUES", "ERROR"))

    def test_length_and_unknown_fields_warn(self):
        long_caption = good_post()["caption_zh"] + "字" * 600
        self.assertTrue(has(self.v(platform="threads", format="text", media=[], caption_zh=long_caption, id="fangcun-2026-11-16-01"), "LENGTH", "WARN"))
        p = good_post()
        p["hastags"] = []
        self.assertTrue(has(rq.validate_post(p, self.folder, self.root), "UNKNOWN_FIELD", "WARN"))

    def test_not_an_object(self):
        self.assertTrue(has(rq.validate_post([], None, self.root), "FORMAT", "ERROR"))


class StatusAndFiles(unittest.TestCase):
    def setUp(self):
        self.tmp, self.root = testutil.make_root()
        self.addCleanup(self.tmp.cleanup)

    def status(self, **review):
        post = good_post(review={**good_post()["review"], **review})
        folder = self.root / "pipeline/review-queue/fangcun/2026-11-16_01"
        if not folder.exists():
            testutil.write_draft(self.root)
        rq.write_post(folder / "post.json", post)
        return rq.validate_all(self.root)[0]["status"]

    def test_status_progression(self):
        self.assertEqual("awaiting-both", self.status())
        self.assertEqual("awaiting-operator", self.status(wife_language="approved"))
        self.assertEqual("awaiting-wife", self.status(operator_facts="approved"))
        self.assertEqual("changes-requested", self.status(wife_language="changes"))
        self.assertEqual("ready-for-final-approval", self.status(wife_language="approved", operator_facts="approved"))

    def test_unreadable_and_duplicate(self):
        folder = testutil.write_draft(self.root)
        (folder / "post.json").write_text("{not json", encoding="utf-8")
        res = rq.validate_all(self.root)
        self.assertTrue(has(res[0]["findings"], "UNREADABLE", "ERROR"))
        (folder / "post.json").write_bytes("�".encode("utf-8")[:2])
        res = rq.validate_all(self.root)
        self.assertTrue(has(res[0]["findings"], "UNREADABLE", "ERROR"))
        # duplicate ids across two folders
        (folder / "post.json").write_text(json.dumps(good_post()), encoding="utf-8")
        second = self.root / "pipeline/review-queue/fangcun/2026-11-16_02"
        (second / "media").mkdir(parents=True)
        (second / "post.json").write_text(json.dumps(good_post()), encoding="utf-8")
        res = rq.validate_all(self.root)
        self.assertTrue(all(has(r["findings"], "DUPLICATE_ID", "ERROR") for r in res))

    def test_weekly_load(self):
        for n, d in enumerate(["2026-11-16", "2026-11-17", "2026-11-23"], start=1):
            post = good_post(scheduled_date=d, id=f"fangcun-{d}-01")
            testutil.write_draft(self.root, post)
        weeks = rq.weekly_load(rq.validate_all(self.root))
        self.assertEqual({"2026-W47": 2, "2026-W48": 1}, weeks)

    def test_validation_never_writes(self):
        folder = testutil.write_draft(self.root)
        before = {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in folder.rglob("*") if p.is_file()}
        rq.validate_all(self.root)
        out = []
        rq.main(["--root", str(self.root), "validate"], out=out.append)
        rq.main(["--root", str(self.root), "list"], out=out.append)
        rq.main(["--root", str(self.root), "approve", str(folder)], out=out.append)
        after = {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in folder.rglob("*") if p.is_file()}
        self.assertEqual(before, after)

    def test_no_code_path_sets_approved_true(self):
        src = Path(rq.__file__).read_text(encoding="utf-8")
        self.assertNotRegex(src, r"""\[['"]approved['"]\]\s*=\s*True""")
        self.assertNotRegex(src, r"""['"]approved['"]\s*:\s*True""")


class CommandLine(unittest.TestCase):
    def setUp(self):
        self.tmp, self.root = testutil.make_root()
        self.addCleanup(self.tmp.cleanup)
        self.out = []

    def run_cli(self, *argv):
        return rq.main(["--root", str(self.root), *argv], out=self.out.append)

    def text(self):
        return "\n".join(self.out)

    def test_new_draft_validate_list_approve(self):
        self.assertEqual(0, self.run_cli("new-draft", "--persona", "sehuan", "--platform", "instagram", "--format", "reel", "--date", "2026-11-18"))
        self.assertIn("2026-11-18_01", self.text())
        self.out.clear()
        self.assertEqual(1, self.run_cli("validate"))  # incomplete scaffold has errors
        self.assertIn("incomplete", self.text())
        self.out.clear()
        self.assertEqual(0, self.run_cli("list"))
        self.assertIn("sehuan-2026-11-18-01", self.text())
        self.assertIn("incomplete", self.text())
        self.out.clear()
        self.assertEqual(0, self.run_cli("list", "--persona", "fangcun"))
        self.assertIn("No drafts match", self.text())
        self.out.clear()
        folder = self.root / "pipeline/review-queue/sehuan/2026-11-18_01"
        self.assertEqual(1, self.run_cli("approve", str(folder)))
        self.assertIn("APPROVAL IS A HUMAN ACTION", self.text())
        self.assertIn("NOT APPROVED", self.text())

    def test_approve_reports_ready_only_when_a_human_has_set_everything(self):
        folder = testutil.write_draft(self.root)
        (folder / "media" / "s1.png").write_bytes(b"x")
        post = good_post(media=[{"path": "media/s1.png", "description": "d", "shot_prompt": "p"}],
                         review={"wife_language": "approved", "operator_facts": "approved", "approved": True, "notes": "human"})
        rq.write_post(folder / "post.json", post)
        self.assertEqual(0, self.run_cli("approve", str(folder / "post.json")))
        self.assertIn("READY", self.text())

    def test_validate_json_and_strict(self):
        testutil.write_draft(self.root)
        self.assertEqual(0, self.run_cli("validate"))
        self.out.clear()
        self.assertEqual(0, self.run_cli("validate", "--json"))
        data = json.loads(self.text())
        self.assertEqual("fangcun-2026-11-16-01", data[0]["id"])
        # the clean draft has WARNs? make one and use --strict
        folder = self.root / "pipeline/review-queue/fangcun/2026-11-16_01"
        rq.write_post(folder / "post.json", good_post(platform="threads", format="text", media=[]))
        self.out.clear()
        self.assertEqual(0, self.run_cli("validate"))
        self.assertEqual(1, self.run_cli("validate", "--strict"))

    def test_empty_queue(self):
        self.assertEqual(0, self.run_cli("list"))
        self.assertIn("empty", self.text())
        self.assertEqual(0, self.run_cli("validate"))

    def test_malformed_posts_never_crash_list_validate_or_approve(self):
        # found in the independent review: list sorted int against str, approve called .get on a list
        d = self.root / "pipeline/review-queue/fangcun"
        cases = {"2026-11-16_01": "[]", "2026-11-16_02": "{bad", "2026-11-16_03": "null",
                 "2026-11-16_04": json.dumps({"id": None, "persona": 5, "platform": [], "scheduled_date": 3, "media": 7, "review": []})}
        for name, text in cases.items():
            (d / name).mkdir(parents=True)
            (d / name / "post.json").write_text(text, encoding="utf-8")
        (d / "2026-11-16_05").mkdir()
        (d / "2026-11-16_05" / "post.json").write_bytes(b"\xff\xfe")
        for argv in (("list",), ("validate",), ("validate", "--json")):
            self.out.clear()
            self.run_cli(*argv)
        for name in list(cases) + ["2026-11-16_05"]:
            self.out.clear()
            rc = self.run_cli("approve", str(d / name))
            self.assertNotEqual(0, rc, name)  # never "ready", never a traceback
            self.assertTrue("NOT APPROVED" in self.text() or "cannot read" in self.text(), name)


class PersonaNameMentions(unittest.TestCase):
    def test_other_persona_name_used_like_a_name_warns(self):
        post = good_post(caption_zh=good_post()["caption_zh"] + "\n同事「步驟」也這樣說。")
        self.assertTrue(has(rq.validate_post(post), "PERSONA_NAME_MENTION", "WARN"))
        self.assertFalse(has(rq.validate_post(good_post()), "PERSONA_NAME_MENTION"))


class SponsorWords(unittest.TestCase):
    def test_sponsor_wording_without_a_sponsorship_type_warns(self):
        post = good_post(hashtags=["#業配", "#收納"])
        self.assertTrue(has(rq.validate_post(post), "SPONSOR_WORD", "WARN"))
        post = good_post(caption_zh=good_post()["caption_zh"] + "\n使用折扣碼 ABC 享優惠")
        self.assertTrue(has(rq.validate_post(post), "SPONSOR_WORD", "WARN"))
        self.assertFalse(has(rq.validate_post(good_post()), "SPONSOR_WORD"))


if __name__ == "__main__":
    unittest.main()
