# Geometric Invariance and Representation Sufficiency in Morphometric Bean and Rice Classification

Public reproducibility repository associated with the manuscript **“Geometric Invariance and Representation Sufficiency in Morphometric Bean and Rice Classification.”**

## Repository scope

This repository is restricted to the **feature-level analytical workflow** reported in the manuscript. It supports reproducibility of the statistical and machine-learning analyses performed from tabular morphometric descriptors.

## Dataset provenance

### 1. Dry Bean — public third-party benchmark

The Dry Bean Dataset is a public benchmark distributed through the **UCI Machine Learning Repository** and attributed to **Murat Koklu and Ilker Ali Ozkan**.

- Records: **13,611**
- Classes: **7**
- Features: **16 morphometric descriptors**
- DOI: **10.24432/C50S4B**
- License: **CC BY 4.0**
- Associated paper: Koklu, M.; Ozkan, I.A. *Multiclass classification of dry beans using computer vision and machine learning techniques*. *Computers and Electronics in Agriculture* 2020, 174, 105507. https://doi.org/10.1016/j.compag.2020.105507

The frozen analytical copy is retained only to preserve the exact inputs and split assignments used in the manuscript.

### 2. INIAP Rice — author-generated morphometric dataset

The INIAP Rice analytical table contains:

- **9,200** grain-level records
- Varieties: **INIAP-11, INIAP-12, INIAP-20**
- Released material: the **tabular morphometric feature table** and reproducibility metadata
- Linear descriptors: **pixels**
- Area-related descriptors: **squared pixels**
- Ratios and engineered shape descriptors: dimensionless where applicable

The manuscript and this repository operate on the **tabular morphometric records**. Original visual assets are outside the scope of this feature-level reproducibility package.

## Reproducibility package

The repository contains:

- frozen morphometric feature tables;
- prespecified train/calibration/test split assignments;
- analysis notebooks for the feature-level workflow;
- numerical outputs supporting manuscript claims;
- machine-readable main and supplementary tables;
- SHA-256 integrity manifests and validation records;
- source-reconciliation and release-scope documentation.

## Authoritative primary frozen results

| Dataset | Frozen representation | Test n | Accuracy | Macro-F1 | MCC |
|---|---|---:|---:|---:|---:|
| Dry Bean | `R1_full_native` | 2,725 | 0.923303 | 0.936605 | 0.907402 |
| INIAP Rice | `R4_hybrid_log_area` | 1,840 | 0.982609 | 0.981165 | 0.973128 |

Notebook 12 provides the confirmatory reviewer-driven representation analyses. Notebook 13B reconciles numerical sources. Notebook 14 adds final minor-revision sensitivity and diagnostic analyses, and Notebook 15 regenerates the final publication figures without changing any statistical result.

## Documentation index

- [`STATUS.md`](STATUS.md) — repository preparation and release status.
- [`DATA_RIGHTS.md`](DATA_RIGHTS.md) — provenance and reuse boundaries.
- [`DATA_CITATION.md`](DATA_CITATION.md) — dataset attribution.
- [`DATA_AVAILABILITY.md`](DATA_AVAILABILITY.md) — manuscript-facing availability wording.
- [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md) — frozen analytical design.
- [`notebooks/INDEX.md`](notebooks/INDEX.md) — notebook sequence and authority hierarchy.
- [`docs/MANUSCRIPT_ASSET_CROSSWALK.md`](docs/MANUSCRIPT_ASSET_CROSSWALK.md) — manuscript-to-repository evidence map.
- [`docs/MANUSCRIPT_LABEL_MAPPING.md`](docs/MANUSCRIPT_LABEL_MAPPING.md) — historical-to-manuscript representation labels.
- [`tables/main/`](tables/main/) and [`tables/supplementary/`](tables/supplementary/) — machine-readable tables.
- [`manifests/`](manifests/) — integrity and validation records.
- [`scripts/verify_integrity.py`](scripts/verify_integrity.py) — integrity verification.
- [`scripts/audit_release_scope.py`](scripts/audit_release_scope.py) — repository-scope guardrail.

## Reproducibility boundary

The repository reproduces the **feature-table statistical and machine-learning analyses** reported in the manuscript. It does not claim to reproduce upstream image acquisition or segmentation.

## Repository status

The repository is **public** at https://github.com/Julians30/geometric-invariance-bean-rice. No archival DOI is claimed at this stage.
