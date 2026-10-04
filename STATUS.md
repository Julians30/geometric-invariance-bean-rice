# Repository preparation status

**Visibility:** Public

**Purpose:** reproducibility package for the manuscript *Geometric Invariance and Representation Sufficiency in Morphometric Bean and Rice Classification*.

## Completed

- [x] Dry Bean provenance and UCI attribution documented.
- [x] INIAP Rice release scope restricted to the 9,200-record tabular morphometric analytical table and reproducibility metadata.
- [x] Data dictionary, frozen split manifests, SHA-256 manifests and release-scope safeguards added.
- [x] Frozen analytical CSVs transferred.
- [x] Frozen split manifests transferred.
- [x] Feature-level notebooks 01–13B transferred with outputs removed.
- [x] Notebook 14 final minor-revision analyses transferred.
- [x] Notebook 15 v4 final publication-figure rebuild transferred.
- [x] Main and supplementary machine-readable analytical tables transferred.
- [x] Numerical claim register and source-reconciliation records added.
- [x] Verified execution environment and dependency documentation added.
- [x] Repository title and citation metadata updated to the final AI manuscript title.
- [x] Repository authors updated to Bryan Orlando Vélez-SanMartín, Julián Coronel-Reyes, and Bryan Iván Barahona-Montalván.
- [x] Data Availability wording aligned with the public repository.
- [x] Repository visibility changed to **Public**.

## Remaining submission checks

- [ ] Run the final strict repository audit:
  ```bash
  python scripts/audit_release_scope.py
  python scripts/audit_notebooks.py
  python scripts/verify_integrity.py --strict
  ```
- [ ] Confirm final repository contents against the exact manuscript and supplementary files being submitted.
- [ ] Decide code/documentation licensing separately from dataset rights.
- [ ] Do not claim a repository DOI unless a real archival DOI has been minted.

## Public repository

https://github.com/Julians30/geometric-invariance-bean-rice

## Release boundary

The reproducibility package is limited to the **tabular morphometric analytical workflow** and associated code, splits, outputs, tables, and integrity records. Original visual assets are outside this repository scope.
