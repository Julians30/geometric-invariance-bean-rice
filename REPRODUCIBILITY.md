# Reproducibility protocol

This repository reproduces the **feature-level analytical workflow** reported in the manuscript. It does not reproduce the original INIAP Rice image-acquisition or segmentation stages.

## Frozen analytical design

- Partition seed: `20260803`
- Approximate allocation: 60% training, 20% calibration, 20% final test
- Dry Bean: exact duplicate rows were grouped before partitioning so that duplicate groups could not cross partitions.
- INIAP Rice: no exact duplicate rows were found in the frozen audit.
- Model and hyperparameter selection were restricted to training data.
- Calibration data were reserved for probability calibration, certainty-threshold selection, and conformal quantiles as applicable.
- Final test data were held untouched for the prespecified evaluation.

## Frozen partition sizes

| Dataset | Train | Calibration | Test | Total |
|---|---:|---:|---:|---:|
| Dry Bean | 8,161 | 2,725 | 2,725 | 13,611 |
| INIAP Rice | 5,520 | 1,840 | 1,840 | 9,200 |

## Primary frozen models

| Dataset | Internal frozen representation | Model | Temperature |
|---|---|---|---:|
| Dry Bean | `R1_full_native` | RBF-SVM | 0.9803716562 |
| INIAP Rice | `R4_hybrid_log_area` | RBF-SVM | 0.9312710154 |

The exact frozen-model provenance is stored in `tables/main/Table_1_frozen_models_and_provenance.csv`.

## Evaluation layers

The analytical pipeline includes:

1. data audit and duplicate grouping;
2. morphometric representation construction;
3. frozen train/calibration/test partitioning;
4. training-only model selection;
5. final model fitting and probability calibration;
6. untouched-test evaluation;
7. paired bootstrap inference and exact McNemar tests;
8. equivalence assessment using a fixed ±0.01 macro-F1 margin;
9. selective classification;
10. conformal prediction;
11. controlled feature-block perturbation;
12. controlled image-space scale sensitivity;
13. final numerical reconciliation and integrity checks.

## Measurement domain

All INIAP Rice measurements are interpreted in image space. Linear dimensions are in pixels, area-related descriptors are in squared pixels, and ECCENTRICITY/EXTENT and engineered ratios are dimensionless as applicable. No pixel-to-millimetre calibration was performed, so physical-size transfer across cameras or acquisition systems is not claimed.

## Integrity

Frozen analytical files should not be edited after release. SHA-256 values are recorded in `manifests/frozen_file_manifest.csv`, and final reconciliation checks are recorded in `manifests/final_notebook13B_validation.csv`.
