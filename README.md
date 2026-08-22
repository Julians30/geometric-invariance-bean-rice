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

The copy used in this project is included only to preserve the exact frozen analytical input and split assignments used in the manuscript. Its inclusion does **not** imply ownership by the manuscript authors.

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

The INIAP Rice contribution released with this study is limited to the numerical morphometric table required to reproduce the feature-level analyses reported in the manuscript.

## Included materials

- Frozen morphometric feature tables used in the analyses.
- Prespecified train/calibration/test split assignments.
- Analysis notebooks and reproducible code.
- Numerical outputs used to support manuscript claims.
- Tables and figure-generation outputs derived from the morphometric data.
- SHA-256 integrity manifests and validation records.

## Not included

- Original INIAP Rice grain images.
- Segmentation masks.
- Image-acquisition files or protocols containing unreleased visual material.
- Other raw visual assets from the doctoral research project.

## Repository structure

```text
geometric-invariance-bean-rice/
├── README.md
├── data/
├── splits/
├── notebooks/
├── results/
├── tables/
├── protocol/
└── manifests/
```

## Reproducibility boundary

The materials in this repository are intended to reproduce the statistical and machine-learning analyses reported from the extracted morphometric features. They do **not** reproduce the original INIAP Rice image-acquisition or segmentation stages.

## Repository status

This repository is currently **private** while the manuscript is under preparation. Public release, if applicable, will follow the journal’s data-sharing requirements and the authors’ publication plan.
