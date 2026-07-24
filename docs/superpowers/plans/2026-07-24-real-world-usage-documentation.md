# Real-World Usage Documentation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> superpowers:subagent-driven-development (recommended) or
> superpowers:executing-plans to implement this plan task-by-task. Steps use
> checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish an anonymized account of real-world Fructal Cap Design usage,
including its complementary relationship with structured software-delivery
skills, and link it from the README.

**Architecture:** Keep the evidence account in one focused document under
`docs/`; keep the README entry to one concise sentence and link. Do not change
the canonical skill, embedded demonstration, validators, metadata, or installed
copy.

**Tech Stack:** Markdown, repository shell validators, Git.

---

## File responsibilities

- `docs/real-world-usage-and-testing.md`: anonymous observed case, comparison
  table, practical interpretation, and evidence limits.
- `README.md`: short discoverability entry linking to the full account.

### Task 1: Add the anonymous usage account

**Files:**
- Create: `docs/real-world-usage-and-testing.md`

- [ ] **Step 1: Establish the evidence and anonymity boundary**

Use only these publishable facts:

- a substantial software project already used a structured software-delivery
  skill suite;
- a separate read-only Fructal review inspected several connected workflows;
- the review found latent workflow-contract failures spanning state, identity,
  ownership, context, recovery, feedback, accessibility, and repeated use;
- the review and later authorized implementation were separate stages;
- implementation used reproduction, focused behavioral coverage, narrow
  owning-layer changes, automated tests, and browser checks.

Exclude project, organization, repository, route, domain, filename, location,
commit, and test-count identifiers.

- [ ] **Step 2: Write the document**

Create `docs/real-world-usage-and-testing.md` with these sections:

```markdown
# Real-world usage and testing

## Case context
## What the Fructal review found
## Why the existing delivery workflow had not found it
## Division of responsibility
## Capability comparison
## Practical result
## Limits of the evidence
```

The opening must label the case facts as `observed`, comparative conclusions as
`inference`, and unresolved generalizability as an `open question`.

- [ ] **Step 3: Include the capability table**

Use this exact comparison structure:

```markdown
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
```

Name and link
[`Superpowers`](https://github.com/obra/superpowers) as the concrete
software-delivery suite in the surrounding prose, while keeping the table
applicable to the broader class.

- [ ] **Step 4: Check anonymity and claim discipline**

Run:

```bash
rg -n -i \
  "bee247|city_radius|wizard reset|47e3192|684 tests|12 browser|unified.search|provider.profile" \
  docs/real-world-usage-and-testing.md
```

Expected: no output and exit status 1 because no identifying term is present.

Run:

```bash
rg -n "observed|inference|open question|Superpowers|Capability" \
  docs/real-world-usage-and-testing.md
```

Expected: output showing all evidence labels, the concrete suite source, and the
comparison table.

### Task 2: Link the account from the README

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Add the discoverability section**

Insert this section between `Demonstrate it in ChatGPT Web` and
`Validate and evaluate`:

```markdown
## Real-world usage and testing

Read the [anonymized real-world usage and testing
account](docs/real-world-usage-and-testing.md) to see what Fructal Cap Design
found beside an established software-delivery skill suite and how the two
methods complemented one another.
```

- [ ] **Step 2: Verify the local link**

Run:

```bash
test -f docs/real-world-usage-and-testing.md
rg -n "Real-world usage and testing|docs/real-world-usage-and-testing.md" README.md
```

Expected: both commands pass and `rg` displays the new heading and link target.

### Task 3: Validate and commit the documentation

**Files:**
- Create: `docs/real-world-usage-and-testing.md`
- Modify: `README.md`

- [ ] **Step 1: Run repository validation**

Run:

```bash
scripts/validate.sh
tests/test-validation.sh
tests/test-live-eval-harness.sh
```

Expected: package validation, deterministic validation regressions, and live
evaluation harness regressions all pass.

- [ ] **Step 2: Review formatting and scope**

Run:

```bash
git diff --check
git diff -- README.md docs/real-world-usage-and-testing.md
git status --short
```

Expected: no whitespace errors; the diff contains only the README link and
anonymous account; status lists only those two implementation files in addition
to this already committed plan.

- [ ] **Step 3: Commit**

Run:

```bash
git add README.md docs/real-world-usage-and-testing.md
git commit -m "Document anonymized Fructal usage"
```

Expected: one documentation commit with no skill, demo, validator, metadata, or
installed-copy change.

- [ ] **Step 4: Verify and publish**

Run:

```bash
git status --short
git log -2 --oneline
git push origin main
git status --short --branch
```

Expected: clean status, the plan and documentation commits at the tip of
`main`, and local `main` aligned with `origin/main`.
