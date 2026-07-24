# Fructal Cap Design

Fructal Cap Design is an open engineering method for constrained workflows,
packaged as a Codex skill.

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
Use $fructal to review this constrained workflow without modifying it: [workflow]
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
installation. Its deliberately plain task lets the embedded skill—not extra
prompt instructions—determine the analysis and response structure.

## Origin and independence

The method was shaped through practical engineering work, including
[SHR-DAW](https://github.com/PaolaShultz/shr-daw). Its name is inspired by a
particularly effective tethered juice-bottle cap: the constraint remains, but
the motion remains natural.

This independent project is not affiliated with or endorsed by
[FRUCTAL Živilska industrija d.o.o.](https://www.fructal.si/).

## Licence

[MIT](LICENSE)
