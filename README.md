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


## Additional scripts

In addition to the main training and evaluation scripts, the repository also provides several auxiliary scripts for ablation experiments, linear probing, feature extraction, fusion evaluation, and attention analysis.

### Ablation experiments

The following scripts train and evaluate different variants of the Stage-2 fusion model:

```bash
python train_stage2_ablation_A.py
python train_stage2_ablation_B.py
python train_stage2_ablation_C.py
python train_stage2_ablation_D.py
python train_stage2_ablation_E.py
python analyze_attention.py 
python analyze_attention_results.py  
python eval_ablation_A.py  
python eval_ablation_B.py  
python eval_ablation_C.py  
python eval_ablation_D.py  
python eval_ablation_E.py  
python eval_fusion.py  
python eval_fusion_print.py  
python extract_train_features.py  
python linear_regression_eval.py  
python linear_regression_train.py  

