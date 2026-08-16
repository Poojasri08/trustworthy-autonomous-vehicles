import pandas as pd
import streamlit as st

from src.security_engine import process_sensor_data
from src.drone_trust_engine import load_drone_data


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
    use_container_width=True
)

st.subheader("Risk Score")

st.bar_chart(df["risk_score"])


# ============================================================
# DRONE MONITOR
# ============================================================

st.divider()

st.title("🚁 Drone Trust Monitor")
st.caption("GPS, IMU, camera and obstacle-distance monitoring")

drone_df = load_drone_data()

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Trust",
    f"{drone_df['trust_score'].mean():.2f}"
)

col2.metric(
    "Average Risk",
    f"{drone_df['risk_score'].mean():.1f}%"
)

col3.metric(
    "Suspicious Readings",
    int((drone_df["trust_level"] == "LOW").sum())
)


st.subheader("Drone Security Monitoring")

st.dataframe(
    drone_df[
        [
            "gps_speed",
            "imu_speed",
            "camera_confidence",
            "distance",
            "attack",
            "trust_score",
            "risk_score",
            "trust_level",
            "reason"
        ]
    ],
    use_container_width=True
)


st.subheader("Drone Trust Score")

st.bar_chart(
    drone_df["trust_score"]
)


st.subheader("Drone Risk Score")

st.bar_chart(
    drone_df["risk_score"]
)