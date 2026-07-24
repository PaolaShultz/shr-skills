# Exact image-generation prompt

```text
Use case: product-mockup
Asset type: polished industrial-design concept presentation board
Primary request: Create one landscape presentation board for the frozen SHR-DAW Console Wedge enclosure concept, a compact Raspberry Pi 5 music workstation. Show the same coherent product in three views: a three-quarter exterior hero view, a cutaway airflow view, and a rear/left-side connector and service view.
Input images: Image 1 is the official Raspberry Pi 5 mechanical drawing, used only as reference for the Pi board and known connector arrangement; Image 2 is the official Raspberry Pi 5 Active Cooler mechanical drawing, used only as reference for the cooler's general envelope. Do not reproduce their dimension annotations and do not treat either drawing as fabrication-ready data.
Scene/backdrop: restrained off-white industrial-design board with a clean grid, generous margins, and subtle warm-gray divider lines.
Subject: a compact professional wedge with a modestly angled 480x320 display surface facing a seated musician, a broad dark lower-front intake grille, warm graphite textured body, thin muted-metal edge accents, and a low rear plinth sitting level with the table. The design should evoke a refined old analog amplified console transformed into a modern small digital mixer, without adding mixer controls.
Exterior view: front-left three-quarter studio render showing the angled display, broad front intake grille, calm monolithic wedge, and low rear plinth.
Airflow cutaway: clean technical cutaway of the same enclosure. Show a GPIO display above the Raspberry Pi 5 and official Active Cooler, with a bottom-mounted PCIe-to-NVMe base and NVMe below. Use clear cool-cyan arrows entering the broad lower-front grille, splitting through the display-to-Pi gap and across the lower NVMe path, rejoining at the rear, and leaving through a small guarded rear exhaust fan and grille. Keep cables clipped away from both air paths.
Connector and service view: rear/left-side three-quarter view of the same rotated-stack concept. Show a recessed left-rear bank with exactly four USB ports and one Ethernet port, and a rear bay with one USB-C power port and exactly two micro-HDMI ports. Show subtle screw lines for a removable display bezel, bottom NVMe hatch, reversible connector bezels, and a removable rear fan cartridge. Show cable departure rearward without clutter.
Style/medium: high-end realistic industrial-design product rendering combined with a precise, readable concept-board diagram; restrained professional presentation, not fantasy concept art and not fabrication CAD.
Composition/framing: 16:9 landscape board. Large exterior hero at left, cutaway centered, smaller rear/side service view at right. Keep all views fully on canvas and visibly depict the same proportions and materials.
Lighting/mood: soft neutral studio lighting, controlled shadows, quiet professional mood.
Color palette: warm graphite, charcoal black, muted aluminum gray, off-white board, cool-cyan airflow arrows; no bright gaming colors.
Materials/textures: fine matte printed-polymer texture, dark perforated grille, subtle metal edge trim, rubber feet; no transparent case.
Text (verbatim): "SHR-DAW CONSOLE WEDGE", "EXTERIOR", "AIRFLOW CUTAWAY", "CONNECTORS + SERVICE", "INTAKE", "EXHAUST", "DISPLAY", "PI 5 + ACTIVE COOLER", "NVME BASE", "USB / ETHERNET", "USB-C POWER / MICRO-HDMI", "CONCEPT — NOT VALIDATED CAD OR THERMAL PROOF"
Constraints: render the concept-warning text prominently and exactly once; use the other labels only where they clarify the three views; keep typography crisp and technical; no dimensions; no invented ports; no added audio jacks; no knobs, faders, keyboard keys, speakers, handles, antennas, or decorative controls; no logos or trademarks; no watermark. The display may show an abstract dark terminal-style 40x13 grid but no additional readable UI copy.
Avoid: generic Raspberry Pi case, gaming PC, RGB lighting, aggressive sci-fi vents, steep tablet stand, oversized rear body, random circuit-board details, extra fans, front-facing cables, exploded-view fragmentation, fabrication tolerances, or claims of thermal validation.
```

## Referenced source assets

- `/tmp/ppd-001-official/pi5-mechanical.png` — Image 1, official Raspberry Pi 5 mechanical drawing rendered locally from the official PDF without edits; reference image.
- `/tmp/ppd-001-official/active-cooler-mechanical.png` — Image 2, official Raspberry Pi 5 Active Cooler mechanical drawing rendered locally from the official PDF without edits; reference image.

## Generation settings

- Tool: `image_gen.imagegen` (built-in image generation).
- Referenced image paths: the two paths above.
- Number of outputs requested: one.
- Size, quality, seed, sampling steps, and underlying image-model identifier: `unavailable` in the built-in tool interface.
