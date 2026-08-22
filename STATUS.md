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
- [x] Frozen partition summaries and class distributions added.
- [x] Leakage-audit structure documented.
- [x] Reconciled seven main machine-readable tables added from Notebook 13B assets.
- [x] Key supplementary tables added, including source reconciliation, exact model metadata, bootstrap intervals, calibration, classwise performance, representation audit, exact McNemar tests, rice equivalence, leakage-sensitivity audits, source-validation summary, and confusion matrices.
- [x] Numerical claim register and final Notebook 13B validation added.
- [x] Internal-to-manuscript representation-label mapping documented.
- [x] Verified execution environment and dependency file added.
- [x] Working pre-publication and post-publication Data Availability statements added.
- [x] Citation metadata added.

## Pending large-file transfer

The following frozen analytical files have been verified against the project Drive and integrity manifests but still require final transfer into GitHub because they are multi-megabyte files:

- [ ] `data/dry_bean_frozen_v1.csv` — 13,611 rows
- [ ] `data/iniap_rice_frozen_v1.csv` — 9,200 rows
- [ ] `splits/dry_bean_split_manifest_v1.csv`
- [ ] `splits/iniap_rice_split_manifest_v1.csv`

These files must be transferred **without modification** so that the recorded SHA-256 values remain valid.

## Before manuscript submission

- [ ] Confirm final repository contents against the manuscript version being submitted.
- [ ] Confirm whether a separate code license will be assigned; do not apply a blanket data license to original INIAP Rice data without an explicit decision.
- [ ] Replace the manuscript's MDPI placeholder Supplementary Materials text with the actual supporting-material description.
- [ ] Replace the manuscript's generic Data Availability Statement with the repository-specific wording when access policy is finalized.
- [ ] Keep repository private until the authors decide that reviewer/editor/public access is appropriate.

## Release boundary

No release step should add original INIAP Rice grain images, segmentation masks, or raw image-acquisition material. Those assets remain outside this repository and outside the article's reproducibility package.
