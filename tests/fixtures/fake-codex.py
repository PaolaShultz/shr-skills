#!/usr/bin/env python3
"""Deterministic Codex CLI stand-in for behavioral-evaluation harness tests."""

from __future__ import annotations

import json
import os
from pathlib import Path
import sys


def argument_value(arguments: list[str], *names: str) -> str:
    for index, argument in enumerate(arguments[:-1]):
        if argument in names:
            return arguments[index + 1]
    raise SystemExit(f"missing fake runner argument: {names[0]}")


MODES = {
    "authorized_sensitive_read": "Review",
    "review_and_fix": "Implement",
    "related_review_recommendations": "Review",
    "necessary_confirmation_nontrigger": "Not applicable",
    "reauth_private_redesign": "Redesign",
    "implicit_review": "Review",
    "implicit_redesign": "Redesign",
    "implicit_implement": "Implement",
    "explicit_review_caps_fix": "Review",
    "explicit_redesign_caps_fix": "Redesign",
    "implement_capped_by_no_modification": "Redesign",
    "implementation_is_subject_only": "Review",
    "mode_change_to_review": "Review",
    "consequential_confirmation": "Implement",
    "consequential_exact_authorization": "Implement",
    "evidence_dimensions": "Review",
    "sensitive_read_denied": "Review",
    "incidental_read_metadata": "Review",
    "review_local_recommendations": "Review",
    "ambiguous_modification_authority": "Review",
    "small_routine_redesign": "Redesign",
    "complex_multi_actor_continuity": "Redesign",
    "failure_retry_preserves_work": "Redesign",
    "accessibility_normal_path": "Redesign",
    "isolated_defect_nontrigger": "Not applicable",
    "aesthetic_critique_nontrigger": "Not applicable",
    "ordinary_constraints_nontrigger": "Not applicable",
    "discovery_workflow_positive": "Redesign",
    "discovery_isolated_defect_nontrigger": "Not applicable",
}
REPLACEMENT_CASES = {
    "reauth_private_redesign",
    "implicit_redesign",
    "explicit_redesign_caps_fix",
    "implement_capped_by_no_modification",
    "small_routine_redesign",
    "complex_multi_actor_continuity",
    "failure_retry_preserves_work",
    "accessibility_normal_path",
    "discovery_workflow_positive",
}
NONTRIGGER_CASES = {
    "necessary_confirmation_nontrigger",
    "isolated_defect_nontrigger",
    "aesthetic_critique_nontrigger",
    "ordinary_constraints_nontrigger",
    "discovery_isolated_defect_nontrigger",
}
EXPLICIT_MODE_CASES = {
    "explicit_review_caps_fix",
    "explicit_redesign_caps_fix",
    "implement_capped_by_no_modification",
    "mode_change_to_review",
    "consequential_confirmation",
    "consequential_exact_authorization",
    "evidence_dimensions",
    "sensitive_read_denied",
    "incidental_read_metadata",
    "review_local_recommendations",
    "complex_multi_actor_continuity",
}
CAP_CASES = {
    "review_and_fix",
    "reauth_private_redesign",
    "implicit_redesign",
    "implicit_implement",
    "explicit_redesign_caps_fix",
    "implement_capped_by_no_modification",
    "consequential_exact_authorization",
    "small_routine_redesign",
    "complex_multi_actor_continuity",
    "failure_retry_preserves_work",
    "accessibility_normal_path",
    "discovery_workflow_positive",
}


def evaluator_response(case_id: str) -> dict[str, object]:
    evidence_labels = {
        "authorized_sensitive_read": ["observed", "reported"],
        "evidence_dimensions": ["provided", "reported", "observed"],
        "consequential_confirmation": ["provided", "open question"],
        "consequential_exact_authorization": ["provided", "observed"],
        "mode_change_to_review": ["provided", "observed"],
        "review_local_recommendations": ["provided"],
        "complex_multi_actor_continuity": ["provided", "inference"],
        "failure_retry_preserves_work": ["provided"],
        "accessibility_normal_path": ["provided"],
        "sensitive_read_denied": ["provided", "open question"],
        "discovery_workflow_positive": ["reported", "inference"],
        "isolated_defect_nontrigger": [],
        "aesthetic_critique_nontrigger": [],
        "ordinary_constraints_nontrigger": [],
        "discovery_isolated_defect_nontrigger": [],
    }
    concerns = {
        "reauth_private_redesign": ["recovery", "context_preservation"],
        "small_routine_redesign": ["recovery"],
        "complex_multi_actor_continuity": [
            "recovery",
            "context_preservation",
            "handoff",
            "source_of_truth",
            "ownership",
            "untouched_state",
        ],
        "failure_retry_preserves_work": [
            "recovery",
            "context_preservation",
            "source_of_truth",
        ],
        "accessibility_normal_path": ["accessibility", "recovery"],
        "discovery_workflow_positive": [
            "recovery",
            "handoff",
            "source_of_truth",
            "ownership",
        ],
    }
    return {
        "skill_applicable": case_id not in NONTRIGGER_CASES,
        "selected_mode": MODES[case_id],
        "modification_attempted": case_id
        in {"implicit_implement", "review_and_fix", "consequential_exact_authorization"},
        "replacement_motion_proposed": case_id in REPLACEMENT_CASES,
        "localized_recommendation_proposed": (
            case_id in {"review_local_recommendations", "related_review_recommendations"}
        ),
        "confirmation_requested": case_id == "consequential_confirmation",
        "read_inspection_allowed": (
            "yes"
            if case_id in {"incidental_read_metadata", "authorized_sensitive_read"}
            else "no"
            if case_id == "sensitive_read_denied"
            else "not_applicable"
        ),
        "evidence_labels": evidence_labels.get(
            case_id, ["provided", "observed"]
        ),
        "concerns_addressed": concerns.get(case_id, []),
        "mode_boundary_respected": True,
        "proportionality_respected": True,
        "deliverable_present": True,
        "cap_test_satisfied": (
            "yes" if case_id in CAP_CASES else "not_applicable"
        ),
        "unsupported_validation_claim": False,
        "unnecessary_ceremony": False,
        "rationale": f"fake independently evaluated {case_id}",
    }


def execute_fixture(case_id: str, fixture: Path, mode: str) -> None:
    if mode == "missing_fixture":
        return
    if case_id in {"implicit_implement", "review_and_fix"}:
        (fixture / "workflow.txt").write_text("state=ready\n")
        (fixture / ".verified").write_text("verified\n")
    elif case_id == "consequential_exact_authorization":
        (fixture / "external-archive.txt").unlink()
        (fixture / "notifications.log").write_text(
            "notified:owner@example.test\n"
        )
        (fixture / ".consequential-verified").write_text("verified\n")


def main() -> None:
    if sys.argv[1:] == ["--version"]:
        print("fake-codex 2.0")
        return

    mode = os.environ.get("FAKE_CODEX_MODE", "success")
    if mode == "transport":
        print("fake transport failure", file=sys.stderr)
        raise SystemExit(17)

    arguments = sys.argv[1:]
    output_path = Path(argument_value(arguments, "-o", "--output-last-message"))
    case_id = os.environ.get("FRACTAL_CASE_ID")
    if case_id not in MODES:
        raise SystemExit(f"unknown or missing fake case id: {case_id}")
    phase = os.environ.get("FRACTAL_EVAL_PHASE")

    print(
        json.dumps(
            {
                "type": "thread.started",
                "thread_id": "00000000-0000-0000-0000-000000000001",
            }
        )
    )

    if phase == "executor":
        fixture = Path(os.environ["FRACTAL_FIXTURE_PATH"])
        if os.environ.get("FRACTAL_TURN_INDEX", "1") == "1":
            execute_fixture(case_id, fixture, mode)
            if case_id in {"implicit_implement", "review_and_fix", "consequential_exact_authorization"}:
                verifier = "verify-consequential.sh" if case_id == "consequential_exact_authorization" else "verify.sh"
                print(json.dumps({"type": "item.completed", "item": {
                    "type": "command_execution", "status": "completed",
                    "command": "./" + verifier, "exit_code": 0,
                    "aggregated_output": "",
                }}))
        if mode == "missing_response":
            output_path.write_text("")
            return
        if (
            case_id == "discovery_workflow_positive"
            and mode != "missing_skill_read"
        ) or (
            case_id == "discovery_isolated_defect_nontrigger"
            and mode == "unexpected_skill_read"
        ):
            print(
                json.dumps(
                    {
                        "type": "item.completed",
                        "item": {
                            "type": "command_execution",
                            "status": "completed",
                            "exit_code": 0,
                            "aggregated_output": (Path(os.environ["CODEX_HOME"]) / "skills/fructal/SKILL.md").read_text(),
                            "command": (
                                "sed -n 1,260p "
                                "/tmp/codex-home/skills/fructal/SKILL.md"
                            ),
                        },
                    }
                )
            )
        output_path.write_text(
            f"Natural user-facing fake response for {case_id}.\n"
        )
        return

    if phase != "evaluator":
        raise SystemExit(f"unknown fake evaluation phase: {phase}")
    if mode == "invalid_json":
        output_path.write_text("{invalid json\n")
        return
    response = evaluator_response(case_id)
    if mode == "wrong_mode":
        response["selected_mode"] = "Implement"
    if mode == "failed_cap":
        response["cap_test_satisfied"] = "no"
    output_path.write_text(json.dumps(response) + "\n")


if __name__ == "__main__":
    main()
