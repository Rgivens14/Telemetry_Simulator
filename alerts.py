import database
import sqlite3
from datetime import datetime

MAX_TEMP = 80.0
MAX_VOLTAGE = 12.8
MAX_OPTICAL_LOSS = 3.0
MAX_VIBRATION = .5

def log_alert(message):
    timestamp = datetime.now().isoformat()
    log_entry = f"[{timestamp}] {message}\n"
    print(log_entry, end="")  # print to screen
    with open("alerts.log", "a") as f:
        f.write(log_entry)     # write to file

def check_alerts(data):
    triggered = []

    #temp alert
    if data["temperature_c"] > MAX_TEMP:
        msg = (f"MAX TEMP EXCEEDED: {data['temperature_c']}°C (Threshold: {MAX_TEMP}°C)")
        log_alert(msg)
        triggered.append(msg)

    #voltage alert
    if data['voltage_kv'] > MAX_VOLTAGE:
        msg = (f"MAX VOLTAGE EXCEEDED: {data['voltage_kv']}v (Threshold: {MAX_VOLTAGE}v)")
        log_alert(msg)
        triggered.append(msg)

    #optical alert
    if data['optical_loss_db'] > MAX_OPTICAL_LOSS:
        msg = (f"MAX OPTICAL LOSS EXCEEDED: {data['optical_loss_db']} (THRESHOLD: {MAX_OPTICAL_LOSS})")
        log_alert(msg)
        triggered.append(msg)

    #vibration alert
    if data['vibration_g'] > MAX_VIBRATION:
         msg = (f"MAX VIBRATION EXCEEDED {data['vibration_g']} (THRESHOLD: {MAX_VIBRATION})")
         log_alert(msg)
         triggered.append(msg)

    return triggered