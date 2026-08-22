# Prespecified frozen splits

This directory stores the frozen train/calibration/test assignments used in the manuscript.

## Files

### Full manifests — pending final large-file transfer

- `dry_bean_split_manifest_v1.csv`
- `iniap_rice_split_manifest_v1.csv`

The full files have already been verified in the project archive and must be transferred **without modification**.

### Compact audit summaries — available

- `Table_split_summary.csv` — dataset-level partition counts and split metadata.
- `Table_split_class_distribution.csv` — class distribution across train, calibration, and test partitions.

## Frozen split protocol

- Split seed: `20260803`
- Split version: `grouped_stratified_60_20_20_v1`
- Target allocation: approximately 60% training, 20% calibration, 20% final test
- Grouping unit: `duplicate_group_id`
- Stratification variable: class label

## Frozen partition sizes

| Dataset | Train | Calibration | Test | Total |
|---|---:|---:|---:|---:|
| Dry Bean | 8,161 | 2,725 | 2,725 | 13,611 |
| INIAP Rice | 5,520 | 1,840 | 1,840 | 9,200 |

## Duplicate-group audit

### Dry Bean

The frozen split manifest contains **13,543 unique duplicate groups** across 13,611 records. There are **68 groups of size 2** (136 rows involved in exact-duplicate groups); all remaining 13,475 groups contain one record. Group-level partitioning prevents any duplicate group from crossing train, calibration, and test partitions.

### INIAP Rice

The frozen split manifest contains **9,200 unique groups for 9,200 records**. No exact duplicate rows were found in the frozen audit.

## Manifest columns

Both full split manifests contain the same 12 fields:

- `dataset_id`
- `record_id`
- `source_excel_row`
- `feature_fingerprint_sha256`
- `full_row_fingerprint_sha256`
- `duplicate_group_id`
- `exact_duplicate_count`
- `class_label`
- `fold_id`
- `partition`
- `split_seed`
- `split_version`

These assignments are part of the prespecified leakage-safe design used for model development, calibration, and untouched final testing. They must not be regenerated after observing test results.
