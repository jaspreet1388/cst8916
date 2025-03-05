
### **Section 1: REST and GraphQL for Data Requests and Updates**

In the IoT healthcare monitioring  scenario, REST API manages data requests and updates using standard HTTP methods. A GET request (/sensor-data) retrieves real-time oxygen and heart rate data from the IoT Edge device, while a POST request (/sensor-data) allows new sensor data to be sent to Azure IoT Hub. To modify an existing record, a PUT request (/sensor-data/{id}) updates specific sensor values, ensuring data accuracy. If invalid or old data needs removal, a DELETE request (/sensor-data/{id}) deletes the specific entry. REST follows a stateless architecture, making each request independent. It supports caching for efficiency and integrates with Azure API Management (APIM) for secure external access. REST's structured endpoints make it simple, scalable, and suitable for handling IoT data efficiently.

The IoT Edge device can host a REST API to expose real-time sensor data, allowing external clients like mobile apps, web apps, and cloud services to request data via HTTP. Azure API Management (APIM) ensures secure external access, while Azure Functions or Web Apps expose an API to fetch processed data from Azure IoT Hub. Running a lightweight web server (FastAPI or Flask) enables real-time data retrieval. A Python-based REST API allows clients to access oxygen level and heart rate readings through GET requests.

To integrate IoT Edge data with the cloud, an Azure Function API can expose IoT Hub data for external applications. This API handles HTTP requests, delivering processed sensor data through a secure API URL. The architecture includes an IoT Edge REST API for local access, an Azure API Gateway for secure exposure, and an Azure Function API for external requests. This scalable and efficient setup supports real-time monitoring, data security, and potential containerized deployments on Azure IoT Edge.

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
 
### ** Which One is Better for IoT Healthcare Monitoring?**  
 
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
 
### **Reason why Hybrid Approach Best for Performance, Scalability, and Real-time in IOT healthcare monitoring is best suited **
| **Factor** | **Why Hybrid Approach Works** |
|------------|--------------------------------|
| **Performance** | WebSockets ensure **low-latency real-time updates**, while REST handles **efficient batch data retrieval**. |
| **Scalability** | REST API can be **horizontally scaled** for handling **large data storage and queries**, while WebSockets can be optimized for **selective real-time monitoring**. |
| **Real-time Capabilities** | WebSockets **eliminate the need for polling**, enabling **instant push-based updates** for sensor alerts. |
| **Efficiency** | REST API reduces unnecessary **real-time network usage**, improving overall **resource efficiency**. |
 
---
 
### **Final Conclusion**
The **WebSockets + REST hybrid approach** ensures **instantaneous real-time alerts** for **critical sensor readings** while maintaining a **scalable and structured API for broader system management**. This balances **performance, efficiency, and real-time requirements**, making it the optimal choice for the **IoT healthcare monitoring system**.
