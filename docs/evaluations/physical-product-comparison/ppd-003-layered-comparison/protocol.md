# PPD-003 combined-arm and layered-comparison protocol

Status: **prospectively frozen before combined-arm execution**

Date: 2026-07-25

This protocol extends the frozen `ppd-002` execution comparison without
modifying or reinterpreting its artifacts or `39/38/38` package result. It
prospectively defines:

1. a fourth execution arm with Fructal Cap Design and Superpowers available
   together;
2. a blind comparison of the two existing prompt-author outputs; and
3. a two-evaluator, five-layer blind assessment of all four execution arms.

The primary purpose is attribution: distinguish prompt-author quality, written
design reasoning, image-generation instruction quality, renderer compliance,
delivery/QC behavior, and complete-package quality.

This is a documented first methodological pass, not an independent study,
replicated benchmark, physical-product acceptance test, or broad ecosystem
comparison.

## Prospective boundary and observed starting state

The experiment orchestrator may inspect the existing repository and frozen
`ppd-002` artifacts before this protocol is committed. The orchestrator must
not inspect a new combined-arm result before this protocol commit is pushed.

The supplied expected repository HEAD was
`69c37665d2689fb11c5c2f38702daa37d70e8c74`. Direct inspection found the clean
local `main` branch and `origin/main` at the later commit
`0e075f5e37963702b0bdb3054256a7af3dd430f1`. The two intervening commits add
the second-pass human-review and cross-renderer boundaries that this task
explicitly requires the orchestrator to read:

- `4ceef0d429c158a8574f7a5b40ec46ac0b28be83`;
- `0e075f5e37963702b0bdb3054256a7af3dd430f1`.

The later clean state is therefore the observed and preserved protocol
baseline. No history is reset or rewritten.

## Frozen sources, package identities, and execution settings

### Common execution state

- Canonical experiment repository:
  `https://github.com/PaolaShultz/shr-skills.git`
- Pre-protocol repository commit:
  `0e075f5e37963702b0bdb3054256a7af3dd430f1`
- Pre-protocol repository tree:
  `34b7ae4b10f701171a02b449fdffd4f3714d7900`
- SHR-DAW source:
  `https://github.com/PaolaShultz/shr-daw`
- SHR-DAW commit:
  `927eb05888951f9955c7d46e856ef7208149bc00`
- Codex CLI:
  `0.145.0`
- Text model:
  `gpt-5.6-sol`
- Reasoning effort:
  `high`
- Collaboration mode:
  default, with subagents available only on explicit request
- Approval policy:
  never
- Execution sandbox:
  workspace-write, matching `ppd-002`
- Shell network:
  restricted by the Codex execution sandbox, matching `ppd-002`
- Built-in web access:
  available
- Built-in image-generation capability:
  available
- Built-in image inspection:
  available
- Output requirement:
  exactly one final image file, as required by the unchanged shared prompt
- Harness intervention after launch:
  prohibited

The combined arm may use standard built-in system skills and tools exposed by
Codex CLI `0.145.0`, including image generation. The only permitted
non-system user-skill packages are the two packages frozen below.

### Fructal Cap Design package

- Source commit:
  `5efbd8a586cfed7538141e25111a247127ca092d`
- Source commit tree:
  `361890504097e25412ced11959dfe39b0299abe8`
- `skills/fructal` tree:
  `84468248f463946a523b7c2c700ea5ab106ede5b`
- Complete exported directory tar SHA-256:
  `832114bb47dd05a605fb7b0715a51ec8434b0a0addb603b7da05e058c8690a94`
- `SKILL.md` SHA-256:
  `11b11556b3092f3fa14b7dd81ecfd96bde635433cff20141d87603f36c48f171`
- `agents/openai.yaml` SHA-256:
  `954569a78cd42bf75a38825119eafb44078bb5b641deb94cf641bdd543148cba`
- Export contents:
  `skills/fructal/SKILL.md` and
  `skills/fructal/agents/openai.yaml`

The complete package must be exported from the frozen commit, not copied from a
later working tree.

### Superpowers package

- Source:
  `https://github.com/obra/superpowers.git`
- Source commit:
  `6efe32c9e2dd002d0c394e861e0529675d1ab32e`
- Source commit tree:
  `7c813df3731f36c37f91a9cf9ead2c466a64aac5`
- Complete exported repository tar SHA-256:
  `e0e91f2a8852557c1aca2ca3bf80edd5964b4df9b302a0489808ef7d418ce956`

The complete repository package at that commit must be installed into the
isolated combined environment. A partial selection of Superpowers skills is
not an equivalent condition.

### Frozen shared execution prompt

- Canonical source:
  `../ppd-002-discovery/control/prompt.md`
- PPD-003 archival copy:
  [`frozen-inputs/shared-execution-prompt.md`](frozen-inputs/shared-execution-prompt.md)
- SHA-256:
  `33a15b008bc6c75c5ac963f7d05d7541204244f416726efb9e414f21264c1049`

The combined arm receives only those exact bytes as its task input. The
orchestration request that created this protocol is method-aware but is not an
experimental-arm input. The harness must not prepend, append, annotate,
improve, regenerate, or wrap the task prompt.

## Combined-arm isolation and ownership contract

Create a fresh temporary experiment root outside every Git repository. Use
distinct isolated `HOME` and `CODEX_HOME` directories for:

- the combined execution arm;
- prompt-quality evaluator 1;
- prompt-quality evaluator 2;
- layered evaluator 1; and
- layered evaluator 2.

Authentication material may be copied into a temporary isolated
`CODEX_HOME` only to authorize the model call. It must never be printed,
included in a checksum manifest, copied into an evaluator workspace, or
archived. Destroy it with the temporary experiment root after the sanitized
public archive is complete.

Under the exact combined launch environment, run a diagnostic before the task
execution. Inspect the actual available-skill payload recorded by Codex, not a
directory listing or flag name. A valid boundary contains:

- built-in system skills;
- `fructal`;
- the complete Superpowers skill set; and
- no other non-system user skill.

An invalid diagnostic stops the combined launch while the harness boundary is
repaired. It does not permit modifying the task prompt.

The combined ownership contract is:

- The unchanged product prompt owns the requested deliverables and
  physical-product scope.
- Fructal Cap Design owns constrained-workflow analysis, actors, constraint
  sources, continuity, recovery, accessibility, service state,
  untouched-state verification, and the implicit Redesign boundary.
- Superpowers owns skill discovery, brainstorming discipline, structured
  concept comparison, and verification before completion.
- Neither method may modify SHR-DAW or another target repository.
- Files created in the disposable output workspace are requested experimental
  deliverables, not target-system modification.
- Explicit task instructions override conflicting generic workflow behavior.
- No arm-specific wrapper may be added to the task prompt.
- The archive records actual skill invocation order and any interaction,
  redundancy, conflict, omission, or blocking behavior.

Skill availability is not counted as skill use. Invocation order and behavior
must be recovered from the sanitized trace.

## Combined-arm run discipline

1. Verify the protocol commit exists on `origin/main`.
2. Create and verify the fresh combined environment.
3. Verify the two package exports and shared prompt hashes.
4. Run the actual available-skill diagnostic under the combined launch
   boundary.
5. Launch one fresh Codex execution with the exact frozen prompt.
6. Make no harness intervention after launch.
7. Preserve unexpected choices, omissions, retries, corrections, or failures
   as evidence.
8. Do not rerun the combined arm merely because its product decision, image,
   or score is unfavorable.
9. A transport failure before model execution may be retried only if the
   failed attempt produced no model result or image; preserve and report the
   failure.
10. Preserve the raw final response byte-for-byte before creating any reading
    copy.

## Prompt-author comparison

The comparison uses only:

- original rough request:
  `../ppd-002-discovery/prompt-authoring/bootstrap-input.md`;
- no-user-skill prompt:
  `../ppd-002-discovery/prompt-authoring/no-user-skill-prompt.md`;
- Superpowers prompt:
  `../ppd-002-discovery/prompt-authoring/superpowers-prompt.md`.

Two independent no-user-skill evaluators receive the rough request and both
prompt outputs under new anonymous labels. They must not receive repository
access, method identities, previous scores, execution outputs, either mapping,
or external sources.

Each evaluator scores each prompt from 0 to 4 on:

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

For each prompt, each evaluator must report:

- preserved meaning;
- useful additions;
- unsupported additions;
- premature decisions;
- omissions;
- distortions;
- likely downstream consequences;
- ten raw scores;
- total score out of 40; and
- confidence.

Longer prompts receive no automatic advantage. The final comparison reports
both raw evaluations, per-dimension means, totals, evaluator disagreement, and
confidence without forcing consensus.

## Exact image-generation instruction extraction

For the no-user-skill, Superpowers-only, Fructal Cap Design-only, and combined
arms, extract instructions only from the sanitized execution traces. Do not
reconstruct instructions from response prose or images.

Every call record must retain:

- arm's anonymous and later revealed identity;
- call order;
- call ID when available;
- timestamp when available;
- exact tool name and namespace;
- exact verbatim argument payload;
- referenced image path or preceding-call relationship;
- whether the call is an initial render or correction;
- tool-reported saved path when available;
- resulting archived image SHA-256; and
- provenance trace SHA-256.

The Superpowers-only arm's initial render and correction are one instruction
chain. Both calls must be preserved and evaluated. The final image hash belongs
to the correction result; the initial output relationship remains explicit.

## Four-arm anonymization and evaluator isolation

Generate a new randomized four-arm mapping after this protocol is committed.
Do not reuse `A`, `B`, or `C`, and do not use labels that reveal method
identity. Use the same four-arm mapping across all five evaluation layers.

Generate a separate two-candidate mapping for prompt-author evaluation.

For each mapping:

1. assign labels using operating-system cryptographic randomness;
2. write a sealed mapping outside every evaluator workspace;
3. record its SHA-256 and creation timestamp before evaluator launch;
4. keep it unavailable to both evaluators;
5. freeze both valid evaluator outputs;
6. only then copy the sealed mapping into the public case and create a
   separate reveal record.

The two evaluators within a comparison receive byte-equivalent inputs and
instructions. They use separate isolated homes, Codex homes, workspaces, and
sessions. They may not communicate, inspect the canonical repository, browse
external sources, identify methods, or inspect previous scores.

For the layered assessment, each evaluator is staged so unavailable evidence
is physically absent:

- Layer 1 workspace: written designs only.
- Layer 2 workspace: written designs and exact image-instruction chains, but no
  images.
- Layer 3 workspace: written designs, exact image-instruction chains, and
  images.
- Layer 4 workspace: raw/reading responses, image files, delivery metadata, and
  sanitized trace-derived tool chronology.
- Layer 5 workspace: complete delivered packages and the original frozen
  40-point rubric.

Each stage is a fresh ephemeral session under the evaluator's isolated home.
The same anonymous mapping is used in every stage. A rendered-image stage is
valid only if the trace confirms direct inspection of all four images. If an
evaluator transport fails or omits required image inspection, preserve it as an
invalid attempt and run a fresh replacement under the same frozen evidence
before mapping reveal.

## Layer 1: written design only

Images and image-generation instructions are absent.

Score 0 to 4 on:

1. hardware fidelity;
2. constraint-source clarity;
3. airflow completeness;
4. fan interaction;
5. connector motion;
6. maintenance, recovery, and untouched-state preservation;
7. musician interaction and repeated use;
8. evidence honesty;
9. verification quality;
10. internal design coherence.

Report one evidence statement per score, total out of 40, confidence, most
consequential strength, most consequential weakness, and material internal
contradictions.

## Layer 2: written design to image instruction

Images are absent. Compare every exact image-generation call in the arm's chain
with the written design.

Score 0 to 4 on:

1. selected product geometry;
2. screen size, orientation, and operator relationship;
3. connector count, type, placement, and cable motion;
4. intake, airflow, cooler, NVMe, and exhaust representation;
5. controls and musician-facing elements;
6. service boundaries and removable parts;
7. materials, proportions, and visual identity;
8. explicit prohibitions against invented features;
9. uncertainty and concept-status honesty;
10. instruction clarity and renderability.

Report one evidence statement per score, total out of 40, confidence, every
material omission/change/addition, and the effect of any correction chain.

## Layer 3: image-model compliance and error attribution

Compare each rendered image with both the exact instruction chain and written
design. Inspect every image directly.

For every discrepancy, assign one or more of:

- `DESIGN_ORIGIN`: the written design itself is inconsistent, unsupported, or
  incomplete.
- `IMAGE_PROMPT_ORIGIN`: the written design is clear, but the image instruction
  omits, weakens, or changes it.
- `RENDERER_ORIGIN`: the image instruction clearly specifies the requirement,
  but the image model omits, invents, or contradicts it.
- `DELIVERY_QC_ORIGIN`: the rendered defect was visible, but the executing
  agent delivered it without correction or disclosure.
- `INDETERMINATE`: available evidence cannot distinguish the source.

Multiple labels are allowed only when causality is genuinely shared. Explain
every label next to its evidence. Attribution totals count label assignments,
not unique discrepancies; multi-labelled discrepancies contribute once to each
assigned origin.

Score 0 to 4 on:

1. overall form;
2. display and controls;
3. native ports and power;
4. airflow and fan direction;
5. component-stack plausibility;
6. service features;
7. consistency across views;
8. absence of invented hardware;
9. legibility and technical communication;
10. agreement with the final written design.

Report one evidence statement per score, total out of 40, confidence,
discrepancy-level attribution, and the most consequential compliance defect.

## Layer 4: delivery and QC behavior

Report, with trace or artifact evidence:

- whether the executing agent inspected its generated image;
- whether it noticed contradictions;
- whether it corrected them;
- whether correction improved the result;
- whether remaining limitations were disclosed;
- whether exactly one final image was delivered; and
- whether prose, image links, filenames, and archived artifacts agree.

This layer is qualitative and is not converted into a numeric vector unless a
later prospective amendment defines one. It therefore has no rubric-profile
similarity percentage.

## Layer 5: complete delivered package

Apply the original frozen 40-point `ppd-002` package rubric to all four arms:

1. hardware fidelity;
2. constraint-source clarity;
3. airflow completeness;
4. fan interaction;
5. connector motion;
6. maintenance and recovery;
7. musician interaction;
8. evidence honesty;
9. verification quality;
10. visual-product coherence.

The anchors and equal weights remain exactly those in
`../ppd-002-discovery/blind-evaluation/prompt.md`.

Report raw scores, one evidence statement per score, total out of 40,
image-to-text agreement, unsupported or inconsistent claims, most
consequential strength and weakness, confidence, and conditional real-musician
preference. Do not overwrite, merge with, or reinterpret the earlier
`39/38/38` result.

## Rubric-profile similarity

For every layer represented by an `n`-dimensional 0-to-4 score vector, compute
every pairwise arm profile:

```text
similarity_percent =
100 × (1 - sum(abs(score_a_i - score_b_i)) / (4 × n))
```

Dimensions:

- prompt-author quality: `n = 10`, one candidate pair;
- Layer 1 written design: `n = 10`, six four-arm pairs;
- Layer 2 image-instruction quality: `n = 10`, six four-arm pairs;
- Layer 3 image-model compliance: `n = 10`, six four-arm pairs;
- Layer 5 complete package: `n = 10`, six four-arm pairs.

Report evaluator-specific values and their arithmetic mean. Preserve enough
precision to reconstruct the calculation and publish displayed percentages to
one decimal place.

Call the result only **rubric-profile similarity**. It is not a percentage of
identical methods, causal equivalence, semantic identity, or proof of
interchangeability. A high percentage may reflect rubric ceiling effects,
coarse integer scoring, a strong shared prompt, correlated evaluator judgment,
or dimensions that omit important product differences.

## Combined-condition interpretation

Reveal method identities only after all valid evaluator outputs are frozen.
Then assess whether the combined condition shows:

- complementarity;
- redundancy;
- instruction conflict;
- extra discovery coverage;
- stronger untouched-state expression;
- better image prompting;
- better renderer-error detection;
- stronger final QC;
- greater token or time cost; or
- no material improvement.

Do not declare a winner from one aggregate score. Rank findings by:

1. consequence;
2. evaluator agreement; and
3. recovery cost.

Keep observed trace/artifact evidence separate from evaluator judgment and
orchestrator inference.

## Public archive contract

The completed case should contain:

- this prospective protocol and its frozen prompt copy;
- package/source hash evidence;
- combined-arm exact prompt, raw response, normalized reading copy, final
  image, metadata, token/duration record, available-skill diagnostic,
  invocation sequence, sanitized compressed trace, exact image-call chain, and
  checksums;
- prompt-author comparison inputs, evaluator instructions, both raw
  evaluations, metadata, sealed mapping, and reveal;
- exact image-instruction extraction for all four arms;
- anonymous per-layer inputs or reconstructable manifests;
- both evaluators' raw staged outputs and consolidated reading copies;
- evaluator metadata and valid-image-inspection evidence;
- sealed four-arm mapping and later reveal;
- formula, raw calculated tables, means, disagreements, confidence,
  attribution totals, and interpretation; and
- one complete `SHA256SUMS` manifest covering every preserved artifact except
  the manifest itself.

Raw final responses remain byte-preserved. Reading copies may change only
local image links to point to the archived image. Document every changed line
or prove the link-only diff.

Sanitized traces must remove at least:

- `encrypted_content`;
- `base_instructions`;
- `internal_chat_message_metadata_passthrough`;
- credentials and authentication data.

Do not publish authentication files, encrypted model content, provider base
instructions, internal message metadata, tokens, device codes, private-project
identity, or private-project paths.

## Claim boundary

This case may support:

- a verified combined execution under two available method packages;
- comparative prompt, design, image-instruction, renderer, QC, and package
  judgments for this frozen case;
- discrepancy-level attribution grounded in the archived evidence;
- evidence of complementarity, redundancy, conflict, omission, or additional
  cost within this run; and
- a stronger reusable experimental boundary.

It does not prove:

- general superiority, inferiority, equivalence, or interchangeability of any
  method;
- causal attribution from one stochastic execution and one image sample;
- that an evaluator's origin label is physically true;
- that any image faithfully represents buildable geometry;
- enclosure fit, cooling, noise, electrical safety, manufacturability,
  serviceability, or musician acceptance;
- independent validation; or
- completion of the pending `ppd-001` evaluation, broad ecosystem comparison,
  second-pass human review, cross-renderer control, or later rough-request
  discovery comparison.

Those reserved tasks remain untouched.

## Completion gates

Before publication:

1. verify all frozen hashes and mapping hashes;
2. validate the complete checksum manifest;
3. verify every local Markdown link;
4. parse every sanitized JSONL trace;
5. scan public artifacts for credentials, authentication data, device codes,
   private paths, private-project identity, and provider-private fields;
6. run `git diff --check`;
7. run `scripts/validate.sh`;
8. run `tests/test-validation.sh`;
9. run `tests/test-live-eval-harness.sh`;
10. inspect the complete diff;
11. commit the completed archive and documentation;
12. push `main` to the verified `origin`; and
13. confirm local `HEAD` equals `origin/main`.

If the experiment exposes another confound, append an amendment or result
boundary. Do not edit this frozen protocol after the combined result is seen.
