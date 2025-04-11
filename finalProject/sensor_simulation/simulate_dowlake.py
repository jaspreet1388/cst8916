from simulate_sensor import run_simulation
import os

location = "Dow's Lake"
conn_string = os.getenv("DOWS_LAKE_CONN_STRING")

run_simulation(location, conn_string)

