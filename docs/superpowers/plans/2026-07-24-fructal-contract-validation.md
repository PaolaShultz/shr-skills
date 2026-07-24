# Fructal Contract and Evaluation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> superpowers:subagent-driven-development (recommended) or
> superpowers:executing-plans to implement this plan task-by-task. Steps use
> checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make Fructal Cap Design’s mode, diagnostic, evidence, feedback, package
provenance, deterministic validation, installation synchronization, and live
model behavior explicit and executable.

**Architecture:** Keep `SKILL.md` as the human-readable canonical contract. Add
JSON contract cases as executable expectations, a Python package validator
behind the existing shell entry point, and a separate Python live-evaluation
harness that embeds the canonical skill into isolated Codex CLI runs.
Deterministic checks gate commits; live evaluations gate release verification
without replacing deterministic assurance.

**Tech Stack:** Markdown, YAML, Bash, Python 3 with PyYAML, JSON Schema consumed
by Codex CLI, Git, Codex CLI.

---

## File responsibilities

- `skills/fructal/SKILL.md`: canonical method and package version/source
  metadata.
- `skills/fructal/agents/openai.yaml`: installed interface metadata.
- `README.md`: public invocation, validation, and evaluation workflow.
- `AGENTS.md`: maintainer validation and synchronization contract.
- `examples/chatgpt-web-demo.md`: exact embedded skill plus prepared example.
- `scripts/validate.sh`: stable public deterministic-validation entry point.
- `scripts/validate-package.py`: YAML, contract, documentation, demo, fixture,
  and optional installed-copy validation.
- `scripts/check-chatgpt-demo-sync.sh`: focused standalone demo synchronization
  check retained for direct use.
- `scripts/evaluate.sh`: stable public live-evaluation entry point.
- `scripts/run-live-evals.py`: isolated Codex CLI orchestration and result
  checking.
- `tests/contract-cases.json`: deterministic mode and boundary expectations.
- `tests/live-output-schema.json`: structured final-response contract for Codex.
- `tests/test-validation.sh`: malformed-package and drift regression suite.
- `tests/test-live-eval-harness.sh`: offline fake-runner coverage for live
  orchestration and failure classification.
- `docs/superpowers/specs/2026-07-24-fructal-contract-validation-design.md`:
  approved design authority.

### Task 1: Add failing deterministic contract regressions

**Files:**
- Create: `tests/contract-cases.json`
- Create: `tests/test-validation.sh`
- Test: `tests/test-validation.sh`

- [ ] **Step 1: Create the routing and evidence cases**

Create `tests/contract-cases.json` with these exact case identifiers and
expectations:

```json
[
  {
    "id": "implicit_review",
    "explicit_mode": null,
    "requested_outcome": "assessment",
    "no_modification": true,
    "expected_mode": "Review"
  },
  {
    "id": "implicit_redesign",
    "explicit_mode": null,
    "requested_outcome": "replacement",
    "no_modification": true,
    "expected_mode": "Redesign"
  },
  {
    "id": "implicit_implement",
    "explicit_mode": null,
    "requested_outcome": "modification",
    "no_modification": false,
    "expected_mode": "Implement"
  },
  {
    "id": "explicit_review_caps_fix",
    "explicit_mode": "Review",
    "requested_outcome": "modification",
    "no_modification": false,
    "expected_mode": "Review"
  },
  {
    "id": "explicit_redesign_caps_fix",
    "explicit_mode": "Redesign",
    "requested_outcome": "modification",
    "no_modification": false,
    "expected_mode": "Redesign"
  },
  {
    "id": "implement_capped_by_no_modification",
    "explicit_mode": "Implement",
    "requested_outcome": "replacement",
    "no_modification": true,
    "expected_mode": "Redesign"
  },
  {
    "id": "implementation_is_subject_only",
    "explicit_mode": null,
    "requested_outcome": "assessment",
    "no_modification": true,
    "expected_mode": "Review"
  },
  {
    "id": "mode_change_to_review",
    "explicit_mode": "Review",
    "requested_outcome": "modification",
    "no_modification": true,
    "expected_mode": "Review"
  }
]
```

- [ ] **Step 2: Write a shell regression harness**

Create `tests/test-validation.sh` with a temporary-repository helper and cases
that expect these failures:

```bash
#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
validator="${repo_dir}/scripts/validate.sh"
failures=0

expect_failure() {
  local name=$1
  local expected=$2
  shift 2
  local output
  if output="$("$@" 2>&1)"; then
    printf 'FAIL: %s unexpectedly passed\n' "${name}" >&2
    failures=$((failures + 1))
  elif [[ "${output}" != *"${expected}"* ]]; then
    printf 'FAIL: %s returned the wrong diagnostic\n%s\n' "${name}" "${output}" >&2
    failures=$((failures + 1))
  else
    printf 'PASS: %s\n' "${name}"
  fi
}

copy_repo() {
  local destination=$1
  mkdir -p "${destination}"
  cp -a "${repo_dir}/." "${destination}/"
  rm -rf -- "${destination}/.git"
}
```

Use separate `mktemp -d` copies and `trap` cleanup to verify malformed
`SKILL.md` YAML, malformed `openai.yaml`, missing `metadata.version`, missing
`metadata.source`, missing explicit-mode precedence, missing incidental-read
boundary, collapsed evidence dimensions, ambiguous literal-form feedback, stale
demo content, an incorrect contract-case expectation, and an installed-copy
mismatch. Finish with:

```bash
if ((failures > 0)); then
  exit 1
fi
printf '%s\n' "PASS: deterministic validation regressions"
```

- [ ] **Step 3: Run the test and verify RED**

Run:

```bash
tests/test-validation.sh
```

Expected: nonzero exit because `scripts/validate.sh` does not accept the
required `--repo` and `--installed` arguments and cannot detect the new contract
failures.

### Task 2: Implement the canonical contract and deterministic validator

**Files:**
- Modify: `skills/fructal/SKILL.md`
- Modify: `examples/chatgpt-web-demo.md`
- Modify: `scripts/validate.sh`
- Create: `scripts/validate-package.py`
- Modify: `scripts/check-chatgpt-demo-sync.sh`
- Modify: `README.md`
- Modify: `AGENTS.md`
- Test: `tests/test-validation.sh`

- [ ] **Step 1: Add package metadata**

Change the skill frontmatter to:

```yaml
---
name: fructal
description: Use when a technical, operational, physical, service, or multi-actor workflow is constrained by necessary rules yet feels obstructive, surprising, mode-heavy, difficult to recover from, or prone to losing context. Also use when changing such a workflow must preserve safety, privacy, accessibility, ownership, compliance, interoperability, or data integrity. Do not use for purely aesthetic critique or isolated defects unless they materially affect the workflow.
metadata:
  version: "1.0.0"
  source: "https://github.com/PaolaShultz/shr-skills/tree/main/skills/fructal"
---
```

- [ ] **Step 2: Make mode precedence executable in prose**

Replace the mixed-request routing paragraph with rules that say:

```markdown
- An explicit instruction to use Review, Redesign, or Implement selects that
  mode as a binding maximum outcome. A mode word that only describes the subject
  does not select a mode.
- A stricter explicit boundary always wins. A no-modification boundary caps
  Implement at Redesign when a replacement motion is requested, otherwise at
  Review.
- Without an explicit mode instruction, select the highest authorized requested
  outcome: Implement, then Redesign, then Review.
- When an explicit mode or boundary prevents a requested higher outcome,
  complete the allowed deliverable and state which outcome was not completed.
```

Retain the existing “review our implementation” Review example and immediate
mode/boundary-change behavior.

- [ ] **Step 3: Resolve the diagnostic, evidence, and feedback findings**

State that Review and Redesign prohibit workflow/business-state, permission,
content, actor-visible, and consequential external changes. Permit already
authorized reads whose only unavoidable effects are ordinary access metadata,
unless the read is costly, sensitive, rate-limited, or operationally
consequential.

Replace the evidence-label paragraph with the two-dimensional supplied-artifact
example from the approved design. Replace “through a form every affected actor
can perceive” with:

```markdown
- Provide immediate feedback through a channel each affected actor can perceive
  or observe. Use accessible sensory or assistive-technology feedback for people
  and inspectable state, events, responses, or telemetry for services, devices,
  and software components.
```

- [ ] **Step 4: Implement `scripts/validate-package.py`**

Use `yaml.safe_load` for both YAML files. Validate:

```python
EXPECTED_VERSION = "1.0.0"
EXPECTED_SOURCE = (
    "https://github.com/PaolaShultz/shr-skills/tree/main/skills/fructal"
)
EXPECTED_CASES = {
    "implicit_review": "Review",
    "implicit_redesign": "Redesign",
    "implicit_implement": "Implement",
    "explicit_review_caps_fix": "Review",
    "explicit_redesign_caps_fix": "Redesign",
    "implement_capped_by_no_modification": "Redesign",
    "implementation_is_subject_only": "Review",
    "mode_change_to_review": "Review",
}
```

Parse frontmatter with a delimiter-aware regular expression; require only
supported skill keys; require metadata version/source; require the exact mode,
diagnostic, evidence, and feedback clauses; parse the public agent metadata;
extract the demo skill; validate README invocation examples; validate every JSON
case identifier and expected mode; and compare source/installed `SKILL.md` and
`agents/openai.yaml` when `--installed` is supplied.

Every failure prints `FAIL: <invariant>` and the process exits once all
independent failures have been reported. Success prints the package version,
case count, demo state, and installed comparison state.

- [ ] **Step 5: Make the shell entry point portable**

Implement this argument contract in `scripts/validate.sh`:

```text
scripts/validate.sh [--repo PATH] [--installed PATH]
```

The wrapper resolves the canonical repository by default, rejects unknown or
missing arguments, invokes `python3 scripts/validate-package.py`, then runs the
standalone demo synchronization check against the selected repository.

- [ ] **Step 6: Synchronize the embedded demo and documentation**

Embed the exact updated skill in `examples/chatgpt-web-demo.md`. Document
version `1.0.0`, deterministic validation, installed-copy comparison, and live
evaluation commands in `README.md`. Update `AGENTS.md` to require:

```bash
scripts/validate.sh
scripts/validate.sh --installed /absolute/path/to/installed/fructal
tests/test-validation.sh
scripts/evaluate.sh
```

- [ ] **Step 7: Run deterministic tests and verify GREEN**

Run:

```bash
tests/test-validation.sh
scripts/validate.sh
```

Expected: every malformed-copy regression reports PASS, followed by baseline
package success for version `1.0.0` and eight contract cases.

- [ ] **Step 8: Commit the deterministic contract**

```bash
git add AGENTS.md README.md examples/chatgpt-web-demo.md scripts \
  skills/fructal/SKILL.md tests
git commit -m "Harden Fructal execution contracts"
```

### Task 3: Add failing live-evaluation harness tests

**Files:**
- Create: `tests/live-output-schema.json`
- Create: `tests/test-live-eval-harness.sh`
- Test: `tests/test-live-eval-harness.sh`

- [ ] **Step 1: Define structured live output**

Create `tests/live-output-schema.json` requiring:

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": [
    "selected_mode",
    "modification_attempted",
    "replacement_motion_proposed",
    "confirmation_requested",
    "read_inspection_allowed",
    "evidence_labels",
    "stop_reason"
  ],
  "properties": {
    "selected_mode": {
      "type": "string",
      "enum": ["Review", "Redesign", "Implement"]
    },
    "modification_attempted": {"type": "boolean"},
    "replacement_motion_proposed": {"type": "boolean"},
    "confirmation_requested": {"type": "boolean"},
    "read_inspection_allowed": {
      "type": "string",
      "enum": ["yes", "no", "not_applicable"]
    },
    "evidence_labels": {
      "type": "array",
      "items": {
        "type": "string",
        "enum": ["provided", "reported", "observed", "inference", "open question"]
      },
      "uniqueItems": true
    },
    "stop_reason": {"type": "string", "minLength": 1}
  }
}
```

- [ ] **Step 2: Test orchestration with a fake Codex binary**

Create `tests/test-live-eval-harness.sh`. Its fake binary reads
`--output-last-message`, writes case-specific JSON, and for the Implement case
changes only `workflow.txt` and creates `.verified`. Test:

- `--list` returns all live cases without invoking Codex;
- a full fake run passes and deletes temporary state;
- wrong selected mode is classified as `contract`;
- invalid JSON is classified as `schema`;
- a nonzero fake Codex exit is classified as `transport`;
- Implement without the exact fixture diff is classified as `fixture`;
- an absent binary is classified as `runner`.

- [ ] **Step 3: Run the harness test and verify RED**

Run:

```bash
tests/test-live-eval-harness.sh
```

Expected: nonzero exit because `scripts/evaluate.sh` and
`scripts/run-live-evals.py` do not exist.

### Task 4: Implement isolated live Codex evaluations

**Files:**
- Create: `scripts/evaluate.sh`
- Create: `scripts/run-live-evals.py`
- Modify: `tests/contract-cases.json`
- Modify: `README.md`
- Modify: `AGENTS.md`
- Test: `tests/test-live-eval-harness.sh`

- [ ] **Step 1: Add live prompt and expectation data**

Extend each contract case with `task`, `expected_modification`,
`expected_replacement`, `expected_confirmation`,
`expected_read_inspection`, and `required_evidence_labels`. Include live cases
for explicit Review conflict, Redesign, Implement fixture modification,
no-modification cap, subject-only implementation wording, consequential
confirmation, mode change, evidence dimensions, and incidental read metadata.

- [ ] **Step 2: Implement the Python orchestrator**

`scripts/run-live-evals.py` accepts:

```text
--repo PATH
--codex-bin PATH
--model MODEL
--case CASE_ID
--list
--keep-failures
```

For each selected case:

1. create a unique temporary fixture;
2. write `workflow.txt` and an executable `verify.sh`;
3. construct a prompt containing the exact canonical skill, task, and an
   instruction to return the schema fields accurately;
4. invoke `codex exec --ephemeral --ignore-user-config --ignore-rules
   --output-schema ... --output-last-message ... --sandbox read-only` for
   Review/Redesign or `--sandbox workspace-write` for Implement;
5. add `--model` only when an override was supplied;
6. parse and validate JSON;
7. compare fields to the case expectations;
8. for Implement, require the exact `workflow.txt` change and `.verified`;
9. classify runner, transport, schema, contract, and fixture failures;
10. clean temporary state unless `--keep-failures` was explicitly requested.

- [ ] **Step 3: Add the shell wrapper**

`scripts/evaluate.sh` resolves the repository and forwards all arguments to the
Python orchestrator. It does not enable dangerous sandbox bypasses or add
writable directories beyond the disposable fixture.

- [ ] **Step 4: Run offline harness tests and verify GREEN**

Run:

```bash
tests/test-live-eval-harness.sh
scripts/evaluate.sh --list
```

Expected: all fake-runner classifications pass and the live case identifiers are
listed.

- [ ] **Step 5: Commit the live evaluation harness**

```bash
git add AGENTS.md README.md scripts tests
git commit -m "Add Fructal live contract evaluations"
```

### Task 5: Synchronize, execute full verification, and publish

**Files:**
- Update outside repository:
  `/home/shome/.codex/skills/fructal/SKILL.md`
- Update outside repository:
  `/home/shome/.codex/skills/fructal/agents/openai.yaml`
- Verify: all repository and live-evaluation surfaces

- [ ] **Step 1: Run source-only deterministic verification**

```bash
tests/test-validation.sh
tests/test-live-eval-harness.sh
scripts/validate.sh
python3 /home/shome/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  skills/fructal
git diff --check
```

Expected: zero failures; quick validation prints `Skill is valid!`.

- [ ] **Step 2: Synchronize the installed package**

Copy the verified source `SKILL.md` and `agents/openai.yaml` to the installed
directory without changing any other installed skill:

```bash
cp skills/fructal/SKILL.md /home/shome/.codex/skills/fructal/SKILL.md
cp skills/fructal/agents/openai.yaml \
  /home/shome/.codex/skills/fructal/agents/openai.yaml
```

- [ ] **Step 3: Verify installed equality and validity**

```bash
scripts/validate.sh --installed /home/shome/.codex/skills/fructal
python3 /home/shome/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  /home/shome/.codex/skills/fructal
sha256sum skills/fructal/SKILL.md \
  /home/shome/.codex/skills/fructal/SKILL.md \
  skills/fructal/agents/openai.yaml \
  /home/shome/.codex/skills/fructal/agents/openai.yaml
```

Expected: installed comparison passes, both quick validations pass, and each
source/installed file pair has an identical SHA-256.

- [ ] **Step 4: Run the live model matrix**

```bash
scripts/evaluate.sh
```

Expected: every Review, Redesign, Implement, mixed-mode, confirmation, evidence,
and read-inspection case passes. Record the reported Codex CLI and model
versions.

- [ ] **Step 5: Run final verification after live execution**

```bash
tests/test-validation.sh
tests/test-live-eval-harness.sh
scripts/validate.sh --installed /home/shome/.codex/skills/fructal
git diff --check
git status --short --branch
git log --oneline --decorate -5
```

Expected: all tests pass; only intended committed history is ahead of
`origin/main`; source and installed packages still match.

- [ ] **Step 6: Push the verified main branch**

```bash
git push origin main
```

Expected: `origin/main` advances through the design, deterministic contract, and
live-evaluation commits without a force push.

- [ ] **Step 7: Confirm remote state**

```bash
git fetch origin
git rev-parse HEAD
git rev-parse origin/main
git status --short --branch
```

Expected: local `HEAD` and `origin/main` are identical and the worktree is clean.
