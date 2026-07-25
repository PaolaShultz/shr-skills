## 1. Final design

The resolved product is a compact wedge console, provisionally **214 × 158 × 92 mm** with a 34 mm-high front and a landscape screen at **28° above horizontal**. The rear skirt reaches the tabletop, so the enclosure sits level while the display faces forward and upward.

The display and computer are mechanically decoupled:

- A replaceable top carrier holds a 7-inch-class display.
- A removable internal cassette carries the Raspberry Pi 5, official Active Cooler, and bottom-mounted NVMe board.
- Five front louvers feed air directly into the display–Pi gap.
- A single 40 mm rear fan pulls that air across the display electronics, Active Cooler, Pi, and NVMe.
- USB-A and Ethernet are grouped on the right. Power and service video terminate in a recessed rear cable bay.
- Eight controller keys plus a separate power key form a narrow console strip without obstructing the intake.

This arrangement was selected because it resolves connector access through component orientation, a rear cable gallery, and modular carriers instead of making the whole product—and every service operation—depend on an upside-down assembly.

## 2. Repository and hardware findings

### Verified

- The authoritative repository state inspected was the [commit-pinned tree for `927eb05888951f9955c7d46e856ef7208149bc00`](https://github.com/PaolaShultz/shr-daw/tree/927eb05888951f9955c7d46e856ef7208149bc00); the page displays abbreviated commit `927eb05`. A local clone was attempted, but shell network resolution was unavailable, so no local checkout is claimed.
- At that revision, SHR-DAW describes itself as a Raspberry Pi music workstation built for a **40×13 terminal**. It supports keyboard, mouse, and configured **4-, 5-, or 8-button controllers**. Its principal screens are terminal-style preset, playback, tracker, loop, recording, and metering views—not a conventional high-resolution touch GUI. See the [commit-specific README](https://github.com/PaolaShultz/shr-daw/blob/927eb05888951f9955c7d46e856ef7208149bc00/README.md).
- Raspberry Pi 5 is an 85 × 56 mm-class board with four mounting holes, one native USB-C power input, two micro-HDMI outputs, four USB-A ports, Gigabit Ethernet, microSD, PCIe FFC, two MIPI connectors, RTC, GPIO, and one four-pin fan header. The exact positions and component heights must come from the [official mechanical drawing](https://pip-assets.raspberrypi.com/categories/892-raspberry-pi-5/documents/RP-008347-DS-1-raspberry-pi-5-mechanical-drawing.pdf?disposition=inline) and a physical board.
- The official Active Cooler is approximately **63.5 × 42.5 × 13.7 mm**, uses the Pi fan header, and should not be repeatedly removed because its pads and push-pins degrade. Its rated maximum airflow is 1.09 CFM. [Product brief](https://datasheets.raspberrypi.com/cooling/raspberry-pi-active-cooler-product-brief.pdf).
- Raspberry Pi throttling starts progressively at 80°C and becomes stronger at 85°C. Official fan control steps occur at 50, 60, 67.5 and 75°C. [Raspberry Pi thermal documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#frequency-management-and-thermal-control).
- Pi 5’s J2 pads accept a normally-open external power switch, so the ninth front key can reproduce the native power-button behavior without simulating power removal. [Official power-button documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#power-button).

### Reasonable inferences

- A 40×13 landscape TUI benefits more from a stable landscape presentation and tactile navigation than from making touch the primary input.
- Screen rotation does not require application-layout changes if the terminal dimensions remain 40×13, but boot console, DRM output, mouse, and touch mapping still require system testing.
- Any USB audio interface, MIDI interface, or headphone/line output is a peripheral. Raspberry Pi 5 has **no native analogue audio jack**.

### Explicit assumptions

- The repository view and brief do not identify the exact display, its controller board, the two reported USB-C connectors, NVMe board, SSD, bottom plate, or exhaust fan.
- The top carrier is therefore sized around a provisional **195 × 125 × 18 mm maximum display envelope**. The official 7-inch Touch Display 2—189.32 × 120.24 mm—is the verified sizing surrogate, not a claim about the existing screen. It uses DSI plus GPIO power and has no USB-C sockets. [Touch Display 2 product brief](https://datasheets.raspberrypi.com/display/touch-display-2-product-brief.pdf).
- The provisional NVMe reference is the Pimoroni PIM699 NVMe Base: 87.6 × 56 mm, 7 mm standoffs, M.2 2230–2280 support. [Product page and dimensional drawing](https://shop.pimoroni.com/products/nvme-base).
- The selected exhaust fan is a Noctua NF-A4x10 5V PWM: nominally 40 × 40 × 10 mm, allow 12.5 mm installed depth, 0.07 A maximum, and 5.24 CFM maximum free-air flow. [Manufacturer specifications](https://www.noctua.at/en/products/nf-a4x10-5v-pwm/specifications).

The “two USB-C connectors” in the brief cannot be native Pi connectors. They must belong to the unidentified display, an attached hub, or another peripheral. The two native Pi video connectors are **micro-HDMI**, not USB-C.

## 3. Orientation and connector decision

| Arrangement evaluated | Consequence | Decision |
|---|---|---|
| Rotate the complete display/Pi stack 180° | Moves the reported crowded edge downward, but puts plugs near the tabletop, increases cable bending and strain, worsens service access, and creates a lower hot/dead zone | Rejected |
| Keep the coupled stack and extend every connector | Mechanically simple, but introduces many high-speed connections and poor cable ownership | Rejected |
| Decouple display and Pi carriers | Keeps the screen landscape, directs display cables into a rear gallery, and lets Pi connectors be organized independently | Selected |

**Conclusion:** do not rotate the complete assembly 180° merely to put the crowded edge at the bottom. Keep the UI landscape and operator-correct. For the Touch Display 2 reference carrier, use only the necessary 90°/270° transform to make its portrait-native panel landscape, with its better viewing direction toward the operator.

Raspberry Pi OS supports desktop orientation changes and console KMS rotation, but its documentation warns that console rotation does not necessarily rotate applications that write directly to DRM. Generic USB-touch mapping is also not guaranteed. [Official orientation instructions](https://www.raspberrypi.com/documentation/accessories/touch-display-2.html#change-display-orientation).

### Connector disposition

| Connector | Status and access |
|---|---|
| 2 × USB 3 Type-A, 2 × USB 2 Type-A | Native Pi ports; directly exposed together on the right |
| Gigabit Ethernet | Native; directly exposed beside USB |
| USB-C power | Native Pi socket internally connected to a short, certified 5 A/PD-rated rear panel pigtail; voltage drop must be validated |
| 2 × micro-HDMI | Native. One feeds the rear full-size HDMI service output through a short adapter; the second is internal/service-only or used by an HDMI display variant |
| microSD | Bottom service slot; normally left empty after validated NVMe boot |
| PCIe FFC | Internal to NVMe base; no external access |
| Fan header | Dedicated to the official Active Cooler |
| RTC connector | Accessible after removing the bottom plate |
| GPIO | Internal: display power if required, controller inputs, and rear-fan control; unused pins receive a keyed insulating shroud |
| MIPI connectors | One available for the reference DSI display; the other remains internal |
| J2 power pads | Wired to the separate front power key |
| Display USB-C sockets | Not native Pi ports. If the existing display is retained, both remain inside the 35 mm rear gallery under a removable service cover until their functions and power requirements are identified |
| Audio/MIDI | Supplied by external USB peripherals; no unsupported analogue jacks are added |

## 4. Mechanical and thermal specification

### Geometry and stack

- External envelope: **214 W × 158 D × 92 H mm**, provisional ±3 mm after hardware measurement.
- Front height: approximately 34 mm.
- Screen: landscape, **28° ±2°** above horizontal.
- Display carrier: replaceable laser-cut/SLS insert for panels up to 195 × 125 × 18 mm; 1.5–2 mm edge clearance and compliant pads, with no load placed on the glass.
- Top-to-bottom stack:
  1. display and carrier;
  2. 8–12 mm intake/plenum clearance;
  3. Active Cooler;
  4. Raspberry Pi 5;
  5. 7 mm NVMe Base standoffs;
  6. NVMe Base and SSD;
  7. minimum 6–8 mm lower airflow gap;
  8. insulated 1.5 mm steel bottom plate.
- The Pi cassette is located in the rear half, with its USB/Ethernet edge aligned to the right opening. Power and HDMI cables run in a sealed perimeter raceway rather than across the intake.

### Airflow

- Five front louvers provide a target effective free area of at least **2,800 mm²** after the removable coarse filter.
- Most air enters directly between display and Pi. A splitter sends approximately 25–30% beneath the Pi toward the NVMe.
- The upper stream washes the display controller and feeds the Active Cooler; upper and lower streams reunite at the rear-left fan chamber.
- One NF-A4x10 5V PWM fan exhausts **outward through the rear**.
- The fan mounts on silicone isolators against a foam-gasketed shroud. The grille stands at least 6 mm from the blades and has at least 60% open area.
- Rear bumpers preserve a small exhaust gap; normal operation should still leave 50 mm clear behind the product.
- Closed perimeter seams around the fan chamber prevent exhaust from looping back into the intake.
- The filter slides out from below the front grille without opening the enclosure.

The Active Cooler keeps its native firmware control. The rear fan uses a separately fused 5 V supply and a transistor/PWM interface; it must not be wired in parallel with the Active Cooler header. Tach feedback is monitored separately. A provisional policy is continuous low speed while powered, increasing with CPU or NVMe temperature and going to full speed on fan/temperature warning.

### Structure, controls and appearance

- Front row: eight 12 mm controller keys with replaceable legends, plus a visually separated power key connected to J2.
- Controller keys are provisionally wired as Linux `gpio-keys`; confirmation that their emitted key events match the repository’s controller profiles is required.
- Console character comes from the shallow wedge, horizontal ventilation, restrained button row, dark graphite finish, and narrow walnut-toned side rails. There are no decorative speakers, fake audio jacks, or nonfunctional vents.
- Four 3 mm silicone feet form an approximately 190 × 138 mm footprint.
- The 1.5 mm steel bottom adds low ballast. Rear and side tip resistance must still be measured with the actual screen and cable loads.

### Materials and manufacturing

Prototype:

- SLS PA12 or ASA outer bezel, 2.2–2.5 mm walls with 1.2 mm ribs.
- 1.2 mm folded 5052-H32 aluminium cassette.
- 1.5 mm zinc-plated/powder-coated steel bottom.
- M2.5 heat-set inserts and captive M2.5 fasteners.
- Laser-cut bezel and connector inserts.
- 0.25 mm PET insulation wherever PCBs face metal.

Production candidate:

- UL94 V-0 PC-ABS bezel, nominal 2 mm walls.
- Formed aluminium inner chassis and stamped steel base.
- Fine-texture graphite powder coat, satin-black grille inserts, moulded or veneered side rails.

### Assembly and service

1. Install the display in its replaceable carrier.
2. Fit the Active Cooler permanently to the powered-off Pi.
3. Fit the SSD and NVMe Base, connect the PCIe FFC, and mount the stack to its cassette.
4. Install front keys, J2 power switch, fan and controller wiring.
5. Route display, HDMI, power, and touch cables through edge clips with service loops; do not crease FFCs.
6. Slide the cassette into keyed rails and connect the display and fan.
7. Fit rear insert, insulated bottom plate, filter and feet.

Routine service needs only the bottom plate. Display replacement uses four top-carrier screws. Pi/NVMe removal does not require removing the Active Cooler.

## 5. The picture

![SHR-DAW resolved wedge console](</tmp/ppd-003.WlYDRb/combined/workspace/output/design/shr-daw-console-final.png>)

[Open the final 1536×1024 PNG](</tmp/ppd-003.WlYDRb/combined/workspace/output/design/shr-daw-console-final.png>)

It shows the selected front-right product view, the direct right-side USB/Ethernet bay, and the rear exhaust and cable bay. The rear HDMI connector shown is a panel extension, not a native full-size Pi connector.

The built-in image generator was used once. Its prompt specified one graphite/walnut wedge console, 28° landscape screen, five front louvers, eight controller keys plus power control, direct right-side USB/Ethernet, and a single rear 40 mm exhaust—without alternative concepts, fake audio connectors, labels, or branding.

## 6. Risks and validation

This proposal has not proven fit, temperature, noise, strength, EMC, or manufacturability. Before fabrication:

1. **Hardware audit:** photograph and measure the actual display, every controller-board projection, connector identity, cable-head length, Pi revision, NVMe board, SSD height and cooler installation.
2. **Power integrity:** measure the rear USB-C pigtail’s voltage drop and connector temperature at maximum CPU, SSD, display and USB-peripheral load. Reject the extension if undervoltage events occur.
3. **Display validation:** run SHR-DAW at the intended font and 40×13 terminal size; verify boot console, TUI, mouse and touch coordinates after rotation.
4. **Thermal soak:** log CPU temperature/throttling, NVMe SMART temperature, display-PCB temperature and internal air temperature for at least 60 minutes at 25°C and 35°C ambient.
5. **Fault tests:** unplug the rear fan, stall it, block 50% of the intake, obstruct the rear clearance, and confirm the Active Cooler remains functional and warnings are observable.
6. **Airflow:** smoke-test the Active Cooler discharge direction and adjust the internal splitter so its outlet does not recirculate.
7. **Acoustics:** measure one metre in front at idle and sustained DAW load. The fan’s published free-air figure is not an enclosure result; grille and cavity tones may dominate.
8. **Mechanical tests:** verify a firm screen press does not lift a foot; conduct cable pull, rearward/side tip, repeated service, button-cycle and drop/transport tests.
9. **Electrical safety:** check metal clearances, PET insulation, strain relief, fan-blade guarding, FFC bend radii and cable abrasion.
10. **Wireless performance:** compare Wi-Fi/Bluetooth RSSI with and without the metal chassis; enlarge the polymer radio window if attenuation is material.

## 7. Comparison record

| Record | Resolved value |
|---|---|
| Repository | [PaolaShultz/shr-daw](https://github.com/PaolaShultz/shr-daw) |
| Authoritative commit | `927eb05888951f9955c7d46e856ef7208149bc00`; commit-pinned tree inspected, no local checkout claimed |
| Research date | 25 July 2026 |
| Identified hardware | Raspberry Pi 5; official Active Cooler |
| Reference/assumed hardware | 7-inch-class display envelope using Touch Display 2 dimensions; Pimoroni PIM699 NVMe Base; Noctua NF-A4x10 5V PWM |
| Unknown hardware | Actual display/controller, identities of two reported USB-C ports, SSD, current NVMe/base board, bottom plate and existing fan |
| Display orientation | Landscape; no 180° inversion of complete assembly |
| Screen angle | 28° ±2° above horizontal |
| Connector strategy | Right-side direct USB-A/Ethernet; rear recessed power and service HDMI; display connectors in protected rear gallery; bottom microSD/RTC service |
| Approximate size | 214 × 158 × 92 mm; 34 mm front height |
| Cooling | Five front louvers → display/Pi plenum and NVMe bypass → single rear exhaust |
| Exhaust fan | Noctua NF-A4x10 5V PWM, nominal 40 × 40 × 10 mm, outward rear flow |
| Component stack | Display / plenum / Active Cooler / Pi 5 / 7 mm standoffs / NVMe Base / lower plenum / insulated steel bottom |
| Materials | PC-ABS or SLS/ASA outer shell, folded aluminium cassette, ballasted steel bottom, PET insulation |
| Fabrication route | SLS or FDM prototype plus laser-cut/folded sheet metal; injection moulding and stamping after validation |
| Service access | Removable bottom and rear insert; slide-out Pi/NVMe cassette; separate four-screw display carrier |
| Principal advantages | Correct landscape UI, straight intake path, coherent connector access, low centre of mass, replaceable display interface |
| Principal compromises | One high-current USB-C panel connection needs validation; second HDMI is service-only; actual display still requires measurement |
| Unresolved assumptions | Display mounting and power, generic touch mapping, rear-fan control electronics, GPIO controller compatibility, thermal balance |
| Primary sources | [Commit tree](https://github.com/PaolaShultz/shr-daw/tree/927eb05888951f9955c7d46e856ef7208149bc00), [Pi hardware](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html), [Pi drawing](https://pip-assets.raspberrypi.com/categories/892-raspberry-pi-5/documents/RP-008347-DS-1-raspberry-pi-5-mechanical-drawing.pdf?disposition=inline), [Active Cooler](https://datasheets.raspberrypi.com/cooling/raspberry-pi-active-cooler-product-brief.pdf), [Touch Display 2](https://datasheets.raspberrypi.com/display/touch-display-2-product-brief.pdf), [NVMe Base](https://shop.pimoroni.com/products/nvme-base), [rear fan](https://www.noctua.at/en/products/nf-a4x10-5v-pwm/specifications) |
| Image filename | [`shr-daw-console-final.png`](</tmp/ppd-003.WlYDRb/combined/workspace/output/design/shr-daw-console-final.png>) |