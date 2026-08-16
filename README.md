# 🚗🔒 Trustworthy Autonomous Vehicles

## 📌 Overview

Autonomous vehicles use artificial intelligence, sensors, and software to make real-time decisions. However, unreliable sensor readings, sensor inconsistencies, and anomalous behavior can create safety and cybersecurity risks.

This project presents a Trust-Aware Cybersecurity Framework for Autonomous Vehicles. The system combines rule-based sensor trust evaluation with machine-learning anomaly detection to identify potentially unsafe or suspicious vehicle behavior.

The project currently includes both a vehicle monitoring system and a drone security simulation.



## 🎯 Objectives

* Monitor autonomous vehicle and drone sensor data
* Evaluate sensor consistency and reliability
* Calculate trust and risk scores
* Detect anomalous sensor behavior using Machine Learning
* Combine rule-based trust with ML anomaly detection
* Generate NORMAL, SUSPICIOUS, and HIGH RISK security decisions
* Provide a visual monitoring dashboard using Streamlit



## 🏗️ System Architecture

### Processing Pipeline

GPS + IMU + Camera + Distance
              ↓
        Trust Engine
              ↓
       Trust + Risk Score
              ↓
       Isolation Forest
              ↓
        ML Anomaly
              ↓
      Security Engine
              ↓
 NORMAL / SUSPICIOUS / HIGH RISK
              ↓
      Streamlit Dashboard



## 🚁 Drone Security System

### The drone simulation uses multiple sensor inputs:

* GPS speed
* IMU speed
* Camera confidence
* Distance

The system evaluates these values for consistency and reliability.

### Trust Calculation

The Trust Engine calculates a trust score between 0 and 1.

Trust Score ≥ 0.8  → HIGH
Trust Score ≥ 0.5  → MEDIUM
Trust Score < 0.5  → LOW

### Risk Calculation

Risk is calculated from the trust score:

Risk = (1 - Trust Score) × 100



## 🤖 ML Anomaly Detection

The system uses the Isolation Forest algorithm to detect unusual sensor behavior.

### ML Features

The model uses:

* GPS speed
* IMU speed
* Camera confidence
* Distance

### ML Output

NORMAL
ANOMALY



## 📊 ML Performance

The Isolation Forest model was evaluated using 130 labeled sensor samples.

### Classification Results

Metric	NORMAL	ANOMALY
Precision	0.91	0.81
Recall	0.95	0.70
F1-Score	0.93	0.75

### Overall Accuracy

89%

### Confusion Matrix

Actual / Predicted	NORMAL	ANOMALY
NORMAL	95	5
ANOMALY	9	21

### Model Interpretation

The model correctly identified:

* 95 normal samples
* 21 anomalous samples

#### It incorrectly classified:

* 5 normal samples as anomalies
* 9 anomalous samples as normal

This demonstrates that the current model is a working prototype, but further improvement is required before real-world deployment.



## 🛡️ Security Engine

#### The Security Engine combines the Trust Engine result with the ML anomaly result.

### Decision Logic

HIGH Trust + NORMAL
        ↓
     NORMAL
LOW Trust + NORMAL
        ↓
   SUSPICIOUS
HIGH Trust + ANOMALY
        ↓
   SUSPICIOUS
LOW Trust + ANOMALY
        ↓
    HIGH RISK

### Security Decision Levels

|  Trust Level   |    ML Result	    |   Security Status  |
|----------------|------------------|--------------------|
|HIGH	           |  NORMAL	        |NORMAL              |
|LOW	           |  NORMAL	        |SUSPICIOUS          |
|HIGH	           |  ANOMALY	        |SUSPICIOUS          |
|LOW	           |  ANOMALY	        |HIGH RISK           |


This layered approach allows rule-based sensor reliability and ML anomaly detection to contribute to the final security decision.


## 🧪 Integration Testing

The complete security pipeline was tested using controlled high-risk sensor conditions.

### High-Risk Test

LOW TRUST
    +
ML ANOMALY
    ↓
HIGH RISK



## 📸 Project Demo

### 🚨 High-Risk Integration Test

The system detects inconsistent sensor readings and identifies the situation as high risk.

![High-Risk Integration Test](screenshots/test_high_risk.png)

### Test Results

Test Case	Trust Level	ML Result	Security Status
1	LOW	ANOMALY	HIGH RISK
2	LOW	ANOMALY	HIGH RISK
3	LOW	ANOMALY	HIGH RISK

The integration test successfully confirmed the intended high-risk decision logic.



## 📊 Streamlit Dashboard

The Streamlit dashboard provides monitoring for both the vehicle and drone systems.

## 🚗 Vehicle Monitor

### Displays:

* Average Trust
* Average Risk
* Detected Attacks
* Sensor information
* Trust score
* Risk score
* Security status

## 🚁 Drone Monitor

### Displays:

* Average Trust
* Average Risk
* ML Anomalies
* High Risk cases
* Sensor information
* Trust score
* Risk score
* Trust level
* ML anomaly
* Security status
* Explanation/reason



## 🧰 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Isolation Forest
* Streamlit
* Git
* GitHub



## 📁 Project Structure

trustworthy-autonomous-vehicles/
│
├── app.py
├── README.md
│
├── data/
│   ├── sensor_data.csv
│   ├── drone_sensor_data.csv
│   └── drone_training_data.csv
│
├── docs/
│   └── architecture.jpeg
│
└── src/
    ├── security_engine.py
    ├── trust_engine.py
    ├── drone_trust_engine.py
    ├── drone_anomaly_detector.py
    ├── drone_security_engine.py
    ├── generate_drone_data.py
    └── test_high_risk.py



## 🚀 How to Run

#### 1. Install Dependencies

    pip install pandas scikit-learn streamlit

#### 2. Run the ML Anomaly Detector

    python src/drone_anomaly_detector.py

#### 3. Run the Drone Security Engine

    python -m src.drone_security_engine

#### 4. Run the High-Risk Integration Test

    python -m src.test_high_risk

#### 5. Run the Streamlit Dashboard

    python -m streamlit run app.py

  Then open the local Streamlit URL shown in the terminal.



## 🔬 Testing Summary

### Component	Result
Trust calculation	✅ Passed
Risk calculation	✅ Passed
Sensor consistency	✅ Passed
Isolation Forest	✅ Passed
ML anomaly detection	✅ Passed
ML validation	✅ 89% accuracy
Trust + ML integration	✅ Passed
NORMAL decision	✅ Passed
SUSPICIOUS decision	✅ Passed
HIGH RISK decision	✅ Passed
Streamlit dashboard	✅ Passed



## ⚠️ Limitations

This project is a research and educational prototype.

### The current system:

* Uses simulated sensor data
* Uses a relatively small dataset
* Uses a rule-based trust model
* Uses an unsupervised Isolation Forest model
* Has not been tested on a real autonomous vehicle
* Is not suitable for safety-critical deployment

The 89% accuracy should therefore be interpreted as a prototype evaluation result, not evidence of production-level autonomous vehicle security.



## 🔮 Future Improvements

* Real-time sensor integration
* Larger and more diverse datasets
* Advanced sensor fusion
* Adaptive trust models
* Real-time cyberattack detection
* More advanced anomaly detection models
* Explainable AI improvements
* Hardware-based autonomous vehicle testing
* Continuous model evaluation
* Real-world cybersecurity attack datasets



## 📌 Project Status

### Current Status: First Complete ML Prototype ✅

The current implementation demonstrates a complete pipeline from simulated sensor data to:

Sensor Data → Trust Evaluation → ML Anomaly Detection → Security Decision → Streamlit Visualization

The next phase is focused on testing, optimization, documentation, and evaluation, rather than adding unnecessary features.



## 👩‍💻 Project

### Trustworthy Autonomous Vehicles: Cybersecurity & AI Framework

A project exploring how sensor trust evaluation and machine-learning anomaly detection can be combined to improve the security and reliability of autonomous systems.
 
