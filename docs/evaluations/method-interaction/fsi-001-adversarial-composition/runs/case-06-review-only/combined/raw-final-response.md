`./reproduce.sh` consistently exits `1` with:

```text
expected=2 actual=3 fields=['alpha', '"beta', 'gamma"']
```

Evidence: [reproduce.sh](/tmp/fsi-001-case-06-review-only-combined-xts7ob92/workspace/reproduce.sh:6) supplies `alpha,"beta,gamma"\n` and expects two fields.

Cause: [csv_reader.py](/tmp/fsi-001-case-06-review-only-combined-xts7ob92/workspace/csv_reader.py:2) uses plain `str.split(",")`, which treats every comma as a delimiter and has no CSV quote awareness. It therefore splits the comma inside `"beta,gamma"`, producing three fields while retaining the quote characters.