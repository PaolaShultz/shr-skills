# Treatment metadata

- Run ID: `ppd-001-treatment`
- Fixed order: control first, treatment second
- Run start: `2026-07-24T20:18:54+02:00` (`Europe/Zagreb`)
- Treatment freeze completion: `2026-07-24T20:25:48+02:00`
  (`Europe/Zagreb`)
- Exact text model identifier: `unavailable`
- Text model family requested by the run: `GPT-5-family`
- Reasoning level: `unavailable`
- Image tool identifier: `image_gen.imagegen`
- Underlying image model identifier: `unavailable`
- Image size/quality/seed/sampling controls: `unavailable`
- Original protocol commit:
  `b9eec17fd7886e96299075a420b856a80c32d104`
- Repository commit immediately before treatment:
  `38d126cabc36d9e6d28d0b0d527c6db3adeac08f` (verified as local `HEAD`
  before treatment)
- Frozen Fructal Cap Design source commit:
  `5efbd8a586cfed7538141e25111a247127ca092d`
- Verified source and installed skill SHA-256:
  `11b11556b3092f3fa14b7dd81ecfd96bde635433cff20141d87603f36c48f171`
- Frozen SHR-DAW source commit:
  `927eb05888951f9955c7d46e856ef7208149bc00`

## Mode and boundary confirmations

- Fructal Cap Design was explicitly invoked in **Redesign** mode.
- The complete canonical skill body was read from
  `/home/shome/p/shr-skills/skills/fructal/SKILL.md` only after its hash passed.
- The installed copy at `/home/shome/.codex/skills/fructal/SKILL.md` was also
  hash-verified, and both bodies matched the frozen SHA-256.
- SHR-DAW and its hardware were not modified.
- The control artifact directory was not read, listed, opened, summarized, or
  inspected.
- No other enclosure-design conversation, control response, control image,
  control metadata, score, or user reaction was inspected.
- The protocol and amendment were not read until the written design, image
  prompt, generated image, and exact local image copy were frozen.
- No treatment score or comparison was produced.

## Tool and network availability

- Shell and filesystem: available
- Web browser/search transport: available
- Direct network access through `curl`: available
- Image generation: available
- Git and existing `origin` remote: available
- Image original as an exact filesystem artifact: available
- Model-internal identifiers and image-generation parameters: unavailable

## Interruptions, retries, failures, and context

- Interruption: none.
- User steering during execution: none.
- Context loss or compaction: none observed.
- Image-generation retries: none.
- Aesthetic correction generations: none.
- Image-generation request count: exactly one substantive request.
- Image-generation transport/tool failure: none.
- Source-access failure: the browser transport returned cache-miss errors for
  all four immutable raw GitHub URLs at the frozen SHR-DAW commit. The identical
  URLs were then read successfully through direct `curl`; no source revision
  changed.
- Instruction-read truncation: one combined shell output containing several
  workflow skill files was truncated by the tool output limit. The relevant
  files were re-read completely in separate bounded reads before design work
  continued.
- The official Raspberry Pi configuration page was accessible. Its generic KMS
  rotation guidance was not treated as proof for the unknown GPIO display.
- First staged-diff check failure: five newly staged Markdown records had one
  extra empty line at EOF. Only those empty lines were removed; frozen design
  prose and the exact fenced image prompt were unchanged. The byte-level
  post-normalization design hash is recorded in `artifact-manifest.md`.
- First private-data scan attempt: failed because the Git regex engine rejected
  an inline case-insensitivity flag. A compatible scan was run afterward.
