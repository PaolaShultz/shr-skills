# Repository instructions

- Treat `skills/fructal/SKILL.md` as the canonical skill source.
- Whenever the skill changes, review and update `README.md` and the embedded
  skill in `examples/chatgpt-web-demo.md`. Update
  `skills/fructal/agents/openai.yaml` when invocation guidance changes.
- Keep the ChatGPT demonstration task natural and short. Do not add response
  formatting, prioritization, evidence-labeling, or other instructions already
  supplied by the skill.
- Run `scripts/validate.sh` before committing a skill change.
- Repository validation cannot prove an installed copy is current. After a
  source change, deliberately synchronize or reinstall the active copy and
  compare its skill and metadata with the source.
