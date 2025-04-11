import time
import json
import random
import os
from datetime import datetime
from dotenv import load_dotenv
from azure.iot.device import IoTHubDeviceClient, Message

load_dotenv()

def simulate_sensor_data(location):
    return {
        "location": location,
        "iceThickness": random.randint(15, 35),  # in cm
        "surfaceTemperature": round(random.uniform(-10, 2), 1),  # in °C
        "snowAccumulation": random.randint(0, 20),  # in cm
        "externalTemperature": round(random.uniform(-20, 5), 1),  # in °C
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

def run_simulation(location, conn_string):
    device_client = IoTHubDeviceClient.create_from_connection_string(conn_string)

    print(f"🚀 Starting simulation for {location}... Press Ctrl+C to stop.")

    try:
        while True:
            data = simulate_sensor_data(location)
            message = Message(json.dumps(data))
            device_client.send_message(message)
            print(f"[{location}] Sent: {data}")
            time.sleep(10)
    except KeyboardInterrupt:
        print(f"\n🛑 Simulation for {location} stopped.")
    finally:
        device_client.shutdown()

