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
 
##### **Final Thought:**
Thus we can conclude that,  **WebSockets should be used for real-time sensor monitoring** to provide **instant updates** on oxygen levels and heart rate for the IOT based healthcare monitioring 
