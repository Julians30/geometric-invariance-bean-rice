# Manuscript supplementary-label crosswalk — AgriEngineering (MDPI), 2026

**Associated manuscript:** *Geometric Invariance and Representation Sufficiency in Morphometric Bean and Rice Classification*.

The labels printed in the manuscript (S1a, S1b, S4b, S4c, S6a, S6b, S9c, etc.) differ from the internal machine-readable filenames retained from the frozen analysis. This is intentional: **internal file numbers must never be used as manuscript table numbers without the mapping below**.

The original supplementary evidence mapping is `tables/supplementary/manuscript_label_crosswalk.csv`. The mapped **original** files listed here are present in the public repository; the new reviewer-round supplements are explicitly documented below.

| Manuscript label | Purpose | Published evidence |
|---|---|---|
| S1a | Dataset provenance and availability | `tables/manuscript_supplementary/Table_S1a_data_provenance_availability.csv`; `data/dataset_provenance.csv`; `data/data_dictionary.csv` |
| S1b | Analytical source reconciliation | `tables/supplementary/Table_S1_source_reconciliation.csv` |
| S2 | Frozen selected-model metadata | `tables/supplementary/Table_S2_exact_model_metadata.csv` |
| S3 | Bootstrap uncertainty for primary metrics | `tables/supplementary/Table_S3_primary_metric_bootstrap_intervals.csv` |
| S4b | Absolute metrics for all representations | `tables/supplementary/Table_S8_all_representation_metrics.csv` |
| S4c | Holm-adjusted paired representation comparisons | `tables/supplementary/Table_S9_all_paired_representation_contrasts.csv` |
| S5 | Exact McNemar comparisons | `tables/supplementary/Table_S10_exact_McNemar_results.csv` |
| S6a | Dry Bean R1 vs R4-C practical equivalence | `tables/manuscript_supplementary/Table_S6a_dry_bean_equivalence.csv` |
| S6b | Five INIAP Rice equivalence comparisons | `tables/supplementary/Table_S11_rice_equivalence_results.csv` |
| S7 | Calibration diagnostics | `tables/supplementary/Table_S5_calibration_audit.csv` |
| S8 | Classwise performance and confusion evidence | `tables/supplementary/Table_S6_classwise_metrics.csv`; `Table_S_confusion_matrix_*.csv` under the same folder |
| S9 | Selective-classification operating-point uncertainty | `tables/supplementary/Table_S13_selective_operating_point_intervals.csv` |
| S9c | Selective classwise coverage at 90% target | `tables/supplementary/Table_S14_selective_classwise_90pct.csv` |
| S10 | Conformal LAC, RAPS, Mondrian, sensitivity and intervals | `tables/supplementary/Table_S15_all_conformal_global_results.csv` through `Table_S19_conformal_paired_comparisons.csv` |
| S11 | Complete controlled R1 feature-block importance | `tables/supplementary/Table_S20_controlled_R1_importance.csv` |
| S12 | Scale-perturbation sensitivity grid | `tables/supplementary/Table_S21_complete_R1_scale_sensitivity.csv` |
| S13 | Duplicate-leakage audits | `tables/supplementary/Table_S22_naive_row_split_audit.csv`; `Table_S23_fixed_test_duplicate_contamination.csv` |
| S14 | Timing, source validation, analysis seeds | `tables/supplementary/Table_S24_notebook12_computational_timing.csv`; `Table_S25_source_validation_summary.csv`; `tables/manuscript_supplementary/Table_S14_analysis_seeds.csv` |

## Numerical source precedence

- Notebook 05: primary frozen predictions, probability calibration, and classwise performance.
- Notebook 07: selective classification using exact frozen champions.
- Notebook 08 v2: canonical multiclass APS conformal analysis.
- Notebook 12 v2: confirmatory representation and practical-equivalence comparisons, controlled feature-block importance, scale and leakage audits.
- Notebook 13B: cross-source reconciliation.
- Notebook 14: final sensitivity/diagnostic analyses.
- Notebook 15: publication-quality figure regeneration only; no replacement of the frozen inferential estimates.

Do not rename the frozen CSV assets merely to make their internal numbering match the manuscript. Machine-readable evidence and manuscript-facing display tables must preserve their original scientific results.

## Release boundary

Original INIAP Rice grain images, segmentation masks, and other unreleased doctoral research assets remain outside this repository. Only the feature-level numerical data, analyses, and reproducibility outputs are provided. No repository DOI is claimed.

## Reviewer-driven supplementary extension — October 2026

The author's final revised text describes **Tables S18–S28 and Figures S7–S10** as a reviewer-driven extension, alongside the original Tables S1a–S17 and Figures S1–S6. The public [reviewer-round archive](../reviewer_round_2026_10/README.md) now includes 26 original numerical CSV exports from NB16–NB18 and cleaned source notebooks. The extension covers year-level provenance, aligned classwise outcomes, independent Cammeo–Osmancik reference replication, harmonized R3-5/R4-5 representations, group-aware inference, independent calibration roles, classwise workload and retrospective precision.

**Scope of this crosswalk:** the numeric CSV exports are public, but no exact one-to-one mapping from each print-formatted S18–S28 table or S7–S10 figure to a file in this repository has been independently checked against the submitted Supplementary Materials package. Do not infer such a mapping from the internal CSV names. Original S1a–S17 mapping is retained, and a dedicated label-level extension should be added only after verifying the finalized supplemental file.

Source image files and acquisition/segmentation code remain outside this feature-table reproducibility release.
