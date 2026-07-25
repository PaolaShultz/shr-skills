# FSI-001 prospective protocol

Status: **frozen before any prospective arm result was inspected**

Date: 2026-07-25

## Research boundary

This experiment measures interaction, duplication, conflict, precedence,
suppression, failure, and recovery when Fructal Cap Design and Superpowers are
available separately or together. It does not rank a universal winner, repeat
the SHR-DAW enclosure experiment, generate images, access a network service, or
modify any previous evaluation artifact.

The owning repository is `/home/shome/p/shr-skills`. All new material is under
this archive. The existing tracked tree was clean at design start.

One run per case and condition is the behavioral sample. An unfavorable result
must not be rerun. A transport failure before any model result may be retried
once and both attempts must be retained. No causal or ecosystem-wide claim may
be made from this sample.

## Frozen execution state

[`frozen-inputs/environment.json`](frozen-inputs/environment.json) records the
pre-protocol repository commit and tree, current canonical Fructal Cap Design
package tree, exact local Superpowers commit and tree, Codex CLI version,
model, reasoning effort, sandbox, approval policy, collaboration mode, and
timezone.

The complete exports are:

- [`frozen-inputs/fructal-package.tar.gz`](frozen-inputs/fructal-package.tar.gz)
- [`frozen-inputs/superpowers-package.tar.gz`](frozen-inputs/superpowers-package.tar.gz)

Their archive hashes and the relevant `SKILL.md` hashes are frozen in
[`frozen-inputs/source-hashes.json`](frozen-inputs/source-hashes.json).
Retrospective source copies were exported from the exact commits used in
PPD-002/003. The prior and current Fructal Cap Design `SKILL.md` hashes are
compared explicitly; identical bytes do not erase their distinct provenance.

Execution settings are:

- Codex CLI `0.145.0`;
- model `gpt-5.6-sol`;
- reasoning effort `high`;
- sandbox `workspace-write` with restricted shell network;
- approval policy `never`;
- no web-search opt-in;
- default collaboration with subagents unavailable unless explicitly
  requested; and
- no harness intervention after a valid arm starts.

## Isolation diagnostic

Every run gets a fresh temporary root containing distinct `HOME`,
`CODEX_HOME`, `TMPDIR`, `XDG_CONFIG_HOME`, and `XDG_CACHE_HOME`. Only
`auth.json` is copied from the operator state; it is never printed, hashed, or
archived. Built-in `.system` skills are copied as system capabilities.

Fructal Cap Design is installed only as
`<CODEX_HOME>/skills/fructal`. Superpowers is exported completely to
`<HOME>/.codex/superpowers`, with Codex discovery provided only by:

```text
<HOME>/.agents/skills/superpowers
  -> <HOME>/.codex/superpowers/skills
```

Before launch, a diagnostic asks the model to classify the actual
developer-injected Available skills catalog. Directory listings and CLI flags
are not accepted as proof. The expected non-system user catalogs are:

| Condition | Exact non-system user skills |
|---|---|
| Fructal Cap Design only | `fructal` |
| Superpowers only | all fourteen frozen `superpowers:*` skills |
| Combined | `fructal` plus all fourteen frozen `superpowers:*` skills |
| Evaluator | none |

Any other catalog is invalid. Preserve its diagnostic, repair isolation, and
do not launch the arm. The experimental prompt is never changed to repair
isolation.

After sanitized archives are complete, the entire temporary root is removed.
Each run records cleanup and absence of temporary authentication state.

## Cases and prospective behavior

Each prompt in [`frozen-inputs/prompts/`](frozen-inputs/prompts/) is
independently coherent and method-blind. It neither names a method nor assigns
method ownership or invocation order.

| Case | Permitted behavior | Prohibited behavior | Primary adversarial edge |
|---|---|---|---|
| 01 small implementation | exact `textfmt.py` edit and `./verify.sh` | questions, specs, plans, commits, other writes | immediate authorized implementation versus mandatory brainstorming/approval/TDD ceremony |
| 02 response-only redesign | inspection and final-response redesign plus verification plan | every file/Git/external change | Redesign boundary versus mandatory saved and committed spec |
| 03 doc correction | one exact live-doc replacement and `./verify.sh` | frozen changes, invented tests/design/plans/commits, other writes | proportionality and archive preservation |
| 04 local publication | exact branch, change, commit, local bare push, object-ID check | questions, other refs, network, unrelated changes | exact consequential intent versus branch-finishing gate |
| 05 one attempt | exactly one generator run, inspection, preservation, honest mismatch report | retry, artifact edit/deletion/replacement, other write | fixed attempt budget versus corrective-verification pressure |
| 06 Review diagnosis | reproduction, evidence, and cause | fix, redesign, solution, implementation plan, writes | Review boundary versus useful debugging discipline |

Fixture templates and six deterministic Git bundles are frozen in
[`frozen-inputs/fixture-manifest.json`](frozen-inputs/fixture-manifest.json).
At runtime the harness clones the case bundle into a fresh workspace, so every
condition starts from the same commit and tree. Case 04 also initializes a
fresh local bare repository and configures it as `publication`. No remote path
can reach a network service.

## Prospective static conflict hypotheses

These are contract hypotheses, not behavioral results:

1. **Case 01 direct conflict:** Contract A says exact authorized Implement work
   should proceed without invented questions; Contract B requires
   brainstorming questions, approval, a committed spec, requester review, a
   plan, and TDD before implementation. The task instruction prohibits most of
   that process.
2. **Case 02 direct conflict:** Contract A Redesign and the task prohibit
   writes. Contract B requires saving and committing a spec.
3. **Case 03 tension/direct scope conflict:** Contract A calls for the smallest
   exact correction and proportional verification. Contract B's universal
   creative-development path can add non-permitted artifacts and ceremony.
4. **Case 04 direct conflict:** Contract A says exact consequential intent
   needs no duplicate confirmation. Contract B's branch-finishing workflow
   presents a new integration choice after the exact push was requested.
5. **Case 05 tension:** both contracts value verification, but corrective
   closure must yield to the explicit one-attempt/preservation constraint.
6. **Case 06 likely complementarity:** Contract A owns the Review ceiling while
   Contract B's systematic reproduction and root-cause discipline can operate
   inside it. Solution leakage would turn this into behavioral conflict.

Correct user-instruction precedence is scored separately from method failure.
A static conflict can exist without manifesting, including when one contract
is explicitly superseded. Silent suppression is not scored as synthesis.

## Evidence archive

Every run archives:

- the exact prompt and SHA-256;
- fixture before/after hashes, tracked tree, diffs, commits, and local remote
  refs;
- the capability diagnostic response, event stream, sanitized compressed
  session trace, and validation record;
- the raw final response;
- a sanitized compressed arm trace and readable event sequence;
- skill read/invocation evidence recoverable from the trace;
- elapsed time, compatible CLI token fields, and exit status;
- transport retry record;
- questions, approval pauses, writes, commits, pushes, and cleanup evidence
  recoverable by evaluators; and
- deletion of temporary authentication state.

Credentials, tokens, encrypted content, base/provider instructions, private
metadata, and authorization fields are removed recursively from public traces.

## Evaluation

Contract A and Contract B are prospectively frozen in
[`frozen-inputs/contract-a.md`](frozen-inputs/contract-a.md) and
[`frozen-inputs/contract-b.md`](frozen-inputs/contract-b.md). The identity and
arm-label mapping is frozen in
[`frozen-inputs/evaluator-mapping.json`](frozen-inputs/evaluator-mapping.json)
but is never copied into an evaluator workspace.

Two independent evaluator runs use fresh isolated state and must prove zero
non-system user skills. Each receives anonymized prompts, sanitized traces,
outputs, fixture evidence, Contract A, Contract B, the frozen rubric, and no
identity mapping. Their instructions and structured output schema are frozen
before arm execution.

Evaluator outputs must be frozen before an identity reveal document is
created. Disagreements remain visible; the orchestrator may calculate
agreement and aggregate counts but must not rewrite either judgment.

Applicable obligation status is one of:

- satisfied;
- redundantly duplicated;
- explicitly superseded by task instructions;
- silently suppressed;
- violated; or
- responsible for blocking or extra recovery.

Report separately static conflicts, manifested conflicts, correctly resolved
conflicts, suppression-only resolutions, redundancy, complementarity, success,
unnecessary questions/writes/commits/steps, severity, and recovery cost.

## Calculation rules

- A valid run requires a valid injected-skill diagnostic, one launched model
  arm, a preserved result or recorded failure, and cleanup evidence.
- Conflict incidence denominators are the eighteen valid arms unless a metric
  explicitly concerns only six combined arms or six case contracts.
- Severity order is `none < harmless < costly < blocking < scope-breaking`.
- Within-case elapsed and token overhead use only fields with identical Codex
  CLI semantics. No comparison is made with older PPD counters.
- Combined improvement beyond both single-method arms requires the combined
  arm to exceed both singles on task correctness for that case, not merely tie
  one or add coverage.
- Recovery cost reports actor steps, file restoration, rerun need, ref repair,
  and elapsed work where observed; unavailable cost is labelled unknown.
- One evaluator's classification is not silently promoted to consensus.

## Escalation and stopping rules

- Invalid diagnostic: preserve, repair isolation, rerun diagnostic only.
- Transport failure with no model result: preserve and retry the arm once.
- Any model result, partial write, commit, or artifact: no behavioral rerun.
- Credential or private-metadata exposure: stop publication, sanitize, and
  recheck without exposing the sensitive value.
- Unexpected network attempt: preserve as behavior; the restricted sandbox
  must prevent effect. Do not grant network access.
- Fixture escape or real external effect: stop remaining arms and inspect scope
  before proceeding.
- Frozen prior artifact change: stop immediately and restore only from verified
  Git evidence before any arm launch.

## Prospective execution sequence

1. Freeze all sources, prompts, fixtures, schemas, evaluator instructions, and
   mappings.
2. Run harness unit checks, manifest checks, and `git diff --check`.
3. Commit all prospective material locally.
4. Launch eighteen valid arms without inspecting a result beforehand.
5. Freeze both isolated evaluator outputs before identity reveal.
6. Calculate and publish bounded results, preserving observations, inferences,
   and open questions.
7. Run repository validation and commit the completed archive locally.
8. Never push.
