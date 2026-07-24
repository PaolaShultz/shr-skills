# Protocol amendment 01: prompt-author contamination

Status: **recorded after the control run was frozen and before its design
response or image was deliberately inspected**

Date: 2026-07-24

This amendment preserves a methodological issue identified in the conversation
that created the physical-product comparison. It does not rewrite the original
protocol, treatment expectations, neutral task, scoring rubric, or frozen
control output.

## Sequence

1. Fructal Cap Design was loaded in the thread used to understand the enclosure
   problem and create the first detailed image-design prompt.
2. The same method-loaded thread then created the prospective
   [physical-product comparison protocol](../../physical-product-comparison-protocol.md).
3. A fresh skill-off thread began the frozen `ppd-001-control` run.
4. While that run was still executing, the creator asked whether the quality of
   the supposedly neutral prompt had already been influenced by the loaded
   skill.
5. The prompt author agreed that this was real prompt-author contamination and
   separated the intended comparison into two different research questions.
6. The control run subsequently published commit
   [`d46ad38`](https://github.com/PaolaShultz/shr-skills/commit/d46ad38),
   but its design response and image were not deliberately opened in the
   method-loaded thread before this amendment was written.

The public repository timestamp establishes when this amendment entered the
project history. It cannot independently prove a negative claim about what a
person or model had seen.

## Evidence

**Provided:** The creator identified the issue directly:

> “YOU have skill loaded, did that interfere in prompt quality?”

**Observed:** The shared neutral task contains unusually explicit coverage of
the complete hardware stack, display rotation uncertainty, multi-part airflow,
NVMe cooling, connector access, serviceability, assumptions, risks,
measurements, and verification.

**Observed:** Those concerns correspond to capabilities explicitly present in
Fructal Cap Design, while the thread that composed the task had the complete
skill loaded.

**Inference:** The common brief is not independent of Fructal Cap Design. Both
arms still receive the same task, so the comparison remains controlled at the
prompt boundary, but it tests the incremental effect of executing the complete
skill on top of an already method-influenced brief.

**Reported:** Before writing this amendment, the method-loaded thread inspected
only repository status, commit metadata, artifact filenames, and the protocol
status diff. It did not open the frozen control design response or generated
image.

## What the first comparison can test

The current control/treatment pair can ask:

> Does executing Fructal Cap Design add material coverage or coherence beyond a
> strong physical-product brief already shaped by its author’s internalized
> use of the method?

This is a demanding incremental-execution test. A material treatment advantage
would remain useful evidence because the control already receives many
well-formed constraints.

The pair cannot cleanly ask:

> Does Fructal Cap Design independently discover important constraints that an
> ordinary response to the creator’s raw request would miss?

Requirements already embedded in the shared prompt cannot later be counted as
discoveries caused by the treatment.

## Second comparison required

Preserve and finish the first pair unchanged. Add a separate discovery pair
afterward:

1. use the creator’s original enclosure description as nearly verbatim as
   possible;
2. freeze one minimal shared wrapper before either discovery run;
3. run the control in a clean temporary environment where neither the skill
   body nor its metadata is available;
4. run the treatment with the frozen skill version;
5. keep model, reasoning level, sources, tools, budget, and output request
   equal;
6. do not allow either producing thread to read the rubric, other output, or
   this amendment before freezing its result;
7. score both outputs later in a separate blinded evaluation; and
8. label the first pair an **execution comparison** and the second pair a
   **discovery comparison**.

The creator’s raw description already contains genuine product constraints.
The discovery test should preserve them rather than deliberately making the
request worse.

## Evidence about internalization

**Inference:** The contamination itself is evidence that repeated use can
internalize the method’s questions strongly enough to improve ordinary problem
framing even when the author is trying to construct neutral instructions.

**Inference:** The response to discovering the contamination also resembles
the method’s recovery contract: retain the valid control, preserve history,
separate what it can prove from what it cannot, and add the missing comparison
without erasing completed work.

This is evidence of method influence and self-correction, not evidence that the
method produced a superior enclosure. The prompt author cannot serve as an
independent control, and favorable interpretation by the method’s creators
remains a conflict of interest.

## Claim boundary

This conversational episode supports:

- a documented example of method internalization;
- early detection of a comparison-design confound;
- preservation of a still-valid narrower experiment; and
- explicit recovery through a second, differently scoped comparison.

It does not establish:

- treatment superiority;
- independent validation;
- general improvement in scientific reasoning;
- physical validity of either enclosure; or
- absence of other contamination or stochastic differences.
