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
            AVG(temperature_c), 
            MAX(temperature_c), 
            MIN(temperature_c) 
        FROM device
    """)
    total, avg_temp, max_temp, min_temp = cur.fetchone()

    print("\n=== Telemetry Historical Summary ===")
    print(f"Total Readouts Recorded: {total}")

    # Guard against an empty database where stats would be None
    if total > 0:
        print("\n--- Temperature Metrics ---")
        print(f"Average Temp: {avg_temp:.2f}°C")
        print(f"Maximum Temp: {max_temp:.2f}°C")
        print(f"Minimum Temp: {min_temp:.2f}°C")
    else:
        print("No historical data found in database.")

    print("====================================\n")

    conn.close()