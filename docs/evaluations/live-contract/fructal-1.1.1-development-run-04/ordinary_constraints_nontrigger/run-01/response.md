No defects found.

[parser.py](/tmp/fructal-eval-ordinary_constraints_nontrigger-01-nf5vuxgo/fixture/parser.py:1) correctly:

- Rejects non-ASCII input.
- Accepts exactly 64 ASCII characters.
- Returns an error for 65 or more characters.

Focused checks for 64 characters, 65 characters, and non-ASCII input all passed. The existing tests cover the essential boundary. `pytest` itself was unavailable, so I verified the same cases directly with Python. No files were modified.