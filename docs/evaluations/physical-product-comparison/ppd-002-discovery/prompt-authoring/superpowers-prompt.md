# SHR-DAW Raspberry Pi 5 enclosure: research, final design, image, and comparison record

Start a new, self-contained research and product-design task. Do not rely on any earlier conversation.

## Objective

Research and design one final, credible, ready-to-build enclosure for SHR-DAW on a Raspberry Pi 5. The result should look like a compact old analog amplified console interpreted as a modern small digital console. Resolve the mechanical, thermal, connector, screen-orientation, assembly, and serviceability questions rather than producing only a visual concept.

The SHR-DAW repository is pinned to this exact source state:

- Repository: https://github.com/PaolaShultz/shr-daw
- Commit: `927eb05888951f9955c7d46e856ef7208149bc00`

Obtain and inspect that exact revision. Verify and report the checked-out commit before relying on repository contents. Do not silently use the current default branch or facts from another revision. Follow repository links only when needed to identify hardware, dimensions, interfaces, or constraints, and distinguish external information from facts present in the pinned revision.

## Starting concept and required contracts

Treat the following as the design brief:

- The entire Raspberry Pi and display assembly is tilted so the display on top faces somewhat forward for comfortable use.
- The front has grille-like air intakes.
- The intake path should feed air as directly as practical into the gap between the display and the Raspberry Pi board.
- The Raspberry Pi has an active CPU cooler, but the complete thermal design must also account for heat from the display and the NVMe device mounted near the bottom plate.
- The rear/lower portion should extend or step down so it sits level with the table or floor, giving the tilted body a stable console-like stance.
- The rear has an exhaust grille and one small 5 V computer fan.
- The final form should read as a compact audio console, not as a generic rectangular electronics box.
- Connector access is a central design problem. Some connectors can be arranged on a side, while power/USB-related connectors and two USB-C connectors appear to be on what is currently the “top” edge when viewed in the display’s normal orientation. Verify the actual hardware and connector mapping from evidence; do not assume this description is electrically exact.
- Seriously investigate physically rotating the display assembly and rotating the displayed interface so that this connector edge becomes the bottom edge. Check software rotation, touch/input mapping if applicable, boot-time behavior, cable routing, bend clearance, cooling, usability, and service access. Compare it with leaving the display in its normal physical orientation, then choose and defend one final arrangement.

Preserve these contracts unless evidence proves one physically unsafe or impossible. If that happens, explain the conflict and make the smallest necessary change.

## Research requirements

Inspect the pinned repository’s documentation, hardware references, configuration, interface layout, and any drawings or images relevant to the enclosure. Then verify important hardware facts using primary sources such as official Raspberry Pi documentation and the actual component manufacturers’ documentation or drawings.

Establish, as far as the evidence permits:

- The exact Raspberry Pi, display, NVMe arrangement, cooler, attached boards, controls, and exposed connectors that the pinned SHR-DAW state expects or depicts.
- Board, display, mounting-hole, connector, and keep-out dimensions.
- Cable types, connector directions, plug-body sizes, and realistic bend/hand-access clearances.
- Cooling requirements and heat sources, including whether the proposed airflow actually washes the CPU cooler, display cavity, and NVMe area rather than bypassing them.
- Safe ways to power and, if appropriate, control the 5 V rear fan without exceeding a supply or header rating.
- Relevant screen and interface rotation support, including any difference between the operating system, boot display, SHR-DAW interface, and touch or pointer coordinates.
- Fabrication, fastening, grounding, dust, acoustics, stability, maintenance, and assembly implications.

Use exact measurements where authoritative values exist. Label estimates, derived values, assumptions, and unresolved facts clearly. Do not invent missing dimensions, performance figures, test results, or compatibility claims. If essential physical information is unavailable, provide the specific measurement that must be taken and design around it with an explicit allowance.

For every important claim, cite a direct source close to the claim. Prefer pinned repository permalinks, official documentation, manufacturer drawings, and datasheets. Record source title, URL, revision or publication date when available, and access date.

## Design work

Evaluate the plausible physical screen orientations and connector-routing arrangements, including the proposed 180-degree physical rotation. Also evaluate the airflow route from the front intakes through the display/board gap and CPU-cooler region to the rear fan, with a deliberate route past or around the NVMe area.

Then select one final design. Do not leave the result as several equal alternatives. The final design must specify:

- Overall form, proportions, display angle, stance, visual language, finishes, and grille treatment.
- An internally consistent dimensional envelope, wall thicknesses, clearances, mounting points, feet, fasteners, and assembly sequence.
- Locations and access directions for every required external connector and control.
- Display physical orientation and software orientation, with the connector and cable-routing consequences.
- Front intake, internal ducting or baffles, exhaust path, rear-fan placement and direction, vent open areas, recirculation prevention, and dust/noise considerations.
- Placement and cooling treatment for the Raspberry Pi, active CPU cooler, display, and NVMe hardware.
- Rear/lower geometry that gives the angled console a stable, level contact with the supporting surface.
- Material and fabrication approach appropriate for a realistic one-off build, plus any inserts, brackets, gaskets, meshes, guards, or strain relief.
- A practical way to open, assemble, clean, and service the device without damaging short internal cables.
- Safety and feasibility limitations, including what must be measured or thermally tested before prolonged use.

Use calculations or clearly explained estimates where they materially support the design. Do not claim a thermal result that has not been measured. Instead, give expected behavior, the basis for that expectation, and a concrete validation procedure with pass/fail thresholds.

## Exactly one picture

Create exactly one final image file, `final-product.png`. It should be a coherent, high-quality single-sheet product visualization of the selected design, not a collection of unrelated concept variants. Show a convincing three-quarter view of the enclosure and use a restrained cutaway, ghosted region, or compact inset within the same image only if needed to make the airflow path, internal stack, rear fan, or connector solution understandable.

The picture must agree with the written final design: display angle and orientation, console proportions, front and rear grilles, connector placement, rear/lower support geometry, materials, and visible controls must not contradict the report. Clearly label the image as an evidence-informed concept visualization rather than a dimensionally authoritative manufacturing drawing.

## Required deliverables

Create a directory named `shr-daw-enclosure-result` containing:

1. `design-report.md`
   - Executive summary and final recommendation.
   - Verified baseline from the pinned commit.
   - Evidence and sources.
   - Requirements and constraints.
   - Screen-orientation and connector investigation.
   - Thermal and airflow reasoning.
   - Final mechanical and industrial design.
   - Dimensions and clearances.
   - Materials, parts, fabrication, assembly, and service procedure.
   - Risks, unresolved measurements, and validation tests.
   - A brief explanation of why the selected design was chosen over the rejected arrangements.

2. `comparison-record.json`
   - A valid JSON record using the schema below.
   - Use numbers with explicit units in adjacent fields.
   - Use `null` for unknown values rather than guessing.
   - Give each uncertain field a confidence of `high`, `medium`, or `low`, plus a short reason or evidence reference.
   - Keep observed facts, calculated or inferred values, assumptions, and proposed design values distinguishable.

3. `final-product.png`
   - The single image described above.

4. `sources.md`
   - A numbered source list with direct URLs, source type, revision/date when available, access date, and a one-line note describing which claims each source supports.

Use this top-level structure for `comparison-record.json`, adding detailed nested fields where helpful but not removing any listed key:

```json
{
  "record_version": "1.0",
  "project": "SHR-DAW Raspberry Pi 5 enclosure",
  "repository": {
    "url": "https://github.com/PaolaShultz/shr-daw",
    "required_commit": "927eb05888951f9955c7d46e856ef7208149bc00",
    "verified_commit": null
  },
  "research_date": null,
  "final_design_name": null,
  "design_summary": null,
  "hardware_baseline": {
    "raspberry_pi": null,
    "display": null,
    "nvme": null,
    "cpu_cooler": null,
    "attached_boards_and_controls": [],
    "required_external_connections": []
  },
  "geometry": {
    "external_width_mm": null,
    "external_depth_mm": null,
    "external_height_front_mm": null,
    "external_height_rear_mm": null,
    "display_angle_deg_from_horizontal": null,
    "wall_thickness_mm": null,
    "minimum_internal_clearances_mm": {},
    "estimated_mass_g": null,
    "footprint_and_stability_notes": null
  },
  "screen_and_connectors": {
    "physical_screen_rotation_deg": null,
    "software_rotation_deg": null,
    "touch_or_pointer_mapping": null,
    "chosen_connector_strategy": null,
    "connector_access_table": [],
    "cable_and_strain_relief_notes": null
  },
  "thermal": {
    "airflow_direction": null,
    "front_intake_free_area_mm2": null,
    "rear_exhaust_free_area_mm2": null,
    "rear_fan_size_mm": null,
    "rear_fan_voltage_v": 5,
    "rear_fan_rated_airflow": null,
    "rear_fan_rated_noise_dba": null,
    "rear_fan_current_a": null,
    "rear_fan_power_and_control": null,
    "cpu_cooling_path": null,
    "display_cooling_path": null,
    "nvme_cooling_path": null,
    "dust_and_recirculation_controls": null,
    "thermal_predictions_are_unverified": true
  },
  "construction": {
    "primary_material": null,
    "fabrication_process": null,
    "finish": null,
    "fasteners_and_inserts": [],
    "grilles_meshes_and_guards": [],
    "assembly_sequence": [],
    "service_access": null
  },
  "aesthetics_and_use": {
    "console_reference": null,
    "visual_features": [],
    "user_posture_and_viewing_notes": null,
    "control_access_notes": null
  },
  "parts_and_cost": {
    "enclosure_specific_parts": [],
    "estimated_total_enclosure_cost": null,
    "cost_currency": null,
    "cost_date": null
  },
  "validation": {
    "required_physical_measurements": [],
    "required_fit_checks": [],
    "required_thermal_tests": [],
    "required_electrical_checks": [],
    "pass_fail_thresholds": []
  },
  "tradeoffs": {
    "main_benefits": [],
    "main_drawbacks": [],
    "rejected_arrangements": []
  },
  "risks_and_unknowns": [],
  "evidence_references": [],
  "field_confidence": {}
}
```

## Quality rules

- Keep the final proposal internally consistent across all four files.
- Make evidence, assumptions, inferences, and design choices easy to distinguish.
- Do not mistake visual plausibility for mechanical or thermal validation.
- Do not hide unresolved connector, cable, mounting, or thermal issues.
- Favor a buildable and serviceable result over decorative complexity.
- Make final decisions wherever evidence supports them; use explicit measurement or test requirements only where a responsible decision cannot yet be made.
- Before finishing, check that the required commit is verified, all required files exist, the JSON parses, the report and record agree, every important factual claim is sourced, and there is exactly one generated image.

Proceed autonomously through research, design, documentation, and image creation. Ask a question only if progress is genuinely impossible without information that cannot be found in the pinned repository or authoritative sources; otherwise state a reasonable assumption and continue.
