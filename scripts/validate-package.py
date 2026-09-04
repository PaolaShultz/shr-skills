#!/usr/bin/env python3
"""Validate the Fructal Cap Design source package and an optional installed copy."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Any

import yaml


EXPECTED_VERSION = "1.1.1"
EXPECTED_SOURCE = (
    "https://github.com/PaolaShultz/shr-skills/tree/main/skills/fructal"
)
PUBLIC_DISPLAY_NAME = "Fructal Cap Design"
EXPECTED_CASES = {
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
LIVE_CASE_FIELDS = {
    "task",
    "expected_modification",
    "expected_replacement",
    "expected_confirmation",
    "expected_read_inspection",
    "required_evidence_labels",
    "sandbox",
}
LIVE_RESULT_FIELDS = {
    "skill_applicable",
    "selected_mode",
    "modification_attempted",
    "replacement_motion_proposed",
    "localized_recommendation_proposed",
    "confirmation_requested",
    "read_inspection_allowed",
    "evidence_labels",
    "concerns_addressed",
    "mode_label_visible",
    "mode_boundary_respected",
    "proportionality_respected",
    "deliverable_present",
    "cap_test_satisfied",
    "unsupported_validation_claim",
    "unnecessary_ceremony",
    "rationale",
}
EVIDENCE_LABELS = {
    "provided",
    "reported",
    "observed",
    "inference",
    "open question",
}
WORKFLOW_CONCERNS = {
    "recovery",
    "context_preservation",
    "handoff",
    "source_of_truth",
    "accessibility",
    "ownership",
    "untouched_state",
}
REQUIRED_SKILL_TEXT = {
    "narrow activation contract is missing": (
        "A requirement or\nconstraint alone does not qualify"
    ),
    "explicit invocation bypasses activation gate": (
        "Explicit `$fructal` invocation does not override this gate"
    ),
    "activation gate is missing": "## Pass the activation gate",
    "proportional application contract is missing": "## Apply proportionally",
    "mode selection contract is missing": "## Select and hold one mode",
    "Review execution path is missing": "### Review",
    "Redesign execution path is missing": "### Redesign",
    "Implement execution path is missing": "### Implement",
    "explicit-mode precedence contract is missing": (
        "An explicit Review, Redesign, or Implement instruction"
    ),
    "incidental read-side-effect contract is missing": "ordinary access metadata",
    "provided-artifact and reported-claim distinction is missing": (
        "`provided artifact` containing a `reported claim`"
    ),
    "actor-appropriate feedback contract is missing": (
        "services, devices, and software components"
    ),
    "Six-question cap acceptance loop is missing": (
        "## Run the six-question cap test in Redesign and Implement"
    ),
    "concrete accessibility verification is missing": "assistive technology",
    "before-and-after behavior contract is missing": "before-and-after behavior",
    "conditional mode visibility contract is missing": (
        "start the final report by stating the selected mode once"
    ),
    "implicit mode suppression contract is missing": (
        "never expose the internal mode as a heading or completion label"
    ),
    "mode phrase distinction is missing": (
        "selects the mode internally but does not expose its label"
    ),
    "incomplete consequential stop boundary is missing": (
        "without inventing or prescribing the future"
    ),
    "consequential confirmation request is missing": (
        "ask once\nfor the exact missing items and confirmation"
    ),
    "silent automatic use contract is missing": (
        "Do not announce, link, or credit Fructal Cap Design"
    ),
    "bounded Review recommendation contract is missing": (
        "Bounded recommendations tied directly to findings are allowed"
    ),
    "bounded Review recommendation limit is missing": (
        "recommendations collectively define that motion"
    ),
    "set-level Review recommendation check is missing": (
        "Judge the recommendation set as a whole"
    ),
    "proportionate evidence-label contract is missing": (
        "label\n   them explicitly only when status matters"
    ),
    "proportionate cap-test reporting contract is missing": (
        "do not print six ceremonial\nanswers"
    ),
    "proportionate path verification contract is missing": (
        "Do\nnot enumerate or test paths the change cannot affect"
    ),
}


class Validation:
    def __init__(self) -> None:
        self.failures: list[str] = []

    def require(self, condition: bool, message: str) -> None:
        if not condition:
            self.failures.append(message)

    def finish(self) -> None:
        if self.failures:
            for failure in self.failures:
                print(f"FAIL: {failure}", file=sys.stderr)
            raise SystemExit(1)


def load_text(path: Path, validation: Validation, label: str) -> str:
    if not path.is_file():
        validation.failures.append(f"missing {label}")
        return ""
    try:
        return path.read_text()
    except OSError as error:
        validation.failures.append(f"cannot read {label}: {error}")
        return ""


def parse_skill_frontmatter(
    text: str, validation: Validation
) -> dict[str, Any]:
    match = re.match(r"\A---\n(.*?)\n---(?:\n|\Z)", text, re.DOTALL)
    if not match:
        validation.failures.append("SKILL.md frontmatter delimiters are invalid")
        return {}
    try:
        parsed = yaml.safe_load(match.group(1))
    except yaml.YAMLError as error:
        validation.failures.append(
            f"invalid SKILL.md frontmatter YAML: {error}"
        )
        return {}
    if not isinstance(parsed, dict):
        validation.failures.append("SKILL.md frontmatter must be a mapping")
        return {}
    return parsed


def parse_agent_metadata(
    text: str, validation: Validation
) -> dict[str, Any]:
    try:
        parsed = yaml.safe_load(text)
    except yaml.YAMLError as error:
        validation.failures.append(
            f"invalid agents/openai.yaml YAML: {error}"
        )
        return {}
    if not isinstance(parsed, dict):
        validation.failures.append("agents/openai.yaml must be a mapping")
        return {}
    return parsed


def normalized_nonblank_lines(text: str) -> list[str]:
    return [line for line in text.splitlines() if line.strip()]


def contains_mapping_key(value: Any, key: str) -> bool:
    if isinstance(value, dict):
        return key in value or any(
            contains_mapping_key(child, key) for child in value.values()
        )
    if isinstance(value, list):
        return any(contains_mapping_key(child, key) for child in value)
    return False


def extract_demo_skill(text: str, validation: Validation) -> str:
    lines = text.splitlines()
    try:
        start = lines.index("SKILL") + 1
    except ValueError:
        validation.failures.append("ChatGPT demo SKILL marker is missing")
        return ""

    for index in range(start, len(lines) - 1):
        if lines[index] == "TASK" and lines[index + 1] == "[INSERT YOUR TASK HERE]":
            return "\n".join(lines[start:index]) + "\n"

    validation.failures.append("ChatGPT demo TASK slot is missing")
    return ""


def validate_public_naming(repo: Path, validation: Validation) -> None:
    public_paths = [
        repo / "AGENTS.md",
        repo / "README.md",
        repo / "examples/chatgpt-web-demo.md",
        repo / "scripts/run-live-evals.py",
        repo / "skills/fructal/SKILL.md",
        repo / "skills/fructal/agents/openai.yaml",
        *sorted((repo / "docs").rglob("*.md")),
    ]
    short_name = re.escape(PUBLIC_DISPLAY_NAME.split()[0])
    shortened = re.compile(rf"\b{short_name}\b(?! Cap Design)")

    for path in public_paths:
        text = load_text(path, validation, str(path.relative_to(repo)))
        if shortened.search(text):
            validation.failures.append(
                "public prose shortens the Fructal Cap Design name: "
                f"{path.relative_to(repo)}"
            )


def validate_contract_cases(
    path: Path, validation: Validation
) -> int:
    text = load_text(path, validation, "tests/contract-cases.json")
    if not text:
        return 0
    try:
        cases = json.loads(text)
    except json.JSONDecodeError as error:
        validation.failures.append(f"invalid contract-cases.json: {error}")
        return 0
    if not isinstance(cases, list):
        validation.failures.append("contract-cases.json must contain a list")
        return 0

    found: dict[str, Any] = {}
    for case in cases:
        if not isinstance(case, dict) or not isinstance(case.get("id"), str):
            validation.failures.append("every contract case must have a string id")
            continue
        case_id = case["id"]
        if case_id in found:
            validation.failures.append(f"duplicate contract case {case_id}")
        found[case_id] = case

    for case_id, expected_mode in EXPECTED_CASES.items():
        case = found.get(case_id)
        if case is None:
            validation.failures.append(f"missing contract case {case_id}")
            continue
        if case.get("expected_mode") != expected_mode:
            validation.failures.append(
                f"contract case {case_id} must expect {expected_mode}"
            )
        for field in sorted(LIVE_CASE_FIELDS):
            if field not in case:
                validation.failures.append(
                    f"contract case {case_id} is missing {field}"
                )
        if not isinstance(case.get("task"), str) or not case.get("task", "").strip():
            validation.failures.append(
                f"contract case {case_id} task must be nonempty"
            )
        for field in (
            "expected_modification",
            "expected_replacement",
            "expected_confirmation",
        ):
            if not isinstance(case.get(field), bool):
                validation.failures.append(
                    f"contract case {case_id} {field} must be boolean"
                )
        if case.get("expected_read_inspection") not in {
            "yes",
            "no",
            "not_applicable",
        }:
            validation.failures.append(
                f"contract case {case_id} expected_read_inspection is invalid"
            )
        labels = case.get("required_evidence_labels")
        if (
            not isinstance(labels, list)
            or any(not isinstance(label, str) for label in labels)
            or not set(labels).issubset(EVIDENCE_LABELS)
            or len(labels) != len(set(labels))
        ):
            validation.failures.append(
                f"contract case {case_id} required_evidence_labels are invalid"
            )
        if not isinstance(case.get("expected_applicable", True), bool):
            validation.failures.append(
                f"contract case {case_id} expected_applicable must be boolean"
            )
        if case.get("expected_cap_test", "not_applicable") not in {
            "yes",
            "no",
            "not_applicable",
        }:
            validation.failures.append(
                f"contract case {case_id} expected_cap_test is invalid"
            )
        if not isinstance(
            case.get("expected_localized_recommendation", False), bool
        ):
            validation.failures.append(
                f"contract case {case_id} expected_localized_recommendation "
                "must be boolean"
            )
        concerns = case.get("required_concerns", [])
        if (
            not isinstance(concerns, list)
            or any(not isinstance(concern, str) for concern in concerns)
            or not set(concerns).issubset(WORKFLOW_CONCERNS)
            or len(concerns) != len(set(concerns))
        ):
            validation.failures.append(
                f"contract case {case_id} required_concerns are invalid"
            )
        if case.get("sandbox") not in {"read-only", "workspace-write"}:
            validation.failures.append(
                f"contract case {case_id} sandbox is invalid"
            )
        if case.get("prompt_style", "embedded") not in {
            "embedded",
            "discovery",
        }:
            validation.failures.append(
                f"contract case {case_id} prompt_style is invalid"
            )
        if case.get("expected_skill_read", "not_applicable") not in {
            "yes",
            "no",
            "not_applicable",
        }:
            validation.failures.append(
                f"contract case {case_id} expected_skill_read is invalid"
            )
        follow_ups = case.get("follow_up_turns", [])
        if (
            not isinstance(follow_ups, list)
            or any(
                not isinstance(turn, str) or not turn.strip()
                for turn in follow_ups
            )
        ):
            validation.failures.append(
                f"contract case {case_id} follow_up_turns are invalid"
            )
        if case.get("fixture_expectation", "unchanged") not in {
            "unchanged",
            "workflow_ready",
            "consequential",
        }:
            validation.failures.append(
                f"contract case {case_id} fixture_expectation is invalid"
            )
        if not isinstance(case.get("forbid_sensitive_read", False), bool):
            validation.failures.append(
                f"contract case {case_id} forbid_sensitive_read must be boolean"
            )

    extras = sorted(set(found) - set(EXPECTED_CASES))
    validation.require(
        not extras,
        f"unexpected contract cases: {', '.join(extras)}",
    )
    return len(found)


def validate_live_output_schema(
    path: Path, validation: Validation
) -> None:
    text = load_text(path, validation, "tests/live-output-schema.json")
    if not text:
        return
    try:
        schema = json.loads(text)
    except json.JSONDecodeError as error:
        validation.failures.append(f"invalid live-output-schema.json: {error}")
        return
    if not isinstance(schema, dict):
        validation.failures.append("live output schema must be an object")
        return
    validation.require(
        set(schema.get("required", [])) == LIVE_RESULT_FIELDS,
        "live output schema required fields differ",
    )
    properties = schema.get("properties")
    validation.require(
        isinstance(properties, dict)
        and set(properties) == LIVE_RESULT_FIELDS,
        "live output schema properties differ",
    )
    validation.require(
        schema.get("additionalProperties") is False,
        "live output schema must reject additional properties",
    )
    validation.require(
        not contains_mapping_key(schema, "uniqueItems"),
        "live output schema uses unsupported keyword uniqueItems",
    )


def validate_evaluation_freezes(repo: Path, validation: Validation) -> None:
    evaluations = repo / "docs/evaluations"
    for manifest in sorted(evaluations.rglob("SHA256SUMS")):
        label = str(manifest.relative_to(repo))
        text = load_text(manifest, validation, label)
        for line_number, line in enumerate(text.splitlines(), start=1):
            match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
            if match is None:
                validation.failures.append(
                    f"invalid checksum entry in {label}:{line_number}"
                )
                continue
            expected, relative_name = match.groups()
            archive = manifest.parent.resolve()
            artifact = (manifest.parent / relative_name).resolve()
            try:
                artifact.relative_to(archive)
            except ValueError:
                validation.failures.append(
                    f"checksum entry escapes its archive in {label}:{line_number}"
                )
                continue
            if not artifact.is_file():
                validation.failures.append(
                    f"frozen artifact is missing: "
                    f"{artifact.relative_to(repo)}"
                )
                continue
            observed = hashlib.sha256(artifact.read_bytes()).hexdigest()
            if observed != expected:
                validation.failures.append(
                    f"frozen artifact checksum differs: "
                    f"{artifact.relative_to(repo)}"
                )


def validate_package(repo: Path, installed: Path | None) -> None:
    validation = Validation()
    skill_path = repo / "skills/fructal/SKILL.md"
    agent_path = repo / "skills/fructal/agents/openai.yaml"
    readme_path = repo / "README.md"
    demo_path = repo / "examples/chatgpt-web-demo.md"
    cases_path = repo / "tests/contract-cases.json"
    live_schema_path = repo / "tests/live-output-schema.json"

    validation.require(
        not (repo / "skills/fructal-cap-design").exists(),
        "legacy skills/fructal-cap-design directory remains",
    )

    skill_text = load_text(skill_path, validation, "skills/fructal/SKILL.md")
    agent_text = load_text(
        agent_path, validation, "skills/fructal/agents/openai.yaml"
    )
    readme_text = load_text(readme_path, validation, "README.md")
    demo_text = load_text(demo_path, validation, "examples/chatgpt-web-demo.md")

    frontmatter = parse_skill_frontmatter(skill_text, validation)
    validation.require(
        set(frontmatter).issubset(
            {"name", "description", "license", "allowed-tools", "metadata"}
        ),
        "SKILL.md frontmatter contains unsupported keys",
    )
    validation.require(frontmatter.get("name") == "fructal", "skill name is not fructal")
    description = frontmatter.get("description")
    validation.require(
        isinstance(description, str) and description.startswith("Use when "),
        "skill description does not start with Use when",
    )
    metadata = frontmatter.get("metadata")
    if not isinstance(metadata, dict):
        metadata = {}
    validation.require(
        metadata.get("version") == EXPECTED_VERSION,
        f"metadata.version must be {EXPECTED_VERSION}",
    )
    validation.require(
        metadata.get("source") == EXPECTED_SOURCE,
        "metadata.source must be the canonical skill URL",
    )

    agent = parse_agent_metadata(agent_text, validation)
    interface = agent.get("interface") if isinstance(agent, dict) else None
    validation.require(
        isinstance(interface, dict),
        "agents/openai.yaml interface must be a mapping",
    )
    if isinstance(interface, dict):
        validation.require(
            interface.get("display_name") == "Fructal Cap Design",
            "agent display_name must be Fructal Cap Design",
        )
        validation.require(
            isinstance(interface.get("short_description"), str)
            and bool(interface["short_description"].strip()),
            "agent short_description is missing",
        )
        validation.require(
            isinstance(interface.get("default_prompt"), str)
            and "$fructal" in interface["default_prompt"],
            "agent default_prompt does not invoke $fructal",
        )

    for message, required_text in REQUIRED_SKILL_TEXT.items():
        validation.require(required_text in skill_text, message)

    for label in ("`provided`", "`reported`", "`observed`", "`inference`", "`open question`"):
        validation.require(label in skill_text, f"{label} evidence label is missing")

    for heading in ("Review:", "Redesign:", "Implement:"):
        validation.require(
            re.search(rf"^{re.escape(heading)}$", readme_text, re.MULTILINE)
            is not None,
            f"README does not expose {heading[:-1]}",
        )
    validation.require(
        "skills/fructal" in readme_text,
        "README does not use the current install path",
    )
    validate_public_naming(repo, validation)

    embedded_skill = extract_demo_skill(demo_text, validation)
    if embedded_skill:
        validation.require(
            normalized_nonblank_lines(embedded_skill)
            == normalized_nonblank_lines(skill_text),
            "embedded ChatGPT demo skill differs from canonical SKILL.md",
        )

    case_count = validate_contract_cases(cases_path, validation)
    validate_live_output_schema(live_schema_path, validation)
    validate_evaluation_freezes(repo, validation)

    installed_state = "not requested"
    if installed is not None:
        installed_skill = load_text(
            installed / "SKILL.md", validation, "installed SKILL.md"
        )
        installed_agent = load_text(
            installed / "agents/openai.yaml",
            validation,
            "installed agents/openai.yaml",
        )
        validation.require(
            installed_skill == skill_text,
            "installed SKILL.md differs from source",
        )
        validation.require(
            installed_agent == agent_text,
            "installed agents/openai.yaml differs from source",
        )
        installed_state = "matches source"

    validation.finish()
    word_count = len(skill_text.split())
    print(
        "PASS: Fructal Cap Design package "
        f"{EXPECTED_VERSION} is valid "
        f"({case_count} contract cases, {word_count} skill words, "
        f"installed: {installed_state})."
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--installed", type=Path)
    args = parser.parse_args()
    validate_package(args.repo.resolve(), args.installed.resolve() if args.installed else None)


if __name__ == "__main__":
    main()
