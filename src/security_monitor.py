import pandas as pd


def security_decision(row):
    # Known attack label in the dataset
    if row["attack"] == 1:
        return "ALERT"

    # Low trust is also suspicious
    if row["trust_score"] < 0.5:
        return "WARNING"

    return "NORMAL"


# Load sensor data
df = pd.read_csv("data/sensor_data.csv")


# Calculate trust score
def calculate_trust(row):
    trust = row["camera_confidence"]

    distance_difference = abs(
        row["distance"] - row["lidar_distance"]
    )

    if distance_difference > 5:
        trust -= 0.3

    return max(0, min(1, trust))


df["trust_score"] = df.apply(calculate_trust, axis=1)

# Security decision
df["security_status"] = df.apply(security_decision, axis=1)

print("\nSecurity Monitoring Results:\n")

print(df[
    [
        "speed",
        "distance",
        "camera_confidence",
        "lidar_distance",
        "attack",
        "trust_score",
        "security_status"
    ]
])