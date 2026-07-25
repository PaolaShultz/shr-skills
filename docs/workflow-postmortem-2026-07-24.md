# Workflow postmortem: self-review, public evidence, and enclosure comparison

Status: **retrospective, public, and privacy-sanitized**

Date: 2026-07-24

## Purpose

This document reconstructs the complete working motion that led from
Fructal Cap Design's self-review through executable contract validation,
real-world evidence publication, and the Raspberry Pi enclosure comparison.

It is a workflow postmortem, not a conversation transcript. It deliberately
omits:

- verbatim conversational wording and incidental clarification questions;
- the identity and implementation details of the private software project;
- private repository paths, operational data, and unpublished evidence;
- conversational details that do not change the engineering record.

The retained material is what a future contributor needs to understand what
was attempted, where an assumption proved incomplete, how that was detected,
what was preserved, how the work corrected itself, and which questions remain
open.

## Evidence vocabulary

- **Provided:** task direction or interpretation supplied by the creator.
- **Reported:** an affected actor's account not independently reproduced here.
- **Observed:** repository history, source, validation output, execution trace,
  or another artifact inspected directly.
- **Inference:** a conclusion derived from provided, reported, or observed
  evidence.
- **Open question:** a material issue that the current evidence does not
  resolve.

## Executive finding

The day developed through five connected layers:

1. clarify and harden the method's own execution contract;
2. convert that contract into deterministic and live model evaluations;
3. document real-world use without exposing private work or overstating
   causality;
4. create a prospective physical-product comparison; and
5. recover that comparison after discovering successive experimental
   confounds.

The strongest result was not a winning score. It was a productive,
self-correcting motion: notice that evidence answers a narrower question than
intended, preserve the valid part, label the limitation, improve the boundary,
and continue without rewriting history.

The most instructive corrections concerned boundaries:

- simplifying an example removed design intelligence;
- generated planning artifacts polluted the public documentation structure;
- a method-loaded prompt author contaminated a supposedly neutral task;
- a temporary `CODEX_HOME` did not isolate host-discovered skills;
- orchestration work was transferred to the creator despite being executable
  by the agent;
- one strong shared prompt created a ceiling effect that hid discovery
  differences;
- package-level scoring conflated design reasoning with image-model behavior;
  and
- separate Fructal Cap Design and Superpowers arms could not test the claim
  that the two are complementary.

These corrections are accomplishments of a successful collaboration. Each one
made the repository, experiment, or claim boundary stronger.

## Starting question and first unresolved gap

**Provided:** The work began as a Fructal Cap Design Review of its own
repository, history, contract cases, validators, live evaluations, and position
among current agent skills and established workflow, service, systems,
human-factors, safety, accessibility, and process-redesign methods.

The requested comparison was to inspect execution contracts rather than
branding and determine:

- what is genuinely distinctive;
- what is widely shared;
- where Fructal Cap Design can appear interchangeable;
- what named alternatives possess that it lacks; and
- which differentiation claims are unsupported.

**Observed:** The work produced a useful practical comparison with
[Superpowers](https://github.com/obra/superpowers), a capability-cluster
account, real-world cases, and explicit claim boundaries. These are preserved
in [Real-world usage and testing](real-world-usage-and-testing.md).

**Open question:** The repository does not yet contain a standalone,
source-complete ecosystem-comparison report matching the full original breadth.
Later empirical work became the dominant motion before that research result
was preserved as a canonical artifact.

**Lesson:** A valuable downstream experiment does not silently complete an
upstream research deliverable. The missing comparison remains open and should
be resumed from its canonical source commit and evidence requirements.

## Phase 1: the method reviewed itself

### Initial contract refinement

The repository history shows a rapid sequence of contract changes:

- [`c70eacc`](https://github.com/PaolaShultz/shr-skills/commit/c70eaccb73470e784c700d8fa5ff39c0a0a9fe45)
  defined Review, Redesign, and Implement execution paths;
- [`d54224b`](https://github.com/PaolaShultz/shr-skills/commit/d54224b9aaa217662ac91d405dbe2ae4549aa6f7)
  hardened explicit modes, modification boundaries, persistence, and
  all-path behavior;
- [`860caf8`](https://github.com/PaolaShultz/shr-skills/commit/860caf89fc0ef556e168f2c53f25fb47c8be077a)
  simplified the ChatGPT demonstration and added synchronization checks;
- [`7986617`](https://github.com/PaolaShultz/shr-skills/commit/7986617e91498002a317a91f4d3f16f7bee44481)
  restored structure lost by that simplification; and
- [`3814c5e`](https://github.com/PaolaShultz/shr-skills/commit/3814c5e2a97ee90479b8591ea1871f71074edc6b)
  restored the six-question cap test and broader design intelligence.

**Observed:** The simplification was mechanically clean but semantically too
aggressive. A shorter demonstration ceased to represent important parts of the
method.

**Recovery:** The lost structure was restored, the canonical skill and embedded
demo were synchronized, and validation began checking the public method rather
than only file shape.

**Lesson:** Concision is not automatically coherence. A derived demonstration
must preserve the complete capability contract even when its surrounding
explanation becomes shorter.

### From prose contract to executable contract

A self-review then identified six concrete weaknesses:

1. modes and mixed-mode behavior were not exercised;
2. explicit mode requests could conflict with outcome-based routing;
3. Review and Redesign could deadlock over harmless incidental read effects;
4. evidence provenance and evidentiary status could collapse together;
5. source provenance and installed-copy drift were not verifiable; and
6. feedback wording assumed a human-facing form even for services, devices, and
   software actors.

The durable design is preserved in
[Fructal Cap Design Contract and Evaluation Design](fructal-contract-validation-design.md).

Implementation followed in:

- [`c047220`](https://github.com/PaolaShultz/shr-skills/commit/c04722092035b27f624b30d7ee5cec9e4be22c56),
  adding package validation, contract fixtures, malformed-package regressions,
  provenance, and installed-copy comparison; and
- [`5c16bb5`](https://github.com/PaolaShultz/shr-skills/commit/5c16bb548023bbd198c5b3e30b6cc8cebb3b635e),
  adding isolated live Codex evaluations, structured result validation,
  disposable fixtures, an offline fake runner, and classified failure modes.

**Inference:** This was successful self-application. The method did not merely
approve itself; it found ambiguity in its own workflow and converted the
findings into deterministic and live regression evidence.

**Limit:** Self-evaluation remains circular. It proves productive
self-correction and contract integrity, not universal correctness.

## Phase 2: practical evidence and method boundaries

### Anonymous software case

**Observed:** A Fructal Cap Design-led cycle on a substantial private software
project found and repaired many cross-step, cross-actor, state-preservation,
recovery, and accessibility problems that had not surfaced during earlier
Superpowers-guided development.

The project remains anonymous in public documentation. The record preserves
the capability distinction:

> Fructal Cap Design discovers and bounds the complete constrained-workflow
> problem; software-delivery skills provide strong planning, debugging,
> test-driven implementation, review, and completion mechanics.

**Inference:** The important result was not that one method invalidated the
other. Fructal Cap Design changed the inspection boundary and exposed
complete-flow problems; Superpowers remained valuable for disciplined
implementation mechanics. The methods are more complementary than
interchangeable.

### Public Raspberry Pi and experimental-audio cases

The public evidence was expanded to include:

- [SHR-DAW](https://github.com/PaolaShultz/shr-daw), where the method operated
  across musician, controller, audio service, software, storage, device,
  ownership, failure, and recovery boundaries; and
- [Moj Sint](https://github.com/PaolaShultz/moj-sint), where a convergent
  preservation-first experimental pattern appeared without evidence that the
  Fructal Cap Design skill itself had been invoked.

This distinction matters:

- SHR-DAW is an explicit application case.
- Moj Sint is capability convergence, not causal proof.

## Phase 3: public-repository cleanup

### Documentation ownership correction

**Observed:** Design and implementation-plan artifacts generated through a
software-delivery workflow landed under `docs/superpowers/`. This made a
third-party workflow name appear to own durable Fructal Cap Design
documentation and left a public link pointing at the wrong location.

**Recovery:** Commit
[`d100ae6`](https://github.com/PaolaShultz/shr-skills/commit/d100ae685ccccd0fc59f7cf8699ed24bdc6a792a)
moved the durable contract design to its canonical repository-owned path,
removed transient plan/spec artifacts from the public tree, and repaired the
link.

**Lesson:** The tool that helps produce a document does not own the document.
Durable artifacts belong to the domain and repository they describe.

## Phase 4: the physical-product experiment

### Prospective protocol

The creator proposed a Raspberry Pi music-workstation enclosure with:

- a forward-facing inclined screen;
- front intake through the display/Pi gap;
- cooling attention for the display, CPU, and bottom NVMe layer;
- a rear 5 V exhaust fan and floor-level rear heel;
- an analog-console or restrained digital-console character; and
- a connector-orientation problem requiring whole-stack rotation analysis.

The [Physical-product design comparison
protocol](physical-product-comparison-protocol.md) was committed in
[`b9eec17`](https://github.com/PaolaShultz/shr-skills/commit/b9eec17fd7886e96299075a420b856a80c32d104)
before evaluation. It froze source commits, expected capabilities, a common
task, run discipline, scoring, and claim boundaries.

The first control artifacts were preserved in
[`d46ad38`](https://github.com/PaolaShultz/shr-skills/commit/d46ad38afa2ac4ade4aba9355e0e0f521c9306c2).

### First confound: prompt-author contamination

**Mistaken assumption:** A task could be treated as neutral because the later
execution thread did not load Fructal Cap Design.

**Signal:** While the control was still running and before its result was
deliberately inspected, the creator noticed that the earlier prompt-authoring
thread had Fructal Cap Design loaded.

**Observed:** The shared prompt already contained unusually complete
constraint-source, actor, state, recovery, accessibility, and verification
coverage aligned with the method.

**Consequence:** The pair could no longer test independent constraint
discovery from the rough request.

**Recovery:** The result was not discarded or relabelled as clean. [Protocol
amendment 01](evaluations/physical-product-comparison/protocol-amendment-01.md),
committed in
[`38d126c`](https://github.com/PaolaShultz/shr-skills/commit/38d126cabc36d9e6d28d0b0d527c6db3adeac08f),
narrowed the valid question to execution over a strong method-influenced brief
and reserved a separate discovery comparison.

The first treatment run was then preserved in
[`449a4ef`](https://github.com/PaolaShultz/shr-skills/commit/449a4ef0ed8c470746a3a23239315d52adcc4040).

**Lesson:** Prompt authorship is part of the treatment. Method influence before
the nominal execution boundary must be frozen and evaluated, not treated as
background.

### Orchestration handoff correction

**Initial motion:** Experimental setup was first expressed as commands the
creator could run, even though the agent could access the relevant repositories
and execute the work directly.

**Correction signal:** The creator pointed out that this divided ownership
unnecessarily and made the experimental state harder to follow.

**Recovery:** The agent resumed ownership of the executable work: inspecting
the environment, freezing inputs, launching isolated runs, preserving
artifacts, creating the blind evaluator, validating the archive, and committing
the public record.

**Lesson:** A request for methodological control does not imply a handoff of
mechanical execution. The agent should own in-scope orchestration and present
the creator only with decisions that genuinely require creator judgment.

### Second confound: incomplete skill isolation

**Mistaken assumption:** A temporary workspace and isolated `CODEX_HOME` would
produce a user-skill-free Codex session.

**Signal:** The supposedly clean prompt-author run invoked Superpowers.

**Observed:** Its actual developer payload still discovered Superpowers through
the normal `HOME`. Neither `--ignore-user-config` nor `--ignore-rules` removed
that host-level discovery.

**Recovery:**

1. preserve the first output as a real Superpowers prompt-authoring arm;
2. isolate both `HOME` and `CODEX_HOME`;
3. run a diagnostic that returned `NONE` for non-system skills;
4. create separate homes and workspaces for each execution arm;
5. verify `NONE`, Superpowers only, and `fructal` only before execution; and
6. run all three conditions concurrently from a byte-identical prompt.

This recovery is recorded in [protocol amendment
02](evaluations/physical-product-comparison/protocol-amendment-02.md).

**Lesson:** Configuration flags and temporary directories are not evidence of
isolation. The actual injected capability set must be inspected under the exact
execution boundary.

## Phase 5: three-arm execution and blind evaluation

The recovered `ppd-002` run used:

- the same Codex CLI, model, reasoning level, execution prompt, and source
  commit;
- separate isolated homes, Codex homes, and workspaces;
- no user skill, Superpowers only, and Fructal Cap Design only conditions; and
- a separate no-user-skill blind evaluator with anonymized inputs.

Direct `git clone` encountered the same sandbox DNS restriction in every arm.
Each arm independently continued through commit-pinned web inspection without
harness intervention. Because the restriction was common, it did not create a
condition-specific advantage.

The complete frozen record is preserved in the
[`ppd-002` three-arm execution
comparison](evaluations/physical-product-comparison/ppd-002-discovery/).

### Result

| Arm | Blind score | Main strength | Main weakness |
| --- | ---: | --- | --- |
| Superpowers only | 39/40 | Strongest integrated written engineering argument | Cutaway contradicted the written airflow and cooler geometry |
| Fructal Cap Design only | 38/40 | Strongest image-to-text agreement and explicit fan-failure handling | Four-inch repeated-use risk and incomplete state-preserving service |
| No user skill | 38/40 | Strongest musician-facing controls and service modularity | Unresolved display-power and internal-HDMI consequences |

The evaluator explicitly treated the one-point spread as judgment uncertainty,
not superiority.

### Ceiling effect

**Observed:** The clean prompt author expanded the rough request into a
comprehensive 981-word prompt that already required most scoring dimensions.

**Inference:** A capable model could reach near-ceiling coverage without a user
skill, leaving little room to observe incremental method effects.

**Recovery:** The result was labelled an execution comparison over a strong
shared prompt, not a discovery comparison.

**Lesson:** A strong common brief improves final output comparability while
simultaneously reducing sensitivity to discovery capability. Those are
different experimental goals and require different designs.

### The treatment missed its own contract

All three arms omitted a formal untouched-state inventory and before/after
comparison for service and reassembly.

This was particularly material for Fructal Cap Design because untouched-state
verification is an explicit skill capability.

**Lesson:** Loading the correct contract does not prove every protected
capability will appear in the output. Evaluation must test contract expression,
not only package availability and mode selection.

## Phase 6: evaluation attribution was still incomplete

After the blind result was frozen, the creator identified another limitation:
the experiment did not independently evaluate the prompt-author outputs or
separate written design quality, image-generation instruction quality, and
image-model compliance.

The current package score is still valid. It measures what was delivered.
However, a visual contradiction may originate in:

- the underlying design;
- the instruction sent to the image generator;
- stochastic noncompliance by the image model; or
- failure to notice and correct the rendered defect before delivery.

Treating those as one method score weakens causal attribution.

[Protocol amendment
03](evaluations/physical-product-comparison/protocol-amendment-03.md) therefore
defines five future evaluation layers:

1. rough request to authored prompt;
2. prompt to written design;
3. written design to image instruction;
4. image instruction to rendered image; and
5. complete delivered package.

It also reserves a fourth Fructal Cap Design plus Superpowers condition.

**Lesson:** Separate methods cannot demonstrate complementarity. A combined arm
requires its own prospectively frozen ownership, invocation-order, conflict,
and verification contract.

## Phase 5: layered completion

The collaboration then completed that reserved work in
[PPD-003](evaluations/physical-product-comparison/ppd-003-layered-comparison/).
This remained an enjoyable, ambitious, self-correcting experiment: a prospective
protocol was pushed before the combined result existed, the exact PPD-002
prompt bytes were reused, an invalid skill diagnostic was corrected before
launch, and one evaluator transport failure was preserved and replaced under
the frozen rule.

The layered result clarified rather than repudiated the earlier work. All four
written designs scored 38–39, while instruction and render layers separated
substantially. The combined condition strengthened service, recovery, and
untouched-state reasoning but lost several of those decisions at the image
handoff. Superpowers retained the only full inspect–correct–reinspect render
loop. This locates the most recoverable improvement in coverage checking and
QC closure, not in abandoning either method.

## Correction and recovery table

| Stage | Initial assumption | Correction signal | What it changed | Recovery | Future safeguard |
| --- | --- | --- | --- | --- | --- |
| Demonstration simplification | Shorter meant equivalent | Six-question and workflow structure disappeared | Public demo underrepresented the method | Restore structure and synchronize against canonical source | Validate semantic capability presence, not only textual compactness |
| Contract quality | Clear prose was enough | Modes, evidence dimensions, read effects, and installed drift were untested | Ambiguity could recur without detection | Add contract cases, malformed fixtures, package validation, and live evaluations | Deterministic contract gates plus isolated live checks |
| Ecosystem research | Downstream practical evidence could stand in for the original comparison | No standalone broad comparison artifact exists | The initial research deliverable remains incomplete | Record the gap explicitly | Freeze and publish research output before opening a new empirical branch |
| Documentation ownership | Tool-generated plan paths were acceptable public locations | Durable Fructal Cap Design docs appeared under `docs/superpowers/` and a link failed | Repository identity and navigation became misleading | Move canonical design to repository-owned docs and remove transient plans | Domain owns durable artifacts; tools do not |
| Neutral prompt | Only execution-arm skill state mattered | Prompt author had Fructal Cap Design loaded | Discovery comparison was contaminated | Preserve result, amend protocol, narrow valid claim | Include prompt authorship inside treatment boundary |
| Work ownership | Creator should run isolation mechanics | The creator identified unnecessary divided ownership | Experimental state was harder to follow | Agent took ownership of orchestration and artifact freezing | Delegate only genuine product, authority, or access decisions |
| Clean Codex environment | Temporary `CODEX_HOME` was sufficient | Superpowers appeared in the developer payload | Supposed control was not clean | Isolate `HOME` and `CODEX_HOME`; diagnose exact skill set | Verify actual injected capabilities under exact launch boundary |
| Ignore flags | `--ignore-user-config` and `--ignore-rules` removed user skills | Diagnostics still listed Superpowers | False confidence in command-line isolation | Stop relying on flags as proof | Behavior and payload inspection outrank flag names |
| Contaminated output | A failed control should be deleted | Output had useful provenance as a Superpowers arm | Deletion would lose evidence | Freeze and relabel honestly | Preserve first, classify second |
| Shared prompt | More complete meant more discriminating | All arms scored 38–39 | Ceiling effect masked discovery differences | Narrow to execution comparison | Use separate execution and raw-request discovery experiments |
| Skill availability | Correct package and mode would express all capabilities | Treatment omitted untouched-state verification | Protected capability did not reach output | Record shared miss and treatment-specific consequence | Score explicit contract expression |
| Final scoring | Package score represented method quality | Render errors contradicted strong prose | Method and image-model attribution collapsed | Add layered prompt/design/image evaluation | Score every transformation and the final package separately |
| Method comparison | Separate Fructal Cap Design and Superpowers arms tested their relationship | Complementarity claim remained untested | Comparison could imply opposition by omission | Reserve combined fourth arm | Include the interaction condition prospectively |
| Quantitative evidence | A high package score fully answered the research question | The creator identified missing attribution layers | Visible quality did not distinguish prompt, design, image instruction, and renderer behavior | Preserve the score and add layered evaluation | Pair outcome measures with interpretive review of what they actually measure |

## Actor and ownership map

| Actor | Legitimate responsibility | Boundary revealed | Corrected boundary |
| --- | --- | --- | --- |
| Creator and affected musician/operator | Product intent, interpretive insight, prioritization, physical acceptance | Was temporarily given executable orchestration that the agent could own | Retain product decisions and interpretation; return executable mechanics to the agent |
| Primary Codex agent | Repository inspection, experiment orchestration, evidence preservation, validation, documentation | Initially externalized runnable steps and accepted insufficient isolation assumptions | Own in-scope execution through verified publication |
| Prompt-author run | Transform the rough request into a task | Its method state was initially outside the experimental model | Treat prompt authorship as an explicit experimental layer |
| Execution-arm model | Research and produce written and visual design artifacts | A correct available-skill set did not guarantee complete contract expression | Evaluate output behavior, not availability alone |
| Image model | Render the supplied visual instruction | Could omit or contradict ports, airflow, power, or geometry | Preserve and score exact image instruction separately from image compliance |
| Blind evaluator | Compare anonymized delivered packages | Aggregate rubric could not isolate where visual defects originated | Apply layered evaluation with equal evidence access |
| Repository validators | Detect deterministic contract and documentation drift | Could not assess human experience or physical validity | Keep deterministic scope explicit; require affected-actor and physical gates separately |

## The “million bees” observation

The Croatian expression *milijun me pčela ubolo* communicates two facts:

1. there were many bees or many stings; and
2. the person experienced the event as if there were a million.

The metaphor is useful here as a model of layered interpretation, not as an
emotional analogy between mistakes and bee stings.

The first reading of the work is the observable repository record: many
commits, discoveries, diagnostics, reruns, artifacts, amendments, scores, and
corrections.

The second reading reveals what that list alone does not: the work formed an
enjoyable, ambitious, self-correcting collaboration. Mistakes became evidence;
corrections improved the method and experiment; and noticing a confound was an
accomplishment rather than a defeat.

The same distinction applies to the evaluation. A `38/40` score describes the
visible package. Reading beneath it reveals that the experiment still needed
better attribution layers—and that the collaboration successfully noticed
this before turning a narrow result into a broad claim.

## Recovery pattern that worked

Across the successful corrections, one reusable sequence emerged:

1. **Stop at the first credible boundary violation.**
2. **Preserve the affected artifact before changing interpretation.**
3. **Separate what was provided, reported, observed, inferred, and unknown.**
4. **Name the exact experimental or workflow question the evidence can still
   answer.**
5. **Locate the real source of the boundary failure.**
6. **Build a diagnostic that tests that source directly.**
7. **Resume from a frozen input under a verified boundary.**
8. **Append the correction without rewriting the earlier record.**
9. **Validate source, artifacts, links, checksums, and remote state.**
10. **Keep physical and affected-actor acceptance open until directly tested.**

This sequence is more important than appearing to have made no mistakes.

## What remained untouched

The recovery deliberately preserved:

- the exclusive Review, Redesign, and Implement modes;
- explicit modification boundaries;
- the constraint-and-motion principle;
- evidence provenance separate from evidentiary status;
- broad actor coverage;
- constraint-source analysis;
- failure and recovery as distinct concerns;
- accessibility in normal and recovery paths;
- the six-question cap test;
- before/after and untouched-state verification as protected capabilities;
- frozen prompts, raw responses, images, hashes, and blind mappings;
- the anonymity of the private case;
- the distinction between concept evidence and physical proof.

## Current state

### Completed and verified

- Fructal Cap Design has deterministic package and contract validation.
- Its embedded demonstration is synchronized with the canonical source.
- Isolated live model evaluations exercise mode and modification contracts.
- Real-world evidence and limitations are publicly documented.
- Durable documentation is stored under repository-owned paths.
- The original two-arm enclosure artifacts are frozen.
- Prompt-author contamination and host-skill contamination are recorded.
- The recovered three-arm execution comparison is frozen, checksummed, blindly
  evaluated, committed, and published.
- The package-level result and its attribution limits are separated.

### Valid but narrow

- `ppd-001` can compare execution over a method-influenced prompt, not clean
  discovery.
- `ppd-002` can compare three execution conditions over one strong neutral
  prompt, not independent problem discovery.
- The blind scores describe delivered packages, not isolated method causality.
- Real-world cases support practical value, not universal superiority.

### Open

1. Complete and publish the original broad ecosystem comparison from primary
   sources.
2. Design a second pass with randomized, anonymous human review of every
   design, preserving small imperfections, whole-product failures, and
   prompt/rubric omissions that model evaluation did not surface.
3. Execute every frozen image instruction with at least one independent image
   renderer under equal attempt and correction rules, so repeated prompt
   defects can be distinguished from renderer-specific artifacts.
4. Run a later four-condition discovery comparison from the creator's minimally
   wrapped rough request.
5. Complete the pending blind evaluation of the original `ppd-001` pair.
6. Build CAD and physical prototypes before making enclosure fit, thermal,
   acoustic, electrical, service, or musician-acceptance claims.

## Claim boundary

This postmortem supports the following conclusions:

- the project can detect and recover from method, documentation, orchestration,
  isolation, and evaluation-boundary failures;
- Fructal Cap Design can be productively applied to its own execution motion;
- the public repository preserves unusually complete evidence for the
  enclosure execution comparison; and
- creator interpretation revealed experimental layers that artifact scores
  alone did not.

It does not establish:

- that every mistake in the full conversation has been reconstructed;
- that Fructal Cap Design is generally superior to Superpowers or no-skill
  execution;
- that the broad ecosystem comparison is complete;
- that one day's self-directed work is independent validation;
- that the enclosure designs are physically valid; or
- that future discovery runs will favor any condition.

## Source map

- [Fructal Cap Design Contract and Evaluation
  Design](fructal-contract-validation-design.md)
- [Real-world usage and testing](real-world-usage-and-testing.md)
- [Physical-product design comparison
  protocol](physical-product-comparison-protocol.md)
- [Protocol amendment 01: prompt-author
  contamination](evaluations/physical-product-comparison/protocol-amendment-01.md)
- [Protocol amendment 02: host-skill isolation and three-arm
  extension](evaluations/physical-product-comparison/protocol-amendment-02.md)
- [Protocol amendment 03: separate prompt, design, and rendering
  evidence](evaluations/physical-product-comparison/protocol-amendment-03.md)
- [`ppd-002` three-arm execution
  comparison](evaluations/physical-product-comparison/ppd-002-discovery/)
- [PPD-003 layered four-arm
  comparison](evaluations/physical-product-comparison/ppd-003-layered-comparison/)
