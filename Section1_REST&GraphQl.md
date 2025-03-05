
**Section 1: REST and GraphQL for Data Requests and Updates**

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
| **Add New Sensor Data** (Equivalent to POST in REST) | ```mutation { addSensorData(oxygen_level: 95, heart_rate: 78) { id oxygen_level heart_rate } }``` |
| **Update Sensor Data** (Equivalent to PUT in REST) | ```mutation { updateSensorData(id: "2", oxygen_level: 97) { id oxygen_level heart_rate } }``` |
| **Delete Sensor Data** (Equivalent to DELETE in REST) | ```mutation { deleteSensorData(id: "2") }``` |
 
✔ **Advantage:** A **single mutation request** can modify or delete data without needing multiple API calls.  
 
---
