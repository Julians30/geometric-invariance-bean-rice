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

The notebook names, roles, and source hierarchy are documented, but the notebook files themselves are still pending final transfer to this repository. Before transfer, each notebook must be checked to ensure that it contains only the feature-level workflow and does not embed unreleased original INIAP Rice visual assets.

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
