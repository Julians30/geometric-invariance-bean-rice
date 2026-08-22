# Testing Geometric Invariance in Leakage-Safe Bean and Rice Classification

Private reproducibility repository associated with the manuscript **“Testing Geometric Invariance in Leakage-Safe Bean and Rice Classification.”**

## Repository scope

This repository is restricted to the **feature-level analytical workflow** used in the manuscript. It supports reproducibility of the statistical and machine-learning analyses performed from extracted morphometric descriptors.

## Dataset provenance — important distinction

This study combines **two datasets with different provenance and ownership status**. They must not be interpreted as belonging to the same source.

### 1. Dry Bean — public third-party benchmark dataset

The **Dry Bean Dataset is not owned by the authors of this repository**. It is a public benchmark dataset distributed through the **UCI Machine Learning Repository** and attributed to **Murat Koklu and Ilker Ali Ozkan**.

- Dataset: **Dry Bean**
- Creators/source attribution: **Koklu, M. and Ozkan, I.A.**
- Repository: **UCI Machine Learning Repository**
- Records: **13,611**
- Classes: **7**
- Features: **16 morphometric descriptors**
- DOI: **10.24432/C50S4B**
- License: **CC BY 4.0**
- Associated paper: Koklu, M.; Ozkan, I.A. *Multiclass classification of dry beans using computer vision and machine learning techniques*. Computers and Electronics in Agriculture, 2020, 174, 105507. https://doi.org/10.1016/j.compag.2020.105507

The frozen copy used in this project is retained only to preserve the exact analytical input and split assignments used in the manuscript. Its inclusion does **not** imply ownership by the manuscript authors.

### 2. INIAP Rice — original dataset from the authors' research

The **INIAP Rice morphometric dataset is an original dataset generated within the authors' research and is not a public third-party benchmark**.

- Records: **9,200**
- Classes/varieties: **INIAP-11, INIAP-12, and INIAP-20**
- Released material: **derived morphometric feature table only**
- Measurement domain: **image space**
- Linear descriptors: interpreted in **pixels**
- Area-related descriptors: interpreted in **squared pixels**
- Shape descriptors: dimensionless where applicable

**Original INIAP Rice grain images, segmentation masks, image-acquisition materials, and other raw visual assets are not included in this repository.** These materials form part of an ongoing doctoral research project and are outside the reproducibility scope of this manuscript.

The INIAP Rice contribution associated with this study is limited to the numerical morphometric table required to reproduce the feature-level analyses reported in the manuscript.

## Reproducibility package scope

The repository is being assembled to contain:

- Frozen morphometric feature tables used in the analyses.
- Prespecified train/calibration/test split assignments.
- Analysis notebooks and reproducible code required for the feature-level workflow.
- Numerical outputs used to support manuscript claims.
- Machine-readable main and supplementary tables.
- SHA-256 integrity manifests and validation records.
- Automated release-scope and integrity checks.

The current preparation status is tracked in [`STATUS.md`](STATUS.md).

## Authoritative primary frozen results

The primary test metrics come from the exact frozen Notebook 05 predictions and were reconciled by Notebook 13B:

| Dataset | Frozen representation | Test n | Accuracy | Macro-F1 | MCC |
|---|---|---:|---:|---:|---:|
| Dry Bean | `R1_full_native` | 2,725 | 0.923303 | 0.936605 | 0.907402 |
| INIAP Rice | `R4_hybrid_log_area` | 1,840 | 0.982609 | 0.981165 | 0.973128 |

Notebook 12 refits are used only for the reviewer-driven confirmatory analyses defined in the source reconciliation; they do **not** replace these primary frozen results.

## Not included

- Original INIAP Rice grain images.
- Segmentation masks.
- Raw image-acquisition files.
- Unreleased visual assets from the doctoral research project.

## Documentation index

- [`DATA_RIGHTS.md`](DATA_RIGHTS.md) — provenance, ownership, and reuse status.
- [`DATA_AVAILABILITY.md`](DATA_AVAILABILITY.md) — working pre-publication and post-publication data-availability wording.
- [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md) — frozen evaluation design and reproducibility protocol.
- [`docs/MANUSCRIPT_LABEL_MAPPING.md`](docs/MANUSCRIPT_LABEL_MAPPING.md) — mapping between historical internal representation names and the scientific manuscript labels.
- [`notebooks/INDEX.md`](notebooks/INDEX.md) — analytical notebook sequence and authority hierarchy.
- [`environment/README.md`](environment/README.md) — verified execution environment.
- [`tables/main/`](tables/main/) — seven reconciled main machine-readable tables.
- [`tables/supplementary/`](tables/supplementary/) — reconciled supplementary machine-readable outputs.
- [`manifests/`](manifests/) — integrity, validation, release-scope, and numerical-claim records.
- [`scripts/verify_integrity.py`](scripts/verify_integrity.py) — SHA-256, file-size, and CSV-shape verification for frozen analytical data.
- [`scripts/audit_release_scope.py`](scripts/audit_release_scope.py) — guardrail preventing accidental inclusion of prohibited original INIAP visual assets.

## Repository structure

```text
geometric-invariance-bean-rice/
├── README.md
├── STATUS.md
├── CITATION.cff
├── DATA_RIGHTS.md
├── DATA_AVAILABILITY.md
├── REPRODUCIBILITY.md
├── requirements.txt
├── data/
├── splits/
├── notebooks/
├── results/
├── tables/
│   ├── main/
│   └── supplementary/
├── protocol/
├── manifests/
├── docs/
├── environment/
├── scripts/
└── .github/workflows/
```

## Automated safeguards

A GitHub Actions workflow runs the repository-scope audit and integrity checker on pushes and pull requests to `main`. The integrity checker reports the four large frozen analytical files as **pending** until they are transferred; once present, their SHA-256 values, sizes, and CSV shapes are checked against the frozen manifest.

## Reproducibility boundary

The materials in this repository are intended to reproduce the statistical and machine-learning analyses reported from the extracted morphometric features. They do **not** reproduce the original INIAP Rice image-acquisition or segmentation stages.

## Repository status

This repository is currently **private** while the manuscript is under preparation. Public release, if applicable, will follow the journal's data-sharing requirements and the authors' publication plan.
