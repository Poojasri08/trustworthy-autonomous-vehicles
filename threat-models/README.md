# 🔐 Threat Models

This directory documents cybersecurity threats that may affect autonomous vehicle systems. Each threat model describes the attack, its potential impact, detection approach, and possible mitigation strategies.

## 🚨 1. Sensor Spoofing

**🎯 Threat Description**

Sensor spoofing occurs when an attacker provides false or manipulated information to a vehicle's sensors. This can cause the vehicle to incorrectly understand its surrounding environment.

**⚔️ Attack Scenario**

An attacker attempts to influence sensor readings so that the vehicle receives incorrect information about objects, distances, or environmental conditions.

**⚠️ Potential Impact**

False sensor readings can reduce sensor reliability, lower the system's trust score, and increase the calculated security risk.

**🔍 Detection Approach**

The system compares sensor readings and identifies unusual or inconsistent values. Suspicious readings may result in anomaly detection and a security alert.

**🛡️ Mitigation**

Using multiple sensors, checking consistency between sensor readings, and reducing trust in unreliable data can help limit the impact of sensor spoofing.

---

## 🧪 2. Sensor Data Tampering

**🎯 Threat Description**

Sensor data tampering occurs when legitimate sensor information is modified before it is processed by the vehicle's security or decision-making system.

**⚔️ Attack Scenario**

An attacker changes sensor values so that the processed data no longer represents the actual environment.

**⚠️ Potential Impact**

Tampered data can produce incorrect trust and risk scores and may cause the system to make decisions using unreliable information.

**🔍 Detection Approach**

The system can monitor sensor values for unexpected changes and compare related measurements to identify inconsistencies.

**🛡️ Mitigation**

Data validation, integrity checks, sensor cross-validation, and continuous monitoring can reduce the risk of undetected tampering.

---

## 📡 3. Communication Attacks

**🎯 Threat Description**

Communication attacks target the exchange of information between vehicle components, sensors, or connected systems.

**⚔️ Attack Scenario**

An attacker attempts to interfere with communication by modifying, delaying, or disrupting information exchanged between system components.

**⚠️ Potential Impact**

Communication problems can result in missing or outdated information and may reduce the reliability of vehicle decisions.

**🔍 Detection Approach**

The system can monitor communication behavior for unexpected delays, missing messages, or unusual data patterns.

**🛡️ Mitigation**

Secure communication protocols, authentication, integrity checks, and continuous monitoring can help protect communication channels.

---

## 📊 4. False Sensor Input

**🎯 Threat Description**

False sensor input occurs when a sensor provides information that conflicts significantly with information from another sensor.

**⚔️ Attack Scenario**

A sensor reports a value that does not agree with another available measurement. This may indicate a faulty sensor, abnormal behavior, or a potential attack.

**⚠️ Potential Impact**

Sensor disagreement can reduce confidence in the affected data and increase the calculated risk level.

**🔍 Detection Approach**

The prototype compares camera confidence and LiDAR-related measurements to identify inconsistent sensor behavior.

**🛡️ Mitigation**

The system can reduce trust in inconsistent readings, compare information from multiple sensors, and generate an alert when significant disagreement is detected.

---

## 🤖 5. AI Decision Manipulation

**🎯 Threat Description**

AI decision manipulation occurs when an attacker attempts to influence the data or conditions used by an AI-based vehicle system.

**⚔️ Attack Scenario**

An attacker provides misleading or manipulated inputs that may influence the AI system's interpretation or decision-making process.

**⚠️ Potential Impact**

Manipulated inputs can reduce confidence in AI decisions and increase the risk of incorrect system behavior.

**🔍 Detection Approach**

Monitoring input consistency, sensor trust, anomaly indicators, and risk scores can help identify suspicious conditions affecting AI-based decisions.

**🛡️ Mitigation**

Input validation, anomaly detection, sensor cross-checking, explainable alerts, and continuous monitoring can improve the reliability of AI-assisted decisions.

---

## 📌 Project Scope

These threat models describe simulated cybersecurity scenarios for the current prototype.

The project uses simulated sensor data and rule-based detection. It is not intended to represent a production autonomous vehicle security system.
