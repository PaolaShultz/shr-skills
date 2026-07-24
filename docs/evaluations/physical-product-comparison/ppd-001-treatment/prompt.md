This is run `ppd-001-treatment`, the second run of the prospective SHR-DAW
physical-product comparison.

TREATMENT BOUNDARY

Use $fructal in Redesign mode for the task below. Hold its no-modification
boundary for the target product and SHR-DAW repository. Image generation is
authorized only for the requested concept artifact.

Before beginning, verify without modifying anything that:

- `/home/shome/p/shr-skills/skills/fructal/SKILL.md`
- `/home/shome/.codex/skills/fructal/SKILL.md`

both have SHA-256:

`11b11556b3092f3fa14b7dd81ecfd96bde635433cff20141d87603f36c48f171`

If either hash differs, stop and report the mismatch without continuing the
experiment.

Do not read, list, open, summarize, or inspect anything inside:

`docs/evaluations/physical-product-comparison/ppd-001-control/`

Do not inspect another enclosure-design conversation, control response, control
image, control metadata, score, or user reaction.

Do not read either of these before freezing the treatment design and image,
because they expose the scoring rubric and contamination analysis:

- `docs/physical-product-comparison-protocol.md`
- `docs/evaluations/physical-product-comparison/protocol-amendment-01.md`

Do not ask routine preference questions. Continue using explicit assumptions
when exact measurements are unavailable.

EXPERIMENT STATE

- Run ID: ppd-001-treatment
- Fixed order: control first, treatment second
- Repository: `/home/shome/p/shr-skills`
- Original protocol commit:
  `b9eec17fd7886e96299075a420b856a80c32d104`
- Repository commit immediately before treatment:
  `38d126cabc36d9e6d28d0b0d527c6db3adeac08f`
- Frozen control commit, which must not be inspected:
  `d46ad38`
- Frozen Fructal Cap Design source commit:
  `5efbd8a586cfed7538141e25111a247127ca092d`
- Frozen skill SHA-256:
  `11b11556b3092f3fa14b7dd81ecfd96bde635433cff20141d87603f36c48f171`
- Frozen SHR-DAW source commit:
  `927eb05888951f9955c7d46e856ef7208149bc00`
- Control text-model identifier: unavailable
- Control reasoning level: unavailable
- Control image tool identifier: `image_gen.imagegen`
- Control underlying image-model identifier: unavailable
- Control had shell, filesystem, web, network, image-generation, and Git remote
  access.
- Use the current thread’s normal GPT-5-family model and reasoning setting.
- Use `image_gen.imagegen` for exactly one substantive image-generation request.
- A pure transport/tool failure may be retried once with the identical image
  prompt; record it. Do not make aesthetic correction generations.
- No blinded scoring or comparison has occurred.
- Do not score this run.

SHARED NEUTRAL TASK — KEEP THIS TASK UNCHANGED

Design the final physical enclosure concept for SHR-DAW, a compact Raspberry Pi
music workstation. Research and design only: do not modify SHR-DAW, create
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

The NVMe, fan, display, and necessary connectors must remain serviceable. Do not
invent exact component dimensions or ports when evidence is unavailable.

Produce:

1. a concise design rationale and selected orientation;
2. the proposed airflow, connector, cable, and service arrangement;
3. assumptions, risks, required measurements, and a verification plan; and
4. one polished concept presentation board containing:
   - a three-quarter exterior view;
   - a cutaway airflow view; and
   - a rear/side connector and service view.

Clearly label the image as a concept rather than validated CAD or thermal proof.

FREEZE AND RECORD THE TREATMENT

Complete the Fructal Cap Design Redesign analysis and written design first. Save
its final, unrevised form before generating the image.

Then derive one image prompt from that frozen design and make exactly one
substantive image-generation request. Do not quietly repair the written design
after seeing weaknesses in the generated image. Record discrepancies separately.

After the written response and image are frozen, you may read:

- `docs/physical-product-comparison-protocol.md`
- `docs/evaluations/physical-product-comparison/protocol-amendment-01.md`

Read them only to follow archival requirements. Do not score the treatment,
inspect the control, or rewrite the frozen response to satisfy the rubric.

Create:

`docs/evaluations/physical-product-comparison/ppd-001-treatment/`

inside `/home/shome/p/shr-skills`, containing:

1. `prompt.md`
   - this exact complete prompt;
   - no paraphrase or shortened reconstruction.

2. `metadata.md`
   - run ID and fixed order;
   - start and completion timestamps with timezone;
   - exact model identifier and reasoning level when exposed;
   - image model/tool identifier when exposed;
   - tool and network availability;
   - original protocol commit, repository pre-treatment commit, frozen
     skill-source commit, verified skill hash, and SHR-DAW commit;
   - confirmation that Fructal Cap Design was invoked in Redesign mode;
   - confirmation that its body matched the frozen hash;
   - confirmation that the control directory was not inspected;
   - unavailable metadata explicitly marked `unavailable`;
   - every interruption, retry, tool failure, or context loss.

3. `sources.md`
   - every source actually inspected;
   - exact immutable commit or URL where available;
   - whether each source was accessible;
   - which statements came from project documentation, official hardware
     documentation, provided requirements, Fructal Cap Design analysis, or
     inference.

4. `design-response.md`
   - the complete frozen written Redesign result;
   - no later corrections silently merged into it.

5. `image-prompt.md`
   - the exact final prompt sent to `image_gen.imagegen`;
   - all referenced images or source assets;
   - generation options or unavailable settings.

6. `artifact-manifest.md`
   - generated-image filename, filesystem path, attachment identity, output
     hint, or other exact locator available;
   - image dimensions and format when exposed;
   - SHA-256 for every locally stored artifact;
   - explicit note if the platform does not expose the original image as a
     filesystem artifact;
   - no screenshot, recompression, or transcription presented as the original.

7. `observations.md`
   - tool failures, generation mismatch, unavailable evidence, or later-noticed
     concerns;
   - observations only;
   - no rubric score, control inspection, or comparative conclusion.

Store the original generated image as `concept-board.png` only if the image tool
provides the original artifact or an exact retrievable output. Do not fabricate
a local image from a screenshot and call it the original.

After the treatment is frozen:

- update only the status/publication-record portion of
  `docs/physical-product-comparison-protocol.md` to say both execution runs are
  frozen and blinded evaluation is pending;
- link the treatment artifact directory there;
- do not alter the protocol’s hypotheses, shared task, wrappers, run discipline,
  rubric, or claim boundary;
- do not alter `protocol-amendment-01.md`;
- add no comparative conclusion to README or the real-world evidence account;
- run `git diff --check`, `scripts/validate.sh`,
  `tests/test-validation.sh`, and `tests/test-live-eval-harness.sh`;
- inspect the complete staged diff and ensure no private data or unrelated file
  is included;
- commit with:
  `Record treatment enclosure design run`
- push the verified `main` branch to the existing `origin`;
- verify that local HEAD and `origin/main` match;
- report artifact paths, commit, validation results, and anything that could
  contaminate the treatment.

Finally, return the frozen written design and generated presentation image to
me. Do not inspect, summarize, score, or anticipate the control result.
