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

GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

for line in process.stdout:
    line = line.strip()

    try:
        json_data = json.loads(line)

        device_id = json_data["device_id"]
        print(f"Device ID: {device_id}")

        temp = json_data["temperature_c"]
        if temp <= 60.00:
            print(f"Temperature: {temp} {GREEN}[OK]{RESET}")
        elif 60.00 <= temp <= 85.00:
            print(f"Temperature: {temp} {YELLOW}[WARN]{RESET}")
        else:
            print(f"Temperature: {temp} {RED}[CRITICAL]{RESET}")

        voltage_kv = json_data["voltage_kv"]
        if voltage_kv <= 20.25:
            print(f"Voltage: {voltage_kv} {GREEN}[OK]{RESET}")
        elif 20.26 <= voltage_kv <= 100.25:
            print(f"Voltage: {voltage_kv} {YELLOW}[WARN]{RESET}")
        else:
            print(f"Voltage: {voltage_kv} {RED}[CRITICAL]{RESET}")

        optical_loss_db = json_data["optical_loss_db"]
        if optical_loss_db < 20.00:
            print(f"Optical DB: {optical_loss_db} {GREEN}[OK]{RESET}")
        elif 20.00 <= optical_loss_db <= 25.00:
            print(f"Optical DB: {optical_loss_db} {YELLOW}[WARN]{RESET}")
        else:
            print(f"Optical DB: {optical_loss_db} {RED}[CRITICAL]{RESET}")

        vibration_g = json_data["vibration_g"]
        if vibration_g < 15.00:
            print(f"Vibration: {vibration_g} {GREEN}[OK]{RESET}")
        elif 15.00 <= vibration_g <80.00:
            print(f"Vibration: {vibration_g} {YELLOW}[WARN]{RESET}")
        else:
            print(f"Vibration: {vibration_g} {RED}[CRITICAL]{RESET}")
    
    except (json.JSONDecodeError, KeyError) as e:
        print(f"Error processing telemetry line: {e}")

    finally:
        print("")
