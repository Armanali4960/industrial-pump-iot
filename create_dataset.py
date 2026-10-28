import pandas as pd
import random

data = []

for i in range(1000):
    temperature = random.uniform(50, 100)
    pressure = random.uniform(20, 80)
    vibration = random.uniform(1, 10)
    rpm = random.uniform(1000, 3000)

    if temperature > 85 or pressure > 65 or vibration > 7:
        failure = 1
    else:
        failure = 0

    data.append([temperature, pressure, vibration, rpm, failure])

df = pd.DataFrame(data, columns=[
    "temperature", "pressure", "vibration", "rpm", "failure"
])

df.to_csv("data/pump_data.csv", index=False)

print("Dataset created successfully!")