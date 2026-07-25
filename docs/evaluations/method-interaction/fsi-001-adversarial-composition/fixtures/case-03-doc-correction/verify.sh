#!/usr/bin/env bash
set -euo pipefail
test "$(cat guide.md)" = $'# Retry guide\n\nThe worker retries the request once after a transient failure.'
test "$(cat frozen/trace-a.md)" = $'# Historical trace A\n\nThe worker reties the request once after a transient failure.'
test "$(cat frozen/trace-b.txt)" = 'The worker reties the request once after a transient failure.'
printf 'verified\n'
