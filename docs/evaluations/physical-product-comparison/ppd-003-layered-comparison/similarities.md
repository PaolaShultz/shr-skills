# Rubric-profile similarities

For every ten-dimensional scored layer:

```text
similarity_percent =
100 × (1 - sum(abs(score_a_i - score_b_i)) / (4 × 10))
```

The values below are evaluator 1 / evaluator 2 / mean.

| Pair | Layer 1 | Layer 2 | Layer 3 | Layer 5 |
|---|---:|---:|---:|---:|
| Superpowers–control | 97.5 / 97.5 / 97.5 | 85.0 / 87.5 / 86.25 | 77.5 / 87.5 / 82.5 | 97.5 / 97.5 / 97.5 |
| Superpowers–Fructal Cap Design | 100 / 95.0 / 97.5 | 90.0 / 92.5 / 91.25 | 80.0 / 87.5 / 83.75 | 97.5 / 87.5 / 92.5 |
| Superpowers–combined | 95.0 / 92.5 / 93.75 | 85.0 / 85.0 / 85.0 | 82.5 / 85.0 / 83.75 | 97.5 / 95.0 / 96.25 |
| Control–Fructal Cap Design | 97.5 / 97.5 / 97.5 | 90.0 / 95.0 / 92.5 | 92.5 / 95.0 / 93.75 | 95.0 / 85.0 / 90.0 |
| Control–combined | 97.5 / 95.0 / 96.25 | 95.0 / 92.5 / 93.75 | 90.0 / 87.5 / 88.75 | 95.0 / 97.5 / 96.25 |
| Fructal Cap Design–combined | 95.0 / 92.5 / 93.75 | 85.0 / 87.5 / 86.25 | 92.5 / 82.5 / 87.5 | 95.0 / 87.5 / 91.25 |

Prompt-author Superpowers–no-user-skill similarity was 92.5% / 90.0% /
91.25%.

These are only rubric-profile similarities. Coarse integer scores, a shared
prompt, correlated evaluator judgment, and ceiling effects can inflate them.
They are not percentages of identical methods, causal equivalence, or proof of
interchangeability. Exact unrounded calculations are in
[`calculations.json`](calculations.json).
