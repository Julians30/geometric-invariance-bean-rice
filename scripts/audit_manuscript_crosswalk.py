#!/usr/bin/env python3
"""Audit manuscript supplementary-label mappings against repository assets.

The manuscript-facing label sequence (S1a, S1b, S4b, S4c, etc.) is different
from the frozen Notebook 13B internal filename sequence. This script prevents
silent numbering drift by verifying that every mapping marked ``available``
points to at least one existing repository asset and that each path explicitly
listed in an available mapping exists.

Mappings marked ``pending_transfer`` are reported but do not fail preparation
mode. Use ``--strict`` before release to require all crosswalk entries to be
available.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CROSSWALK = ROOT / "tables" / "supplementary" / "manuscript_label_crosswalk.csv"


def referenced_paths(value: str) -> list[str]:
    paths: list[str] = []
    for item in value.split("|"):
        cleaned = item.strip()
        if not cleaned:
            continue
        # Keep only repository-relative path-like references.
        if "/" in cleaned and not cleaned.startswith("http"):
            paths.append(cleaned)
    return paths


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Fail if any manuscript supplementary mapping is still pending transfer.",
    )
    args = parser.parse_args()

    if not CROSSWALK.exists():
        print(f"MANUSCRIPT CROSSWALK AUDIT: FAIL — missing {CROSSWALK.relative_to(ROOT)}")
        return 2

    failures: list[str] = []
    pending: list[str] = []
    checked = 0

    with CROSSWALK.open("r", encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            checked += 1
            label = row["manuscript_label"].strip()
            status = row["status"].strip()
            paths = referenced_paths(row["repository_or_project_asset"])

            if status == "available":
                if not paths:
                    failures.append(f"{label}: available mapping contains no repository path")
                    continue
                for relative in paths:
                    if not (ROOT / relative).exists():
                        failures.append(f"{label}: mapped available asset is missing: {relative}")
            else:
                pending.append(f"{label}: {status}")

    if failures:
        print("MANUSCRIPT CROSSWALK AUDIT: FAIL")
        for failure in failures:
            print(f" - {failure}")
        return 1

    if args.strict and pending:
        print("MANUSCRIPT CROSSWALK AUDIT: FAIL (strict mode)")
        for item in pending:
            print(f" - {item}")
        return 1

    print("MANUSCRIPT CROSSWALK AUDIT: PASS")
    print(f"Checked {checked} manuscript supplementary mappings.")
    if pending:
        print("Pending transfer mappings:")
        for item in pending:
            print(f" - {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
