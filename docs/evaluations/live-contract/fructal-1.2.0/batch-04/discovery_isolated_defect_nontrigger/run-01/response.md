`parse_name(null)` throws because the helper directly calls:

```js
value.trim()
```

When `value` is `null`, JavaScript cannot access a `trim` method on it, so it raises a `TypeError`. The helper has no null check or input normalization before calling `trim()`.