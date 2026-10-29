# Mapping between frozen internal labels and manuscript labels

The frozen notebooks preserve internal representation names created during the analytical workflow. The manuscript uses dataset-specific scientific labels to distinguish a complete native invariant subset in Dry Bean from a nonredundant engineered invariant basis in INIAP Rice.

This mapping prevents the internal word `complete` from being misinterpreted for rice.

## Dry Bean

| Frozen/internal label | Manuscript label | Meaning |
|---|---|---|
| `R1_full_native` | R1 | all 16 native predictors |
| `R2_measured_core` | R2 | six-column measured core, including dimensionless EXTENT; excludes ECCENTRICITY |
| `R3_complete_invariant` | R3-C | complete native dimensionless subset; audit set, not a minimal algebraic basis |
| `R4_complete_log_area` | R4-C | R3-C plus log(pixel area) |

## INIAP Rice

| Frozen/internal label | Manuscript label | Meaning |
|---|---|---|
| `R1_full_native` | R1 | seven native predictors |
| `R2_measured_core` | R2 | six-column measured core including dimensionless EXTENT; excludes algebraically redundant ECCENTRICITY |
| `R3_complete_invariant` | R3-NR | historical/reanalysis internal name for the nonredundant engineered invariant basis |
| `R4_complete_log_area` | R4-NR | historical/reanalysis internal name for R3-NR plus log(pixel area) |
| `R4_hybrid_log_area` | R4-NR | exact frozen Notebook 05 champion; feature set is identical to the later R4-complete reanalysis set |

## Important interpretation rule

For INIAP Rice, `complete` in legacy internal filenames **does not mean that every available dimensionless native column is included**. The scientific manuscript label is `R3-NR`/`R4-NR` because the engineered basis is intentionally nonredundant. Native ECCENTRICITY is omitted from the engineered invariant basis because it is algebraically determined by aspect ratio within rounding tolerance.

The exact frozen rice champion remains the original Notebook 05 `R4_hybrid_log_area` model. Later reanalysis labels do not replace or retrain that frozen champion.

## Reviewer-driven harmonized representations (NB18)

Both datasets use **exactly the same five invariant predictors** in R3-5: `aspect_ratio`, `extent`, `solidity`, `circularity`, `ellipse_fill`. R4-5 adds exactly `log_area` (six predictors). See [NB18 full schema and performance](../reviewer_round_2026_10/NB18/NB18_02_rendimiento_y_esquema.csv), and its [group-paired sensitivity intervals](../reviewer_round_2026_10/NB18/NB18_03_contrastes_pareados_grupales.csv).

**Interpretation:** R1–R2 is chiefly a redundancy comparison; R3-C (Dry Bean, eight native dimensionless descriptors) differs from R3-NR (INIAP Rice, five engineered invariants). Neither is interchangeable with R3-5. R4-C, R4-NR and R4-5 add log-area to their own respective basis. Retain the legacy source column `AspectRation` for code compatibility but display the human-readable name *aspect ratio* in prose.
