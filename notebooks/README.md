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

## Current published notebooks

The complete feature-level analytical sequence **01–15, including 13B**, is published in this folder. Notebooks 01–13B were distributed as output-stripped source copies. Notebooks 14 and 15 have also been cleaned of stored execution outputs and non-null execution counters, without modifying their code cells.

The historical `../manifests/notebook_release_audit.csv` records the original cleaning and preparation of notebooks 01–13B; its `pending_transfer` statuses describe the former preparation stage and are **not the current GitHub availability status**.

The manuscript-facing authority hierarchy and roles for every notebook are recorded in [`INDEX.md`](INDEX.md). Historical `AI_MDPI` substrings in immutable notebook filenames do not signify the current journal; the associated manuscript is submitted to *Agriculture* (MDPI).

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
