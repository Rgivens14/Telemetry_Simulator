import sqlite3
import database

def test_insert_readout():
    # 1. Arrange: Connect to a temporary in-memory database
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()

    # Create the table schema in memory
    cur.execute("""
        CREATE TABLE device (
            timestamp TEXT,
            device_id INTEGER,
            temperature_c REAL,
            voltage_kv REAL,
            optical_loss_db REAL,
            vibration_g REAL
        )
    """)

    sample_data = {
        "device_id": 505,
        "temperature_c": 72.3,
        "voltage_kv": 12.1,
        "optical_loss_db": 1.8,
        "vibration_g": 0.25
    }

    # 2. Act: Insert the data into our in-memory DB
    database.insert_readout(conn, sample_data)

    # 3. Assert: Query the table and check that the row exists
    cur.execute("SELECT device_id, temperature_c, voltage_kv FROM device")
    row = cur.fetchone()

    # row should be (505, 72.3, 12.1)
    assert row is not None
    assert row[0] == 505
    assert row[1] == 72.3
    assert row[2] == 12.1

    conn.close()