# ZIT cross-renderer extension

Status: **eight primary renders complete and technically validated**

This non-destructive extension executes the four completed PPD-003 product
designs through Z-Image-Turbo (ZIT) in ComfyUI. It adds renderer evidence
without modifying any frozen source design, instruction, image, evaluation,
score, or blind mapping.

## Two separate questions

**Set A — exact transfer** sends each initial full image-generation instruction
to ZIT byte-for-byte. No generic suffix, negative prompt, translation,
reordering, or other wrapper is added. It asks whether a visual defect follows
the same instruction across renderers.

**Set B — ZIT-adapted** uses one standalone prompt per already-frozen design,
written before any ZIT image was seen. Each prompt restructures the same product
facts for ZIT and maps substantive clauses back to the frozen design and
initial image instruction. It asks how well ZIT communicates the same design
when renderer-specific prompt structure is allowed.

Set B is not a fifth workflow-method arm and does not repair an upstream design.
The Superpowers source correction is retained in
`prompts/superpowers-source-correction-evidence.txt`, but it is not applied as
an edit to an unrelated ZIT image. Its already-frozen requirements are
consolidated into the standalone adapted prompt.

## Frozen common controls

- Canvas: 1536×1024 landscape, batch size 1
- Seed: `25072026`
- Steps: 12
- CFG: 1
- Model shift: 4.0
- Sampler: `dpmpp_2m_sde_heun_gpu`
- Scheduler: `simple`
- Denoise: 1
- LoRA: none
- Server mode: deterministic
- Attempts: one per condition and set; no aesthetic retries or cherry-picking

Two identical RTX 3060 servers may execute jobs concurrently. Physical GPU 0
uses port 8188 and physical GPU 1 uses port 8189. GPU assignment changes only
execution capacity; prompts, model files, workflows, seed, and sampling
controls are identical.

The seed is a ZIT reproducibility control only. It is not claimed to correspond
to another image model's latent seed.

## Archive map

- `manifest.json` — machine-readable job, prompt, workflow, and output record
- `provenance.json` — source conditions, runtime, tooling, and model hashes
- `frozen-settings.json` — common controls and retry/inspection policy
- `prompts/exact-transfer/` — four byte-exact Set A prompts
- `prompts/adapted/` — four frozen standalone Set B prompts
- `mappings/` — source-to-adapted clause maps
- `workflows/jobs/` — eight exact ComfyUI API graphs
- `logs/` — submission, history, generation, and retry evidence
- `outputs/set-a/` and `outputs/set-b/` — one PNG per condition

## Evidence boundary

These files are concept renders. They are not CAD, thermal, manufacturability,
acoustic, EMC, electrical, fabrication, regulatory, or physical-validation
evidence. This thread performs technical file and provenance validation only:
no semantic scoring, winner selection, or visual repair.

## Technical result

All eight planned primary renders completed: four Set A and four Set B. Every
archived output is a unique, decodable 1536×1024 RGB PNG associated with one
frozen condition, prompt, workflow, server submission, and ComfyUI history
record. Primary generation count: 8. Infrastructure failure count: 0. Retry
count: 0. Visual inspection and semantic scoring performed in this thread: no.
