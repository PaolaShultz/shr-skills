# Physical-product design comparison protocol

Status: **first execution pair frozen with evaluation pending; three-arm
execution extension frozen and blindly evaluated**

This prospective protocol records how Fructal Cap Design is expected to affect
the design of a real Raspberry Pi music-workstation enclosure before either
comparison result is seen. Repository history timestamps the protocol; it is
not an academic preregistration or an independent study.

The comparison asks whether Fructal Cap Design contributes material design
coverage beyond what the same model produces from the same physical-product
brief without the skill.

## Frozen starting evidence

The first comparison is tied to:

- Fructal Cap Design source commit
  [`5efbd8a`](https://github.com/PaolaShultz/shr-skills/commit/5efbd8a586cfed7538141e25111a247127ca092d);
- `skills/fructal/SKILL.md` SHA-256
  `11b11556b3092f3fa14b7dd81ecfd96bde635433cff20141d87603f36c48f171`;
- SHR-DAW source commit
  [`927eb05`](https://github.com/PaolaShultz/shr-daw/commit/927eb05888951f9955c7d46e856ef7208149bc00);
- the official
  [Raspberry Pi 5 mechanical drawing](https://pip.raspberrypi.com/documents/RP-008347-DS);
- the official
  [Raspberry Pi 5 Active Cooler mechanical drawing](https://datasheets.raspberrypi.com/cooling/raspberry-pi-active-cooler-mechanical-drawing.pdf);
- the same model, image-generation capability, source access, and initial
  context in two fresh threads.

Record the exact model identifiers, date, tool versions, and any unavailable
source or capability when the runs occur. Later repository changes do not
retroactively change this first comparison.

## Expected Fructal Cap Design contribution

The following expectations are recorded before seeing either output.

Fructal Cap Design is expected to:

1. separate fixed hardware, thermal, electrical, connector, service, safety,
   musician, and visual constraints from inherited layout assumptions;
2. treat the musician, assembler, maintainer, Raspberry Pi, GPIO display,
   Active Cooler, NVMe base, case fan, cables, and connected equipment as
   affected actors or components;
3. make the complete motion coherent across normal use, cable connection,
   cooling, cleaning, fan failure, storage replacement, screen service, and
   repeated assembly;
4. preserve screen readability while considering rotation of the complete
   hardware stack instead of assuming that text orientation fixes connector
   orientation;
5. distinguish daily connectors, service connectors, and unused connectors
   rather than exposing every board port indiscriminately;
6. trace airflow past the display underside, Pi board, Active Cooler, and
   bottom-mounted NVMe instead of treating CPU temperature as the whole thermal
   problem;
7. retain access, cable bend radius, strain relief, fan ownership, acoustic and
   electrical noise, and physical measurements as explicit constraints;
8. preserve uncertainty about the exact display, driver rotation, NVMe base,
   standoffs, assembled dimensions, and secondary-fan control;
9. keep the result at concept and verification-plan status rather than
   presenting an image as validated CAD or thermal evidence; and
10. produce one coherent enclosure motion whose remaining difficulty belongs
    to the real hardware rather than accidental case geometry.

These are hypotheses about comparative behavior, not scored successes.

## Shared neutral task

Use the following task text unchanged in both fresh threads:

```text
Design the final physical enclosure concept for SHR-DAW, a compact Raspberry Pi
music workstation. Research and design only: do not modify repositories, create
fabrication-ready CAD, order parts, or change hardware.

Use these sources:
- https://github.com/PaolaShultz/shr-daw
- README.md
- docs/PI5_HEADROOM_PLAN.md
- docs/PI5_NVME_INSTALL.md
- docs/WORKSPACE_HANDOFF.md
- https://pip.raspberrypi.com/documents/RP-008347-DS
- https://datasheets.raspberrypi.com/cooling/raspberry-pi-active-cooler-mechanical-drawing.pdf
- https://www.raspberrypi.com/documentation/computers/configuration.html

Known stack:
- Raspberry Pi 5, 2 GB;
- official Raspberry Pi 5 Active Cooler;
- 480×320 GPIO-connected display above the Pi;
- bottom-mounted PCIe-to-NVMe base and 128 GB NVMe;
- 27 W USB-C power supply;
- one proposed small 5 V rear case fan.

The enclosure should look like a compact old analog amplified console refined
into a modern small digital mixer: a restrained, professional wedge rather than
a generic Raspberry Pi case or gaming computer. The display sits in a modestly
angled upper surface and faces slightly toward the seated musician.

The lower front face has a broad intake grille. Air should travel through the
gap between the screen and Pi, cool more than the CPU hotspot, reach the
bottom-mounted NVMe, and leave through a rear grille with the small case fan.
The rear body extends slightly into a low plinth that sits level with the table.

Connector placement is unresolved. One long Pi edge has four USB ports and
Ethernet. The adjacent short edge has USB-C power and two micro-HDMI ports.
Explore whether rotating the complete Pi/display/NVMe stack 180 degrees and
rotating the displayed content in software improves cable access. Do not assume
that the exact GPIO display supports rotation until its model and driver are
known.

The NVMe, fan, display, and necessary connectors must remain serviceable.
Do not invent exact component dimensions or ports when evidence is unavailable.

Produce:
1. a concise design rationale and selected orientation;
2. the proposed airflow, connector, cable, and service arrangement;
3. assumptions, risks, required measurements, and a verification plan; and
4. one polished concept presentation board containing a three-quarter exterior
   view, a cutaway airflow view, and a rear/side connector and service view.

Clearly label the image as a concept rather than validated CAD or thermal proof.
```

The shared task contains product requirements supplied before the comparison.
It intentionally does not request Fructal Cap Design's evidence vocabulary,
constraint-source analysis, lifecycle tracing, six-question test, or report
structure.

## Treatment and control

Start two fresh threads with no result or discussion from the other thread.

### Treatment wrapper

```text
Use $fructal in Redesign mode for the task below. Hold the Redesign
no-modification boundary and use image generation only for the requested concept
presentation.

[PASTE THE SHARED NEUTRAL TASK UNCHANGED]
```

Confirm that the loaded skill matches the frozen SHA-256 before the treatment
run. Save the complete prompt, text response, generated image, tool trace where
available, model identifier, and timestamp.

### Skill-off control wrapper

```text
Do not invoke, load, quote, or use Fructal Cap Design or another
workflow-design skill for this task. Complete the product-design task directly.
Image generation is allowed only for the requested concept presentation.

[PASTE THE SHARED NEUTRAL TASK UNCHANGED]
```

The control should run in an environment where the Fructal Cap Design body is
not available. A clean temporary skill environment is stronger than prompt-only
suppression because globally visible skill metadata can still influence
selection. Do not alter or delete the normal installed copy merely to create the
control.

## Run discipline

1. Freeze and archive the two exact prompts before either run.
2. Use fresh threads with equal source and image-tool access.
3. Keep model, reasoning level, tool permissions, and output budget equal.
4. Prefer random run order and do not give the second run feedback derived from
   the first.
5. Do not revise either output before comparison.
6. Preserve raw text and original images; record later annotations separately.
7. Rename the outputs `A` and `B` for an assessor who does not know which used
   the skill.
8. Score reasoning separately from render quality. Image-generation variance
   must not be mistaken for workflow-design quality.
9. Treat one pair as a case study. Prefer at least three paired runs before
   inferring a repeatable model-level effect.

## Scoring

Score every dimension from 0 to 4 using only material present in the output:

| Dimension | 0 | 2 | 4 |
| --- | --- | --- | --- |
| Hardware fidelity | Invents or contradicts the stack | Mostly correct with gaps | Correctly preserves the complete known stack and unknowns |
| Constraint-source clarity | Treats preferences as facts | Some constraints are distinguished | Fixed, chosen, inferred, and open constraints remain distinct |
| Airflow completeness | Decorative vents only | CPU path is plausible | Display, Pi, cooler, NVMe, intake, exhaust, and recirculation are coherent |
| Fan interaction | Ignores the two fans | Mentions interaction | Addresses flow direction, control ownership, noise, failure, and obstruction |
| Connector motion | Ports are cosmetic holes | Main ports are reachable | Daily, service, unused, strain, and complete-stack rotation are coherent |
| Maintenance and recovery | Requires destructive disassembly | Some service access | Cleaning, fan failure, NVMe, screen, cables, and reassembly preserve state |
| Musician interaction | Generic enclosure | Screen angle and cables are considered | Viewing, reach, cable paths, noise, stability, and repeated use work together |
| Evidence honesty | Render is presented as solved | Some caveats | Concept, measurements, CAD, thermal, acoustic, and electrical evidence stay distinct |
| Verification quality | No testable next step | General testing advice | Specific fit, thermal, airflow, acoustic, electrical, cable, service, and untouched-state checks |
| Visual-product coherence | Generic Pi case | Recognizable wedge product | Exterior, internal layout, connectors, vents, and service strategy express one product |

Record the raw scores and short evidence for each. Do not change weights after
seeing the outputs. The ten dimensions have equal weight for the first
comparison; the maximum is 40.

Also record unscored observations:

- useful capability found only in the treatment;
- useful capability found only in the control;
- requirement both missed;
- unsupported claim in either result;
- whether either design is preferred by the creator/musician, and why.

## Claim boundary

A treatment result with materially stronger scores would support this claim:

> In this controlled Raspberry Pi enclosure case, Fructal Cap Design improved
> coverage and coherence of the physical-product design contract compared with
> the same task completed without the skill.

It would not prove:

- that either enclosure is physically safe, cool, quiet, manufacturable, or
  usable;
- that Fructal Cap Design always improves industrial design;
- that the image model faithfully rendered the written design;
- that the observed difference generalizes to other models, operators, or
  products; or
- that Fructal Cap Design caused every difference between stochastic runs.

Physical measurements, CAD fit checks, a printed prototype, thermal and
acoustic trials, connector and cable trials, service repetition, and affected
musician use remain separate future evidence.

## Publication record

Current run state:

- control run `ppd-001-control` is frozen in
  [`docs/evaluations/physical-product-comparison/ppd-001-control/`](evaluations/physical-product-comparison/ppd-001-control/);
- [protocol amendment 01](evaluations/physical-product-comparison/protocol-amendment-01.md)
  records prompt-author contamination identified before deliberate inspection
  of the frozen control result;
- treatment run `ppd-001-treatment` is frozen in
  [`docs/evaluations/physical-product-comparison/ppd-001-treatment/`](evaluations/physical-product-comparison/ppd-001-treatment/);
- both `ppd-001` execution runs are frozen and blinded evaluation is pending;
- [protocol amendment
  02](evaluations/physical-product-comparison/protocol-amendment-02.md) records
  the host-skill isolation defect, dual-home recovery, and three-arm extension;
- [protocol amendment
  03](evaluations/physical-product-comparison/protocol-amendment-03.md) records
  the need to score prompt, written design, image instruction, rendered image,
  and complete package separately, and reserves a combined Fructal Cap Design
  plus Superpowers arm; it also defines the current work as a first
  methodological pass and reserves structured human review of every design for
  a second pass, including same-prompt execution with an independent image
  renderer to separate prompt defects from renderer-specific artifacts;
- the [`ppd-002` three-arm
  comparison](evaluations/physical-product-comparison/ppd-002-discovery/)
  preserves no-user-skill, Superpowers-only, and Fructal Cap Design-only
  executions from a byte-identical prompt; and
- its separate blind evaluator scored the three arms `38/40`, `39/40`, and
  `38/40` respectively and treated the one-point spread as within judgment
  uncertainty;
- the [PPD-003 layered four-arm
  comparison](evaluations/physical-product-comparison/ppd-003-layered-comparison/)
  prospectively froze and executed the combined condition, blindly compared
  both prompt authors, extracted every exact render-call chain, and used two
  new judges to score written design, image instruction, renderer compliance,
  delivery/QC, and complete package separately; and
- the [2026-07-24 workflow
  postmortem](workflow-postmortem-2026-07-24.md) reconstructs the complete
  experiment motion, orchestration corrections, recoveries, and remaining work
  without rewriting the frozen records.

The preserved records include:

- the frozen treatment and control prompts;
- raw responses and original images;
- model and tool metadata;
- blind scores and the revealed arm mapping;
- comparison findings; and
- sanitized compressed execution traces.

Any physical prototype evidence remains future work.

Append results without rewriting these pre-run expectations or scoring rules.
