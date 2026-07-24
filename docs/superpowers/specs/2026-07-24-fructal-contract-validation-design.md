# Fructal Contract and Evaluation Design

## Purpose

Resolve the six findings from the 2026-07-24 Review of Fructal Cap Design:

1. validation does not exercise Review, Redesign, Implement, or mixed-mode
   behavior;
2. an explicit named mode can conflict with outcome-based routing;
3. Review and Redesign can deadlock when real inspection has incidental
   read-side effects;
4. `provided` and `reported` overlap when supplied material contains an
   attributed claim;
5. an installed skill cannot identify its source version and repository
   validation cannot detect drift by itself;
6. “through a form every affected actor can perceive” is ambiguous for devices,
   services, and software actors.

The result must retain the current broad workflow-engineering scope, the three
exclusive modes, the Review no-solution boundary, the Redesign no-modification
boundary, Implement persistence, consequential-action safeguards, accessibility,
and the restored Fructal-cap test.

## Contract changes

### Mode precedence

The skill will distinguish an explicit mode instruction from a mode word that
only describes the subject.

- “Use Review mode” is a binding maximum outcome. A conflicting request to
  modify the system remains Review, and the report identifies the prohibited
  outcome without offering a replacement motion.
- “Use Redesign mode” permits a replacement motion but never target-system
  modification.
- “Use Implement mode” permits ordinary in-scope modification unless a stricter
  explicit boundary prohibits it.
- A no-modification boundary always overrides Implement. It selects Redesign
  when a replacement motion is requested and Review otherwise.
- In the absence of an explicit mode instruction, the requested outcome selects
  the highest authorized mode.
- Subject wording such as “review our implementation” does not explicitly select
  Implement.

This makes the named mode an intentional requester boundary without allowing a
mere noun or verb to route the task.

### Diagnostic boundary

Review and Redesign will prohibit changes to workflow or business state,
permissions, content, actor-visible outcomes, and consequential external state.
They may perform read-only inspection whose only unavoidable effects are
ordinary access metadata such as logs, request counters, or last-access
timestamps, when that inspection is already authorized and is not itself
costly, sensitive, rate-limited, or operationally consequential.

Unknown or material side effects remain unavailable evidence rather than
silently authorized inspection. Disposable isolated diagnostics remain allowed
and must be cleaned up. A stricter requester boundary such as “no external
requests” or “no writes of any kind” still wins.

### Evidence dimensions

Evidence provenance and evidentiary status become separate dimensions:

- `provided`: material or a task fact supplied directly by the requester;
- `reported`: a claim attributed to another actor or source that has not been
  independently verified;
- `observed`: evidence directly inspected or measured in the task;
- `inference`: a conclusion derived from provided, reported, or observed
  evidence;
- `open question`: an unresolved material gap.

A supplied support document can therefore be a `provided artifact` containing a
`reported claim`. Directly reading the document is observed evidence that the
document contains the claim, not that the claim is true.

### Actor-appropriate feedback

The redesign rule will require immediate feedback through a channel each
affected actor can perceive or observe. Human actors require accessible sensory
or assistive-technology feedback where applicable; services, devices, and
software components require inspectable state, events, responses, or telemetry.
No literal form or UI is implied.

## Package provenance and synchronization

`SKILL.md` frontmatter will carry:

- semantic package version `1.0.0`;
- canonical source URL
  `https://github.com/PaolaShultz/shr-skills/tree/main/skills/fructal`.

The same metadata must appear in the embedded ChatGPT demo and installed copy.
The repository validator will accept an optional installed-skill directory and
compare both `SKILL.md` and `agents/openai.yaml` byte-for-byte with the source.
Source-only validation remains portable; release verification supplies the
installed path explicitly.

The package version identifies skill behavior without embedding a Git commit
that cannot be known until after the commit is created. Git history remains the
exact source-history authority for a given version.

## Deterministic validation

The current shell validator will remain the public entry point. Its checks will
be divided by responsibility:

1. structural validation parses `SKILL.md` frontmatter and
   `agents/openai.yaml`, validates required schema and package metadata, and
   rejects malformed YAML;
2. contract validation checks the canonical routing table and required
   safeguards;
3. documentation validation checks README mode examples and package identity;
4. demo validation confirms that the embedded skill is exactly synchronized,
   allowing only blank-line formatting differences already used for readable
   Markdown;
5. optional install validation compares the active copy with the canonical
   source;
6. regression tests exercise validators against deliberately broken disposable
   package copies and prove each relevant failure is detected.

Contract fixtures will cover:

- implicit Review, Redesign, and Implement outcomes;
- explicit Review, Redesign, and Implement instructions;
- explicit mode versus conflicting higher outcome;
- no-modification caps;
- subject words that must not route the mode;
- a consequential Implement action that still requires exact confirmation;
- a mid-task mode or boundary change;
- the two-dimensional evidence-label example;
- permitted incidental read metadata and prohibited material read-side effects.

The deterministic suite is the commit gate because it is repeatable and does not
depend on network or model variance.

## Live model evaluations

A separate evaluation command will invoke the locally installed Codex CLI with
the canonical skill embedded in each prompt. It will use ephemeral sessions,
ignore user configuration and repository rules that could alter the evaluated
contract, request structured JSON output, and operate only on isolated fixtures.
The command accepts an explicit model override and always reports the model used.

Review and Redesign cases run with a read-only sandbox. Implement cases run with
workspace-write access only inside a disposable fixture repository so the model
must make and verify a harmless change. No evaluation receives target-system
credentials, production paths, deployment authority, or permission for external
effects; Codex authentication is used only to run the requested model.

Each response schema records:

- selected mode;
- whether modification was attempted;
- whether a replacement motion was proposed;
- whether confirmation was requested;
- evidence labels used;
- completion or stop reason.

The evaluator checks deterministic properties of that structured response and,
for Implement, the disposable fixture diff and verification marker. Raw
transcripts and generated fixture state stay outside the repository and are
deleted after a successful run; concise pass/fail output remains available to
the operator.

Live evaluations are a required release check but not the only commit gate. A
model failure is reported distinctly from validator, authentication, transport,
schema, or fixture failures. The harness does not weaken an expected contract to
make a nondeterministic run green.

## Failure behavior

- Structural or deterministic contract failures exit nonzero with the exact
  invariant and file or fixture that failed.
- Missing installed-copy input skips only installation comparison during
  source-only validation; release verification treats the installed path as
  required.
- Missing Codex CLI, authentication failure, unavailable model, invalid JSON, or
  an unmet live expectation exits nonzero and identifies the failure class.
- Temporary evaluation state is created in a uniquely named directory and
  cleaned up on success or interruption. A failed run prints the retained
  diagnostic directory only when retaining it is explicitly requested.
- No validator or evaluator edits the canonical source or active installed
  package.

## Verification

Implementation follows test-first red-green cycles:

1. add failing regression cases for the six findings and observe the expected
   failures against the current validator and skill;
2. implement the smallest contract and validator changes that make those cases
   pass;
3. run source validation, malformed-package regression tests, demo
   synchronization, installed-copy comparison, official skill validation,
   Markdown/diff checks, and the live evaluation matrix;
4. synchronize the installed copy only after source checks pass, rerun install
   comparison and live evaluations against the synchronized content, then
   review the complete diff.

Release evidence must name the deterministic commands, live cases and model,
observed results, package version, installed-copy comparison, commit, and pushed
remote branch.
