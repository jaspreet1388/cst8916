# **Final Project Assignment: Real-time Monitoring System for Rideau Canal Skateway**
## **Scenario Description: Rideau Canal Skateway Monitoring**




The Rideau Canal Skateway is one of Ottawa’s most iconic winter attractions, drawing thousands of visitors each season. Ensuring the safety of skaters requires real-time monitoring of environmental conditions such as ice thickness, surface temperature, snow accumulation, and weather data.

This project implements a real-time monitoring system that simulates IoT sensors at key locations along the canal. The system continuously analyzes this data to detect unsafe skating conditions and stores the results for future analysis.
To address this, we can design a real-time monitoring system that simulates IoT sensors which is deployed at key locations along the Rideau Canal (Dow’s Lake, Fifth Avenue, NAC). These sensors collect data about the following parameters every 10 seconds:

Ice Thickness (in cm): Critical for determining whether the ice is thick enough to support skaters.
Surface Temperature (in °C): Helps identify the potential for ice melting, which could be dangerous for skaters.
Snow Accumulation (in cm): Impacts the strength and usability of the ice surface.
External Temperature (in °C): Provides weather context and indicates whether external weather conditions might be a risk.

This system continuously monitors the data from these sensors and processes it in real-time to detect unsafe conditions. The data is then stored in Azure Blob Storage for further analysis.

The key challenge that this system addresses is the real-time monitoring and detection of unsafe ice conditions, which helps authorities take timely actions to ensure skater safety along the Rideau Canal Skateway.


## System Architecture

### Objective:
To continuously monitor ice conditions across multiple locations on the Rideau Canal and determine whether it's safe for public skating — using simulated IoT sensors, real-time data streaming, and cloud-based analytics.

---

## Components:

### 1. IoT Sensor Simulation
Simulated sensors mimic environmental monitoring devices at key locations:
- Dow’s Lake
- Fifth Avenue
- NAC

Each device generates telemetry every 10 seconds:
- `iceThickness` (in cm)
- `surfaceTemperature` (°C)
- `snowAccumulation` (cm)
- `externalTemperature` (°C)
- `timestamp` (ISO 8601)

Devices are registered with Azure IoT Hub and connect securely via the SDK.

---

### 2. Azure IoT Hub (Ingestion Layer)
Azure IoT Hub acts as the message broker:
- Ingests real-time telemetry from all sensors
- Supports device registration and secure authentication
- Routes data to processing endpoints like Stream Analytics
- Uses internal **partitioning** for scalability

---

### 3. Azure Stream Analytics (Processing Layer)
Processes incoming data with a real-time query:
- Input: `rideauinput` (IoT Hub)
- Output: `rideauoutput` (Blob Storage)
- Uses `TumblingWindow(minute, 5)` to group events every 5 minutes by location
- Calculates:
  - `AVG(iceThickness)`
  - `MAX(snowAccumulation)`
 - Outputs structured JSON results to Blob Storage

---

### 4. Azure Blob Storage (Storage Layer)
Stores final processed data:
- Organized by date and location (e.g., `canal-data/2025-04-10/dowslake-17:05.json`)
- JSON format for easy querying and downstream consumption
- Can be used for:
  - Historical analysis
  - Power BI dashboards
  - Trigger-based alerts

---

### 🔁 End-to-End Data Flow

```text
Simulated IoT Sensors
        ↓
 Azure IoT Hub (Device-to-Cloud)
        ↓
Azure Stream Analytics (Real-Time Processing)
        ↓
Azure Blob Storage (Processed Output)

