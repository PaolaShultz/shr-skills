# Real-world usage and testing

Fructal Cap Design has four distinct kinds of practical evidence:

1. it was applied to its own execution contract and produced regression-tested
   improvements;
2. it found latent workflow failures in an anonymous private software project
   already using a disciplined software-delivery skill suite;
3. it drove a public musician/operator workflow audit and repair across the
   software, controllers, audio services, storage, and Raspberry Pi environment
   of [SHR-DAW](https://github.com/PaolaShultz/shr-daw);
4. its capability cluster independently appeared in the experimental workflow
   of [Moj Sint](https://github.com/PaolaShultz/moj-sint), without evidence that
   the Fructal skill itself was invoked there.

These cases demonstrate practical utility at different boundaries. They do not
establish a universal success rate or independent validation across every
technical, physical, service, or operational domain.

## Evidence vocabulary

This document keeps provenance and evidentiary status separate:

- `provided/reported` records a statement from a creator, operator, or other
  affected actor;
- `observed` records repository history, source, tests, machine behavior, or
  another artifact inspected directly;
- `inference` records a conclusion derived from that evidence;
- `open question` records what still requires affected-actor, physical,
  longitudinal, or independent evidence.

Repository evidence can prove that a change and its checks exist. It cannot by
itself prove that a musician, operator, customer, or other affected person finds
the resulting workflow better.

## Case 1: Fructal applied to itself

### Initial method and refinement

**Observed:** The
[first published contract](https://github.com/PaolaShultz/shr-skills/blob/814898424a53767a9e1b49975a748c891da1f614/skills/fructal-cap-design/SKILL.md)
already contained the constraint-and-motion principle, workflow tracing,
recovery beside failure, state preservation, a six-question acceptance test,
and before/after verification.

The public history then records successive refinements:

| Commit | Observed change |
| --- | --- |
| [`19768e3`](https://github.com/PaolaShultz/shr-skills/commit/19768e3e347c859dec97d33f2008647cb1a9bf18) | Refined the initial audit method |
| [`2b5aa37`](https://github.com/PaolaShultz/shr-skills/commit/2b5aa3786446f6dfb7899a5e6f9a55718bbe20ca) | Generalized the method from user-interface workflows to technical, physical, service, and multi-actor systems |
| [`aaa9770`](https://github.com/PaolaShultz/shr-skills/commit/aaa97703422aa4a2ceb5ab7d3f6ff7e27ccc075d) | Tightened evidence classification and reporting |
| [`c70eacc`](https://github.com/PaolaShultz/shr-skills/commit/c70eaccb73470e784c700d8fa5ff39c0a0a9fe45) | Defined Review, Redesign, and Implement execution paths |
| [`d54224b`](https://github.com/PaolaShultz/shr-skills/commit/d54224b9aaa217662ac91d405dbe2ae4549aa6f7) | Hardened mode changes, authorization, persistence, and all-path behavior |
| [`3814c5e`](https://github.com/PaolaShultz/shr-skills/commit/3814c5e2a97ee90479b8591ea1871f71074edc6b) | Restored the six-question design intelligence and deterministic validation |

This history alone shows iterative development. The stronger self-application
case begins when Fructal was explicitly used to review its own contract.

### The self-review

**Observed:** A Fructal Review identified six material weaknesses:

1. validation did not exercise Review, Redesign, Implement, or mixed-mode
   behavior;
2. explicit mode instructions could conflict with outcome-based routing;
3. Review and Redesign could deadlock when real inspection had harmless
   incidental read effects;
4. a supplied artifact and an attributed claim inside it could collapse into one
   evidence label;
5. the installed skill could not identify its exact source package, and source
   validation could not detect installed-copy drift;
6. human-oriented feedback language was ambiguous for teams, services, devices,
   and software components.

The resulting
[contract-evaluation design](https://github.com/PaolaShultz/shr-skills/blob/a03c709fe503d58f016613c777fdaaaa52316bd5/docs/superpowers/specs/2026-07-24-fructal-contract-validation-design.md)
preserved the broad workflow-engineering scope, exclusive modes, Review's
no-solution boundary, Redesign's no-modification boundary, Implement
persistence, consequential-action safeguards, accessibility, and the
Fructal-cap test.

The review therefore did not treat every existing behavior as a defect. It
separated protected capabilities from friction in the method's own execution
motion.

### From findings to executable contract

The self-improvement sequence followed Fructal's own mode boundaries:

1. **Review:** inspect the existing skill, identify evidence, separate
   constraints from friction, and report six findings without changing the
   contract;
2. **Redesign:** specify mode precedence, diagnostic read boundaries,
   two-dimensional evidence handling, actor-appropriate feedback, package
   provenance, deterministic validation, and isolated live evaluation;
3. **Implement:** change the owning skill and package, add contract fixtures,
   add deliberately broken regression packages, and verify both permitted and
   prohibited behavior.

The implementation landed in:

- [Harden Fructal execution contracts](https://github.com/PaolaShultz/shr-skills/commit/c04722092035b27f624b30d7ee5cec9e4be22c56),
  which added the package validator, 11 contract cases, deterministic regression
  tests, package provenance, installed-copy comparison, and the revised skill
  contract;
- [Add Fructal live contract evaluations](https://github.com/PaolaShultz/shr-skills/commit/5c16bb548023bbd198c5b3e30b6cc8cebb3b635e),
  which added isolated Codex execution, structured result validation,
  disposable read-only and workspace-write fixtures, an offline fake runner,
  fixture-state verification, and classified runner, transport, schema,
  contract, and fixture failures.

**Inference:** This demonstrates self-hosting capability. Fructal can inspect
and improve the workflow through which Fructal itself is selected, authorized,
executed, and verified.

### What self-application proves and does not prove

The Git history and passing regressions demonstrate that the review produced
specific, executable improvements rather than favorable prose alone.

**Open question:** Self-evaluation can still be circular. A method may optimize
for its own criteria, and a test suite may encode those same criteria. The case
therefore supports contract integrity and productive self-correction, not
universal correctness or independent validation of the method.

## Case 2: Anonymous software-project review

### Case context

**Observed:** A substantial private software project was already being developed
with [`Superpowers`](https://github.com/obra/superpowers), a structured
software-delivery skill suite covering design, planning, debugging, test-driven
development, verification, review, and branch completion.

A separate read-only Fructal review inspected several connected workflows as
complete constrained motions rather than as a collection of known features or
defects. The review and the later authorized implementation were separate
stages.

The project remains intentionally anonymous. Its name, organization, private
repository, routes, implementation identifiers, and unpublished test evidence
are not linked from this public account.

### What the Fructal review found

**Observed:** The review identified multiple workflow-contract failures that the
existing software-delivery process had not surfaced. The individual components
often worked, but their combined motion could still:

- lose or obscure state between steps;
- confuse displayed context with persisted identity;
- make ownership or responsibility unclear;
- preserve an action while losing the actor's position or intent;
- provide incomplete feedback after filtering, navigation, or delayed work;
- make cancellation, reset, retry, return, or repeated use behave differently
  from the normal path;
- treat accessibility as a local control property instead of part of the whole
  workflow;
- expose implementation boundaries that actors should not have to manage.

These were not all conventional defects. Some were gaps between individually
valid components, some required clarification of the intended product contract,
and some became reproducible behavioral failures.

### Why the existing delivery workflow had not found it

**Inference:** A software-delivery skill suite usually begins with a framed
feature, defect, or implementation goal and asks how to execute that work
reliably. Its strongest mechanisms activate after the problem has been named:
design approval, plans, root-cause debugging, focused tests, implementation
discipline, review, and fresh verification.

Fructal begins earlier and at a different boundary. It asks:

- who initiates, continues, and experiences the result;
- which constraints are necessary and what establishes each one;
- where the system makes an actor manage accidental implementation friction;
- what happens through feedback, cancellation, failure, retry, interruption,
  handoff, delay, return, and repeated use;
- whether context, position, entered work, ownership, and intent survive;
- whether recovery returns every affected actor to motion;
- whether accessibility is part of the normal and recovery paths;
- what must remain untouched.

This broader inspection can reveal unreported workflow friction even when local
tests pass and no single component appears broken.

### Division of responsibility

**Observed:** Fructal supplied the discovery and preservation boundary. It
separated necessary constraints from existing behavior, distinguished observed
defects from product decisions and open questions, and identified the state and
actor contracts that later changes had to preserve.

The subsequent authorized implementation used the software-delivery suite's
strongest mechanisms: reproduce suspected defects, add focused behavioral
coverage, make narrow owning-layer changes, run broader automated tests, inspect
browser-visible behavior, and verify completion from fresh evidence.

The practical sequence was:

> Fructal discovers and bounds the right workflow problem; software-delivery
> skills help implement the resulting change reliably.

### Capability comparison

| Capability | Fructal Cap Design | Structured software-delivery skills |
| --- | --- | --- |
| Finding unreported workflow friction | Primary strength | Secondary |
| Cross-step and cross-actor continuity | Primary strength | Partial |
| Separating necessary constraints from existing behavior | Explicit | Not a central contract |
| Recovery, cancellation, return, and repeated use | Explicit lifecycle | Usually task-dependent |
| Preserving context, work, ownership, and intent | Explicit acceptance condition | Usually requirement-dependent |
| Accessibility in the normal path | Integrated | Depends on the task and tests |
| Root-cause debugging of a known defect | Supporting process | Primary strength |
| Test-driven implementation | Required when appropriate | Primary strength |
| Repository and branch discipline | Defers to the owning environment | Primary strength |
| Verification before completion | Required | Primary strength |

This table compares primary responsibilities, not absolute capability. Either
method can contribute outside its strongest area when the task and environment
provide the necessary evidence.

### Practical result

**Inference:** Fructal and structured software-delivery skills are more
complementary than interchangeable.

Fructal was stronger in this case at problem-space coverage: discovering latent
friction across actors, steps, state boundaries, recovery paths, and necessary
constraints. The delivery suite was stronger at implementation mechanics:
debugging a known failure, test-driven repair, repository discipline, review,
and completion evidence.

The case demonstrates why passing local tests does not prove that a complete
workflow remains coherent. It also demonstrates why a broad workflow review is
not a substitute for disciplined implementation. Both layers were needed.

## Case 3: SHR-DAW on Raspberry Pi

### System and actor scope

[SHR-DAW](https://github.com/PaolaShultz/shr-daw) is an MIT-licensed compact
Raspberry Pi music workstation for a 40×13 terminal, optional MIDI controllers,
software instruments, FT2-style sequencing, WAV loops, effects, JACK routing,
and audio recording.

**Observed:** Its constrained workflows span:

- the musician and system operator;
- keyboard, mouse, and four-, five-, or eight-button MIDI controllers;
- a compact terminal interface with strict geometry and position constraints;
- Rust application and Project state;
- software instruments, JACK clients, MIDI routes, and external processes;
- private Projects, Ideas, presets, loops, recordings, and configuration;
- install, setup, diagnosis, interruption, shutdown, and recovery;
- bounded real-time audio behavior and physical equipment safety.

This makes it a materially different test from a conventional web or desktop
software workflow. The actor's physical position, musical position, live notes,
routes, audio ownership, unfinished work, and external equipment state can all
matter at once.

### The complete musician/operator audit

The public
[workflow audit and repair ledger](https://github.com/PaolaShultz/shr-daw/blob/6c2313609e03ecf9289de452d38abf56cf7ac72b/docs/WORKFLOW_AUDIT_HANDOFF.md)
records the first complete musician/operator workflow audit.

**Observed:** The ledger:

- preserves the original findings after repair instead of rewriting history;
- distinguishes `READY`, `DECISION`, `PHYSICAL`, `VERIFIED`, and `DONE` work;
- separates provided/reported evidence, observed artifacts, inference, and open
  questions;
- registers each necessary privacy, ownership, safety, interoperability,
  portability, accessibility, and data-integrity constraint with its source;
- inventories install, setup, launch, shutdown, navigation, Help, routing,
  instruments, Projects, Files, Patterns, Tracks, loops, effects, recording,
  diagnosis, failure, return, and repeated-use paths;
- ranks findings by consequence, frequency, and recovery cost;
- separates 15 unambiguous repairs from 10 owner decisions and eight
  physical/user evidence gates;
- verifies normal completion, cancellation, failure and retry, repeated use,
  interruption and handoff, accessibility and controller parity, untouched
  state, and separately authorized physical paths.

### What the audit found

The largest initial risks were at workflow boundaries rather than inside
isolated components:

1. unsaved Project edits could be lost through Load or keyboard quit;
2. a Tracks screen described as a draft could mutate the Project and live
   routing before completion;
3. recording or transport could continue on Home without authoritative
   ownership and status;
4. editing one Routing input could collapse several configured performance
   inputs into one;
5. FT2 order navigation could reset the musician's row despite an explicit
   position-preservation rule;
6. install and setup actions were individually careful but did not behave as one
   interruption-safe journey;
7. Loop Library browsing could stop transport before the musician committed a
   selection;
8. controller-visible naming workflows actually required keyboard text entry;
9. effect and transport ownership could be unclear across screens;
10. diagnostics could present optional audio absence as whole-product failure.

Other open findings concerned automatic LAN publication when opening Help,
privileged network binding, controller character entry, Project ownership during
audition, and the difference between status visibility and direct control.
Those decisions were retained instead of being silently chosen to make
implementation convenient.

### Repair sequence

The [audit handoff commit](https://github.com/PaolaShultz/shr-daw/commit/3c65e11a6297e6a922da2a7953bebec3b1cc688b)
created the durable ledger before implementation.

[Repair audited musician workflows](https://github.com/PaolaShultz/shr-daw/commit/6d55069cbc4e803c27416de04ec055acbc2d1aa8)
then changed the owning UI, navigation, setup, installation, and documentation
surfaces. The first repair queue:

- added dirty Project tracking and Save/Discard/Cancel protection;
- made Home report authoritative background transport and recording ownership;
- restored exact nested draft values on cancellation;
- preserved every configured performance input during a Routing edit;
- preserved and clamped FT2 row, page, lane, and column across navigation;
- exposed installer consequences before system changes and reported
  interruption/completion state;
- grouped diagnostic capability status without hiding exact failures;
- made keyboard-required naming honest in the controller-visible workflow;
- delayed transport changes until Loop Library preview or commitment;
- clarified effects ownership and reconciled UI, Help, and documentation;
- removed stale paths only after their replacement behavior was proven.

The source-only pass remained separate from the later authorized build,
connected-system, screenshot, and physical checks.

### Combined acceptance evidence

[Complete workflow audit acceptance](https://github.com/PaolaShultz/shr-daw/commit/ae0298718694a3e8c3dc2954f1545fa07986ecff)
recorded the combined acceptance.

**Observed machine evidence included:**

- locked checks, debug and release builds, and warning-denied Clippy;
- 662 passing tests plus four intentionally ignored private renderers in each
  complete test profile;
- 16 focused workflow and JACK lifecycle tests;
- regeneration and exact drift validation of all 105 real terminal-interface
  screenshots;
- shell, Python, XML, JSON, demo, static, documentation, and diff checks;
- isolated installer and setup trees, interactive and noninteractive setup,
  idempotent rerun, interruption recovery, preflight, and grouped diagnosis;
- 60-second synthetic 18-channel raw capture and three-source final-mix stress
  with full PCM equality and zero drop, overflow, callback, or xrun faults;
- real synchronized 24-bit/48 kHz capture and real three-source final-bus
  recording;
- live source-loss, real-xrun, JACK-loss, low-space, and forced-interruption
  recording drills;
- conservative recovery of an interrupted partial take followed by a clean
  replacement recording;
- discovery and repair of a synth teardown defect during acceptance;
- final connected release checkpoints with no new xruns, missed deadlines,
  oversized callbacks, route drift, or owned-process residue.

Later public changes continued the same constrained-workflow pattern:

- [Repair menu navigation and recovery contracts](https://github.com/PaolaShultz/shr-daw/commit/95d53145be8ef9397543c4afa16ddc5d874c45fe)
  aligned controller profiles, overlays, navigation, caller return, Files,
  Projects, tracker, effect, and Help behavior;
- [Complete menu repair acceptance](https://github.com/PaolaShultz/shr-daw/commit/62a3bc57418cb111d2008ee064965414cb215505)
  reconciled implementation, documentation, and generated interface evidence;
- [Repair Raspberry Pi audio setup and diagnosis](https://github.com/PaolaShultz/shr-daw/commit/8e9a964f18505bf291a4d269969d5e2dc9427af8)
  made performance tuning, configuration ownership, interruption recovery,
  diagnosis, rollback, and untouched administrator state explicit and added a
  dedicated 528-line regression harness;
- [Document Raspberry Pi 5 NVMe installation](https://github.com/PaolaShultz/shr-daw/commit/6c2313609e03ecf9289de452d38abf56cf7ac72b)
  recorded the current clean-machine installation boundary without overstating
  incomplete physical acceptance.

### Affected-actor evidence

**Provided/reported:** The creator, product owner, musician, and Raspberry Pi
operator reports that the repaired flows changed the system from a confusing
state into workflows that now feel notably coherent and effective.

This is affected-actor evidence under Fructal's own evidence contract. It is
qualitative and comes from one deeply involved creator/operator, but it is
stronger than an inference derived from tests or screenshots alone.

**Inference:** The positive experience is plausibly connected to the
preservation-first repairs because the reported improvement corresponds to
observable changes in position, work retention, ownership, feedback,
navigation, cancellation, and recovery—not merely to additional features.

**Open question:** Independent musicians, different controllers, long-term
repeated use, clean-machine installation, and later physical-interface
acceptance may reveal different results. The public SHR-DAW documentation
correctly retains those gates rather than presenting machine evidence as owner
observation.

## Case 4: Moj Sint as a convergent workflow

### Why this case is different

[Moj Sint](https://github.com/PaolaShultz/moj-sint) is an MIT-licensed,
low-level headless Rust synthesizer under active sound research for later use
as a distinct external SHR-DAW instrument.

This is not presented as another direct Fructal application.

**Observed:** A search across the complete 106-commit local repository history
found no reference to `Fructal`. A separate search across the original Codex
session logs for the project's foundation, oscillator research, experimental
policy, and first five-family listening gate found no Fructal or
`fructal-cap-design` invocation. Those sessions explicitly used general
software-delivery workflows including brainstorming, planning, test-driven
development, and verification.

**Observed:** Fructal's
[first public commit](https://github.com/PaolaShultz/shr-skills/commit/814898424a53767a9e1b49975a748c891da1f614)
predates Moj Sint's
[initial design and handoff](https://github.com/PaolaShultz/moj-sint/commit/1d828b57a9a48de8d6e1476bf6bb75168faa9043)
by about fifteen hours. The case therefore does not show that Moj Sint
independently invented the method before Fructal existed. It shows that a
Fructal-like execution pattern emerged in another difficult workflow without a
recorded invocation of the skill.

### The primordial Fructal-like pattern

The
[portable foundation](https://github.com/PaolaShultz/moj-sint/commit/1aa6a6bd9f8074c8391621820684267524365b67)
already separated necessary real-time, ownership, provenance, platform,
human-acceptance, modification, and verification constraints from the mechanics
of individual sound experiments.

The later
[experimental artifact policy](https://github.com/PaolaShultz/moj-sint/commit/6e10c95bb26ae48ba83193d59ba7343bbf1bdcab)
made recovery and continuity unusually explicit:

- generated audio, measurement tables, manifests, and batch-specific reports
  were disposable by default;
- a rejected experiment retained its durable conclusion while its generated
  batch was deleted;
- preserving an exact tone, batch, report, parameter file, or preset required
  explicit authorization;
- parameter variations inside one graph could not be presented as genuinely
  different sound mechanisms;
- reproducible source, tests, and durable evidence could remain even when the
  reviewed output was discarded.

The
[multi-family listening gate](https://github.com/PaolaShultz/moj-sint/commit/882492e5b22f5cb1033ad5b2f8977734e6a6bf53)
then kept five experimental sources outside the production engine, gave each a
distinct perceptual hypothesis and audible failure condition, used automated
measurements only to reject defects and characterize behavior, and reserved
musical acceptance for human listening. The
[recorded verdict](https://github.com/PaolaShultz/moj-sint/commit/da526a940c58a4893a1e3d564d1a1587dcc0c7f9)
retained a cautiously positive direction without selecting, integrating,
ranking, or macro-mapping a source.

### Capability correspondence

| Moj Sint execution behavior | Corresponding Fructal capability |
| --- | --- |
| Real-time, ownership, provenance, hardware-evidence, and listening rules are separated from experimental mechanics | Constraint-source analysis |
| Disposable research sources remain isolated from the production `Engine` | Explicit modification and mode boundaries |
| Automated, x86 workstation, AArch64 compile, native Pi, and human-listening claims remain distinct | Evidence provenance and evidentiary status |
| Listener, engine, host, SHR-DAW, JACK, Raspberry Pi, and audio hardware are treated as affected actors | People, services, devices, and software actor coverage |
| Rejected audio is removed while conclusions and reproducible generators remain | Recovery beside failure |
| Unusual sound premises are preserved rather than normalized into conventional synthesizer categories | Context and intent preservation |
| Engine, presets, stable macros, host integration, and hardware claims are repeatedly recorded as unchanged | Before/after and untouched-state verification |
| Rejected batches constrain later experiments without being mislabeled as success | Failure, delayed outcome, return, and repeated-use tracing |

### Current local evidence

**Observed:** The local repository is currently clean at `bab9a7a`, contains 106
commits, and is 50 commits ahead of its public remote. Its most recent
experimental sequence preserved the first strongly positive `Coupled Wire`
reference, rejected later envelope/motion variants, kept the production engine
and integration boundaries untouched, and produced one controlled-thump
successor awaiting human listening.

Those 50 later commits are not yet public, so this paragraph is direct local
repository evidence rather than independently reproducible public evidence.
The public links above intentionally stop at history already available on the
remote.

**Provided/reported:** The creator reports that this preservation-first
experimental flow turned several previously messy sound-development motions
into useful and coherent ones.

**Inference:** Moj Sint is evidence that the capability cluster formalized by
Fructal can be valuable outside conventional product-interface work. It also
shows that parts of the cluster can emerge from a careful combination of domain
constraints, human acceptance, disciplined implementation, and durable
handoffs.

**Unsupported claim:** Moj Sint was built by invoking Fructal, or proves that
Fructal caused the improvement.

**Open question:** A future explicitly logged Fructal Review, Redesign, or
Implement cycle could compare the existing workflow with a deliberately
Fructal-routed one and provide stronger causal evidence.

## Combined evidence

| Evidence layer | What it demonstrates | Main limitation |
| --- | --- | --- |
| Fructal applied to itself | The method can expose ambiguity in its own execution contract and convert findings into regression-tested improvements | Self-evaluation can be circular |
| Anonymous private software project | It can find cross-component workflow failures that an established delivery discipline did not surface | Private case with limited public reproducibility |
| Public SHR-DAW case | It can operate across people, controllers, software, audio services, devices, ownership, safety, state, and recovery on a real Raspberry Pi system | One primary creator/operator; broader replication remains open |
| Moj Sint convergent workflow | Its capability cluster maps onto a successful preservation-first creative/technical research flow even without a recorded Fructal invocation | Convergence is not causal proof; the newest 50 commits are not yet public |

Together, the cases support a narrower, evidence-backed conclusion:

> Fructal Cap Design has demonstrated value as a discovery and preservation
> layer above disciplined implementation—first on itself, then in a private
> software product, and then across a public Raspberry Pi
> musician/operator system. Moj Sint separately shows the same capability
> cluster emerging in experimental sound research without proving that Fructal
> caused it.

The cases do not show that Fructal replaces debugging, test-driven development,
human-centered research, accessibility standards, safety analysis, or durable
workflow runtimes. They show that Fructal can find and bound the complete
workflow problem those specialist processes then help analyze, implement, or
verify.

## Future production comparison

**Open question:** The anonymous private software case currently has extensive
local behavioral and browser evidence but no published before/after production
comparison.

A future validation pass is reserved to:

1. capture the existing public production workflow before the next deployment;
2. build and deploy the already tested replacement state through the private
   project's normal production process;
3. capture the same public paths, actors, browser states, URLs, submitted
   values, recovery paths, accessibility paths, and untouched state after
   deployment;
4. compare production before/after evidence with the complete local
   cross-browser and server-state evidence;
5. keep all private repository paths, source, credentials, operational details,
   and unpublished data out of this public repository;
6. report differences honestly instead of assuming local and production
   behavior are identical.

This will strengthen the anonymous case only after both production states have
been directly observed. Until then, the current public account makes no
production-effectiveness claim.

## Overall limits

These cases provide:

- direct repository evidence of self-correction;
- direct public source, test, screenshot, machine, audio, and recovery evidence;
- one anonymous private-project implementation;
- one public-project convergence case whose newest local history is not yet
  published;
- qualitative evidence from one affected creator/operator.

They do not yet provide:

- independent evaluation of Fructal by an unrelated team;
- controlled comparison against another method on identical work;
- multiple affected actors across unrelated domains;
- longitudinal outcome measurements;
- a general success rate;
- professional certification for accessibility, safety, legal, clinical, or
  regulated work.

The evidence is therefore substantial enough to support practical use and
continued evaluation, but not a universal superiority claim.
