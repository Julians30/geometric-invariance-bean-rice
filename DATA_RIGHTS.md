# Data provenance, ownership, and reuse status

This repository contains analytical materials derived from **two datasets with different provenance and rights status**. This distinction must be preserved in any public release.

## Dry Bean Dataset — third-party public benchmark

The Dry Bean Dataset is not owned by the manuscript authors. It is distributed by the UCI Machine Learning Repository and attributed to Murat Koklu and Ilker Ali Ozkan.

- Records: 13,611
- Classes: 7
- Native morphometric features: 16
- UCI DOI: `10.24432/C50S4B`
- License: CC BY 4.0
- Associated publication: Koklu, M.; Ozkan, I.A. *Multiclass classification of dry beans using computer vision and machine learning techniques*. *Computers and Electronics in Agriculture* 2020, 174, 105507. https://doi.org/10.1016/j.compag.2020.105507

Any redistributed analytical copy must preserve attribution to the original Dry Bean source.

## INIAP Rice morphometric dataset — author-generated analytical table

The INIAP Rice table used in this manuscript contains:

- 9,200 grain-level records;
- INIAP-11 (3,000), INIAP-12 (4,000), and INIAP-20 (2,200);
- numerical morphometric descriptors used by the feature-level analyses;
- linear variables expressed in pixels and area-related variables in squared pixels;
- dimensionless descriptors where applicable.

The public-release scope, if activated, is limited to the **numerical morphometric table and associated reproducibility metadata**. Original visual assets are outside the scope of this repository.

## Repository code and documentation

Code/documentation licensing should be handled separately from dataset rights. No blanket data license should be interpreted as overriding the provenance or reuse terms of the Dry Bean benchmark or the authors' INIAP Rice analytical table.
