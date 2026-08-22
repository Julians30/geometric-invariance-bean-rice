# Notebook index and analytical roles

Only notebooks supporting the **feature-level morphometric workflow** belong in this repository. Notebooks or files for original INIAP Rice image acquisition, raw-image storage, or segmentation asset generation are outside the release scope.

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
| 08 | `08_prediccion_conformal_multiclase_CANONICA_v2_Grain_AI_MDPI_COLAB.ipynb` | canonical multiclass conformal prediction using frozen champions |
| 09 | `09_ablacion_interpretabilidad_morfometrica_Grain_AI_MDPI_COLAB_v2.ipynb` | ablation and feature/block interpretability |
| 10 | `10_sensibilidad_incertidumbre_medicion_morfometrica_Grain_AI_MDPI_COLAB.ipynb` | morphometric measurement/scale sensitivity |
| 11 | `11_tablas_figuras_manuscrito_Grain_AI_MDPI_COLAB_v4_FINAL.ipynb` | manuscript tables and analytical figures |
| 12 | `12_reanalisis_guiado_por_revisor_Grain_AI_MDPI_COLAB_v2_CORREGIDO.ipynb` | reviewer-driven corrected representation, equivalence, leakage and sensitivity analyses |
| 13 | `13_final_freeze_revised_manuscript_assets_Grain_AI_MDPI_COLAB.ipynb` | earlier manuscript-asset freeze; retained for provenance but not preferred over 13B reconciliation |
| 13B | `13B_reconciliacion_final_activos_manuscrito_Grain_AI_MDPI_COLAB.ipynb` | final source reconciliation and authoritative manuscript-asset validation |

## Authority hierarchy

- **Primary performance/calibration/classwise/confusion:** Notebook 05.
- **Selective classification:** Notebook 07.
- **Canonical APS conformal results:** Notebook 08 v2.
- **Corrected representations, exact McNemar, equivalence, controlled block importance, scale and leakage audits:** Notebook 12 v2.
- **Final cross-source reconciliation:** Notebook 13B.

The Notebook 13 non-reconciled export should not override the final 13B reconciliation. The repository's `tables/main/` assets are sourced from the 13B reconciled package.
