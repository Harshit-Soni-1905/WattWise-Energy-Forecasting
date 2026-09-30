import streamlit as st
import pandas as pd
import joblib


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="WattWise | Energy Forecast",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# LOAD MODEL
# =========================================================

model = joblib.load("energy_forecasting_model.pkl")
features = joblib.load("model_features.pkl")


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(0,255,170,0.08), transparent 25%),
        radial-gradient(circle at 90% 20%, rgba(0,180,255,0.08), transparent 25%),
        #07111f;
    color: #f5f7fa;
}

.main {
    padding-top: 1rem;
}


/* SIDEBAR */

section[data-testid="stSidebar"] {
    background: #050d18;
    border-right: 1px solid rgba(255,255,255,0.08);
}


/* HERO */

.hero {
    padding: 35px 40px;
    border-radius: 24px;
    background: linear-gradient(
        135deg,
        rgba(0,255,170,0.12),
        rgba(0,170,255,0.08)
    );
    border: 1px solid rgba(0,255,170,0.15);
    margin-bottom: 25px;
}

.hero-title {
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 8px;
    letter-spacing: -1px;
    color: white;
}

.hero-title span {
    color: #00e6a7;
}

.hero-subtitle {
    color: #a9b7c8;
    font-size: 17px;
}


/* SECTION TITLES */

.section-title {
    font-size: 22px;
    font-weight: 700;
    margin-top: 10px;
    margin-bottom: 15px;
    color: white;
}


/* GLASS CARDS */

.glass-card {
    background: rgba(255,255,255,0.035);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 20px;
    padding: 22px;
    margin-bottom: 18px;
    backdrop-filter: blur(10px);
}


/* PREDICTION CARD */

.metric-card {
    background: linear-gradient(
        135deg,
        rgba(0,230,167,0.14),
        rgba(0,150,255,0.08)
    );
    border: 1px solid rgba(0,230,167,0.18);
    border-radius: 22px;
    padding: 28px;
    text-align: center;
}

.metric-label {
    color: #9baabd;
    font-size: 14px;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.metric-value {
    font-size: 38px;
    font-weight: 800;
    color: #00e6a7;
    margin-top: 8px;
}

.metric-unit {
    color: #b5c0ce;
    font-size: 15px;
}


/* BADGES */

.badge {
    display: inline-block;
    padding: 7px 13px;
    border-radius: 20px;
    background: rgba(0,230,167,0.10);
    border: 1px solid rgba(0,230,167,0.18);
    color: #00e6a7;
    font-size: 13px;
    margin-right: 5px;
}


/* BUTTON */

.stButton > button {
    width: 100%;
    border-radius: 14px;
    border: none;
    padding: 14px 20px;
    font-size: 17px;
    font-weight: 700;
    background: linear-gradient(
        90deg,
        #00e6a7,
        #00b7ff
    );
    color: #041018;
    transition: 0.25s;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(0,230,167,0.20);
}


/* INPUTS */

div[data-baseweb="input"],
div[data-baseweb="select"] {
    border-radius: 12px;
}


/* FOOTER */

.footer {
    text-align: center;
    color: #667589;
    padding: 30px 0 10px 0;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## ⚡ WattWise")

    st.markdown(
        '<p style="color:#91a0b3;">AI-powered electricity consumption forecasting.</p>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("### 🧠 Model")

    st.markdown(
        '<span class="badge">XGBoost</span> <span class="badge">Regression</span>',
        unsafe_allow_html=True
    )

    st.markdown("")

    st.markdown("### 📊 Model Performance")

    st.metric("R² Score", "99.56%")
    st.metric("MAE", "318.53 MW")
    st.metric("RMSE", "432.89 MW")

    st.markdown("---")

    st.markdown("""
### 📌 Features Used

• Previous hour  
• Previous day  
• Previous week  
• Hour of day  
• Day of week  
• Month
""")

    st.markdown("---")

    st.caption("HCL P_203 • Energy Consumption Forecasting")


# =========================================================
# HERO
# =========================================================

st.markdown(
    '<div class="hero"><div class="hero-title">⚡ <span>WattWise</span></div><div class="hero-subtitle">Intelligent Energy Consumption Forecasting powered by Machine Learning</div></div>',
    unsafe_allow_html=True
)


# =========================================================
# FORECAST CONFIGURATION
# =========================================================

st.markdown(
    '<div class="section-title">🎛️ Forecast Configuration</div>',
    unsafe_allow_html=True
)

left, right = st.columns(2)


# =========================================================
# TIME INFORMATION
# =========================================================

with left:

    st.markdown(
        '<div class="glass-card">',
        unsafe_allow_html=True
    )

    st.markdown("### 🕒 Time Information")

    # Hour

    hour = st.slider(
        "Hour of Day",
        min_value=0,
        max_value=23,
        value=12
    )

    # Day

    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    day_of_week = st.selectbox(
        "Day of Week",
        options=list(range(7)),
        format_func=lambda x: days[x],
        index=2
    )

    # Month

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    month = st.selectbox(
        "Month",
        options=list(range(1, 13)),
        format_func=lambda x: months[x - 1],
        index=6
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# HISTORICAL CONSUMPTION
# =========================================================

with right:

    st.markdown(
        '<div class="glass-card">',
        unsafe_allow_html=True
    )

    st.markdown("### ⚡ Historical Consumption")

    lag_1 = st.number_input(
        "Previous Hour (MW)",
        min_value=0.0,
        max_value=100000.0,
        value=30000.0,
        step=100.0
    )

    lag_24 = st.number_input(
        "Previous Day, Same Hour (MW)",
        min_value=0.0,
        max_value=100000.0,
        value=30000.0,
        step=100.0
    )

    lag_168 = st.number_input(
        "Previous Week, Same Hour (MW)",
        min_value=0.0,
        max_value=100000.0,
        value=30000.0,
        step=100.0
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# HISTORICAL SIGNAL VISUALIZATION
# =========================================================

st.markdown(
    '<div class="section-title">📈 Historical Consumption Signals</div>',
    unsafe_allow_html=True
)

chart_data = pd.DataFrame({
    "Period": [
        "Previous Hour",
        "Previous Day",
        "Previous Week"
    ],
    "Consumption (MW)": [
        lag_1,
        lag_24,
        lag_168
    ]
})

st.bar_chart(
    chart_data.set_index("Period"),
    height=280
)


# =========================================================
# FORECAST
# =========================================================

st.markdown(
    '<div class="section-title">🔮 Forecast</div>',
    unsafe_allow_html=True
)


# =========================================================
# PREDICTION
# =========================================================

if st.button("⚡ Generate Energy Forecast"):

    input_data = pd.DataFrame(
        [[
            hour,
            day_of_week,
            month,
            lag_1,
            lag_24,
            lag_168
        ]],
        columns=features
    )

    prediction = model.predict(input_data)[0]


    # =====================================================
    # MAIN PREDICTION CARD
    # =====================================================

    st.markdown(
        f'''
<div class="metric-card">
<div class="metric-label">Predicted Energy Consumption</div>
<div class="metric-value">{prediction:,.2f}</div>
<div class="metric-unit">Megawatts (MW)</div>
</div>
''',
        unsafe_allow_html=True
    )

    st.markdown("")


    # =====================================================
    # INPUT SUMMARY
    # =====================================================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Previous Hour",
            f"{lag_1:,.0f} MW"
        )

    with col2:
        st.metric(
            "Previous Day",
            f"{lag_24:,.0f} MW"
        )

    with col3:
        st.metric(
            "Previous Week",
            f"{lag_168:,.0f} MW"
        )


    # =====================================================
    # FORECAST INSIGHT
    # =====================================================

    average_history = (
        lag_1 +
        lag_24 +
        lag_168
    ) / 3

    difference = prediction - average_history

    st.markdown("### 💡 Forecast Insight")

    if difference > 1000:

        st.info(
            f"""
The model predicts **{prediction:,.0f} MW**.

This is approximately **{abs(difference):,.0f} MW higher**
than the average of the three historical reference values.
"""
        )

    elif difference < -1000:

        st.info(
            f"""
The model predicts **{prediction:,.0f} MW**.

This is approximately **{abs(difference):,.0f} MW lower**
than the average of the three historical reference values.
"""
        )

    else:

        st.info(
            f"""
The model predicts **{prediction:,.0f} MW**,
which is close to the average of the historical
reference values.
"""
        )


# =========================================================
# MODEL EXPLANATION
# =========================================================

with st.expander("🧠 How does this model work?"):

    st.markdown("""
### XGBoost Energy Forecasting

The model learns relationships between historical
electricity consumption and time-based patterns.

### Input Signals

- Previous hour consumption
- Previous day consumption
- Previous week consumption
- Hour of day
- Day of week
- Month

### Machine Learning Model

**XGBoost Regression**

### Test Performance

| Metric | Value |
|---|---:|
| MAE | 318.53 MW |
| RMSE | 432.89 MW |
| R² | 0.9956 |

The model currently performs a **one-step-ahead
prediction** using the supplied historical
consumption values.
""")


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    '<div class="footer">⚡ WattWise Energy Forecasting<br>HCL Project P_203 • Machine Learning • XGBoost</div>',
    unsafe_allow_html=True
)