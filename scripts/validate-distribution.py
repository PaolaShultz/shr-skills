#!/usr/bin/env python3
"""Validate cross-host packaging without changing the canonical skill."""

from __future__ import annotations

from html.parser import HTMLParser
import json
from pathlib import Path
import re
import struct
import sys
import xml.etree.ElementTree as ET

import yaml


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "distribution" / "plugins" / "fructal"
VERSION = "1.2.0"


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag not in {"a", "link", "img"}:
            return
        values = dict(attrs)
        for field in ("href", "src"):
            value = values.get(field)
            if value:
                self.links.append(value)


def load_json(path: Path, errors: list[str]) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"{path.relative_to(ROOT)} is not valid JSON: {error}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"{path.relative_to(ROOT)} must contain an object")
        return {}
    return value


def check_equal(left: Path, right: Path, label: str, errors: list[str]) -> None:
    try:
        if left.read_bytes() != right.read_bytes():
            errors.append(f"{label} is not byte-identical to its canonical source")
    except OSError as error:
        errors.append(f"cannot compare {label}: {error}")


def check_manifest(path: Path, host: str, errors: list[str]) -> None:
    value = load_json(path, errors)
    expected = {
        "name": "fructal",
        "version": VERSION,
        "skills": "./skills/",
    }
    for key, wanted in expected.items():
        if value.get(key) != wanted:
            errors.append(f"{host} manifest {key} must be {wanted!r}")
    display_name = value.get(
        "displayName", value.get("interface", {}).get("displayName")
    )
    if display_name != "Fructal Cap Design":
        errors.append(f"{host} manifest must use the public name Fructal Cap Design")


def check_test_cases(errors: list[str]) -> None:
    path = ROOT / "distribution" / "submission-test-cases.json"
    value = load_json(path, errors)
    if value.get("version") != VERSION:
        errors.append(f"submission test cases version must be {VERSION!r}")
    contract_path = ROOT / "tests" / "contract-cases.json"
    try:
        contract_cases = json.loads(contract_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"cannot read contract cases: {error}")
        contract_cases = []
    if not isinstance(contract_cases, list):
        errors.append("contract cases must contain an array")
        contract_cases = []
    contract_ids = {
        case["id"] for case in contract_cases
        if isinstance(case, dict) and isinstance(case.get("id"), str)
    }
    positives = value.get("positive")
    negatives = value.get("negative")
    if not isinstance(positives, list) or len(positives) < 5:
        errors.append("submission test cases require at least five positive cases")
        positives = []
    if not isinstance(negatives, list) or len(negatives) < 3:
        errors.append("submission test cases require at least three negative cases")
        negatives = []
    positive_fields = {
        "id", "prompt", "expected_workflow_behavior", "expected_result_shape",
        "fixture", "evidence", "contract_case_ids",
    }
    negative_fields = {
        "id", "scenario", "expected_safe_behavior", "why_not_complete",
    }
    for index, case in enumerate(positives):
        if not isinstance(case, dict) or not positive_fields <= set(case):
            errors.append(f"positive submission case {index + 1} is incomplete")
            continue
        references = case["contract_case_ids"]
        if not isinstance(references, list) or not references or not all(
            isinstance(reference, str) for reference in references
        ):
            errors.append(
                f"positive submission case {index + 1} requires nonempty contract_case_ids"
            )
            continue
        for reference in references:
            if reference not in contract_ids:
                errors.append(
                    f"positive submission case {index + 1} references unknown "
                    f"contract case {reference!r} in tests/contract-cases.json"
                )
    for index, case in enumerate(negatives):
        if not isinstance(case, dict) or not negative_fields <= set(case):
            errors.append(f"negative submission case {index + 1} is incomplete")


def check_issue_template(errors: list[str]) -> None:
    path = ROOT / ".github" / "ISSUE_TEMPLATE" / "adversarial-workflow.yml"
    try:
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as error:
        errors.append(f"issue template is invalid: {error}")
        return
    ids = [
        item.get("id")
        for item in value.get("body", [])
        if isinstance(item, dict) and item.get("type") != "markdown"
    ]
    expected = [
        "starting-state",
        "necessary-constraint",
        "obstructed-motion",
        "expected-boundary",
        "observed-response",
        "reproducibility",
    ]
    if ids != expected:
        errors.append("issue template fields do not match the external-case contract")
    for item in value.get("body", []):
        if isinstance(item, dict) and item.get("type") != "markdown":
            if item.get("validations", {}).get("required") is not True:
                errors.append(f"issue template field {item.get('id')} must be required")


def check_site(errors: list[str]) -> None:
    required = {
        "index.html", "privacy.html", "terms.html", "assets/site.css", ".nojekyll",
    }
    for name in required:
        if not (ROOT / "docs" / name).is_file():
            errors.append(f"landing site is missing docs/{name}")

    for page in (ROOT / "docs").glob("*.html"):
        parser = LinkParser()
        try:
            parser.feed(page.read_text(encoding="utf-8"))
        except OSError as error:
            errors.append(f"cannot read {page.relative_to(ROOT)}: {error}")
            continue
        for link in parser.links:
            if link.startswith(("https://", "http://", "mailto:", "#")):
                continue
            target = (page.parent / link.split("#", 1)[0]).resolve()
            if not target.exists():
                errors.append(
                    f"{page.relative_to(ROOT)} has missing local target {link}"
                )


def check_assets(errors: list[str]) -> None:
    expected = {
        "fructal-icon.svg": "0 0 512 512",
        "fructal-logo.svg": "0 0 1280 320",
    }
    for name, view_box in expected.items():
        path = PLUGIN / "assets" / name
        try:
            root = ET.parse(path).getroot()
        except (OSError, ET.ParseError) as error:
            errors.append(f"{path.relative_to(ROOT)} is not valid SVG: {error}")
            continue
        if root.attrib.get("viewBox") != view_box:
            errors.append(f"{path.relative_to(ROOT)} has the wrong viewBox")

    png_expected = {
        "fructal-icon-512.png": (512, 512),
        "fructal-logo-1280x320.png": (1280, 320),
    }
    for name, dimensions in png_expected.items():
        path = PLUGIN / "assets" / name
        try:
            data = path.read_bytes()
            width, height = struct.unpack(">II", data[16:24])
        except (OSError, struct.error) as error:
            errors.append(f"{path.relative_to(ROOT)} is not a readable PNG: {error}")
            continue
        if not data.startswith(b"\x89PNG\r\n\x1a\n") or (width, height) != dimensions:
            errors.append(
                f"{path.relative_to(ROOT)} must be {dimensions[0]} by {dimensions[1]} PNG"
            )


def check_github_discovery_layout(errors: list[str]) -> None:
    """Keep generated wrappers out of GitHub's documented skill conventions."""

    discovered: list[Path] = []
    for candidate in ROOT.rglob("SKILL.md"):
        relative = candidate.relative_to(ROOT)
        parts = relative.parts
        hidden = any(part.startswith(".") for part in parts)
        plugin_ancestor = "plugins" in parts

        root_skill = len(parts) == 2
        plain_skill = (
            len(parts) >= 3
            and parts[-3] == "skills"
            and not hidden
            and not plugin_ancestor
        )
        namespaced_skill = (
            len(parts) >= 4
            and parts[-4] == "skills"
            and not hidden
            and not plugin_ancestor
        )
        plugin_skill = (
            len(parts) == 5
            and parts[0] == "plugins"
            and parts[2] == "skills"
        )
        if root_skill or plain_skill or namespaced_skill or plugin_skill:
            discovered.append(relative)

    expected = [Path("skills/fructal/SKILL.md")]
    if sorted(discovered) != expected:
        rendered = ", ".join(str(path) for path in sorted(discovered)) or "none"
        errors.append(
            "GitHub skill discovery must expose only skills/fructal/SKILL.md; "
            f"found {rendered}"
        )


def check_public_text(errors: list[str]) -> None:
    private_markers = [
        re.compile(r"sk-[A-Za-z0-9]{20,}"),
        re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
        re.compile(r"-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----"),
    ]
    roots = [
        ROOT / "README.md",
        ROOT / ".agents",
        ROOT / ".claude-plugin",
        ROOT / ".github" / "ISSUE_TEMPLATE" / "adversarial-workflow.yml",
        ROOT / "distribution",
        PLUGIN,
        ROOT / "docs" / "index.html",
        ROOT / "docs" / "privacy.html",
        ROOT / "docs" / "terms.html",
        ROOT / "docs" / "assets",
        ROOT / "docs" / "distribution-report-1.1.1.md",
    ]
    paths: list[Path] = []
    for root in roots:
        if root.is_file():
            paths.append(root)
        elif root.is_dir():
            paths.extend(path for path in root.rglob("*") if path.is_file())
    for path in paths:
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for marker in private_markers:
            if marker.search(text):
                errors.append(f"possible private credential in {path.relative_to(ROOT)}")
        misspelling = "fra" + "ctal"
        if re.search(rf"\b{misspelling}\b|{misspelling}-", text, re.IGNORECASE):
            errors.append(
                f"incorrect public-name spelling or technical identifier in {path.relative_to(ROOT)}"
            )


def main() -> None:
    errors: list[str] = []
    check_equal(
        ROOT / "skills" / "fructal" / "SKILL.md",
        PLUGIN / "skills" / "fructal" / "SKILL.md",
        "plugin skill mirror",
        errors,
    )
    check_equal(ROOT / "LICENSE", PLUGIN / "LICENSE", "plugin license", errors)
    check_equal(
        PLUGIN / "assets" / "fructal-icon.svg",
        ROOT / "docs" / "assets" / "fructal-icon.svg",
        "landing-page icon mirror",
        errors,
    )
    check_equal(
        PLUGIN / "assets" / "fructal-logo.svg",
        ROOT / "docs" / "assets" / "fructal-logo.svg",
        "landing-page logo mirror",
        errors,
    )
    check_manifest(PLUGIN / ".codex-plugin" / "plugin.json", "OpenAI", errors)
    check_manifest(PLUGIN / ".claude-plugin" / "plugin.json", "Claude", errors)
    check_test_cases(errors)
    check_issue_template(errors)
    check_site(errors)
    check_assets(errors)
    check_github_discovery_layout(errors)
    check_public_text(errors)

    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        raise SystemExit(1)
    print("PASS: cross-host distribution package")


if __name__ == "__main__":
    main()
