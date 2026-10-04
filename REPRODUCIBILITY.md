# Reproducibility protocol

This repository reproduces the **feature-level analytical workflow** reported in the manuscript *Geometric Invariance and Representation Sufficiency in Morphometric Bean and Rice Classification*.

## Frozen analytical design

- Partition seed: `20260803`
- Approximate allocation: 60% training, 20% calibration, 20% final test.
- Dry Bean: exact duplicate rows were grouped before partitioning so duplicate groups could not cross partitions.
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

## Evaluation layers

1. data audit and duplicate grouping;
2. morphometric representation construction;
3. frozen train/calibration/test partitioning;
4. training-only model selection;
5. final model fitting and probability calibration;
6. untouched-test evaluation;
7. paired bootstrap inference and exact McNemar tests;
8. equivalence assessment using the primary ±0.01 macro-F1 margin and post hoc ±0.005 sensitivity;
9. selective classification;
10. conformal prediction;
11. controlled feature-block perturbation;
12. controlled morphometric coordinate-scale sensitivity;
13. matched five-variable invariant-basis audit;
14. training-only learning curves;
15. final numerical reconciliation and publication-figure regeneration.

## Measurement domain

INIAP Rice linear dimensions are interpreted in pixels, area-related descriptors in squared pixels, and ratios/shape descriptors as dimensionless where applicable. No physical-unit calibration is claimed. The repository supports reproducibility of the feature-level analyses rather than upstream image-acquisition or segmentation procedures.

## Integrity

Frozen analytical files should not be edited after release. SHA-256 values are recorded in `manifests/frozen_file_manifest.csv`, and reconciliation checks are stored under `manifests/`. Notebook 13B is the cross-source reconciliation authority; Notebook 14 contains final minor-revision analyses; Notebook 15 regenerates final publication figures only.
