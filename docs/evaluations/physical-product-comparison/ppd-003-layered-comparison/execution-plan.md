# PPD-003 Layered Comparison Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> `superpowers:executing-plans` to implement this plan task-by-task. Do not use
> collaboration subagents; isolated Codex subprocesses are experimental arms
> and blind evaluators only.

**Goal:** Execute and publish the combined Fructal Cap Design plus Superpowers
arm and a two-evaluator layered attribution study without altering PPD-001 or
PPD-002 history.

**Architecture:** A prospectively frozen case owns immutable inputs, isolated
temporary execution/evaluator environments, sanitized trace-derived evidence,
sealed mappings, deterministic calculations, and a final public archive. The
combined arm receives the byte-identical PPD-002 prompt; evaluators receive
staged anonymous evidence so later-layer artifacts cannot influence earlier
scores.

**Tech Stack:** Git, Codex CLI 0.145.0, JSONL, gzip, jq, SHA-256, Markdown,
PNG, Bash, and Python standard-library calculation/validation helpers.

---

Execution is inline on the repository's explicit single-developer `main`
workflow. The required prospective commit and push precede every new arm
result.

### Task 1: Freeze and publish the prospective protocol

**Files:**

- Create: `docs/evaluations/physical-product-comparison/ppd-003-layered-comparison/protocol.md`
- Create: `docs/evaluations/physical-product-comparison/ppd-003-layered-comparison/execution-plan.md`
- Create: `docs/evaluations/physical-product-comparison/ppd-003-layered-comparison/frozen-inputs/shared-execution-prompt.md`

- [ ] Verify every source commit, tree, package export, file, and prompt hash
      recorded in `protocol.md`.
- [ ] Verify the PPD-003 prompt copy is byte-identical to
      `ppd-002-discovery/control/prompt.md`.
- [ ] Run `git diff --check`, `scripts/validate.sh`,
      `tests/test-validation.sh`, and `tests/test-live-eval-harness.sh`.
- [ ] Inspect the complete prospective diff and confirm it contains no result.
- [ ] Commit with an imperative prospective subject.
- [ ] Push `main` to verified `origin`.
- [ ] Verify the local prospective commit equals `origin/main`.

Expected outcome: the protocol is publicly timestamped before the combined
result exists.

### Task 2: Build and diagnose the combined execution boundary

**Temporary state outside repositories:**

- Create one experiment root with `mktemp -d`.
- Create isolated combined `HOME`, `CODEX_HOME`, and output workspace.
- Export the complete Fructal Cap Design package from `5efbd8a`.
- Export the complete Superpowers package from `6efe32c`.
- Copy authentication material only into the isolated `CODEX_HOME`; never
  print or archive it.

- [ ] Hash the installed exports and compare with `protocol.md`.
- [ ] Verify the task prompt SHA-256 is
      `33a15b008bc6c75c5ac963f7d05d7541204244f416726efb9e414f21264c1049`.
- [ ] Run a diagnostic Codex session with the exact combined home, Codex home,
      workspace, model, effort, sandbox, and config boundary.
- [ ] Inspect the diagnostic trace's actual available-skill payload.
- [ ] Require built-in system skills, `fructal`, all Superpowers skills, and no
      other non-system user skills.
- [ ] Preserve a sanitized readable diagnostic and diagnostic metadata.

Expected outcome: the observed model payload proves the combined skill
boundary before execution.

### Task 3: Execute and freeze the combined arm

**Files to archive:**

- `combined/prompt.md`
- `combined/raw-response.md`
- `combined/design-response.md`
- `combined/concept-board.png`
- `combined/metadata.md`
- `combined/available-skills.md`
- `combined/skill-invocation-sequence.md`
- `combined/image-instruction-chain.md`
- `combined/session.jsonl.gz`

- [ ] Launch Codex once with the exact prompt bytes on standard input.
- [ ] Make no harness intervention after launch.
- [ ] Preserve stdout JSONL, last response bytes, output workspace, token
      count, timestamps, and duration.
- [ ] Locate the single final image from tool events and the delivered response.
- [ ] Create a reading copy changing only the local image link.
- [ ] Sanitize the session JSONL by deleting provider-private and credential
      fields recursively.
- [ ] Parse the sanitized trace and extract skill-read order, image calls,
      image inspections, corrections, and completion checks.
- [ ] Record all output and provenance hashes.

Expected outcome: one immutable fourth-arm record with a reconstructable
delivery and QC chain.

### Task 4: Run the blind prompt-author comparison

**Files to archive:**

- `prompt-author-comparison/inputs/`
- `prompt-author-comparison/evaluator-prompt.md`
- `prompt-author-comparison/evaluator-1/`
- `prompt-author-comparison/evaluator-2/`
- `prompt-author-comparison/sealed-mapping.md`
- `prompt-author-comparison/reveal.md`
- `prompt-author-comparison/results.md`

- [ ] Generate a randomized two-label mapping outside both evaluator
      workspaces and record its pre-launch SHA-256.
- [ ] Create two byte-equivalent workspaces containing only the rough request,
      two anonymous prompts, rubric, and output schema.
- [ ] Diagnose `NONE` for non-system user skills under each isolated
      evaluator boundary.
- [ ] Launch both no-user-skill evaluators independently with browsing and
      repository inspection prohibited.
- [ ] Freeze both raw structured outputs and sanitized traces.
- [ ] Validate ten integer scores per candidate, totals, required analysis
      fields, and confidence.
- [ ] Archive the sealed mapping and reveal only after both outputs validate.
- [ ] Calculate means, disagreements, totals, and the prompt-profile similarity.

Expected outcome: prompt authorship is evaluated independently from every
execution result.

### Task 5: Extract all four image-instruction chains

**Files to archive:**

- `image-instructions/control.md`
- `image-instructions/superpowers.md`
- `image-instructions/treatment.md`
- `image-instructions/combined.md`
- `image-instructions/provenance.md`

- [ ] Parse the four sanitized execution traces.
- [ ] Extract exact image call arguments without reconstructing prose.
- [ ] Retain call order, ID, timestamp, initial/correction role, referenced
      image relationship, saved-path event, final image hash, and trace hash.
- [ ] Confirm the Superpowers chain contains both initial and correction calls.
- [ ] Compare extracted prompt bytes with the trace payload bytes.

Expected outcome: every image instruction is verbatim and provenance-linked.

### Task 6: Run two staged blind layered evaluators

**Files to archive:**

- `layered-evaluation/anonymous-inputs/`
- `layered-evaluation/evaluator-prompts/`
- `layered-evaluation/evaluator-1/`
- `layered-evaluation/evaluator-2/`
- `layered-evaluation/sealed-mapping.md`
- `layered-evaluation/reveal.md`

- [ ] Generate a new randomized four-label mapping outside evaluator
      workspaces and record its pre-launch SHA-256.
- [ ] Build byte-equivalent staged workspaces for both evaluators.
- [ ] Diagnose `NONE` for non-system user skills under both isolated
      evaluator boundaries.
- [ ] Run Layer 1 with written designs only.
- [ ] Run Layer 2 with written designs and image instructions only.
- [ ] Run Layer 3 with written designs, instructions, and images.
- [ ] Run Layer 4 with trace-derived delivery evidence and complete artifact
      linkage.
- [ ] Run Layer 5 with complete packages and the original frozen rubric.
- [ ] Verify Layer 3 and Layer 5 traces show direct inspection of all four
      images.
- [ ] Validate all structured results and freeze them before reveal.
- [ ] Archive the sealed mapping and reveal.

Expected outcome: two independent evaluations preserve layer boundaries and
raw disagreement.

### Task 7: Calculate and interpret results

**Files to archive:**

- `calculations/raw-scores.json`
- `calculations/similarities.csv`
- `calculations/results.md`
- `interpretation.md`

- [ ] Calculate evaluator-specific and mean scores for Layers 1, 2, 3, and 5.
- [ ] Report Layer 4 delivery/QC facts without inventing a numeric vector.
- [ ] Count every Layer 3 origin-label assignment by evaluator and mean/total.
- [ ] Compute all six arm-pair rubric-profile similarities for each numeric
      layer and evaluator, plus means.
- [ ] Recompute every table independently from the raw structured output.
- [ ] Interpret the combined condition only after reveal.
- [ ] Rank material findings by consequence, evaluator agreement, and recovery
      cost.
- [ ] Preserve the one-run, stochastic-renderer, model-evaluator, and physical
      acceptance limits.

Expected outcome: the public summary separates artifact quality from origin
attribution and avoids a one-score winner claim.

### Task 8: Complete publication, verification, and remote confirmation

**Files:**

- Create: `docs/evaluations/physical-product-comparison/ppd-003-layered-comparison/README.md`
- Create: `docs/evaluations/physical-product-comparison/ppd-003-layered-comparison/SHA256SUMS`
- Modify: `README.md`
- Modify: `docs/physical-product-comparison-protocol.md`
- Modify: `docs/real-world-usage-and-testing.md`
- Modify: `docs/workflow-postmortem-2026-07-24.md`
- Create an amendment/result boundary only if new evidence requires it.

- [ ] Verify all frozen source, prompt, package, image, trace, and mapping
      hashes.
- [ ] Verify `SHA256SUMS` covers every case file except itself and validates.
- [ ] Parse every sanitized JSONL trace.
- [ ] Verify every local Markdown link and image target.
- [ ] Scan for credentials, tokens, device codes, private-project paths or
      identities, and provider-private fields.
- [ ] Verify PPD-001 and PPD-002 tracked files are byte-unchanged.
- [ ] Run `git diff --check`.
- [ ] Run `scripts/validate.sh`.
- [ ] Run `tests/test-validation.sh`.
- [ ] Run `tests/test-live-eval-harness.sh`.
- [ ] Inspect the complete diff and repository status.
- [ ] Commit the completed archive and documentation with an imperative subject.
- [ ] Push `main` to verified `origin`.
- [ ] Verify local `HEAD`, local `origin/main`, and remote
      `refs/heads/main` are identical.
- [ ] Destroy the temporary experiment root only after every required public
      artifact and hash is verified.

Expected outcome: the full case is independently reconstructable without
publishing authentication or provider-private content.
