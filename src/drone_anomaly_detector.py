import pandas as pd
from sklearn.ensemble import IsolationForest


def train_anomaly_detector(
    file_path="data/drone_training_data.csv"
):
    df = pd.read_csv(file_path)

    features = [
        "gps_speed",
        "imu_speed",
        "camera_confidence",
        "distance"
    ]

    X = df[features]

    model = IsolationForest(
        contamination=0.23,
        random_state=42
    )

    model.fit(X)

    # Isolation Forest:
    # 1 = normal
    # -1 = anomaly
    predictions = model.predict(X)

    df["ml_prediction"] = predictions

    df["ml_anomaly"] = df["ml_prediction"].apply(
        lambda x: "ANOMALY" if x == -1 else "NORMAL"
    )

    return model, df


if __name__ == "__main__":
    model, results = train_anomaly_detector()

    print(
        results[
            [
                "gps_speed",
                "imu_speed",
                "camera_confidence",
                "distance",
                "attack",
                "ml_anomaly"
            ]
        ].head(20)
    )

    print("\nML anomaly counts:")
    print(results["ml_anomaly"].value_counts())