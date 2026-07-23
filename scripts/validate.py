#!/usr/bin/env python3
"""Validate the public Fructal skill package with only the Python standard library."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "fructal"
SKILL = SKILL_DIR / "SKILL.md"
AGENT = SKILL_DIR / "agents" / "openai.yaml"
README = ROOT / "README.md"
DEMO = ROOT / "examples" / "chatgpt-web-demo.md"
OLD_SKILL_DIR = ROOT / "skills" / "fructal-cap-design"

failures: list[str] = []


def require(condition: bool, message: str) -> None:
    if not condition:
        failures.append(message)


require(not OLD_SKILL_DIR.exists(), "legacy skills/fructal-cap-design directory remains")

for path in (SKILL, AGENT, README, DEMO):
    require(path.is_file(), f"missing {path.relative_to(ROOT)}")

skill_text = SKILL.read_text() if SKILL.is_file() else ""
agent_text = AGENT.read_text() if AGENT.is_file() else ""
readme_text = README.read_text() if README.is_file() else ""
demo_text = DEMO.read_text() if DEMO.is_file() else ""

require(re.search(r"^name: fructal$", skill_text, re.MULTILINE) is not None, "skill name is not fructal")
require(
    re.search(r"^description: Use when ", skill_text, re.MULTILINE) is not None,
    "description does not start with 'Use when'",
)
require("$fructal" in agent_text, "agent prompt does not invoke $fructal")
require("fructal-cap-design" not in agent_text, "agent metadata uses the legacy invocation")

for term in ("product", "service", "system", "physical"):
    require(term in skill_text.lower(), f"skill does not cover {term} workflows")

for term in ("Review", "Redesign", "Implement"):
    require(term in skill_text, f"skill does not define {term} mode")

for term in ("observed", "inference", "open question"):
    require(term in skill_text, f"skill does not classify {term} evidence")

for term in ("actor", "handoff", "delayed"):
    require(term in skill_text.lower(), f"skill does not address {term}")

require("purely aesthetic" in skill_text.lower(), "skill lacks an aesthetic false-positive boundary")
require("isolated defect" in skill_text.lower(), "skill lacks an isolated-defect boundary")
require("decision" in skill_text.lower() and "one click" in skill_text.lower(), "coherent motion is not qualified")

require("skills/fructal" in readme_text, "README does not use the new skill path")
require("$fructal" in readme_text, "README does not show the short invocation")
require("SHR-DAW" in readme_text, "README does not preserve provenance")
require("not affiliated" in readme_text.lower(), "README lacks the independence disclaimer")
require("examples/chatgpt-web-demo.md" in readme_text, "README does not link the demonstration")
require("ChatGPT Web" in readme_text, "README does not identify the standard ChatGPT demonstration")
require(
    re.search(r"no\s+installation", readme_text, re.IGNORECASE) is not None,
    "README does not explain that the demo needs no installation",
)

require("First message" in demo_text and "Second message" in demo_text, "demonstration lacks the two-message sequence")
require(
    "raw.githubusercontent.com/PaolaShultz/shr-skills/main/skills/fructal/SKILL.md" in demo_text,
    "demonstration does not link the raw skill text",
)
require("analysis and report only" in demo_text.lower(), "demonstration is not explicitly review-only")
require("expected answer" not in demo_text.lower(), "demonstration leaks an expected answer")

require(len(skill_text.split()) <= 650, "SKILL.md exceeds the 650-word portability budget")

if failures:
    for failure in failures:
        print(f"FAIL: {failure}")
    sys.exit(1)

print("PASS: Fructal package structure and universal contract are valid")
