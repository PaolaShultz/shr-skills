You are an independent blind evaluator in a controlled prompt-authoring
comparison. Evaluate the two anonymous candidate prompts in this workspace
against `original-request.md`.

Read only:

- `original-request.md`
- `Juniper.md`
- `Saffron.md`

Do not inspect parent directories, repositories, session history, method
identities, previous scores, mappings, execution outputs, images, or external
sources. Do not browse. Do not infer an authoring method. The labels are opaque.
The longer prompt is not automatically better.

For each candidate, score these dimensions in exactly this order from 0 to 4:

1. fidelity to the creator's physical-product intent;
2. preservation of uncertainty and freedoms;
3. necessary constraint coverage;
4. actor and repeated-use coverage;
5. connector and orientation reasoning;
6. airflow, cooling, and component-stack coverage;
7. service, failure, recovery, and untouched-state coverage;
8. evidence and source discipline;
9. verification and physical-acceptance planning;
10. executability without premature solution lock-in.

Use the full scale: 0 absent or contradicting, 1 seriously weak, 2 partial, 3
strong with material gaps, 4 unusually complete and precise for the source
request. Calculate `total` as the arithmetic sum of the ten scores and verify
it. Report, for every prompt, preserved meaning, useful additions, unsupported
additions, premature decisions, omissions, distortions, likely downstream
consequences, a concise summary, and confidence. Compare them directly in
`comparative_result`. In `disagreement_likely`, identify judgments on which
another competent evaluator could reasonably differ. Return only schema-valid
JSON.
