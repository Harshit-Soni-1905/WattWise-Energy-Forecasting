# ⚡ WattWise - Energy Consumption Forecasting

> Machine Learning based electricity consumption forecasting using XGBoost and an interactive Streamlit dashboard.

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

---

## 📂 Dataset

The project uses the **PJME Hourly Energy Consumption Dataset**.

### Dataset columns

| Column | Description |
|---|---|
| `Datetime` | Timestamp of electricity consumption |
| `PJME_MW` | Electricity consumption in Megawatts |

### Dataset information

- Start: January 2002
- End: August 2018
- Records: ~145K hourly observations
- Target: `PJME_MW`

The dataset contains historical hourly electricity consumption measurements.

---

# 🔍 Exploratory Data Analysis

Several patterns were investigated during exploratory data analysis.

### 1. Overall Consumption Trend

The complete time series was visualized to understand long-term electricity consumption patterns and seasonal variations.

### 2. Yearly Pattern

The 2017 consumption pattern showed noticeable seasonal behavior, including higher consumption during winter and summer periods.

### 3. Daily Pattern

Hourly analysis showed that electricity consumption generally:

- Reaches lower levels during early morning hours
- Increases during the morning
- Reaches higher levels during the evening
- Decreases during nighttime

### 4. Weekly Pattern

Average consumption also differed between weekdays and weekends, with weekdays generally showing higher consumption than weekends.

---

# 🛠️ Feature Engineering

To capture temporal and historical relationships, the following features were created.

### Time-based features

```text
Hour
DayOfWeek
Month
