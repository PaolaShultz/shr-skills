The defect is in [parser.js](/tmp/fructal-eval-isolated_defect_nontrigger-01-zmjc9rcs/fixture/parser.js:2).

`parse_name(null)` reaches `value.trim()`, but `null` has no `trim` method, producing:

```text
TypeError: Cannot read properties of null (reading 'trim')
```

Reproduced by running `node parser.test.js`; it exits with status 1. The normal string case passes. The function needs an explicit nullable-input guard, with the intended fallback or rejection behavior defined by its contract.

No files were changed.