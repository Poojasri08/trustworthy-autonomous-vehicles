🚗🔒 Trustworthy Autonomous Vehicles

A cybersecurity and trustworthy-AI prototype for detecting unreliable sensor behavior in autonomous systems.

The project combines sensor consistency checking, trust scoring, risk assessment, explainable security decisions, and machine-learning anomaly detection.

Current prototype: simulated autonomous vehicle and drone sensor data. No physical vehicle or drone is required.

⸻

🎯 What This Project Does

Autonomous systems depend on multiple sensors to make decisions. If a sensor is manipulated, corrupted, or produces unreliable data, the system may make unsafe decisions.

This project addresses that problem by asking:

Can we measure how trustworthy sensor data is before allowing the system to rely on it?

The prototype:

1. Reads simulated sensor data.
2. Checks whether sensor readings are consistent.
3. Calculates a trust score.
4. Converts trust into a risk score.
5. Generates an explanation for suspicious behavior.
6. Uses Isolation Forest to detect unusual sensor patterns.
7. Combines rule-based trust analysis with ML anomaly detection.
8. Displays the results through a Streamlit dashboard.

⸻

🚁 Drone Security Prototype

The drone prototype monitors:

* GPS speed
* IMU speed
* Camera confidence
* Obstacle distance

Example

If:

GPS speed = 20 m/s
IMU speed = 45 m/s
Camera confidence = 0.40
Distance = 5 m

the system identifies multiple warning signals:

GPS/IMU disagreement
Camera confidence is low
Obstacle distance is small

This results in:

Low Trust
High Risk
ML Anomaly
High Risk Security Status

⸻

🧠 Trust Model

The current rule-based trust engine starts with camera confidence and reduces trust when suspicious conditions are detected.

Checks

Condition	Effect
GPS and IMU speeds differ significantly	Trust decreases
Camera confidence < 0.5	Trust decreases
Obstacle distance < 5 m	Trust decreases

The final trust score is constrained between:

0.0 → 1.0

Trust classification

Trust >= 0.8       → HIGH
Trust >= 0.5       → MEDIUM
Trust < 0.5        → LOW

⸻

🤖 Machine Learning

The project uses Isolation Forest for unsupervised anomaly detection.

The model analyzes:

* GPS speed
* IMU speed
* Camera confidence
* Obstacle distance

The ML system produces:

NORMAL

or:

ANOMALY

The ML result is then combined with the rule-based trust result.

Combined decision

LOW Trust + ML Anomaly
        ↓
HIGH RISK
LOW Trust OR ML Anomaly
        ↓
SUSPICIOUS
HIGH/MEDIUM Trust + Normal ML result
        ↓
NORMAL

⸻

📊 Dashboard

The project includes a Streamlit dashboard displaying:

Autonomous Vehicle Monitor

* Average Trust
* Average Risk
* Detected Attacks
* Sensor monitoring table
* Risk chart

Drone Trust & AI Security Monitor

* Average Trust
* Average Risk
* ML Anomalies
* High Risk cases
* GPS speed
* IMU speed
* Camera confidence
* Obstacle distance
* Trust level
* ML anomaly status
* Security status
* Explanation/reason

⸻

🏗️ Architecture

                 Sensor Data
                     │
          ┌──────────┴──────────┐
          │                     │
     Rule-Based Logic       ML Detection
          │                     │
          ↓                     ↓
     Trust Score          ML Anomaly
          │                     │
          ↓                     ↓
      Risk Score ────────→ Combined
                              │
                              ↓
                    Security Decision
                              │
                              ↓
                     Streamlit Dashboard

⸻

📁 Project Structure

trustworthy-autonomous-vehicles/
│
├── data/
│   ├── sensor_data.csv
│   ├── drone_sensor_data.csv
│   └── drone_training_data.csv
│
├── docs/
│
├── src/
│   ├── trust_engine.py
│   ├── security_engine.py
│   ├── drone_trust_engine.py
│   ├── drone_anomaly_detector.py
│   ├── drone_security_engine.py
│   └── generate_drone_data.py
│
├── threat-models/
│
├── app.py
├── requirements.txt
├── SECURITY.md
├── CONTRIBUTING.md
└── README.md

⸻

⚙️ Installation

Clone the repository:

git clone https://github.com/Poojasri08/trustworthy-autonomous-vehicles.git
cd trustworthy-autonomous-vehicles

Install dependencies:

python -m pip install -r requirements.txt

If needed, install the main ML and dashboard libraries:

python -m pip install pandas scikit-learn streamlit

⸻

▶️ Running the Project

Test the drone trust engine

python .\src\drone_trust_engine.py

Test the ML anomaly detector

python .\src\drone_anomaly_detector.py

Test the combined security engine

python -m src.drone_security_engine

Launch the dashboard

python -m streamlit run app.py

The dashboard will normally be available at:

http://localhost:8501

⸻

🧪 Current Dataset

The prototype currently uses simulated data rather than data collected from a physical drone.

The training dataset contains:

* Normal sensor behavior
* GPS/IMU inconsistencies
* Low camera confidence
* Short obstacle distances

This allows the cybersecurity logic and ML pipeline to be tested without requiring physical hardware.

⸻

🔐 Security Focus

The project explores security problems including:

* Sensor spoofing
* Sensor inconsistency
* Data manipulation
* AI anomaly detection
* Trust-aware decision making
* Explainable security decisions

The current implementation is a research and educational prototype, not a production-grade autonomous vehicle security system.

⸻

🚧 Current Limitations

* Sensor data is simulated.
* The dataset is relatively small.
* The trust model is rule-based.
* ML evaluation is currently limited.
* No physical drone hardware is connected.
* No real-time sensor communication is implemented.
* The current model should not be used for safety-critical autonomous decisions.

⸻

🔮 Future Work

Possible future improvements:

* Larger and more realistic datasets
* Real-time sensor streams
* Additional sensor types
* Better anomaly-detection evaluation
* Precision/recall and confusion-matrix analysis
* Adaptive trust thresholds
* Real hardware integration
* Secure communication between sensors
* More advanced explainable-AI techniques

⸻

📚 References

* CARLA Simulator
* Apollo Autonomous Driving Platform
* OWASP security resources
* Scikit-learn documentation
* Streamlit documentation

⸻

📄 License

This project is licensed under the MIT License.