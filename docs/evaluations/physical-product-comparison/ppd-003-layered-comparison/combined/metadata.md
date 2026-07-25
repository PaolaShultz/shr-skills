# Combined arm metadata

## Frozen launch

- Condition: Fructal Cap Design and Superpowers available together.
- Prompt: [`prompt.md`](prompt.md), SHA-256
  `33a15b008bc6c75c5ac963f7d05d7541204244f416726efb9e414f21264c1049`.
- Model: `gpt-5.6-sol`.
- Reasoning effort: `high`.
- Harness command reported `codex-cli 0.145.0` immediately before launch.
- The session's own `session_meta.cli_version` unexpectedly records `0.144.5`.
  This mismatch is preserved as an observed harness-metadata confound; the arm
  was not rerun.
- Approval policy: `never`.
- Sandbox: workspace write, shell network disabled.
- Started: `2026-07-25T07:31:17.498765434+02:00`.
- Ended: `2026-07-25T07:44:37.119979149+02:00`.
- Elapsed: 799.61 seconds.
- Maximum resident set size: 197,436 KiB.
- Exit status: 0.
- Session ID: `019f97c1-a329-76f0-9aca-83ee30eec59a`.

## Token accounting

The final trace token event reports:

| Field | Tokens |
|---|---:|
| Input | 4,755,553 |
| Cached input | 4,548,096 |
| Output | 30,110 |
| Reasoning output | 18,948 |
| Total | 4,785,663 |

These are provider-reported cumulative trace values, not an independently
metered billing calculation.

## Deliverables

- Byte-preserved response:
  [`raw-response.md`](raw-response.md), SHA-256
  `f35749522366e6c7f90a73a921fb9ff3cc57fd45ac4023a888aebf0b47e0a392`.
- Link-normalized reading copy:
  [`reading-response.md`](reading-response.md). Its only changes are the three
  image targets, from the disposable absolute path to `concept-board.png`.
- Final image:
  [`concept-board.png`](concept-board.png), 1536 × 1024 RGB PNG, SHA-256
  `c32a834bce8f867280477b567bb70b44bacdc9219e29e36754f21744099aed69`.
- Exactly one PNG existed in the requested output workspace at completion.
- Sanitized compressed trace: [`session.jsonl.gz`](session.jsonl.gz).
- CLI event stream: [`execution-events.jsonl`](execution-events.jsonl).
- Exact image call: [`image-generation/call-01.json`](image-generation/call-01.json).
- Exact image result:
  [`image-generation/call-01-result.json`](image-generation/call-01-result.json).

## Runtime capability request

The arm requested installation of the GitHub plugin while researching. The
tool returned `completed: false` and `user_confirmed: false`; no plugin was
installed. The isolated environment still contained only the frozen
Fructal Cap Design package and Superpowers package as non-system user skills.
The rejected request is retained in the trace as execution behavior.

## Trace sanitation

The public trace removes these object fields recursively:
`encrypted_content`, `base_instructions`,
`internal_chat_message_metadata_passthrough`, credential and authorization
fields, access and refresh tokens, identity and device codes, client secrets,
API keys, and authentication tokens. The image result payload remains so that
the image-generation call chain can be reconstructed.
