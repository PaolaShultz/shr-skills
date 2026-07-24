You are designing a buildable enclosure and physical product concept for SHR-DAW running on a Raspberry Pi 5. Carry out the research and design work now, then present one resolved final design. Do not merely restate the brief.

Repository:

- https://github.com/PaolaShultz/shr-daw
- Treat commit `927eb05888951f9955c7d46e856ef7208149bc00` as the only authoritative repository state.
- Clone or inspect that exact commit. Confirm the checked-out commit before drawing conclusions. Do not use behavior, files, screenshots, or documentation from a different revision without clearly identifying them as external context.

Research enough to make the physical design credible. Inspect the repository for the user interface, intended display orientation, input model, hardware assumptions, and anything else that affects enclosure design. Also consult authoritative current sources for the exact Raspberry Pi 5, display, active cooler, NVMe/base hardware, connectors, cable clearances, airflow needs, mounting dimensions, and orientation constraints that are relevant. Prefer primary sources and cite direct links. If the exact display, NVMe board, bottom plate, fan, or other component cannot be identified from the repository or brief, do not silently invent it: state what is unknown, choose a clearly labeled design assumption where necessary, and explain how the enclosure can accommodate the uncertainty.

The product brief:

- The complete Raspberry Pi assembly is housed in a compact enclosure and tilted so the screen on top faces somewhat forward toward the operator.
- The front should use grille-like air intakes.
- Because the assembly is tilted, the desired intake path is approximately straight into the gap between the display and the Raspberry Pi board.
- The Pi has an active cooler focused mainly on the CPU. The display and an NVMe device mounted near the bottom plate also contribute heat and need consideration.
- The rear should extend down so it sits level on the supporting surface despite the tilted main body.
- The rear should also have a grille and one small active 5 V computer fan for exhaust.
- The visual character should evoke an old analog amplified console or a compact modern digital console, while remaining a coherent, manufacturable product rather than a decorative pastiche.
- Connector access is a central problem. Some connectors are on a side that is comparatively easy to organize. Power, USB, and two USB-C connectors are on the edge that appears to be the “top” relative to the current screen orientation.
- Investigate whether rotating the screen and interface orientation could put that difficult connector edge at the bottom. Evaluate this rather than assuming it is good or bad. Account for software rotation, touch/input mapping if applicable, connector and cable clearance, strain relief, usability, cooling, service access, stability, and appearance.

Resolve ambiguities in connector identity and location from evidence wherever possible. Do not preserve an incorrect connector description merely because it appears in the brief. Explicitly distinguish native Raspberry Pi connectors from connectors supplied by attached boards or peripherals.

Develop several plausible physical arrangements internally, compare their consequences, and select one final configuration. The final configuration must specify:

- overall form, stance, approximate size, screen angle, and display orientation;
- placement and access strategy for every relevant connector;
- front intake, internal airflow route, exhaust fan placement and direction, grille treatment, and measures intended to limit recirculation, dead zones, noise, and dust;
- treatment of CPU, display, NVMe, and other meaningful heat sources;
- internal stack order, mounting approach, cable routing, strain relief, assembly sequence, and serviceability;
- rear leveling geometry, feet, stability, and tip resistance;
- enclosure materials, wall thickness or fabrication assumptions, fasteners, finishes, and a realistic prototyping/manufacturing route;
- control layout and visual details that create the console character without obstructing ventilation or ports;
- safety and reliability concerns, including fan failure, blocked vents, sharp bends, electrical clearance, and realistic limitations of the proposal.

Make exactly one new picture: a single polished product-design image of the selected final configuration. It may be a carefully arranged multi-view presentation within one image if that communicates the enclosure better than one perspective, but it must remain one image file and one coherent presentation. Show enough of the front, screen angle, side connector solution, and rear exhaust/leveling form to make the design understandable. Avoid unsupported labels, impossible port geometry, and decorative details that conflict with the written design. Do not generate alternate concept images.

Your final response must contain:

1. **Final design** — a concise description of the resolved product and why its configuration was selected.
2. **Repository and hardware findings** — the facts that materially affected the design, with citations and a clear distinction between verified facts, reasonable inferences, and assumptions.
3. **Orientation and connector decision** — the evaluated options and a direct conclusion on whether to rotate the display/interface so the difficult connector edge becomes the bottom.
4. **Mechanical and thermal specification** — dimensions or dimension ranges, component arrangement, airflow, fan, grilles, materials, mounting, cable management, assembly, and maintenance details sufficient for a next-stage CAD pass.
5. **The picture** — embed or link the one final image and briefly identify what is shown.
6. **Risks and validation** — unresolved fit questions, thermal and acoustic risks, and concrete measurements or tests required before fabrication.
7. **Comparison record** — a compact, consistently formatted table recording at least:
   - repository URL and exact commit;
   - research date;
   - identified hardware and unknown hardware;
   - chosen display orientation and angle;
   - connector strategy;
   - approximate external dimensions;
   - cooling layout, fan size/voltage, and airflow direction;
   - component stack;
   - materials and fabrication route;
   - service-access approach;
   - principal design advantages;
   - principal compromises;
   - unresolved assumptions;
   - sources used;
   - image filename.

Use exact values only when supported by evidence. When estimating, provide a range or label the value as provisional. Keep the final design internally consistent across the prose, specifications, comparison table, and picture. Do not claim that thermal performance, acoustics, structural strength, fit, or manufacturability has been proven without calculation or physical testing.
