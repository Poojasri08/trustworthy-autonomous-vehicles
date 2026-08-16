import streamlit as st

from src.security_engine import process_sensor_data
from src.drone_security_engine import analyze_drone


st.set_page_config(
    page_title="Trustworthy Autonomous Vehicles",
    page_icon="🚗",
    layout="wide"
)


# ============================================================
# VEHICLE MONITOR
# ============================================================

st.title("🚗 Trustworthy Autonomous Vehicle Monitor")
st.caption("Sensor trust and cybersecurity monitoring")

df = process_sensor_data("data/sensor_data.csv")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Trust",
    f"{df['trust_score'].mean():.2f}"
)

col2.metric(
    "Average Risk",
    f"{df['risk_score'].mean():.1f}%"
)

col3.metric(
    "Detected Attacks",
    int(df["attack"].sum())
)

st.subheader("Vehicle Security Monitoring")

st.dataframe(
    df[
        [
            "speed",
            "distance",
            "camera_confidence",
            "lidar_distance",
            "attack",
            "trust_score",
            "risk_score",
            "security_status"
        ]
    ],
    width="stretch"
)

st.subheader("Vehicle Risk Score")

st.bar_chart(df["risk_score"])


# ============================================================
# DRONE MONITOR
# ============================================================

st.divider()

st.title("🚁 Drone Trust & AI Security Monitor")

st.caption(
    "Rule-based sensor trust combined with ML anomaly detection"
)

drone_df = analyze_drone()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Average Trust",
    f"{drone_df['trust_score'].mean():.2f}"
)

col2.metric(
    "Average Risk",
    f"{drone_df['risk_score'].mean():.1f}%"
)

col3.metric(
    "ML Anomalies",
    int((drone_df["ml_anomaly"] == "ANOMALY").sum())
)

col4.metric(
    "High Risk",
    int((drone_df["security_status"] == "HIGH RISK").sum())
)


st.subheader("Drone Security Monitoring")

st.dataframe(
    drone_df[
        [
            "gps_speed",
            "imu_speed",
            "trust_score",
            "risk_score",
            "trust_level",
            "ml_anomaly",
            "security_status",
            "reason"
        ]
    ],
    width="stretch"
)


st.subheader("Drone Trust Score")

st.bar_chart(
    drone_df["trust_score"]
)


st.subheader("Drone Risk Score")

st.bar_chart(
    drone_df["risk_score"]
)