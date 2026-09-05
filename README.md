# Fructal Cap Design

Fructal Cap Design is an open engineering method for constrained workflows,
packaged as a Codex skill. The current package version is **1.2.0**.

> A necessary constraint must guide the motion, never make the actor wrestle
> with the system.

It separates necessary constraints from accidental friction, traces materially
relevant workflow continuity across actors and interruptions, and creates a
more natural motion without weakening safety, privacy, accessibility,
ownership, compliance, or data integrity. Its depth scales with consequence,
complexity, uncertainty, reversibility, and the number of affected actors.

Fructal Cap Design applies when the handling of a necessary constraint causes
avoidable obstruction of completion, recovery, handoff, or continuity in:

- software and technical systems;
- physical tools, machines, and controls;
- services and operational processes;
- multi-actor, approval, permission, and handoff workflows.

Identify the retained constraint and a concrete obstruction linked to its
handling. A credible report can justify investigation; even one defective
control can qualify. Size and actor count do not decide. Ordinary requirements,
aesthetics, and local defects without that connection use ordinary design or
debugging instead. Declining the method does not abandon the task.

It supports three modes: Review, Redesign, and Implement. Review is the safe
default when the requested outcome or modification authority is unclear.

Review produces evidence and findings and may include requested bounded
recommendations without proposing an end-to-end replacement motion. Choose
Redesign for a proposed replacement without modification, or Implement for an
authorized change with verification. Related Review recommendations are allowed; a complete replacement sequence,
state model, or ownership structure belongs in Redesign. Mode labels are not
required. Authorized sensitive or rate-limited reads are permitted within their
limits. All six cap questions remain unchanged.

Version 1.2.0 cuts the skill from 1,914 to 1,104 words (42%) and strengthens verification; see the
[release notes](distribution/release-notes-1.2.0.md).

## Read the method

- [Skill source](skills/fructal/SKILL.md)
- [Raw skill text](https://raw.githubusercontent.com/PaolaShultz/shr-skills/main/skills/fructal/SKILL.md)
- [1.1 proportionality revision](docs/fructal-1.1-proportionality-design.md)
- [1.1.1 behavioral evaluation revision](docs/fructal-1.1.1-behavioral-evaluation-design.md)

## Install

The repository follows the open Agent Skills layout. Install the canonical
skill with the skills.sh CLI:

    DISABLE_TELEMETRY=1 npx skills add PaolaShultz/shr-skills --skill fructal

For GitHub Copilot, Codex, Claude Code, Cursor, and other agents supported by
the current GitHub CLI preview, install the published 1.2.0 skill with:

    gh skill install PaolaShultz/shr-skills fructal@v1.2.0 --agent AGENT --scope user

Replace <code>AGENT</code> with a value supported by
<code>gh skill install</code>, such as <code>codex</code>,
<code>claude-code</code>, or <code>cursor</code>. GitHub documents this preview
for GitHub CLI 2.90.0 or later.

Claude Code can also install the repository marketplace:

    claude plugin marketplace add PaolaShultz/shr-skills
    claude plugin install fructal@shr-skills

That plugin invokes the skill as <code>/fructal:fructal</code>.

Cursor's current first-party flow can import the repository directly: open
**Cursor Settings → Rules → Add Rule → Remote Rule (Github)** and enter
<https://github.com/PaolaShultz/shr-skills>. Cursor documents GitHub import but
not a general public skill-marketplace submission.

You can also ask Codex:

```text
Install the skill from https://github.com/PaolaShultz/shr-skills/tree/main/skills/fructal
```

Then choose one form and replace the bracketed text:

Review:

```text
Use $fructal to review this constrained workflow and report findings only, without modifying it: [workflow]
```

Redesign:

```text
Use $fructal to redesign this constrained workflow without modifying it: [workflow]
```

Implement:

```text
Use $fructal to implement and verify this constrained workflow change: [change]
```

The method is named **Fructal Cap Design**. Lowercase `fructal` is only its
short Codex skill identifier and invocation name; the spelling is intentional.

## Distribution and support

The OpenAI and Claude plugin wrappers in
[distribution/plugins/fructal](distribution/plugins/fructal) contain one
byte-identical mirror of the canonical skill. Run
<code>scripts/sync-distribution.py</code> after a canonical change; validation
rejects drift. The wrapper is nested below a non-discoverable package path so
GitHub skill search lists only the canonical <code>skills/fructal</code> entry.

- [Public site](https://paolashultz.github.io/shr-skills/)
- [Support and bug reports](https://github.com/PaolaShultz/shr-skills/issues)
- [Adversarial workflow case form](https://github.com/PaolaShultz/shr-skills/issues/new?template=adversarial-workflow.yml)
- [Privacy](https://paolashultz.github.io/shr-skills/privacy.html)
- [Terms](https://paolashultz.github.io/shr-skills/terms.html)
- [1.2.0 release notes](distribution/release-notes-1.2.0.md)
- [Submission test cases](distribution/submission-test-cases.json)
- [Historical 1.1.1 distribution ledger](docs/distribution-report-1.1.1.md)

## Demonstrate it in ChatGPT Web

The [ChatGPT Web demonstration](examples/chatgpt-web-demo.md) requires no
installation. Copy one prompt containing the complete skill and a task slot,
then insert any problem or use the short prepared EV-charger example.

The resulting conversation shows the method, problem, and evidence-backed
response directly, with almost no explanatory framing.

## Real-world usage and testing

Read the [real-world usage and testing
account](docs/real-world-usage-and-testing.md) for Fructal Cap Design's
self-application, an anonymized private software case, and the public
[SHR-DAW](https://github.com/PaolaShultz/shr-daw) Raspberry Pi workflow audit,
repair, and acceptance evidence. The SHR-DAW case also records a low-power-first
development position: its editing, builds, tests, QA, and release work ran
directly on the target Raspberry Pi rather than requiring a desktop
workstation. The private case now also includes an anonymized three-arm
implementation replay. It held Superpowers constant while comparing historical
Fructal Cap Design, no Fructal Cap Design, and the then-current revision over
the same repair brief authored by Fructal Cap Design. That replay supports a
bounded implementation-stage workflow-integrity claim, not a discovery
advantage or universal superiority claim. The public replay account does not
identify the tested skill revisions and does not validate 1.2.0. The account
also covers the
[Moj Sint](https://github.com/PaolaShultz/moj-sint) convergent experimental
workflow and its explicit claim boundaries. A
[physical-product comparison
record](docs/physical-product-comparison-protocol.md) preserves the prospective
protocol, prompt-contamination recovery, frozen enclosure runs, and a blind
three-arm comparison of no user skill, Superpowers, and Fructal Cap Design. The
[PPD-003 layered comparison](docs/evaluations/physical-product-comparison/ppd-003-layered-comparison/)
adds the prospectively frozen combined arm, two blind prompt-author judges,
two five-layer artifact judges, exact render-call extraction, and error-origin
attribution. Its separate
[ZIT cross-renderer
extension](docs/evaluations/physical-product-comparison/ppd-003-layered-comparison/cross-renderer/zit-001/)
re-renders all four frozen designs with a second image system while preserving
both byte-identical and renderer-adapted prompt conditions. The
[FSI-001 adversarial method-composition
experiment](docs/evaluations/method-interaction/fsi-001-adversarial-composition/)
tests six deterministic local workflows with Fructal Cap Design,
Superpowers, and both packages together, including isolated skill diagnostics,
two anonymous evaluators, obligation-level evidence, conflict incidence,
suppression, cost, and recovery. The
[2026-07-24 workflow
postmortem](docs/workflow-postmortem-2026-07-24.md) reconstructs the complete
motion, including missed assumptions, recovery decisions, orchestration
corrections, preserved boundaries, and open work.

## Validate and evaluate

Run deterministic package, contract-case, documentation, and demo checks:

```bash
scripts/validate.sh
tests/test-validation.sh
python3 tests/test-distribution.py
```

After synchronizing an installed copy, include its absolute skill directory:

```bash
scripts/validate.sh --installed /absolute/path/to/installed/fructal
```

Run the isolated live Codex evaluation matrix:

```bash
tests/test-live-eval-harness.sh
scripts/evaluate.sh
```

Deterministic checks are the commit gate. The behavioral matrix captures
a natural executor response and fixture effects, then asks a separate isolated
evaluator to judge the actual output against the contract. It exercises
activation and non-activation, installed-skill discovery, proportionality,
Review recommendations, mode boundaries and changes, both sides of
consequential confirmation, permitted and prohibited reads, evidence, recovery,
continuity, accessibility, the cap test, and untouched state.

Submission examples link related coverage through `contract_case_ids` in
`tests/contract-cases.json`; distribution validation rejects missing case IDs
and stale submission versions. These references are not execution results for
the submission prompts. Static checks do not establish semantic consistency
of all documentation; review current-facing prose when the contract changes,
and keep historical evidence explicitly tied to its original revision.

`scripts/evaluate.sh --skill-git-ref REVISION` supports historical comparison.
`--repetitions N` repeats every selected case, and `--archive-dir PATH`
preserves successful responses, event evidence, fixture snapshots, evaluations,
metadata, and a SHA-256 manifest for audit.
`--judge-model MODEL` selects a different judge; the default uses the executor
model. Current archives also retain failed fixture checks and frozen inputs.

The [1.2.0 regression record](docs/evaluations/live-contract/fructal-1.2.0/)
records the development matrix, discovered failures, and focused corrections.

The historical 1.1.1 candidate passed the [complete 24-case release
matrix](docs/evaluations/live-contract/fructal-1.1.1/) and [21 repeated
high-risk runs](docs/evaluations/live-contract/fructal-1.1.1-critical-repetitions/).
Development-failure archives remain beside them so the published evidence does
not hide the iterations that changed the contract and evaluator. These scores
do not validate 1.2.0. The harness is a development regression suite, not a
held-out benchmark or evidence of benefit over a no-skill baseline.

## Origin and independence

The method was shaped through practical engineering work, including
[SHR-DAW](https://github.com/PaolaShultz/shr-daw). Its name is inspired by a
particularly effective tethered juice-bottle cap: the constraint remains, but
the motion remains natural.

This independent project is not affiliated with or endorsed by
[FRUCTAL Živilska industrija d.o.o.](https://www.fructal.si/).

## Licence

[MIT](LICENSE)
