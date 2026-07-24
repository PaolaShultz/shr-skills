# Real-world usage and testing

## Case context

**Observed:** A substantial software project was already being developed with
[`Superpowers`](https://github.com/obra/superpowers), a structured
software-delivery skill suite covering design, planning, debugging, test-driven
development, verification, review, and branch completion.

A separate read-only Fructal Cap Design review then inspected several connected
workflows as complete constrained motions rather than as a collection of known
features or defects. The review and the later authorized implementation were
separate stages.

The project is intentionally anonymous. Its name, organization, domain,
repository, routes, implementation identifiers, and test counts are not part of
this account.

## What the Fructal review found

**Observed:** The review identified multiple workflow-contract failures that the
existing software-delivery process had not surfaced. The individual components
often worked, but their combined motion could still:

- lose or obscure state between steps;
- confuse displayed context with persisted identity;
- make ownership or responsibility unclear;
- preserve an action while losing the actor's position or intent;
- provide incomplete feedback after filtering, navigation, or delayed work;
- make cancellation, reset, retry, return, or repeated use behave differently
  from the normal path;
- treat accessibility as a local control property instead of part of the whole
  workflow;
- expose implementation boundaries that actors should not have to manage.

These were not all conventional defects. Some were gaps between individually
valid components, some required clarification of the intended product contract,
and some became reproducible behavioral failures.

## Why the existing delivery workflow had not found it

**Inference:** A software-delivery skill suite usually begins with a framed
feature, defect, or implementation goal and asks how to execute that work
reliably. Its strongest mechanisms activate after the problem has been named:
design approval, plans, root-cause debugging, focused tests, implementation
discipline, review, and fresh verification.

Fructal begins earlier and at a different boundary. It asks:

- who initiates, continues, and experiences the result;
- which constraints are necessary and what establishes each one;
- where the system makes an actor manage accidental implementation friction;
- what happens through feedback, cancellation, failure, retry, interruption,
  handoff, delay, return, and repeated use;
- whether context, position, entered work, ownership, and intent survive;
- whether recovery returns every affected actor to motion;
- whether accessibility is part of the normal and recovery paths;
- what must remain untouched.

This broader inspection can reveal unreported workflow friction even when local
tests pass and no single component appears broken.

## Division of responsibility

**Observed:** Fructal supplied the discovery and preservation boundary. It
separated necessary constraints from existing behavior, distinguished observed
defects from product decisions and open questions, and identified the state and
actor contracts that later changes had to preserve.

The subsequent authorized implementation used the software-delivery suite's
strongest mechanisms: reproduce suspected defects, add focused behavioral
coverage, make narrow owning-layer changes, run broader automated tests, inspect
browser-visible behavior, and verify completion from fresh evidence.

The practical sequence was:

> Fructal discovers and bounds the right workflow problem; software-delivery
> skills help implement the resulting change reliably.

## Capability comparison

| Capability | Fructal Cap Design | Structured software-delivery skills |
| --- | --- | --- |
| Finding unreported workflow friction | Primary strength | Secondary |
| Cross-step and cross-actor continuity | Primary strength | Partial |
| Separating necessary constraints from existing behavior | Explicit | Not a central contract |
| Recovery, cancellation, return, and repeated use | Explicit lifecycle | Usually task-dependent |
| Preserving context, work, ownership, and intent | Explicit acceptance condition | Usually requirement-dependent |
| Accessibility in the normal path | Integrated | Depends on the task and tests |
| Root-cause debugging of a known defect | Supporting process | Primary strength |
| Test-driven implementation | Required when appropriate | Primary strength |
| Repository and branch discipline | Defers to the owning environment | Primary strength |
| Verification before completion | Required | Primary strength |

This table compares primary responsibilities, not absolute capability. Either
method can contribute outside its strongest area when the task and environment
provide the necessary evidence.

## Practical result

**Inference:** Fructal and structured software-delivery skills are more
complementary than interchangeable.

Fructal was stronger in this case at problem-space coverage: discovering latent
friction across actors, steps, state boundaries, recovery paths, and necessary
constraints. The delivery suite was stronger at implementation mechanics:
debugging a known failure, test-driven repair, repository discipline, review,
and completion evidence.

The case demonstrates why passing local tests does not prove that a complete
workflow remains coherent. It also demonstrates why a broad workflow review is
not a substitute for disciplined implementation. Both layers were needed.

## Limits of the evidence

**Open question:** One substantial use does not establish a universal success
rate, numerical superiority, or equal effectiveness in other technical,
physical, service, operational, or safety-critical settings.

The case is direct evidence that Fructal found material workflow problems not
previously surfaced by the existing delivery process in this project. It is
evidence of practical complementarity, not proof that Fructal will outperform
every alternative method or skill suite.
