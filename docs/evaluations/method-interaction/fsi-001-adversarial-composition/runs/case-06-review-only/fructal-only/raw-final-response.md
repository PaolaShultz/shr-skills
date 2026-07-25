Review mode; no files or state were modified.

- **Observed reproduction:** `PYTHONDONTWRITEBYTECODE=1 ./reproduce.sh` exited `1`, producing:
  `expected=2 actual=3 fields=['alpha', '"beta', 'gamma"']`
- **Source evidence:** [csv_reader.py:2](/tmp/fsi-001-case-06-review-only-fructal-only-17d20opq/workspace/csv_reader.py:2) removes the newline and calls Python’s plain `str.split(",")`.
- **Cause:** `str.split(",")` treats every comma as a delimiter without recognizing CSV quoting. Consequently, the comma inside `"beta,gamma"` is split and the quote characters remain in the output.