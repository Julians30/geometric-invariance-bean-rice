# Submission-ready repository wording

This file contains working text for the manuscript and submission system. It should be synchronized with the exact repository access policy used at submission.

## Data Availability Statement — while repository remains private

> **Data Availability Statement:** The Dry Bean dataset used in this study is a public third-party benchmark available from the UCI Machine Learning Repository (Koklu and Ozkan, 2020; https://doi.org/10.24432/C50S4B). The INIAP Rice dataset used in the present analysis is an original 9,200-record morphometric dataset generated within the authors' research. The article reproducibility package is restricted to the derived numerical morphometric feature table, prespecified leakage-safe train/calibration/test split assignments, feature-level analysis code, numerical outputs, and integrity manifests. The project repository is maintained privately during manuscript preparation and will be made accessible in accordance with the journal's review and publication requirements. Original INIAP Rice grain images, segmentation masks, raw image-acquisition assets, and other unreleased visual materials are not included because they form part of an ongoing doctoral research programme. The released feature-level resources are intended to reproduce the statistical and machine-learning analyses reported from the morphometric descriptors; they do not reproduce the upstream image-acquisition or segmentation stages.

## Data Availability Statement — after an intentional public repository release

Use this version only after the repository is actually accessible to readers and the four release-intended frozen CSV files and release-safe notebooks have passed the strict repository checks.

> **Data Availability Statement:** The Dry Bean dataset used in this study is publicly available from the UCI Machine Learning Repository (Koklu and Ozkan, 2020; https://doi.org/10.24432/C50S4B). The derived 9,200-record INIAP Rice morphometric feature table used in the present analysis, prespecified leakage-safe train/calibration/test split assignments, feature-level analysis notebooks, machine-readable numerical outputs, and SHA-256 integrity manifests are available in the associated project repository. Original INIAP Rice grain images, segmentation masks, raw image-acquisition assets, and other unreleased visual materials are not included because they form part of an ongoing doctoral research programme. The released resources reproduce the feature-level statistical and machine-learning analyses reported in the manuscript but do not reproduce the upstream image-acquisition or segmentation stages.

Do not insert the repository URL into the public-release wording until access has actually been enabled.

## Supplementary Materials — working manuscript wording

> **Supplementary Materials:** Machine-readable supplementary materials accompanying this study include source-reconciliation records; exact frozen model metadata; bootstrap uncertainty intervals for the primary performance metrics; probability-calibration audits; classwise performance metrics and confusion matrices; corrected representation audits and representation-level performance results; exact McNemar comparisons; practical-equivalence analyses for INIAP Rice; selective-classification results; controlled permutation-importance analyses; image-space scale-sensitivity analyses; leakage-sensitivity audits; computational timing; source-validation summaries; and numerical claim/integrity manifests. Additional full selective-classification and conformal-prediction operating-point tables are retained in the project archive and may be included in the final journal supplementary package as required.

## Repository citation wording

Until the associated article has final bibliographic metadata, cite Dry Bean to its original UCI source and associated paper. Do not assign an invented DOI to the INIAP Rice morphometric dataset or to this repository.

After article acceptance/publication, update `CITATION.cff`, `DATA_CITATION.md`, and this document with the final manuscript DOI and any intentionally assigned permanent repository/data identifier.

## Mandatory pre-release checks

Before changing repository visibility or inserting a public GitHub link into the manuscript, run:

```bash
make release-check
```

The release gate must confirm:

1. no prohibited original INIAP Rice visual assets are inside the repository;
2. release notebooks are output-stripped and contain no flagged raw-image loading calls;
3. both frozen morphometric CSVs and both full split-manifest CSVs are present;
4. SHA-256, byte size, row count, and column count match the frozen manifests.
