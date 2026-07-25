#!/usr/bin/env python3
"""Submit one frozen ZIT set and archive results without opening the images."""

from __future__ import annotations

import argparse
import hashlib
import json
import time
import urllib.parse
import urllib.request
import uuid
from datetime import datetime, timezone
from pathlib import Path


ARCHIVE = Path(__file__).resolve().parent
CONDITIONS = ("control", "superpowers", "fructal-cap-design", "combined")
SERVERS = {
    "control": "http://127.0.0.1:8188",
    "superpowers": "http://127.0.0.1:8189",
    "fructal-cap-design": "http://127.0.0.1:8188",
    "combined": "http://127.0.0.1:8189",
}


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def request_json(url: str, payload: dict | None = None) -> dict:
    data = None
    headers = {}
    if payload is not None:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(url, data=data, headers=headers)
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def write_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def append_event(value: dict) -> None:
    with (ARCHIVE / "logs" / "generation-log.jsonl").open(
        "a", encoding="utf-8"
    ) as stream:
        stream.write(json.dumps(value, ensure_ascii=False) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("set_id", choices=("set-a", "set-b"))
    args = parser.parse_args()
    set_id = args.set_id
    output_dir = ARCHIVE / "outputs" / set_id
    submissions_path = ARCHIVE / "logs" / f"{set_id}-submissions.json"
    if submissions_path.exists() or any(output_dir.glob("*.png")):
        raise SystemExit(f"refusing to rerun frozen set with existing state: {set_id}")

    submissions = []
    for condition in CONDITIONS:
        server = SERVERS[condition]
        workflow_path = (
            ARCHIVE / "workflows" / "jobs" / f"{set_id}-{condition}.api.json"
        )
        workflow_bytes = workflow_path.read_bytes()
        graph = json.loads(workflow_bytes)
        submitted_at = now()
        result = request_json(
            f"{server}/prompt",
            {"prompt": graph, "client_id": str(uuid.uuid4())},
        )
        record = {
            "set": set_id,
            "condition": condition,
            "server": server,
            "submitted_at": submitted_at,
            "prompt_id": result["prompt_id"],
            "queue_number": result.get("number"),
            "workflow_sha256": hashlib.sha256(workflow_bytes).hexdigest(),
        }
        submissions.append(record)
        append_event({"event": "submitted", **record})
    write_json(submissions_path, submissions)

    pending = {record["prompt_id"]: record for record in submissions}
    deadline = time.monotonic() + 1800
    while pending and time.monotonic() < deadline:
        for prompt_id, record in list(pending.items()):
            history = request_json(f"{record['server']}/history/{prompt_id}")
            if prompt_id not in history:
                continue
            item = history[prompt_id]
            write_json(
                ARCHIVE
                / "logs"
                / f"{set_id}-{record['condition']}-history.json",
                item,
            )
            images = [
                image
                for output in item.get("outputs", {}).values()
                for image in output.get("images", [])
            ]
            if len(images) != 1:
                raise RuntimeError(
                    f"{set_id}/{record['condition']} returned "
                    f"{len(images)} images"
                )
            image = images[0]
            params = urllib.parse.urlencode(
                {
                    "filename": image["filename"],
                    "subfolder": image.get("subfolder", ""),
                    "type": image.get("type", "output"),
                }
            )
            with urllib.request.urlopen(
                f"{record['server']}/view?{params}", timeout=60
            ) as response:
                image_bytes = response.read()
            output_path = output_dir / f"{record['condition']}.png"
            output_path.write_bytes(image_bytes)
            append_event(
                {
                    "event": "completed",
                    **record,
                    "completed_at": now(),
                    "comfyui_filename": image["filename"],
                    "comfyui_subfolder": image.get("subfolder", ""),
                    "output_path": str(output_path.relative_to(ARCHIVE)),
                    "output_sha256": hashlib.sha256(image_bytes).hexdigest(),
                    "output_size_bytes": len(image_bytes),
                    "visual_inspection_performed": False,
                }
            )
            del pending[prompt_id]
        if pending:
            time.sleep(2)
    if pending:
        raise TimeoutError(f"timed out waiting for: {sorted(pending)}")


if __name__ == "__main__":
    main()
