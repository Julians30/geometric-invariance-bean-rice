#!/usr/bin/env python3
"""Verify frozen analytical files against the repository integrity manifest.

The script checks only feature-level analytical assets. It does not expect or
validate original INIAP Rice images, segmentation masks, or acquisition files.
"""

from __future__ import annotations

import csv
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifests" / "frozen_file_manifest.csv"

REPOSITORY_PATHS = {
    ("dry_bean", "csv"): ROOT / "data" / "dry_bean_frozen_v1.csv",
    ("iniap_rice", "csv"): ROOT / "data" / "iniap_rice_frozen_v1.csv",
    ("dry_bean", "parquet"): ROOT / "data" / "dry_bean_frozen_v1.parquet",
    ("iniap_rice", "parquet"): ROOT / "data" / "iniap_rice_frozen_v1.parquet",
}


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(chunk_size), b""):
            digest.update(chunk)
    return digest.hexdigest()


def count_csv(path: Path) -> tuple[int, int]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        header = next(reader)
        rows = sum(1 for _ in reader)
    return rows, len(header)


def main() -> int:
    if not MANIFEST.exists():
        print(f"ERROR: manifest not found: {MANIFEST}")
        return 2

    failures = 0
    checked = 0
    pending = 0

    with MANIFEST.open("r", encoding="utf-8-sig", newline="") as handle:
        for record in csv.DictReader(handle):
            key = (record["dataset_id"], record["format"])
            target = REPOSITORY_PATHS.get(key)
            if target is None:
                continue

            if not target.exists():
                print(f"PENDING: {target.relative_to(ROOT)}")
                pending += 1
                continue

            checked += 1
            expected_hash = record["sha256"].strip().lower()
            observed_hash = sha256_file(target)
            hash_ok = observed_hash == expected_hash

            size_ok = target.stat().st_size == int(record["size_bytes"])
            shape_ok = True
            shape_note = ""
            if record["format"] == "csv":
                rows, cols = count_csv(target)
                shape_ok = rows == int(record["rows"]) and cols == int(record["columns"])
                shape_note = f", rows={rows}, columns={cols}"

            ok = hash_ok and size_ok and shape_ok
            status = "PASS" if ok else "FAIL"
            print(
                f"{status}: {target.relative_to(ROOT)} "
                f"sha256={observed_hash}, bytes={target.stat().st_size}{shape_note}"
            )
            if not ok:
                failures += 1

    print(f"\nChecked: {checked}; pending: {pending}; failures: {failures}")
    if failures:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
