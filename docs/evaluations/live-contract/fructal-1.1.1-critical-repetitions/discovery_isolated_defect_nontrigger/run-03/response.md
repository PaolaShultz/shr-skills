`parse_name(null)` throws because [parser.js](/tmp/fructal-eval-discovery_isolated_defect_nontrigger-03-wo7ray27/fixture/parser.js:2) calls:

```js
value.trim()
```

When `value` is `null`, it has no methods or properties, so accessing `trim` raises a `TypeError`. The helper assumes `value` is a string and performs no null check or conversion.