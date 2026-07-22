---
name: fructal-cap-design
description: Audit and redesign constrained user workflows so necessary rules, safety, and state remain intact but feel natural. Use when an interface or physical interaction feels awkward, requires too many steps, surprises the user, fights recovery, exposes implementation details, layers conflicting modes, loses selection or context, or satisfies a safety/compliance requirement in an obstructive way. Also use when simplifying a workflow without weakening its essential constraints.
---

# Fructal Cap Design

Apply this principle:

> A necessary constraint must guide the user, never make them wrestle with the
> product.

The name comes from a tethered bottle cap that meets the same constraint as
awkward competitors but rolls cleanly out of the way and guides itself back
into place. Preserve the tether; redesign the motion.

## Audit the workflow

1. State the user's intended outcome in plain language.
2. Separate hard constraints from accidental implementation friction. Preserve
   safety, ownership, compliance, data integrity, and explicit user choices.
3. Trace the actual path from starting state to outcome, including feedback,
   cancellation, failure, retry, and return. Count decisions and mode changes,
   not only clicks.
4. Identify each point where the product makes the user manage its internals.

Look especially for:

- a label whose action does something unexpected;
- one action causing several hidden state changes;
- mutually exclusive modes that remain layered;
- selection, cursor, page, or context moving without intent;
- repeated confirmation for reversible operations;
- irreversible operations without meaningful confirmation;
- automatic loading, advancing, or substitution;
- errors that name a fault but offer no nearby recovery;
- safety mechanisms that obstruct the normal action;
- repeated controls required only because implementation state leaked into the
  interface.

## Redesign the motion

Choose the smallest coherent change that makes the intended path natural:

- Make the obvious action produce the obvious result.
- Give one action one primary outcome.
- Preserve the user's place and selection unless changing them is the action.
- Make genuinely exclusive modes replace one another.
- Keep safe defaults visible through behavior rather than repeated ceremony.
- Confirm destructive or externally consequential actions; make reversible
  actions easy to try and undo.
- Put recovery beside the failure and retain the user's work.
- Reveal advanced choices progressively instead of forcing them through the
  main path.
- Prefer direct manipulation and immediate feedback over hidden automation.
- Minimize cognitive friction, not raw button count. Fewer controls are not an
  improvement if they create mystery or overloaded modes.

Do not “solve” friction by removing a required safety constraint, hiding an
important state change, or inventing adjacent features.

## Run the Fructal-cap test

For the proposed workflow, answer:

1. Does the obvious action do the obvious thing?
2. Can the normal outcome happen in one natural motion?
3. Does the constraint stay out of the way until it is needed?
4. Are location, selection, and intent preserved?
5. Does recovery guide the user back into place?
6. Is any remaining effort intrinsic to the task rather than caused by the
   implementation?

If any answer is no, revise the motion or explain the unavoidable tradeoff.

## Verify behavior

Check at least these paths when they apply:

- normal completion;
- cancellation or Back;
- repeated use;
- failure and retry;
- interruption or mode change;
- existing state that must remain untouched.

State before-and-after behavior precisely. For code changes, add focused tests
for the user-visible contract and avoid broad unrelated redesign. For a review,
report the friction, preserved constraint, proposed natural motion, and
verification scenarios without modifying the product unless asked.
