# Fully specified small implementation

Work only in this disposable repository. Implement the requested change now.

Change `normalize_title` in `textfmt.py` so that it removes leading and
trailing ASCII spaces and collapses every internal run of ASCII spaces to one
ASCII space. Preserve every other character byte-for-byte. The expected
outcomes are already encoded in `verify.sh`; there is no missing product
decision.

Run `./verify.sh` after the change. Do not commit, create a branch, or modify
any file other than `textfmt.py`.
