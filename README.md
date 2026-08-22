# Testing Geometric Invariance in Leakage-Safe Bean and Rice Classification

Private reproducibility repository associated with the manuscript **“Testing Geometric Invariance in Leakage-Safe Bean and Rice Classification.”**

## Repository scope

This repository is restricted to the **feature-level analytical workflow** used in the manuscript. It is intended to support reproducibility of the statistical and machine-learning analyses performed from extracted morphometric descriptors.

### Included materials

- Frozen morphometric feature tables used in the analyses.
- Prespecified train/calibration/test split assignments.
- Analysis notebooks and reproducible code.
- Numerical outputs used to support manuscript claims.
- Tables and figure-generation outputs derived from the morphometric data.
- SHA-256 integrity manifests and validation records.

### Not included

**Original INIAP Rice grain images, segmentation masks, and image-acquisition materials are not included in this repository.** These materials form part of an ongoing doctoral research project and are outside the reproducibility scope of this manuscript.

The INIAP Rice data released for this study consist only of derived morphometric measurements expressed in image-space pixels, squared pixels, or dimensionless shape descriptors, as applicable.

## Datasets

### Dry Bean

- 13,611 records.
- Seven classes.
- Public benchmark source: UCI Machine Learning Repository.
- Analyses in this repository use the frozen feature-level dataset generated for the study.

### INIAP Rice

- 9,200 records.
- Three varieties: INIAP-11, INIAP-12, and INIAP-20.
- Feature-level morphometric table only.
- Measurements include pixel-based geometric descriptors and dimensionless shape variables.
- No original images or segmentation masks are distributed.

## Planned repository structure

```text
geometric-invariance-bean-rice/
├── README.md
├── data/
├── splits/
├── notebooks/
├── results/
├── tables/
└── manifests/
```

## Reproducibility boundary

The materials in this repository are sufficient to reproduce the statistical and machine-learning analyses reported from the extracted morphometric features. They do **not** reproduce the original image-acquisition or segmentation stages.

## Repository status

This repository is currently **private** while the manuscript is under preparation. Public release, if applicable, will follow the journal’s data-sharing requirements and the authors’ publication plan.
