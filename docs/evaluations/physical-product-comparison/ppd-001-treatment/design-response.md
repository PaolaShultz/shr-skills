# SHR-DAW final enclosure concept

## Fructal Cap Design Redesign

**Mode: Redesign.** This is a research concept and verification plan. It does
not modify SHR-DAW or its hardware, and it is not validated CAD, a fabrication
drawing, or thermal proof.

## Intended outcome and evidence boundary

The enclosure should let a seated musician place the unit, connect it, read it,
and keep cables out of the playing area in one obvious motion. It should also
let an assembler or service technician reach the display, Raspberry Pi, Active
Cooler, NVMe assembly, fan, and connectors without turning routine service into
a near-total teardown. The software maintainer is a third actor because the
selected physical orientation may depend on display-driver rotation. The Pi,
NVMe, display, and both fans are affected actors in the thermal path.

`Provided`: the required stack, wedge character, broad front intake, rear
exhaust, low level plinth, service requirements, and unresolved connector
orientation.

`Observed`: the frozen SHR-DAW documentation describes a 2 GB Raspberry Pi 5,
official Active Cooler, 27 W supply, bottom PCIe-to-NVMe base, 128 GB NVMe, and
480×320 GPIO display. It says the Pi 5 hardware is not installed or measured,
the GPIO display prevents a top M.2 HAT, and exact housing dimensions and CAD
must wait for measurement of the physical stack. The official Raspberry Pi 5
and Active Cooler drawings give approximate reference envelopes, explicitly
not production data. Official Raspberry Pi OS documentation describes KMS
rotation for supported display outputs, but that does not prove that this
unknown GPIO display, its boot path, framebuffer, driver, or SHR-DAW terminal
will rotate correctly.

`Inference`: a direct rear/side port exposure is mechanically simpler and more
recoverable than filling a small enclosure with USB, Ethernet, power, and HDMI
panel extensions. A slightly negative-pressure front-to-rear path can cool the
whole stack only if the screen, cooler, Pi, and NVMe do not form bypasses or
dead zones.

`Open question`: the exact display model and driver, complete stack envelope,
port clearances, Active Cooler flow interaction, NVMe-base geometry, case-fan
electrical source, and measured thermal/acoustic performance are unavailable.

There is no existing enclosure sequence to validate. The nearest documented
sequence is an intended stack awaiting physical assembly and measurement.

## Constraint and friction analysis

The highest-priority friction is cable placement. If frequently used USB and
Ethernet ports face the musician or discharge sideways near the front, cable
plugs, loops, and strain occupy the same space as playing and viewing. The
consequence and frequency are high, and recovery would otherwise require
adapters or a new shell.

Second is thermal short-circuiting. A local CPU cooler does not by itself prove
air reaches the Pi power and I/O areas or the bottom NVMe. A rear fan can also
pull mostly from a nearby leak instead of the front grille. The consequence is
high, its frequency is continuous, and the fault is hard to see without
instrumentation.

Third is coupled service. A monolithic shell or trapped fastener stack could
require removal of the display to reach the NVMe, removal of the Pi to reach
the fan, or disturbance of GPIO and PCIe connections for a simple replacement.
The consequence is medium to high and recovery carries connector and cable
damage risk.

Fourth is treating software rotation as a settled mechanical fact. An
unsupported or partial rotation path could leave boot diagnostics or the TUI
upside down. The consequence is high but it is recoverable before fabrication
if made an explicit gate.

## Selected concept and orientation

Select the **rear-I/O rotated-stack orientation** for the concept: rotate the
complete Pi/display/NVMe stack 180 degrees from its presumed display-native
assembly direction so the USB/Ethernet bank is exposed directly through a
recessed rear connector bay. Put the adjacent USB-C power and micro-HDMI edge
in a recessed right-rear side bay, with cables guided rearward rather than
across the musician's work surface. This handedness is an explicit ergonomic
assumption to verify with the real boards and cables.

The display remains above the Pi in a modestly inclined upper deck facing the
seated musician. The enclosure is a compact, stable wedge: a restrained dark
warm-grey body, softly radiused side cheeks, a thin display bezel, minimal
high-contrast legends, and a broad horizontal front grille. Its visual
reference is an old amplified analog console reduced to the essentials and
refined as a modern digital mixer—not a computer tower, gaming case, or generic
Pi box. The rear extends into a low plinth whose feet establish a level,
non-rocking table plane.

This orientation is selected, not yet validated. **Fabrication release is
blocked until the exact GPIO display proves an upright boot-to-application
path after 180-degree software rotation.** If that test fails, retain the outer
wedge, airflow path, and service architecture, but re-index the internal stack
and redesign the removable connector inserts from measured geometry. Do not
bury the uncertainty in permanent panel extensions or claim that generic KMS
documentation proves compatibility.

Before, connector and display orientation are unresolved and could force the
musician to manage cables around the active surface. After the proposed
motion, normal USB/Ethernet cables enter one labelled recessed rear bay, power
and diagnostic display cables enter the adjacent rearward-facing side bay, and
the musician sees one upright display and one clear front-to-rear ventilation
direction. The remaining rotation decision is a visible pre-fabrication gate.

## Airflow arrangement

Use the broad lower-front grille as the only intentional room-air inlet. Behind
it, a shallow full-width intake plenum spreads air rather than aiming a narrow
jet only at the CPU. A removable coarse dust screen may be tested, but no
filter is assumed until its pressure loss and cleaning interval are measured.

From the front plenum, divide the flow with shaped, removable guide surfaces:

- an upper path crosses the open gap between the display and Pi and supplies
  the Active Cooler without enclosing or opposing its unknown measured flow;
- a lower path passes along the Pi underside and bottom NVMe base, with real
  clearance around the drive and adapter rather than a decorative slot; and
- both paths rejoin in a rear exhaust chamber pulled by the proposed small 5 V
  fan through a guarded rear grille.

Seal unintended large gaps around the rear connector inserts so the exhaust fan
cannot bypass the front intake. Keep cable bundles against side channels and
out of both air paths. Mount the rear fan on an independent gasketed cassette
with vibration isolation; do not let the shell become its sounding board. The
case fan assists whole-volume exchange while the official Active Cooler
retains local cooling. Neither airflow direction nor thermal adequacy is
claimed until smoke-flow and instrumented load tests confirm it.

The front and rear open areas must be sized from the selected fan's measured
pressure-flow curve and acceptable noise, not from appearance alone. The
passive openings must also avoid an abrupt unsafe state if the case fan stalls;
degraded operation may throttle, but the enclosure must not depend on an
unobservable single fan to prevent damage.

## Connector and cable arrangement

Expose the Pi connectors directly wherever the measured stack permits:

- a recessed rear bay for the four USB ports and Ethernet, with finger room,
  plug-body clearance, visible labels, and space for normal cable bend radii;
- a recessed right-rear side bay for USB-C power and the two micro-HDMI ports,
  shaped so the official power plug exits rearward and is not the enclosure's
  load-bearing foot; and
- removable, separately printable bay inserts, so measured cut-outs can change
  without replacing the main shell.

Do not add imagined audio, MIDI, storage, switch, or display ports. Do not
assume a GPIO pin is free for the case fan merely because a 5 V fan is proposed:
the display already occupies the GPIO region. Choose the fan supply, connector,
protection, control behavior, and safe shutdown state only after the display
wiring and power budget are known. Use keyed internal plugs and strain relief;
do not solder the fan or display permanently into the shell.

Keep external cables outside the intake mouth and feet. A shallow rear cable
ledge in the plinth can support bend radius and strain relief without enclosing
plugs or forcing a particular cable diameter. The unit must remain stable with
the heaviest expected rear and side cable set attached.

## Service arrangement

Organize service as three independent motions, always after clean shutdown and
power disconnection:

1. The upper display deck lifts as one retained-fastener module. The display is
   mounted to its underside with a measured bracket and a short, restrained
   service loop, giving access to the GPIO connection and Active Cooler without
   peeling adhesive or balancing a loose screen.
2. A captive-fastener bottom hatch in the level plinth exposes the NVMe drive
   and its base fasteners. Drive replacement must not require removing the
   display or Pi unless the measured base itself makes that intrinsic.
3. The rear fan cassette withdraws from the rear after unplugging one keyed
   connector. Its guard, fan, vibration mounts, and grille can be cleaned or
   replaced without disturbing GPIO or PCIe.

The front grille/dust screen releases separately for cleaning. Internal cable
clips are releasable and leave visible service slack. Use distinct fastener
lengths only when unavoidable, and mark their locations inside the removable
panels. Preserve access to the Pi fasteners and all connectors; do not use the
outer shell as a permanent clamp on the electronics stack.

## Assumptions, risks, and required measurements

Assumptions to test are that the rotated connector bays land at the rear and
right-rear without cable collisions; the display is readable at a modest fixed
incline; direct port access is possible; a front-to-rear pressure path can
reach both levels; and the wedge remains stable under cable pull. The finish,
shell process, wall construction, fasteners, fan size, grille geometry, and
display angle are deliberately not fixed.

Measure the real display PCB and visible area, header/ribbon position, backlight
and driver hardware, viewing angles, touch or control clearances if any, and
the boot-to-SHR rotation behavior. Measure the assembled X/Y/Z envelope and
mounting points of the Pi, cooler, standoffs, bottom base, PCIe ribbon, NVMe,
thermal pads, and every protruding component. Measure plug bodies and safe bend
radii for the official USB-C supply and representative USB, Ethernet, and
micro-HDMI cables. Measure the selected case fan's envelope, voltage/current,
connector, flow direction, pressure-flow behavior, starting behavior, noise,
and control/supply compatibility.

Material risks are display rotation failure; GPIO or PCIe strain; fan and
Active Cooler interaction; recirculation through connector gaps; an NVMe dead
zone; fan tonal noise transmitted by the shell; dust loading; RF/EMI effects
from any conductive structure; inaccessible fasteners; cable-induced tipping;
and an attractive grille that fails finger, debris, or structural protection.

## Verification plan

1. **Freeze measured geometry.** Photograph and measure every stack component,
   port, fastener, plug, keep-out, and cable path. Reconcile those measurements
   against the official reference drawings. Build a full-scale nonfunctional
   volume mock-up before dimensional CAD.
2. **Resolve rotation before enclosure CAD.** Identify the display model,
   controller, connection protocol, framebuffer/DRM path, and driver. In a
   reversible test configuration, verify upright output from firmware/boot
   diagnostics through console startup and SHR-DAW at 480×320. Power-cycle,
   reboot, recover from a bad setting, and confirm the original configuration
   can be restored. Test the physical 180-degree stack only if this passes.
3. **Check musician motion and accessibility.** At a table, test display
   legibility from representative seated positions, glare, reach, port labels,
   one-handed plug insertion where reasonable, two-handed high-force plugs,
   cable clearance, foot stability, and cable-pull tipping. Include users with
   differing reach, vision, and motor control where available; do not infer
   their acceptance from the designer's use.
4. **Prototype the air path.** Use a nonfinal vented shell with interchangeable
   baffles and connector inserts. Confirm direction and dead zones with smoke
   or threads, then instrument CPU, RP1/power area where practical, NVMe SMART
   temperature, clocks, throttling, and fan state during idle, sustained
   SHR-DAW-representative load, storage activity, and combined load at recorded
   ambient conditions. Compare case-fan on, case-fan failed/off, partial intake
   obstruction, and dust-screen states. Check that the two fans do not fight.
5. **Measure acoustics.** Record fan speed/control state, distance, background,
   tonal components, vibration, and perceived distraction at the musician's
   position. Try isolation and grille/baffle changes before increasing fan
   speed. Human listening is required for acceptance.
6. **Exercise normal and recovery service.** Repeatedly clean the front screen,
   remove and refit the fan cassette, access the NVMe, open the display deck,
   and reconnect GPIO/PCIe using documented shutdown and ESD precautions.
   Verify that interruption leaves no hanging panel or strained cable, wrong
   fastener use is hard to make, and a failed replacement can return to the
   previous known-good part without disturbing unrelated assemblies.
7. **Verify source-of-truth continuity.** Record the accepted orientation,
   measured drawings, display rotation configuration and rollback, fan part and
   electrical route, cable examples, thermal/acoustic results, and service
   sequence together. Hand the prototype and record to another assembler and
   repeat the setup and service checks. Keep SHR-DAW software, user data,
   hardware configuration, and unrelated accessories unchanged throughout
   enclosure evaluation.

## Six-question cap test

1. **One clear result:** yes—the musician connects at the recessed rear/side,
   sees the display, and leaves the front clear.
2. **Coherent motion:** yes—the port orientation, airflow direction, and
   service layers agree; display rotation remains a visible gate rather than a
   hidden assumption.
3. **Constraint without obstruction:** yes in concept—the GPIO display,
   bottom NVMe, cooling, and connector edges determine the shell and access
   panels without making daily use absorb their complexity.
4. **Context and position preserved:** yes—the stack relationships and direct
   ports remain intact, while independent panels preserve service position and
   cable intent.
5. **Feedback and recovery:** supported—the screen provides ordinary operating
   feedback; removable inserts, retained panels, keyed plugs, and reversible
   rotation testing provide nearby recovery. Thermal feedback still requires
   the planned instrumentation and cannot be claimed from the concept.
6. **Only intrinsic effort remains:** mostly—power disconnection, ESD care,
   cable clearance, and component measurement are intrinsic. The unavoidable
   tradeoff is that the final connector cut-outs and display orientation cannot
   be settled honestly before the exact hardware is measured and its driver is
   tested.
