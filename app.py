from src.security_engine import process_sensor_data
import streamlit as st

st.set_page_config(
    page_title="Trustworthy Autonomous Vehicles",
    page_icon="🚗",
    layout="wide"
)

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

st.subheader("Security Monitoring")

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

st.subheader("Risk Score")

st.bar_chart(
    df["risk_score"]
)