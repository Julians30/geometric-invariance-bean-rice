# Data

This directory is reserved exclusively for the **morphometric feature tables** used in the manuscript.

## Provenance and ownership

### Dry Bean

`dry_bean_frozen_v1.csv` is derived from the **public Dry Bean benchmark dataset** distributed by the **UCI Machine Learning Repository**. The dataset is attributed to **Murat Koklu and Ilker Ali Ozkan** and is **not owned by the authors of this repository**.

- 13,611 records
- 7 classes
- 16 morphometric features
- DOI: 10.24432/C50S4B
- License: CC BY 4.0

The frozen file is retained only to document the exact analytical version used in this study. See [`THIRD_PARTY_ATTRIBUTION.md`](THIRD_PARTY_ATTRIBUTION.md) for the dedicated source and reuse notice.

### INIAP Rice

`iniap_rice_frozen_v1.csv` corresponds to the **original INIAP Rice morphometric dataset generated within the authors' research**.

- 9,200 records
- 3 varieties: INIAP-11, INIAP-12, INIAP-20
- Numerical morphometric descriptors only
- Linear measurements interpreted in pixels
- Area-related measurements interpreted in squared pixels
- Dimensionless shape descriptors where applicable

See [`INIAP_RICE_SCOPE.md`](INIAP_RICE_SCOPE.md) for the explicit article-release boundary and current reuse status.

## Files

- `dry_bean_frozen_v1.csv` — pending final large-file transfer.
- `iniap_rice_frozen_v1.csv` — pending final large-file transfer.
- `data_dictionary.csv` — available.
- `THIRD_PARTY_ATTRIBUTION.md` — available.
- `INIAP_RICE_SCOPE.md` — available.

## INIAP Rice release restriction

**Do not upload original INIAP Rice grain images, segmentation masks, image-acquisition files, or other raw visual materials.** Those materials are part of an ongoing doctoral research project and are outside the scope of this repository.

Only the derived morphometric table necessary for the feature-level analyses is included.

## Reproducibility note

The frozen datasets must be uploaded **without modification** so that their SHA-256 values remain consistent with `../manifests/frozen_file_manifest.csv`. After transfer, run:

```bash
python scripts/verify_integrity.py
```

The release-scope guard can be checked with:

```bash
python scripts/audit_release_scope.py
```
