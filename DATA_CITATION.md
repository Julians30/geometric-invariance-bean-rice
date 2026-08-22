# Data citation guidance

This project uses two datasets with different provenance. Citation and attribution must preserve that distinction.

## Dry Bean

The Dry Bean Dataset is a **third-party public benchmark** and must be cited to its original source rather than attributed to the manuscript authors.

Recommended dataset citation:

> Koklu, M.; Ozkan, I.A. (2020). *Dry Bean* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C50S4B

Associated publication:

> Koklu, M.; Ozkan, I.A. Multiclass classification of dry beans using computer vision and machine learning techniques. *Computers and Electronics in Agriculture* 2020, 174, 105507. https://doi.org/10.1016/j.compag.2020.105507

The Dry Bean source reports a CC BY 4.0 license. Redistribution of the frozen analytical copy in this repository does not imply ownership by the manuscript authors.

## INIAP Rice

The 9,200-record INIAP Rice morphometric dataset is **original research data associated with this study**. The article repository is limited to the derived morphometric feature table and related feature-level analytical materials.

Original grain images, segmentation masks, and raw acquisition assets are not released with the article because they form part of an ongoing doctoral research programme.

A permanent public data citation or DOI for the INIAP Rice morphometric table should be added here only after the authors decide the final publication/reuse mechanism. No identifier is invented during private manuscript preparation.

## Associated manuscript

When the article receives its final bibliographic metadata and DOI, `CITATION.cff` and this file should be updated so that users can cite the manuscript separately from the third-party Dry Bean dataset.
