# Fructal Cap Design 1.1 proportionality revision

Status: implemented and evaluated locally on 2026-09-02. Publication is outside
this record.

## Objective and evidence

This revision preserves Fructal Cap Design's preservation-first execution
contract while reducing over-activation and ceremony for small work.

The input feedback is `provided`: an unfamiliar evaluator found the principle,
modes, evidence discipline, recovery, accessibility, ownership, and safety
strong, while questioning trigger breadth, repeated wording, mandatory visible
mode labels, Review's prohibition on all recommendations, evidence-label
ceremony, and exhaustive verification.

Directly inspected `observed` evidence included:

- the complete 1.0.1 `SKILL.md`, package metadata, agent interface, README, and
  embedded ChatGPT demonstration;
- all current contract cases, output schema, package validator, live evaluator,
  fake runner, and regression scripts;
- the contract/evaluation design, real-world evidence account, workflow
  postmortem, FSI-001 results and retrospective, and PPD-003 results and result
  boundary;
- the skill's Git evolution from generalization through mode, all-path,
  six-question, evidence, feedback, naming, and package hardening.

The evidence shows behavioral value for strict mode ceilings, exact
consequential intent, provenance/status separation, recovery and continuity,
actor-appropriate feedback, accessibility, and untouched-state verification.
FSI-001 also shows overlap and measurable cost when evidence and verification
obligations are repeated. It does not prove that the 1.0.1 trigger actually
over-activates in production; narrowing the trigger is an `inference` supported
by its breadth, the evaluator feedback, and the method's stronger evidence as a
specialized consequential-workflow tool.

## Preserved behavioral contract

Universal invariants:

- preserve supported constraints rather than deleting them;
- select and hold one Review, Redesign, or Implement authorization boundary;
- prevent unauthorized modification and unstated consequential external action;
- distinguish supplied material, attributed claims, observation, inference,
  and material unknowns;
- preserve safety, privacy, accessibility, ownership, compliance,
  interoperability, and data integrity;
- never present a proposal or untested implementation as validated;
- continue safe in-scope work without non-blocking questions.

Conditional rigor expands with consequence, complexity, uncertainty,
irreversibility, and affected actors. Actor mapping, lifecycle tracing,
explicit evidence labels, cap-test discussion, and broad verification are
required only where they can affect the outcome or confidence. Recovery,
interruption, handoff, context, source-of-truth continuity, accessibility, and
untouched state remain mandatory whenever the changed contract materially
touches them.

## Intentional changes

| Concern | 1.0.1 | 1.1.0 |
| --- | --- | --- |
| Activation | Broad domain list plus constrained-workflow symptoms | Material obstruction of completion, recovery, handoff, or continuity; ordinary requirements, aesthetics, and isolated defects are explicit non-triggers |
| Proportionality | Report scaled, but analysis and verification lists remained prominent | Depth and checks scale explicitly; irrelevant actors, labels, paths, and tests are prohibited |
| Mode visibility | Always state the selected mode | Always hold it internally; name it only when the task explicitly names a mode |
| Review | Findings only; no localized remediation | Requested finding-level recommendations are allowed; end-to-end replacement and modification remain prohibited |
| Evidence vocabulary | Every material category was framed as a label | All distinctions remain; explicit labels are used only when status matters to a claim, risk, or decision |
| Verification | One exhaustive-looking path list in the reporting contract | One consolidated risk-selected list covering only materially affected paths |
| Host/process overlap | Generic execution duties appeared as independent obligations | Planning, debugging, delivery, and verification methods operate inside the selected mode and cannot expand authority |
| Naming | Display name was coherent but the skill text did not explain the identifier | Public name, technical identifier, invocation, display name, and prompt are explicitly aligned |

The package version advances from 1.0.1 to 1.1.0 because Review output,
activation, and mode-display behavior intentionally change while the core
authorization contract remains compatible.

## Evaluation design

The live matrix grew from 11 to 20 cases. It covers:

| Required scenario | Case |
| --- | --- |
| Review without modification authority | `implicit_review`, `explicit_review_caps_fix` |
| Redesign without implementation | `implicit_redesign`, `explicit_redesign_caps_fix` |
| Explicit implementation | `implicit_implement` |
| Ambiguous modification authority | `ambiguous_modification_authority` |
| Destructive or consequential action | `consequential_confirmation` |
| Small routine workflow issue | `small_routine_redesign` |
| Complex multi-actor/source-of-truth workflow | `complex_multi_actor_continuity` |
| Failure/retry with retained context | `failure_retry_preserves_work` |
| Accessibility in the normal path | `accessibility_normal_path` |
| Isolated defect non-trigger | `isolated_defect_nontrigger` |
| Pure aesthetic non-trigger | `aesthetic_critique_nontrigger` |
| Ordinary engineering constraint non-trigger | `ordinary_constraints_nontrigger` |

The schema now records applicability, focused versus thorough scale, localized
Review recommendations, and material workflow concerns as well as the existing
mode, modification, replacement, confirmation, inspection, evidence, and stop
fields. Historical skill text can be tested with `--skill-git-ref` against the
same current cases.

An attempted structured mode-announcement field was deliberately removed. The
same schema necessarily exposes `selected_mode`, and the evaluated model kept
treating that forced JSON field as a visible mode announcement even when the
skill prohibited a prose heading. That measurement could not distinguish
contract behavior from evaluator instrumentation. Conditional mode visibility
is instead protected by deterministic package validation; an unstructured live
output regression remains useful future work.

## Evaluation results

The final 1.1.0 matrix passed all 20 cases with Codex CLI 0.152.1 and
`gpt-5.6-sol`. Focused reruns also passed all four activation controls and all
three authorization-boundary controls used while refining the contract.

Historical 1.0.1 and revised prompts were also exercised against the expanded
matrix during development. Those paired runs exposed variable old-prompt
behavior around isolated-defect activation and Review recommendations, but a
provisional exact scale assertion for the accessibility case rejected both
prompts even though both addressed accessibility and recovery. The assertion
was removed because focused versus thorough was not an outcome requirement for
that modest case. The paired runs therefore informed the contract and fixture
design; they are not reported as a causal score showing that wording alone made
1.1.0 superior.

As a secondary size metric, the canonical skill changed from 235 lines, 1,795
words, and 12,693 bytes to 237 lines, 1,736 words, and 12,616 bytes. The two
additional lines are not treated as a regression: the revision removes 59
words while adding an explicit activation gate and retaining behaviorally
valuable safeguards.

## Deliberately rejected conclusions

- Line count is not the objective. Unique design rules and proven safeguards
  remain even where host behavior overlaps.
- Review does not become Redesign. It may offer bounded, requested advice but
  cannot prescribe a coherent replacement motion.
- Consequential-intent and no-modification rules remain in the portable skill.
  FSI-001 supports their ownership value even when a host also has safeguards.
- The six-question test remains intact. Only performative printing and
  irrelevant application are removed.
- The established Fructal Cap Design identity remains. The revision resolves
  identifier/display ambiguity in prose rather than renaming the method.

## Remaining limits

Live model results are one run per case on one CLI/model combination and do not
prove future-model behavior. Deterministic checks protect text and fixture
contracts, not real-world acceptance. The added cases are compact synthetic
workflows; affected-actor, production, physical, legal, safety, and professional
accessibility evidence remain separate gates.
