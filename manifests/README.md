# Integrity, provenance, and validation manifests

This directory stores the compact records used to preserve traceability between frozen analytical inputs, split design, manuscript claims, and final reconciliation checks.

## Current files

- `frozen_file_manifest.csv` — archival row count, column count, file size, and SHA-256 for frozen Dry Bean and INIAP Rice CSV/Parquet analytical files.
- `split_file_manifest.csv` — row count, column count, file size, and SHA-256 for the two full frozen split-manifest CSVs intended for the repository release.
- `split_leakage_audit.csv` — checks that grouped train/calibration/test assignments are leakage-safe.
- `representation_split_alignment.csv` — confirms representation-level records remain aligned to the same frozen partitions.
- `final_split_validation.csv` — final split validation summary.
- `numerical_claim_register.csv` — high-value manuscript numerical claims and their authoritative analytical source.
- `final_notebook13B_validation.csv` — final source-reconciliation and manuscript-asset validation checks.
- `release_scope.csv` — explicit include/exclude policy for datasets, notebooks, tables, and original INIAP visual assets.

## Release-intended integrity verification

The article repository is currently intended to include exactly four large frozen CSV assets:

1. `data/dry_bean_frozen_v1.csv`
2. `data/iniap_rice_frozen_v1.csv`
3. `splits/dry_bean_split_manifest_v1.csv`
4. `splits/iniap_rice_split_manifest_v1.csv`

After transfer, run:

```bash
python scripts/verify_integrity.py --strict
```

The script verifies SHA-256, file size, row count, and column count. In normal preparation mode, absent large files are reported as `PENDING`; in `--strict` mode, any missing release-intended file fails the check.

The Parquet hashes remain in `frozen_file_manifest.csv` as archival provenance, but Parquet files are not currently required for the public article repository because the CSV tables are sufficient for the planned feature-level release.

## Release-scope verification

Before any reviewer or public release, run:

```bash
python scripts/audit_release_scope.py
```

This protects the repository boundary: only the INIAP Rice morphometric feature table and feature-level analytical materials belong here. Original grain images, segmentation masks, raw acquisition assets, and other unreleased doctoral-research visual material are excluded.

## Provenance rule

Dry Bean is a third-party UCI benchmark attributed to Koklu and Ozkan. INIAP Rice is original research data. These provenance categories must remain separate in documentation and licensing decisions.
