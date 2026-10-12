import base64
import csv
import json
import os
import re
import unittest
from pathlib import Path
from unittest import mock

import gen_image
import provenance
import testutil

PNG = b"\x89PNG\r\n\x1a\n" + b"fake-image-bytes\x00\xff\x10" * 4 + b"tEXtC2PA-like-marker"
KEY = "TESTKEY-" + "z" * 24


class Collect:
    def __init__(self):
        self.out, self.err = [], []

    def o(self, s=""):
        self.out.append(str(s))

    def e(self, s=""):
        self.err.append(str(s))

    @property
    def stdout(self):
        return "\n".join(self.out)

    @property
    def stderr(self):
        return "\n".join(self.err)


def no_network(*a, **k):
    raise AssertionError("a network call was attempted")


def gemini_ok(url, headers, data, timeout=0):
    body = {"candidates": [{"content": {"parts": [{"text": "here"}, {"inlineData": {"mimeType": "image/png", "data": base64.b64encode(PNG).decode()}}]}}]}
    return 200, json.dumps(body).encode()


def openai_ok(url, headers, data, timeout=0):
    return 200, json.dumps({"data": [{"b64_json": base64.b64encode(PNG).decode()}]}).encode()


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp, self.root = testutil.make_root()
        self.addCleanup(self.tmp.cleanup)
        self.c = Collect()

    def run_gen(self, argv, env=None, post=no_network):
        argv = ["--root", str(self.root)] + argv
        return gen_image.run(argv, env=env if env is not None else {}, post=post, out=self.c.o, err=self.c.e)

    def base_args(self, provider="gemini", out="assets/fangcun/photoreal/R01_cand_x_1.png", extra=()):
        return ["--provider", provider, "--persona", "fangcun", "--out", out, "--model", "test-model-id",
                "--prompt", "An original adult woman, plain warm off-white studio backdrop, waist-up."] + list(extra)


class PromptCheck(unittest.TestCase):
    def test_real_people_and_characters_are_blocked(self):
        for p in ["portrait of Taylor Swift", "a woman, 周杰倫 style", "Hello Kitty as a human", "mickey mouse hands",
                  "an avatar like Lil Miquela", "built from LEGO bricks"]:
            with self.subTest(p=p):
                self.assertFalse(gen_image.check_prompt(p).ok)

    def test_name_is_blocked_even_inside_a_prohibition(self):
        self.assertFalse(gen_image.check_prompt("must not look like Zendaya").ok)
        self.assertFalse(gen_image.check_prompt("Do not resemble Taylor Swift").ok)

    def test_likeness_phrases_with_a_name(self):
        for p in ["looks like Zhang", "in the style of Hayao", "based on Madonna", "長得像某某", "神似某位演員"]:
            with self.subTest(p=p):
                self.assertFalse(gen_image.check_prompt(p).ok, p)

    def test_prohibitions_without_a_name_pass(self):
        p = ("This person is original and not based on, copied from or meant to resemble any real individual. "
             "Please avoid: any resemblance to a real person; an idol, model or beauty-filter look.")
        r = gen_image.check_prompt(p)
        self.assertTrue(r.ok)
        self.assertEqual([], r.warnings)

    def test_affirmative_celebrity_wording_warns(self):
        r = gen_image.check_prompt("a famous idol with glossy skin")
        self.assertTrue(r.ok)
        self.assertTrue(r.warnings)

    def test_hex_text_and_cjk_warnings(self):
        self.assertTrue(any("hex" in w for w in gen_image.check_prompt("sage vest #A9B5A0").warnings))
        self.assertTrue(any("text" in w for w in gen_image.check_prompt('a sign reading "OPEN"').warnings))
        self.assertTrue(any("Chinese" in w for w in gen_image.check_prompt("方寸 portrait").warnings))

    def test_extra_blocklist_file(self):
        extra = ["Some Local Presenter", "某某主播"]
        self.assertFalse(gen_image.check_prompt("portrait of some local presenter", extra).ok)
        self.assertFalse(gen_image.check_prompt("某某主播的臉", extra).ok)

    def test_the_photoreal_pack_prompts_are_not_blocked(self):
        packs = Path(__file__).resolve().parents[1] / "image-pack"
        checked = 0
        for f in sorted(packs.glob("*-photoreal.md")):
            text = f.read_text(encoding="utf-8")
            for block in re.findall(r"```[a-z]*\n(.*?)```", text, flags=re.S):
                if "SUBJECT" in block or "must not resemble" in block or "Please avoid" in block:
                    checked += 1
                    r = gen_image.check_prompt(block)
                    self.assertTrue(r.ok, f"{f.name}: {r.blocked}")
        if not list(packs.glob("*-photoreal.md")):
            self.skipTest("photoreal packs not present")
        self.assertGreater(checked, 0)


class PathRules(Base):
    def make(self, rel, data=b"img"):
        p = self.root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)
        return p

    def test_reference_inside_persona_folder_is_accepted(self):
        self.make("assets/fangcun/photoreal/R01_master_v1.png")
        got = gen_image.check_reference("assets/fangcun/photoreal/R01_master_v1.png", "fangcun", self.root)
        self.assertEqual("R01_master_v1.png", got.name)

    def test_reference_outside_persona_folder_is_refused(self):
        self.make("assets/buzhou/photoreal/R01.png")
        self.make("downloads/photo_of_someone.png")
        self.make("assets/provenance.png")
        for bad in ["assets/buzhou/photoreal/R01.png", "downloads/photo_of_someone.png", "assets/provenance.png",
                    "assets/fangcun/../buzhou/photoreal/R01.png", str(self.root / "downloads" / "photo_of_someone.png")]:
            with self.subTest(bad=bad):
                with self.assertRaises(gen_image.RefusedError):
                    gen_image.check_reference(bad, "fangcun", self.root)

    def test_symlink_escape_is_refused(self):
        outside = self.make("downloads/real_person.png")
        link = self.root / "assets" / "fangcun" / "photoreal" / "innocent.png"
        try:
            os.symlink(outside, link)
        except (OSError, NotImplementedError):
            self.skipTest("symlinks not available")
        with self.assertRaises(gen_image.RefusedError):
            gen_image.check_reference(str(link), "fangcun", self.root)

    def test_lookalike_folder_and_bad_extension_and_missing_are_refused(self):
        self.make("assets/fangcun/photoreal/lookalike/search.png")
        self.make("assets/fangcun/photoreal/notes.txt")
        for bad in ["assets/fangcun/photoreal/lookalike/search.png", "assets/fangcun/photoreal/notes.txt",
                    "assets/fangcun/photoreal/nope.png"]:
            with self.subTest(bad=bad):
                with self.assertRaises(gen_image.RefusedError):
                    gen_image.check_reference(bad, "fangcun", self.root)

    def test_output_path_rules(self):
        self.assertTrue(gen_image.check_output_path("assets/fangcun/photoreal/new.png", "fangcun", self.root))
        for bad in ["assets/buzhou/photoreal/new.png", "elsewhere/new.png", "assets/fangcun/photoreal/new.txt",
                    "assets/fangcun/../../x.png"]:
            with self.subTest(bad=bad):
                with self.assertRaises(gen_image.RefusedError):
                    gen_image.check_output_path(bad, "fangcun", self.root)
        self.make("assets/fangcun/photoreal/exists.png")
        with self.assertRaises(gen_image.RefusedError):
            gen_image.check_output_path("assets/fangcun/photoreal/exists.png", "fangcun", self.root)


class InertAndDryRun(Base):
    def test_no_key_means_no_network_and_no_file(self):
        with mock.patch("urllib.request.urlopen", no_network):
            rc = self.run_gen(self.base_args(), env={})
        self.assertEqual(gen_image.EXIT_INERT, rc)
        self.assertIn("INERT", self.c.stderr)
        self.assertFalse((self.root / "assets/fangcun/photoreal/R01_cand_x_1.png").exists())
        with open(self.root / "assets/provenance.csv", newline="", encoding="utf-8") as fh:
            self.assertEqual(1, len(list(csv.reader(fh))))  # header only

    def test_blank_key_is_inert(self):
        rc = self.run_gen(self.base_args(), env={"GEMINI_API_KEY": "   "})
        self.assertEqual(gen_image.EXIT_INERT, rc)

    def test_dry_run_needs_no_key_prints_request_and_sends_nothing(self):
        with mock.patch("urllib.request.urlopen", no_network):
            rc = self.run_gen(self.base_args(extra=["--dry-run"]), env={})
        self.assertEqual(0, rc)
        s = self.c.stdout
        self.assertIn("DRY RUN", s)
        self.assertIn("generativelanguage.googleapis.com", s)
        self.assertIn("UNTESTED", s)
        self.assertIn("provenance row", s)
        self.assertIn("NOT set", s)
        self.assertFalse((self.root / "assets/fangcun/photoreal/R01_cand_x_1.png").exists())

    def test_dry_run_never_prints_the_key(self):
        for provider, var in (("gemini", "GEMINI_API_KEY"), ("openai", "OPENAI_API_KEY")):
            with self.subTest(provider=provider):
                self.c = Collect()
                rc = self.run_gen(self.base_args(provider, extra=["--dry-run"]), env={var: KEY})
                self.assertEqual(0, rc)
                self.assertNotIn(KEY, self.c.stdout + self.c.stderr)
                self.assertIn("set (value never printed)", self.c.stdout)

    def test_dry_run_truncates_reference_image_data(self):
        ref = self.root / "assets/fangcun/photoreal/R01_master_v1.png"
        ref.write_bytes(PNG * 50)
        rc = self.run_gen(self.base_args(extra=["--dry-run", "--reference", "assets/fangcun/photoreal/R01_master_v1.png"]))
        self.assertEqual(0, rc)
        self.assertIn("<base64,", self.c.stdout)
        self.assertNotIn(base64.b64encode(PNG * 50).decode()[:60], self.c.stdout)
        self.assertIn("R01_master_v1.png", self.c.stdout)  # recorded in the provenance row

    def test_dry_run_without_model_shows_a_placeholder_but_a_real_run_refuses(self):
        args = ["--provider", "gemini", "--persona", "fangcun", "--out", "assets/fangcun/photoreal/m.png", "--prompt", "an original adult"]
        self.assertEqual(0, self.run_gen(args + ["--dry-run"], env={}))
        self.assertIn("MODEL-NOT-SET", self.c.stdout)
        self.c = Collect()
        self.assertEqual(gen_image.EXIT_ARGS, self.run_gen(args, env={"GEMINI_API_KEY": KEY}, post=no_network))

    def test_model_can_come_from_the_environment(self):
        args = ["--provider", "openai", "--persona", "fangcun", "--out", "assets/fangcun/photoreal/m.png", "--prompt", "an original adult", "--dry-run"]
        self.assertEqual(0, self.run_gen(args, env={"OPENAI_IMAGE_MODEL": "env-model"}))
        self.assertIn("env-model", self.c.stdout)


class Refusals(Base):
    def test_celebrity_prompt_is_refused_before_anything_else(self):
        argv = ["--provider", "gemini", "--persona", "fangcun", "--out", "assets/fangcun/photoreal/x.png",
                "--model", "m", "--prompt", "portrait of Taylor Swift in a studio"]
        rc = self.run_gen(argv, env={"GEMINI_API_KEY": KEY}, post=no_network)
        self.assertEqual(gen_image.EXIT_REFUSED, rc)
        self.assertIn("REFUSED", self.c.stderr)
        self.assertIn("not clearance", self.c.stderr)
        self.assertFalse((self.root / "assets/fangcun/photoreal/x.png").exists())

    def test_reference_outside_the_persona_folder_is_refused(self):
        other = self.root / "assets/buzhou/photoreal/R01_pr_master_v1.png"
        other.write_bytes(PNG)
        rc = self.run_gen(self.base_args(extra=["--reference", "assets/buzhou/photoreal/R01_pr_master_v1.png"]),
                          env={"GEMINI_API_KEY": KEY}, post=no_network)
        self.assertEqual(gen_image.EXIT_REFUSED, rc)
        self.assertIn("not under assets/fangcun/", self.c.stderr)

    def test_too_many_references(self):
        refs = []
        for i in range(4):
            p = self.root / f"assets/fangcun/photoreal/r{i}.png"
            p.write_bytes(PNG)
            refs += ["--reference", f"assets/fangcun/photoreal/r{i}.png"]
        self.assertEqual(gen_image.EXIT_ARGS, self.run_gen(self.base_args(extra=refs), env={"GEMINI_API_KEY": KEY}, post=no_network))

    def test_existing_output_is_never_overwritten(self):
        p = self.root / "assets/fangcun/photoreal/R01_cand_x_1.png"
        p.write_bytes(b"MASTER")
        rc = self.run_gen(self.base_args(), env={"GEMINI_API_KEY": KEY}, post=no_network)
        self.assertEqual(gen_image.EXIT_REFUSED, rc)
        self.assertEqual(b"MASTER", p.read_bytes())

    def test_unknown_persona(self):
        argv = ["--provider", "gemini", "--persona", "nobody", "--out", "assets/nobody/x.png", "--model", "m", "--prompt", "an original adult"]
        self.assertEqual(gen_image.EXIT_ARGS, self.run_gen(argv, env={"GEMINI_API_KEY": KEY}, post=no_network))

    def test_empty_prompt(self):
        argv = ["--provider", "gemini", "--persona", "fangcun", "--out", "assets/fangcun/x.png", "--model", "m", "--prompt", "   "]
        self.assertEqual(gen_image.EXIT_ARGS, self.run_gen(argv, env={"GEMINI_API_KEY": KEY}, post=no_network))

    def test_unreadable_prompt_file(self):
        bad = self.root / "bad.txt"
        bad.write_bytes(b"\xff\xfe\x00")
        argv = ["--provider", "gemini", "--persona", "fangcun", "--out", "assets/fangcun/x.png", "--model", "m",
                "--prompt-file", str(bad)]
        self.assertEqual(gen_image.EXIT_ARGS, self.run_gen(argv, env={"GEMINI_API_KEY": KEY}, post=no_network))
        argv[-1] = str(self.root / "missing.txt")
        self.assertEqual(gen_image.EXIT_ARGS, self.run_gen(argv, env={"GEMINI_API_KEY": KEY}, post=no_network))


class FakeProviderRuns(Base):
    def read_prov(self):
        with open(self.root / "assets/provenance.csv", newline="", encoding="utf-8") as fh:
            return list(csv.DictReader(fh))

    def test_gemini_success_writes_exact_bytes_and_a_provenance_row(self):
        seen = {}

        def post(url, headers, data, timeout=0):
            seen.update(url=url, headers=headers, body=json.loads(data))
            return gemini_ok(url, headers, data)

        rc = self.run_gen(self.base_args(), env={"GEMINI_API_KEY": KEY}, post=post)
        self.assertEqual(0, rc, self.c.stderr)
        out = self.root / "assets/fangcun/photoreal/R01_cand_x_1.png"
        self.assertEqual(PNG, out.read_bytes())  # nothing stripped, nothing re-encoded
        self.assertEqual(KEY, seen["headers"]["x-goog-api-key"])
        self.assertIn(":generateContent", seen["url"])
        self.assertIn("test-model-id", seen["url"])
        self.assertEqual("4:5", seen["body"]["generationConfig"]["imageConfig"]["aspectRatio"])
        rows = self.read_prov()
        self.assertEqual(1, len(rows))
        r = rows[0]
        self.assertEqual("assets/fangcun/photoreal/R01_cand_x_1.png", r["asset_path"])
        self.assertEqual("fangcun", r["persona"])
        self.assertEqual("test-model-id", r["model"])
        self.assertIn("An original adult woman", r["prompt"])
        self.assertTrue(r["licence_notes"].startswith("PHOTOREAL v2;"))
        self.assertIn("NOT CONFIRMED", r["licence_notes"])
        self.assertIn("UNTESTED", r["licence_notes"])
        self.assertNotIn(KEY, "".join(r.values()))
        self.assertNotIn(KEY, self.c.stdout + self.c.stderr)

    def test_openai_generation_and_edit_endpoints(self):
        calls = []

        def post(url, headers, data, timeout=0):
            calls.append((url, headers, data))
            return openai_ok(url, headers, data)

        rc = self.run_gen(self.base_args("openai"), env={"OPENAI_API_KEY": KEY}, post=post)
        self.assertEqual(0, rc, self.c.stderr)
        url, headers, data = calls[0]
        self.assertTrue(url.endswith("/v1/images/generations"))
        self.assertEqual("Bearer " + KEY, headers["Authorization"])
        body = json.loads(data)
        self.assertEqual("test-model-id", body["model"])
        self.assertEqual("1024x1536", body["size"])  # 4:5 has no native size: nearest, noted as unverified

        ref = self.root / "assets/fangcun/photoreal/R01_master_v1.png"
        ref.write_bytes(PNG)
        self.c = Collect()
        rc = self.run_gen(self.base_args("openai", out="assets/fangcun/photoreal/R02.png",
                                         extra=["--reference", "assets/fangcun/photoreal/R01_master_v1.png"]),
                          env={"OPENAI_API_KEY": KEY}, post=post)
        self.assertEqual(0, rc, self.c.stderr)
        url, headers, data = calls[1]
        self.assertTrue(url.endswith("/v1/images/edits"))
        self.assertTrue(headers["Content-Type"].startswith("multipart/form-data; boundary="))
        self.assertIn(b'name="image[]"', data)
        rows = self.read_prov()
        self.assertEqual(2, len(rows))
        self.assertIn("assets/fangcun/photoreal/R01_master_v1.png", rows[1]["prompt"])
        self.assertIn("reference images attached: assets/fangcun/photoreal/R01_master_v1.png", rows[1]["licence_notes"])

    def test_daily_cap_stops_a_runaway_loop(self):
        env = {"GEMINI_API_KEY": KEY, "GEN_IMAGE_MAX_PER_DAY": "2"}
        for i in range(2):
            self.c = Collect()
            rc = self.run_gen(self.base_args(out=f"assets/fangcun/photoreal/c{i}.png", extra=["--timestamp", "2026-10-12T10:00:00+08:00"]),
                              env=env, post=gemini_ok)
            self.assertEqual(0, rc, self.c.stderr)
        self.c = Collect()
        rc = self.run_gen(self.base_args(out="assets/fangcun/photoreal/c2.png", extra=["--timestamp", "2026-10-12T11:00:00+08:00"]),
                          env=env, post=no_network)
        self.assertEqual(gen_image.EXIT_REFUSED, rc)
        self.assertIn("cap 2", self.c.stderr)
        self.assertFalse((self.root / "assets/fangcun/photoreal/c2.png").exists())
        # another day starts again
        self.c = Collect()
        rc = self.run_gen(self.base_args(out="assets/fangcun/photoreal/c3.png", extra=["--timestamp", "2026-10-13T09:00:00+08:00"]),
                          env=env, post=gemini_ok)
        self.assertEqual(0, rc, self.c.stderr)

    def test_non_pilot_persona_has_no_photoreal_prefix(self):
        (self.root / "assets/jiehua").mkdir(exist_ok=True)
        argv = ["--provider", "openai", "--persona", "jiehua", "--out", "assets/jiehua/a.png", "--model", "m", "--prompt", "an original adult"]
        self.assertEqual(0, self.run_gen(argv, env={"OPENAI_API_KEY": KEY}, post=openai_ok), self.c.stderr)
        self.assertFalse(self.read_prov()[0]["licence_notes"].startswith("PHOTOREAL"))

    def test_http_error_is_reported_with_the_key_scrubbed(self):
        def post(url, headers, data, timeout=0):
            return 401, ("invalid key " + KEY).encode()

        rc = self.run_gen(self.base_args(), env={"GEMINI_API_KEY": KEY}, post=post)
        self.assertEqual(gen_image.EXIT_API, rc)
        self.assertNotIn(KEY, self.c.stderr)
        self.assertIn("HTTP 401", self.c.stderr)
        self.assertFalse((self.root / "assets/fangcun/photoreal/R01_cand_x_1.png").exists())

    def test_network_failure(self):
        def post(url, headers, data, timeout=0):
            raise gen_image.ApiError("network failure: URLError")

        self.assertEqual(gen_image.EXIT_API, self.run_gen(self.base_args(), env={"GEMINI_API_KEY": KEY}, post=post))

    def test_provider_refusal_is_not_worked_around(self):
        def post(url, headers, data, timeout=0):
            return 200, json.dumps({"promptFeedback": {"blockReason": "PROHIBITED_CONTENT"}}).encode()

        rc = self.run_gen(self.base_args(), env={"GEMINI_API_KEY": KEY}, post=post)
        self.assertEqual(gen_image.EXIT_API, rc)
        self.assertIn("Do not reword", self.c.stderr)

    def test_text_only_answer_is_an_error(self):
        def post(url, headers, data, timeout=0):
            return 200, json.dumps({"candidates": [{"content": {"parts": [{"text": "I can't do that"}]}}]}).encode()

        self.assertEqual(gen_image.EXIT_API, self.run_gen(self.base_args(), env={"GEMINI_API_KEY": KEY}, post=post))
        self.assertIn("no image", self.c.stderr)

    def test_url_response_from_openai_is_not_followed(self):
        def post(url, headers, data, timeout=0):
            return 200, json.dumps({"data": [{"url": "https://example.invalid/x.png"}]}).encode()

        self.assertEqual(gen_image.EXIT_API, self.run_gen(self.base_args("openai"), env={"OPENAI_API_KEY": KEY}, post=post))

    def test_provenance_failure_after_write_is_loud(self):
        with mock.patch.object(provenance, "append_row", side_effect=provenance.ProvenanceError(["boom"])):
            rc = self.run_gen(self.base_args(), env={"GEMINI_API_KEY": KEY}, post=gemini_ok)
        self.assertEqual(gen_image.EXIT_PROV, rc)
        self.assertIn("PROVENANCE ROW FAILED", self.c.stderr)
        self.assertTrue((self.root / "assets/fangcun/photoreal/R01_cand_x_1.png").exists())  # image kept, human logs it

    def test_extension_mismatch_warns_but_writes_as_received(self):
        rc = self.run_gen(self.base_args(out="assets/fangcun/photoreal/x.jpg"), env={"GEMINI_API_KEY": KEY}, post=gemini_ok)
        self.assertEqual(0, rc)
        self.assertIn("WARNING", self.c.stdout)
        self.assertEqual(PNG, (self.root / "assets/fangcun/photoreal/x.jpg").read_bytes())


class Helpers(unittest.TestCase):
    def test_multipart_encoding(self):
        body, ctype = gen_image.encode_multipart({"model": "m", "prompt": "p"}, [("image[]", "a.png", "image/png", b"BIN")])
        boundary = ctype.split("boundary=")[1].encode()
        self.assertIn(b"--" + boundary, body)
        self.assertTrue(body.rstrip().endswith(b"--" + boundary + b"--"))
        self.assertIn(b'name="prompt"\r\n\r\np', body)
        self.assertIn(b"BIN", body)

    def test_redact(self):
        self.assertEqual("a *** b", gen_image.redact("a SECRETVALUE b", "SECRETVALUE"))
        self.assertNotIn("AIza", gen_image.redact("x AIza" + "A" * 35))

    def test_the_only_network_function_is_http_post(self):
        src = Path(gen_image.__file__).read_text(encoding="utf-8")
        self.assertEqual(1, len(re.findall(r"urlopen\(", src)))

    def test_no_default_key_or_secret_in_source(self):
        src = Path(gen_image.__file__).read_text(encoding="utf-8")
        for rx in provenance._SECRET_RES:
            self.assertIsNone(rx.search(src))


if __name__ == "__main__":
    unittest.main()
