#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repo_dir="$(cd -- "${script_dir}/.." && pwd)"
source_file="${1:-${repo_dir}/skills/fructal/SKILL.md}"
demo_file="${2:-${repo_dir}/examples/chatgpt-web-demo.md}"
embedded_file="$(mktemp)"

trap 'rm -f -- "${embedded_file}"' EXIT

awk '
  !in_skill && /^SKILL$/ { in_skill = 1; next }
  in_skill {
    if (pending_task) {
      if ($0 == "[INSERT YOUR TASK HERE]") {
        pending_task = 0
        exit
      }
      print "TASK"
      pending_task = 0
    }
    if ($0 == "TASK") {
      pending_task = 1
      next
    }
    print
  }
  END {
    if (pending_task) {
      print "TASK"
    }
  }
' "${demo_file}" > "${embedded_file}"

if ! diff -u --label "canonical skill" --label "embedded demo skill" \
  <(sed '/^[[:space:]]*$/d' "${source_file}") \
  <(sed '/^[[:space:]]*$/d' "${embedded_file}"); then
  printf '%s\n' \
    "ChatGPT demo is stale. Update its embedded SKILL from skills/fructal/SKILL.md."
  exit 1
fi

printf '%s\n' "ChatGPT demo skill matches the canonical source."
