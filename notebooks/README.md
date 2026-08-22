# Analysis notebooks

This directory is reserved for the reproducible notebooks supporting the **feature-level morphometric analyses** reported in the manuscript.

The detailed file-by-file authority hierarchy is maintained in [`INDEX.md`](INDEX.md).

## Analytical sequence

1. Data audit and freeze.
2. Redundancy and representation construction.
3. Frozen partition generation and validation.
4. Training-only model selection.
5. Final fitting, calibration, and primary frozen testing.
6. Paired statistical inference.
7. Selective classification.
8. Canonical conformal prediction.
9. Ablation and morphometric interpretability analyses.
10. Measurement and image-space scale sensitivity.
11. Manuscript tables and analytical figures.
12. Reviewer-driven confirmatory reanalysis.
13. Final manuscript-asset freeze and reconciliation.

## Current transfer status

The notebook names, roles, and source hierarchy are documented, but the release-safe notebook files themselves are still pending final transfer to this repository.

A release audit has now been performed on the complete analytical notebook sequence available in the project archive: **01, 02, 03, 04, 05, 06, 07, 08 canonical v2, 09 v2, 10, 11 final, 12 corrected, 13, and 13B**. Output-stripped copies were created for all 14 notebooks.

Across the complete source sequence, **384 executed outputs and 85 embedded image outputs were removed**, with **zero cell attachments** detected. A targeted source-code audit also found **zero raw-image loading calls or raw raster-file references** matching the release guard patterns. The `.png` references retained in code are generated analytical figures, while `mask` occurrences are analytical Boolean masks rather than segmentation-mask loading operations.

The machine-readable audit, cleaned notebook sizes, and SHA-256 values are stored in `../manifests/notebook_release_audit.csv`.

## Release-safe notebook policy

Notebooks intended for GitHub should be distributed in an **output-stripped form**:

- preserve code cells and Markdown;
- clear code-cell execution counts;
- remove all executed outputs;
- remove cell attachments;
- preserve the analytical logic and notebook metadata needed for reproducibility.

The utility `../scripts/clean_notebook_for_release.py` implements this transformation without modifying source code.

## Required inclusion boundary

Suitable notebook content includes:

- loading frozen morphometric tables;
- duplicate/group auditing;
- representation engineering;
- frozen split use;
- model selection and evaluation;
- calibration, selective classification, and conformal prediction;
- inferential, equivalence, importance, leakage, and image-space scale analyses;
- numerical table and analytical-figure generation.

## Explicit exclusions

Do **not** upload notebooks whose purpose is original INIAP Rice image acquisition, raw-image storage, segmentation-mask generation, or upstream visual preprocessing that exposes unreleased doctoral-research assets.

The repository must remain reproducible from the released morphometric feature table without implying release of the original images or segmentation masks.
