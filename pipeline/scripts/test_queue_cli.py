"""Tests of queue.py as a program (run in a subprocess), including the stdlib name-clash guard."""
import json
import subprocess
import sys
import unittest
from pathlib import Path

import testutil

SCRIPTS = Path(__file__).resolve().parent


def run(*args, cwd=SCRIPTS):
    return subprocess.run([sys.executable, *args], cwd=cwd, capture_output=True, text=True, encoding="utf-8", timeout=60)


class QueueScript(unittest.TestCase):
    def setUp(self):
        self.tmp, self.root = testutil.make_root()
        self.addCleanup(self.tmp.cleanup)

    def test_help(self):
        r = run("queue.py", "--help")
        self.assertEqual(0, r.returncode, r.stderr)
        for word in ("new-draft", "validate", "list", "approve"):
            self.assertIn(word, r.stdout)

    def test_new_draft_and_validate_as_a_program(self):
        r = run("queue.py", "--root", str(self.root), "new-draft", "--persona", "buzhou", "--platform", "youtube_shorts",
                "--format", "short", "--date", "2026-11-17")
        self.assertEqual(0, r.returncode, r.stderr)
        post = json.loads((self.root / "pipeline/review-queue/buzhou/2026-11-17_01/post.json").read_text(encoding="utf-8"))
        self.assertEqual("buzhou-2026-11-17-01", post["id"])
        r = run("queue.py", "--root", str(self.root), "validate")
        self.assertEqual(1, r.returncode)
        self.assertIn("incomplete", r.stdout)

    def test_approve_has_no_way_to_approve(self):
        r = run("queue.py", "approve", "--help")
        self.assertEqual(0, r.returncode)
        self.assertNotIn("--set", r.stdout)
        self.assertIn("never approves", run("queue.py", "--help").stdout)

    def test_importing_queue_from_this_folder_still_gives_the_standard_library(self):
        code = "import queue; q = queue.Queue(); q.put(7); print(q.get(), queue.Empty.__name__)"
        r = run("-c", code, cwd=SCRIPTS)  # cwd on sys.path: queue.py would shadow the stdlib without the guard
        self.assertEqual(0, r.returncode, r.stderr)
        self.assertEqual("7 Empty", r.stdout.strip())

    def test_thread_pool_works_with_this_folder_on_the_path(self):
        code = "from concurrent.futures import ThreadPoolExecutor as T\nwith T(2) as ex: print(sum(ex.map(lambda x: x, [1, 2, 3])))"
        r = run("-c", code, cwd=SCRIPTS)
        self.assertEqual(0, r.returncode, r.stderr)
        self.assertEqual("6", r.stdout.strip())


if __name__ == "__main__":
    unittest.main()
