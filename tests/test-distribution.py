#!/usr/bin/env python3
"""Regression tests for the cross-host distribution validator."""

from pathlib import Path
import json
import shutil
import subprocess
import tempfile


ROOT = Path(__file__).resolve().parents[1]


def run_validator(root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["python3", str(root / "scripts" / "validate-distribution.py")],
        cwd=root,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def main() -> None:
    clean = run_validator(ROOT)
    if clean.returncode:
        raise SystemExit(clean.stdout)

    with tempfile.TemporaryDirectory() as temporary:
        copied = Path(temporary) / "repo"
        shutil.copytree(ROOT, copied, ignore=shutil.ignore_patterns(".git"))
        canonical_skill = (ROOT / "skills" / "fructal" / "SKILL.md").read_bytes()

        mirror = (
            copied
            / "distribution"
            / "plugins"
            / "fructal"
            / "skills"
            / "fructal"
            / "SKILL.md"
        )
        mirror.write_text(mirror.read_text() + "\n# deliberate drift\n")
        drift = run_validator(copied)
        if drift.returncode == 0 or "not byte-identical" not in drift.stdout:
            raise SystemExit("validator did not reject a drifted skill mirror")

        mirror.write_bytes(canonical_skill)
        cases_path = copied / "distribution" / "submission-test-cases.json"
        original_cases = cases_path.read_text()
        for references, expected_error in (
            (["nonexistent-case"], "unknown contract case"),
            ([], "requires nonempty contract_case_ids"),
            ("implicit_review", "requires nonempty contract_case_ids"),
            ([{}], "requires nonempty contract_case_ids"),
        ):
            cases = json.loads(original_cases)
            cases["positive"][0]["contract_case_ids"] = references
            cases_path.write_text(json.dumps(cases, indent=2) + "\n")
            invalid_reference = run_validator(copied)
            if invalid_reference.returncode == 0 or expected_error not in invalid_reference.stdout:
                raise SystemExit("validator did not reject invalid contract-case references")

        cases = json.loads(original_cases)
        cases["version"] = "0.0.0"
        cases_path.write_text(json.dumps(cases, indent=2) + "\n")
        stale_version = run_validator(copied)
        if stale_version.returncode == 0 or "version must be" not in stale_version.stdout:
            raise SystemExit("validator did not reject stale submission-case version")

        cases = json.loads(original_cases)
        cases["negative"] = cases["negative"][:2]
        cases_path.write_text(json.dumps(cases, indent=2) + "\n")
        incomplete = run_validator(copied)
        if incomplete.returncode == 0 or "at least three negative" not in incomplete.stdout:
            raise SystemExit("validator did not reject an incomplete negative case set")
        cases_path.write_text(original_cases)

        duplicate = copied / "plugins" / "fructal" / "skills" / "fructal" / "SKILL.md"
        duplicate.parent.mkdir(parents=True)
        duplicate.write_bytes(canonical_skill)
        doubled = run_validator(copied)
        if doubled.returncode == 0 or "GitHub skill discovery" not in doubled.stdout:
            raise SystemExit("validator did not reject a duplicate GitHub skill entry")

    print(
        "PASS: distribution validator rejects drift, invalid case references, "
        "stale versions, incomplete cases, "
        "and duplicate GitHub skill entries"
    )


if __name__ == "__main__":
    main()
