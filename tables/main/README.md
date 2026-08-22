# Main manuscript tables — reconciled machine-readable outputs

These CSV files are the **Notebook 13B reconciled manuscript assets** and should be preferred over earlier non-reconciled exports.

## Included tables

1. `Table_1_frozen_models_and_provenance.csv` — exact frozen champions and provenance.
2. `Table_2_exact_frozen_test_performance.csv` — authoritative frozen-test performance from the exact Notebook 05 predictions.
3. `Table_3_corrected_representation_contrasts.csv` — corrected representation contrasts from the confirmatory reanalysis.
4. `Table_4_original_selective_classification.csv` — selective classification from the exact frozen champions.
5. `Table_5_original_canonical_APS.csv` — canonical APS conformal prediction from the exact frozen champions.
6. `Table_6_controlled_R1_block_importance.csv` — controlled same-model block-importance analysis on R1.
7. `Table_7_controlled_R1_scale_sensitivity.csv` — controlled image-space scale perturbation analysis.

## Authority rule

Do not replace the primary performance values in Table 2 with metrics from later refitted Notebook 12 models. Notebook 12 is a confirmatory reviewer-driven reanalysis for specific inferential and sensitivity layers; the frozen primary champions and their primary predictions remain those from Notebook 05.

## Measurement interpretation

Scale perturbations are transformations in **image space**. They are not calibrated changes in physical grain dimensions because no pixel-to-millimetre calibration was performed.

## Internal representation labels

For INIAP Rice, some frozen/reanalysis filenames retain historical `complete` terminology. Use `../../docs/MANUSCRIPT_LABEL_MAPPING.md` when mapping these internal names to manuscript labels R3-NR and R4-NR.
