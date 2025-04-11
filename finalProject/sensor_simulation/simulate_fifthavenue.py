from simulate_sensor import run_simulation
import os

location = "Fifth Avenue"
conn_string = os.getenv("FIFTH_AVE_CONN_STRING")

run_simulation(location, conn_string)

