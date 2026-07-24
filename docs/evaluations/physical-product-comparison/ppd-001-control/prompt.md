This is run `ppd-001-control`, the first run of the prospective SHR-DAW
  physical-product comparison.

  CONTROL BOUNDARY

  Do not invoke, load, quote, imitate, or use Fructal Cap Design. Do not use
  another workflow-design, service-design, systems-design, or brainstorming skill.
  The image-generation capability is allowed because it produces the requested
  artifact rather than supplying the design method.

  If Fructal Cap Design metadata is automatically present in the environment, do
  not open its body. Record that ambient metadata exposure as a possible control
  contamination. Do not silently convert this into a treatment run.

  Do not read this comparison protocol before freezing the design result because
  it contains the treatment hypotheses and scoring rubric:

  /home/shome/p/shr-skills/docs/physical-product-comparison-protocol.md

  Do not inspect another enclosure-design conversation or any treatment result.
  Do not ask routine preference questions. Continue using explicit assumptions
  when exact measurements are unavailable.

  EXPERIMENT STATE

  - Run ID: ppd-001-control
  - Run order: control first, treatment second
  - Protocol repository: /home/shome/p/shr-skills
  - Protocol commit before this run:
    b9eec17fd7886e96299075a420b856a80c32d104
  - Frozen Fructal Cap Design source commit:
    5efbd8a586cfed7538141e25111a247127ca092d
  - Frozen skill SHA-256:
    11b11556b3092f3fa14b7dd81ecfd96bde635433cff20141d87603f36c48f171
  - Frozen SHR-DAW source commit:
    927eb05888951f9955c7d46e856ef7208149bc00
  - No treatment result exists yet.
  - Do not score this run. Scoring happens only after both outputs are frozen and
    renamed for blinded comparison.

  SHARED NEUTRAL TASK — DO NOT ADD METHOD-SPECIFIC REQUIREMENTS

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

  FREEZE AND RECORD THE RUN

  Complete the written design first. Save its final, unrevised form before
  generating the image. Then create the image from that frozen design. Do not
  quietly repair the written design after seeing weaknesses in the generated
  image; record any mismatch separately.

  After both text and image are frozen, you may read:

  /home/shome/p/shr-skills/docs/physical-product-comparison-protocol.md

  Read it only to follow the archival requirements. Do not score the result or
  rewrite the frozen response to satisfy the rubric.

  Create:

  docs/evaluations/physical-product-comparison/ppd-001-control/

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
     - protocol, skill-source, skill-hash, and SHR-DAW commits;
     - whether Fructal Cap Design metadata was ambiently visible;
     - confirmation that its body was not opened or used;
     - unavailable metadata explicitly marked `unavailable`;
     - any interruption, retry, tool failure, or context loss.

  3. `sources.md`
     - every source actually inspected;
     - exact immutable commit or URL where available;
     - whether each source was accessible;
     - which statements came from project documentation, official hardware
       documentation, provided requirements, or inference.

  4. `design-response.md`
     - the complete frozen written design;
     - no later corrections silently merged into it.

  5. `image-prompt.md`
     - the exact final prompt sent to the image-generation tool;
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
     - observations only—no rubric score and no treatment comparison.

  Store the original generated image as `concept-board.png` only if the image tool
  provides the original artifact or an exact retrievable output. Do not fabricate
  a local image from a screenshot and call it the original.

  After the run is frozen:

  - update only the status/publication-record portion of
    `docs/physical-product-comparison-protocol.md` to say that the control is
    frozen and the treatment is pending;
  - do not alter its hypotheses, shared task, wrappers, run discipline, rubric, or
    claim boundary;
  - add no comparative conclusion to the README or real-world evidence account;
  - run `git diff --check`, `scripts/validate.sh`,
    `tests/test-validation.sh`, and `tests/test-live-eval-harness.sh`;
  - inspect the complete staged diff and ensure no private data or unrelated file
    is included;
  - commit the experimental record with:
    `Record control enclosure design run`
  - push the verified `main` branch to the repository’s existing `origin`;
  - verify that local HEAD and `origin/main` match;
  - report the artifact paths, commit, validation results, and anything that could
    contaminate the control.

  Finally, return the frozen written design and generated presentation image to me.
  Do not provide or anticipate the treatment result.
