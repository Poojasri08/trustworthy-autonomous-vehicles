Threat Models



This directory documents potential cybersecurity threats affecting autonomous vehicle systems and the security risks considered in this prototype.



Threat Categories



1\. Sensor Spoofing



An attacker may provide false or manipulated sensor readings.



Example: Camera and LiDAR measurements disagree significantly.



Potential impact: Incorrect perception of the vehicle’s surroundings.



Detection in this prototype: Sensor consistency checks and trust scoring.



2\. Low-Confidence Sensor Data



A sensor may produce readings with unusually low confidence.



Example: Camera confidence falls significantly below normal levels.



Potential impact: Reduced reliability of the vehicle’s perception system.



Detection in this prototype: Camera confidence is included in the trust and risk assessment.



3\. Sensor Manipulation



An attacker may manipulate sensor values to make the vehicle’s environment appear different from reality.



Potential impact: Unsafe or incorrect system decisions.



Detection in this prototype: Cross-sensor comparison and anomaly detection.



Prototype Response



The current prototype does not automatically prevent an attack. Instead, it:



1\. Processes sensor readings.

2\. Checks for inconsistencies and anomalies.

3\. Calculates a trust score.

4\. Calculates a risk score.

5\. Assigns a security status.

6\. Provides an explanation for suspicious samples.



Limitations



This is a rule-based prototype using a simulated dataset. It is not a production autonomous-vehicle security system and has not been validated against real vehicle data or real-world attacks.

