---
name: fructal
description: Use when a necessary constraint creates workflow-level obstruction in completion, recovery, handoff, or continuity across actors, states, channels, or systems, especially when change must preserve safety, privacy, accessibility, ownership, compliance, interoperability, or data integrity. Activate only for workflow-level friction; a requirement or constraint alone does not qualify. Never activate for purely aesthetic critique or an isolated defect unless evidence connects it to a broader workflow failure.
metadata:
  version: "1.1.0"
  source: "https://github.com/PaolaShultz/shr-skills/tree/main/skills/fructal"
---

# Fructal Cap Design

Apply this principle:

> A necessary constraint must guide the motion, never make the actor wrestle
> with the system.

The name comes from a tethered cap that satisfies a necessary constraint
without obstructing normal use. Preserve the constraint; redesign the motion.
An actor may be a person, team, service, device, or software component.
**Fructal Cap Design** is the intentional public name; lowercase `fructal` is
only the technical skill name and `$fructal` invocation.

## Pass the activation gate

Apply only to workflow-level conflict between a necessary constraint and the
motion through completion, recovery, handoff, or continuity. A requirement or
constraint alone does not qualify. Purely aesthetic critique and an isolated
defect without evidence of broader workflow failure stay outside this method.
An explicit `$fructal` request may apply it proportionally to a small workflow
issue; small does not mean exhaustive.

## Apply proportionally

Scale the work by consequence, complexity, uncertainty, reversibility, and the
number of affected actors. A small, local, reversible issue needs only enough
evidence to distinguish its constraint from friction, a focused application of
the cap test, and a focused check. A consequential, repeated, or multi-actor
workflow needs explicit actors and constraint sources, lifecycle and continuity
analysis, and thorough verification.

Do not enumerate irrelevant actors, paths, evidence labels, or tests. Depth is
valuable only where failure could change the outcome or confidence.

## Select and hold one mode

Select from the requested outcome and boundaries, not isolated keywords.

| Mode | Deliverable | Modify the system? |
| --- | --- | --- |
| **Review** | Evidence, findings, bounded recommendations if requested, and material open decisions | No |
| **Redesign** | Evidence plus a replacement motion and verification plan | No |
| **Implement** | An authorized change plus verification evidence | Yes |

- An explicit Review, Redesign, or Implement instruction selects that mode as a
  binding maximum outcome. A word that describes the subject is not a mode
  instruction:
  "review our implementation" selects Review.
- A stricter boundary always wins. A no-modification boundary caps Implement at
  Redesign when a replacement is requested, otherwise at Review.
- Without an explicit mode, select the highest authorized requested outcome:
  Implement, then Redesign, then Review. Default to Review when the outcome or
  modification authority is unclear.
- When a boundary prevents a higher outcome, complete the allowed deliverable
  and state what was not completed. Ask only if a material choice blocks it.

The mode is an internal control, not a required response heading. Analysis or
design inside Implement does not activate another mode's stop boundary. A later
mode change, boundary, or cancellation takes effect immediately: preserve safe
evidence and completed work, then stop newly prohibited action.

An Implement request authorizes ordinary in-scope modification. It does not
authorize an unstated deployment, deletion, purchase, message, permission
change, or other external effect. Treat a destructive or externally
consequential step as confirmed only when the action, target, and consequence
are explicit; otherwise ask once immediately before it. Do not ask again after
exact confirmation.

Ask only when the answer blocks safe progress: a material decision, missing
authority, necessary unavailable evidence, or an unconfirmed consequential
action. Other planning, debugging, delivery, or verification methods operate
inside the selected mode and cannot expand its authority.

## Execute the selected mode

### Review

Establish evidence, separate constraints from friction, and rank findings.
Bounded recommendations tied directly to findings are allowed when requested;
do not prescribe an end-to-end replacement motion. A findings-only or
no-recommendation boundary is stricter and must be respected. Do not change the
target system, actor-visible outcomes, permissions, content, business state, or
consequential external state.

Already-authorized read-only inspection may proceed when its only unavoidable
effects are ordinary access metadata such as logs, request counters, or
last-access timestamps. Treat costly, sensitive, rate-limited, operationally
consequential, or materially uncertain reads as unavailable evidence.
Disposable isolated diagnostics are allowed; clean up their temporary state
when safe. A stricter boundary such as "no external requests" or "no writes of
any kind" overrides these allowances. Stop after the Review deliverable.

### Redesign

Perform proportionate evidence and constraint analysis, then design the
smallest coherent replacement motion and its verification plan. Use Review's
diagnostic boundary. Do not modify the target system or present the proposal as
validated. Stop after the Redesign deliverable.

### Implement

Inspect enough of the owning system and current decisions to avoid a blind
change. Make the smallest coherent authorized change while preserving supported
constraints and unrelated state. Run checks proportionate to the affected
contract. Diagnose and repair in-scope failures, then rerun the failed checks.
Continue until verification passes or a genuine blocker leaves no safe
authorized work. Report the exact change, observed verification, and remaining
uncertainty.

## Establish evidence and constraints

1. Identify the intended outcome, current motion, and materially affected
   actors. Unknown actors are gaps to carry, not automatic reasons to stop.
2. Inspect the real workflow and current decisions when available. Treat code,
   documentation, research, support evidence, analytics, and expert judgment
   according to what each can prove.
3. Keep provenance and evidentiary status distinct: `provided` is requester-
   supplied material or fact; `reported` is an attributed but unverified claim;
   `observed` is directly inspected or measured evidence; `inference` is a
   derived conclusion; `open question` is a material unresolved gap. A
   `provided artifact` containing a `reported claim` proves the artifact says
   it, not that the claim is true. Use these distinctions in reasoning; label
   them explicitly only when status matters to a claim, risk, or decision.
4. Trace feedback and any materially relevant cancellation, failure, retry,
   interruption, handoff, delay, return, or repeated use. Never claim
   real-world validation without evidence from affected actors.

Name the source of each material constraint: actor or outcome requirement;
safety, privacy, law, or policy; accessibility; authorization, ownership, or
security; data integrity; interoperability or platform limits; verified
operational or business requirements; or verified technical facts. Mark
assumptions. Keep independently sourced constraints separate; do not use one to
justify another without evidence. Existing behavior is not automatically a
constraint.

Look for friction such as:

- layered exclusive modes, surprising labels, hidden effects, unclear
  responsibility, or controls that expose implementation or organizational
  internals;
- lost input, selection, focus, physical position, context, ownership, or
  intent;
- defaults or automation acting before consequences are legible;
- handoff, delay, cross-channel context loss, source-of-truth drift, or
  cross-actor effects without clear status;
- failure without nearby recovery or retained work;
- circular waits, stalled approvals, queue starvation, or ownerless progress;
- accessibility treated as an exception rather than part of the normal path;
- repeated decisions whose effort is not intrinsic to the outcome.

Rank material friction by consequence, frequency, and recovery cost.

## Redesign the motion in Redesign and Implement

- Make the obvious action produce one clear primary result. Create one coherent
  motion—not necessarily one click—and minimize cognitive friction rather than
  raw step count.
- Preserve necessary decisions, explicit choices, entered work, position,
  context, ownership, and intent.
- Make genuinely exclusive modes replace one another. Combine nested or
  orthogonal modes only when their interaction remains clear and safe.
- Make defaults, automation, continuously relevant constraints, and meaningful
  consequences legible at the point they matter without obstructing unrelated
  work.
- Do not treat setup, selection, authentication, or authorization as consent to
  a consequential action. Expose coupled effects before commitment, require
  exact intent for destructive or external effects, avoid duplicate
  confirmation after explicit intent, and make reversible actions easy to try
  and undo.
- Put recovery beside failure and retain work wherever safe. Reveal advanced
  choices, exceptions, and escalation progressively.
- Give each affected actor prompt, perceivable feedback: accessible sensory or
  assistive technology feedback for people; inspectable state, events,
  responses, or telemetry for services, devices, and software components.
- Prefer direct, inspectable control when it improves clarity, while preserving
  automation, accessibility, and expert paths that require another interaction.

Do not remove supported constraints, hide consequential state, weaken
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

If an applicable answer is no, revise the motion or state the supported
unavoidable tradeoff. In Implement, repeat the applicable questions against
observed verification. The test guides the work; do not print six ceremonial
answers unless they help the requester assess the result.

## Report and verify

Name the selected mode only when the task explicitly says `Review mode`,
`Redesign mode`, or `Implement mode`. Otherwise never expose the internal mode
as a heading or completion label.

Scale the report to the task without repeating evidence. Include only what is
applicable:

- Review: outcome and current motion, material evidence status, constraint
  sources, prioritized friction, requested bounded recommendations, and open
  decisions.
- Redesign: relevant before-and-after behavior, replacement motion, what remains
  unchanged, risks, verification scenarios, and material open decisions. A
  verification plan is not validated behavior.
- Implement: exact changes, relevant before-and-after behavior, preserved state,
  checks and observed results, and residual risks or open questions.

Choose verification from the affected contract and actual risk. Cover normal
completion and any materially affected cancellation, failure and retry,
repeated use, interruption or handoff, cross-channel or source-of-truth
continuity, stalled progress, accessibility—including relevant keyboard,
assistive technology, sensory, reach, and motor paths—and untouched state. Do
not enumerate or test paths the change cannot affect. Add focused checks for
actor-visible or system-observable behavior, and never equate automated checks
with real-world or affected-actor acceptance.

Keep visual or cosmetic observations separate from workflow findings. Route an
isolated defect to disciplined debugging without redesigning around it, while
holding the selected mode boundary and retaining ownership of the in-scope
result.
