import pandas as pd


def calculate_trust(row):
    trust = row["camera_confidence"]

    speed_difference = abs(
        row["gps_speed"] - row["imu_speed"]
    )

    if speed_difference > 5:
        trust -= 0.3

    if row["camera_confidence"] < 0.5:
        trust -= 0.3

    if row["distance"] < 5:
        trust -= 0.2

    trust = max(0, min(1, trust))

    return round(trust, 2)


def classify_trust(trust):
    if trust >= 0.8:
        return "HIGH"
    elif trust >= 0.5:
        return "MEDIUM"
    else:
        return "LOW"


def calculate_risk(trust):
    return round((1 - trust) * 100, 1)


def explain_row(row):
    reasons = []

    speed_difference = abs(
        row["gps_speed"] - row["imu_speed"]
    )

    if speed_difference > 5:
        reasons.append("GPS and IMU readings are inconsistent")

    if row["camera_confidence"] < 0.5:
        reasons.append("Camera confidence is low")

    if row["distance"] < 5:
        reasons.append("Obstacle distance is very small")

    if not reasons:
        return "Sensor readings are consistent"

    return "; ".join(reasons)


def load_drone_data(file_path="data/drone_sensor_data.csv"):
    df = pd.read_csv(file_path)

    df["trust_score"] = df.apply(
        calculate_trust,
        axis=1
    )

    df["trust_level"] = df["trust_score"].apply(
        classify_trust
    )

    df["risk_score"] = df["trust_score"].apply(
        calculate_risk
    )

    df["reason"] = df.apply(
        explain_row,
        axis=1
    )

    return df


if __name__ == "__main__":
    df = load_drone_data()

    print(
        df[
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
        ]
    )