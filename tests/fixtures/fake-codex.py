#!/usr/bin/env python3
"""Deterministic Codex CLI stand-in for live-evaluation harness tests."""

from __future__ import annotations

import json
import os
from pathlib import Path
import re
import sys


def argument_value(arguments: list[str], *names: str) -> str:
    for index, argument in enumerate(arguments[:-1]):
        if argument in names:
            return arguments[index + 1]
    raise SystemExit(f"missing fake runner argument: {names[0]}")


def response_for(case_id: str) -> dict[str, object]:
    modes = {
        "implicit_review": "Review",
        "implicit_redesign": "Redesign",
        "implicit_implement": "Implement",
        "explicit_review_caps_fix": "Review",
        "explicit_redesign_caps_fix": "Redesign",
        "implement_capped_by_no_modification": "Redesign",
        "implementation_is_subject_only": "Review",
        "mode_change_to_review": "Review",
        "consequential_confirmation": "Implement",
        "evidence_dimensions": "Review",
        "incidental_read_metadata": "Review",
    }
    replacement_cases = {
        "implicit_redesign",
        "explicit_redesign_caps_fix",
        "implement_capped_by_no_modification",
    }
    evidence_labels = {
        "evidence_dimensions": ["provided", "reported", "observed"],
        "consequential_confirmation": ["provided", "open question"],
        "mode_change_to_review": ["provided"],
    }
    return {
        "selected_mode": modes[case_id],
        "modification_attempted": case_id == "implicit_implement",
        "replacement_motion_proposed": case_id in replacement_cases,
        "confirmation_requested": case_id == "consequential_confirmation",
        "read_inspection_allowed": (
            "yes" if case_id == "incidental_read_metadata" else "not_applicable"
        ),
        "evidence_labels": evidence_labels.get(
            case_id, ["provided", "observed"]
        ),
        "stop_reason": f"fake completed {case_id}",
    }


def main() -> None:
    if sys.argv[1:] == ["--version"]:
        print("fake-codex 1.0")
        return

    mode = os.environ.get("FAKE_CODEX_MODE", "success")
    if mode == "transport":
        print("fake transport failure", file=sys.stderr)
        raise SystemExit(17)

    arguments = sys.argv[1:]
    output_path = Path(argument_value(arguments, "-o", "--output-last-message"))
    fixture_path = Path(argument_value(arguments, "-C", "--cd"))
    prompt = arguments[-1]
    match = re.search(r"^CASE_ID: ([a-z0-9_]+)$", prompt, re.MULTILINE)
    if not match:
        raise SystemExit("fake runner prompt has no CASE_ID")
    if (
        "For read_inspection_allowed, use yes or no only when the task "
        "explicitly asks whether inspection may proceed"
    ) not in prompt:
        raise SystemExit("fake runner prompt does not define read inspection")
    case_id = match.group(1)

    if mode == "invalid_json":
        output_path.write_text("{invalid json\n")
        return

    response = response_for(case_id)
    if mode == "wrong_mode":
        response["selected_mode"] = "Implement"

    if case_id == "implicit_implement" and mode != "missing_fixture":
        workflow = fixture_path / "workflow.txt"
        workflow.write_text("state=ready\n")
        (fixture_path / ".verified").write_text("verified\n")

    output_path.write_text(json.dumps(response) + "\n")


if __name__ == "__main__":
    main()
