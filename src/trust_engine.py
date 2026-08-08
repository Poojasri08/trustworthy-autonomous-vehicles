import pandas as pd


def calculate_trust(row):
    trust = row["camera_confidence"]

    # Compare camera distance with LiDAR distance
    distance_difference = abs(
        row["distance"] - row["lidar_distance"]
    )

    # Reduce trust when sensor readings disagree
    if distance_difference > 5:
        trust -= 0.3

    # Keep score between 0 and 1
    trust = max(0, min(1, trust))

    return round(trust, 2)


def classify_trust(trust):
    if trust >= 0.8:
        return "HIGH"
    elif trust >= 0.5:
        return "MEDIUM"
    else:
        return "LOW"


# Load sensor data
df = pd.read_csv("data/sensor_data.csv")

# Calculate trust score
df["trust_score"] = df.apply(calculate_trust, axis=1)

# Classify trust level
df["trust_level"] = df["trust_score"].apply(classify_trust)

# Display results
print(df[
    [
        "speed",
        "distance",
        "camera_confidence",
        "lidar_distance",
        "attack",
        "trust_score",
        "trust_level"
    ]
])