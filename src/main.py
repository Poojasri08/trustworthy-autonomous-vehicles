import pandas as pd


def calculate_trust(row):
    trust = row["camera_confidence"]

    distance_difference = abs(
        row["distance"] - row["lidar_distance"]
    )

    if distance_difference > 5:
        trust -= 0.3

    return max(0, min(1, trust))


def classify_trust(trust):
    if trust >= 0.8:
        return "HIGH"
    elif trust >= 0.5:
        return "MEDIUM"
    return "LOW"


def security_decision(row):
    if row["attack"] == 1:
        return "ALERT"

    if row["trust_score"] < 0.5:
        return "WARNING"

    return "NORMAL"


def explain_row(row):
    reasons = []

    if row["camera_confidence"] < 0.7:
        reasons.append("Low camera confidence")

    distance_difference = abs(
        row["distance"] - row["lidar_distance"]
    )

    if distance_difference > 5:
        reasons.append("Camera and LiDAR readings disagree")

    if row["attack"] == 1:
        reasons.append("Sample is labelled as an attack")

    if not reasons:
        reasons.append("Sensor readings appear consistent")

    return "; ".join(reasons)
def calculate_risk(trust_score, attack):
    risk = (1 - trust_score) * 100

    if attack == 1:
        risk += 30

    return round(min(100, risk), 2)

# Load data
df = pd.read_csv("data/sensor_data.csv")

# Trust evaluation
df["trust_score"] = df.apply(calculate_trust, axis=1)
df["trust_level"] = df["trust_score"].apply(classify_trust)
df["risk_score"] = df.apply(
    lambda row: calculate_risk(
        row["trust_score"],
        row["attack"]
    ),
    axis=1
)

# Security monitoring
df["security_status"] = df.apply(security_decision, axis=1)

# Explainability
df["explanation"] = df.apply(explain_row, axis=1)

# Display final results
columns = [
    "speed",
    "distance",
    "camera_confidence",
    "lidar_distance",
    "attack",
    "trust_score",
    "trust_level",
    "risk_score",
    "security_status",
    "explanation"
]
print("\n=== TRUSTWORTHY AUTONOMOUS VEHICLE SECURITY MONITOR ===\n")
print(df[columns].to_string(index=False))