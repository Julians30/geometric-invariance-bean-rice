# Computational environment

The executed notebooks were run in Google Colab on CPU. The final reconciliation notebook recorded the following environment:

- Python: `3.12.13`
- NumPy: `2.0.2`
- pandas: `2.2.2`
- scikit-learn: `1.6.1`
- pyarrow: `18.1.0`
- Platform: `Linux-6.6.122+-x86_64-with-glibc2.35`
- CPU count observed: `2`
- GPU required: no

Additional packages used across the workflow include SciPy, joblib, statsmodels, CatBoost, Matplotlib, openpyxl, and tabulate. Exact versions for packages not explicitly recorded by the final reconciliation notebook are intentionally not invented here.

The top-level `requirements.txt` pins only versions that were explicitly recovered from the executed notebooks and leaves the remaining dependencies unpinned.
