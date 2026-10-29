# Geometric Invariance and Representation Sufficiency in Morphometric Bean and Rice Classification

[![Repository scope audit](https://github.com/Julians30/geometric-invariance-bean-rice/actions/workflows/repository-audit.yml/badge.svg?branch=main)](https://github.com/Julians30/geometric-invariance-bean-rice/actions/workflows/repository-audit.yml) [![Code License: MIT](https://img.shields.io/badge/Code%20License-MIT-blue.svg)](LICENSE) ![Python](https://img.shields.io/badge/Language-Python-3776AB?logo=python&logoColor=white) ![Status](https://img.shields.io/badge/Status-Under%20review%20%C2%B7%20AgriEngineering-2E6DA4)

Public reproducibility repository associated with the manuscript **“Geometric Invariance and Representation Sufficiency in Morphometric Bean and Rice Classification.”**

**Editorial status (28 October 2026):** manuscript **under review** at *AgriEngineering* (MDPI); section: *Computer Applications and Artificial Intelligence in Agriculture*; Special Issue: *Deep Detection, Machine Learning and Computer Applications in Agriculture*. It is not yet accepted or published. Reproducibility scope: morphometric feature-table analyses only, not upstream images or segmentation.

## Code license and data rights

**Software license: MIT.** The authors' original Python scripts, source notebooks, and repository automation code are available under the [MIT License](LICENSE). See [LICENSE_SCOPE.md](LICENSE_SCOPE.md) for exactly what it covers.

**Datasets are separate from the software license.** Dry Bean retains its original **CC BY 4.0** terms and attribution to Koklu and Ozkan. The author-generated INIAP Rice 9,200-record morphometric table is publicly accessible for research reproducibility, but **no separate public reuse license is granted by the MIT license**. The original grain images and acquisition/segmentation assets are not shared. Consult [DATA_RIGHTS.md](DATA_RIGHTS.md) before reusing any dataset or non-software research asset.

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

Notebook 12 provides the aligned representation reanalysis, Notebook 13B reconciles numerical sources, Notebook 14 adds sensitivity/diagnostics and Notebook 15 regenerates presentation figures. NB16–NB18 provide separate peer-review additions; none replaces the original frozen selected-model results.

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

## October 2026 peer-review evidence (NB16–NB18)

The [reviewer-round evidence archive](reviewer_round_2026_10/README.md) contains **26 additional CSV results** and five cleaned, source-preserving notebooks under [notebooks/reviewer_round_2026_10/](notebooks/reviewer_round_2026_10/). These are additions to—not replacements for—the frozen primary results and existing Notebooks 01–15.

- **NB16:** per-class confusion/F1, duplicate-group-aware inference, independent calibration sensitivity, 2025/2026 provenance audit and Cammeo–Osmancik within-dataset replication.
- **NB17:** class-size profiles, margin/precision sensitivity and LAC/APS/RAPS/Mondrian diagnostics.
- **NB17B:** independent subset and calibration/test-disjointness audit.
- **NB18:** matched R3-5/R4-5 five-variable invariant comparisons and group-paired uncertainty; R4-5 adds exactly one log-area descriptor.

The INIAP Rice source acquisitions occurred on multiple dates in **2025 and 2026**, not one session. The 9,200-row table contains 2,400 records overlapping prior work and 6,800 additional records. No specific acquisition months, lot-disjoint or cross-device validation are claimed. The added [record-level provenance manifest](reviewer_round_2026_10/NB16/NB16_10_manifest_procedencia_usado.csv) is feature-table metadata and is not original imagery.

For numbered paper tables, use the [current manuscript-to-asset crosswalk](docs/MANUSCRIPT_ASSET_CROSSWALK.md). Historical repository-internal Table_1/Table_2 labels **do not** match final manuscript Table 1/Table 2 numbers. The manuscript Figure 1 is a workflow diagram; the legacy file named `figures/main/Figure_1_corrected_representation_performance.png` is a different analytical figure and **must not** be cited as manuscript Figure 1.
