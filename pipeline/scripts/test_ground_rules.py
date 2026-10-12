import unittest

import ground_rules as gr


def codes(text, level=None):
    return [(f.level, f.code) for f in gr.scan_text(text, "x") if level is None or f.level == level]


class LivedExperience(unittest.TestCase):
    def test_flags_testimony_words(self):
        for t in ["今天開箱，好用到想回購", "我試了一個月", "我買了這個櫃子", "實測心得", "我用過三個月", "穿起來很舒服"]:
            with self.subTest(t=t):
                self.assertIn(("FLAG", "LIVED_EXPERIENCE"), codes(t))

    def test_duration_claim(self):
        self.assertIn(("FLAG", "LIVED_EXPERIENCE"), codes("連續30天都在用"))

    def test_english_testimony(self):
        for t in ["I tried this for a month", "I've been using it daily", "In my experience it works", "my flat is tiny"]:
            with self.subTest(t=t):
                self.assertIn(("FLAG", "LIVED_EXPERIENCE"), codes(t))

    def test_denial_is_downgraded_to_info_never_hidden(self):
        # sentence taken from personas/fangcun/bible.md S20 (the J2 denial) must not be a FLAG
        t = "腰上的捲尺只是造型，不是我量出來的。數字都有出處，在最後一張。"
        self.assertNotIn(("FLAG", "LIVED_EXPERIENCE"), codes(t))
        self.assertIn(("INFO", "LIVED_EXPERIENCE_DENIED"), codes(t))
        t2 = "這個帳號不做開箱和實測，因為我是 AI，沒有實際使用過任何裝置。"
        self.assertEqual([], codes(t2, "FLAG"))
        self.assertTrue(codes(t2, "INFO"))

    def test_denial_does_not_cross_a_clause_break(self):
        # the negator is in a previous clause, so the claim still counts
        self.assertIn(("FLAG", "LIVED_EXPERIENCE"), codes("我不是專家。我用了三個月"))

    def test_clean_explainer_has_no_hits(self):
        self.assertEqual([], codes("先算三個數字，再比較兩種排法。請以現場丈量為準。"))


class Vocabulary(unittest.TestCase):
    def test_mainland_high_confidence_flags(self):
        for t, bad in [("這支視頻很短", "視頻"), ("信息整理", "信息"), ("軟件更新", "軟件"), ("質量比較", "質量"), ("博主推薦", "博主")]:
            with self.subTest(bad=bad):
                hits = [f for f in gr.scan_text(t, "x") if f.code == "MAINLAND_VOCAB"]
                self.assertTrue(hits)
                self.assertIn(bad, hits[0].message)

    def test_taiwan_forms_are_clean(self):
        self.assertEqual([], codes("影片、資訊、品質、軟體、儲存、創作者、網紅"))

    def test_soft_terms_only_warn(self):
        self.assertEqual([("WARN", "MAINLAND_SOFT")], codes("請關注我們"))

    def test_simplified_characters(self):
        self.assertIn(("FLAG", "SIMPLIFIED_CHARS"), codes("这个视频"))

    def test_traditional_and_ambiguous_characters_are_not_flagged(self):
        # 里 台 后 干 云 面 只 表 are valid Traditional; persona names must stay clean
        self.assertEqual([], codes("方寸 步驟 色環 歲歲 里程 規格 等一下 歸位 轉乘 接話 台灣 皇后 乾淨 雲 面 只 表"))

    def test_every_simplified_character_is_outside_big5(self):
        # the list is meant to hold characters Taiwan's Big5 repertoire lacks, plus a short reviewed list of
        # Simplified forms that Big5 carries as variants. Anything else would be a mistake.
        allowed_big5_variants = set("网体据机种价气极构确离赶优儿吨圣坏怀惊扰挂柜洁苹茧荐触晒厂")
        for ch in gr.SIMPLIFIED_ONLY:
            try:
                ch.encode("big5")
            except UnicodeEncodeError:
                continue
            self.assertIn(ch, allowed_big5_variants, f"{ch} encodes in Big5 but is not in the reviewed variant list")

    def test_no_duplicate_or_ambiguous_entries(self):
        self.assertEqual(len(gr.SIMPLIFIED_ONLY), len(gr.SIMPLIFIED_SET))
        for ch in "台里后干云面只表制向內才余谷松週周發髮復複覆範洒涂胜适划":
            self.assertNotIn(ch, gr.SIMPLIFIED_SET)


class RegulatedTerritory(unittest.TestCase):
    def test_health_and_weight_loss(self):
        for t in ["三週瘦 5 公斤", "顯瘦又顯高", "抗菌防霉", "改善失眠"]:
            with self.subTest(t=t):
                self.assertIn(("FLAG", "HEALTH_CLAIM"), codes(t))

    def test_fabric_performance_words_only_warn(self):
        self.assertEqual([("WARN", "PERFORMANCE_CLAIM")], codes("這件很透氣"))

    def test_finance(self):
        for t in ["存股也能被動收入", "年化報酬 8%", "比特幣怎麼買"]:
            with self.subTest(t=t):
                self.assertIn(("FLAG", "FINANCE_CLAIM"), codes(t))

    def test_gambling_and_politics(self):
        self.assertIn(("FLAG", "GAMBLING"), codes("百家樂攻略"))
        self.assertIn(("FLAG", "POLITICS"), codes("選舉前的穿搭"))
        self.assertIn(("WARN", "POLITICS_ADJACENT"), codes("藍綠色系"))

    def test_fake_popularity_and_undisclosing(self):
        self.assertIn(("ERROR", "FAKE_POPULARITY"), codes("#f4f #互粉"))
        self.assertIn(("FLAG", "UNDISCLOSING"), codes("真人實拍"))

    def test_superlative_warns_unless_denied(self):
        self.assertIn(("WARN", "SUPERLATIVE"), codes("這是最好的選擇"))
        self.assertNotIn(("WARN", "SUPERLATIVE"), codes("我沒辦法說哪個最好"))


class ClaimDetection(unittest.TestCase):
    def test_strong_and_numeric(self):
        self.assertTrue(gr.has_strong_claim("官方公告的尺寸"))
        self.assertFalse(gr.has_strong_claim("先算三個數字"))
        self.assertTrue(gr.has_numeric("寬 80 公分"))
        self.assertFalse(gr.has_numeric("三個數字"))


class ReviewAdditions(unittest.TestCase):
    """Added in the independent Phase 4 review: misses found by probing the scanner."""

    def test_time_and_habit_words_between_i_and_the_verb(self):
        for t in ["我昨天試了這個收納盒", "我每天都用這個工具", "我之前買過一組", "我平常都用這個", "我一直在穿", "我正在使用",
                  "我也在用這個工具", "我的衣櫃只有七件", "親自體驗過", "實際使用後發現很好用"]:
            with self.subTest(t=t):
                self.assertIn(("FLAG", "LIVED_EXPERIENCE"), codes(t))

    def test_bare_mei_is_not_a_denial(self):
        # 沒想到 ("unexpectedly") must not downgrade a claim to INFO
        self.assertIn(("FLAG", "LIVED_EXPERIENCE"), codes("沒想到我親測有效"))
        self.assertEqual([], codes("沒想到我親測有效", "INFO"))
        # a negator glued to the term still denies
        self.assertEqual([], codes("這個角色沒試穿過這件", "FLAG"))

    def test_experience_aspect_verbs_warn_and_denials_are_info(self):
        self.assertIn(("WARN", "LIVED_ASPECT"), codes("這個角色用過"))
        self.assertIn(("INFO", "LIVED_ASPECT_DENIED"), codes("角色沒有使用過此商品，內容僅就公開規格與資料說明。"))
        self.assertEqual([], codes("角色沒有使用過此商品，內容僅就公開規格與資料說明。", "FLAG"))

    def test_undisclosing_variants(self):
        for t in ["非 AI 製作", "不是 AI，是真人", "這是真人拍攝", "本人出鏡示範"]:
            with self.subTest(t=t):
                self.assertIn(("FLAG", "UNDISCLOSING"), codes(t))
        # the disclosure wording itself must stay clean
        self.assertEqual([], codes("我是 AI 虛擬角色，並非真人。"))

    def test_more_health_wording(self):
        for t in ["可以改善睡眠", "這家買了會瘦"]:
            with self.subTest(t=t):
                self.assertIn(("FLAG", "HEALTH_CLAIM"), codes(t))
        self.assertIn(("WARN", "PERFORMANCE_CLAIM"), codes("看起來比較瘦"))

    def test_more_mainland_tech_vocabulary(self):
        self.assertIn(("FLAG", "MAINLAND_VOCAB"), codes("找到硬盤裡的檔案"))
        self.assertIn(("WARN", "MAINLAND_SOFT"), codes("打開用戶界面"))
        # Taiwan forms that contain a mainland form as a substring stay clean
        self.assertEqual([], codes("演算法與手機號碼"))


if __name__ == "__main__":
    unittest.main()
