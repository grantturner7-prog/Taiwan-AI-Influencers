import csv
import io
import unittest
from pathlib import Path
from unittest import mock

import provenance
import testutil


def row(**over):
    r = {
        "timestamp": "2026-10-12T10:00:00+08:00",
        "asset_path": "assets/fangcun/photoreal/a.png",
        "persona": "fangcun",
        "tool": "Gemini (app)",
        "model": "label as shown",
        "prompt": "line one, with comma\nline two with \"quotes\"",
        "licence_notes": "commercial use per those terms: NOT CONFIRMED",
    }
    r.update(over)
    return r


class ProvenanceTests(unittest.TestCase):
    def setUp(self):
        self.tmp, self.root = testutil.make_root()
        self.addCleanup(self.tmp.cleanup)
        (self.root / "assets" / "fangcun" / "photoreal" / "a.png").write_bytes(b"x")
        self.csv = self.root / "assets" / "provenance.csv"

    def read_rows(self):
        with open(self.csv, newline="", encoding="utf-8") as fh:
            return list(csv.reader(fh))

    def test_valid_row_is_appended_and_round_trips(self):
        provenance.append_row(row(), self.root)
        rows = self.read_rows()
        self.assertEqual(provenance.COLUMNS, rows[0])
        self.assertEqual(2, len(rows))
        self.assertEqual(row()["prompt"], rows[1][5])  # commas, newline and quotes survive
        self.assertEqual("fangcun", rows[1][2])

    def test_header_is_the_documented_one(self):
        self.assertEqual(["timestamp", "asset_path", "persona", "tool", "model", "prompt", "licence_notes"], provenance.COLUMNS)
        with open(Path(__file__).resolve().parents[2] / "assets" / "provenance.csv", newline="", encoding="utf-8") as fh:
            self.assertEqual(provenance.COLUMNS, next(csv.reader(fh)))

    def test_every_missing_or_blank_field_is_refused_and_nothing_is_written(self):
        before = self.csv.read_bytes()
        for col in provenance.COLUMNS:
            for bad in (None, "", "   "):
                with self.subTest(col=col, bad=bad):
                    r = row()
                    if bad is None:
                        del r[col]
                    else:
                        r[col] = bad
                    with self.assertRaises(provenance.ProvenanceError):
                        provenance.append_row(r, self.root)
        self.assertEqual(before, self.csv.read_bytes())

    def test_missing_file_is_refused_unless_overridden(self):
        with self.assertRaises(provenance.ProvenanceError):
            provenance.append_row(row(asset_path="assets/fangcun/photoreal/nope.png"), self.root)
        provenance.append_row(row(asset_path="assets/fangcun/photoreal/nope.png"), self.root, check_exists=False)

    def test_path_rules(self):
        for bad in ("/etc/passwd", "../outside.png", "assets/../../x.png", "C:\\x.png"):
            with self.subTest(bad=bad):
                self.assertTrue(provenance.validate_row(row(asset_path=bad), self.root, check_exists=False))

    def test_persona_rules(self):
        self.assertTrue(provenance.validate_row(row(persona="nobody"), self.root))
        self.assertTrue(provenance.validate_row(row(persona="Fang Cun"), self.root))
        self.assertEqual([], provenance.validate_row(row(persona="studio"), self.root))

    def test_timestamp_rules(self):
        self.assertEqual([], provenance.validate_row(row(timestamp="2026-10-11"), self.root))
        self.assertEqual([], provenance.validate_row(row(timestamp="2026-10-12T09:30:00+08:00"), self.root))
        for bad in ("yesterday", "2026-13-40", "12/10/2026", "2026-10-12T25:00:00+08:00"):
            with self.subTest(bad=bad):
                self.assertTrue(provenance.validate_row(row(timestamp=bad), self.root))

    def test_secrets_are_refused(self):
        for secret in ("AIza" + "A" * 35, "sk-" + "b" * 30, "Bearer " + "c" * 30, "api_key=" + "d" * 20):
            with self.subTest(secret=secret[:6]):
                self.assertTrue(provenance.validate_row(row(prompt="prompt " + secret), self.root))
                self.assertTrue(provenance.validate_row(row(licence_notes=secret), self.root))

    def test_wrong_header_is_never_touched(self):
        self.csv.write_text("a,b,c\r\n", encoding="utf-8")
        before = self.csv.read_bytes()
        with self.assertRaises(provenance.ProvenanceError):
            provenance.append_row(row(), self.root)
        self.assertEqual(before, self.csv.read_bytes())

    def test_old_rows_are_never_rewritten_and_a_missing_newline_is_repaired(self):
        provenance.append_row(row(), self.root)
        data = self.csv.read_bytes().rstrip(b"\r\n")  # simulate an editor that dropped the final newline
        self.csv.write_bytes(data)
        provenance.append_row(row(asset_path="assets/fangcun/photoreal/a.png", prompt="second"), self.root)
        new = self.csv.read_bytes()
        self.assertTrue(new.startswith(data))
        self.assertEqual(3, len(self.read_rows()))

    def test_creates_file_with_header_when_missing(self):
        self.csv.unlink()
        provenance.append_row(row(), self.root)
        self.assertEqual(provenance.COLUMNS, self.read_rows()[0])

    def test_unknown_columns_are_refused(self):
        r = row()
        r["extra"] = "x"
        with self.assertRaises(provenance.ProvenanceError):
            provenance.append_row(r, self.root)

    def test_check_file(self):
        provenance.append_row(row(), self.root)
        self.assertEqual([], provenance.check_file(self.root))
        with open(self.csv, "ab") as fh:
            fh.write(b"a,b\r\n")
        probs = provenance.check_file(self.root)
        self.assertTrue(any("2 fields" in p for p in probs))

    def test_cli_add_and_check(self):
        out = io.StringIO()
        with mock.patch("sys.stdout", out):
            rc = provenance.main(["--root", str(self.root), "add", "--asset", "assets/fangcun/photoreal/a.png",
                                  "--persona", "fangcun", "--tool", "t", "--model", "m", "--prompt", "p",
                                  "--licence-notes", "NOT CONFIRMED", "--timestamp", "2026-10-12"])
        self.assertEqual(0, rc)
        with mock.patch("sys.stdout", io.StringIO()):
            self.assertEqual(0, provenance.main(["--root", str(self.root), "check"]))
        err = io.StringIO()
        with mock.patch("sys.stderr", err):
            rc = provenance.main(["--root", str(self.root), "add", "--asset", "assets/fangcun/photoreal/missing.png",
                                  "--persona", "fangcun", "--tool", "t", "--model", "m", "--prompt", "p",
                                  "--licence-notes", "n", "--timestamp", "2026-10-12"])
        self.assertEqual(1, rc)
        self.assertIn("REFUSED", err.getvalue())

    def test_cli_unreadable_prompt_file_is_refused_without_a_traceback(self):
        err = io.StringIO()
        with mock.patch("sys.stderr", err):
            rc = provenance.main(["--root", str(self.root), "add", "--asset", "assets/fangcun/photoreal/a.png",
                                  "--persona", "fangcun", "--tool", "t", "--model", "m",
                                  "--prompt-file", str(self.root / "does-not-exist.txt"),
                                  "--licence-notes", "n", "--timestamp", "2026-10-12"])
        self.assertEqual(2, rc)
        self.assertIn("REFUSED", err.getvalue())
        bad = self.root / "bad.txt"
        bad.write_bytes(b"\xff\xfe\x00")
        with mock.patch("sys.stderr", io.StringIO()):
            rc = provenance.main(["--root", str(self.root), "add", "--asset", "assets/fangcun/photoreal/a.png",
                                  "--persona", "fangcun", "--tool", "t", "--model", "m", "--prompt-file", str(bad),
                                  "--licence-notes", "n", "--timestamp", "2026-10-12"])
        self.assertEqual(2, rc)
        self.assertEqual(1, len(self.read_rows()))  # header only


if __name__ == "__main__":
    unittest.main()
