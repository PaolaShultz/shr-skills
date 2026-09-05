No issues found.

[parser.py](/tmp/fructal-eval-ordinary_constraints_nontrigger-01-65lzgl39/fixture/parser.py:1) correctly:

- Accepts ASCII strings of 64 characters or fewer.
- Rejects strings longer than 64 characters.
- Rejects non-ASCII characters.

Existing tests and additional boundary checks passed. `pytest` was unavailable, so assertions were executed directly with Python. No files were changed.