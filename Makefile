.PHONY: audit integrity verify status

# Check that prohibited original INIAP visual assets are not in the release scope.
audit:
	python scripts/audit_release_scope.py

# Verify frozen data against SHA-256, size and CSV shape when the large files are present.
integrity:
	python scripts/verify_integrity.py

# Run both repository checks.
verify: audit integrity

# Show the repository preparation checklist.
status:
	@cat STATUS.md
