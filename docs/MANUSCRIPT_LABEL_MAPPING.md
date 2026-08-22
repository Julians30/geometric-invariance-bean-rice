# Mapping between frozen internal labels and manuscript labels

The frozen notebooks preserve internal representation names created during the analytical workflow. The manuscript uses dataset-specific scientific labels to distinguish a complete native invariant subset in Dry Bean from a nonredundant engineered invariant basis in INIAP Rice.

This mapping prevents the internal word `complete` from being misinterpreted for rice.

## Dry Bean

| Frozen/internal label | Manuscript label | Meaning |
|---|---|---|
| `R1_full_native` | R1 | all 16 native predictors |
| `R2_measured_core` | R2 | directly measured geometric core |
| `R3_complete_invariant` | R3-C | complete native dimensionless subset; audit set, not a minimal algebraic basis |
| `R4_complete_log_area` | R4-C | R3-C plus log(pixel area) |

## INIAP Rice

| Frozen/internal label | Manuscript label | Meaning |
|---|---|---|
| `R1_full_native` | R1 | seven native predictors |
| `R2_measured_core` | R2 | measured geometric core |
| `R3_complete_invariant` | R3-NR | historical/reanalysis internal name for the nonredundant engineered invariant basis |
| `R4_complete_log_area` | R4-NR | historical/reanalysis internal name for R3-NR plus log(pixel area) |
| `R4_hybrid_log_area` | R4-NR | exact frozen Notebook 05 champion; feature set is identical to the later R4-complete reanalysis set |

## Important interpretation rule

For INIAP Rice, `complete` in legacy internal filenames **does not mean that every available dimensionless native column is included**. The scientific manuscript label is `R3-NR`/`R4-NR` because the engineered basis is intentionally nonredundant. Native ECCENTRICITY is omitted from the engineered invariant basis because it is algebraically determined by aspect ratio within rounding tolerance.

The exact frozen rice champion remains the original Notebook 05 `R4_hybrid_log_area` model. Later reanalysis labels do not replace or retrain that frozen champion.
