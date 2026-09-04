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

        mirror = copied / "plugins" / "fructal" / "skills" / "fructal" / "SKILL.md"
        mirror.write_text(mirror.read_text() + "\n# deliberate drift\n")
        drift = run_validator(copied)
        if drift.returncode == 0 or "not byte-identical" not in drift.stdout:
            raise SystemExit("validator did not reject a drifted skill mirror")

        mirror.write_bytes(canonical_skill)
        cases_path = copied / "distribution" / "submission-test-cases.json"
        cases = json.loads(cases_path.read_text())
        cases["negative"] = cases["negative"][:2]
        cases_path.write_text(json.dumps(cases, indent=2) + "\n")
        incomplete = run_validator(copied)
        if incomplete.returncode == 0 or "at least three negative" not in incomplete.stdout:
            raise SystemExit("validator did not reject an incomplete negative case set")

    print("PASS: distribution validator rejects drift and incomplete case sets")


if __name__ == "__main__":
    main()
