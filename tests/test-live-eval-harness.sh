#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
evaluator="${repo_dir}/scripts/evaluate.sh"
fake_codex="${repo_dir}/tests/fixtures/fake-codex.py"
temporary_root="$(mktemp -d)"
failures=0

trap 'rm -rf -- "${temporary_root}"' EXIT

record_failure() {
  printf 'FAIL: %s\n' "$1" >&2
  failures=$((failures + 1))
}

expect_success() {
  local name=$1
  shift
  local output
  if ! output="$("$@" 2>&1)"; then
    record_failure "${name} returned nonzero: ${output}"
  else
    printf 'PASS: %s\n' "${name}"
  fi
}

expect_failure_class() {
  local name=$1
  local failure_class=$2
  shift 2
  local output
  if output="$("$@" 2>&1)"; then
    record_failure "${name} unexpectedly passed"
  elif [[ "${output}" != *"FAIL[${failure_class}]"* ]]; then
    record_failure "${name} returned the wrong class: ${output}"
  else
    printf 'PASS: %s\n' "${name}"
  fi
}

list_output="$("${evaluator}" --list 2>&1)" || {
  record_failure "--list returned nonzero: ${list_output}"
  list_output=""
}
for case_id in implicit_review implicit_redesign implicit_implement \
  explicit_review_caps_fix; do
  if [[ "${list_output}" != *"${case_id}"* ]]; then
    record_failure "--list omitted ${case_id}"
  fi
done

mkdir -p "${temporary_root}/tmp"
expect_success "full fake live matrix" \
  env TMPDIR="${temporary_root}/tmp" \
  "${evaluator}" --codex-bin "${fake_codex}"
if find "${temporary_root}/tmp" -mindepth 1 -maxdepth 1 -type d |
  grep -q .; then
  record_failure "successful run retained temporary evaluation state"
else
  printf '%s\n' "PASS: successful run cleaned temporary state"
fi

expect_failure_class "wrong selected mode" "contract" \
  env FAKE_CODEX_MODE=wrong_mode \
  "${evaluator}" --codex-bin "${fake_codex}" \
  --case explicit_review_caps_fix

expect_failure_class "invalid model JSON" "schema" \
  env FAKE_CODEX_MODE=invalid_json \
  "${evaluator}" --codex-bin "${fake_codex}" --case implicit_review

expect_failure_class "Codex process failure" "transport" \
  env FAKE_CODEX_MODE=transport \
  "${evaluator}" --codex-bin "${fake_codex}" --case implicit_review

expect_failure_class "missing Implement fixture change" "fixture" \
  env FAKE_CODEX_MODE=missing_fixture \
  "${evaluator}" --codex-bin "${fake_codex}" --case implicit_implement

expect_failure_class "missing Codex runner" "runner" \
  "${evaluator}" --codex-bin "${temporary_root}/does-not-exist" \
  --case implicit_review

if ((failures > 0)); then
  exit 1
fi

printf '%s\n' "PASS: live evaluation harness regressions"
