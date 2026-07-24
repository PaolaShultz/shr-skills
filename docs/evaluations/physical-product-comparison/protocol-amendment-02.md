# Protocol amendment 02: host-skill isolation and three-arm extension

Status: **recorded after the affected runs and preserved as an experimental
recovery record**

Date: 2026-07-24

This amendment records a second isolation defect, its recovery, and the
addition of a Superpowers comparison arm. It does not retroactively alter the
frozen `ppd-001` pair or the rubric.

## Sequence

1. A temporary `CODEX_HOME` and temporary workspace were created for a
   supposedly no-user-skill prompt-author run.
2. The run invoked Superpowers.
3. Inspection of the persisted session showed that its actual developer
   payload still listed Superpowers from
   `/home/shome/.codex/superpowers`.
4. `--ignore-user-config` and `--ignore-rules` were tested and did not remove
   those host-discovered skills.
5. Isolating both `HOME` and `CODEX_HOME` was tested. The same diagnostic then
   returned `NONE` for non-system skills.
6. The original result was frozen and relabelled as a Superpowers
   prompt-authoring arm.
7. A new no-user-skill prompt-author run produced the shared execution prompt.
8. That byte-identical prompt was executed concurrently under three verified
   conditions: no user skill, Superpowers only, and Fructal Cap Design only.
9. A separate no-user-skill evaluator received anonymized responses and images
   without the arm mapping and produced the frozen blind scores.

## Evidence

**Observed:** `CODEX_HOME` alone isolated normal Codex config, authentication,
sessions, memories, and `skills/`, but it did not prevent this installation's
host-level Superpowers discovery through the normal `HOME`.

**Observed:** With only `CODEX_HOME` isolated, the diagnostic listed the full
Superpowers skill set even when `--ignore-user-config` and `--ignore-rules`
were present.

**Observed:** With both `HOME` and `CODEX_HOME` isolated, the diagnostic
returned `NONE`.

**Observed:** Separate pre-run diagnostics returned `NONE`, Superpowers only,
and `fructal` only for the three execution workspaces.

**Inference:** A temporary work directory or temporary `CODEX_HOME` alone
cannot establish a clean user-skill boundary in this installation. The actual
developer payload must be checked.

**Inference:** Preserving the first result as a named Superpowers arm retains
useful evidence without misrepresenting it as a clean control.

## What PPD-002 can test

`ppd-002` can ask:

> Given one shared prompt authored by a no-user-skill Codex run, how do the
> same model and tools behave when execution has no user skill, Superpowers
> only, or Fructal Cap Design only?

It cannot cleanly ask:

> Which method independently discovers the most important constraints from the
> creator's rough description?

The execution prompt was expanded to 981 words by a model before any execution
arm saw it. That prompt itself already requires much of the eventual rubric.

## Result boundary

The blind evaluator scored:

- Superpowers only: `39/40`;
- Fructal Cap Design only: `38/40`; and
- no-user-skill control: `38/40`.

The evaluator described the one-point difference as within judgment
uncertainty.

This supports:

- a verified three-arm execution case;
- evidence that all three produced high-coverage concepts from the same strong
  prompt;
- evidence that Fructal Cap Design did not gain a blind-score advantage in
  this run;
- evidence that the treatment failed to express its explicit untouched-state
  verification capability; and
- a reusable isolation check for future skill comparisons.

It does not establish:

- general Superpowers superiority;
- general equivalence between the three conditions;
- real enclosure safety or usability;
- causal attribution from a single stochastic run;
- independent validation; or
- the result of a direct rough-request discovery comparison.

Full evidence is preserved in
[`ppd-002-discovery/`](ppd-002-discovery/).
