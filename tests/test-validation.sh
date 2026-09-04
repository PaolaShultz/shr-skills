#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
validator="${repo_dir}/scripts/validate.sh"
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

expect_failure() {
  local name=$1
  local expected=$2
  shift 2
  local output
  if output="$("$@" 2>&1)"; then
    record_failure "${name} unexpectedly passed"
  elif [[ "${output}" != *"${expected}"* ]]; then
    record_failure "${name} returned the wrong diagnostic: ${output}"
  else
    printf 'PASS: %s\n' "${name}"
  fi
}

copy_repo() {
  local name=$1
  local destination="${temporary_root}/${name}"
  mkdir -p "${destination}"
  cp -a "${repo_dir}/." "${destination}/"
  rm -rf -- "${destination}/.git"
  printf '%s\n' "${destination}"
}

replace_text() {
  local file=$1
  local needle=$2
  local replacement=$3
  python3 - "${file}" "${needle}" "${replacement}" <<'PY'
from pathlib import Path
import sys

path = Path(sys.argv[1])
needle = sys.argv[2]
replacement = sys.argv[3]
text = path.read_text()
if needle not in text:
    raise SystemExit(f"missing mutation needle in {path}: {needle}")
path.write_text(text.replace(needle, replacement, 1))
PY
}

delete_line_containing() {
  local file=$1
  local needle=$2
  python3 - "${file}" "${needle}" <<'PY'
from pathlib import Path
import sys

path = Path(sys.argv[1])
needle = sys.argv[2]
lines = path.read_text().splitlines(keepends=True)
if not any(needle in line for line in lines):
    raise SystemExit(f"missing deletion needle in {path}: {needle}")
path.write_text("".join(line for line in lines if needle not in line))
PY
}

delete_json_key() {
  local file=$1
  local item_index=$2
  local key=$3
  python3 - "${file}" "${item_index}" "${key}" <<'PY'
from pathlib import Path
import json
import sys

path = Path(sys.argv[1])
item_index = int(sys.argv[2])
key = sys.argv[3]
data = json.loads(path.read_text())
if key not in data[item_index]:
    raise SystemExit(f"missing JSON key in {path}: {key}")
del data[item_index][key]
path.write_text(json.dumps(data, indent=2) + "\n")
PY
}

delete_schema_required_field() {
  local file=$1
  local field=$2
  python3 - "${file}" "${field}" <<'PY'
from pathlib import Path
import json
import sys

path = Path(sys.argv[1])
field = sys.argv[2]
data = json.loads(path.read_text())
data["required"].remove(field)
path.write_text(json.dumps(data, indent=2) + "\n")
PY
}

add_unsupported_unique_items() {
  local file=$1
  python3 - "${file}" <<'PY'
from pathlib import Path
import json
import sys

path = Path(sys.argv[1])
data = json.loads(path.read_text())
data["properties"]["evidence_labels"]["uniqueItems"] = True
path.write_text(json.dumps(data, indent=2) + "\n")
PY
}

mutate_or_record() {
  local name=$1
  shift
  if ! "$@"; then
    record_failure "${name} could not prepare its malformed fixture"
    return 1
  fi
}

expect_success "canonical package" "${validator}" --repo "${repo_dir}"

case_dir="$(copy_repo shortened-public-name)"
replace_text "${case_dir}/README.md" \
  "Fructal Cap Design is an open engineering method" \
  "Fructal is an open engineering method"
expect_failure "shortened public name" \
  "public prose shortens the Fructal Cap Design name: README.md" \
  "${validator}" --repo "${case_dir}"

case_dir="$(copy_repo malformed-skill-yaml)"
replace_text "${case_dir}/skills/fructal/SKILL.md" \
  "name: fructal" "name: [fructal"
expect_failure "malformed SKILL.md YAML" \
  "invalid SKILL.md frontmatter YAML" \
  "${validator}" --repo "${case_dir}"

case_dir="$(copy_repo malformed-agent-yaml)"
replace_text "${case_dir}/skills/fructal/agents/openai.yaml" \
  "interface:" "interface: ["
expect_failure "malformed openai.yaml" \
  "invalid agents/openai.yaml YAML" \
  "${validator}" --repo "${case_dir}"

case_dir="$(copy_repo missing-version)"
if mutate_or_record "missing version" delete_line_containing \
  "${case_dir}/skills/fructal/SKILL.md" 'version: "1.1.1"'; then
  expect_failure "missing package version" \
    "metadata.version must be 1.1.1" \
    "${validator}" --repo "${case_dir}"
fi

case_dir="$(copy_repo broad-activation)"
if mutate_or_record "narrow activation" delete_line_containing \
  "${case_dir}/skills/fructal/SKILL.md" \
  "constraint alone does not qualify"; then
  expect_failure "missing narrow activation" \
    "narrow activation contract is missing" \
    "${validator}" --repo "${case_dir}"
fi

case_dir="$(copy_repo invocation-bypasses-activation)"
replace_text "${case_dir}/skills/fructal/SKILL.md" \
  'Explicit `$fructal` invocation does not override this gate' \
  'Explicit `$fructal` invocation always overrides this gate'
expect_failure "explicit invocation bypasses activation" \
  "explicit invocation bypasses activation gate" \
  "${validator}" --repo "${case_dir}"

case_dir="$(copy_repo missing-proportionality)"
replace_text "${case_dir}/skills/fructal/SKILL.md" \
  "## Apply proportionally" "## Apply uniformly"
expect_failure "missing proportional application" \
  "proportional application contract is missing" \
  "${validator}" --repo "${case_dir}"

case_dir="$(copy_repo missing-review-recommendations)"
replace_text "${case_dir}/skills/fructal/SKILL.md" \
  "Bounded recommendations tied directly to findings are allowed" \
  "Recommendations are forbidden"
expect_failure "missing bounded Review recommendations" \
  "bounded Review recommendation contract is missing" \
  "${validator}" --repo "${case_dir}"

case_dir="$(copy_repo missing-review-recommendation-limit)"
replace_text "${case_dir}/skills/fructal/SKILL.md" \
  "recommendations collectively define that motion" \
  "recommendations remain local regardless of their combined effect"
expect_failure "missing bounded Review recommendation limit" \
  "bounded Review recommendation limit is missing" \
  "${validator}" --repo "${case_dir}"

case_dir="$(copy_repo missing-set-level-review-check)"
replace_text "${case_dir}/skills/fructal/SKILL.md" \
  "Judge the recommendation set as a whole" \
  "Judge every recommendation independently"
expect_failure "missing set-level Review recommendation check" \
  "set-level Review recommendation check is missing" \
  "${validator}" --repo "${case_dir}"

case_dir="$(copy_repo missing-conditional-mode-output)"
replace_text "${case_dir}/skills/fructal/SKILL.md" \
  "start the final report by stating the selected mode once" \
  "omit the selected mode from the final report"
expect_failure "missing conditional mode output" \
  "conditional mode visibility contract is missing" \
  "${validator}" --repo "${case_dir}"

case_dir="$(copy_repo missing-implicit-mode-suppression)"
replace_text "${case_dir}/skills/fructal/SKILL.md" \
  "never expose the internal mode" \
  "always expose the internal mode"
expect_failure "missing implicit mode suppression" \
  "implicit mode suppression contract is missing" \
  "${validator}" --repo "${case_dir}"

case_dir="$(copy_repo missing-mode-phrase-distinction)"
replace_text "${case_dir}/skills/fructal/SKILL.md" \
  "selects the mode internally but does not expose its label" \
  "selects the mode internally and exposes its label"
expect_failure "missing mode phrase distinction" \
  "mode phrase distinction is missing" \
  "${validator}" --repo "${case_dir}"

case_dir="$(copy_repo incomplete-consequential-stop)"
replace_text "${case_dir}/skills/fructal/SKILL.md" \
  "without inventing or prescribing the future" \
  "and prescribe the future"
expect_failure "incomplete consequential stop boundary" \
  "incomplete consequential stop boundary is missing" \
  "${validator}" --repo "${case_dir}"

case_dir="$(copy_repo missing-consequential-confirmation-request)"
replace_text "${case_dir}/skills/fructal/SKILL.md" \
  "for the exact missing items and confirmation" \
  "for the missing details"
expect_failure "missing consequential confirmation request" \
  "consequential confirmation request is missing" \
  "${validator}" --repo "${case_dir}"

case_dir="$(copy_repo announced-automatic-use)"
replace_text "${case_dir}/skills/fructal/SKILL.md" \
  "Do not announce, link, or credit Fructal Cap Design" \
  "Always announce and link Fructal Cap Design"
expect_failure "announced automatic use" \
  "silent automatic use contract is missing" \
  "${validator}" --repo "${case_dir}"

case_dir="$(copy_repo missing-source)"
if mutate_or_record "missing source" delete_line_containing \
  "${case_dir}/skills/fructal/SKILL.md" \
  "https://github.com/PaolaShultz/shr-skills/tree/main/skills/fructal"; then
  expect_failure "missing package source" \
    "metadata.source must be the canonical skill URL" \
    "${validator}" --repo "${case_dir}"
fi

case_dir="$(copy_repo missing-mode-precedence)"
if mutate_or_record "mode precedence" delete_line_containing \
  "${case_dir}/skills/fructal/SKILL.md" \
  "An explicit Review, Redesign, or Implement instruction"; then
  expect_failure "missing explicit-mode precedence" \
    "explicit-mode precedence contract is missing" \
    "${validator}" --repo "${case_dir}"
fi

case_dir="$(copy_repo missing-read-boundary)"
if mutate_or_record "incidental read boundary" delete_line_containing \
  "${case_dir}/skills/fructal/SKILL.md" \
  "ordinary access metadata"; then
  expect_failure "missing incidental-read boundary" \
    "incidental read-side-effect contract is missing" \
    "${validator}" --repo "${case_dir}"
fi

case_dir="$(copy_repo collapsed-evidence)"
if mutate_or_record "evidence dimensions" delete_line_containing \
  "${case_dir}/skills/fructal/SKILL.md" \
  "provided artifact"; then
  expect_failure "collapsed evidence dimensions" \
    "provided-artifact and reported-claim distinction is missing" \
    "${validator}" --repo "${case_dir}"
fi

case_dir="$(copy_repo ambiguous-feedback)"
if mutate_or_record "actor feedback" delete_line_containing \
  "${case_dir}/skills/fructal/SKILL.md" \
  "and software components."; then
  expect_failure "ambiguous actor feedback" \
    "actor-appropriate feedback contract is missing" \
    "${validator}" --repo "${case_dir}"
fi

case_dir="$(copy_repo stale-demo)"
replace_text "${case_dir}/examples/chatgpt-web-demo.md" \
  "# Fructal Cap Design" "# Stale Fructal Cap Design"
expect_failure "stale embedded demo" \
  "embedded ChatGPT demo skill differs from canonical SKILL.md" \
  "${validator}" --repo "${case_dir}"

case_dir="$(copy_repo incorrect-contract-case)"
replace_text "${case_dir}/tests/contract-cases.json" \
  '"expected_mode": "Review"' '"expected_mode": "Implement"'
expect_failure "incorrect contract expectation" \
  "contract case implicit_review must expect Review" \
  "${validator}" --repo "${case_dir}"

case_dir="$(copy_repo incomplete-live-case)"
delete_json_key "${case_dir}/tests/contract-cases.json" 0 "task"
expect_failure "incomplete live contract case" \
  "contract case implicit_review is missing task" \
  "${validator}" --repo "${case_dir}"

case_dir="$(copy_repo incomplete-live-schema)"
delete_schema_required_field \
  "${case_dir}/tests/live-output-schema.json" "rationale"
expect_failure "incomplete live output schema" \
  "live output schema required fields differ" \
  "${validator}" --repo "${case_dir}"

case_dir="$(copy_repo unsupported-live-schema-keyword)"
add_unsupported_unique_items \
  "${case_dir}/tests/live-output-schema.json"
expect_failure "unsupported live output schema keyword" \
  "live output schema uses unsupported keyword uniqueItems" \
  "${validator}" --repo "${case_dir}"

case_dir="$(copy_repo changed-frozen-artifact)"
printf '\nchanged after freeze\n' >> \
  "${case_dir}/docs/evaluations/physical-product-comparison/ppd-003-layered-comparison/README.md"
expect_failure "changed frozen artifact" \
  "frozen artifact checksum differs: docs/evaluations/physical-product-comparison/ppd-003-layered-comparison/README.md" \
  "${validator}" --repo "${case_dir}"

installed_dir="${temporary_root}/installed/fructal"
mkdir -p "${installed_dir}/agents"
cp "${repo_dir}/skills/fructal/SKILL.md" "${installed_dir}/SKILL.md"
cp "${repo_dir}/skills/fructal/agents/openai.yaml" \
  "${installed_dir}/agents/openai.yaml"
printf '\n# stale installed copy\n' >> "${installed_dir}/SKILL.md"
expect_failure "installed-copy drift" \
  "installed SKILL.md differs from source" \
  "${validator}" --repo "${repo_dir}" --installed "${installed_dir}"

if ((failures > 0)); then
  exit 1
fi

printf '%s\n' "PASS: deterministic validation regressions"
