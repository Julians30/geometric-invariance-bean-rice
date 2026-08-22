# Supplementary tables

This folder contains **reconciled machine-readable supplementary outputs** from the final Notebook 13B manuscript-asset reconciliation.

## Source hierarchy

The manuscript does not use a single notebook as the authority for every analysis layer. The authoritative sources are documented in `Table_S1_source_reconciliation.csv`:

- **Notebook 05:** primary frozen performance, calibration, confusion matrices, and classwise metrics.
- **Notebook 07:** selective classification using the exact frozen Notebook 05 champions.
- **Notebook 08 v2:** canonical conformal prediction using the exact frozen Notebook 05 champions.
- **Notebook 12 v2:** confirmatory reviewer-driven analyses for corrected representations, exact McNemar tests, equivalence, controlled importance, scale sensitivity, and leakage audits.

Notebook 12 refitted predictions are **not substitutes for the primary frozen Notebook 05 predictions**. This separation is intentional and is preserved in the manuscript claim register.

## Files currently included

- `Table_S1_source_reconciliation.csv`
- `Table_S2_exact_model_metadata.csv`
- `Table_S3_primary_metric_bootstrap_intervals.csv`
- `Table_S5_calibration_audit.csv`
- `Table_S6_classwise_metrics.csv`
- `Table_S7_complete_representation_audit.csv`
- `Table_S10_exact_McNemar_results.csv`
- `Table_S11_rice_equivalence_results.csv`
- `Table_S22_naive_row_split_audit.csv`
- `Table_S23_fixed_test_duplicate_contamination.csv`
- `Table_S25_source_validation_summary.csv`
- `Table_S_confusion_matrix_dry_bean.csv`
- `Table_S_confusion_matrix_iniap_rice.csv`

Additional large supplementary tables may be added later if needed for the journal submission package. The CSV files are preferred here because they are machine-readable and directly auditable.

## Representation-label note

Some frozen/reanalysis files retain historical internal names such as `R3_complete_invariant` for INIAP Rice. The manuscript scientific labels are dataset-specific. See `../../docs/MANUSCRIPT_LABEL_MAPPING.md` before interpreting those internal labels.
