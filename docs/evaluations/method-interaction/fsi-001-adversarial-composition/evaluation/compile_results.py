#!/usr/bin/env python3
"""Compile frozen FSI-001 runs and evaluator judgments."""

from __future__ import annotations

from collections import Counter
import gzip
import hashlib
import json
from pathlib import Path
import re
from typing import Any


ARCHIVE = Path(__file__).resolve().parents[1]
CONDITIONS = ("fructal-only", "superpowers-only", "combined")
SUCCESS_ORDER = {"no": 0, "partial": 1, "yes": 2}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def skill_reads(trace: Path) -> list[str]:
    reads: list[str] = []
    with gzip.open(trace, "rt") as handle:
        for line in handle:
            item = json.loads(line)
            payload = item.get("payload", {})
            if not (
                item.get("type") == "response_item"
                and payload.get("type")
                in ("custom_tool_call", "function_call")
            ):
                continue
            call = str(
                payload.get("input") or payload.get("arguments") or ""
            )
            for path in re.findall(r"/[^\s\"']*SKILL\.md", call):
                if "/superpowers/skills/" in path:
                    name = path.split("/superpowers/skills/", 1)[1].split(
                        "/", 1
                    )[0]
                    reads.append(f"superpowers:{name}")
                elif "/skills/.system/" in path:
                    name = path.split("/skills/.system/", 1)[1].split(
                        "/", 1
                    )[0]
                    reads.append(f"system:{name}")
                elif "/skills/fructal/" in path:
                    reads.append("fructal")
    return reads


def compile_derived_run_evidence() -> dict[str, dict[str, Any]]:
    first = evaluator_assessments("evaluator-1")
    second = evaluator_assessments("evaluator-2")
    records: dict[str, dict[str, Any]] = {}
    for metadata_path in sorted((ARCHIVE / "runs").glob("*/*/metadata.json")):
        run_dir = metadata_path.parent
        metadata = load_json(metadata_path)
        case_id = metadata["case_id"]
        condition = metadata["condition"]
        before = load_json(run_dir / "fixture-before.json")
        after = load_json(run_dir / "fixture-after.json")
        before_tree = before["tree_hashes"]
        after_tree = after["tree_hashes"]
        modified = sorted(
            path
            for path in before_tree.keys() & after_tree.keys()
            if before_tree[path] != after_tree[path]
        )
        added = sorted(after_tree.keys() - before_tree.keys())
        removed = sorted(before_tree.keys() - after_tree.keys())
        reads = skill_reads(run_dir / "session.jsonl.gz")
        unique_reads = list(dict.fromkeys(reads))
        before_remote = set(before.get("remote_refs", "").splitlines())
        after_remote = set(after.get("remote_refs", "").splitlines())
        questions = [
            first[(case_id, condition)]["questions"],
            second[(case_id, condition)]["questions"],
        ]
        records[f"{case_id}/{condition}"] = {
            "case_id": case_id,
            "condition": condition,
            "skill_read_events": reads,
            "unique_skill_first_read_order": unique_reads,
            "modified_files": modified,
            "added_files": added,
            "removed_files": removed,
            "fixture_branch_before": before["branch"],
            "fixture_branch_after": after["branch"],
            "fixture_head_before": before["head"],
            "fixture_head_after": after["head"],
            "local_remote_refs_added": sorted(after_remote - before_remote),
            "evaluator_question_counts": questions,
            "approval_policy": metadata["approval_policy"],
            "approval_pause_observed": any(questions),
            "exit_status": metadata["exit_status"],
            "cleanup": load_json(run_dir / "cleanup.json"),
        }
    return records


def evaluator_assessments(evaluator_id: str) -> dict[tuple[str, str], dict]:
    mapping = load_json(
        ARCHIVE / "frozen-inputs" / "evaluator-mapping.json"
    )["arms"]
    result = load_json(
        ARCHIVE / "evaluation" / evaluator_id / "evaluation.json"
    )
    assessments: dict[tuple[str, str], dict] = {}
    for assessment in result["case_assessments"]:
        case_id = assessment["case_id"]
        condition = mapping[case_id][assessment["arm_label"]]
        assessments[(case_id, condition)] = assessment
    return assessments


def compile_obligations() -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    method_for_contract = {
        "A": "Fructal Cap Design",
        "B": "Superpowers",
    }
    available_contracts = {
        "fructal-only": {"A"},
        "superpowers-only": {"B"},
        "combined": {"A", "B"},
    }
    mapping = load_json(
        ARCHIVE / "frozen-inputs" / "evaluator-mapping.json"
    )["arms"]
    for evaluator_id in ("evaluator-1", "evaluator-2"):
        result = load_json(
            ARCHIVE / "evaluation" / evaluator_id / "evaluation.json"
        )
        for assessment in result["case_assessments"]:
            case_id = assessment["case_id"]
            arm_label = assessment["arm_label"]
            condition = mapping[case_id][arm_label]
            for obligation in assessment["obligations"]:
                contract = obligation["contract"]
                records.append(
                    {
                        "evaluator_id": evaluator_id,
                        "case_id": case_id,
                        "arm_label": arm_label,
                        "condition": condition,
                        "contract": contract,
                        "method": method_for_contract[contract],
                        "contract_available": contract
                        in available_contracts[condition],
                        "obligation": obligation["obligation"],
                        "status": obligation["status"],
                        "evidence": obligation["evidence"],
                        "consequence": obligation["consequence"],
                        "recovery_cost": obligation["recovery_cost"],
                    }
                )
    return records


def count_field(assessments: dict, field: str) -> dict[str, int]:
    return dict(sorted(Counter(item[field] for item in assessments.values()).items()))


def checksum_lines() -> list[str]:
    lines: list[str] = []
    for path in sorted(ARCHIVE.rglob("*")):
        relative = path.relative_to(ARCHIVE)
        if (
            not path.is_file()
            or path.name == "SHA256SUMS"
            or "__pycache__" in relative.parts
        ):
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        lines.append(f"{digest}  {relative}")
    return lines


def combined_skill_reads() -> dict[str, Any]:
    contract_a_cases: list[str] = []
    contract_b_cases: list[str] = []
    read_order: dict[str, list[str]] = {}
    for trace in sorted((ARCHIVE / "runs").glob("*/combined/session.jsonl.gz")):
        case_id = trace.parent.parent.name
        calls: list[str] = []
        with gzip.open(trace, "rt") as handle:
            for line in handle:
                item = json.loads(line)
                payload = item.get("payload", {})
                if (
                    item.get("type") == "response_item"
                    and payload.get("type")
                    in ("custom_tool_call", "function_call")
                ):
                    calls.append(
                        str(
                            payload.get("input")
                            or payload.get("arguments")
                            or ""
                        )
                    )
        text = "\n".join(calls)
        a_position = text.find("/skills/fructal/SKILL.md")
        b_position = text.find("/superpowers/skills/")
        order: list[tuple[int, str]] = []
        if a_position >= 0:
            contract_a_cases.append(case_id)
            order.append((a_position, "Contract A"))
        if b_position >= 0:
            contract_b_cases.append(case_id)
            order.append((b_position, "Contract B"))
        read_order[case_id] = [label for _, label in sorted(order)]
    all_cases = sorted(path.parent.parent.name for path in (ARCHIVE / "runs").glob("*/combined/metadata.json"))
    return {
        "contract_a_read_cases": len(contract_a_cases),
        "contract_b_read_cases": len(contract_b_cases),
        "contract_a_not_read_cases": len(all_cases) - len(contract_a_cases),
        "contract_a_case_ids": sorted(contract_a_cases),
        "contract_b_case_ids": sorted(contract_b_cases),
        "read_order": read_order,
    }


def compile_results() -> dict[str, Any]:
    runs = sorted((ARCHIVE / "runs").glob("*/*/metadata.json"))
    valid_runs = 0
    run_metrics: dict[str, dict[str, Any]] = {}
    for metadata_path in runs:
        run_dir = metadata_path.parent
        metadata = load_json(metadata_path)
        diagnostic = load_json(
            run_dir / "capability-diagnostic" / "result.json"
        )
        cleanup = load_json(run_dir / "cleanup.json")
        trace_valid = False
        try:
            with gzip.open(run_dir / "session.jsonl.gz", "rt") as handle:
                trace_valid = any(True for _ in handle)
        except OSError:
            trace_valid = False
        valid = (
            diagnostic["no_other_user_skills"]
            and metadata["exit_status"] == 0
            and cleanup["temporary_root_removed"]
            and cleanup["auth_state_removed"]
            and trace_valid
        )
        valid_runs += int(valid)
        metrics = load_json(run_dir / "metrics.json")
        usage = metrics.get("usage", {})
        run_metrics.setdefault(metadata["case_id"], {})[
            metadata["condition"]
        ] = {
            "elapsed_seconds": metrics["elapsed_seconds"],
            "input_tokens": usage.get("input_tokens"),
            "cached_input_tokens": usage.get("cached_input_tokens"),
            "output_tokens": usage.get("output_tokens"),
            "reasoning_output_tokens": usage.get("reasoning_output_tokens"),
            "compatible_counter_semantics": metrics[
                "token_counter_semantics"
            ],
        }

    first = evaluator_assessments("evaluator-1")
    second = evaluator_assessments("evaluator-2")
    keys = sorted(first)
    agreement: dict[str, dict[str, int]] = {}
    for field in (
        "task_success",
        "static_conflict",
        "behavioral_conflict",
        "severity",
        "precedence",
    ):
        agree = sum(first[key][field] == second[key][field] for key in keys)
        agreement[field] = {"agree": agree, "disagree": len(keys) - agree}

    task_success = Counter()
    consensus_by_arm: dict[str, str] = {}
    for key in keys:
        if first[key]["task_success"] != second[key]["task_success"]:
            raise RuntimeError(f"task-success disagreement for {key}")
        status = first[key]["task_success"]
        task_success[status] += 1
        consensus_by_arm[f"{key[0]}/{key[1]}"] = status

    combined_better: list[str] = []
    for case_id in sorted({key[0] for key in keys}):
        combined = SUCCESS_ORDER[consensus_by_arm[f"{case_id}/combined"]]
        singles = [
            SUCCESS_ORDER[
                consensus_by_arm[f"{case_id}/fructal-only"]
            ],
            SUCCESS_ORDER[
                consensus_by_arm[f"{case_id}/superpowers-only"]
            ],
        ]
        if combined > max(singles):
            combined_better.append(case_id)

    overhead: dict[str, Any] = {}
    totals = {
        condition: {
            "elapsed_seconds": 0.0,
            "input_tokens": 0,
            "output_tokens": 0,
        }
        for condition in CONDITIONS
    }
    for case_id, case_metrics in sorted(run_metrics.items()):
        combined = case_metrics["combined"]
        overhead[case_id] = {}
        for single in ("fructal-only", "superpowers-only"):
            comparison = case_metrics[single]
            overhead[case_id][f"combined_minus_{single}"] = {
                "elapsed_seconds": round(
                    combined["elapsed_seconds"]
                    - comparison["elapsed_seconds"],
                    3,
                ),
                "input_tokens": combined["input_tokens"]
                - comparison["input_tokens"],
                "output_tokens": combined["output_tokens"]
                - comparison["output_tokens"],
            }
        for condition in CONDITIONS:
            totals[condition]["elapsed_seconds"] += case_metrics[condition][
                "elapsed_seconds"
            ]
            totals[condition]["input_tokens"] += case_metrics[condition][
                "input_tokens"
            ]
            totals[condition]["output_tokens"] += case_metrics[condition][
                "output_tokens"
            ]
    for condition in CONDITIONS:
        totals[condition]["elapsed_seconds"] = round(
            totals[condition]["elapsed_seconds"], 3
        )

    evaluator_summaries: dict[str, Any] = {}
    for evaluator_id, assessments in (
        ("evaluator-1", first),
        ("evaluator-2", second),
    ):
        obligations = Counter()
        by_contract = Counter()
        for assessment in assessments.values():
            for obligation in assessment["obligations"]:
                obligations[obligation["status"]] += 1
                by_contract[
                    f"{obligation['contract']}:{obligation['status']}"
                ] += 1
        evaluator_summaries[evaluator_id] = {
            "task_success": count_field(assessments, "task_success"),
            "static_conflict": count_field(assessments, "static_conflict"),
            "behavioral_conflict": count_field(
                assessments, "behavioral_conflict"
            ),
            "severity": count_field(assessments, "severity"),
            "precedence": count_field(assessments, "precedence"),
            "obligation_status": dict(sorted(obligations.items())),
            "obligation_status_by_contract": dict(sorted(by_contract.items())),
            "obligations_total": sum(obligations.values()),
        }

    return {
        "valid_runs": valid_runs,
        "invalid_runs": len(runs) - valid_runs,
        "transport_retries": sum(
            max(0, len(load_json(path)["transport_attempts"]) - 1)
            for path in runs
        ),
        "task_success_consensus": {
            status: task_success.get(status, 0)
            for status in ("yes", "partial", "no")
        },
        "task_success_by_arm": consensus_by_arm,
        "combined_better_than_both_singles": combined_better,
        "evaluator_agreement": agreement,
        "evaluator_summaries": evaluator_summaries,
        "combined_skill_reads": combined_skill_reads(),
        "run_metrics": run_metrics,
        "within_case_overhead": overhead,
        "condition_totals": totals,
        "token_comparison_boundary": (
            "Only FSI-001 Codex CLI turn.completed fields are compared; "
            "older evaluation counters are excluded."
        ),
    }


def main() -> None:
    destination = ARCHIVE / "calculations.json"
    destination.write_text(
        json.dumps(compile_results(), indent=2, sort_keys=True) + "\n"
    )
    obligations = ARCHIVE / "evaluation" / "obligations.jsonl"
    obligations.write_text(
        "".join(
            json.dumps(record, sort_keys=True) + "\n"
            for record in compile_obligations()
        )
    )
    for key, record in compile_derived_run_evidence().items():
        case_id, condition = key.split("/", 1)
        destination = (
            ARCHIVE / "runs" / case_id / condition / "derived-evidence.json"
        )
        destination.write_text(
            json.dumps(record, indent=2, sort_keys=True) + "\n"
        )
    (ARCHIVE / "SHA256SUMS").write_text("\n".join(checksum_lines()) + "\n")


if __name__ == "__main__":
    main()
