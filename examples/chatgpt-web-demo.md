# See it in action

Copy the prompt below into ChatGPT.

```text
Use the SKILL below to execute the TASK.

SKILL
---
name: fructal
description: Use when a technical, operational, physical, service, or multi-actor workflow is constrained by necessary rules yet feels obstructive, surprising, mode-heavy, difficult to recover from, or prone to losing context. Also use when changing such a workflow must preserve safety, privacy, accessibility, ownership, compliance, interoperability, or data integrity. Do not use for purely aesthetic critique or isolated defects unless they materially affect the workflow.
metadata:
  version: "1.0.0"
  source: "https://github.com/PaolaShultz/shr-skills/tree/main/skills/fructal"
---

# Fructal Cap Design

Apply this principle:

> A necessary constraint must guide the motion, never make the actor wrestle
> with the system.

The name comes from a tethered cap that satisfies a necessary constraint
without obstructing normal use. Preserve the constraint; redesign the motion.
An actor may be a person, team, service, device, or software component.

## Select and hold one mode

Select from the requested outcome and boundaries, not isolated keywords or the
example prompt that invoked the skill.

| Mode | Deliverable | Modify the system? |
| --- | --- | --- |
| **Review** | Evidence, findings, and any material open decisions | No |
| **Redesign** | Evidence plus a replacement motion and verification plan | No |
| **Implement** | An authorized change plus verification evidence | Yes |

- Review is the outcome for assessment or explanation without a replacement
  motion or change.

- Redesign is the outcome for a proposal or plan without authorized
  modification.

- Implement is the outcome for actual in-scope modification or approval of a
  prior proposal. Review or design work requested alongside the change remains
  analysis inside Implement.

- An explicit instruction to use Review, Redesign, or Implement selects that
  mode as a binding maximum outcome. A mode word that only describes the subject
  does not select a mode; "review our implementation" selects Review.

- A stricter explicit boundary always wins. A no-modification boundary caps
  Implement at Redesign when a replacement motion is requested, otherwise at
  Review.

- Without an explicit mode instruction, select the highest authorized requested
  outcome: Implement, then Redesign, then Review.

- When an explicit mode or boundary prevents a requested higher outcome,
  complete the allowed deliverable and state which outcome was not completed.
  Do not ask unless a material choice blocks that deliverable.

- When the requested outcome remains unclear, default to Review.

State the selected mode. Only one mode is active; analysis or design performed
inside Implement does not activate another mode's stop boundary. Hold the mode
until the requester changes or cancels scope. Any explicit mode change, boundary
change, or cancellation takes effect immediately: retain safe evidence and
completed work, then stop any newly prohibited action.

An explicit Implement request authorizes ordinary in-scope modification. For a
destructive or externally consequential step, treat the original request as
confirmation only when it makes the action, target, and consequence explicit.
Otherwise ask once immediately before that step; do not ask again after exact
confirmation. General implementation approval does not by itself authorize an
unstated deployment, deletion, purchase, message, permission change, or other
external effect.

Ask only when the answer blocks safe in-scope progress: a material decision,
missing authority, necessary unavailable evidence, or a consequential action
outside the confirmed scope. Do not invent questions or stop for non-blocking
preferences.

## Execute the selected mode

### Review

Establish evidence, separate constraints from friction, rank the findings, and
report only material decisions that remain open. Do not prescribe a replacement
motion, localized remediation, or other solution. Do not change workflow or
business state, permissions, content, actor-visible outcomes, or consequential
external state. Already-authorized read-only inspection may proceed when its
only unavoidable effects are ordinary access metadata such as logs, request
counters, or last-access timestamps. Treat the read as unavailable evidence
when it is costly, sensitive, rate-limited, operationally consequential, or has
unknown material effects. Disposable isolated diagnostics are allowed; clean up
their temporary state when safe. A stricter requester boundary such as "no
external requests" or "no writes of any kind" overrides this allowance. Stop
after the review deliverable.

### Redesign

Perform the evidence and constraint analysis without taking the Review stop,
then design the smallest coherent replacement motion and its verification plan.
Use the same diagnostic boundary as Review. Do not modify the target system or
present the proposed motion as validated. Stop after the redesign deliverable.

### Implement

Complete enough evidence analysis and motion design to avoid a blind change.
Inspect the owning system, its current decisions, and applicable instructions.
Complete the authorized scope through the smallest coherent owning changes,
preserving supported constraints and unrelated state. Add and run appropriate
tests, trials, or checks. If a check fails, diagnose and repair within scope,
then rerun it. Continue until verification passes or a genuine blocker leaves
no safe authorized work; do not reclassify a fixable failure as residual
uncertainty. Verify relevant normal and recovery paths, then report the exact
changes, scope covered, evidence, and remaining uncertainty.

## Establish evidence

1. State the intended outcome and identify every relevant actor who initiates,
   continues, or experiences the result. Do not block on an unknown actor;
   label the gap and continue where safe.

2. Inspect the real workflow and its current decisions when available. Treat
   documentation, research, support evidence, analytics, code, and expert
   judgment according to what each can actually prove.

3. Classify provenance and evidentiary status separately. Label material or a
   task fact supplied directly by the requester as `provided`; an unverified
   claim attributed to another actor or source as `reported`; evidence directly
   inspected or measured in the task as `observed`; a derived conclusion as
   `inference`; and an unresolved material gap as `open question`. Labels may
   combine: a supplied support document is a `provided artifact` containing a
   `reported claim`. Observing the document proves that it contains the claim,
   not that the claim is true. Never claim real-world validation without
   evidence from affected actors.

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

- handoffs, delays, cross-channel context loss, source-of-truth drift, or
  cross-actor effects without clear status;

- errors without nearby recovery or retained work;

- circular waits, stalled approvals, queue starvation, or unclear ownership that
  prevents any actor from progressing;

- accessibility needs treated as exceptional instead of part of normal use;

- repeated decisions whose effort is not intrinsic to the task.

Rank friction by consequence, frequency, and recovery cost.

## Redesign the motion in Redesign and Implement

Apply this section only in Redesign and Implement. Review stops before
prescribing a replacement motion.

- Make the obvious action produce one clear primary result.

- Create one coherent motion. This does not mean one click: preserve necessary
  decisions, but order them so their purpose and consequences are clear.
  Minimize cognitive friction rather than raw clicks, steps, or controls.

- Preserve explicit choices, entered work, location, and intent.

- Make genuinely exclusive modes replace one another. Combine nested or
  orthogonal modes only when their interaction remains obvious and safe.

- Make defaults and automatic behavior legible before meaningful consequence.

- Keep continuously relevant constraints and safety state legible without
  obstructing unrelated work.

- Do not treat setup, selection, authentication, or authorization as consent to
  a consequential action unless that intent is explicit.

- Make destructive or externally consequential actions legible and require
  exact actor intent. Expose coupled consequential effects before commitment.
  Do not add duplicate confirmation after that intent is explicit. Make
  reversible actions easy to try and undo.

- Put recovery beside failure and retain work wherever safe.

- Reveal advanced choices, exception handling, and escalation progressively
  instead of forcing them through the normal path.

- Provide immediate feedback through a channel each affected actor can perceive
  or observe. Use accessible sensory or assistive-technology feedback for people
  and inspectable state, events, responses, or telemetry for services, devices,
  and software components.

- Prefer direct, inspectable control when it improves clarity; do not force it
  where automation, accessibility, or expert use requires another interaction.

Do not remove supported constraints, hide consequential state changes, weaken
accessibility or ownership, justify manipulation as a business requirement, or
invent unrelated changes.

## Run the six-question cap test in Redesign and Implement

Before finalizing a replacement motion, ask:

1. Does the obvious action produce one clear result?

2. Is the motion coherent without hiding a necessary decision or consequence?

3. Is each constraint visible or active when needed without obstructing
   unrelated work?

4. Are context, position, entered work, ownership, and intent preserved?

5. Do feedback and recovery guide every affected actor back into motion?

6. Is the remaining effort intrinsic to the outcome rather than the system?

If any answer is no, revise the motion or state the supported unavoidable
tradeoff. In Implement, repeat the test against observed verification results.

## Report and verify

Scale the report to the task and selected mode. Use the smallest structure that
preserves the necessary evidence without repeating it.

For every mode, include when applicable:

1. intended outcome and current sequence; state when none exists, and include a
   nearest analogous sequence only when evidence supports it;

2. evidence status;

3. constraint, source, and confidence;

4. friction and priority by consequence, frequency, and recovery cost.

For Redesign, add the replacement motion, what must remain unchanged, risks,
verification scenarios, and any material decisions still required. Treat
verification as a plan; do not claim the proposed motion has been validated.

For Redesign and Implement, state relevant before-and-after behavior precisely.
Their verification plans and checks must cover the applicable normal
completion, cancellation, failure and retry, repeated use, interruption, actor
handoff, cross-channel and source-of-truth continuity, stalled-progress or
circular-wait paths, accessibility—including keyboard, assistive technology,
sensory, reach, and motor paths—and untouched state.

For Implement, add the exact change, what remained unchanged, tests or other
checks run, observed results, and residual risks or open questions. Add focused
checks for the actor-visible or system-observable contract. Never claim
real-world or affected-actor validation without that evidence.

Keep visual or cosmetic observations separate from workflow findings. Refer an
isolated defect to an available debugging process; if none exists, apply
disciplined root-cause analysis directly. Keep the selected mode boundary, do
not stop at an ownerless referral, and do not redesign around the defect.

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
and locks the connector for 60 seconds without explaining why. Redesign the
workflow without weakening electrical safety, payment authorization, connector
security, or fraud controls.
```
