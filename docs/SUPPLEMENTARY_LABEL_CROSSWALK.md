# Manuscript supplementary-label crosswalk

The final manuscript uses **display labels** such as `S1a`, `S1b`, `S4b`, `S4c`, `S6a`, `S6b`, `S9c`, etc. The final Notebook 13B project archive, however, retains a separate sequence of **internal machine-readable filenames** (`Table_S1_...`, `Table_S10_...`, and so forth). These two numbering systems must not be assumed to be identical.

This crosswalk preserves the distinction and maps each manuscript-facing supplementary label to the authoritative machine-readable evidence in the repository/project archive.

| Manuscript display label | Manuscript purpose | Repository / project evidence | Status |
|---|---|---|---|
| **S1a** | Field-by-field dataset provenance and availability | `data/dataset_provenance.csv`, `data/data_dictionary.csv`, `DATA_RIGHTS.md`, `data/THIRD_PARTY_ATTRIBUTION.md`, `data/INIAP_RICE_SCOPE.md` | documented; manuscript-facing compact table to be generated from these sources |
| **S1b** | Analytical source reconciliation | `tables/supplementary/Table_S1_source_reconciliation.csv` | available |
| **S2** | Exact selected-model metadata | `tables/supplementary/Table_S2_exact_model_metadata.csv` | available |
| **S3** | Duplicate-group bootstrap uncertainty intervals for primary metrics | `tables/supplementary/Table_S3_primary_metric_bootstrap_intervals.csv` | available |
| **S4b** | Complete absolute confirmatory metrics for all representations | `tables/supplementary/Table_S8_all_representation_metrics.csv` | available |
| **S4c** | Complete dataset-specific Holm families for paired representation contrasts | final Notebook 13B asset `Table_S9_all_paired_representation_contrasts.csv` | pending GitHub transfer |
| **S5** | Exact McNemar comparisons | `tables/supplementary/Table_S10_exact_McNemar_results.csv` | available |
| **S6a** | Dry Bean practical-equivalence interpretation for R1 vs R4-C | R1–R4-C paired bootstrap contrast in `tables/main/Table_3_corrected_representation_contrasts.csv`; the 95% interval lies fully inside ±0.01 | supported; manuscript-facing compact table to be generated |
| **S6b** | Five prespecified INIAP Rice equivalence contrasts | `tables/supplementary/Table_S11_rice_equivalence_results.csv` | available |
| **S7** | Before/after probability-calibration diagnostics | `tables/supplementary/Table_S5_calibration_audit.csv` | available |
| **S8** | Complete classwise performance | `tables/supplementary/Table_S6_classwise_metrics.csv`; confusion-matrix values in `Table_S_confusion_matrix_dry_bean.csv` and `Table_S_confusion_matrix_iniap_rice.csv` support Supplementary Figures S1–S2 | available |
| **S9 / S9c** | Selective-classification uncertainty and classwise coverage at the calibration-selected operating point | final assets `Table_S13_selective_operating_point_intervals.csv` and `tables/supplementary/Table_S14_selective_classwise_90pct.csv`; complete operating-point grid in `Table_S12_all_selective_operating_points.csv` | classwise table available; interval/grid files pending GitHub transfer |
| **S10** | LAC, RAPS, Mondrian and deterministic conformal-sensitivity results | final conformal asset family `Table_S15`–`Table_S19` (global, classwise, quantiles, intervals and paired comparisons) | pending GitHub transfer |
| **S11** | Complete controlled R1 block-permutation results | `tables/supplementary/Table_S20_controlled_R1_importance.csv` | available |
| **S12** | Complete image-space scale-perturbation grid | `tables/supplementary/Table_S21_complete_R1_scale_sensitivity.csv` | available |
| **S13** | Complete duplicate-leakage audits | `tables/supplementary/Table_S22_naive_row_split_audit.csv` and `Table_S23_fixed_test_duplicate_contamination.csv` | available |
| **S14** | Full computational timing, source validation and analysis-seed documentation | `tables/supplementary/Table_S24_notebook12_computational_timing.csv`, `Table_S25_source_validation_summary.csv`, protocol/notebook documentation, and manuscript seed record | timing/validation available; compact seed table to be added |

## Important interpretation rule

An internal filename number is **not** a manuscript supplementary-table number. For example:

- internal `Table_S10_exact_McNemar_results.csv` supports manuscript **Supplementary Table S5**;
- internal `Table_S20_controlled_R1_importance.csv` supports manuscript **Supplementary Table S11**;
- internal `Table_S21_complete_R1_scale_sensitivity.csv` supports manuscript **Supplementary Table S12**.

The repository keeps the internal filenames unchanged because they are frozen analytical assets. Manuscript-facing tables can be assembled in a separate `tables/manuscript_supplementary/` layer without renaming or overwriting the frozen evidence.

## Source-control principle

Where the manuscript-facing table is assembled from more than one frozen analytical source, the assembly must be deterministic and must not change any reported numerical result. The authoritative source hierarchy remains:

- Notebook 05 — primary frozen predictions;
- Notebook 07 — selective classification;
- Notebook 08 v2 — canonical conformal prediction;
- Notebook 12 v2 — confirmatory representation, equivalence, importance, scale and leakage analyses;
- Notebook 13B — final reconciliation.

## Release boundary

This crosswalk concerns numerical, feature-level supplementary material only. Original INIAP Rice grain images, segmentation masks, raw acquisition assets and other unreleased visual material from the doctoral research programme remain outside the repository.
