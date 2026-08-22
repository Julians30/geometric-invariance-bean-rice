# Integrity, provenance, and validation manifests

This directory stores the compact records used to preserve traceability between frozen analytical inputs, split design, manuscript claims, and final reconciliation checks.

## Current files

- `frozen_file_manifest.csv` — expected row count, column count, file size, and SHA-256 for the frozen Dry Bean and INIAP Rice analytical files.
- `split_leakage_audit.csv` — checks that grouped train/calibration/test assignments are leakage-safe.
- `representation_split_alignment.csv` — confirms representation-level records remain aligned to the same frozen partitions.
- `final_split_validation.csv` — final split validation summary.
- `numerical_claim_register.csv` — high-value manuscript numerical claims and their authoritative analytical source.
- `final_notebook13B_validation.csv` — final source-reconciliation and manuscript-asset validation checks.
- `release_scope.csv` — explicit include/exclude policy for datasets, notebooks, tables, and original INIAP visual assets.

## Integrity verification

After the four large frozen CSV files are transferred, run:

```bash
python scripts/verify_integrity.py
```

The script verifies SHA-256, file size, and CSV dimensions against `frozen_file_manifest.csv`.

## Release-scope verification

Before any reviewer or public release, run:

```bash
python scripts/audit_release_scope.py
```

This protects the repository boundary: only the INIAP Rice morphometric feature table and feature-level analytical materials belong here. Original grain images, segmentation masks, raw acquisition assets, and other unreleased doctoral-research visual material are excluded.

## Provenance rule

Dry Bean is a third-party UCI benchmark attributed to Koklu and Ozkan. INIAP Rice is original research data. These provenance categories must remain separate in documentation and licensing decisions.
