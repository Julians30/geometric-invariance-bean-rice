# Repository preparation status

**Visibility:** Private

**Purpose:** final pre-submission reproducibility package for the manuscript *Geometric Invariance and Representation Sufficiency in Morphometric Bean and Rice Classification*.

## Completed

- [x] Dry Bean provenance and UCI attribution documented.
- [x] INIAP Rice release scope restricted to the 9,200-record tabular morphometric analytical table and reproducibility metadata.
- [x] Data dictionary, frozen split manifests, SHA-256 manifests and release-scope safeguards added.
- [x] Frozen analytical CSVs transferred:
  - `data/dry_bean_frozen_v1.csv`
  - `data/iniap_rice_frozen_v1.csv`
- [x] Frozen split manifests transferred:
  - `splits/dry_bean_split_manifest_v1.csv`
  - `splits/iniap_rice_split_manifest_v1.csv`
- [x] Feature-level notebooks 01–13B transferred with outputs removed.
- [x] Notebook 14 final minor-revision analyses transferred.
- [x] Notebook 15 v4 final publication-figure rebuild transferred.
- [x] Main and supplementary machine-readable analytical tables transferred.
- [x] Numerical claim register and source-reconciliation records added.
- [x] Verified execution environment and dependency documentation added.
- [x] Repository title and citation metadata updated to the final AI manuscript title.
- [x] Repository authors updated to Bryan Orlando Vélez-SanMartín, Julián Coronel-Reyes, and Bryan Iván Barahona-Montalván.
- [x] Data Availability wording aligned with the feature-level tabular reproducibility scope.
- [x] Automated release-scope and integrity checks included.

## Final steps before manuscript submission

- [ ] Run the final strict repository audit:
  ```bash
  python scripts/audit_release_scope.py
  python scripts/audit_notebooks.py
  python scripts/verify_integrity.py --strict
  ```
- [ ] Confirm the final repository contents against the exact manuscript and supplementary files being submitted.
- [ ] Decide code/documentation licensing separately from dataset rights.
- [ ] Change repository visibility from **Private** to **Public** before the manuscript claims that the GitHub materials are publicly available.
- [ ] Once public, replace the manuscript Data Availability Statement with the repository-specific public wording in `DATA_AVAILABILITY.md`.
- [ ] Do not claim a repository DOI unless a real archival DOI has been minted.

## Release boundary

The reproducibility package is limited to the **tabular morphometric analytical workflow** and associated code, splits, outputs, tables, and integrity records. Original visual assets are outside this repository scope.
