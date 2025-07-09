
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Define time range (hourly data for 3 days)
start_time = datetime(2025, 7, 1, 0, 0)
timestamps = [start_time + timedelta(hours=i) for i in range(72)]

# Define machine IDs
machines = ['M1', 'M2', 'M3', 'M4', 'M5']

# Generate synthetic factory data
data = []
for ts in timestamps:
    for machine in machines:
        uptime = np.random.uniform(80, 100)  # uptime in %
        energy = np.random.uniform(20, 40)   # energy consumed in kWh
        units = np.random.randint(80, 150)   # units produced
        temp = np.random.uniform(35, 50)     # temperature in °C
        data.append([
            ts.strftime('%Y-%m-%d %H:%M'),
            machine,
            round(uptime, 2),
            round(energy, 2),
            units,
            round(temp, 2)
        ])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    "Timestamp", "Machine_ID", "Uptime (%)",
    "Energy_Consumed (kWh)", "Units_Produced", "Temperature (°C)"
])

# Save to Excel
df.to_excel("factory_dataset_generated_by_python.xlsx", index=False)
