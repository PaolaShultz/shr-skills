# Fructal Cap Design 1.1.1 behavioral evaluation revision

Status: implemented and release-validated on 2026-09-04.

## Purpose

Version 1.1.0 improved activation and proportionality, but its live matrix
asked the executor to return its own structured compliance labels. Except for
one small Implement fixture, a run could therefore claim that it proposed a
replacement, stayed within Review, or satisfied a workflow concern without
producing an independently judged deliverable.

The same matrix embedded the complete skill in every prompt. That tested
behavior after injection, not whether the installed skill description caused
appropriate automatic discovery. Successful outputs were discarded, mode
changes were described inside one prompt rather than exercised across turns,
and one run per case could not characterize stochastic reliability.

## Contract corrections

The portable skill receives two narrow clarifications:

- explicit `$fructal` invocation does not bypass the workflow-level
  activation gate;
- Review recommendations become Redesign when they collectively define the
  workflow's complete sequence, state model, or ownership structure.

The README mode-visibility wording is aligned with the canonical rule: when the
requester explicitly names a mode, start the final report by stating it once;
otherwise do not expose the internal mode.
The visibility exception is deliberately literal: `Review mode`, `Redesign
mode`, and `Implement mode` qualify, while an action verb such as `review our
implementation` and an outcome that merely implies a mode do not.
Automatically discovered use stays silent unless the requester asks about the
method or attribution materially assists the task. An Implement response that
must stop for missing consequential authorization asks once for the exact
missing items and confirmation, identifies preserved state, and does not invent
a future workflow.

## Behavioral evaluator

Each ordinary contract case now has two isolated model phases:

1. The executor receives the skill and task, produces a natural user-facing
   response, and may act only in a disposable fixture.
2. A separate evaluator receives the canonical contract, user conversation,
   executor response, readable event evidence, and fixture before/after state.
   It judges the actual deliverable rather than accepting executor-authored
   compliance labels.

Deterministic fixture checks remain authoritative for writes, verification
markers, exact simulated consequential actions, untouched state, and prohibited
sensitive reads. Evaluator JSON covers semantic boundaries that deterministic
state cannot establish: replacement versus localized advice, proportionality,
mode-label visibility, cap-test quality, unsupported validation claims, and
unnecessary ceremony.

Each case asserts only the semantic dimensions central to that scenario. The
matrix does not require every correct evidence category in every case; that
would conflate independent behaviors and turn reasonable evaluator variation
into contract failure. Dedicated evidence cases retain strict provenance
assertions.

The evaluator uses a fresh isolated context. By default it uses the same model
family as the executor, so it reduces direct self-reporting but is not a
substitute for independent human or cross-model judgment.

## Added adversarial coverage

The matrix expands from 20 to 24 cases:

- an exactly authorized simulated deletion and notification must proceed
  without duplicate confirmation and must produce exact fixture evidence;
- a paid, rate-limited, unauthorized read must remain unread and become an
  explicit evidence gap;
- a natural multi-turn session changes from Implement to Review before
  modification, and the later boundary must govern the final result;
- an implicitly discovered installed skill must be read for an unlabelled
  multi-actor refund obstruction;
- the installed skill must not be read for a natural isolated helper defect.

Existing Redesign and Implement cases now permit semantic cap-test assertions.
Implicit cases test that the final response does not expose an internal mode
label. Review recommendation cases test the new aggregate boundary.

## Evidence preservation and repetition

The live runner accepts:

- `--repetitions N` for repeated independent executions;
- `--archive-dir PATH` for responses, executor and evaluator event streams,
  stderr, fixture snapshots, evaluations, per-run metadata, root metadata, and
  a generated SHA-256 manifest;
- `--skill-git-ref REVISION` for historical skill comparison.

An archive path must be empty, preventing accidental replacement of a prior
evidence set. Failed contract judgments are preserved when an archive is
requested; temporary authentication and isolated runtime state remain outside
the archive and are deleted with the run root.

## Observed evaluation results

The final candidate passed the complete 24-case matrix once and seven selected
high-risk cases three times each: 45 successful behavioral runs with zero
failures. Both archives were produced with `gpt-5.6-sol` through Codex CLI
0.153.2 and have generated SHA-256 manifests:

- [complete release matrix](evaluations/live-contract/fructal-1.1.1/)
- [three-repetition critical suite](evaluations/live-contract/fructal-1.1.1-critical-repetitions/)

The development archives are intentionally retained. Their failed judgments
exposed and drove corrections for aggregate Review recommendations, explicit
versus implied mode-label visibility, incomplete consequential authorization,
silent automatic discovery, scenario fixtures that lacked the artifact being
reviewed, an evidence case that did not pass the activation gate, and evaluator
definitions that conflated continuation gates or fixture verification with
consequential confirmation or unsupported real-world validation. They also
show the evaluator's stochastic classification variability and why one green
run is not enough evidence.

## Remaining limits

- Synthetic fixtures cannot establish affected-actor, production, physical,
  legal, safety, or professional accessibility acceptance.
- Two discovery cases are a guardrail, not a general precision/recall estimate.
- A same-model independent evaluator can share systematic biases with the
  executor.
- The 45 green runs are a development acceptance sample, not a statistical
  reliability claim; retained earlier failures demonstrate prompt and
  evaluator sensitivity.
- Repetition measures observed variability for the selected model and prompts;
  it does not establish a timeless success rate.
- Comparative value still requires a prospectively frozen no-skill or
  alternative-method arm and blinded assessment.
