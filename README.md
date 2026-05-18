# Multi-source Soil Moisture Product Prediction Fusion

This repository contains the implementation of the two-stage consensus feature learning framework proposed in:

> "Multi-source Soil Moisture Product Prediction Fusion Method Based on Two-stage Consensus Feature Learning"

The framework integrates ERA5, CoLM, and SMCI soil moisture products through prediction-layer fusion.

---

# Environment

The code was developed and tested with the following environment:

| Item | Details |
| :--- | :--- |
| Python | 3.12.7 |
| Conda | 24.9.2 |
| Key packages | torch, numpy 1.26.4, pandas 2.2.2, xarray 2023.6.0, netCDF4 1.7.2, scikit-learn 1.5.1, matplotlib 3.9.2, cartopy 0.25.0 |

The complete environment configuration is provided in:

```text
environment.yml
```
Create the environment using:

```bash
conda env create -f environment.yml
conda activate <environment_name>
```
---

# Input Data

The framework requires the following datasets:

- Meteorological forcing data
- ERA5 soil moisture product
- CoLM soil moisture product
- SMCI soil moisture product

## Supported formats
- NumPy(npy)

## Data characteristics

| Item | Description |
| :--- | :--- |
| Spatial resolution | 0.25° |
| Temporal resolution | Daily |
| Study region | Northeast China |

Example validation data are provided in:

```text
**Dataset Name**: Multi-source Soil Moisture Product Prediction Fusion Dataset

**Download Link**: https://doi.org/10.5281/zenodo.20048620
```

---
# Workflow

The recommended execution order is:

## Step 1: Train product-specific prediction models

```bash
python trainer1-era5.py
python trainer1-colm.py
python trainer1-smci.py
```

These scripts independently train prediction models for ERA5, CoLM, and SMCI products.

---

## Step 2: Train the Stage-2 fusion model

```bash
python trainer_stage2.py
```

This script trains the prediction-layer fusion model using consensus feature learning.

---

## Step 3: Evaluate the models

### Evaluate Stage-1 models

```bash
python eval.py
```

### Evaluate Stage-2 fusion model

```bash
python eval_stage2.py
```

---
# Additional Scripts

In addition to the main training and evaluation scripts, the repository also provides auxiliary scripts for ablation experiments, feature extraction, linear probing, fusion evaluation, and attention analysis.

---

## Ablation Experiments

The following scripts train and evaluate different variants of the Stage-2 fusion model.

### Training

```bash
python train_stage2_ablation_A.py
python train_stage2_ablation_B.py
python train_stage2_ablation_C.py
python train_stage2_ablation_D.py
python train_stage2_ablation_E.py
```

### Evaluation

```bash
python eval_ablation_A.py
python eval_ablation_B.py
python eval_ablation_C.py
python eval_ablation_D.py
python eval_ablation_E.py
```

These scripts are used to assess the contribution of different components in the proposed framework.

---

## Attention Analysis

```bash
python analyze_attention.py
python analyze_attention_results.py
```

These scripts analyze the attention weights learned by the fusion model and examine the relative importance of different source products and learned representations.

---

## Feature Extraction

```bash
python extract_train_features.py
```

This script extracts latent representations learned by the Stage-1 models.

---

## Linear Probing

```bash
python linear_regression_train.py
python linear_regression_eval.py
```

These scripts evaluate the information content and transferability of latent features using linear regression models.

---

## Metrics Evaluation

```bash
python eval_fusion.py
python eval_fusion_print.py
```

These scripts evaluate and summarize the fusion performance of the proposed framework.

---
# Outputs

The framework generates multiple output files for prediction results, evaluation metrics, ablation experiments, and analysis tasks.

## Prediction Outputs

| File pattern | Description |
| :--- | :--- |
| `pred_*.npy` | Predicted soil moisture results |
| `obs_*.npy` | Corresponding observation/reference data |
| `pred_stage2_*.npy` | Prediction-layer fusion results |
| `pred_ablation*.npy` | Predictions from ablation experiments |

---

## Evaluation Metrics

The repository provides multiple evaluation metrics for different products and experiments.

| File pattern | Description |
| :--- | :--- |
| `rmse_*.npy` | Root Mean Square Error (RMSE) |
| `urmse_*.npy` | Unbiased RMSE |
| `bias_*.npy` | Bias |
| `r_*.npy` | Correlation coefficient |
| `r2_*.npy` | Coefficient of determination (R²) |
| `KGE_*.npy` | Kling-Gupta Efficiency (KGE) |

These metrics are generated for:
- ERA5
- CoLM
- SMCI
- Stage-2 fusion results
- Ablation experiments

---
# Reproducibility

This repository includes:

- executable training and evaluation scripts,
- environment configuration files,
- sample input datasets,
- example outputs,
- and analysis scripts used in the manuscript.

These resources are provided to facilitate reproducibility and validation of the reported results.

---
