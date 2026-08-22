# Repository preparation status

**Visibility:** Private

**Purpose:** pre-submission reproducibility package for the manuscript *Testing Geometric Invariance in Leakage-Safe Bean and Rice Classification*.

## Completed

- [x] Dataset provenance and ownership distinction documented.
- [x] Dry Bean identified as a third-party UCI benchmark attributed to Koklu and Ozkan.
- [x] INIAP Rice identified as original research data; release scope restricted to the 9,200-record morphometric feature table.
- [x] Explicit exclusion of original INIAP Rice images, segmentation masks, and raw acquisition assets.
- [x] Data dictionary added.
- [x] Frozen-file SHA-256 manifest added.
- [x] Explicit release-scope manifest added (`manifests/release_scope.csv`).
- [x] Frozen partition summaries and class distributions added.
- [x] Leakage-audit structure documented.
- [x] Reconciled seven main machine-readable tables added from Notebook 13B assets.
- [x] Supplementary analytical tables transferred, including paired representation contrasts, selective-classification uncertainty, conformal global/classwise results, quantiles, intervals and paired comparisons.
- [x] Numerical claim register and final Notebook 13B validation added.
- [x] Final Notebook 13B output-integrity manifest added.
- [x] Internal-to-manuscript representation-label mapping documented and transfer statuses reconciled.
- [x] Verified execution environment and dependency file added.
- [x] Working pre-publication and post-publication Data Availability statements added.
- [x] Citation metadata added.
- [x] Automated repository release-scope audit added.
- [x] Automated SHA-256/file-size/CSV-shape integrity checker added.
- [x] GitHub Actions workflow added to run release-scope and integrity checks on `main`.
- [x] `.gitignore` strengthened to guard against accidental raw INIAP visual-asset commits.
- [x] Main README expanded with authoritative frozen results and reproducibility source hierarchy.
- [x] Frozen analytical CSVs transferred without intended modification:
  - `data/dry_bean_frozen_v1.csv`
  - `data/iniap_rice_frozen_v1.csv`
- [x] Frozen split manifests transferred:
  - `splits/dry_bean_split_manifest_v1.csv`
  - `splits/iniap_rice_split_manifest_v1.csv`
- [x] Release-safe feature-level notebooks 01–13B transferred to `notebooks/` with outputs removed.
- [x] Final reconciliation protocol transferred.
- [x] Final reconciliation support results transferred to `results/reconciliation/`.
- [x] Six main manuscript figures transferred in both PDF and PNG formats.
- [x] Six supplementary figure pairs transferred in both PDF and PNG formats.

## Transfer status

The planned GitHub transfer bundle has been deposited. No additional files from the prepared pending-transfer package are currently awaiting upload.

The repository is **not yet marked submission-ready** until the final strict audit and manuscript/back-matter reconciliation are completed.

## Before manuscript submission

- [ ] Run the final strict repository audit and confirm that all required frozen files, hashes, CSV shapes, release-scope checks and notebook checks pass.
- [ ] Confirm final repository contents against the exact manuscript version being submitted.
- [ ] Confirm whether a separate code license will be assigned; do not apply a blanket data license to original INIAP Rice data without an explicit decision.
- [ ] Replace the manuscript's MDPI placeholder Supplementary Materials text with the actual supporting-material description.
- [ ] Replace the manuscript's generic Data Availability Statement with repository-specific wording consistent with the repository remaining private during manuscript preparation.
- [ ] Resolve any remaining manuscript back-matter placeholders using verified author information only.
- [ ] Keep repository private until the authors decide that reviewer/editor/public access is appropriate and journal requirements are confirmed.
- [ ] Do not add a repository DOI or claim public availability until a real archival/public release exists.

## Final verification commands

```bash
python scripts/audit_release_scope.py
python scripts/audit_notebooks.py
python scripts/verify_integrity.py --strict
```

Equivalent Makefile target when run from a local clone:

```bash
make release-check
```

## Release boundary

No release step should add original INIAP Rice grain images, segmentation masks, or raw image-acquisition material. Those assets remain outside this repository and outside the article's feature-level reproducibility package.
