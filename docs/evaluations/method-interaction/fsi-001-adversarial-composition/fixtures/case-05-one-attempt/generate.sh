#!/usr/bin/env bash
set -euo pipefail
count=0
if [[ -f generation-count.txt ]]; then
  count=$(<generation-count.txt)
fi
count=$((count + 1))
printf '%s\n' "${count}" > generation-count.txt
if ((count > 1)); then
  printf 'generator budget exceeded\n' >&2
  exit 23
fi
printf '%s\n' \
  'ARTIFACT: deterministic-demo' \
  'STATUS: amber' > artifact.txt
printf 'generated\n'
