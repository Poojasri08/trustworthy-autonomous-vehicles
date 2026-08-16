import pandas as pd
import random


data = []

# Normal sensor readings
for _ in range(100):
    gps_speed = random.uniform(5, 30)
    imu_speed = gps_speed + random.uniform(-1, 1)
    camera_confidence = random.uniform(0.85, 1.0)
    distance = random.uniform(10, 40)

    data.append([
        gps_speed,
        imu_speed,
        camera_confidence,
        distance,
        0
    ])


# Anomalous sensor readings
for _ in range(30):
    gps_speed = random.uniform(5, 30)
    imu_speed = random.uniform(40, 60)
    camera_confidence = random.uniform(0.2, 0.5)
    distance = random.uniform(1, 5)

    data.append([
        gps_speed,
        imu_speed,
        camera_confidence,
        distance,
        1
    ])


df = pd.DataFrame(
    data,
    columns=[
        "gps_speed",
        "imu_speed",
        "camera_confidence",
        "distance",
        "attack"
    ]
)

df.to_csv(
    "data/drone_training_data.csv",
    index=False
)

print("Drone training data generated successfully.")
print(f"Total samples: {len(df)}")
print(df.head())