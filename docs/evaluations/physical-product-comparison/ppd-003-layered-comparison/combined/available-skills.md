# Combined-boundary available-skill diagnostic

## Outcome

The first diagnostic attempt exposed only Fructal Cap Design. Inspection showed
that the exported Superpowers package was present but its Codex discovery link
was absent. No product arm was launched under that invalid boundary.

The corrected diagnostic used the same launch boundary as the product arm and
exposed:

- built-in system skills: `imagegen`, `openai-docs`, `plugin-creator`,
  `skill-creator`, and `skill-installer`;
- non-system user package: Fructal Cap Design as technical skill `fructal`;
- non-system user package: Superpowers with its fourteen constituent skills;
- no other non-system user skills.

The complete diagnostic response is preserved in
[`attempt-02-valid-session.jsonl.gz`](isolation-diagnostic/attempt-02-valid-session.jsonl.gz).
The failed diagnostic is preserved in
[`attempt-01-missing-superpowers-session.jsonl.gz`](isolation-diagnostic/attempt-01-missing-superpowers-session.jsonl.gz).

## Discovery correction

Codex discovered the isolated Superpowers export through:

```text
<isolated HOME>/.agents/skills/superpowers
  -> <isolated HOME>/.codex/superpowers/skills
```

Both ends were inside the disposable combined home. The product prompt and
product workspace were unchanged. The correction happened before launch and
did not add another user-skill package.
