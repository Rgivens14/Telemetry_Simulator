import sqlite3
from datetime import datetime

# Inserting the values that are called
def insert_readout(conn, data):
    cur = conn.cursor()
    timestamp = datetime.now().isoformat()

    values = (
        timestamp,
        data["device_id"],
        data["temperature_c"],
        data["voltage_kv"],
        data["optical_loss_db"],
        data["vibration_g"]
    )

    query = """
        INSERT INTO device (timestamp, device_id, temperature_c, voltage_kv, optical_loss_db, vibration_g)
        VALUES (?, ?, ?, ?, ?, ?)
    """

    #try statement for if the database is locked
    try:
        cur.execute(query, values)
        conn.commit()
    except sqlite3.OperationalError as e:
        print(f"Database error: {e}")

if __name__ == "__main__":
    # Main setup for the script
    conn = sqlite3.connect("telemetry_database.db")
    cur = conn.cursor()

    # Checking for an existing table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS device (
            timestamp TEXT,
            device_id INTEGER,
            temperature_c REAL,
            voltage_kv REAL,
            optical_loss_db REAL,
            vibration_g REAL
        )
    """)

    # Test inserting a fake readout by CALLING the function
    fake_reading = {
        "device_id": 999,
        "temperature_c": 50.0,
        "voltage_kv": 12.0,
        "optical_loss_db": 1.5,
        "vibration_g": 0.1
    }

    insert_readout(conn, fake_reading)

    # Clean up
    conn.close()
    print("Database created and 1 test row inserted successfully!")