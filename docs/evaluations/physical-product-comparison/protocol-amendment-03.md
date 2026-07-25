# Protocol amendment 03: separate prompt, design, and rendering evidence

Status: **recorded for the next work session; no additional run executed**

Date: 2026-07-24

This amendment records a post-evaluation limitation in `ppd-002`, a fourth
combined execution condition, and an interpretation principle that emerged
from the full experiment thread. It does not change the frozen artifacts or
blind scores.

## Attribution limitation

**Reported:** The creator judged the test incomplete because prompts were not
evaluated as outputs in their own right. Scoring only the final response and
picture can collapse a method's reasoning, its image-generation instruction,
and the image model's compliance into one result.

**Observed:** The `ppd-002` blind evaluator scored written design reasoning
across nine dimensions and final visual-product coherence as the tenth. It
also discussed image-to-text agreement separately. It did not independently
score:

1. the prompt-author's transformation of the creator's rough request;
2. the written product design before image generation;
3. the instruction sent to the image generator; and
4. the rendered image's compliance with that instruction and the written
   design.

**Observed:** This matters in the existing result. The Superpowers-only arm
lost its visual point because its cutaway contradicted the written airflow path
and cooler geometry. The no-user-skill arm lost its visual point partly because
the picture omitted display-power and routing consequences described in prose.
Those contradictions are real defects in the delivered artifact, but the
current aggregate does not establish whether each originated in design
reasoning, image prompting, or stochastic image generation.

**Inference:** The `38/40`, `39/40`, and `38/40` scores remain valid for the
submitted final packages under the frozen rubric. They are weaker evidence for
comparing the underlying methods themselves.

## Required layered evaluation

The next analysis should preserve each layer and score it separately:

| Layer | Primary question | Evidence |
| --- | --- | --- |
| Rough request → authored prompt | What important meaning, constraints, actors, uncertainties, and freedoms were preserved, added, distorted, or lost? | Original request and frozen prompt-author outputs |
| Prompt → written design | Did the execution discover and resolve the requested physical workflow without relying on render quality? | Execution prompt, research trace, and written response |
| Written design → image instruction | Did the image instruction faithfully encode the selected design, ports, airflow, service boundaries, and prohibited inventions? | Exact image-generation request recovered from the execution trace |
| Image instruction → rendered image | Did the image model comply, omit, invent, or contradict? | Exact image instruction and generated image |
| Complete delivered package | Does the combined prose-and-image artifact remain coherent and useful? | Final response and image together |

The same blind mapping and equal evidence access should be used within each
layer. A renderer error should still count against the delivered package, but
it should not silently become evidence that the workflow method reasoned
incorrectly.

## Fourth execution condition

**Reported:** Fructal Cap Design and Superpowers have been described as
complementary rather than opposing technologies.

**Inference:** A comparison containing either one alone but not their
combination cannot test that claim.

A fourth arm is therefore reserved:

> Fructal Cap Design plus Superpowers, with no other user skills available.

It is not to be executed in this work session. Before execution, freeze:

- the exact source commit and hash of both skill packages;
- which skill owns discovery, mode selection, planning, execution, and
  verification;
- their invocation order and how conflicting instructions are resolved;
- whether the arm receives the existing `ppd-002` shared prompt for direct
  execution comparability or participates in a later rough-request discovery
  comparison;
- the exact model, reasoning effort, tools, time boundary, and image allowance;
- a diagnostic proving that both intended packages, and no other user skills,
  are available; and
- the layered evaluation rubric above.

The most comparable immediate extension is to give the combined arm the
existing byte-identical `ppd-002` execution prompt. A later discovery study
should begin from the creator's rough request and include all intended
conditions prospectively.

## “A million bees stung me”

The Croatian expression *milijun me pčela ubolo* carries two kinds of
information at once:

1. the exaggeration indicates that there were many bees or many stings; and
2. the exaggeration reports the person's internal experience: it felt like a
   million.

Applied to this experiment thread, the first reading is the observable record:
multiple prompt-contamination discoveries, isolation repairs, reruns, frozen
artifacts, comparison arms, image contradictions, and evaluation limitations.

The mapping is structural, not emotional: a sting does not stand for an error.
The creator reported enjoying the work, its accomplishments, and the way the
collaboration repeatedly corrected itself.

The second reading therefore reveals the pattern beneath the event count:
mistakes became evidence, corrections strengthened the method and experiment,
and identifying a confound was productive progress rather than defeat.

**Inference:** Both readings matter, but they answer different questions.
Counting turns, tokens, artifacts, or rubric points describes the outer
workflow. Reading the pattern explains the quality of the collaboration and
what its corrections accomplished.

The same principle applies to `ppd-002`: a final score can say `38/40` while a
second reading shows that the score does not isolate prompt authorship, design
reasoning, image instruction, and renderer behavior. Recognizing that hidden
layer is a successful self-correction, not evidence that the working experience
was negative.

## Next-session boundary

The next session may:

1. freeze a layered prompt/design/image rubric;
2. blindly evaluate the two existing prompt-author outputs;
3. extract and evaluate each existing image-generation instruction;
4. decide and freeze the combined-arm execution contract;
5. execute the combined arm only after those controls exist; and
6. append results without rewriting `ppd-002`.

It must not treat the existing one-point spread as method superiority or erase
the package-level result merely because attribution is incomplete.
