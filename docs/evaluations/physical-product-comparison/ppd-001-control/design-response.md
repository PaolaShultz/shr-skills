# SHR-DAW Console Wedge

## Design rationale and selected orientation

The enclosure is a compact, warm-graphite wedge with a broad dark front grille, a modestly inclined display plane, and a low rear plinth that rests flat on the table. Its cues come from old amplified consoles—one purposeful face, a dark ventilation field, a few visible service fasteners—refined into a quiet modern digital instrument. It has no decorative RGB, gaming vents, fake controls, or generic clear Raspberry Pi-case treatment.

Select the **180-degree rotated stack** as the concept orientation. Orientation here is defined by connector destination: the USB-C power and two micro-HDMI ports face the rear connector bay, while the four USB ports and Ethernet face a recessed left-rear side bay. Compared with a screen-upright arrangement that leaves power/HDMI toward the lower front, this keeps the permanent power lead and occasional display cables away from the musician's hands and lets USB, MIDI, audio, and Ethernet leads depart sideways and then rearward.

This choice is provisional rather than a claim that the screen can rotate. Raspberry Pi's general console documentation supports KMS output rotation, but that does not establish support for the unknown 480×320 GPIO display or its driver. The internal carrier and two connector bezels should therefore be reversible: if the exact display cannot rotate reliably from boot through SHR-DAW, the same enclosure architecture can accept the unrotated stack with swapped blanking/I/O inserts rather than forcing a different shell.

The display should be angled only enough to face a seated musician comfortably, determined with a full-scale sight-line mock-up rather than an invented angle. A slightly raised rear shoulder shades and protects the display without becoming a tall tablet stand.

## Airflow arrangement

The broad lower-front grille is the only intended intake. Behind it, a low-resistance plenum divides the incoming air into two connected paths:

- The upper path rises through the real gap between display and Pi, washing the board area and feeding the official Active Cooler without sealing or starving its inlet.
- The lower path passes along the bottom NVMe base and drive, including the PCIe area, before rejoining the upper path in a rear collection plenum.

A small 5 V fan sits in a screw-removable rear cartridge and exhausts through a guarded rear grille. A close-fitting fan surround prevents it from drawing most of its air from gaps immediately beside the fan. The two internal paths remain generous and connected rather than becoming narrow ducts; the intent is to cool the Pi board, power circuitry, controller silicon, and NVMe as well as the CPU hotspot. Cable bundles are clipped to the side walls and kept out of the screen-to-Pi gap and the NVMe stream.

The official references give only approximate component envelopes: the Pi drawing shows an 85 × 56 mm board, and the Active Cooler drawing shows a 63.50 × 42.50 mm plan envelope and 13.70 mm height. Both drawings explicitly warn that their dimensions are reference-only and subject to tolerances or change. They inform the concept but must not drive production geometry. Cooler inlet/exhaust direction and clearance must be confirmed on the actual assembly before adding baffles.

The intake screen, if used, slides out from the underside without opening the electronics bay. Thermal tests should compare open grille, grille plus screen, case fan on, and case fan off; the screen is omitted if it creates unacceptable restriction or noise.

## Connectors, cables, and service

The rear connector bay exposes USB-C power and both micro-HDMI ports directly, without internal extensions. The USB-C lead enters inside the footprint of the rear plinth, turns with a measured bend radius, and is retained by a removable strain-relief clip so a pull is not transmitted directly to the board. The micro-HDMI openings receive individual removable blanks when unused.

The four USB ports and Ethernet remain directly accessible in the recessed left-rear bay. Its rearward chamfer gives straight plug insertion plus a natural cable exit toward the back of the desk. The recess must be sized from the largest real USB and Ethernet plugs likely to be used, not connector shells alone. No audio, MIDI, network, or display port is added by the enclosure.

Service uses screw-retained modules rather than glue or hidden snap fits:

- The display bezel lifts from the upper face after removing underside-accessible screws; it includes a documented slack loop and strain relief for the GPIO/display connection.
- The Pi/display/NVMe assembly mounts to one removable carrier. The carrier supports either of the two 180-degree orientations and leaves Active Cooler fasteners reachable.
- A bottom hatch within the plinth exposes the NVMe drive and base fasteners without removing the display.
- The rear fan cartridge removes independently after its guarded connector is unplugged.
- Reversible rear and side I/O bezels allow the stack orientation to be changed after the display-rotation test.

Every service operation begins powered off and unplugged. The assembly sequence must allow the display, fan, Pi/cooler, NVMe drive, and NVMe base to be replaced individually without cutting ties, peeling adhesive, or desoldering enclosure wiring.

## Assumptions and risks

Assumptions:

- The provided component list is the intended stack, but the exact display, NVMe-base, SSD, and rear-fan models are not yet known.
- The display is approximately coextensive with the Pi in plan and leaves a usable air gap; neither point is accepted until measured.
- Rear power/HDMI plus left-rear USB/Ethernet is compatible with the intended desk and cable approach.
- A printed non-metallic main shell is still intended, as stated in the project plan; material, wall construction, inserts, and finish remain undecided.

Primary risks:

- The GPIO display may not support 180-degree rotation in its actual boot/console/driver path, or rotation may begin only after unreadable boot stages.
- The display PCB, header, or mounting hardware may obstruct the Active Cooler, recirculate its discharge, or leave too little screen-to-Pi flow area.
- The bottom base, PCIe ribbon, NVMe controller, or SSD may place its hotspot where the proposed lower stream does not reach it.
- A rear fan may add tonal noise, grille turbulence, vibration, electrical noise, or insufficient static pressure. Its current draw, control method, connector, fail-safe behavior, and GPIO conflicts are unknown.
- Large USB plugs, Ethernet boots, micro-HDMI adapters, and the 27 W USB-C lead may collide with the shell or exceed the plinth's bend space.
- Exhaust may recirculate if the unit is pushed against a wall; the plinth and rear grille need a verified keep-clear zone.
- Enclosure material or hardware may impair Wi-Fi/Bluetooth if it crosses the Pi antenna keep-out, which has not been established from the inspected sources.

## Required measurements

Before CAD, record:

1. Exact model, PCB outline, visible area, bezel overlap, thickness, mounting holes, connector/pin use, and driver for the 480×320 display.
2. Complete assembled stack envelope in both orientations, including standoffs, GPIO engagement, cooler, bottom base, SSD, PCIe ribbon, screw access, and safe compression/clearance limits.
3. Actual positions and protrusions of every required connector, plus insertion grip space and bend radius for representative power, USB, Ethernet, and micro-HDMI cables.
4. Active Cooler inlet, discharge, and keep-clear zones on the running physical assembly.
5. NVMe controller/SSD hotspot location and whether the base provides a heat spreader.
6. Rear fan dimensions, airflow direction, pressure/flow curve, acoustic specification, rated and startup current, connector, control requirements, and safe power source after accounting for display GPIO use.
7. Seated eye position, normal reach, desired display sight line, desk depth, and rear-wall/cable clearance.
8. Antenna location and keep-out, enclosure material behavior, fastener stack, print tolerances, and foot height.

## Verification plan

1. **Rotation proof:** identify the display and driver, then test normal and 180-degree output from power-on messages through the Raspberry Pi OS Lite console and the 40×13 SHR-DAW UI. Check text geometry, refresh, blanking/wake, and any touch mapping if touch exists. Preserve a tested rollback before selecting the rotated carrier holes.
2. **Fit and sight line:** build a full-scale nonfunctional card/foam mock-up around measured components and real plugged cables. Confirm seated legibility, reach, cable exits, rear clearance, connector insertion, and access to every service screw.
3. **Air-path prototype:** use a dimensionally representative vented prototype. Confirm front-intake-to-rear-exhaust movement with safe visualisation and local velocity/temperature checks; specifically look for short-circuiting near the rear fan and stagnant zones at the NVMe, Pi underside, power area, and screen corners.
4. **Thermal comparison:** at a recorded ambient temperature, compare open bench, enclosed fan-off, and enclosed fan-on states under repeatable CPU/audio and sustained NVMe-write loads. Log CPU temperature, clocks, throttling flags, NVMe SMART temperature when available, workload stability, and intake/exhaust temperatures. Repeat with the intended grille screen and with realistic cable occupancy. The enclosure is rejected or revised if it introduces throttling, unstable storage, or a material regression from the agreed baseline.
5. **Acoustic/electrical check:** at the seated position, check fan tone, grille turbulence, vibration, and changes across control states. With the normal audio interface and routing, test for fan-correlated electrical or acoustic contamination before accepting the fan power/control arrangement.
6. **Cable and service trial:** perform repeated power, USB, Ethernet, and micro-HDMI insertion/removal with the case restrained only by its feet. Time a display, fan, and NVMe replacement; verify that no step strains the GPIO connection or PCIe ribbon and that reassembly cannot pinch cables into either air path.
7. **Fault checks:** verify safe temperatures and recoverable behavior for a stopped/disconnected case fan, a partially blocked intake, and accidental placement near a rear wall. Define the minimum rear keep-clear distance from evidence, then mark it in later product documentation.

This is a researched enclosure concept, not validated CAD, a fabrication specification, or thermal proof.
