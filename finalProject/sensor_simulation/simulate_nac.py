from simulate_sensor import run_simulation
import os

location = "NAC"
conn_string = os.getenv("NAC_CONN_STRING")

run_simulation(location, conn_string)

