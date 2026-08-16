import pandas as pd

from src.drone_anomaly_detector import train_anomaly_detector
from src.drone_trust_engine import calculate_trust, classify_trust, calculate_risk


# Train the existing Isolation Forest
model, _ = train_anomaly_detector()


# Extreme test cases for ML inference
test_cases = pd.DataFrame([
    {
        "gps_speed": 100,
        "imu_speed": 0,
        "camera_confidence": 0.1,
        "distance": 1
    },
    {
        "gps_speed": 80,
        "imu_speed": 5,
        "camera_confidence": 0.2,
        "distance": 2
    },
    {
        "gps_speed": 60,
        "imu_speed": 0,
        "camera_confidence": 0.1,
        "distance": 1
    }
])


features = [
    "gps_speed",
    "imu_speed",
    "camera_confidence",
    "distance"
]


# ML prediction
predictions = model.predict(test_cases[features])

test_cases["ml_anomaly"] = pd.Series(predictions).map({
    1: "NORMAL",
    -1: "ANOMALY"
})


# Trust calculation
test_cases["trust_score"] = test_cases.apply(
    calculate_trust,
    axis=1
)

test_cases["trust_level"] = test_cases["trust_score"].apply(
    classify_trust
)

test_cases["risk_score"] = test_cases["trust_score"].apply(
    calculate_risk
)


# Combined security decision
def determine_status(row):

    if (
        row["trust_level"] == "LOW"
        and row["ml_anomaly"] == "ANOMALY"
    ):
        return "HIGH RISK"

    if (
        row["trust_level"] == "LOW"
        or row["ml_anomaly"] == "ANOMALY"
    ):
        return "SUSPICIOUS"

    return "NORMAL"


test_cases["security_status"] = test_cases.apply(
    determine_status,
    axis=1
)


print("\n===== HIGH-RISK INTEGRATION TEST =====\n")

print(
    test_cases[
        [
            "gps_speed",
            "imu_speed",
            "camera_confidence",
            "distance",
            "trust_score",
            "trust_level",
            "ml_anomaly",
            "security_status"
        ]
    ].to_string(index=False)
)