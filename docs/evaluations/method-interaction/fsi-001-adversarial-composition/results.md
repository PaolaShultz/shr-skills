# Results and bounded interpretation

## Outcome

All **18/18 arms were valid**: each had the expected injected user-skill
catalog, a readable sanitized trace, task-process exit status 0, and confirmed
temporary-root/auth cleanup. There were no invalid arms and no transport
retries.

The two evaluators agreed on task outcome for every arm:

| Outcome | Arms |
|---|---:|
| Yes | 13 |
| Partial | 3 |
| No | 2 |

The three partial outcomes were the combined Case 04 local publication and the
combined/Superpowers-only Case 06 Review arms. The two failures were the
single-method Case 04 arms.

This is not a winner result. Combined availability improved task correctness
beyond both single-method arms in **one of six cases**, and that improvement
was only from `no` to `partial`.

## Case outcomes

| Case | Fructal Cap Design only | Superpowers only | Combined |
|---|---|---|---|
| 01 small implementation | Yes; final scope exact, but two incorrect intermediate edits and recovery | Yes | Yes |
| 02 response-only redesign | Yes | Yes | Yes |
| 03 doc correction | Yes | Yes | Yes |
| 04 local publication | No; stopped at read-only `.git` | No; stopped at read-only `.git` | Partial; pushed exact local remote ref through a temporary clone, but original workspace remained on `main` without the requested local branch |
| 05 one attempt | Yes | Yes | Yes |
| 06 Review diagnosis | Yes; used `PYTHONDONTWRITEBYTECODE=1` | Partial; left prohibited `__pycache__` | Partial; created then removed prohibited `__pycache__` |

Case 04 is materially confounded by the prospectively frozen
`workspace-write` sandbox mounting fixture `.git` metadata read-only. The
combined arm recovered safely enough to create the exact commit and local bare
remote ref, but its substitute clone meant the exact current-repository branch
outcome was not achieved. This was preserved rather than rerun.

## Static and manifested conflict

The evaluators agreed that static conflict existed in **12/18 assessments**,
covering Cases 01, 02, 04, and 05. They disagreed on all six assessments for
Cases 03 and 06:

- Evaluator 1: static conflict in 18/18;
- Evaluator 2: static conflict in 12/18.

The supported range is therefore **four to six of six case contracts**, with
four cases agreed. The disagreements concern whether proportionality pressure
in an exact documentation correction and mode-bound debugging discipline count
as contract conflict or merely correct task specialization.

No behavioral conflict had two-evaluator agreement. Evaluator 1 classified the
two Case 06 cache-writing arms as manifested conflict; Evaluator 2 classified
the same writes as task-boundary violations without method conflict. The file
effects are objective even though their conflict attribution is disputed.

No method-contract conflict caused an unnecessary user question or commit. The
strongest literal conflicts—mandatory question/approval/spec/commit gates
versus exact implementation or response-only boundaries—were resolved by task
instructions, usually correctly.

## Precedence and suppression

The clearest behavioral asymmetry was invocation, not final prose:

- Superpowers was read in **6/6 combined arms**.
- Fructal Cap Design was read in **1/6 combined arms**.
- In that one arm, Superpowers appeared first in the read command.
- Fructal Cap Design was not read in five combined cases, including the
  explicit Review-mode diagnosis.

Thus Superpowers dominated skill discovery and Fructal Cap Design was silently
suppressed at the invocation layer in five cases. Availability alone did not
produce composition.

Final-action precedence was usually the explicit task instruction. Evaluator
2 classified task-instruction precedence in 13/18 arms; Evaluator 1 did so in
8/18, instead classifying four combined arms as synthesis. Precedence agreement
was only 9/18, so claims beyond the read-order evidence should remain cautious.

## Complementarity

The strongest observed composition was Case 02, the only combined arm that
read both contracts. Fructal Cap Design supplied the Redesign/no-write ceiling,
constraint preservation, recovery, and actor continuity. Superpowers supplied
structured option comparison and verification discipline. The arm produced a
coherent response-only redesign without questions or writes.

That complementarity did not improve binary task correctness beyond the two
single-method arms; all three succeeded. Its value was coverage and structure,
not a uniquely correct outcome.

Across the other combined cases, apparent complementarity cannot be attributed
to both methods because Fructal Cap Design was not read.

## Redundancy and ceremony

The contracts overlap most in evidence-before-claim, verification, failure
inspection, and preservation. Evaluator 1 recorded three obligations as
explicitly redundant; Evaluator 2 expressed the same overlap narratively but
used other obligation statuses.

No arm created a design spec, implementation plan, or unnecessary commit despite
the generic Superpowers contracts. Explicit task instructions suppressed that
ceremony. Read and verification ceremony still had measurable cost.

Across the six compatible FSI-001 counters:

| Condition | Elapsed | Input tokens | Output tokens |
|---|---:|---:|---:|
| Fructal Cap Design only | 305.449 s | 608,614 | 10,914 |
| Superpowers only | 477.380 s | 1,019,027 | 16,127 |
| Combined | 566.055 s | 1,277,988 | 19,673 |

Combined totals were 88.675 seconds (18.6%) and 258,961 input tokens (25.4%)
above Superpowers only, and 260.606 seconds (85.3%) and 669,374 input tokens
(110.0%) above Fructal Cap Design only. Case 04 recovery dominates part of
that difference. Within cases, combined was slower than Fructal Cap Design
only in all six; it was slower than Superpowers only in three and faster in
three. These are descriptive costs, not causal efficiency estimates.

Older PPD token counters are excluded because their semantics differ.

## Severity and recovery

Both evaluators agreed on:

- **costly:** Fructal Cap Design-only Case 01, due to two incorrect
  implementations and extra verification/recovery;
- **costly:** combined Case 04, due to substitute-clone recovery, one failed
  commit attempt for missing identity, extra local writes, and an incomplete
  original-workspace result;
- **blocking:** both single-method Case 04 arms, because the sandbox blocked
  `.git` mutation and neither recovered; and
- **no scope-breaking severity:** neither evaluator used `scope-breaking`.

Case 06 had prohibited writes:

- Superpowers only left a bytecode cache, requiring deletion and a clean-state
  recheck.
- Combined generated the cache twice and removed it before handoff. Final state
  recovery did not erase the transient no-write violation.
- Fructal Cap Design only avoided the write by setting
  `PYTHONDONTWRITEBYTECODE=1` before reproduction.

Case 05 shows correctly resolved verification pressure: all arms used exactly
one generator attempt, preserved the mismatching artifact and attempt counter,
and reported `amber` versus expected `green` without corrective action.

## Obligation dataset

[`evaluation/obligations.jsonl`](evaluation/obligations.jsonl) contains all
445 evaluator obligation records with evaluator ID, anonymous arm label,
revealed condition, contract/method identity, contract availability, status,
evidence, consequence, and recovery cost.

The evaluators used different granularity:

| Evaluator | Obligations | Satisfied | Superseded | Suppressed | Duplicated | Violated |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 261 | 166 | 63 | 0 | 3 | 29 |
| 2 | 184 | 130 | 28 | 6 | 0 | 20 |

Counts are not averaged because the evaluators decomposed obligations
differently. Their original JSON remains authoritative.

## Stable ownership rules

The cases support these bounded rules:

1. The exact user task owns permitted writes, output boundary, and
   consequential intent.
2. Fructal Cap Design should own the maximum outcome mode and workflow
   continuity/recovery constraints.
3. Superpowers debugging, TDD, planning, and verification may operate inside
   that maximum outcome only when the explicit boundary permits their writes
   and gates.
4. Exact consequential authorization eliminates a duplicate branch-finishing
   or confirmation question.
5. One verification record should satisfy overlapping evidence obligations;
   duplicate wording is not additional assurance.
6. Skill discovery must load all co-relevant workflow contracts before one
   process skill establishes orchestration.

## Skill changes indicated by the cases

The first five rules can be compatibility ownership rules. The sixth requires
a Superpowers discovery-contract change or equivalent platform orchestration:
`using-superpowers` should not let its own first-read mandate silently suppress
another relevant workflow contract.

Two narrower changes are also supported:

- systematic debugging should explicitly suppress incidental bytecode/cache
  writes under a no-write Review boundary; and
- branch-finishing guidance should explicitly stop when the requester already
  specified and authorized the exact branch and local push consequence.

The cases do not show a need to weaken Fructal Cap Design's one-attempt,
no-write, exact-intent, or Review boundaries. They do suggest documenting that
other process skills operate inside the selected mode rather than beside it.

## Retrospective refinements

FSI-001 refines, but does not rewrite, the earlier PPD conclusions:

- “No blocking conflict” remains true for the earlier combined enclosure run,
  but it understated non-blocking contradiction, redundancy, and suppression.
- The earlier first-mover hypothesis was reproduced: Superpowers was first in
  every combined arm and Fructal Cap Design was fully read only once.
- The earlier combined arm's short duration cannot be treated as general
  efficiency. Across these six cases, combined elapsed time exceeded both
  condition totals.
- The earlier strong-written/weak-handoff and prose-reconciliation findings
  remain event-level observations specific to PPD-003; FSI-001 used no images
  and does not re-test renderer behavior.

## Remaining uncertainty

- There is one run per arm, one model, one fixed package order, and one CLI.
- Read order was not randomized.
- A skill description in the injected catalog may influence behavior without a
  full `SKILL.md` read; the 5/6 suppression count concerns observable reads.
- Evaluators disagreed materially on static conflict, behavioral conflict,
  precedence, severity language, and obligation granularity.
- The Case 04 sandbox confound prevented a clean test of branch-finishing
  ceremony under directly writable `.git`.
- No claim here generalizes beyond these six cases or establishes causal
  certainty.
