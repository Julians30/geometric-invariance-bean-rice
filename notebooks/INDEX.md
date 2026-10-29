# Notebook index and analytical roles

Only notebooks supporting the **feature-level morphometric workflow** belong in this repository.

## Core analytical sequence

| Stage | Project notebook | Role |
|---|---|---|
| 01 | `01_auditoria_y_congelamiento_Grain_Robustness_Q1_v2_DRIVE_ROBUSTO.ipynb` | source audit, duplicate audit, frozen feature-level data and integrity records |
| 02 | `02_redundancia_y_representaciones_Grain_Robustness_Q1.ipynb` | redundancy audit and morphometric representation construction |
| 03 | `03_particiones_congeladas_Grain_Robustness_Q1.ipynb` | duplicate-aware frozen train/calibration/test partitions |
| 04 | `04_seleccion_modelos_solo_entrenamiento_Grain_Robustness_Q1.ipynb` | model/hyperparameter selection restricted to training data |
| 05 | `05_entrenamiento_final_calibracion_y_prueba_base_Grain_Robustness_Q1.ipynb` | exact frozen champions, calibration and primary frozen-test predictions |
| 06 | `06_inferencia_estadistica_pareada_Grain_AI_MDPI_COLAB_v2.ipynb` | paired inferential analyses |
| 07 | `07_incertidumbre_clasificacion_selectiva_Grain_AI_MDPI_COLAB.ipynb` | selective classification using frozen champions |
| 08 | `08_prediccion_conformal_multiclase_CANONICA_v2_Grain_AI_MDPI_COLAB.ipynb` | canonical multiclass conformal prediction |
| 09 | `09_ablacion_interpretabilidad_morfometrica_Grain_AI_MDPI_COLAB_v2.ipynb` | ablation and block-reliance diagnostics |
| 10 | `10_sensibilidad_incertidumbre_medicion_morfometrica_Grain_AI_MDPI_COLAB.ipynb` | morphometric measurement/scale sensitivity |
| 11 | `11_tablas_figuras_manuscrito_Grain_AI_MDPI_COLAB_v4_FINAL.ipynb` | manuscript tables and analytical figures |
| 12 | `12_reanalisis_guiado_por_revisor_Grain_AI_MDPI_COLAB_v2_CORREGIDO.ipynb` | corrected representation, equivalence, leakage and sensitivity analyses |
| 13 | `13_final_freeze_revised_manuscript_assets_Grain_AI_MDPI_COLAB.ipynb` | earlier manuscript-asset freeze retained for provenance |
| 13B | `13B_reconciliacion_final_activos_manuscrito_Grain_AI_MDPI_COLAB.ipynb` | authoritative source reconciliation and manuscript-asset validation |
| 14 | `14_revision_menor_figuras_profesionales_Grain_AI_MDPI_COLAB_v2_CORREGIDO.ipynb` | final margin-sensitivity, matched-basis, learning-curve, reliability and publication-quality diagnostic analyses |
| 15 | `15_reconstruccion_figuras_finales_Grain_AI_MDPI_COLAB_v4.ipynb` | final publication-figure regeneration; no statistical re-estimation |

## Authority hierarchy

- **Primary performance/calibration/classwise/confusion:** Notebook 05.
- **Selective classification:** Notebook 07.
- **Canonical APS conformal results:** Notebook 08 v2.
- **Corrected representations, exact McNemar, equivalence, controlled block importance, scale and leakage audits:** Notebook 12 v2.
- **Cross-source reconciliation:** Notebook 13B.
- **Final minor-revision sensitivity/diagnostics:** Notebook 14.
- **Final figure rendering only:** Notebook 15 v4.

Notebook 15 changes presentation only and must not be treated as a new inferential source.

## Reviewer-round notebooks (added 28 October 2026)

The following *supplementary* analyses are published in [reviewer_round_2026_10](reviewer_round_2026_10/). They are distinct from the frozen notebook sequence and must not be used to retrospectively replace the original selected models or frozen test partitions. Execution outputs and execution counts were removed before publication; cell sources were preserved.

| Analysis | Notebook | Role |
|---|---|---|
| NB16 | [NB16 reviewer analyses](reviewer_round_2026_10/NB16_AgriEngineering_4664292_Ensayos_Revision_CPU_COLAB.ipynb) | classwise F1/confusions, duplicate-group inference, calibration sensitivity, acquisition provenance |
| NB16 reference | [Cammeo–Osmancik](reviewer_round_2026_10/NB16_AgriEngineering_Validacion_Externa_Cammeo_CPU.ipynb) | within-dataset independent reference comparison (not cross-dataset model transfer) |
| NB17 | [NB17 complementary analysis](reviewer_round_2026_10/NB17_AgriEngineering_4664292_Ensayos_Complementarios_CPU.ipynb) | class-size profiles, margin sensitivity, LAC/RAPS/Mondrian checks |
| NB17B | [NB17B partition audit](reviewer_round_2026_10/NB17B_Auditoria_Particiones_4664292_CORREGIDO.ipynb) | duplicate-group-disjoint calibration/test checks |
| NB18 | [NB18 symmetric representations](reviewer_round_2026_10/NB18_Representaciones_Simetricas_4664292_CPU.ipynb) | harmonized five-feature R3-5 and log-area R4-5 exploratory comparison |

The code originally resolves some inputs relative to the project Google Drive path `Grain_Robustness_Q1`; a new user may need to adapt input paths to a checkout or local copies. The numerical outputs are published separately as CSVs; do not mistake cleared notebook cells for absent results.
