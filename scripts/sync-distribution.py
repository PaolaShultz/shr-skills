#!/usr/bin/env python3
"""Synchronize generated host packages from the canonical Fructal Cap Design source."""

from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "fructal"


def main() -> None:
    skill_source = ROOT / "skills" / "fructal" / "SKILL.md"
    skill_target = PLUGIN / "skills" / "fructal" / "SKILL.md"
    license_source = ROOT / "LICENSE"
    license_target = PLUGIN / "LICENSE"
    icon_source = PLUGIN / "assets" / "fructal-icon.svg"
    icon_target = ROOT / "docs" / "assets" / "fructal-icon.svg"
    logo_source = PLUGIN / "assets" / "fructal-logo.svg"
    logo_target = ROOT / "docs" / "assets" / "fructal-logo.svg"

    skill_target.parent.mkdir(parents=True, exist_ok=True)
    icon_target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(skill_source, skill_target)
    shutil.copyfile(license_source, license_target)
    shutil.copyfile(icon_source, icon_target)
    shutil.copyfile(logo_source, logo_target)
    print(f"synced {skill_target.relative_to(ROOT)}")
    print(f"synced {license_target.relative_to(ROOT)}")
    print(f"synced {icon_target.relative_to(ROOT)}")
    print(f"synced {logo_target.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
