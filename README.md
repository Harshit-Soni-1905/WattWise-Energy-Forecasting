# ⚡ WattWise - Energy Consumption Forecasting

> Machine Learning based electricity consumption forecasting using XGBoost and an interactive Streamlit dashboard.

🌐 **Live Demo:** [WattWise | Energy Forecast · Streamlit](https://wattwise-energy-forecasting-mbdbdm3tqh5uhhypgwfxqw.streamlit.app/)

---

## 📌 Overview

**WattWise** is an energy consumption forecasting application developed as part of **HCL Project P_203 - Energy Consumption Forecasting**.

The project uses historical electricity consumption data to learn temporal consumption patterns and predict electricity demand using an **XGBoost Regression model**.

The trained model is integrated into an interactive **Streamlit dashboard** where users can provide historical consumption values and time information to generate an energy consumption forecast.

---

## 🎯 Problem Statement

Electricity consumption varies significantly depending on:

- Hour of the day
- Day of the week
- Month
- Recent electricity consumption
- Daily consumption patterns
- Weekly consumption patterns

The objective of this project is to build a machine learning model that can learn these patterns and estimate electricity consumption for a given time point.

---

## 🚀 Features

- ⚡ Electricity consumption forecasting
- 🤖 XGBoost Regression model
- 🕒 Time-based feature engineering
- 📊 Historical consumption analysis
- 📈 Interactive data visualization
- 🎛️ Interactive Streamlit dashboard
- 💡 Forecast interpretation
- 📊 Model performance metrics
- 🌑 Modern dark-themed UI
- 🌐 Deployed on Streamlit Community Cloud

---

## 🌐 Live Demo

Try the deployed application here:

👉 **[WattWise | Energy Forecast · Streamlit](https://wattwise-energy-forecasting-mbdbdm3tqh5uhhypgwfxqw.streamlit.app/)**

---

## 📂 Dataset

The project uses the **PJME Hourly Energy Consumption Dataset**.

### Dataset Columns

| Column | Description |
|---|---|
| `Datetime` | Timestamp of electricity consumption |
| `PJME_MW` | Electricity consumption in Megawatts |

### Dataset Information

- Start: January 2002
- End: August 2018
- Records: ~145K hourly observations
- Target: `PJME_MW`

---

## 🔍 Exploratory Data Analysis

Several patterns were investigated during exploratory data analysis.

### Overall Consumption Trend

The complete time series was visualized to understand long-term electricity consumption patterns and seasonal variations.

### Yearly Pattern

The 2017 consumption pattern showed noticeable seasonal behavior, including higher consumption during winter and summer periods.

### Daily Pattern

Hourly analysis showed that electricity consumption generally:

- Reaches lower levels during early morning hours
- Increases during the morning
- Reaches higher levels during the evening
- Decreases during nighttime

### Weekly Pattern

Average consumption also differed between weekdays and weekends, with weekdays generally showing higher consumption than weekends.

---

## 🛠️ Feature Engineering

To capture temporal and historical relationships, the following features were created.

### Time-Based Features

- `Hour`
- `DayOfWeek`
- `Month`

### Lag Features

| Feature | Meaning |
|---|---|
| `Lag_1` | Consumption during the previous hour |
| `Lag_24` | Consumption at the same hour on the previous day |
| `Lag_168` | Consumption at the same hour during the previous week |

These features allow the model to learn short-term, daily, and weekly consumption patterns.

---

## 📊 Train-Test Split

Because this is a time-series forecasting problem, the dataset was split chronologically rather than randomly.

| Set | Observations | Period |
|---|---|---|
| Training | 116,158 | 2002-01-08 → 2015-04-11 |
| Testing | 29,040 | 2015-04-11 → 2018-08-03 |

This preserves the chronological order of the data and prevents future observations from being used during training.

---

## 🤖 Machine Learning Model

The project uses an **XGBoost Regressor** with the following configuration:

```python
XGBRegressor(
    n_estimators=500,
    learning_rate=0.05,
    max_depth=8,
    subsample=0.8,
    colsample_bytree=0.8,
    objective="reg:squarederror",
    random_state=42
)
```

### Model Inputs

`Hour`, `DayOfWeek`, `Month`, `Lag_1`, `Lag_24`, `Lag_168`

### Target

`PJME_MW`

---

## 📈 Model Performance

The model was evaluated on the chronological test dataset.

| Metric | Result |
|---|---|
| MAE | 318.53 MW |
| RMSE | 432.89 MW |
| R² Score | 0.9956 |

### Interpretation

The model achieved an R² score of 0.9956 on the test set, indicating that it captured most of the variation in the observed electricity consumption values. MAE and RMSE provide additional measures of prediction error in Megawatts.

---

## 🔎 Feature Importance

| Feature | Importance |
|---|---|
| `Lag_1` | 0.737165 |
| `Lag_24` | 0.184869 |
| `Hour` | 0.035523 |
| `Lag_168` | 0.020929 |
| `DayOfWeek` | 0.016425 |
| `Month` | 0.005089 |

The model relies heavily on recent consumption information, particularly the previous hour and the previous day's consumption. Feature importance shows how much the model relies on each feature and should not be interpreted as causal influence.

---

## 🖥️ Streamlit Dashboard

The trained model is integrated into an interactive Streamlit application called **WattWise**.

- **🕒 Time Information:** users select the hour of day, day of week, and month
- **⚡ Historical Consumption:** users provide the previous hour, previous day, and previous week consumption
- **📈 Visualization:** historical consumption signals are shown in an interactive chart
- **🔮 Prediction:** the model generates the predicted electricity consumption in MW
- **💡 Forecast Insight:** the prediction is compared with the average of the three historical reference values, with a simple interpretation

---

## 🏗️ Project Structure

```text
WattWise-Energy-Forecasting/
│
├── app.py
├── energy_forecasting_model.pkl
├── model_features.pkl
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Harshit-Soni-1905/WattWise-Energy-Forecasting.git
```

Navigate into the project:

```bash
cd WattWise-Energy-Forecasting
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`.

---

## 🧠 Machine Learning Pipeline

```text
Raw Energy Dataset
        ↓
Data Cleaning
        ↓
Datetime Processing
        ↓
Exploratory Data Analysis
        ↓
Feature Engineering (Time + Lag Features)
        ↓
Chronological Train-Test Split
        ↓
XGBoost Regression
        ↓
Model Evaluation
        ↓
Model Serialization
        ↓
Streamlit Dashboard
        ↓
Deployment on Streamlit Community Cloud
        ↓
Energy Consumption Prediction
```

---

## 📌 Current Forecasting Approach

The current application performs a **one-step-ahead prediction** using the supplied historical consumption values. The user provides the relevant lag values and time information, and the trained XGBoost model predicts consumption for that input.

The current application is not a recursive 24-hour forecasting system.

---

## 🔮 Future Improvements

- 📅 Automatic date/time input
- 📂 CSV upload for historical consumption
- 🤖 Automatic lag feature generation
- 📈 Multi-step forecasting
- 🔮 24-hour ahead forecasting
- 🌡️ Weather-based features
- 📉 Prediction confidence intervals
- 🔄 Automated model retraining

---

## 🧰 Technologies Used

Python · Pandas · NumPy · Scikit-learn · XGBoost · Joblib · Streamlit · Matplotlib

---

## 👨‍💻 Author

**Harshit Soni**
B.Tech Computer Science & Engineering
ABES Engineering College

GitHub: [Harshit-Soni-1905](https://github.com/Harshit-Soni-1905)

---

## 📜 Project

HCL Industry Project - P_203
Energy Consumption Forecasting
Built using Machine Learning and Streamlit.
