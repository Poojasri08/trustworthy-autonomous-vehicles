import pandas as pd


def explain_row(row):
    reasons = []

    distance_difference = abs(
        row["distance"] - row["lidar_distance"]
    )

    if row["camera_confidence"] < 0.7:
        reasons.append("Low camera confidence")

    if distance_difference > 5:
        reasons.append("Camera and LiDAR distance readings disagree")

    if row["attack"] == 1:
        reasons.append("Dataset labels this sample as an attack")

    if not reasons:
        reasons.append("Sensor readings appear consistent")

    return "; ".join(reasons)


df = pd.read_csv("data/sensor_data.csv")

df["explanation"] = df.apply(explain_row, axis=1)

print("\nExplainable Security Results:\n")

print(df[
    [
        "speed",
        "distance",
        "camera_confidence",
        "lidar_distance",
        "attack",
        "explanation"
    ]
].to_string(index=False))
