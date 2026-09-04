`parse_name(null)` throws because [parser.js](/tmp/fructal-eval-discovery_isolated_defect_nontrigger-02-mzei5pme/fixture/parser.js:2) calls:

```js
value.trim()
```

When `value` is `null`, JavaScript cannot access the `trim` property on it, so it raises a `TypeError`. `trim()` exists on strings, not on `null`.