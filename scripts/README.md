# Repository verification scripts

These scripts are repository-level safeguards for the pre-submission reproducibility package.

## `audit_release_scope.py`

Checks that the repository does not contain prohibited original INIAP Rice visual assets within the article release scope. It also verifies that the principal provenance and release-boundary documents are present.

Run:

```bash
python scripts/audit_release_scope.py
```

Expected result before release: `RELEASE-SCOPE AUDIT: PASS`.

## `verify_integrity.py`

Checks the **four release-intended frozen CSV files**:

- `data/dry_bean_frozen_v1.csv`
- `data/iniap_rice_frozen_v1.csv`
- `splits/dry_bean_split_manifest_v1.csv`
- `splits/iniap_rice_split_manifest_v1.csv`

Expected hashes and dimensions come from `manifests/frozen_file_manifest.csv` and `manifests/split_file_manifest.csv`.

For each present file it verifies:

- SHA-256;
- byte size;
- CSV row count;
- CSV column count.

During repository preparation, missing large files are reported as `PENDING`:

```bash
python scripts/verify_integrity.py
```

Immediately before reviewer/public release, use strict mode so that any missing release-intended file fails verification:

```bash
python scripts/verify_integrity.py --strict
```

## Make targets

The repository `Makefile` provides shortcuts:

```bash
make audit
make integrity
make verify
```

These checks do not inspect or require original INIAP Rice grain images or segmentation masks because those assets are intentionally outside the repository scope.
