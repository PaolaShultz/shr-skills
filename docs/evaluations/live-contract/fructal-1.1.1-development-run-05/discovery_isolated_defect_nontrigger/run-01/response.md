`parse_name(null)` throws because the helper directly calls:

```js
value.trim()
```

When `value` is `null`, JavaScript cannot access a `trim` method on it, so it raises a `TypeError`. The function assumes `value` is a string and has no null check or normalization.