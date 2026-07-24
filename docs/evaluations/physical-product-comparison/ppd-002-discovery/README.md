# PPD-002 three-arm execution comparison

Status: **three execution arms frozen and blindly evaluated**

Date: 2026-07-24

This case asks how the same model responds to a Raspberry Pi enclosure task
under three user-skill conditions:

1. no user skill;
2. Superpowers only; and
3. Fructal Cap Design only.

It extends the original two-arm protocol after prompt-author contamination was
identified in `ppd-001`. This is a documented case study, not an independent
study or a general benchmark.

## Frozen inputs

- SHR-DAW repository:
  [`PaolaShultz/shr-daw`](https://github.com/PaolaShultz/shr-daw)
- SHR-DAW commit:
  [`927eb05888951f9955c7d46e856ef7208149bc00`](https://github.com/PaolaShultz/shr-daw/commit/927eb05888951f9955c7d46e856ef7208149bc00)
- Fructal Cap Design source commit:
  [`5efbd8a586cfed7538141e25111a247127ca092d`](https://github.com/PaolaShultz/shr-skills/commit/5efbd8a586cfed7538141e25111a247127ca092d)
- Fructal Cap Design `SKILL.md` SHA-256:
  `11b11556b3092f3fa14b7dd81ecfd96bde635433cff20141d87603f36c48f171`
- Superpowers source commit:
  [`6efe32c9e2dd002d0c394e861e0529675d1ab32e`](https://github.com/obra/superpowers/commit/6efe32c9e2dd002d0c394e861e0529675d1ab32e)
- Shared execution prompt SHA-256:
  `33a15b008bc6c75c5ac963f7d05d7541204244f416726efb9e414f21264c1049`
- Codex CLI: `0.145.0`
- Model: `gpt-5.6-sol`
- Reasoning effort: `high`

The no-user-skill prompt author received the creator's rough request and wrote
the shared execution prompt. All three execution arms then received a
byte-identical copy.

## Isolation recovery

The first attempted clean prompt-author run used an isolated `CODEX_HOME` but
retained the normal `HOME`. Its actual developer payload still listed
Superpowers from `/home/shome/.codex/superpowers`, and the run invoked
Superpowers.

That result was preserved as a Superpowers prompt-authoring arm. It was not
mislabelled as the neutral control.

The recovered boundary isolated both `HOME` and `CODEX_HOME`. A diagnostic
using the same boundary returned `NONE` for available non-system skills. The
three execution workspaces were then checked separately:

| Arm | Diagnostic result |
| --- | --- |
| No-user-skill control | `NONE` |
| Superpowers | Superpowers skills only |
| Fructal Cap Design | `fructal` only |

Each execution also used a separate `CODEX_HOME`, so sessions, memories, and
state could not flow between arms. All three began concurrently. Direct
`git clone` failed under the same sandbox DNS restriction in every arm; each
continued through commit-pinned web inspection without harness intervention.

## Blind result

The evaluator used no user skills, did not have the mapping, inspected the
three anonymized responses and images, and applied the frozen ten-dimension
rubric.

| Revealed arm | Blind label | Score | Tokens | Duration |
| --- | --- | ---: | ---: | ---: |
| Superpowers only | A | 39/40 | 208811 | 16m 21s |
| Fructal Cap Design only | B | 38/40 | 245523 | 15m 51s |
| No-user-skill control | C | 38/40 | 197454 | 11m 25s |

The evaluator explicitly treated the one-point spread as within judgment
uncertainty. This run does **not** show that Fructal Cap Design outperformed
either alternative.

### Material differences

- **Superpowers only:** strongest integrated written engineering argument and
  the only seven-inch DSI-style baseline without the control's separate
  display-power path. Its technical cutaway contradicted the written airflow
  path and depicted the cooler inaccurately.
- **Fructal Cap Design only:** strongest image-to-text agreement, compact
  packaging, explicit fan ownership and fail-full-speed behavior, and the only
  backlight-after-soft-shutdown check. Its assumed four-inch display created a
  repeated-use/readability risk, and screen replacement plus reassembly-state
  preservation were underdeveloped.
- **No-user-skill control:** strongest musician-facing concept through the
  seven-inch display, eight controls, replaceable legends, optional touch, and
  separate screen cassette. Its assumed HDMI/USB display introduced a
  two-supply and internal-HDMI routing problem not fully represented in the
  image or connector summary.

### Shared miss

All three arms described service and reassembly, but none defined a formal
untouched-state check that inventories cable routes, connector seating,
fasteners, fan direction, gaskets, switch settings, and software/storage state
before opening and compares them after reassembly.

This is especially material for the Fructal Cap Design arm because
before/after and untouched-state verification is an explicit capability of the
skill. The treatment loaded the correct frozen skill and selected Redesign
mode, yet did not fully express that contract in its result.

## Interpretation

**Observed:** All three responses scored between 38 and 39. The generated
shared prompt was already detailed enough to require evidence separation,
complete hardware and connector treatment, failure analysis, recovery, and a
comparison record.

**Inference:** This run has a strong ceiling effect. A capable model executing
the detailed neutral prompt covered most of the rubric without a user skill,
leaving little room for a one-run incremental advantage.

**Observed:** Fructal Cap Design used about 24% more tokens than the control and
about 18% more than Superpowers. It finished about 39% slower than the control
and about 3% faster than Superpowers.

**Inference:** In this case, the added Fructal Cap Design execution cost did
not produce a higher blind score. It did produce a particularly coherent
exterior result and several recovery details, but it also failed to surface one
of its own explicit verification requirements.

**Open question:** Results may differ when the same three execution conditions
receive the creator's rough request directly, without a separate model turning
it into a comprehensive 981-word prompt first.

## Artifacts

- [`prompt-authoring/`](prompt-authoring/) preserves the common bootstrap input,
  the no-user-skill prompt, the accidentally produced Superpowers prompt, and
  both provenance records.
- [`control/`](control/) preserves the no-user-skill prompt, response, image,
  metadata, and sanitized compressed session trace.
- [`superpowers/`](superpowers/) preserves the Superpowers-only execution.
- [`treatment/`](treatment/) preserves the Fructal Cap Design-only execution.
- [`blind-evaluation/`](blind-evaluation/) preserves the anonymized judge inputs,
  rubric prompt, evaluation, revealed mapping, metadata, and sanitized
  compressed session trace.

Within each execution arm, `raw-response.md` preserves the frozen response with
its original temporary image path. `design-response.md` changes only that image
link to the archived `concept-board.png`. `SHA256SUMS` covers every preserved
artifact except the checksum file itself. The session traces retain observable
messages, tool activity, and timing while omitting encrypted model content,
provider base instructions, and internal message metadata.

The images are concept evidence only. No result proves physical fit, cooling,
noise, electrical safety, manufacturability, or affected-musician acceptance.
