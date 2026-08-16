from src.drone_trust_engine import load_drone_data
from src.drone_anomaly_detector import train_anomaly_detector


def analyze_drone():

    # Rule-based trust analysis
    trust_df = load_drone_data()

    # ML anomaly detection
    _, ml_df = train_anomaly_detector()

    # Add ML result
    trust_df["ml_anomaly"] = ml_df["ml_anomaly"]

    # Combined security decision
    def determine_status(row):

        if row["trust_level"] == "LOW" and row["ml_anomaly"] == "ANOMALY":
            return "HIGH RISK"

        if row["trust_level"] == "LOW" or row["ml_anomaly"] == "ANOMALY":
            return "SUSPICIOUS"

        return "NORMAL"

    trust_df["security_status"] = trust_df.apply(
        determine_status,
        axis=1
    )

    return trust_df


if __name__ == "__main__":

    df = analyze_drone()

    print(
        df[
            [
                "gps_speed",
                "imu_speed",
                "trust_score",
                "risk_score",
                "trust_level",
                "ml_anomaly",
                "security_status"
            ]
        ]
    )