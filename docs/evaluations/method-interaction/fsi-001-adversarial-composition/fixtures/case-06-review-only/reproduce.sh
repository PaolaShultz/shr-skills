#!/usr/bin/env bash
set -euo pipefail
python3 - <<'PY'
from csv_reader import split_fields

actual = split_fields('alpha,"beta,gamma"\n')
print(f"expected=2 actual={len(actual)} fields={actual}")
raise SystemExit(0 if actual == ["alpha", "beta,gamma"] else 1)
PY
