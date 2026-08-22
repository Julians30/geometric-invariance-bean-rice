# Manuscript-to-repository asset crosswalk

This document maps the principal analytical claims and manuscript components to the repository files that support them. It is intended to prevent source drift between the frozen Notebook 05 results, the later confirmatory Notebook 12 reanalysis, and the final Notebook 13B reconciliation.

## Methods and data provenance

| Manuscript component | Repository support |
|---|---|
| Dataset provenance and rights | `DATA_RIGHTS.md`, `data/THIRD_PARTY_ATTRIBUTION.md`, `data/INIAP_RICE_SCOPE.md` |
| Morphometric variable definitions | `data/data_dictionary.csv` |
| Frozen file hashes | `manifests/frozen_file_manifest.csv` |
| Release boundary | `manifests/release_scope.csv`, `scripts/audit_release_scope.py` |
| Frozen split design | `REPRODUCIBILITY.md`, `splits/README.md`, `splits/Table_split_summary.csv`, `splits/Table_split_class_distribution.csv` |
| Notebook authority hierarchy | `notebooks/INDEX.md`, `tables/supplementary/Table_S1_source_reconciliation.csv` |
| Internal/manuscript representation labels | `docs/MANUSCRIPT_LABEL_MAPPING.md` |

## Main manuscript tables

| Main table | Repository asset | Authoritative analytical source |
|---|---|---|
| Table 1 — frozen models and provenance | `tables/main/Table_1_frozen_models_and_provenance.csv` | Notebook 05, reconciled by Notebook 13B |
| Table 2 — frozen test performance | `tables/main/Table_2_exact_frozen_test_performance.csv` | exact frozen Notebook 05 predictions |
| Table 3 — corrected representation contrasts | `tables/main/Table_3_corrected_representation_contrasts.csv` | Notebook 12 v2 confirmatory reanalysis |
| Table 4 — selective classification | `tables/main/Table_4_original_selective_classification.csv` | Notebook 07 using exact frozen Notebook 05 champions |
| Table 5 — canonical APS conformal prediction | `tables/main/Table_5_original_canonical_APS.csv` | Notebook 08 v2 using exact frozen Notebook 05 champions |
| Table 6 — controlled R1 block importance | `tables/main/Table_6_controlled_R1_block_importance.csv` | Notebook 12 v2 |
| Table 7 — controlled R1 scale sensitivity | `tables/main/Table_7_controlled_R1_scale_sensitivity.csv` | Notebook 12 v2 |

## Primary frozen results

The authoritative primary test metrics are those stored in `tables/main/Table_2_exact_frozen_test_performance.csv`:

- Dry Bean: accuracy 0.923303; macro-F1 0.936605; MCC 0.907402.
- INIAP Rice: accuracy 0.982609; macro-F1 0.981165; MCC 0.973128.

Later Notebook 12 refits are **not** substitutes for these frozen primary predictions.

## Key supplementary audit assets

| Analytical question | Repository asset |
|---|---|
| Did recomputation reproduce the exact Notebook 05 metrics? | `tables/supplementary/Table_S4_primary_metric_reconciliation.csv` |
| What were the exact frozen model metadata and features? | `tables/supplementary/Table_S2_exact_model_metadata.csv` |
| What are the bootstrap uncertainty intervals for primary metrics? | `tables/supplementary/Table_S3_primary_metric_bootstrap_intervals.csv` |
| What is the probability-calibration audit? | `tables/supplementary/Table_S5_calibration_audit.csv` |
| How did each class perform? | `tables/supplementary/Table_S6_classwise_metrics.csv` |
| What features belong to each corrected representation? | `tables/supplementary/Table_S7_complete_representation_audit.csv` |
| How did all evaluated representations perform? | `tables/supplementary/Table_S8_all_representation_metrics.csv` |
| Are paired classification differences significant? | `tables/supplementary/Table_S10_exact_McNemar_results.csv` |
| Are the rice representations practically equivalent within ±0.01 macro-F1? | `tables/supplementary/Table_S11_rice_equivalence_results.csv` |
| How does 90% selective classification behave by class? | `tables/supplementary/Table_S14_selective_classwise_90pct.csv` |
| How strong are scale-dependent and shape blocks under controlled permutation? | `tables/supplementary/Table_S20_controlled_R1_importance.csv` |
| How sensitive is R1 to systematic image-space scale perturbation? | `tables/supplementary/Table_S21_complete_R1_scale_sensitivity.csv` |
| What happens under naive row-level splitting? | `tables/supplementary/Table_S22_naive_row_split_audit.csv` |
| What is the fixed-test duplicate-contamination audit? | `tables/supplementary/Table_S23_fixed_test_duplicate_contamination.csv` |
| What was Notebook 12 computational timing? | `tables/supplementary/Table_S24_notebook12_computational_timing.csv` |
| Did all final source-validation checks pass? | `tables/supplementary/Table_S25_source_validation_summary.csv` |
| What are the class-level confusion matrices? | `tables/supplementary/Table_S_confusion_matrix_dry_bean.csv`, `tables/supplementary/Table_S_confusion_matrix_iniap_rice.csv` |

## Numerical claim control

`manifests/numerical_claim_register.csv` records the high-value manuscript claims and their authoritative sources. `manifests/final_notebook13B_validation.csv` records the final reconciliation checks.

## Data-release boundary

The crosswalk applies only to feature-level numerical analyses. Original INIAP Rice grain images, segmentation masks, raw acquisition assets, and unreleased visual material from the doctoral research programme are outside the repository and are not required to reproduce the reported analyses from the morphometric feature table.
