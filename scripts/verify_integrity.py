#!/usr/bin/env python3
"""Verify the four release-intended frozen CSV files.

The article reproducibility package is intended to release two frozen
feature-level datasets and two frozen split manifests. Original INIAP Rice
images, segmentation masks, and acquisition files are outside this scope.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_MANIFEST = ROOT / "manifests" / "frozen_file_manifest.csv"
SPLIT_MANIFEST = ROOT / "manifests" / "split_file_manifest.csv"

DATA_PATHS = {
    "dry_bean": ROOT / "data" / "dry_bean_frozen_v1.csv",
    "iniap_rice": ROOT / "data" / "iniap_rice_frozen_v1.csv",
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


def expected_release_files() -> list[dict[str, str]]:
    records: list[dict[str, str]] = []

    if not DATA_MANIFEST.exists():
        raise FileNotFoundError(f"Missing data manifest: {DATA_MANIFEST}")
    if not SPLIT_MANIFEST.exists():
        raise FileNotFoundError(f"Missing split manifest: {SPLIT_MANIFEST}")

    with DATA_MANIFEST.open("r", encoding="utf-8-sig", newline="") as handle:
        for record in csv.DictReader(handle):
            if record["format"] != "csv":
                continue
            dataset_id = record["dataset_id"]
            target = DATA_PATHS.get(dataset_id)
            if target is None:
                continue
            records.append(
                {
                    "asset_type": "frozen_dataset",
                    "dataset_id": dataset_id,
                    "path": str(target.relative_to(ROOT)),
                    "rows": record["rows"],
                    "columns": record["columns"],
                    "size_bytes": record["size_bytes"],
                    "sha256": record["sha256"],
                }
            )

    with SPLIT_MANIFEST.open("r", encoding="utf-8-sig", newline="") as handle:
        for record in csv.DictReader(handle):
            records.append(
                {
                    "asset_type": "frozen_split",
                    "dataset_id": record["dataset_id"],
                    "path": record["path"],
                    "rows": record["rows"],
                    "columns": record["columns"],
                    "size_bytes": record["size_bytes"],
                    "sha256": record["sha256"],
                }
            )

    return records


def verify_record(record: dict[str, str]) -> tuple[str, str]:
    target = ROOT / record["path"]
    if not target.exists():
        return "PENDING", record["path"]

    observed_hash = sha256_file(target)
    observed_size = target.stat().st_size
    rows, columns = count_csv(target)

    hash_ok = observed_hash == record["sha256"].strip().lower()
    size_ok = observed_size == int(record["size_bytes"])
    shape_ok = rows == int(record["rows"]) and columns == int(record["columns"])

    status = "PASS" if hash_ok and size_ok and shape_ok else "FAIL"
    detail = (
        f"{record['path']} | sha256={observed_hash} | bytes={observed_size} "
        f"| rows={rows} | columns={columns}"
    )
    return status, detail


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat missing release-intended files as a failure.",
    )
    args = parser.parse_args()

    try:
        records = expected_release_files()
    except FileNotFoundError as exc:
        print(f"ERROR: {exc}")
        return 2

    failures = 0
    pending = 0
    passed = 0

    print("Frozen release-file integrity verification")
    print("Expected release-intended CSV files:", len(records))

    for record in records:
        status, detail = verify_record(record)
        print(f"{status}: {detail}")
        if status == "PASS":
            passed += 1
        elif status == "PENDING":
            pending += 1
        else:
            failures += 1

    print(f"\nPassed: {passed}; pending: {pending}; failures: {failures}")

    if failures:
        return 1
    if args.strict and pending:
        print("STRICT MODE: pending release-intended files are treated as failure.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
