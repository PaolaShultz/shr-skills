# FSI-001 adversarial method composition

FSI-001 is a bounded, controlled experiment on how Fructal Cap Design and
Superpowers behave when separately available and available together. It is not
a winner test and does not repeat the SHR-DAW enclosure work.

The experiment has six deterministic local cases and three conditions per
case:

- Fructal Cap Design only;
- the complete Superpowers package only; and
- both packages together.

Every arm receives byte-identical case prompts. Each arm uses a fresh isolated
`HOME` and `CODEX_HOME`, a validated injected-skill catalog, no network task,
no image generation, and no real external effect. Two isolated evaluators
receive anonymized traces, outputs, fixtures, and contracts only.

The archive separates the prospective protocol, retrospective event evidence,
frozen inputs, fixtures, raw runs, evaluator outputs, calculations, and final
interpretation. Prior evaluation archives remain unchanged.

## Navigation

- [`protocol.md`](protocol.md): frozen prospective design and escalation rules
- [`retrospective/findings.md`](retrospective/findings.md): separate
  retrospective analysis
- [`retrospective/interactions.json`](retrospective/interactions.json):
  event-level interaction records
- [`frozen-inputs/`](frozen-inputs/): packages, prompts, contracts, schemas,
  mappings, environment, and manifests
- [`fixtures/`](fixtures/): six deterministic repository templates
- [`runs/`](runs/): eighteen arm archives
- [`evaluation/`](evaluation/): harness, tests, and two evaluator archives
- [`results.md`](results.md): bounded findings
- [`calculations.json`](calculations.json): machine-readable calculations
- [`SHA256SUMS`](SHA256SUMS): final archive checksums

The protocol commit and completed-results commit are recorded in
`results.md` after execution.
