import argparse
import sqlite3

# 1. Setup the CLI parser
parser = argparse.ArgumentParser(description="Industrial Telemetry System")

parser.add_argument(
    "--summary",
    action="store_true",
    help="Display historical summary statistics from the database"
)

args = parser.parse_args()

# 2. Check if the user passed --summary
if args.summary:
    conn = sqlite3.connect("telemetry_database.db")
    cur = conn.cursor()

    # Query the aggregated temperature metrics
    cur.execute("""
        SELECT 
            COUNT(*), 
            AVG(temperature_c), MAX(temperature_c), MIN(temperature_c),
            AVG(voltage_kv), MAX(voltage_kv), MIN(voltage_kv),
            AVG(optical_loss_db), MAX(optical_loss_db), MIN(optical_loss_db)
        FROM device
    """)
    (total, avg_temp, max_temp, min_temp,
     avg_volt, max_volt, min_volt,
     min_optical, max_optical, avg_optical) = cur.fetchone()

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

    else:
        print("No historical data found in database.")

    print("====================================\n")



    conn.close()