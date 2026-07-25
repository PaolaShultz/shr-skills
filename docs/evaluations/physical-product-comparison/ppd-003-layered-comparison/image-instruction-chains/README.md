# Exact image-generation instruction chains

These files were mechanically extracted from the sanitized PPD-002 and PPD-003
execution traces. They do not reconstruct prompts from prose or images.
Every `call-*.json` retains the verbatim image-tool arguments, including
referenced-image provenance. Every paired result file retains the call ID,
timestamp, completion status, revised prompt, saved-path provenance, and
SHA-256 of the generated PNG decoded from the trace result.

| Arm | Call order | Role | Call ID | Resulting PNG SHA-256 |
|---|---:|---|---|---|
| PPD-002 no-user-skill control | 1 | Initial and final render | `call_GHjxiyoiz9h1LcVZLKuJ0o11` | `6d9a5c651903bd05e5b0b6db2f2472292db182b843752a10dfee7b6f1939be68` |
| PPD-002 Superpowers | 1 | Initial render | `call_VZVEkcoNTAzI5GsANusURMZv` | `1b8d205e2b3302f6d4c1e3765c35597596cdd4c422cef8255535fc457cd908cb` |
| PPD-002 Superpowers | 2 | Surgical correction | `call_d8C7yi1eQ6m7Q0lMscOanCoY` | `2c814677ab444079c4bc04cd9c6ceebd28575c31b3a80ec7fcc12d691503944f` |
| PPD-002 Fructal Cap Design | 1 | Initial and final render | `call_3mTkMlWl3GM9dfaUqa5JJBkY` | `a97c6c7e62fbfdf055a5e00a051417accb6edfc9a91e429204c8fc727247b9c7` |
| PPD-003 combined | 1 | Initial and final render | `call_reGoDxEU6CMx6UoR83uHmFEa` | `c32a834bce8f867280477b567bb70b44bacdc9219e29e36754f21744099aed69` |

Directories:

- [`control/`](control/) — PPD-002 no-user-skill control.
- [`superpowers/`](superpowers/) — PPD-002 Superpowers initial render and
  correction chain.
- [`treatment/`](treatment/) — PPD-002 Fructal Cap Design.
- [`combined/`](combined/) — PPD-003 combined condition.

The PPD-002 Superpowers final archived image is the result of call 2. The
intermediate call-1 image is preserved inside the existing sanitized trace and
is identified by its decoded hash above; it is not substituted for the final
package image.
