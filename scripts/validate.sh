#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repo_dir="$(cd -- "${script_dir}/.." && pwd)"
skill_file="${repo_dir}/skills/fructal/SKILL.md"
metadata_file="${repo_dir}/skills/fructal/agents/openai.yaml"
readme_file="${repo_dir}/README.md"
demo_file="${repo_dir}/examples/chatgpt-web-demo.md"
failures=0

fail() {
  printf 'FAIL: %s\n' "$1" >&2
  failures=$((failures + 1))
}

require_file() {
  [[ -f "$1" ]] || fail "missing ${1#${repo_dir}/}"
}

require_text() {
  local file=$1
  local pattern=$2
  local message=$3
  rg -q -- "$pattern" "$file" || fail "$message"
}

for required_file in \
  "${skill_file}" \
  "${metadata_file}" \
  "${readme_file}" \
  "${demo_file}"; do
  require_file "${required_file}"
done

if [[ -d "${repo_dir}/skills/fructal-cap-design" ]]; then
  fail "legacy skills/fructal-cap-design directory remains"
fi

require_text "${skill_file}" '^name: fructal$' \
  "skill name is not fructal"
require_text "${skill_file}" '^description: Use when ' \
  "skill description does not start with Use when"
require_text "${skill_file}" '^## Select and hold one mode$' \
  "mode selection contract is missing"
require_text "${skill_file}" '^### Review$' \
  "Review execution path is missing"
require_text "${skill_file}" '^### Redesign$' \
  "Redesign execution path is missing"
require_text "${skill_file}" '^### Implement$' \
  "Implement execution path is missing"
require_text "${skill_file}" '`provided`' \
  "provided evidence label is missing"
require_text "${skill_file}" '`reported`' \
  "reported evidence label is missing"
require_text "${skill_file}" '^## Run the Fructal-cap test in Redesign and Implement$' \
  "Fructal-cap acceptance loop is missing"
require_text "${skill_file}" 'assistive technology' \
  "concrete accessibility verification is missing"
require_text "${skill_file}" 'before-and-after behavior' \
  "before-and-after behavior contract is missing"
require_text "${metadata_file}" '\$fructal' \
  "agent metadata does not invoke \$fructal"
require_text "${readme_file}" 'skills/fructal' \
  "README does not use the current install path"
require_text "${readme_file}" '^Review:$' \
  "README does not expose Review"
require_text "${readme_file}" '^Redesign:$' \
  "README does not expose Redesign"
require_text "${readme_file}" '^Implement:$' \
  "README does not expose Implement"
require_text "${demo_file}" '^\[INSERT YOUR TASK HERE\]$' \
  "ChatGPT demo task slot is missing"

if ! "${script_dir}/check-chatgpt-demo-sync.sh"; then
  failures=$((failures + 1))
fi

if ((failures > 0)); then
  exit 1
fi

skill_words="$(wc -w < "${skill_file}")"
printf 'PASS: Fructal package invariants are valid (%s skill words).\n' \
  "${skill_words}"
