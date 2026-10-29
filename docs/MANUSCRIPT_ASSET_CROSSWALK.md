# Manuscript-to-repository crosswalk — AgriEngineering 4664292 (October 2026)

**Authoritative paper for numbering:** the unchanged 32-page author-supplied revised manuscript *Geometric Invariance and Representation Sufficiency in Morphometric Bean and Rice Classification*, with **Tables 1–13 and Figures 1–12**. This document supersedes the earlier crosswalk that described frozen repository CSVs as if their internal Table_1/Table_2 names were current manuscript table numbers.

**Important:** the GitHub frozen output filenames preserve *historical internal numbering*. Never cite a repository file as a manuscript table/figure by basename alone. Primary selected-model scores are from NB05, aligned RBF-SVM representation refits from NB12, and post-review NB16–NB18 results are separate.

## Current manuscript tables

| Current manuscript table | Content | Repository evidence/source | Status |
|---|---|---|---|
| **Table 1** | Frozen train/calibration/test counts | `splits/Table_split_summary.csv`; `splits/Table_split_class_distribution.csv` | Published |
| **Table 2** | Dataset-specific R1/R2/R3-C/R3-NR/R4 definitions | `tables/supplementary/Table_S7_complete_representation_audit.csv`; `docs/MANUSCRIPT_LABEL_MAPPING.md` | Published; labels interpreted through crosswalk |
| **Table 3** | Originally selected models, macro-F1 and other test metrics | `tables/main/Table_2_exact_frozen_test_performance.csv`; `tables/supplementary/Table_S2_exact_model_metadata.csv` | Published, **NB05 authority** |
| **Table 4** | Dry Bean aligned per-class F1 | `reviewer_round_2026_10/NB16/NB16_01_f1_por_clase.csv` | Published, NB16 |
| **Table 5** | INIAP Rice aligned per-class F1 | `reviewer_round_2026_10/NB16/NB16_01_f1_por_clase.csv` | Published, NB16 |
| **Table 6** | Aligned representation contrasts and group-aware inference | `tables/main/Table_3_corrected_representation_contrasts.csv`; `tables/supplementary/Table_S9_all_paired_representation_contrasts.csv` | Published, NB12 |
| **Table 7** | Harmonized five-feature representation sensitivity | `reviewer_round_2026_10/NB18/NB18_02_rendimiento_y_esquema.csv`; `reviewer_round_2026_10/NB18/NB18_03_contrastes_pareados_grupales.csv` | Published, **exploratory NB18** |
| **Table 8** | Cammeo–Osmancik within-dataset replication | `reviewer_round_2026_10/NB16/NB16_Cammeo_representation_test_results.csv`; `NB16_Cammeo_paired_bootstrap.csv` in same folder | Published, NB16 reference |
| **Table 9** | Controlled native R1 block permutation | `tables/main/Table_6_controlled_R1_block_importance.csv`; `tables/supplementary/Table_S20_controlled_R1_importance.csv` | Published, NB12 |
| **Table 10** | Selective-classification 90% operating point | `tables/main/Table_4_original_selective_classification.csv`; `tables/supplementary/Table_S13_selective_operating_point_intervals.csv` | Published, NB07 |
| **Table 11** | Canonical APS conformal coverage | `tables/main/Table_5_original_canonical_APS.csv` | Published, NB08 |
| **Table 12** | Coherent native-R1 scale sensitivity | `tables/main/Table_7_controlled_R1_scale_sensitivity.csv` | Published, NB12 |
| **Table 13** | Literature comparison with other Dry Bean studies | Text and cited literature in manuscript; not one of the frozen analysis CSVs | Manuscript comparison |

## Current manuscript figures

| Manuscript figure | Meaning | Public repository asset status |
|---|---|---|
| **Figure 1** | Leakage-safe workflow diagram (nine stages) | Present in the revised manuscript; **not** the historical file `figures/main/Figure_1_corrected_representation_performance.png` |
| **Figures 2–3** | Training-only Spearman correlation matrices (Dry Bean and INIAP Rice) | Present in revised manuscript; not separately indexed under the current `figures/main` legacy filenames |
| **Figures 4–6** | Aligned classwise confusion matrices | Numerical matrices: `reviewer_round_2026_10/NB16/NB16_02_matrices_confusion_long.csv`; earlier aggregate supplementary PNGs are separate |
| **Figure 7** | Absolute aligned representation macro-F1 | Legacy plot `figures/main/Figure_1_corrected_representation_performance.png` |
| **Figure 8** | Paired R1 macro-F1 differences | Legacy plot `figures/main/Figure_2_corrected_paired_contrasts.png` |
| **Figure 9** | Controlled R1 permutation reliance | Legacy plot `figures/main/Figure_3_controlled_R1_block_importance.png` |
| **Figure 10** | Selective risk–coverage | Legacy plot `figures/main/Figure_4_risk_coverage_curves.png` |
| **Figure 11** | Conformal APS summary | Legacy plot `figures/main/Figure_5_conformal_APS_summary.png` |
| **Figure 12** | Native R1 scale perturbation | Legacy plot `figures/main/Figure_6_controlled_R1_scale_sensitivity.png` |

## Supplementary material and reviewer extension

The manuscript describes **original Tables S1a–S17 and Figures S1–S6**, plus **reviewer-driven Tables S18–S28 and Figures S7–S10**. The early internal supplement mapping remains at [SUPPLEMENTARY_LABEL_CROSSWALK.md](SUPPLEMENTARY_LABEL_CROSSWALK.md). The additional numerical source exports are in [reviewer_round_2026_10](../reviewer_round_2026_10/README.md); **these CSV filenames are analytic-output names, not a claim that publication-formatted S18–S28 tables or S7–S10 figure assets have all been transferred to the repository.**

| Reviewer concern | Machine-readable source |
|---|---|
| 2025/2026 source provenance and 2,400-record overlap | `reviewer_round_2026_10/NB16/NB16_10_manifest_procedencia_usado.csv`; `NB16_08_metricas_test_por_campana.csv` |
| Aligned classwise F1 and SIRA/DERMASON confusions | `reviewer_round_2026_10/NB16/NB16_01_f1_por_clase.csv`; `NB16_02_matrices_confusion_long.csv`; `reviewer_round_2026_10/NB17/NB17_02_SIRA_DERMASON_area_errores.csv` |
| Duplicate-group inference | `reviewer_round_2026_10/NB16/NB16_03_McNemar_agrupado_y_bootstrap.csv` |
| Separate 40/30/30 calibration roles and test disjointness | `reviewer_round_2026_10/NB16/NB16_04_split_calibracion_selectiva.csv`; `reviewer_round_2026_10/NB17B/NB17B_01_control_particiones.csv` |
| Conformal LAC/APS/RAPS/Mondrian and per-class review burden | `reviewer_round_2026_10/NB17/NB17_05_conformal_global_LAC_APS_RAPS_Mondrian.csv`; `reviewer_round_2026_10/NB16/NB16_07_carga_revision_por_clase.csv` |
| ±0.005 margin sensitivity and retrospective precision | `reviewer_round_2026_10/NB17/NB17_04_sensibilidad_margenes_equivalencia.csv`; `NB17_03_bootstrap_pareado_precision_y_MDD.csv` |
| Harmonized R3-5/R4-5 feature symmetry and paired intervals | `reviewer_round_2026_10/NB18/NB18_02_rendimiento_y_esquema.csv`; `NB18_03_contrastes_pareados_grupales.csv` |
| Cammeo–Osmancik replication | `reviewer_round_2026_10/NB16/NB16_Cammeo_representation_test_results.csv`; `NB16_Cammeo_paired_bootstrap.csv` |

## Scientific interpretation guardrails

1. Original frozen Dry Bean selected R1 macro-F1 **0.936605** differs from the aligned R1 refit **0.935440** (different probability-estimation seed); do not replace one with the other.
2. Original selected rice R4-NR macro-F1 **0.981165** is not the native R1 comparison baseline **0.977587**.
3. R2 includes **dimensionless EXTENT**; ECCENTRICITY is excluded as redundancy, so R1–R2 does not constitute a size-removal ablation.
4. Dry Bean R3-C and rice R3-NR have different definitions; R3-5/R4-5 are subsequent, symmetric reviewer-driven checks.
5. The main numerical margin **±0.01** and sensitivity **±0.005** are not independently validated economic thresholds.
6. INIAP image acquisition occurred across **2025 and 2026**, without a single-session claim or independent lot-disjoint or cross-device validation.
7. The Cammeo–Osmancik experiment is a separate within-dataset replication, not model transfer from INIAP.
