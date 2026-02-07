import numpy as np
from sklearn.ensemble import IsolationForest
import time

# --- CONFIGURATION ---
SYSTEM_NAME = "EdgeVigil Sentry Node #01"
# Healthy machine baseline calibration data
BASELINE_DATA = np.random.normal([0.5, 12.0, 45.0], [0.05, 0.2, 2.0], (500, 3))

# --- CALIBRATION ---
print(f"[{SYSTEM_NAME}] Calibrating Edge Model...")
model = IsolationForest(contamination=0.02, random_state=42)
model.fit(BASELINE_DATA)
print(f"[{SYSTEM_NAME}] Monitoring Active.\n")

# --- SIMULATE SENSOR FEED ---
def get_sensor_reading(fault=False):
    if not fault:
        return np.random.normal([0.5, 12.0, 45.0], [0.05, 0.2, 2.0])
    return [1.8, 12.8, 68.0] # Simulating high vibration & heat

# --- EXECUTION LOOP ---
for i in range(6):
    is_fault = (i == 5) 
    sample = get_sensor_reading(is_fault)
    score = model.decision_function([sample])[0]

    print(f"FEED: Vib={sample[0]:.2f}G | Current={sample[1]:.2f}A | Temp={sample[2]:.1f}C | Score={score:.3f}")

    if score < -0.5:
        print("\n>>> 🚨 CRITICAL ANOMALY DETECTED!")
        print(">>> [PRESCRIPTION]: Lubrication failure. Grease bearings immediately.")
        print(">>> [GREEN INTEGRITY]: Preventing 22.5kg CO2 waste.\n")
