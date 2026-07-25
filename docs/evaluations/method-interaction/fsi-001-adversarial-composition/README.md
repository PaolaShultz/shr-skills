# FSI-001 adversarial method composition

FSI-001 is a bounded, controlled experiment on how Fructal Cap Design and
Superpowers behave when separately available and available together. It is not
a winner test and does not repeat the SHR-DAW enclosure work.

The completed experiment has six deterministic local cases and three
conditions per case:

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
- [`evaluation/obligations.jsonl`](evaluation/obligations.jsonl):
  evaluator-level obligation dataset
- [`results.md`](results.md): bounded findings
- [`calculations.json`](calculations.json): machine-readable calculations
- [`SHA256SUMS`](SHA256SUMS): final archive checksums

Prospective protocol commit:
`c73ed745652ec849476fcb75150597efc4343294`. The completed-results commit is
the commit containing this final archive and is reported at handoff.
