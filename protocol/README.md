# Frozen analytical protocol

`frozen_split_and_modeling_protocol_v1.json` records the prespecified split, model-selection, evaluation, multiplicity, and restriction rules used before final test reporting.

## Important temporal interpretation

The JSON preserves the **original frozen protocol terminology**. Later reviewer-driven work in Notebook 12 introduced corrected/expanded representation definitions for specific confirmatory analyses. Those later definitions do not retroactively alter the original split or model-selection protocol.

For the final manuscript interpretation:

- use `docs/MANUSCRIPT_LABEL_MAPPING.md` for dataset-specific scientific representation labels;
- use `tables/supplementary/Table_S1_source_reconciliation.csv` for the authority hierarchy between Notebook 05, 07, 08 v2, and 12 v2;
- use `manifests/final_notebook13B_validation.csv` for final reconciliation checks.

## Frozen restrictions retained throughout the study

- no conversion from image-space pixels to physical units;
- no claim of real camera-domain validation;
- no test-set-guided feature, representation, model, hyperparameter, threshold, or calibration selection;
- exact duplicate groups must remain within one partition.

## Scope boundary

This protocol concerns feature-level numerical analyses only. It does not define a public release of original INIAP Rice images, segmentation masks, or raw acquisition materials.
