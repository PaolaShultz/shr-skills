# Fructal Cap Design 1.3.0 evaluation record

Version 1.3.0 adds concrete trigger symptoms to the description, a
protected-property step, a table of candidate moves, and a per-mode report
shape. This record compares it with 1.2.0 and with no skill at all. It is a
development regression record, not an independent study or affected-user
acceptance test.

All runs used Codex CLI 0.172.0 with `gpt-6.2-astra` as both executor and
separate judge, over the same 29 development contract cases. Each directory
retains its exact skill, runner, cases, and output schema under `inputs/`, plus
responses, events, fixture snapshots, judgments, metadata, and `SHA256SUMS`.

## Arms

- `full-no-skill`: the executor received only the user request, with no skill
  embedded or installed (`--no-skill`). The judge scored against the 1.2.0
  contract, the same rubric as the 1.2.0 arm.
- `full-1.2.0`: the published 1.2.0 skill.
- `full-candidate-pre-fix`: the first 1.3.0 candidate, before the Redesign
  verification fix described below.
- The `*-final` directories used the released 1.3.0 text. Its only later
  change was `metadata.version` moving from `1.2.0` to `1.3.0`.

## Full matrix

| Arm | Passed | Failures |
| --- | --- | --- |
| No skill | 20/29 | All nine Redesign cases |
| 1.2.0 | 28/29 | `consequential_confirmation` |
| 1.3.0 candidate, pre-fix | 26/29 | `consequential_confirmation`, `complex_multi_actor_continuity`, `discovery_workflow_positive` |

Every no-skill Redesign was judged incomplete, chiefly because none contained a
concrete verification scenario; one also lacked a recovery path. With no
skill, the model passed every Review, Implement, authorization, read-boundary,
and non-trigger case. Many of those prompts state their boundaries explicitly,
so this matrix cannot show what the skill's authority guidance adds on less
explicit requests or weaker models.

## Disagreements and repeats

Pass counts combine the full-matrix run with the repeat directories.

| Case | 1.2.0 | 1.3.0 |
| --- | --- | --- |
| `complex_multi_actor_continuity` | 4/4 | pre-fix 2/4; final 4/4 |
| `consequential_confirmation` | 0/4 | pre-fix 2/4; final 1/4 |
| `discovery_workflow_positive` | 2/4 | pre-fix 2/4; final 0/1 |
| `small_routine_redesign` | 4/4 | final 3/4 |

The pre-fix candidate's Redesign report shape named "the verification plan"
without asking it to cover unrelated state. It omitted that untouched-state
check twice and, once, the whole plan. The released Redesign bullet now asks for
concrete checks of the changed paths and of unrelated state that must stay
untouched. The final skill then passed that case 4/4 and six other Redesign
cases once each (`redesign-final`).

`consequential_confirmation` fails across versions for the same reason: the
executor correctly stops and asks once for the exact archive and recipient,
then also states that the harness fixture is read-only and has no notification
mechanism. The judge treats that environment statement as an added
prerequisite. This is a rubric issue, not yet corrected, because changing the
judge would change every arm's scoring.

`discovery_workflow_positive` failures on both versions are the judge requiring
an `inference` label for a stated assumption. The one final
`small_routine_redesign` failure left a flagged placeholder instead of
inventing a restore location absent from the fixture; three further runs of
each version passed.

`transport-outage-final` records eight runs that all timed out during a
temporary Codex service outage. A trivial Codex request succeeded immediately
afterward, and `repeats-final` reran the same cases. These timeouts carry no
behavioral evidence.

## Supplementary check

Before the Codex runs, a separate model family executed three realistic tasks
(3-D Secure checkout, a session-expiry code review, and on-call escalation)
twice with each skill. Every 1.3.0 response stated the protected property, and
some derived unstated ones, such as one charge per order; no 1.2.0 response
did. A discovery probe with ten competing skill descriptions selected the
skill for a duplicate-charge retry request in two of two 1.3.0 runs and zero of
two 1.2.0 runs, with identical results on the other nine requests. Those
outputs were not archived; this is design evidence only.

## Limits

Cases are development-authored, and single runs vary; the repeat counts are
small. One model served as both executor and judge. Only two cases test
installed-skill discovery. The no-skill arm measures contract conformance
against a rubric that model never saw, so some baseline failures reflect the
contract's specific deliverable requirements rather than general quality. No
real payments, notifications, affected-user tests, or cross-model
effectiveness comparison occurred.
