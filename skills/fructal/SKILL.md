---
name: fructal
description: Use when a technical, operational, physical, service, or multi-actor workflow is constrained by necessary rules yet feels obstructive, surprising, mode-heavy, difficult to recover from, or prone to losing context. Also use when changing such a workflow must preserve safety, privacy, accessibility, ownership, compliance, interoperability, or data integrity. Do not use for purely aesthetic critique or isolated defects unless they materially affect the workflow.
---

# Fructal Cap Design

Apply this principle:

> A necessary constraint must guide the motion, never make the actor wrestle
> with the system.

The name comes from a tethered cap that satisfies a necessary constraint
without obstructing normal use. Preserve the constraint; redesign the motion.
An actor may be a person, team, service, device, or software component.

## Choose the mode

Honor the requested scope. When it is unclear, default to Review.

| Mode | Deliverable | Modify the system? |
| --- | --- | --- |
| **Review** | Evidence, findings, and questions | No |
| **Redesign** | Review plus proposed motions and verification | No |
| **Implement** | An approved change with appropriate tests | Yes |

## Establish evidence

1. State the intended outcome and identify every actor who initiates, continues,
   or experiences the result.
2. Inspect the real workflow and its current decisions when available. Treat
   documentation, research, support evidence, analytics, code, and expert
   judgment according to what each can actually prove.
3. Label claims as `provided` or `reported`, `observed`, `inference`, or
   `open question`. Reserve `observed` for direct evidence. Never claim
   real-world validation without evidence from affected actors.
4. Trace the path through feedback, cancellation, failure, retry, interruption,
   handoff, delayed outcome, return, and repeated use where applicable.

## Separate constraints from friction

Name the source of every claimed constraint: explicit actor, system, or outcome
requirement; safety, privacy, law, or policy; accessibility; authorization,
ownership, or security; data integrity; interoperability or platform limits;
verified operational or business requirements; or verified technical facts.
Mark assumptions. Keep independently sourced constraints separate; do not use
one to justify another without evidence. Existing behavior is not automatically
a constraint.

Look for:

- mutually exclusive modes that remain layered;
- surprising labels, hidden side effects, or unclear responsibility;
- controls that expose implementation or organizational internals;
- lost input, selection, focus, physical position, context, or ownership;
- defaults or automation that act before consequences are legible;
- handoffs, delays, and cross-actor effects without clear status;
- errors without nearby recovery or retained work;
- repeated decisions whose effort is not intrinsic to the task.

Rank friction by consequence, frequency, and recovery cost.

## Redesign the motion

- Make the obvious action produce one clear primary result.
- Create one coherent motion. This does not mean one click: preserve necessary
  decisions, but order them so their purpose and consequences are clear.
- Preserve explicit choices, entered work, location, and intent.
- Make genuinely exclusive modes replace one another.
- Make defaults and automatic behavior legible before meaningful consequence.
- Do not treat setup, selection, authentication, or authorization as consent to
  a consequential action unless that intent is explicit.
- Confirm destructive or externally consequential actions; make reversible
  actions easy to try and undo.
- Put recovery beside failure and retain work wherever safe.
- Prefer direct, inspectable control when it improves clarity; do not force it
  where automation, accessibility, or expert use requires another interaction.

Do not remove supported constraints, hide consequential state changes, weaken
accessibility or ownership, justify manipulation as a business requirement, or
invent unrelated changes.

## Report and verify

Scale the report to the task. Default to the smallest structure that preserves
the evidence, constraints, proposal, risks, and decisions. Do not repeat the
same evidence across sections. For each finding include:

1. intended outcome and observed sequence;
2. evidence status;
3. constraint, source, and confidence;
4. friction and priority by consequence, frequency, and recovery cost;
5. smallest coherent improvement and what must remain unchanged;
6. risk, verification scenarios, and decision required.

Verify normal completion, cancellation, failure and retry, repeated use,
interruption, actor handoff, relevant accessibility paths, and untouched
existing state. Keep visual or cosmetic observations separate from workflow
findings. Refer an isolated defect to the appropriate debugging process instead
of redesigning around it.
