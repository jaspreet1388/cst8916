### Real-Time IoT Monitoring System for Heart Rate and Oxygen Sensors 

**Objective:** To understand the design, components, and working of a real-time IoT-based monitoring system for heart rate and oxygen sensors, along with its applications in healthcare.

Introduction With advancements in the Internet of Things (IoT), real-time health monitoring systems have become an essential part of modern healthcare. This assignment focuses on an IoT-based system that continuously tracks heart rate and oxygen saturation (SpO2) levels, enabling remote patient monitoring and real-time alerts.

## **1. System Components for IOT monitoring **

**a. Wearable Sensors** Heart Rate Sensor (PPG, ECG): Measures beats per minute (BPM). Oxygen Sensor (SpO2, Pulse Oximeter): Measures blood oxygen saturation levels.
These sensors are embedded in smartwatches, fitness bands, or medical-grade devices.

**b. Microcontroller/Edge Device**
Examples: ESP32, Raspberry Pi, or any IoT-enabled medical device.
Collects raw sensor data and processes it before transmission.

**c. Communication Module**
Wireless Protocols: Bluetooth, Wi-Fi, LoRa, Zigbee, or NB-IoT.
Ensures secure and efficient data transfer.

**d. Cloud/Edge Computing**
Cloud Platforms: Azure IoT Hub, AWS IoT Core, Google Cloud IoT.
Processes real-time data, applies analytics, and detects anomalies.
Edge computing may be utilized for fast, low-latency processing.

**e. Database & Storage**
Time-Series Databases: InfluxDB, Firebase, or Azure Cosmos DB.
Stores historical data for analysis and predictive modeling.

**f. Real-Time Dashboard & Alerts**
Visualization Tools: Power BI, Grafana, or a custom web dashboard.
Alerts: Sends SMS, emails, or notifications if vitals cross predefined thresholds.
AI/ML Integration: Detects abnormal patterns indicating potential health issues.

## **2. System Workflow:**
**a. Data Acquisition:** Sensors capture heart rate and SpO2 data.

**b. Edge Processing:** Microcontroller filters noise and formats data.

**c. Data Transmission:** Securely sent via Bluetooth/Wi-Fi to cloud servers.

**d. Cloud Analytics:** AI algorithms detect irregularities (e.g., arrhythmia, hypoxia).

**e. Real-Time Alerts:** Notifications triggered in case of abnormal readings.

**f. Data Visualization:** Healthcare professionals and patients monitor trends on dashboards.

**g. Long-Term Analysis:** Predictive analytics identify risks over time.

## **3. Use Cases for IOT monitoring system:**
**a. Remote Patient Monitoring:** Helps doctors track chronic patients remotely.

**b. Athlete Performance Tracking:** Monitors vitals during training sessions.

**c. Elderly Care:** Alerts caregivers in case of abnormal vitals.

**d. Hospital ICUs:** Enables real-time tracking of multiple patients.

### **Section 1: REST and GraphQL for Data Requests and Updates**

In IoT healthcare monitoring, REST API facilitates data exchange using standard HTTP methods. A GET request retrieves real-time oxygen and heart rate data from an IoT Edge device, while a POST request sends new sensor data to Azure IoT Hub. A PUT request updates existing sensor values, ensuring accuracy, and a DELETE request removes outdated data. REST follows a stateless architecture, making each request independent, supporting caching for efficiency, and integrating with Azure API Management (APIM) for secure external access.
IoT Edge devices can host a REST API using FastAPI or Flask, enabling mobile and web apps to access real-time data. Azure Functions or Web Apps expose processed IoT Hub data via secure APIs. An Azure Function API allows external applications to retrieve sensor readings efficiently. The setup includes an IoT Edge REST API, Azure API Gateway, and an Azure Function API, ensuring scalability, security, and real-time monitoring with potential containerized deployments on Azure IoT Edge.

**Using REST API for Data Requests and Updates**
**REST API Structure**
REST APIs follow a **resource-based URL structure** with multiple endpoints for different data operations.
 
### **REST API Endpoints**
| HTTP Method | Endpoint | Purpose |
|------------|----------|---------|
| **GET** | `/sensor-data` | Fetch all sensor data |
| **GET** | `/sensor-data/{id}` | Fetch specific sensor data by ID |
| **POST** | `/sensor-data` | Upload new sensor data |
| **PUT** | `/sensor-data/{id}` | Update existing sensor data |
| **DELETE** | `/sensor-data/{id}` | Delete specific sensor data |
 
---


**GraphQL for Handling Data Operations**
GraphQL provides a single endpoint (/graphql) that allows clients to request exactly the data they need using queries (for retrieving data) and mutations (for modifying data). Unlike REST, which requires multiple endpoints for different operations, GraphQL enables flexible and batch requests through a single query for the heart rate and oxygen sensor data for the IOT healthcare monitoring system.

## GraphQL Queries (Retrieving Data)  
Queries in GraphQL work like **GET requests in REST**, allowing clients to fetch **specific fields** instead of retrieving the full dataset.  
 
| **Operation** | **GraphQL Query** |
|--------------|------------------|
| **Fetch Sensor Data** (Equivalent to GET in REST) | ```query { getSensorData(id: "1") { oxygen_level heart_rate } }``` |
 
**Advantage:** Clients receive **only the requested fields**, reducing unnecessary sensor  data transfer.  
 
---
 
## GraphQL Mutations (Modifying Data)  
Mutations handle **POST, PUT, and DELETE** operations by modifying data on the server.  
 
| **Operation** | **GraphQL Mutation** |
|--------------|------------------|
| **Add New Sensor Data** (Equivalent to POST in REST) | ```mutation { addSensorData(oxygen_level, heart_rate) { id oxygen_level heart_rate } }``` |
| **Update Sensor Data** (Equivalent to PUT in REST) | ```mutation { updateSensorData(id, oxygen_level) { id oxygen_level heart_rate } }``` |
| **Delete Sensor Data** (Equivalent to DELETE in REST) | ```mutation { deleteSensorData(id) }``` |
 
**Advantage:** A **single mutation request** can modify or delete information collected from the sensors without needing multiple API calls.  


---
 
### Which One is Better for IoT Healthcare Monitoring
 
| **Use Case** | **Preferred Method** | **Reason** |
|-------------|---------------|---------|
| **Simple IoT Data Retrieval (Heart Rate & Oxygen Levels)** | REST API | Easier to implement, well-supported, efficient for simple data retrieval |
| **Low Bandwidth IoT Devices (e.g., Wearable Health Trackers)** | GraphQL | Fetch **only required fields**, reducing **network traffic** |
| **Real-Time Patient Monitoring (ICU, Home Health Devices)** | GraphQL | **Subscriptions** push data **instantly** when new sensor readings are available |
| **Large-Scale IoT Deployment (Hospitals, Healthcare Networks)** | REST API | More **scalable**, better **caching**, and **efficient batch processing** |
| **Complex Queries (Multiple Sensor Types, AI/Analytics, Patient Data Aggregation)** | GraphQL | Query **multiple sensor readings** with a **single request** |
 
---
 
---
### **Section2:  WebSockets for Real-time Communication** 

WebSockets would significantly enhance the IoT healthcare monitoring system by enabling **bi-directional, low-latency communication** between IoT Edge devices, cloud services, and client applications. Unlike REST and GraphQL, which require repeated polling to retrieve new data, WebSockets allow a persistent connection, ensuring **real-time updates** for critical sensor readings like **oxygen levels and heart rate**.
 
**Implementation of WebSockets in IoT Healthcare Monitoring**

1. **Establishing a WebSocket Connection:**  

   - A WebSocket server runs on the IoT Edge device or a cloud service.

   - Clients (web apps, mobile apps) establish a WebSocket connection to receive live sensor data.

2. **Continuous Streaming of Sensor Data:**  

   - The IoT Edge device continuously streams **oxygen level and heart rate** data to connected clients.

   - Clients **receive instant updates** instead of making repeated GET requests.
 
3. **Event-driven Data Transmission:**  

   - Instead of polling REST endpoints, **WebSockets push new data** only when the sensor detects changes.

   - The WebSocket server can **broadcast alerts** when oxygen levels drop below a critical threshold.
 
4. **Two-way Communication for Control & Alerts:**  

   - Doctors or system admins can send commands (e.g., reset device, request additional data) via WebSockets.

   - The IoT Edge device can respond **immediately**, enhancing responsiveness.
 
#### **Example WebSocket Implementation:**

```python

import asyncio

import websockets

import json
 
async def sensor_data(websocket, path):

    while True:

        # Simulating real-time sensor data

        sensor_reading = {"oxygen_level", "heart_rate"}

        await websocket.send(json.dumps(sensor_reading))

        await asyncio.sleep(1)  # Sends data  every second
 
start_server = websockets.serve(sensor_data_oxygen_heartRate, "localhost", port_number)
 
asyncio.get_event_loop().run_until_complete(start_server)

asyncio.get_event_loop().run_forever()

```

This WebSocket server **continuously streams live sensor data** to clients, ensuring real-time updates.
 
---
**Exploring WebSockets Differ from REST and GraphQL in Managing Real-time Data Flow in IoT Healthcare Monitoring**
 
**IoT healthcare monitoring system** while using the **REST and GraphQL** for data retrieval and updates have limitations. However, both the limitations could be handled by using the websockets which provides the **real-time communication**, making **WebSockets a more suitable alternative** for streaming continuous sensor data for frequent updates.
 
#### **1. REST vs. WebSockets for Real-time IoT sensor Data**
| Feature | REST | WebSockets |
|---------|------|-----------|
| **Communication Type** | Request-response (stateless) | Persistent, bi-directional |
| **Real-time Capability** | Requires frequent polling (e.g., multiple `GET /sensor-data` requests) | Continuous, event-driven updates (e.g., real-time heart rate & oxygen levels) |
| **Efficiency** | High network overhead due to repeated requests | Low latency as data is pushed only when updates occur |
| **Use Case** | Retrieving stored sensor data at intervals | Streaming live sensor data for real-time monitoring |
 
##### **Example in IoT Healthcare Monitoring**
- In  **REST-based setup** for the IOT monitoring system, a client fetches oxygen and heart rate data using:  
  ```http
  GET /sensor-data
  ```
  This request has to be repeated periodically to get **new readings**.
- **WebSockets solve this issue** by **pushing** updates automatically:
  ```python
  await websocket.send(json.dumps({"oxygen_level", "heart_rate"}))
  ```
  This **removes the need for polling**, reducing **API load** and **latency**.
 
---
 
#### **2. GraphQL vs. WebSockets for Real-time IoT Data**
| Feature | GraphQL | WebSockets |
|---------|---------|-----------|
| **Query Flexibility** | Clients request specific fields (e.g., `{ getSensorData(id: "1") { oxygen_level } }`) | Streams live updates without needing queries |
| **Real-time Data Handling** | Uses **subscriptions**, but still requires request-response for queries | Continuous streaming with **push-based updates** |
| **Efficiency** | Reduces over-fetching but needs polling for updates | **Zero polling**, as changes trigger automatic updates |
| **Use Case** | Requesting specific sensor data fields efficiently | **Instant updates** when oxygen levels or heart rate change |
 
##### **Example in IoT Healthcare Monitoring**
- In your **GraphQL setup**, a client would use a query to fetch real-time data:
  ```graphql
  subscription {
    sensorData {
      oxygen_level
      heart_rate
    }
  }
  ```
  This **requires a subscription setup**, but still depends on a request-response model.
 
- With **WebSockets**, the **server continuously streams updates** whenever a new reading is available, reducing **latency and bandwidth use**.
 
---
 
### **Comparison between REST, GraphQL and Websockets for IoT Healthcare Monitoring**
| Scenario | Best Approach |
|----------|--------------|
| **Fetching past sensor data (e.g., stored records)** | REST or GraphQL |
| **Requesting only specific fields** | GraphQL |
| **Real-time monitoring of oxygen & heart rate** | WebSockets |
 

Thus we can conclude that,  **WebSockets should be used for real-time sensor monitoring** to provide **instant updates** on oxygen levels and heart rate for the IOT based healthcare monitioring 

---
 
---
### **Section 3: Technology Recommendation and Justification**

**Recommended Technology Approach**
Based on the analysis of **REST, GraphQL**, and **WebSockets** from Sections 1 and 2, we have come to conclusion that a **hybrid approach combining WebSockets with REST API** is best for  **IoT healthcare monitoring system**.
 
- **WebSockets** should be used for real-time **continuous streaming of critical sensor data** (e.g., **oxygen levels and heart rate**) to enable **instant updates** without polling overhead.
- **REST API** should be used for **non-real-time data retrieval, historical sensor records, configuration management, and user interactions** that don’t require live updates.
 
---
 
 ### **Justification for the Hybrid Approach**
**1. Real-time Data Streaming with WebSockets**
- The **primary requirement of IoT healthcare monitoring** is to ensure **continuous and instant updates** from sensors **without delays**.
- **REST and GraphQL require polling**, which increases **network load and latency**, whereas **WebSockets maintain a persistent, low-latency connection**.
- **Example:** If a patient’s **oxygen level drops suddenly**, a **WebSocket-based push notification** can alert doctors instantly instead of waiting for the next REST request.
 
**2. Efficient Data Management with REST API**
- **REST API remains useful for non-real-time operations**, such as:
  - Retrieving **historical sensor data** for analysis.
  - **User authentication and device configurations**.
  - **Storing and updating patient records** in a structured database.
- **Example:** A doctor can request **past 24-hour oxygen level trends** using REST instead of receiving continuous WebSocket updates.
 
#### **3. Scalability and Performance Considerations**
- **WebSockets are ideal for high-frequency real-time data updates**, but they are **resource-intensive**.
- **REST API complements WebSockets** by handling **bulk data retrieval**, reducing server load and ensuring scalability.
- The hybrid approach allows **scalable deployment**—**WebSockets for active patient monitoring** and **REST for data access**.
 
---
 
### Reason why Hybrid Approach Best for Performance, Scalability, and Real-time in IOT healthcare monitoring is best suited 
| **Factor** | **Why Hybrid Approach Works** |
|------------|--------------------------------|
| **Performance** | WebSockets ensure **low-latency real-time updates**, while REST handles **efficient batch data retrieval**. |
| **Scalability** | REST API can be **horizontally scaled** for handling **large data storage and queries**, while WebSockets can be optimized for **selective real-time monitoring**. |
| **Real-time Capabilities** | WebSockets **eliminate the need for polling**, enabling **instant push-based updates** for sensor alerts. |
| **Efficiency** | REST API reduces unnecessary **real-time network usage**, improving overall **resource efficiency**. |
 
---
 
### **Final Conclusion**
The **WebSockets + REST hybrid approach** ensures **instantaneous real-time alerts** for **critical sensor readings** while maintaining a **scalable and structured API for broader system management**. This balances **performance, efficiency, and real-time requirements**, making it the optimal choice for the **IoT healthcare monitoring system**.
