# Repository instructions

- For planning, public positioning, evidence, handoffs, or ambiguous context,
  consult the `Fructal Cap Design` index in
  `/home/shome/Documents/knowledge` with `zk`, then verify against this source
  repository and its validators.
- Canonical source/docs change first. After material state, workflow, evidence,
  or decision changes, update the relevant concise knowledge note and run
  `/home/shome/Documents/knowledge/.zk/validate.sh`.
- Agents own knowledge organization and synchronization; the user is not
  expected to edit notes. Never store exact HEAD, clean/ahead status,
  validation counts, or source/installed hashes as current knowledge.
- Use `Fructal Cap Design` as the public name in prose. Reserve lowercase
  `fructal` for the technical skill identifier, directory, metadata, and
  `$fructal` invocation; never shorten the method's public name to one word.
- Treat `skills/fructal/SKILL.md` as the canonical skill source.
- Whenever the skill changes, review and update `README.md` and the embedded
  skill in `examples/chatgpt-web-demo.md`. Update
  `skills/fructal/agents/openai.yaml` when invocation guidance changes.
- Keep the ChatGPT demonstration task natural and short. Do not add response
  formatting, prioritization, evidence-labeling, or other instructions already
  supplied by the skill.
- Run `tests/test-validation.sh`, `tests/test-live-eval-harness.sh`, and
  `scripts/validate.sh` before committing a skill change. Run
  `scripts/evaluate.sh` before publishing a release.
- Repository validation cannot prove an installed copy is current. After a
  source change, deliberately synchronize or reinstall the active copy and
  compare its skill and metadata with the source by running
  `scripts/validate.sh --installed /absolute/path/to/installed/fructal`.
