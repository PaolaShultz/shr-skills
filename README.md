# Fructal Cap Design

Fructal Cap Design is an open engineering method for constrained workflows,
packaged as a Codex skill. The current package version is **1.0.0**.

> A necessary constraint must guide the motion, never make the actor wrestle
> with the system.

It separates necessary constraints from accidental friction, traces the real
workflow across actors and interruptions, and proposes a more natural motion
without weakening safety, privacy, accessibility, ownership, compliance, or
data integrity.

Fructal Cap Design applies to:

- software and technical systems;
- physical tools, machines, and controls;
- services and operational processes;
- multi-actor, approval, permission, and handoff workflows.

It supports three explicit modes: Review, Redesign, and Implement. Review is the
safe default when the requested mode is unclear.

Review produces findings without proposing a replacement motion. Choose
Redesign for a proposed replacement without modification, or Implement for an
authorized change with verification.

## Read the method

- [Skill source](skills/fructal/SKILL.md)
- [Raw skill text](https://raw.githubusercontent.com/PaolaShultz/shr-skills/main/skills/fructal/SKILL.md)

## Install

Ask Codex:

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
short Codex skill identifier and invocation name.

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
workstation. The account also covers the
[Moj Sint](https://github.com/PaolaShultz/moj-sint) convergent experimental
workflow and its explicit claim boundaries. A
[physical-product comparison
record](docs/physical-product-comparison-protocol.md) preserves the prospective
protocol, prompt-contamination recovery, frozen enclosure runs, and a blind
three-arm comparison of no user skill, Superpowers, and Fructal Cap Design. The
[2026-07-24 workflow
postmortem](docs/workflow-postmortem-2026-07-24.md) reconstructs the complete
motion, including missed assumptions, recovery decisions, orchestration
corrections, preserved boundaries, and open work.

## Validate and evaluate

Run deterministic package, contract-case, documentation, and demo checks:

```bash
scripts/validate.sh
tests/test-validation.sh
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

Deterministic checks are the commit gate. Live evaluations exercise the
Review, Redesign, Implement, mixed-mode, confirmation, evidence, and diagnostic
contracts against a model in disposable read-only or workspace-write fixtures.

## Origin and independence

The method was shaped through practical engineering work, including
[SHR-DAW](https://github.com/PaolaShultz/shr-daw). Its name is inspired by a
particularly effective tethered juice-bottle cap: the constraint remains, but
the motion remains natural.

This independent project is not affiliated with or endorsed by
[FRUCTAL Živilska industrija d.o.o.](https://www.fructal.si/).

## Licence

[MIT](LICENSE)
