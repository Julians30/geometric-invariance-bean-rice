#!/usr/bin/env python3
"""Create a release-safe Jupyter notebook copy.

The cleaner preserves code, Markdown, and notebook metadata needed for
reproducibility while removing executed outputs, execution counts, and cell
attachments. This prevents embedded analytical figures—or any accidentally
embedded visual material—from being distributed inside notebook JSON.

It does not alter code logic or source text.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def clean_notebook(source: Path, destination: Path) -> dict[str, int | str]:
    with source.open("r", encoding="utf-8") as handle:
        notebook = json.load(handle)

    outputs_removed = 0
    image_outputs_removed = 0
    attachments_removed = 0

    for cell in notebook.get("cells", []):
        if cell.get("cell_type") == "code":
            for output in cell.get("outputs", []):
                outputs_removed += 1
                for mime_type in output.get("data", {}):
                    if str(mime_type).startswith("image/"):
                        image_outputs_removed += 1
            cell["outputs"] = []
            cell["execution_count"] = None

        attachments = cell.get("attachments")
        if attachments:
            attachments_removed += len(attachments)
            cell.pop("attachments", None)

    metadata = notebook.get("metadata", {})
    metadata.pop("widgets", None)

    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8") as handle:
        json.dump(notebook, handle, ensure_ascii=False, indent=1)
        handle.write("\n")

    return {
        "outputs_removed": outputs_removed,
        "image_outputs_removed": image_outputs_removed,
        "attachments_removed": attachments_removed,
        "clean_size_bytes": destination.stat().st_size,
        "clean_sha256": sha256_file(destination),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()

    report = clean_notebook(args.source, args.destination)
    print(f"Release-safe notebook written to: {args.destination}")
    for key, value in report.items():
        print(f"{key}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
