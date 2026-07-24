# Sources inspected

## Provided requirements

- Complete `ppd-001-control` prompt in [`prompt.md`](prompt.md): accessible. Source for the requested stack, enclosure character, airflow goals, connector facts, service requirements, experiment state, and archival instructions.
- Repository `AGENTS.md` instructions supplied immediately before the run prompt: accessible in conversation context. Source only for repository naming, validation, synchronization, and publication rules; not a physical-design source.

## SHR-DAW project documentation

All four files below were read from the immutable SHR-DAW commit `927eb05888951f9955c7d46e856ef7208149bc00`, fetched from `https://github.com/PaolaShultz/shr-daw.git`. All were accessible.

- `README.md`: source for SHR-DAW's compact Raspberry Pi music-workstation purpose, 40×13 terminal interface, and normal software context.
- `docs/PI5_HEADROOM_PLAN.md`: source for the planned Pi 5 2 GB, official Active Cooler, 27 W supply, bottom-mounted PCIe-to-NVMe base, 128 GB NVMe, GPIO-connected 480×320 display above the Pi, self-designed printed housing, required cooler airflow, connector exposure, cable-strain avoidance, and measurement-before-CAD boundary.
- `docs/PI5_NVME_INSTALL.md`: source for the bottom-mounted NVMe/base arrangement, top GPIO position reserved for the display, power-off service precautions, PCIe ribbon sensitivity, and base-manufacturer dependency.
- `docs/WORKSPACE_HANDOFF.md`: source for the current statement that the Pi 5 stack is ordered but not installed or measured and that the housing remains measurement-dependent.
- Repository root at `https://github.com/PaolaShultz/shr-daw/tree/927eb05888951f9955c7d46e856ef7208149bc00`: accessible; used to confirm the immutable source commit and repository identity.

No other SHR-DAW enclosure conversation, physical-product result, or treatment result was inspected.

## Official Raspberry Pi documentation

- Raspberry Pi 5 mechanical drawing, `https://pip.raspberrypi.com/documents/RP-008347-DS`: accessible as a one-page PDF. The downloaded original had SHA-256 `5dd680d6c1f5e7aa9c7b020695e315d04aac862df82ff01d4e9041cd0668d7f2`. Source for the approximate 85 × 56 mm board outline, mounting and connector arrangement shown in the drawing, and the explicit warning that dimensions are approximate, reference-only, tolerance-dependent, incomplete, and subject to change.
- Raspberry Pi 5 Active Cooler mechanical drawing, `https://datasheets.raspberrypi.com/cooling/raspberry-pi-active-cooler-mechanical-drawing.pdf`: accessible as a one-page PDF. The downloaded original had SHA-256 `3cc3bccc4b58d0690c2b18251cffc3863091305c32fd5d198f152722ba2bd09f`. Source for the approximate 63.50 × 42.50 mm plan envelope and 13.70 mm height, plus the warning that dimensions are approximate, tolerance-dependent, and subject to change.
- Raspberry Pi configuration documentation, `https://www.raspberrypi.com/documentation/computers/configuration.html`: accessible as live documentation; immutable revision unavailable. The display-configuration section was inspected. Source for the general Raspberry Pi OS statement that console display rotation can be requested with KMS `video=` rotation parameters. It does **not** establish that the unknown GPIO display or its driver supports rotation.

## Image-production instructions

These were inspected only to operate the allowed artifact-generation capability, not as physical-design or workflow-design sources:

- `/home/shome/.codex/skills/.system/imagegen/SKILL.md`: accessible.
- `/home/shome/.codex/skills/.system/imagegen/references/prompting.md`: accessible.
- `/home/shome/.codex/skills/.system/imagegen/references/sample-prompts.md`: accessible.

The Fructal Cap Design skill body was not opened.

## Post-freeze archival source

- `docs/physical-product-comparison-protocol.md` at pre-run protocol commit `b9eec17fd7886e96299075a420b856a80c32d104`: accessible only after both `design-response.md` and `concept-board.png` were frozen. The starting-evidence, treatment/control wrapper, run-discipline, claim-boundary, and publication-record material needed for archival and the permitted status update was inspected. It was not used to revise or score the frozen design.
- `concept-board.png`: the original generated output was inspected after generation only to record visible mismatches. It was not used to revise `design-response.md`.

## Inference used in the frozen design

The selected connector destinations, reversible carrier/bezels, split intake plenum, cable routing, service-module arrangement, aesthetic treatment, risks, measurement list, and verification plan are design inferences from the provided requirements and inspected evidence. They are proposals, not statements found in project or official documentation.

The display model, display PCB dimensions, rotation support, NVMe-base model and geometry, SSD hotspot, case-fan model and electrical/control interface, Active Cooler airflow direction in the assembled stack, cable bend radii, antenna keep-out, enclosure dimensions, display angle, material details, and thermal/acoustic performance were unavailable and were not represented as verified facts.
