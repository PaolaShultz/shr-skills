#!/usr/bin/env python3
"""Checks for deterministic FSI-001 result compilation."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


ARCHIVE = Path(__file__).resolve().parents[1]
SCRIPT = ARCHIVE / "evaluation" / "compile_results.py"


def load_compiler():
    spec = importlib.util.spec_from_file_location("fsi_compile", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load result compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CompileResultsTests(unittest.TestCase):
    def test_compilation_counts_runs_and_agreed_task_outcomes(self):
        compiler = load_compiler()
        result = compiler.compile_results()
        self.assertEqual(result["valid_runs"], 18)
        self.assertEqual(
            result["evaluator_agreement"]["task_success"],
            {"agree": 18, "disagree": 0},
        )
        self.assertEqual(
            result["task_success_consensus"],
            {"yes": 13, "partial": 3, "no": 2},
        )

    def test_compilation_detects_combined_method_read_suppression(self):
        compiler = load_compiler()
        result = compiler.compile_results()
        reads = result["combined_skill_reads"]
        self.assertEqual(reads["contract_a_read_cases"], 1)
        self.assertEqual(reads["contract_b_read_cases"], 6)
        self.assertEqual(reads["contract_a_not_read_cases"], 5)

    def test_only_one_combined_arm_improves_beyond_both_singles(self):
        compiler = load_compiler()
        result = compiler.compile_results()
        self.assertEqual(
            result["combined_better_than_both_singles"],
            ["case-04-local-publication"],
        )

    def test_obligation_dataset_preserves_both_evaluators(self):
        compiler = load_compiler()
        records = compiler.compile_obligations()
        self.assertEqual(len(records), 445)
        self.assertEqual(
            {record["evaluator_id"] for record in records},
            {"evaluator-1", "evaluator-2"},
        )
        self.assertTrue(
            all(
                {
                    "case_id",
                    "condition",
                    "method",
                    "contract",
                    "status",
                    "evidence",
                }.issubset(record)
                for record in records
            )
        )

    def test_derived_run_evidence_contains_read_order_and_interactions(self):
        compiler = load_compiler()
        records = compiler.compile_derived_run_evidence()
        self.assertEqual(len(records), 18)
        case = records[
            "case-02-response-only-redesign/combined"
        ]
        self.assertEqual(
            case["unique_skill_first_read_order"][:2],
            ["superpowers:using-superpowers", "fructal"],
        )
        self.assertEqual(case["evaluator_question_counts"], [0, 0])
        self.assertFalse(case["approval_pause_observed"])

    def test_checksum_manifest_is_sorted_and_excludes_itself(self):
        compiler = load_compiler()
        lines = compiler.checksum_lines()
        self.assertEqual(lines, sorted(lines, key=lambda line: line.split("  ", 1)[1]))
        self.assertFalse(any(line.endswith("  SHA256SUMS") for line in lines))
        self.assertFalse(any("__pycache__" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
