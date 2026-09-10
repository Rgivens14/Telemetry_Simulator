import subprocess #use .Popen to get instant output
import json #

#you will need to create a monitor. Use the subproccess to run the simulator
#make sure that the compile output is converted to its text form

process = subprocess.Popen(
    ["./telemetry_sim"],
    stdout=subprocess.PIPE,
    text=True
)

MAX_TEMP = 85.0
MAX_VIBRATION = 75.0
MAX_VOLTAGE = 125.25

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

print(f"{GREEN}[OK]{RESET} System normal")
print(f"{RED}[ALERT]{RESET} High temperature detected!")

for line in process.stdout:
    line = line.strip()
    #print("Received raw line:", line)

    try:
        json_data = json.loads(line)
        temp = json_data["temperature_c"]
        print(temp)

    except (json.JSONDecodeError, KeyError) as e:
        print(f"Error processing telemetry line: {e}")
