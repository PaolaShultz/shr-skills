# Real-World Usage Documentation Design

## Purpose

Document an anonymized real-world use of Fructal Cap Design that demonstrates
the method's practical role beside a structured software-delivery skill suite.
The account must explain what Fructal discovered, what implementation discipline
contributed afterward, and why the two approaches are complementary rather than
interchangeable.

The documentation must not identify the project, organization, repository,
routes, domain, or proprietary implementation details.

## Deliverables

Create one public document:

- `docs/real-world-usage-and-testing.md`

Add one concise README entry under a new `## Real-world usage and testing`
heading. The entry will describe the document as an anonymized practical account
and link to it. The README will not repeat the case study.

The canonical skill, embedded demonstration, package metadata, validators, and
installed copy will remain unchanged.

## Evidence boundary

The public account may state that:

- a read-only Fructal review examined several connected software workflows;
- it found multiple workflow-contract failures that had not been surfaced by
  the software-delivery skill suite already used on the project;
- the findings concerned cross-step state, identity, ownership, recovery,
  context, accessibility, and actor-visible feedback;
- the review and later implementation were separate authorized stages;
- subsequent implementation used reproduction, focused behavioral coverage,
  narrow owning-layer changes, broader automated tests, and browser checks.

The account must not publish project-specific counts, commit identifiers,
filenames, routes, locations, product terminology, or details that could identify
the source project. It must not imply that one case proves universal superiority
or general real-world validation of the method.

Claims must distinguish:

- `observed`: what happened in the documented use;
- `inference`: what that use suggests about the methods' respective roles;
- `open question`: what cannot be concluded from one case.

## Document structure

The public document will contain:

1. **Case context** — an anonymous software project already using a disciplined
   agentic software-delivery workflow.
2. **What the Fructal review found** — generalized classes of latent
   workflow-contract failures, without project details.
3. **Why the existing skill suite did not find them** — the difference between
   executing a framed feature or defect rigorously and inspecting the whole
   constrained workflow for unreported friction.
4. **Division of responsibility** — Fructal for problem-space discovery and
   preservation boundaries; the software-delivery suite for debugging, TDD,
   implementation, review, and completion discipline.
5. **Capability table** — retain the layered comparison requested by the
   maintainer:

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

6. **Practical conclusion** — the methods are highly complementary: Fructal
   helps discover and bound the right workflow problem; software-delivery skills
   help implement the resulting change reliably.
7. **Limits of the evidence** — one substantial use supports the practical
   distinction but does not establish universal effectiveness, numerical
   superiority, or a general success rate.

The comparison may name and link Superpowers as the concrete skill suite used,
while keeping the project anonymous. The table heading will remain generic so
its distinction applies beyond one implementation.

## Presentation

Use concise engineering prose rather than promotional language. Lead with the
observed outcome, preserve the evidence labels, and avoid unsupported
percentages or subjective numeric scores in the public document.

No screenshots or diagrams are required. The comparison table is the smallest
visual structure that materially clarifies the division of responsibility.

## Validation

Before committing the implementation:

1. scan the document and README diff for identifying project details;
2. verify every local Markdown link;
3. run `scripts/validate.sh`;
4. run `tests/test-validation.sh`;
5. run `tests/test-live-eval-harness.sh`;
6. run `git diff --check`;
7. review the complete diff and confirm that the skill, embedded demonstration,
   metadata, and installed copy did not change.

The live model evaluation matrix is not required because the skill contract is
unchanged.
