# Fructal Cap Design 1.3.0

Version 1.3.0 makes the method easier to find and gives it concrete design
moves. All six cap questions and every mode, authority, and evidence rule from
1.2.0 are unchanged. The canonical skill, ChatGPT demo, and host packages are
synchronized.

- The description names typical constraints and symptoms: re-entering data
  after a timeout or reauthentication, duplicate requests or charges after a
  retry, approvals stuck between teams, and work users believe is gone.
- Each constraint is stated as the property it protects. That property is
  fixed; the mechanism enforcing it is open to redesign unless a source fixes
  it too.
- A short table offers candidate moves that keep a constraint while removing
  its friction, to be checked against the constraint's source.
- A Report section leads with the outcome and states each mode's parts. A
  Redesign's verification plan checks both the changed paths and unrelated
  state that must stay untouched.
- The live harness gains `--no-skill`, which gives the executor only the user
  request so a no-skill baseline can be judged against the same contract.

The skill grows from 1,104 to 1,498 words.

## Evidence

On the 29-case development matrix with `gpt-6.2-astra` as executor and judge,
no skill passed 20, 1.2.0 passed 28, and the first 1.3.0 candidate passed 26.
Every no-skill failure was a Redesign, chiefly lacking concrete verification.
Repeats traced the candidate's extra failure to a Redesign verification gap,
which the released text corrects; the final skill then passed that case 4/4.
Two test defects shared by both versions were then corrected: the judge now
knows the harness sandbox, and the discovery case requires the evidence
distinction it actually exercises. The affected cases then passed 4/4 on 1.2.0
and 8/8 on 1.3.0, and eight authority and mode cases passed under the new judge.

See the [1.3.0 evaluation record](../docs/evaluations/live-contract/fructal-1.3.0/)
for every archive, repeat, and limit. These are development cases, not a
held-out benchmark, and they do not establish cross-model reliability or
affected-user acceptance. The final skill was not rerun on the full matrix.
