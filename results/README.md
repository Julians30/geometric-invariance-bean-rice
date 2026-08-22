# Results

This directory is reserved for final numerical outputs generated from the frozen morphometric datasets and the prespecified analysis pipeline.

Only outputs that support the manuscript’s reported analyses should be retained here. Intermediate exploratory files that are not used in the manuscript should remain outside the release package.

## Authoritative primary results

The primary frozen-test results come from the **exact frozen Notebook 05 predictions**, as reconciled by Notebook 13B. They must not be replaced by the confirmatory Notebook 12 refits.

| Dataset | Frozen representation | Model | Test n | Accuracy | Macro-F1 | MCC |
|---|---|---|---:|---:|---:|---:|
| Dry Bean | `R1_full_native` | RBF-SVM | 2,725 | 0.923303 | 0.936605 | 0.907402 |
| INIAP Rice | `R4_hybrid_log_area` | RBF-SVM | 1,840 | 0.982609 | 0.981165 | 0.973128 |

Machine-readable values are stored in `../tables/main/Table_2_exact_frozen_test_performance.csv`.

## Important source separation

- Primary performance/calibration/classwise/confusion: Notebook 05.
- Selective classification: Notebook 07.
- Canonical APS conformal prediction: Notebook 08 v2.
- Corrected representation comparisons, exact McNemar, equivalence, controlled importance, scale sensitivity, and leakage audits: Notebook 12 v2.
- Final reconciliation: Notebook 13B.

The formal source map is `../tables/supplementary/Table_S1_source_reconciliation.csv`.

## Dataset boundary

Dry Bean is a public third-party UCI benchmark attributed to Koklu and Ozkan. INIAP Rice is the authors' original 9,200-record morphometric dataset. Only feature-level numerical data and derived analytical outputs are within this repository; original INIAP Rice grain images and segmentation masks are excluded.
