# Machine-readable manuscript tables

This directory contains machine-readable tables derived from the frozen feature-level analytical workflow and used to construct, audit, or verify the manuscript.

## Structure

- `main/` — reconciled main manuscript tables from the final Notebook 13B asset package.
- `supplementary/` — selected supplementary tables required to audit model provenance, uncertainty, calibration, representation comparisons, leakage controls, and class-level results.

## Source hierarchy

The authoritative analytical source depends on the analysis layer:

1. **Primary frozen performance, calibration, confusion matrices, and classwise metrics:** exact frozen Notebook 05 predictions.
2. **Selective classification:** Notebook 07 using the exact frozen Notebook 05 champions.
3. **Canonical APS conformal prediction:** Notebook 08 v2 using the exact frozen Notebook 05 champions.
4. **Corrected representation comparisons, exact McNemar tests, equivalence testing, controlled block importance, scale sensitivity, and leakage audits:** Notebook 12 v2 confirmatory reanalysis.
5. **Final manuscript reconciliation and source validation:** Notebook 13B.

See `tables/supplementary/Table_S1_source_reconciliation.csv` and `manifests/final_notebook13B_validation.csv` for the formal source reconciliation.

## Measurement boundary

All INIAP Rice results in these tables are derived from numerical morphometric features. Linear descriptors are interpreted in image-space pixels, area-related descriptors in squared pixels, and shape descriptors as dimensionless where applicable. No physical-unit conversion is assumed.

## Excluded material

No original INIAP Rice grain images, segmentation masks, image-acquisition files, or other raw visual assets belong in this directory or elsewhere in this repository.
