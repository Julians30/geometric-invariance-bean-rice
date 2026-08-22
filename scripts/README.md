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

Checks frozen analytical files against `manifests/frozen_file_manifest.csv`.

For each present file it verifies:

- SHA-256;
- byte size;
- CSV row count;
- CSV column count.

Until the large analytical files are transferred, the script reports them as `PENDING` rather than treating their absence as a hash failure. After final transfer, all release-intended CSV files should be present and pass verification.

Run:

```bash
python scripts/verify_integrity.py
```

## Make targets

The repository `Makefile` provides shortcuts:

```bash
make audit
make integrity
make verify
```

These checks do not inspect or require original INIAP Rice grain images or segmentation masks because those assets are intentionally outside the repository scope.
