# Fructal Cap Design 1.3.1

Version 1.3.1 corrects one Redesign regression in 1.3.0. All six cap
questions and every mode, authority, and evidence rule are unchanged.

1.3.0 introduced its table of candidate moves with "check each against the
constraint's source." In the full-matrix rerun of the released skill, the model
read that as license to propose only what the current system already has:
asked to redesign a draft-hiding control, it made the restore action
conditional ("if immediate restoration is supported") instead of proposing it.
1.3.1 says instead to confirm that each move still satisfies the constraint's
source, and that in Redesign a move the current system lacks belongs in the
proposal, stated as something to build.

The skill grows from 1,498 to 1,520 words.

## Evidence

On the 29-case development matrix with `gpt-6.2-astra` as executor and judge,
the released 1.3.0 passed 28 under the corrected judge; its one failure was
`small_routine_redesign`, which it passed 3/5 overall against 1.2.0's 4/4. The
1.3.1 text passed that case 5/5 and every other Redesign case and two evidence
and mode cases once each (10/10). On the full matrix, 1.3.1 passed 28 of 29.
The one failure was a harness false negative: the executor ran the verifier
successfully, then chained a `git status` that failed in the fixture, and the
harness read the chained exit code. The harness now requires the verifier's
own success marker instead, with regression tests for a chained, failed, and
missing verifier. Under the fixed harness both Implement verifier cases passed
3/3.

See the [1.3.0 evaluation record](../docs/evaluations/live-contract/fructal-1.3.0/),
which now also covers 1.3.1. These are development cases, not a held-out
benchmark, and they do not establish cross-model reliability or affected-user
acceptance.
