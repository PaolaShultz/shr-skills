# See it in action

Copy the prompt below into ChatGPT.

```text
Use the SKILL below to execute the TASK.

SKILL
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

## Choose and hold the mode

Select the mode from the requested outcome and boundaries, not from the example
prompt that invoked the skill.

| Mode | Deliverable | Modify the system? |
| --- | --- | --- |
| **Review** | Evidence, findings, and decision questions | No |
| **Redesign** | Review plus a replacement motion and verification plan | No |
| **Implement** | An authorized change plus verification evidence | Yes |

- Requests to review, audit, assess, or explain select Review.

- Requests to propose, redesign, or plan without modification select Redesign.

- Requests to fix, change, build, apply, or implement select Implement. An
  explicit request to do the work, or approval of a prior proposal, authorizes
  in-scope modification; do not ask for the same approval again.

- When wording and boundaries conflict, honor the boundary. For example,
  "redesign, but do not modify" selects Redesign.

- When the requested outcome remains unclear, default to Review.

State the selected mode. Hold its boundary: Review and Redesign never modify
the system. Implement includes the analysis needed for a sound change and must
not stop after reporting while safe, authorized work remains. Ask only when a
material decision, missing authority, or consequential action remains outside
the approved scope.

## Execute the selected mode

### Review

Establish evidence, separate constraints from friction, rank the findings, and
report decision questions. Do not prescribe a replacement motion or modify the
system. Stop after the review deliverable.

### Redesign

Perform the Review analysis without stopping at its deliverable, then design
the smallest coherent replacement motion and its verification plan. Do not
modify the system or present the proposed motion as validated. Stop after the
redesign deliverable.

### Implement

Complete enough Review and Redesign work to avoid a blind change. Inspect the
owning system, its current decisions, and applicable instructions. Implement
the smallest coherent improvement, preserving supported constraints and
unrelated state. Add and run appropriate tests, trials, or checks. Verify the
changed motion across relevant normal and recovery paths, then report the exact
change, evidence, and residual uncertainty.

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

## Redesign the motion in Redesign and Implement

Apply this section only in Redesign and Implement. Review stops before
prescribing a replacement motion.

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

Scale the report to the task and selected mode. Use the smallest structure that
preserves the necessary evidence without repeating it.

For every mode, include:

1. intended outcome and current sequence;

2. evidence status;

3. constraint, source, and confidence;

4. friction and priority by consequence, frequency, and recovery cost.

For Redesign, add the replacement motion, what must remain unchanged, risks,
verification scenarios, and decisions required. Treat verification as a plan;
do not claim the proposed motion has been validated.

For Implement, add the exact change, what remained unchanged, tests or other
checks run, observed results, and residual risks or open questions. Verification
must cover the applicable normal completion, cancellation, failure and retry,
repeated use, interruption, actor handoff, accessibility, and untouched-state
paths. Never claim real-world or affected-actor validation without that
evidence.

Keep visual or cosmetic observations separate from workflow findings. Refer an
isolated defect to the appropriate debugging process instead of redesigning
around it.

TASK
[INSERT YOUR TASK HERE]
```

Replace `[INSERT YOUR TASK HERE]` with any technical, operational, physical,
service, or other constrained workflow you want Fructal Cap Design to address.

Or use the prepared example below:

```text
An EV charger must authenticate payment before power flows. If the driver
connects the cable before paying, the charger rejects the session and requires
unplugging, paying, and reconnecting. When payment fails, it shows an error code
and locks the connector for 60 seconds without explaining why. Improve the
workflow without weakening electrical safety, payment authorization, connector
security, or fraud controls.

Use Redesign mode. Keep the answer under 500 words. Prioritize the three
highest-impact findings. Use one compact findings table and one proposed flow.
Do not repeat the same evidence across sections. Treat facts supplied in this
task as provided, not observed.
```
