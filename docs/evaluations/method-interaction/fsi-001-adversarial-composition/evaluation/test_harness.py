#!/usr/bin/env python3
"""Deterministic checks for the FSI-001 experiment harness."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


ARCHIVE = Path(__file__).resolve().parents[1]
HARNESS_PATH = ARCHIVE / "evaluation" / "harness.py"


def load_harness():
    spec = importlib.util.spec_from_file_location("fsi_harness", HARNESS_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load harness module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class HarnessTests(unittest.TestCase):
    def test_all_six_method_blind_prompts_have_unique_frozen_hashes(self):
        harness = load_harness()
        prompts = sorted((ARCHIVE / "frozen-inputs" / "prompts").glob("*.md"))
        self.assertEqual(len(prompts), 6)
        hashes = {
            hashlib.sha256(path.read_bytes()).hexdigest() for path in prompts
        }
        self.assertEqual(len(hashes), 6)
        for path in prompts:
            text = path.read_text()
            self.assertNotIn("Fructal Cap Design", text)
            self.assertNotIn("Superpowers", text)
            self.assertEqual(harness.case_id_from_prompt(path), path.stem)

    def test_condition_skill_catalogs_are_exact(self):
        harness = load_harness()
        expected = {
            "fructal-only": {"fructal"},
            "superpowers-only": {
                f"superpowers:{name}"
                for name in harness.SUPERPOWERS_SKILL_NAMES
            },
            "combined": {
                "fructal",
                *{
                    f"superpowers:{name}"
                    for name in harness.SUPERPOWERS_SKILL_NAMES
                },
            },
        }
        self.assertEqual(harness.EXPECTED_USER_SKILLS, expected)

    def test_six_frozen_fixture_repositories_clone_identically(self):
        harness = load_harness()
        bundles = sorted(
            (ARCHIVE / "frozen-inputs" / "fixture-bundles").glob("*.bundle")
        )
        self.assertEqual(len(bundles), 6)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for bundle in bundles:
                first = root / f"{bundle.stem}-first"
                second = root / f"{bundle.stem}-second"
                harness.materialize_fixture(bundle.stem, first)
                harness.materialize_fixture(bundle.stem, second)
                self.assertEqual(
                    harness.git(first, "rev-parse", "HEAD"),
                    harness.git(second, "rev-parse", "HEAD"),
                )
                self.assertEqual(
                    harness.hash_tree(first), harness.hash_tree(second)
                )

    def test_source_hashes_cover_every_relevant_skill_file(self):
        hashes = json.loads(
            (ARCHIVE / "frozen-inputs" / "source-hashes.json").read_text()
        )
        superpower_keys = {
            key
            for key in hashes
            if key.startswith("superpowers/skills/")
            and key.endswith("/SKILL.md")
        }
        self.assertEqual(len(superpower_keys), 14)
        self.assertIn("skills/fructal/SKILL.md", hashes)

    def test_generator_fixture_allows_exactly_one_attempt(self):
        harness = load_harness()
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary) / "workspace"
            harness.materialize_fixture("case-05-one-attempt", workspace)
            first = harness.run_local_generator(workspace)
            second = harness.run_local_generator(workspace)
            self.assertEqual(first.returncode, 0)
            self.assertNotEqual(second.returncode, 0)
            self.assertEqual(
                (workspace / "generation-count.txt").read_text(), "2\n"
            )
            self.assertIn(
                "STATUS: amber", (workspace / "artifact.txt").read_text()
            )

    def test_frozen_artifacts_are_byte_identical_after_live_doc_edit(self):
        harness = load_harness()
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary) / "workspace"
            harness.materialize_fixture("case-03-doc-correction", workspace)
            frozen_before = harness.hash_tree(workspace / "frozen")
            live = workspace / "guide.md"
            live.write_text(live.read_text().replace("reties", "retries"))
            self.assertEqual(
                harness.hash_tree(workspace / "frozen"), frozen_before
            )

    def test_sanitizer_removes_sensitive_fields_recursively(self):
        harness = load_harness()
        raw = {
            "auth": {"access_token": "secret", "safe": 1},
            "encrypted_content": "ciphertext",
            "nested": [{"api_key": "secret", "value": "kept"}],
        }
        sanitized = harness.sanitize_object(raw)
        self.assertEqual(
            sanitized,
            {"auth": {"safe": 1}, "nested": [{"value": "kept"}]},
        )

    def test_obligation_schema_uses_frozen_status_vocabulary(self):
        schema = json.loads(
            (ARCHIVE / "frozen-inputs" / "obligation-schema.json").read_text()
        )
        statuses = schema["properties"]["status"]["enum"]
        self.assertEqual(
            statuses,
            [
                "satisfied",
                "redundantly duplicated",
                "explicitly superseded by task instructions",
                "silently suppressed",
                "violated",
                "responsible for blocking or extra recovery",
            ],
        )

    def test_evaluator_workspace_redacts_method_identities(self):
        harness = load_harness()
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary) / "workspace"
            harness.build_evaluator_workspace(workspace)
            forbidden = (
                "Fructal Cap Design",
                "Superpowers",
                "fructal-only",
                "superpowers-only",
                "/skills/fructal/",
                "/superpowers/skills/",
            )
            for path in workspace.rglob("*"):
                if not path.is_file():
                    continue
                if path.suffix == ".gz":
                    import gzip

                    with gzip.open(path, "rt") as handle:
                        text = handle.read()
                else:
                    text = path.read_text()
                for marker in forbidden:
                    self.assertNotIn(marker, text, f"{marker} in {path}")


if __name__ == "__main__":
    unittest.main()
