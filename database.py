import _sqlite3

conn = _sqlite3.connect("telemetry_database.db")

cur = conn.cursor()
cur.execute("CREATE TABLE device(device_id, temperature_c, voltage_kv, optical_loss_db, vibration_g)")