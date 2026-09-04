The isolated defect is in [parser.js](/tmp/fructal-eval-isolated_defect_nontrigger-01-0cbsv_mn/fixture/parser.js:2):

```js
return value.trim();
```

[parser.test.js](/tmp/fructal-eval-isolated_defect_nontrigger-01-0cbsv_mn/fixture/parser.test.js:4) passes `null`, so property access occurs before `trim()` can run. Node confirms:

```text
TypeError: Cannot read properties of null (reading 'trim')
```

Root cause: `parse_name` assumes `value` is a string but lacks the required null guard. The intended null behavior—such as returning an empty string, preserving `null`, or rejecting it with a deliberate error—is unspecified. No files were changed. Fructal Cap Design was not activated because the evidence shows an isolated defect, not workflow-level friction.