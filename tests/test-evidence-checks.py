#!/usr/bin/env python3
"""Regression probes for observed evidence and preserved fixture state."""

import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


SPEC = importlib.util.spec_from_file_location(
    "live_evals", Path(__file__).resolve().parents[1] / "scripts/run-live-evals.py"
)
LIVE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(LIVE)


def event(command, output="", exit_code=0):
    return json.dumps({"type": "item.completed", "item": {
        "type": "command_execution", "status": "completed",
        "command": command, "aggregated_output": output, "exit_code": exit_code,
    }})


class EvidenceChecks(unittest.TestCase):
    def test_path_mention_is_not_inspection(self):
        mention = json.dumps({"type": "item.completed", "item": {
            "type": "agent_message", "text": "I did not read skills/fructal/SKILL.md",
        }})
        self.assertFalse(LIVE.skill_read_observed(mention, "contract body"))
        self.assertFalse(LIVE.skill_read_observed(event("cat skills/fructal/SKILL.md", "", 1), "contract body"))

    def test_relative_read_and_chunked_content(self):
        events = event("cd skills/fructal && sed -n 1p SKILL.md", "first line\n")
        events += "\n" + event("sed -n 2p SKILL.md", "second line\n")
        self.assertTrue(LIVE.skill_read_observed(events, "first line\nsecond line\n"))
        self.assertFalse(LIVE.skill_read_observed(events, "first line\nmissing line\n"))

    def test_full_command_results_reach_judge(self):
        output = "x" * 17000 + "VERIFIER FAILED"
        rendered = LIVE.readable_events(event("./verify.sh", output, 1))
        self.assertIn(output, rendered)
        self.assertIn("exit_code=1", rendered)

    def test_nested_permission_and_symlink_changes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "nested").mkdir()
            file = root / "nested/state.txt"
            file.write_text("keep")
            before = LIVE.snapshot_fixture(root)
            file.chmod(0o600)
            self.assertNotEqual(before, LIVE.snapshot_fixture(root))
            (root / "link").symlink_to("nested/state.txt")
            self.assertEqual(LIVE.snapshot_fixture(root)["link"], {"symlink": "nested/state.txt"})

    def test_marker_alone_and_unrelated_mutation_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "workflow.txt").write_text("state=blocked\n")
            (root / "other.txt").write_text("keep")
            before = LIVE.snapshot_fixture(root)
            (root / "workflow.txt").write_text("state=ready\n")
            (root / ".verified").write_text("verified\n")
            case = {"expected_modification": True}
            with self.assertRaisesRegex(LIVE.EvaluationFailure, "verifier execution"):
                LIVE.validate_fixture(case, root, before, LIVE.snapshot_fixture(root), "", "")
            LIVE.validate_fixture(case, root, before, LIVE.snapshot_fixture(root), "", event("/bin/bash -lc './verify.sh'"))
            (root / "other.txt").write_text("corrupted")
            with self.assertRaisesRegex(LIVE.EvaluationFailure, "unrelated state"):
                LIVE.validate_fixture(case, root, before, LIVE.snapshot_fixture(root), "", event("./verify.sh"))

    def test_encoded_forbidden_read_rejected(self):
        case = {"expected_modification": False, "forbid_sensitive_read": True}
        with self.assertRaisesRegex(LIVE.EvaluationFailure, "evidence was read"):
            LIVE.validate_fixture(case, Path("."), {}, {}, "", event("base64 sensitive.txt", "U0VOU0lUSVZF"))


if __name__ == "__main__":
    unittest.main()
