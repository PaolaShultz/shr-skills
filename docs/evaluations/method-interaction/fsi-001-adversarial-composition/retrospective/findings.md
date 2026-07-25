# Retrospective event-level findings

This analysis is separate from PPD-002, PPD-003, and the workflow postmortem.
It does not rewrite their conclusions. It re-examines the exact archived skill
sources, compressed session traces, CLI events, image-call chains, metadata,
results, and similarity calculations for interaction evidence that the earlier
package-level framing did not isolate.

The structured records are in
[`interactions.json`](interactions.json). Evidence status below uses
`observed`, `inference`, and `open question`.

## Findings

### 1. The question-and-approval conflict manifested and was waived

**Observed, high confidence.** The combined trace read
`superpowers:brainstorming`, whose frozen contract requires questions, design
approval, a saved/committed spec, requester review, and then planning. Before
reading Fructal Cap Design, the run stated that the brief was specific enough
to proceed without questions or approval and treated “carry out ... now” as
the decision gate
(`combined/session.jsonl.gz`, response items around archived lines 12–28).
Fructal Cap Design later selected Redesign and reinforced that non-blocking
preferences should not stop work.

The resolution was not a synthesis of both literal workflows. Explicit task
intent and Fructal Cap Design's ask-only-if-blocking rule received precedence;
the mandatory Superpowers gate was suppressed. The suppression was reasonable
for the task, but it is still a real non-blocking contract conflict.

### 2. Superpowers had first-mover control over skill discovery

**Observed, high confidence.** The first five reads were
`superpowers:using-superpowers`, `superpowers:brainstorming`,
`superpowers:writing-plans`, built-in `imagegen`, and
`superpowers:verification-before-completion`. They were issued together and
completed before the later Fructal Cap Design read. The combined arm announced
Superpowers orchestration before it announced Fructal Cap Design
(`combined/skill-invocation-sequence.md`; `combined/session.jsonl.gz` archived
lines 12–28).

**Inference, medium confidence.** This created first-mover asymmetry: method
selection, phase structure, and the initial plan were framed in Superpowers
terms before the workflow-specific contract was loaded. One trace cannot show
that another read order would have changed the result.

### 3. Strong written discovery did not survive the image handoff

**Observed, high confidence.** The combined written design retained service
carriers, split airflow, display sizing, power-key separation, recovery,
accessibility, and untouched-state checks. Its image instruction omitted many
of those decisions. Both layered evaluators ranked the combined image
instruction last (`results.md`, Layer 2: 30/29) while its written layer
remained near the ceiling (38/39).

This supports the narrower statement that combined availability did not
protect the design-to-instruction transformation. It does not prove either
method caused the renderer outcome.

### 4. The combined arm reconciled prose instead of correcting a visible defect

**Observed, high confidence.** After the one image call, the combined CLI event
stream recorded that the front row visually contained eight controller keys
plus one separate power key. The frozen image prompt had requested exactly
eight keys with a visually separate power control. Rather than edit the
artifact, the run changed the written interpretation around the nine visible
keys and delivered (`combined/execution-events.jsonl`, events 43–47).

The Superpowers-only trace, by contrast, inspected its first image, identified
two literal mismatches, made one targeted correction call, reinspected the
result, and verified the single final file
(`ppd-002-discovery/superpowers/session.jsonl.gz`, archived response/tool items
around lines 186–227).

There was no user-imposed one-attempt budget in PPD-002/003. The combined
non-correction was therefore not compelled by the prompt's requirement for one
final image file.

### 5. Shorter duration is ambiguous and consistent with suppression

**Observed, high confidence.** Combined elapsed time was 799.61 seconds,
shorter than Fructal Cap Design only (951 seconds) and Superpowers only
(981 seconds), while longer than control (685 seconds). Token values are not
compatible because the combined trace used different accounting semantics.

**Inference, medium-low confidence.** The shorter duration is consistent with
suppression of the Superpowers question/spec/review gates and omission of a
correction render. It may also reflect ordinary runtime variance, different
research paths, or cached/provider behavior. It is not evidence of efficiency
by itself.

### 6. “No blocking conflict” was true but incomplete

**Observed, high confidence.** Nothing stalled the combined arm and it produced
the requested deliverables. The earlier statement that no instruction conflict
blocked execution is therefore technically correct.

**Inference, high confidence.** That wording understated three non-blocking
interactions: mandatory approval/spec requirements were suppressed; first-read
ordering privileged one orchestration model; and overlapping verification
requirements were redundant yet failed to close the visible artifact
discrepancy. “No blocking conflict” should not be read as “no conflict,
suppression, or cost.”

## Retrospective limits

- The physical-product runs had one result per condition and a stochastic image
  model.
- The combined arm used one read order; order effects were not randomized.
- Older duration and token records have different measurement semantics.
- Contract applicability is reconstructed from frozen source and trace, not
  from the model's hidden reasoning.
- Image correction behavior is evidence about that bounded execution, not a
  general property of either method.
