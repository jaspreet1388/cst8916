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



### 2. Azure IoT Hub (Ingestion Layer)
Azure IoT Hub acts as the message broker:
- Ingests real-time telemetry from all sensors
- Supports device registration and secure authentication
- Routes data to processing endpoints like Stream Analytics
- Uses internal **partitioning** for scalability



### 3. Azure Stream Analytics (Processing Layer)
Processes incoming data with a real-time query:
- Input: `rideauinput` (IoT Hub)
- Output: `rideauoutput` (Blob Storage)
- Uses `TumblingWindow(minute, 5)` to group events every 5 minutes by location
- Calculates:
  - `AVG(iceThickness)`
  - `MAX(snowAccumulation)`
 - Outputs structured JSON results to Blob Storage



### 4. Azure Blob Storage (Storage Layer)
Stores final processed data:
- Organized by date and location (e.g., `canal-data/2025-04-10/dowslake-17:05.json`)
- JSON format for easy querying and downstream consumption
- Can be used for:
  - Historical analysis
  - Power BI dashboards
  - Trigger-based alerts

![image](https://github.com/user-attachments/assets/ac5aaf57-477a-4c94-9ed7-7b1a753e9897)


### End-to-End Data Flow

```text
Simulated IoT Sensors
        ↓
 Azure IoT Hub (Device-to-Cloud)
        ↓
Azure Stream Analytics (Real-Time Processing)
        ↓
Azure Blob Storage (Processed Output)

```

## **Here are the step by step implemenation:**

For the purpose of implementing the project we need the sensor, IOT Hub and analyzing stream and later on which can be used for the represenation through PowerBI. To implement the project we first need to created the IOT hub with sensors which will recieve the data, this can be created on azure IOT hub, after that we need to simulate the data from the host, data is simulated and with the connection string information, they are updated to the devices on the hub, later that data can be analyzed on the IOT stream analytics job and appropriate information can be derived.



## IoT Sensor Simulation

### Overview:
Three virtual sensors to simulate the environmental monitoring devices located at:
- Dow’s Lake
- Fifth Avenue
- NAC

Each sensor:
- Is generating telemetry data every 10 seconds
- Sends the data to Azure IoT Hub using the **Azure IoT Device SDK for Python**

### JSON Payload Format:
```json
{
  "location": "Dow's Lake",
  "iceThickness": 27,
  "surfaceTemperature": -1.2,
  "snowAccumulation": 8,
  "externalTemperature": -5,
  "timestamp": "2025-04-10T12:00:00Z"
}

```
## Scripts Used:
The script used on the linux to stimulate the data are stored in the **sensor-simulation/** directory of the final project, these are  :

- simulate_dowslake.py

- simulate_fifthavenue.py

- simulate_nac.py

- simulate_sensor.py (shared logic)

- .env file stores device connection strings

## Azure IoT Hub Configuration:
### For the purpose readability, the screenshots of the configuration are included separately under screenshots/ folder

Here are the steps of the configuration followed :
### Azure IoT Hub Configuration

Azure IoT Hub serves as the central message broker for device-to-cloud communication. It collects telemetry data from the simulated IoT sensors and routes it to downstream services such as Azure Stream Analytics.

---

### Step-by-Step Configuration

### 1. Create the IoT Hub

1. Go to the azure portal.
2. Search for **IoT Hub** → Click **+ Create**.
3. In the **Basics** tab:
   - **Subscription**: Choose your Azure subscription.
   - **Resource Group**: Create or select an existing group (e.g., `rideau-rg`).
   - **IoT Hub Name**: The name of the hub (e.g., `rideaucanalhub`).
   - **Region**: Choose a nearby region like `Canada Central`.
4. In the **Tier** section, choose **Standard (S1)** — required for multiple devices and routing.

Click **Review + Create**, then **Create**.

---

### 2. Register IoT Devices

Once the IoT Hub is deployed:

1. Go to your IoT Hub → **Devices**.
2. Click **+ New Device** and add:
   - `DowsLakeDevice`
   - `FifthAvenueDevice`
   - `NACDevice`
3. Leave authentication type as **Symmetric key**.
4. Save each device and copy their **Primary Connection Strings** for use in simulation scripts.

---

### 3. Verify Endpoints

Azure IoT Hub has a built-in Event Hub-compatible endpoint used for routing messages to services like Stream Analytics.

To view:
1. In your IoT Hub, go to **Built-in endpoints**.
2. Review:
   - **Event Hub-compatible name**
   - **Partition count** (default is 4)
   - **Endpoint**: `messages/events` ← This is the default path Stream Analytics listens to.

---

### 4. Configure Message Routing (Optional)

   - Endpoint: default Event Hub endpoint (`messages/events`)

> By default all device messages go to the default endpoint automatically.

## Azure Stream Analytics Job

Azure Stream Analytics (ASA) is used to process telemetry data from IoT devices in real-time. It ingests data from Azure IoT Hub, applies a custom SQL-like query to evaluate skating conditions, and outputs the results to Azure Blob Storage.
For the purpose of simplification the screenshots of the azure stream analytics are inlcuded in the directory **screenshots/Azure_SA_job.pdf**.

**Here are the steps of the configuration :**
---

### Job Configuration Overview

| Configuration Component | Value |
|--------------------------|-------|
| **Job Name**             | `rideaustream` |
| **Streaming Units**      | Minimum `2`, recommended `3+` |
| **Input Source**         | Azure IoT Hub (`rideauinput`) |
| **Output Destination**   | Azure Blob Storage (`rideauoutput`) |
| **Output Format**        | JSON |
| **Windowing**            | Tumbling Window (5-minute interval) |
| **Partition Alignment**  | Input SU count matched to IoT Hub partitions |

---

### Input Configuration (IoT Hub)

- **Alias**: `rideauinput`
- **Source**: Azure IoT Hub
- **Consumer Group**: `$Default`
- **Serialization Format**: JSON
- **Encoding**: UTF-8
- **Timestamp Source**: Use `timestamp` field from device messages

---

### Output Configuration (Blob Storage)

- **Alias**: `rideauoutput`
- **Sink Type**: Azure Blob Storage
- **Container Name**: `canal-data`
- **Output Format**: JSON (CSV optional)
- **Path Pattern**: `skateway/{date}/{location}` (optional but recommended)

---

### Sample Query: 5-Minute Tumbling Window

This query analyzes ice and snow data per location every 5 minutes and determines safety status.
```sql
-- Select the location field from each incoming message
SELECT 
    location,

    -- Calculate the average ice thickness over the 5-minute window
    AVG(iceThickness) AS avgIceThickness,

    -- Find the maximum snow accumulation over the 5-minute window
    MAX(snowAccumulation) AS maxSnowAccumulation,

    -- Output the system-generated timestamp marking the end of the window
    System.Timestamp AS timestamp

-- Define the output target for the processed results
INTO
    rideauoutput  -- This refers to the Blob Storage output alias

-- Define the input source for the stream of data
FROM
    rideauinput   -- This refers to the IoT Hub input alias

-- Group and aggregate the data
GROUP BY
    location,  -- Perform separate aggregations for each location (e.g., Dow’s Lake, NAC, etc.)

    -- Use a TumblingWindow to group events into fixed, non-overlapping 5-minute intervals
    TumblingWindow(minute, 5)

```
### Sample Output : JSON format
```json
{
  "location": "NAC",
  "avgIceThickness": 17.8,
  "maxSnowAccumulation": 13,
  "timestamp": "2025-04-10T14:55:00Z",
}
```

## Azure Blob Storage

Azure Blob Storage is used to **store the processed output** of real-time data from Azure Stream Analytics. The processed data includes safety analysis per location based on ice thickness and snow accumulation.


### Folder Structure and File Organization

The output files are written to a **container** in Azure Blob Storage, commonly named `canal-data` or `rideau-data`.

![image](https://github.com/user-attachments/assets/85f9e05a-6965-40ec-bdc5-047a7a07ba91)

The output is explained in comments as :
```json
{
  "location": "NAC",                 // The sensor location where the data was recorded (e.g., NAC, DowsLake, FifthAvenue)

  "avgIceThickness": 17.8,           // Average ice thickness (in cm) during the 5-minute aggregation window
                                     // Used to assess whether the ice is safe for skating

  "maxSnowAccumulation": 13,         // Maximum snow accumulation (in cm) during the same time window
                                     // High values may indicate poor surface conditions

  "timestamp": "2025-04-10T14:55:00Z", // The end time of the 5-minute tumbling window
                                       // Automatically generated by Azure Stream Analytics using System.Timestamp


}
```

To decrese the complexity so that SU units are not over leveraged, the query doesnot include the safety parameter, which can also be include and the sample for that is :
  ``` json
"condition": "Unsafe"              // A derived label based on safety thresholds:
                                     // Unsafe if ice thickness < 20 cm or snow > 12 cm
```


## Usage Instructions:

This section provides step-by-step guidance for running the IoT sensor simulation, configuring Azure services, and accessing the processed results stored in Azure Blob Storage.

---

### Running the IoT Sensor Simulation

#### Clone the Repository
```bash
git clone finalProject
cd finalProject/sensor-simulation
```
### 2. Install Required Python Dependencies

Install python latest version if required, then install the required packages manually:

```bash
pip install azure-iot-device python-dotenv
```

- `azure-iot-device`: Connects the Python script to Azure IoT Hub
- `python-dotenv`: Loads environment variables from a `.env` file

#### 3. Set Up Environment Variables
Create a `.env` file and paste your IoT Hub device connection strings:

```env
DOWS_LAKE_CONN_STRING="HostName=...;DeviceId=DowsLakeDevice;SharedAccessKey=..."
FIFTH_AVE_CONN_STRING="HostName=...;DeviceId=FifthAvenueDevice;SharedAccessKey=..."
NAC_CONN_STRING="HostName=...;DeviceId=NACDevice;SharedAccessKey=..."
```

#### 4. Run the Simulation Scripts
Open three separate terminal windows or tabs and run each script:

```bash
python simulate_dowslake.py
python simulate_fifthavenue.py
python simulate_nac.py
```

Each script continuously sends telemetry data every 10 seconds to Azure IoT Hub.

---

### Configuring Azure Services: 
Azure services have been explained in detail above, to summarise that here are brief steps : 


#### Azure IoT Hub
- Create an **IoT Hub** (Standard Tier) in Azure.
- Register 3 devices: `DowsLakeDevice`, `FifthAvenueDevice`, and `NACDevice`.
- Copy their **connection strings** and add them to the simulation script `.env` file.

#### Azure Stream Analytics Job
- Create a **Stream Analytics job** in the same region.
- Add **IoT Hub as input** (`rideauinput`), format: JSON.
- Add **Blob Storage as output** (`rideauoutput`), format: JSON.
- Use a 5-minute tumbling window query to process and label safety status.
- Set **Streaming Units** to 2 or more.
- Start the job to begin real-time processing.

#### zure Blob Storage
- Create a **Blob container** (e.g., `rideau-data`).
- Processed data will be stored in **JSON format**


### Sample Output

```json
{
  "location": "NAC",
  "avgIceThickness": 17.8,
  "maxSnowAccumulation": 13,
  "timestamp": "2025-04-10T14:55:00Z",
  "condition": "Unsafe" // this is sample statement which was reduced to simplify the query and SUs
}
```
The sample of simulated data through script :
![image](https://github.com/user-attachments/assets/073d6401-7b4d-4afe-a67e-c0bc0c173e6a)




## Summary of configuration: 

| Task | Description |
|------|-------------|
| Sensor Simulation | Run 3 Python scripts to send data to Azure |
| Azure IoT Hub | Receives data from simulated devices |
| Stream Analytics | Processes and labels unsafe conditions |
| Blob Storage | Stores summarized, structured output in JSON |

## Results

The system successfully simulates real-time environmental monitoring of the Rideau Canal Skateway, processes data in Azure Stream Analytics, and stores summarized insights in Azure Blob Storage for safety evaluation and analysis.

---

### Key Findings

- Data was aggregated every **5 minutes** per location using a **Tumbling Window**.
- **Average ice thickness** and **maximum snow accumulation** were calculated in each time window.
- A safety condition was applied using logic like:
  - `Unsafe` if `AVG(iceThickness) < 20 cm` or `MAX(snowAccumulation) > 12 cm`
  - `Safe` otherwise

---

### Sample Output File (JSON)

A typical processed result file looks like this:

```json
{
  "location": "NAC",
  "avgIceThickness": 17.8,
  "maxSnowAccumulation": 13,
  "timestamp": "2025-04-10T14:55:00Z",
  "condition": "Unsafe" // this is reduced field which was not included in the actual query to reduce the SU units and complexity of query
}
```
The screen shot of the json output files in the container:
![image](https://github.com/user-attachments/assets/3bd54176-6a8c-46cc-aeac-0d0e33fb7dfb)

The screenshot of the actual json output:
![image](https://github.com/user-attachments/assets/0a1bcd18-2375-4cd7-9b31-70aee92ec3b0)

## Reflection

### Challenges Faced

1. **Stream Analytics Job Failing to Start**
   - **Issue**: The Stream Analytics job repeatedly failed due to insufficient Streaming Units (SUs) for the complexity of the query.
   - **Solution**: The query was simplified in phases, and the SU count was gradually increased to match the number of IoT Hub partitions, resolving performance issues.


2. **Query Optimization in Stream Analytics**
   - **Issue**: Writing efficient and low-resource-consuming queries with `GROUP BY`, `AVG`, and `CASE` statements.
   - **Solution**: The query was tested step-by-step starting from `SELECT *`, then incrementally building up to the final logic using tumbling windows and safety conditions.



### Lessons Learned
The important lesson learned is : 
- **Start simple**: Begin with minimal setups and build incrementally.
- **Monitor often**: Azure CLI and portal monitoring tools are essential for real-time debugging.
- **Streaming Units matter**: Always align SU count with input complexity and partition count.


---

### Outcome

Despite the challenges, the system was successfully deployed and validated end-to-end. It provides real-time safety evaluations of ice conditions and offers structured outputs suitable for further analysis, reporting, or automation.















