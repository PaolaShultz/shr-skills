# Evaluator identity reveal

The identity reveal was created only after both evaluator outputs were frozen.

- Evaluator 1 output SHA-256:
  `8cae97ff855e3f05a6e6c8601b8f9d2c5a74a5104717b7f7ea53efd15914b1d9`
- Evaluator 2 output SHA-256:
  `3d7a82a0c6d6bf34ece0a1709ef21c812900e378b5d107de87e95160e9979fa3`

Contract identities:

- Contract A: Fructal Cap Design
- Contract B: Superpowers

Arm identities:

| Case | Kappa | Lambda | Mu |
|---|---|---|---|
| 01 small implementation | combined | Fructal Cap Design only | Superpowers only |
| 02 response-only redesign | Superpowers only | combined | Fructal Cap Design only |
| 03 doc correction | Fructal Cap Design only | Superpowers only | combined |
| 04 local publication | combined | Superpowers only | Fructal Cap Design only |
| 05 one attempt | Superpowers only | Fructal Cap Design only | combined |
| 06 Review diagnosis | Fructal Cap Design only | combined | Superpowers only |

This reproduces the mapping frozen in
`frozen-inputs/evaluator-mapping.json`; it does not modify evaluator judgments.
