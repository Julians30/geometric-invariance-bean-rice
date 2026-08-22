#!/usr/bin/env python3
"""Audit release notebooks for embedded outputs and raw-image loading code.

Release notebooks should contain source code and Markdown only. Executed outputs,
cell attachments, and execution counts are removed before distribution. The
source audit flags common raw-image loading calls so that original INIAP Rice
visual assets cannot be accidentally pulled into the article workflow.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_DIR = ROOT / "notebooks"

RAW_IMAGE_LOAD_PATTERNS = {
    "cv2.imread": re.compile(r"\bcv2\s*\.\s*imread\s*\(", re.I),
    "PIL.Image.open": re.compile(r"\bImage\s*\.\s*open\s*\(", re.I),
    "keras.load_img": re.compile(r"\bload_img\s*\(", re.I),
    "skimage.io.imread": re.compile(r"\b(?:skimage\.)?io\s*\.\s*imread\s*\(", re.I),
    "matplotlib.imread": re.compile(r"\b(?:plt|matplotlib\.pyplot)\s*\.\s*imread\s*\(", re.I),
}


def cell_source(cell: dict) -> str:
    source = cell.get("source", "")
    if isinstance(source, list):
        return "".join(str(item) for item in source)
    return str(source)


def main() -> int:
    notebook_files = sorted(NOTEBOOK_DIR.glob("*.ipynb"))
    if not notebook_files:
        print("NOTEBOOK RELEASE AUDIT: PENDING")
        print("No .ipynb release copies are currently present in notebooks/.")
        return 0

    problems: list[str] = []

    for path in notebook_files:
        try:
            notebook = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            problems.append(f"{path.name}: invalid notebook JSON ({exc})")
            continue

        for index, cell in enumerate(notebook.get("cells", []), start=1):
            outputs = cell.get("outputs", [])
            if outputs:
                problems.append(
                    f"{path.name}: cell {index} contains {len(outputs)} executed output(s)"
                )

            if cell.get("attachments"):
                problems.append(f"{path.name}: cell {index} contains attachment(s)")

            if cell.get("cell_type") == "code" and cell.get("execution_count") is not None:
                problems.append(
                    f"{path.name}: cell {index} retains execution_count={cell.get('execution_count')}"
                )

            source = cell_source(cell)
            for label, pattern in RAW_IMAGE_LOAD_PATTERNS.items():
                if pattern.search(source):
                    problems.append(
                        f"{path.name}: cell {index} contains raw-image loading call ({label})"
                    )

    if problems:
        print("NOTEBOOK RELEASE AUDIT: FAIL")
        for problem in problems:
            print(f" - {problem}")
        return 1

    print("NOTEBOOK RELEASE AUDIT: PASS")
    print(
        f"Checked {len(notebook_files)} release notebook(s): no outputs, attachments, "
        "execution counts, or common raw-image loading calls detected."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
