import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Trustworthy Autonomous Vehicles",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 Trustworthy Autonomous Vehicle Monitor")
st.caption("Sensor trust and cybersecurity monitoring")

df = pd.read_csv("data/sensor_data.csv")


def calculate_trust(row):
    trust = row["camera_confidence"]

    distance_difference = abs(
        row["distance"] - row["lidar_distance"]
    )

    if distance_difference > 5:
        trust -= 0.3

    return max(0, min(1, trust))


def calculate_risk(trust_score, attack):
    risk = (1 - trust_score) * 100

    if attack == 1:
        risk += 30

    return min(100, round(risk, 2))


df["trust_score"] = df.apply(calculate_trust, axis=1)

df["risk_score"] = df.apply(
    lambda row: calculate_risk(
        row["trust_score"],
        row["attack"]
    ),
    axis=1
)

df["security_status"] = df.apply(
    lambda row: (
        "ALERT"
        if row["attack"] == 1
        else "WARNING"
        if row["trust_score"] < 0.5
        else "NORMAL"
    ),
    axis=1
)

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

st.bar_chart(
    df["risk_score"]
)