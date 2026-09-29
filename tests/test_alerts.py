import alerts

def test_temperature_over_threshold():
    # 1. Arrange: Create a dictionary where temperature is clearly over 80.0
    telemetry_data = {
        "device_id": 101,
        "temperature_c": 95.0,  # exceeds MAX_TEMP (80.0)
        "voltage_kv": 12.0,
        "optical_loss_db": 1.0,
        "vibration_g": 0.1
    }

    # 2. Act: Run your alert check
    results = alerts.check_alerts(telemetry_data)

    # 3. Assert: Check if an alert was triggered!
    assert len(results) == 1
    assert "MAX TEMP EXCEEDED" in results[0]

def test_voltage_over_threshold():
    # 1. Arrange: Voltage is high, everything else is normal
    telemetry_data = {
        "device_id": 101,
        "temperature_c": 50.0,
        "voltage_kv": 15.0,  # exceeds MAX_VOLTAGE (12.8)
        "optical_loss_db": 1.0,
        "vibration_g": 0.1
    }

    # 2. Act
    results = alerts.check_alerts(telemetry_data)

    # 3. Assert
    assert len(results) == 1
    assert "MAX VOLTAGE EXCEEDED" in results[0]

def test_optical_over_threshold():
    telemetry_data = {
            "device_id": 101,
            "temperature_c": 50.0,
            "voltage_kv": 12.0,
            "optical_loss_db": 3.1, #exceeds MAX_OPTICAL_LOSS (3.0)
            "vibration_g": 0.1
        }

    results = alerts.check_alerts(telemetry_data)

    assert len(results) == 1
    assert "MAX OPTICAL LOSS EXCEEDED" in results[0]

def test_vibration_over_threshold():
    telemetry_data = {
                "device_id": 101,
                "temperature_c": 50.0,
                "voltage_kv": 12.0,
                "optical_loss_db": 1.0,
                "vibration_g": 0.6 #exceeds the max vibration
            }
    
    results = alerts.check_alerts(telemetry_data)
    
    assert len(results) == 1
    assert "MAX VIBRATION EXCEEDED" in results[0]
