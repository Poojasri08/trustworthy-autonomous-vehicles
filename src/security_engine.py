import pandas as pd


def calculate_trust(row):
    trust = row["camera_confidence"]

    distance_difference = abs(
        row["distance"] - row["lidar_distance"]
    )

    if distance_difference > 5:
        trust -= 0.3

    return round(max(0, min(1, trust)), 2)


def classify_trust(trust):
    if trust >= 0.8:
        return "HIGH"
    elif trust >= 0.5:
        return "MEDIUM"
    return "LOW"


def detect_anomaly(row):
    distance_difference = abs(
        row["distance"] - row["lidar_distance"]
    )

    return (
        row["camera_confidence"] < 0.7
        or distance_difference > 5
        or row["attack"] == 1
    )


def calculate_risk(trust_score, attack):
    risk = (1 - trust_score) * 100

    if attack == 1:
        risk += 30

    return min(100, round(risk, 2))


def classify_security(row):
    if row["attack"] == 1:
        return "ALERT"

    if row["trust_score"] < 0.5:
        return "WARNING"

    return "NORMAL"


def explain_row(row):
    reasons = []

    distance_difference = abs(
        row["distance"] - row["lidar_distance"]
    )

    if row["camera_confidence"] < 0.7:
        reasons.append("Low camera confidence")

    if distance_difference > 5:
        reasons.append("Camera and LiDAR readings disagree")

    if row["attack"] == 1:
        reasons.append("Dataset labels this sample as an attack")

    if not reasons:
        reasons.append("Sensor readings appear consistent")

    return "; ".join(reasons)


def process_sensor_data(file_path):
    df = pd.read_csv(file_path)

    df["anomaly_detected"] = df.apply(
        detect_anomaly,
        axis=1
    )

    df["trust_score"] = df.apply(
        calculate_trust,
        axis=1
    )

    df["trust_level"] = df["trust_score"].apply(
        classify_trust
    )

    df["risk_score"] = df.apply(
        lambda row: calculate_risk(
            row["trust_score"],
            row["attack"]
        ),
        axis=1
    )

    df["security_status"] = df.apply(
        classify_security,
        axis=1
    )

    df["explanation"] = df.apply(
        explain_row,
        axis=1
    )

    return df