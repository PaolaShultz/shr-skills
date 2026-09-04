#!/usr/bin/env python3
"""Synchronize generated host packages from the canonical Fructal Cap Design source."""

from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "fractal-cap-design"


def main() -> None:
    skill_source = ROOT / "skills" / "fructal" / "SKILL.md"
    skill_target = PLUGIN / "skills" / "fructal" / "SKILL.md"
    license_source = ROOT / "LICENSE"
    license_target = PLUGIN / "LICENSE"
    icon_source = PLUGIN / "assets" / "fractal-cap-icon.svg"
    icon_target = ROOT / "docs" / "assets" / "fractal-cap-icon.svg"
    logo_source = PLUGIN / "assets" / "fractal-cap-logo.svg"
    logo_target = ROOT / "docs" / "assets" / "fractal-cap-logo.svg"

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
