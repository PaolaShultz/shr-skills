#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
default_repo_dir="$(cd -- "${script_dir}/.." && pwd)"
selected_repo="${default_repo_dir}"
arguments=("$@")

while (($# > 0)); do
  case "$1" in
    --repo)
      if (($# < 2)); then
        printf '%s\n' "FAIL: --repo requires a path" >&2
        exit 2
      fi
      selected_repo=$2
      shift 2
      ;;
    --installed)
      if (($# < 2)); then
        printf '%s\n' "FAIL: --installed requires a path" >&2
        exit 2
      fi
      shift 2
      ;;
    *)
      printf 'FAIL: unknown argument %s\n' "$1" >&2
      exit 2
      ;;
  esac
done

python3 "${script_dir}/validate-package.py" "${arguments[@]}"
"${script_dir}/check-chatgpt-demo-sync.sh" \
  "${selected_repo}/skills/fructal/SKILL.md" \
  "${selected_repo}/examples/chatgpt-web-demo.md"
