#!/usr/bin/env python3
"""Deterministically validate the frozen ZIT cross-renderer archive."""

from __future__ import annotations

import binascii
import hashlib
import json
import struct
import zlib
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE_ROOT = ROOT.parents[1]
EXPECTED_CONDITIONS = {
    "control",
    "superpowers",
    "fructal-cap-design",
    "combined",
}
SOURCE_CALLS = {
    "control": SOURCE_ROOT / "image-instruction-chains/control/call-01.json",
    "superpowers": (
        SOURCE_ROOT / "image-instruction-chains/superpowers/call-01.json"
    ),
    "fructal-cap-design": (
        SOURCE_ROOT / "image-instruction-chains/treatment/call-01.json"
    ),
    "combined": SOURCE_ROOT / "image-instruction-chains/combined/call-01.json",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_png(path: Path) -> tuple[int, int]:
    data = path.read_bytes()
    assert data[:8] == b"\x89PNG\r\n\x1a\n", f"bad PNG signature: {path}"
    offset = 8
    width = height = None
    color_type = None
    bit_depth = None
    compressed = bytearray()
    saw_iend = False
    while offset < len(data):
        length = struct.unpack(">I", data[offset : offset + 4])[0]
        chunk_type = data[offset + 4 : offset + 8]
        payload = data[offset + 8 : offset + 8 + length]
        stored_crc = struct.unpack(
            ">I", data[offset + 8 + length : offset + 12 + length]
        )[0]
        actual_crc = binascii.crc32(chunk_type + payload) & 0xFFFFFFFF
        assert stored_crc == actual_crc, f"bad PNG CRC: {path} {chunk_type!r}"
        if chunk_type == b"IHDR":
            width, height, bit_depth, color_type, _, _, interlace = struct.unpack(
                ">IIBBBBB", payload
            )
            assert interlace == 0, f"unexpected interlace: {path}"
        elif chunk_type == b"IDAT":
            compressed.extend(payload)
        elif chunk_type == b"IEND":
            saw_iend = True
        offset += 12 + length
    assert saw_iend and offset == len(data), f"incomplete PNG: {path}"
    assert (width, height, bit_depth, color_type) == (
        1536,
        1024,
        8,
        2,
    ), f"unexpected PNG format: {path}"
    pixels = zlib.decompress(bytes(compressed))
    assert len(pixels) == height * (1 + width * 3), f"bad PNG raster: {path}"
    return width, height


def main() -> None:
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    settings = json.loads(
        (ROOT / "frozen-settings.json").read_text(encoding="utf-8")
    )
    assert manifest["status"] == "technically_validated"
    assert manifest["primary_generation_count"] == 8
    assert manifest["retry_count"] == 0
    assert settings["common_generation_controls"] == {
        "width": 1536,
        "height": 1024,
        "batch_size": 1,
        "seed": 25072026,
        "steps": 12,
        "cfg": 1,
        "sampler_name": "dpmpp_2m_sde_heun_gpu",
        "scheduler": "simple",
        "denoise": 1,
        "model_shift": 4.0,
        "lora": None,
    }

    jobs = manifest["jobs"]
    outputs = manifest["outputs"]
    assert len(jobs) == len(outputs) == 8
    expected_pairs = {
        (set_id, condition)
        for set_id in ("set-a", "set-b")
        for condition in EXPECTED_CONDITIONS
    }
    assert {(job["set"], job["condition"]) for job in jobs} == expected_pairs
    assert {(item["set"], item["condition"]) for item in outputs} == expected_pairs

    for condition, source_path in SOURCE_CALLS.items():
        source = json.loads(source_path.read_text(encoding="utf-8"))
        archived = (
            ROOT / "prompts" / "exact-transfer" / f"{condition}.txt"
        ).read_text(encoding="utf-8")
        assert archived == source["arguments"]["prompt"]
    correction = json.loads(
        (
            SOURCE_ROOT
            / "image-instruction-chains/superpowers/call-02.json"
        ).read_text(encoding="utf-8")
    )
    assert (
        ROOT / "prompts/superpowers-source-correction-evidence.txt"
    ).read_text(encoding="utf-8") == correction["arguments"]["prompt"]

    output_hashes = set()
    for job in jobs:
        pair = (job["set"], job["condition"])
        output = next(
            item
            for item in outputs
            if (item["set"], item["condition"]) == pair
        )
        prompt_path = ROOT / job["prompt_path"]
        workflow_path = ROOT / job["workflow_path"]
        output_path = ROOT / output["path"]
        history_path = (
            ROOT / "logs" / f"{job['set']}-{job['condition']}-history.json"
        )
        workflow = json.loads(workflow_path.read_text(encoding="utf-8"))
        history = json.loads(history_path.read_text(encoding="utf-8"))

        assert sha256(prompt_path) == job["prompt_sha256"]
        assert sha256(workflow_path) == job["workflow_sha256"]
        assert workflow["4"]["inputs"]["text"] == prompt_path.read_text(
            encoding="utf-8"
        )
        assert workflow["2"]["inputs"]["shift"] == 4.0
        assert workflow["6"]["inputs"] == {
            "width": 1536,
            "height": 1024,
            "batch_size": 1,
        }
        assert workflow["7"]["inputs"]["seed"] == 25072026
        assert workflow["7"]["inputs"]["steps"] == 12
        assert workflow["7"]["inputs"]["cfg"] == 1
        assert workflow["7"]["inputs"]["sampler_name"] == (
            "dpmpp_2m_sde_heun_gpu"
        )
        assert workflow["7"]["inputs"]["scheduler"] == "simple"
        assert workflow["7"]["inputs"]["denoise"] == 1
        assert "11" not in workflow
        assert history["prompt"][1] == output["prompt_id"]
        assert history["prompt"][2] == workflow
        assert history["status"]["status_str"] == "success"
        assert history["status"]["completed"] is True
        history_images = [
            image
            for node in history["outputs"].values()
            for image in node.get("images", [])
        ]
        assert len(history_images) == 1
        assert history_images[0]["filename"].startswith(
            f"{job['condition']}_"
        )
        assert output_path.stat().st_size == output["size_bytes"]
        assert sha256(output_path) == output["sha256"]
        assert validate_png(output_path) == (output["width"], output["height"])
        output_hashes.add(output["sha256"])
    assert len(output_hashes) == 8

    events = [
        json.loads(line)
        for line in (ROOT / "logs/generation-log.jsonl")
        .read_text(encoding="utf-8")
        .splitlines()
    ]
    completions = [event for event in events if event["event"] == "completed"]
    assert len(completions) == 8
    assert {
        (event["set"], event["condition"]) for event in completions
    } == expected_pairs
    assert all(event["visual_inspection_performed"] is False for event in completions)
    retry_record = json.loads(
        (ROOT / "logs/failure-retries.json").read_text(encoding="utf-8")
    )
    assert retry_record["failure_count"] == 0
    assert retry_record["retry_count"] == 0
    assert retry_record["failures"] == []
    assert retry_record["retries"] == []
    print("PASS: 8 frozen ZIT jobs, 8 unique valid PNGs, 0 failures, 0 retries")


if __name__ == "__main__":
    main()
