#!/usr/bin/env python3
"""Audit the repository release boundary.

This guardrail protects the manuscript repository from accidental inclusion of
original INIAP Rice visual assets. Analytical plots under ``figures/`` are not
prohibited; the restriction applies to raw/acquisition/segmentation material
and raster image files placed under ``data/``.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FORBIDDEN_DIR_NAMES = {
    "raw_images",
    "images_raw",
    "segmentation_masks",
    "masks",
    "acquisition_raw",
}

RASTER_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".tif",
    ".tiff",
    ".webp",
}

REQUIRED_DOCUMENTS = {
    "README.md",
    "DATA_RIGHTS.md",
    "DATA_AVAILABILITY.md",
    "REPRODUCIBILITY.md",
    "STATUS.md",
    "data/README.md",
    "manifests/release_scope.csv",
}


def main() -> int:
    problems: list[str] = []

    for required in sorted(REQUIRED_DOCUMENTS):
        if not (ROOT / required).exists():
            problems.append(f"Missing required repository document: {required}")

    for path in ROOT.rglob("*"):
        if ".git" in path.parts:
            continue

        relative = path.relative_to(ROOT)

        if path.is_dir() and path.name.lower() in FORBIDDEN_DIR_NAMES:
            problems.append(f"Forbidden raw-asset directory present: {relative}")

        if path.is_file() and "data" in relative.parts and path.suffix.lower() in RASTER_EXTENSIONS:
            problems.append(f"Raster image found inside feature-table data scope: {relative}")

    if problems:
        print("RELEASE-SCOPE AUDIT: FAIL")
        for problem in problems:
            print(f" - {problem}")
        return 1

    print("RELEASE-SCOPE AUDIT: PASS")
    print("No prohibited original INIAP visual assets were detected in the release scope.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
