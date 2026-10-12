# License scope

This repository supports the manuscript **Geometric Invariance and Representation Sufficiency in Morphometric Bean and Rice Classification**, submitted to *Agriculture* (MDPI).

## Software: MIT License

The [MIT License](LICENSE) grants reuse rights for the authors' original software and associated software documentation in this repository, including:

- `scripts/` (Python analysis and verification utilities);
- `notebooks/` (the published source notebooks, to the extent the included code and supporting software documentation are owned by the authors);
- `Makefile` and `.github/workflows/` (automation and validation scripts).

Any third-party code or components retain their original licensing and attribution where applicable. A citation to the associated scientific work is appreciated; the MIT license itself requires preservation of its copyright and permission notices, not a scientific citation.

## Datasets and research outputs: not relicensed under MIT

The MIT license **does not** grant any license to the research data or other non-software research assets, including:

- `data/dry_bean_frozen_v1.csv`, which originates from the Dry Bean Dataset available through UCI under its source CC BY 4.0 terms and attribution requirements;
- `data/iniap_rice_frozen_v1.csv`, an author-generated morphometric analytical table publicly accessible here without a separate public reuse license granted by this notice;
- `splits/`, `tables/`, `results/`, `manifests/`, `figures/`, `protocol/` research data, analytical outputs, manifest values, charts and other scientific assets, which are **not automatically MIT-licensed**.

For precise rights and provenance, see [DATA_RIGHTS.md](DATA_RIGHTS.md), [DATA_CITATION.md](DATA_CITATION.md), [data/INIAP_RICE_SCOPE.md](data/INIAP_RICE_SCOPE.md), and the original Dry Bean source. Software source files located inside a data/results folder, if any, are only covered when expressly indicated; do not infer a blanket license for that folder.

Original INIAP Rice images, segmentation masks and raw acquisition materials are not in this repository and are not licensed here.

Public access to the numerical INIAP Rice table is distinct from permission to redistribute or republish it. The authors may specify the reuse terms of the author-generated dataset separately.

The scientific manuscript is not relicensed under MIT; publisher/publication terms apply separately.
