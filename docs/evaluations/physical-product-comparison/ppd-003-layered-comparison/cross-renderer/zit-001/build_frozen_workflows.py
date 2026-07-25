#!/usr/bin/env python3
"""Build the eight frozen ZIT API graphs without changing source workflows."""

from __future__ import annotations

import json
from pathlib import Path


ARCHIVE = Path(__file__).resolve().parent
SOURCE_WORKFLOW = Path(
    "/home/shome/.hermes/skills/comfyui-skill/data/local/"
    "z-image-turbo-bf16-userflow-api/workflow.json"
)
CONDITIONS = ("control", "superpowers", "fructal-cap-design", "combined")
SETS = {
    "set-a": ARCHIVE / "prompts" / "exact-transfer",
    "set-b": ARCHIVE / "prompts" / "adapted",
}
SEED = 25072026


def build(set_id: str, condition: str, prompt_path: Path) -> dict:
    graph = json.loads(SOURCE_WORKFLOW.read_text(encoding="utf-8"))
    graph["2"]["inputs"]["shift"] = 4.0
    graph["4"]["inputs"]["text"] = prompt_path.read_text(encoding="utf-8")
    graph["6"]["inputs"].update(
        {"width": 1536, "height": 1024, "batch_size": 1}
    )
    graph["7"]["inputs"].update(
        {
            "seed": SEED,
            "steps": 12,
            "cfg": 1,
            "sampler_name": "dpmpp_2m_sde_heun_gpu",
            "scheduler": "simple",
            "denoise": 1,
        }
    )
    graph["10"]["inputs"]["filename_prefix"] = (
        f"ppd-003-zit/{set_id}/{condition}"
    )
    return graph


def main() -> None:
    output_dir = ARCHIVE / "workflows" / "jobs"
    output_dir.mkdir(parents=True, exist_ok=True)
    for set_id, prompt_dir in SETS.items():
        for condition in CONDITIONS:
            graph = build(set_id, condition, prompt_dir / f"{condition}.txt")
            output = output_dir / f"{set_id}-{condition}.api.json"
            output.write_text(
                json.dumps(graph, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )


if __name__ == "__main__":
    main()
