# Manuscript-facing supplementary tables

This directory is a **presentation layer** for the supplementary labels cited in the final manuscript. It does not replace or rename the frozen analytical assets in `../supplementary/`.

The final manuscript uses labels such as `S1a`, `S1b`, `S4b`, `S4c`, `S6a`, `S6b`, and `S9c`, whereas the final Notebook 13B archive retains a separate internal filename sequence. The authoritative mapping is documented in:

- `../../docs/SUPPLEMENTARY_LABEL_CROSSWALK.md`
- `../supplementary/manuscript_label_crosswalk.csv`

## Rules

1. Never infer manuscript table identity from an internal filename number alone.
2. Preserve all frozen source files unchanged.
3. Any manuscript-facing compact table assembled here must be traceable to one or more frozen repository/project assets.
4. No manuscript-facing table may introduce new model fitting, test-set selection, or numerical reinterpretation.
5. Original INIAP Rice grain images, segmentation masks, and raw acquisition assets remain outside the repository.

## Currently assembled directly from frozen/documented evidence

- `Table_S1a_data_provenance_availability.csv`
- `Table_S6a_dry_bean_equivalence.csv`
- `Table_S14_analysis_seeds.csv`

Additional manuscript-facing files may be added as deterministic views/copies of the frozen machine-readable evidence before submission.
