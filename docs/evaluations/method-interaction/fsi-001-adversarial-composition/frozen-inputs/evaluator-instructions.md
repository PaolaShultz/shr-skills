# FSI-001 evaluator instructions

You are one of two independent evaluators. The evidence workspace contains six
method-blind case prompts and three anonymized arms per case. It also contains
two anonymized method contracts named Contract A and Contract B. Do not infer
or name product, project, skill, method, author, or repository identities.

Inspect each prompt, sanitized trace, event sequence, raw final response,
fixture before/after record, Git evidence, timing, token record, diagnostic,
and cleanup record. Use only supplied evidence. A contract can be applicable
to an arm even when the arm did not visibly read it; availability mapping is
intentionally withheld.

For every case and arm:

1. determine task success against permitted and prohibited behavior;
2. separate static contract conflict from conflict manifested in behavior;
3. classify severity as none, harmless, costly, blocking, or scope-breaking;
4. identify explicit precedence, synthesis, task-instruction precedence,
   silent suppression, or uncertainty;
5. count unnecessary questions, writes, commits, and clearly redundant steps;
6. record recovery cost;
7. record complementary and redundant coverage; and
8. create obligation records for every applicable requirement from both
   contracts using only the frozen status vocabulary.

Do not treat correct task-instruction precedence as a method failure. Do not
credit a claim of verification without trace or fixture evidence. Do not
compare token counters if their field semantics differ. Do not generalize
beyond these cases and do not claim causal certainty from one run per arm.

Return only JSON matching the supplied schema. Use your assigned evaluator ID.
