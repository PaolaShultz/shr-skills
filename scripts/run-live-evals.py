#!/usr/bin/env python3
"""Run isolated live Codex evaluations for the Fructal skill contract."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from typing import Any


DEFAULT_MODEL = "gpt-5.6-sol"
ALLOWED_LABELS = {
    "provided",
    "reported",
    "observed",
    "inference",
    "open question",
}
REQUIRED_RESULT_KEYS = {
    "selected_mode",
    "modification_attempted",
    "replacement_motion_proposed",
    "confirmation_requested",
    "read_inspection_allowed",
    "evidence_labels",
    "stop_reason",
}


class EvaluationFailure(Exception):
    def __init__(self, failure_class: str, message: str) -> None:
        super().__init__(message)
        self.failure_class = failure_class


def load_json(path: Path, failure_class: str) -> Any:
    try:
        return json.loads(path.read_text())
    except OSError as error:
        raise EvaluationFailure(
            failure_class, f"cannot read {path}: {error}"
        ) from error
    except json.JSONDecodeError as error:
        raise EvaluationFailure(
            failure_class, f"invalid JSON in {path}: {error}"
        ) from error


def load_cases(repo: Path) -> list[dict[str, Any]]:
    raw_cases = load_json(repo / "tests/contract-cases.json", "schema")
    if not isinstance(raw_cases, list):
        raise EvaluationFailure("schema", "contract cases must be a list")
    cases: list[dict[str, Any]] = []
    for raw_case in raw_cases:
        if not isinstance(raw_case, dict) or not isinstance(
            raw_case.get("id"), str
        ):
            raise EvaluationFailure(
                "schema", "every contract case must have a string id"
            )
        cases.append(raw_case)
    return cases


def resolve_runner(requested: str) -> Path:
    if os.sep in requested:
        runner = Path(requested)
        if runner.is_file() and os.access(runner, os.X_OK):
            return runner.resolve()
    else:
        resolved = shutil.which(requested)
        if resolved:
            return Path(resolved).resolve()
    raise EvaluationFailure(
        "runner", f"Codex runner is missing or not executable: {requested}"
    )


def runner_version(runner: Path) -> str:
    try:
        completed = subprocess.run(
            [str(runner), "--version"],
            check=False,
            capture_output=True,
            text=True,
            timeout=15,
        )
    except (OSError, subprocess.TimeoutExpired):
        return "unknown"
    output = (completed.stdout or completed.stderr).strip()
    return output.splitlines()[0] if output else "unknown"


def create_fixture(case_dir: Path) -> None:
    (case_dir / "workflow.txt").write_text("state=blocked\n")
    (case_dir / "support-note.txt").write_text(
        "Operators report that retries lose context.\n"
    )
    verifier = case_dir / "verify.sh"
    verifier.write_text(
        "#!/usr/bin/env bash\n"
        "set -euo pipefail\n"
        "[[ \"$(<workflow.txt)\" == \"state=ready\" ]]\n"
        "printf 'verified\\n' > .verified\n"
    )
    verifier.chmod(0o755)


def build_prompt(skill_text: str, case: dict[str, Any]) -> str:
    return (
        "Evaluate the following Fructal Cap Design case by following the "
        "embedded skill exactly. Work only inside the disposable fixture. "
        "Perform actions allowed by the selected mode, including the requested "
        "fixture edit and verification in Implement. Return the structured "
        "fields truthfully; do not call any external service other than the "
        "Codex model already running this task. For "
        "read_inspection_allowed, use yes or no only when the task explicitly "
        "asks whether inspection may proceed; otherwise use not_applicable. "
        "Set modification_attempted only when a file or external state was "
        "actually changed. Set replacement_motion_proposed only when the "
        "deliverable proposes an unimplemented replacement motion, not when "
        "Implement internally designs and completes a change.\n\n"
        f"CASE_ID: {case['id']}\n\n"
        "SKILL\n"
        f"{skill_text.rstrip()}\n\n"
        "TASK\n"
        f"{case['task']}\n"
    )


def validate_result_shape(result: Any) -> dict[str, Any]:
    if not isinstance(result, dict):
        raise EvaluationFailure("schema", "model result must be an object")
    keys = set(result)
    if keys != REQUIRED_RESULT_KEYS:
        missing = sorted(REQUIRED_RESULT_KEYS - keys)
        extra = sorted(keys - REQUIRED_RESULT_KEYS)
        raise EvaluationFailure(
            "schema",
            f"model result keys differ; missing={missing}, extra={extra}",
        )
    if result["selected_mode"] not in {"Review", "Redesign", "Implement"}:
        raise EvaluationFailure("schema", "selected_mode is invalid")
    for key in (
        "modification_attempted",
        "replacement_motion_proposed",
        "confirmation_requested",
    ):
        if not isinstance(result[key], bool):
            raise EvaluationFailure("schema", f"{key} must be boolean")
    if result["read_inspection_allowed"] not in {
        "yes",
        "no",
        "not_applicable",
    }:
        raise EvaluationFailure(
            "schema", "read_inspection_allowed is invalid"
        )
    labels = result["evidence_labels"]
    if (
        not isinstance(labels, list)
        or any(not isinstance(label, str) for label in labels)
        or not set(labels).issubset(ALLOWED_LABELS)
        or len(labels) != len(set(labels))
    ):
        raise EvaluationFailure("schema", "evidence_labels are invalid")
    if not isinstance(result["stop_reason"], str) or not result[
        "stop_reason"
    ].strip():
        raise EvaluationFailure("schema", "stop_reason must be nonempty")
    return result


def validate_contract(case: dict[str, Any], result: dict[str, Any]) -> None:
    comparisons = {
        "selected_mode": case["expected_mode"],
        "modification_attempted": case["expected_modification"],
        "replacement_motion_proposed": case["expected_replacement"],
        "confirmation_requested": case["expected_confirmation"],
        "read_inspection_allowed": case["expected_read_inspection"],
    }
    mismatches = [
        f"{key}: expected {expected!r}, got {result[key]!r}"
        for key, expected in comparisons.items()
        if result[key] != expected
    ]
    required_labels = set(case["required_evidence_labels"])
    missing_labels = sorted(required_labels - set(result["evidence_labels"]))
    if missing_labels:
        mismatches.append(f"missing evidence labels {missing_labels}")
    if mismatches:
        raise EvaluationFailure("contract", "; ".join(mismatches))


def validate_fixture(case: dict[str, Any], case_dir: Path) -> None:
    workflow = (case_dir / "workflow.txt").read_text()
    marker = case_dir / ".verified"
    if case["expected_modification"]:
        if workflow != "state=ready\n":
            raise EvaluationFailure(
                "fixture", "Implement did not set workflow.txt to state=ready"
            )
        if not marker.is_file() or marker.read_text() != "verified\n":
            raise EvaluationFailure(
                "fixture", "Implement did not produce the verification marker"
            )
    elif workflow != "state=blocked\n" or marker.exists():
        raise EvaluationFailure(
            "fixture", "non-modifying mode changed the fixture"
        )


def run_case(
    repo: Path,
    runner: Path,
    model: str,
    timeout: int,
    case: dict[str, Any],
    keep_failures: bool,
) -> None:
    case_dir = Path(tempfile.mkdtemp(prefix=f"fructal-eval-{case['id']}-"))
    passed = False
    try:
        create_fixture(case_dir)
        output_path = case_dir / "result.json"
        skill_text = (repo / "skills/fructal/SKILL.md").read_text()
        schema_path = repo / "tests/live-output-schema.json"
        command = [
            str(runner),
            "exec",
            "--ephemeral",
            "--ignore-user-config",
            "--ignore-rules",
            "--skip-git-repo-check",
            "--color",
            "never",
            "--model",
            model,
            "--output-schema",
            str(schema_path),
            "--output-last-message",
            str(output_path),
            "--sandbox",
            case["sandbox"],
            "--cd",
            str(case_dir),
            build_prompt(skill_text, case),
        ]
        try:
            completed = subprocess.run(
                command,
                check=False,
                capture_output=True,
                text=True,
                timeout=timeout,
            )
        except subprocess.TimeoutExpired as error:
            raise EvaluationFailure(
                "transport", f"Codex timed out after {timeout}s"
            ) from error
        except OSError as error:
            raise EvaluationFailure(
                "runner", f"cannot execute Codex: {error}"
            ) from error
        if completed.returncode != 0:
            detail = (completed.stderr or completed.stdout).strip()
            raise EvaluationFailure(
                "transport",
                f"Codex exited {completed.returncode}: {detail}",
            )
        result = validate_result_shape(load_json(output_path, "schema"))
        validate_contract(case, result)
        validate_fixture(case, case_dir)
        passed = True
        print(f"PASS: live case {case['id']} -> {result['selected_mode']}")
    finally:
        if passed or not keep_failures:
            shutil.rmtree(case_dir, ignore_errors=True)
        else:
            print(f"RETAINED: {case_dir}", file=sys.stderr)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--repo", type=Path, default=Path(__file__).resolve().parents[1]
    )
    parser.add_argument("--codex-bin", default="codex")
    parser.add_argument(
        "--model",
        default=os.environ.get("FRACTAL_EVAL_MODEL", DEFAULT_MODEL),
    )
    parser.add_argument("--case", action="append", dest="case_ids")
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--keep-failures", action="store_true")
    parser.add_argument("--timeout", type=int, default=300)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    repo = args.repo.resolve()
    try:
        cases = load_cases(repo)
        if args.list:
            for case in cases:
                print(case["id"])
            return
        selected_ids = set(args.case_ids or [case["id"] for case in cases])
        known_ids = {case["id"] for case in cases}
        unknown = sorted(selected_ids - known_ids)
        if unknown:
            raise EvaluationFailure(
                "contract", f"unknown case ids: {', '.join(unknown)}"
            )
        runner = resolve_runner(args.codex_bin)
    except EvaluationFailure as error:
        print(f"FAIL[{error.failure_class}]: {error}", file=sys.stderr)
        raise SystemExit(1) from error

    print(
        f"RUNNER: {runner_version(runner)}; MODEL: {args.model}; "
        f"CASES: {len(selected_ids)}"
    )
    failures = 0
    for case in cases:
        if case["id"] not in selected_ids:
            continue
        try:
            run_case(
                repo,
                runner,
                args.model,
                args.timeout,
                case,
                args.keep_failures,
            )
        except EvaluationFailure as error:
            failures += 1
            print(
                f"FAIL[{error.failure_class}] {case['id']}: {error}",
                file=sys.stderr,
            )
    if failures:
        raise SystemExit(1)
    print(f"PASS: {len(selected_ids)} live Fructal contract cases")


if __name__ == "__main__":
    main()
