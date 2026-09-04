No correctness issues found.

[parser.py](/tmp/fructal-eval-ordinary_constraints_nontrigger-01-bj1amcay/fixture/parser.py:1) correctly:

- Accepts ASCII strings of 0–64 characters.
- Rejects 65 or more characters.
- Rejects non-ASCII input.
- Preserves accepted input unchanged.

Focused boundary checks passed, including all lengths through 64 and longer inputs. The supplied tests cover the essential 64/65 boundary and non-ASCII rejection.

`pytest` was unavailable in the fixture, so I verified the behavior directly with Python assertions. No files were modified.