import argparse
import sqlite3

# 1. Setup the CLI parser
parser = argparse.ArgumentParser(description="Industrial Telemetry System")

parser.add_argument(
    "--summary",
    action="store_true",
    help="Display historical summary statistics from the database"
)

parser.add_argument(
    "--db",
    type=str,
    default="telemetry_database.db",
    help="Path to SQLite database file (default: telemetry_database.db)"
)

args = parser.parse_args()

# 2. Check if the user passed --summary
if args.summary:
    conn = sqlite3.connect(args.db)
    cur = conn.cursor()

    # Query the aggregated temperature metrics
    cur.execute("""
        SELECT 
            COUNT(*), 
            MIN(temperature_c), AVG(temperature_c), MAX(temperature_c),
            MIN(voltage_kv), AVG(voltage_kv), MAX(voltage_kv),
            MIN(optical_loss_db), AVG(optical_loss_db), MAX(optical_loss_db),
            MIN(vibration_g), AVG(vibration_g), MAX(vibration_g)
        FROM device
    """)
    (total, min_temp, avg_temp, max_temp,
     min_volt, avg_volt, max_volt,
     min_optical, avg_optical, max_optical,
     min_vibration, avg_vibration, max_vibration) = cur.fetchone()

    print("\n=== Telemetry Historical Summary ===")
    print(f"Total Readouts Recorded: {total}")

    # Guard against an empty database where stats would be None
    if total > 0:
        print("\n--- Temperature Metrics ---")
        print(f"Average Temp: {avg_temp:.2f}°C")
        print(f"Maximum Temp: {max_temp:.2f}°C")
        print(f"Minimum Temp: {min_temp:.2f}°C")

        print("\n--- Voltage Metrics ---")
        print(f"Average Voltage: {avg_volt:.2f}V")
        print(f"Minimum Voltage: {min_volt:.2f}V")
        print(f"Maximum Voltage: {max_volt:.2f}V")

        print("\n--- Optical Loss Metrics ---")
        print(f"Average Optical: {avg_optical:.2f}")
        print(f"Minimum Optical: {min_optical:.2f}")
        print(f"Maximum Optical: {max_optical:.2f}")

        print("\n--- Vibration Metrics ---")
        print(f"Average Vibration: {avg_vibration:.2f}")
        print(f"Minimum Vibration: {min_vibration:.2f}")
        print(f"Maximum Vibration: {max_vibration:.2f}")
    else:
        print("No historical data found in database.")

    print("====================================\n")



    conn.close()