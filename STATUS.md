# Repository status — Agriculture (MDPI) submission

**Repository:** https://github.com/Julians30/geometric-invariance-bean-rice
**Visibility:** Public
**Associated manuscript:** *Geometric Invariance and Representation Sufficiency in Morphometric Bean and Rice Classification*.
**Journal:** *Agriculture* (MDPI).

## Published reproducibility assets

- Dry Bean frozen feature-level CSV (13,611 records) and INIAP Rice frozen feature-level CSV (9,200 records).
- Full frozen train/calibration/test split manifests for both datasets.
- Notebooks 01–15, including 13B; public versions have their execution outputs and execution counters cleared.
- Main and supplementary numerical tables, figures, frozen protocol, source-reconciliation evidence, and SHA-256 manifests.
- Documentation of third-party Dry Bean attribution and the restricted feature-level release scope for INIAP Rice.

## Verified scientific results (unchanged)

| Dataset | Accuracy | Macro-F1 | MCC | Source |
|---|---:|---:|---:|---|
| Dry Bean | 0.923303 | 0.936605 | 0.907402 | Frozen Notebook 05, main Table 2 |
| INIAP Rice | 0.982609 | 0.981165 | 0.973128 | Frozen Notebook 05, main Table 2 |

Notebook 12 contains separate confirmatory representation and sensitivity analyses; Notebook 13B reconciles the manuscript evidence, and Notebook 15 regenerates figures without changing statistical results.

## Submission checks

Run these commands on the current public repository checkout:

```bash
python scripts/audit_release_scope.py
python scripts/audit_notebooks.py
python scripts/audit_manuscript_crosswalk.py --strict
python scripts/verify_integrity.py --strict
```

Also confirm that the most recent GitHub Actions audit succeeds. Previous workflow failures on October 4, 2026 were caused by stored outputs/execution counters in notebooks 14 and 15; these were removed without changing their code.

## Outstanding editorial/rights decisions

- Confirm licensing terms for this repository's code and documentation independently of the Dry Bean source license and INIAP Rice data reuse terms.
- Confirm exact consistency of the submitted *Agriculture* manuscript and supplementary material with repository table/figure mappings.
- Update citation metadata after an actual article DOI is assigned; no article or repository DOI is claimed here.

## Scope and limitations

Only feature-level morphometric data and analytical code/results are released. Original INIAP Rice grain images, masks, and acquisition assets are not part of this repository. The deposit does not reproduce the upstream image-acquisition or segmentation stages. Do not assume a license for original INIAP Rice tabular data unless explicitly granted.
