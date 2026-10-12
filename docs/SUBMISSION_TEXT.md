# Submission-ready repository wording — Agriculture (MDPI)

**Associated manuscript:** *Geometric Invariance and Representation Sufficiency in Morphometric Bean and Rice Classification*.

The repository is publicly accessible at https://github.com/Julians30/geometric-invariance-bean-rice. Do not use historical statements suggesting it is still private or that the four frozen CSV files have not yet been uploaded.

## Recommended Data Availability Statement

> The Dry Bean dataset is publicly available from the UCI Machine Learning Repository (DOI: 10.24432/C50S4B). The 9,200-record INIAP Rice morphometric feature table, frozen training/calibration/test assignments, feature-level analysis notebooks, numerical outputs, supplementary tables and SHA-256 integrity manifests are publicly available at https://github.com/Julians30/geometric-invariance-bean-rice. The deposit supports reproducibility of the reported morphometric-descriptor analyses. Original INIAP Rice grain images, segmentation masks, and raw image-acquisition assets are outside the scope of this repository and are not redistributed.

## Supplementary Materials — scope

The supplementary evidence includes provenance records; frozen-model metadata; bootstrap uncertainty for primary metrics; calibration audits; classwise metrics and confusion matrices; representation and practical-equivalence analyses; exact McNemar comparisons; selective-classification and conformal results; feature-block importance; scale and duplicate-leakage sensitivity; and documented analysis seeds and timing. Manuscript labels such as S1a, S4c and S9c are mapped to their source files in `tables/supplementary/manuscript_label_crosswalk.csv`. Internal asset numbers are not equivalent to manuscript table numbers.

## Source and rights boundaries

Dry Bean is a third-party public benchmark attributed to Koklu and Ozkan. The INIAP Rice release is a **numerical feature table**; it does not include original doctoral-project image assets. Code/documentation and author-generated data reuse rights must be declared separately, without applying the Dry Bean license to other files by default.

No article DOI or repository DOI should be invented. Update `CITATION.cff` and `DATA_CITATION.md` only when actual publication identifiers become available.

## Checks on the public repository

```bash
python scripts/audit_release_scope.py
python scripts/audit_notebooks.py
python scripts/audit_manuscript_crosswalk.py --strict
python scripts/verify_integrity.py --strict
```

Confirm that GitHub Actions is passing after the notebook 14/15 output-cleanup commits, and check exact correspondence to the final *Agriculture* submission package.
