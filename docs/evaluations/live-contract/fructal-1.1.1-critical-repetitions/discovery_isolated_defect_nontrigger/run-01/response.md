`parse_name(null)` throws because it directly calls:

```js
value.trim()
```

When `value` is `null`, JavaScript cannot access a `trim` method on it, so it raises a `TypeError`. The local cause is the missing null check before `.trim()` in [parser.js](/tmp/fructal-eval-discovery_isolated_defect_nontrigger-01-b1gn0shb/fixture/parser.js:2).