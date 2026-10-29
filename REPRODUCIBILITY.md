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

## Review-round sensitivity analyses (2026)

The original seed 20260803 splits and test predictions are retained. The additional reviewer analyses and source notebooks are linked in [reviewer_round_2026_10/README.md](reviewer_round_2026_10/README.md). NB16 and NB17 provide group-aware inference and a **separate** duplicate-group-disjoint 40/30/30 calibration sensitivity: temperature estimation, selective threshold, conformal quantiles. NB17B audits disjoint calibration/test records and groups. NB18 adds the same five invariants—aspect ratio, extent, solidity, circularity, ellipse fill—to both crops (R3-5), and separately adds log(pixel area) (R4-5). These are reviewer-driven exploratory checks, not retroactive model selection or new prespecified tests.

Do not interchange the original Dry Bean R1 champion macro-F1 (0.936605) with the aligned R1 refit (0.935440), which used a distinct probability-estimation seed. Rice's original selected R4-NR champion has macro-F1 0.981165; the aligned native R1 reference has macro-F1 0.977587. The primary numerical margin ±0.01 and exploratory ±0.005 sensitivity are distinct from externally validated operating-cost thresholds.
