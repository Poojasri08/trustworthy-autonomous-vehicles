import pandas as pd
from sklearn.ensemble import IsolationForest


class AnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(
            contamination=0.1,
            random_state=42
        )

    def train(self, data):
        self.model.fit(data)

    def predict(self, data):
        prediction = self.model.predict(data)

        if prediction[0] == -1:
            return "ANOMALY"
        else:
            return "NORMAL"


if __name__ == "__main__":
    df = pd.read_csv("data/training_data.csv")

    features = [
        "speed",
        "distance",
        "camera_confidence",
        "lidar_distance"
    ]

    X = df[features]

    detector = AnomalyDetector()
    detector.train(X)

    result = detector.predict(X.iloc[[0]])

    print("ML Anomaly Result:", result)