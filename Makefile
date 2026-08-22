.PHONY: audit integrity integrity-strict verify release-check status

# Check that prohibited original INIAP visual assets are not in the release scope.
audit:
	python scripts/audit_release_scope.py

# Verify present release-intended frozen CSV files; missing large files are reported as PENDING.
integrity:
	python scripts/verify_integrity.py

# Strict pre-release verification: all four intended frozen CSV files must be present and valid.
integrity-strict:
	python scripts/verify_integrity.py --strict

# Preparation-mode repository verification.
verify: audit integrity

# Reviewer/public-release gate. This is expected to fail until all four large CSV files are transferred.
release-check: audit integrity-strict

# Show the repository preparation checklist.
status:
	@cat STATUS.md
