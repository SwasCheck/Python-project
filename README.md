# 📊 Factory Efficiency Dashboard — Power BI Project

#  Overview
This project simulates a **smart factory dashboard** that helps monitor machine efficiency and environmental performance in real-time using **Power BI**. It includes visualizations for:
- Machine uptime
- Energy consumption
- Units produced
- Temperature
- Alert flags for maintenance issues

---

#🧠 Key Features

- **Real-time-style data** using hourly timestamps
- ⚠️ **Alert system** for overheating machines (`Temperature > 45°C`)
- 📉 Line chart for energy trends
- 📊 Bar chart for production comparison
- 🟢 Card visuals for summary stats
- 🎛️ Slicers for machine and time filtering
- 🚨 Conditional formatting to highlight performance issues

---

##🧪 Dataset

- **Generated with Python** using the `pandas`, `numpy`, and `datetime` libraries
- Includes 5 machines (`M1`–`M5`)
- Simulated for 72 hours (3 days)
- Data points:
  - `Timestamp`
  - `Machine_ID`
  - `Uptime (%)`
  - `Energy_Consumed (kWh)`
  - `Units_Produced`
  - `Temperature (°C)`
  - `Alert` (DAX-generated)

📁 Files:

factory_dataset_generated_by_python.xlsx — Clean dataset
factory_data_generator.py — Python script used to generate the data
factory_dashboard.pbix - Power B1 


---

## 🛠 Tools Used

| Tool        | Purpose                      |
|-------------|------------------------------|
| Power BI    | Dashboard & visual analytics |
| Python      | Data simulation (pandas, numpy, datetime) |
| Excel       | Data import/export format    |

---

## 📸 Dashboard Layout
------------------------------------------------------
|  Total Units  | Avg Temp | Avg Uptime             |
------------------------------------------------------
|  Energy Consumption (Line Chart)                  |
------------------------------------------------------
|  Units Produced by Machine (Bar Chart)            |
------------------------------------------------------
|  Table: Machine, Uptime, Temp, Alert (Color-coded)|
------------------------------------------------------
|  Slicers: Machine ID | Timestamp (range)          |
------------------------------------------------------

