# WattWise Energy Forecasting

> AI-powered electricity consumption forecasting platform built with XGBoost and an interactive Streamlit dashboard.

## Overview
WattWise predicts household and commercial electricity load demands using historical time-series features and gradient boosting, helping optimize energy distribution and reduce waste.

## Features
- **Time-Series Feature Engineering:** Extracts temporal lags, rolling averages, and calendar features from raw power consumption logs (`PJME_hourly.csv`).
- **XGBoost Regressor:** Optimized gradient boosting model trained on historical energy usage metrics.
- **Streamlit Interactive UI:** Live forecasting dashboard allowing users to input parameters and visualize load predictions instantly.

## Tech Stack
- **Languages:** Python
- **Libraries:** XGBoost, Scikit-Learn, Pandas, NumPy, Streamlit, Matplotlib, Seaborn

## Run Locally
```bash
git clone https://github.com/Harshit-Soni-1905/WattWise-Energy-Forecasting.git
cd WattWise-Energy-Forecasting
pip install -r requirements.txt
streamlit run app.py
```
