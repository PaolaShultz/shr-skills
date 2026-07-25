# Blind prompt-author comparison

Two isolated no-user-skill evaluators compared Juniper and Saffron against the
same original rough request. Both ranked Juniper narrowly higher.

| Prompt condition | Evaluator 1 | Evaluator 2 | Mean |
|---|---:|---:|---:|
| Superpowers prompt author | 37 | 39 | 38.0 |
| No-user-skill prompt author | 36 | 37 | 36.5 |

The result is not “longer is better.” Both evaluators credited the
no-user-skill prompt with greater compactness and solution freedom. They
credited the Superpowers prompt with stronger evidence traceability,
machine-comparable recording, and measurable acceptance planning, while
penalizing its fixed artifact schema and presentation conventions as possible
workflow over-specification.

Raw records:

- [Evaluator 1](evaluator-1/evaluation.json)
- [Evaluator 2](evaluator-2/evaluation.json)
- [Original and anonymous inputs](inputs/)
- [Frozen evaluator prompt](evaluator-prompt.md)
- [Output schema](output-schema.json)

The evaluators agreed on the direction but differed on magnitude by one point.
Their rubric-profile similarity between the two prompt score vectors was
92.5% and 90.0%, mean 91.25%.
