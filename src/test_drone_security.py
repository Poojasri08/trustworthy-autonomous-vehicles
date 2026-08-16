from src.drone_security_engine import analyze_drone


def test_security_pipeline():

    df = analyze_drone()

    print("\n===== DRONE SECURITY INTEGRATION TEST =====\n")

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
        ].to_string(index=False)
    )

    print("\n===== SECURITY STATUS SUMMARY =====\n")

    print(
        df["security_status"].value_counts()
    )


if __name__ == "__main__":
    test_security_pipeline()