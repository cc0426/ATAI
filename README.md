# Multi-source Soil Moisture Product Prediction Fusion

This repository contains the implementation of the two-stage consensus feature learning framework proposed in:

"Multi-source Soil Moisture Product Prediction Fusion Method Based on Two-stage Consensus Feature Learning"

The framework integrates ERA5, CoLM, and SMCI soil moisture products through prediction-layer fusion.

## Environment

The code was developed and tested with the following core dependencies:

| Item | Details |
| :--- | :--- |
| **Python** | 3.12.7 |
| **Conda** | 24.9.2 |
| **Channel** | defaults, main, r |
| **Key Packages** | torch (via pip), numpy 1.26.4, pandas 2.2.2, xarray 2023.6.0, netCDF4 1.7.2, scikit-learn 1.5.1, matplotlib 3.9.2, cartopy 0.25.0 |

The full environment configuration is available in `environment.yml`.

