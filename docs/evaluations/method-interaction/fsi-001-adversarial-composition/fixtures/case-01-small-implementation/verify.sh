#!/usr/bin/env bash
set -euo pipefail
python3 - <<'PY'
from textfmt import normalize_title

assert normalize_title("  alpha   beta  ") == "alpha beta"
assert normalize_title("gamma") == "gamma"
assert normalize_title("a\t  b") == "a\t b"
assert normalize_title("  café  noir  ") == "café noir"
print("verified")
PY
