# Fructal Cap Design 1.1.1 distribution report

Access date for every source below: **2026-09-04**.

This report distinguishes preparation, validation, submission, publication,
external review, and external acceptance. Private application IDs, review URLs,
account details, and attestations are intentionally excluded.

## First-party documentation ledger

| Channel | Current first-party documentation |
| --- | --- |
| OpenAI Plugins Directory | <https://developers.openai.com/plugins/deploy/submission>, <https://developers.openai.com/plugins/build/plugins>, <https://developers.openai.com/plugins/guides/optimize-metadata>, <https://developers.openai.com/plugins/app-guidelines> |
| OpenAI Developer Showcase | <https://developers.openai.com/community>, <https://developers.openai.com/showcase> |
| Anthropic plugin directory | <https://claude.com/docs/plugins/submit>, <https://code.claude.com/docs/en/plugins>, <https://code.claude.com/docs/en/plugin-marketplaces>, <https://code.claude.com/docs/en/plugins-reference> |
| GitHub agent skills | <https://cli.github.com/manual/gh_skill_publish>, <https://cli.github.com/manual/gh_skill_install>, <https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills> |
| GitHub Pages | <https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site>, <https://docs.github.com/en/rest/pages/pages> |
| Agent Skills | <https://agentskills.io/home>, <https://agentskills.io/specification> |
| skills.sh | <https://skills.sh/docs>, <https://skills.sh/docs/faq>, <https://skills.sh/docs/cli>, <https://skills.sh/docs/api> |
| Cursor | <https://cursor.com/docs/skills> |
| OpenAI Developer Forum | <https://community.openai.com/guidelines>, <https://community.openai.com/categories> |
| Show HN | <https://news.ycombinator.com/showhn.html> |
| VoltAgent Awesome Agent Skills | <https://github.com/VoltAgent/awesome-agent-skills/blob/main/CONTRIBUTING.md> |

## Channel ledger

| Channel | Status | Public location or next official surface | Observed basis |
| --- | --- | --- | --- |
| Canonical repository | Published | <https://github.com/PaolaShultz/shr-skills> | Corrected distribution source is on `main`; local and remote `main` were observed at the same commit. |
| Public landing page | Published | <https://paolashultz.github.io/shr-skills/> | GitHub Pages publishes `main:/docs`; landing, privacy, and terms pages returned HTTP 200 and rendered with the correct public name. |
| OpenAI Plugins Directory | Blocked by user-only action | <https://platform.openai.com/plugins> | The skills-only bundle, listing fields, prompts, tests, URLs, and release notes are prepared and locally validated. The portal requires an authenticated organization role, verified publisher identity, region declarations, and attestations that repository evidence cannot establish. No submission was made. |
| Anthropic plugin directory | Blocked by user-only action | <https://platform.claude.com/plugins/submit> | The public plugin and marketplace validate and install cleanly. Submission requires an authenticated Console Developer, Admin, or Owner account; no submission was made. |
| GitHub agent skill | Published | <https://github.com/PaolaShultz/shr-skills/releases/tag/v1.1.1> | GitHub CLI 2.100.0 passed `gh skill publish --dry-run` and published `v1.1.1`. The corrected plugin ZIP is attached to the release. |
| skills.sh | Validated | <https://skills.sh/PaolaShultz/shr-skills/fructal> | A telemetry-disabled clean install succeeded. Current documentation provides no manual submission; the prospective page is still a soft 404, so no listing is claimed and no install was fabricated. |
| Cursor | Validated | <https://github.com/PaolaShultz/shr-skills> | Current docs support GitHub Remote Rule import. No general public marketplace submission is documented; the team marketplace is not a public directory. |
| OpenAI Developer Showcase | Not applicable | <https://developers.openai.com/showcase> | The current official Community link resolves to the Showcase index, which exposes no public submission form or documented submission flow. Nothing was submitted. |
| OpenAI Developer Forum | Blocked by user-only action | <https://community.openai.com/c/community/21> | The Community category is the documented fit and indexed duplicate searches found no equivalent post. Authenticated browser control was unavailable, so no announcement was posted. |
| Show HN | Deliberately deferred | <https://news.ycombinator.com/showhn.html> | The project is directly installable, but the official submission page was logged out and the required personal authorship/availability facts cannot be inferred. Indexed duplicate searches found no equivalent submission. No post was made. |
| VoltAgent list | Deliberately deferred | <https://github.com/VoltAgent/awesome-agent-skills> | Contribution rules require observable real community usage; no such external adoption evidence is asserted. |

## Evidence and claim boundary

The retained evidence includes a complete 24-case release matrix and 21
critical repetitions, with failed development runs preserved. Natural
execution and semantic judgment are separate and reproducible. The evaluator
was another isolated run of the same model family; there is no independent
validation, scientific proof, production acceptance, or affected-user
acceptance claim.

## Packaging and verification observations

- The canonical `skills/fructal/SKILL.md`, the plugin mirror, and the active
  installed copy were compared; the source and plugin mirror are byte-identical
  and installed-copy validation passed.
- Repository validation, validation regression tests, the live-evaluation
  harness tests, distribution tests, the current Claude plugin validators, the
  GitHub skill dry run, clean GitHub/Claude/skills.sh installs, link checks,
  landing-page browser rendering, knowledge validation, and `git diff --check`
  passed.
- `scripts/evaluate.sh` was not rerun because distribution packaging did not
  change the behavioral contract. The existing version 1.1.1 evaluation
  archives were retained and reused as directed.
- The telemetry-disabled skills.sh install succeeded under Node 22.13.0 while
  reporting that the current CLI declares Node 22.20.0 or later; this is a
  compatibility warning, not a failed install.
- The published `v1.1.1` Git tag identifies the original GitHub skill
  publication commit. Its canonical `skills/fructal` content is correct, so
  GitHub skill installation is correct. A generated plugin wrapper in that
  tag's automatic source archives has the earlier naming error; the tag was not
  moved because publication rules prohibit history rewriting. Plugin consumers
  should use the corrected release asset
  `fructal-1.1.1.zip` or current `main`.
- Evidence-led OpenAI Forum and Show HN drafts are preserved in
  `distribution/announcement-drafts.md`; they are preparation artifacts, not
  claims that either post was made.

## Submission and announcement outcome

The only completed directory-style publication command was GitHub skill
publication. No OpenAI or Anthropic directory form was submitted, and no
OpenAI Forum or Show HN announcement was posted. No private application IDs,
review URLs, account data, or unverifiable attestations were created or stored.
