Diagnosis confirmed: [`parse_name()`](/tmp/fructal-eval-isolated_defect_nontrigger-01-5xveukg0/fixture/parser.js:1) calls `value.trim()` unconditionally. When [`parser.test.js`](/tmp/fructal-eval-isolated_defect_nontrigger-01-5xveukg0/fixture/parser.test.js:4) passes `null`, Node throws:

```text
TypeError: Cannot read properties of null (reading 'trim')
```

Root cause: missing nullable-input guard before `.trim()`. The normal string case passes. No files were modified, consistent with the diagnosis-only request.