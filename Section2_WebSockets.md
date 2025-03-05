### **Q1: How WebSockets Could Be Used for Real-time Communication in IoT Healthcare Monitoring**  

WebSockets would significantly enhance the IoT healthcare monitoring system by enabling **bi-directional, low-latency communication** between IoT Edge devices, cloud services, and client applications. Unlike REST and GraphQL, which require repeated polling to retrieve new data, WebSockets allow a persistent connection, ensuring **real-time updates** for critical sensor readings like **oxygen levels and heart rate**.
 
#### **Implementation of WebSockets in IoT Healthcare Monitoring**

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

        sensor_reading = {"oxygen_level": 98, "heart_rate": 72}

        await websocket.send(json.dumps(sensor_reading))

        await asyncio.sleep(1)  # Sends data every second
 
start_server = websockets.serve(sensor_data, "localhost", 8765)
 
asyncio.get_event_loop().run_until_complete(start_server)

asyncio.get_event_loop().run_forever()

```

This WebSocket server **continuously streams live sensor data** to clients, ensuring real-time updates.
 
---
 
