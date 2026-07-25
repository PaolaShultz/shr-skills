# Results and interpretation

## Outcome

The fourth arm completed with Fructal Cap Design and Superpowers available
together. It delivered one final 1536 × 1024 image after 799.61 seconds. The
valid launch diagnostic showed both requested user-skill packages and no other
non-system user skills.

The combined condition added material value in written discovery, service
state, recovery, and untouched-state expression, but not in image prompting,
renderer-error correction, or final aggregate package quality. It therefore
does not justify a winner claim.

## Layer scores

Each cell is evaluator 1 / evaluator 2 / mean.

| Condition | Layer 1 written | Layer 2 instruction | Layer 3 renderer compliance | Layer 5 package |
|---|---:|---:|---:|---:|
| No user skill | 39 / 39 / 39.0 | 32 / 32 / 32.0 | 30 / 33 / 31.5 | 38 / 38 / 38.0 |
| Superpowers | 38 / 38 / 38.0 | 36 / 35 / 35.5 | 35 / 34 / 34.5 | 39 / 39 / 39.0 |
| Fructal Cap Design | 38 / 38 / 38.0 | 34 / 34 / 34.0 | 33 / 35 / 34.0 | 38 / 36 / 37.0 |
| Combined | 38 / 39 / 38.5 | 30 / 29 / 29.5 | 30 / 28 / 29.0 | 38 / 39 / 38.5 |

The previous PPD-002 39/38/38 result remains unchanged. Layer 5 is a new
four-arm evaluation with new labels and two new evaluators.

## Error attribution

Across both Layer 3 evaluations, origin-label assignments total:

| Origin | Evaluator 1 | Evaluator 2 | Combined assignments |
|---|---:|---:|---:|
| `DESIGN_ORIGIN` | 0 | 1 | 1 |
| `IMAGE_PROMPT_ORIGIN` | 11 | 10 | 21 |
| `RENDERER_ORIGIN` | 4 | 3 | 7 |
| `DELIVERY_QC_ORIGIN` | 5 | 11 | 16 |
| `INDETERMINATE` | 1 | 0 | 1 |

These are multi-label assignments, not mutually exclusive defect counts.
The strongest agreed result is that more loss occurred between written design
and image instruction than in the written design itself. Renderer stochasticity
was real but explains fewer assigned discrepancies than prompt omission and
delivery/QC combined.

## Combined-condition interpretation

Ranked by consequence, agreement, and recovery cost:

1. **Image-prompt omission:** both evaluators scored the combined instruction
   chain last. It dropped the removable carriers, service boundaries, internal
   stack, split airflow, exact display sizing, separate power key, and some
   connector decisions from a strong written design.
2. **Visible control contradiction:** the prompt demanded exactly eight keys;
   the renderer produced nine visually identical keys. The written design
   required eight controller keys plus a separate power key. The arm inspected
   the image but reconciled prose instead of correcting the render.
3. **Complementary discovery:** the combined written record retained strong
   uncertainty handling, service recovery, accessibility, repeated-use checks,
   and untouched-state verification. Layer 1 remained at the ceiling.
4. **Redundancy without blocking conflict:** both methods reinforced evidence
   discipline and verification. No instruction conflict blocked execution, but
   repeated verification language did not protect the image handoff.
5. **QC comparison:** only the Superpowers arm performed a full
   inspect–correct–reinspect image loop. The combined arm detected renderer
   deviations but did not render a correction.
6. **Cost:** combined elapsed time was 13:19, between the PPD-002 control
   (11:25) and the two method arms (15:51 and 16:21). Its trace reports
   4,785,663 cumulative tokens, far above the earlier metadata counters, but
   the combined trace also records an unexpected internal CLI version and
   different accounting semantics, so token values are not directly
   comparable.

## Prompt-author result

The Superpowers-authored prompt scored 37/39 (mean 38.0), versus 36/37
(mean 36.5) for the no-user-skill prompt. The narrow advantage came from
evidence traceability and acceptance planning, with an explicit penalty for
workflow over-specification. See
[`prompt-author-evaluation/`](prompt-author-evaluation/).

## Boundaries

The result supports a workflow conclusion, not a product verdict: preserve the
strong written design, then run an explicit design-to-image coverage check and
a post-render discrepancy gate. A polished image cannot recover constraints
omitted from its prompt, and inspection without corrective action is not the
same as QC closure.
