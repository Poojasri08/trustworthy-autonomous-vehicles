import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report, confusion_matrix


def train_anomaly_detector():

    df = pd.read_csv("data/drone_training_data.csv")

    features = [
        "gps_speed",
        "imu_speed",
        "camera_confidence",
        "distance"
    ]

    X = df[features]

    model = IsolationForest(
        contamination=0.2,
        random_state=42
    )

    model.fit(X)

    predictions = model.predict(X)

    df["ml_anomaly"] = pd.Series(predictions).map({
        1: "NORMAL",
        -1: "ANOMALY"
    })

    return model, df


if __name__ == "__main__":

    model, df = train_anomaly_detector()

    df["actual_status"] = df["attack"].map({
        0: "NORMAL",
        1: "ANOMALY"
    })

    print("\nML anomaly counts:")
    print(df["ml_anomaly"].value_counts())

    print("\nConfusion Matrix:")

    print(
        confusion_matrix(
            df["actual_status"],
            df["ml_anomaly"],
            labels=["NORMAL", "ANOMALY"]
        )
    )

    print("\nClassification Report:")

    print(
        classification_report(
            df["actual_status"],
            df["ml_anomaly"],
            labels=["NORMAL", "ANOMALY"],
            zero_division=0
        )
    )