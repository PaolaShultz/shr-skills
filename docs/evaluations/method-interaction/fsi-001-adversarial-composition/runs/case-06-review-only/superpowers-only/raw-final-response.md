### Evidence

- `./reproduce.sh` exits with status `1`:
  `expected=2 actual=3 fields=['alpha', '"beta', 'gamma"']`
- [csv_reader.py](/tmp/fsi-001-case-06-review-only-superpowers-only-tl16xlk6/workspace/csv_reader.py:2) strips the newline and calls Python’s plain `str.split(",")`.

### Cause

`str.split(",")` is not quote-aware. It treats the comma inside `"beta,gamma"` as a delimiter and leaves the quote characters intact, producing three fields instead of two.