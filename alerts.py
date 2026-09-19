import database
import sqlite3

MAX_TEMP = 80.0
MAX_VOLTAGE = 12.8
MAX_OPTICAL_LOSS = 3.0
MAX_VIBRATION = .5

def check_alerts(data):
    if data["temperature_c"] > MAX_TEMP:
        alert = f"Max Temp of {MAX_TEMP} has exceeded to {data['temperature_c']}"
        print(alert)

        with open("alerts.log", "a") as f: #use "a" since "w" keeps overwriting the previous records
            f.write(alert + "\n")