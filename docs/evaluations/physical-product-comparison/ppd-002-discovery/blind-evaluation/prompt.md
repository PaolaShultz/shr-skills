Evaluate three anonymized physical-product design results:

- `A-response.md` with `A-image.png`
- `B-response.md` with `B-image.png`
- `C-response.md` with `C-image.png`

Do not inspect files outside the current workspace. Do not try to identify what
method, skill, or prompt history produced an arm. Judge only material present in
each response and image. Inspect all three images directly. Separate written
reasoning quality from image-generation quality.

Score every dimension from 0 to 4. The anchors are:

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

Use 1 and 3 for performance between the stated anchors. The dimensions have
equal weight and the maximum is 40.

For each arm:

1. give the ten raw scores;
2. give one short evidence statement per score;
3. calculate and verify the total;
4. separately assess whether the image agrees with the written design;
5. identify unsupported or internally inconsistent claims; and
6. state the most consequential strength and weakness.

Then provide:

- overall ranking with tied results allowed;
- score differences that are actually material rather than cosmetic;
- a useful capability found only in each arm, if any;
- a requirement all arms missed;
- unsupported claims in any arm;
- whether any design is preferable for a real musician and why;
- confidence and limitations, including stochastic image variance and the lack
  of physical measurements or a prototype.

Write the complete evaluation to `blind-evaluation.md`. Do not modify the six
input artifacts.
