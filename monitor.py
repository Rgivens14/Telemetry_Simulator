import subprocess #use .Popen to get instant output
import json #

#you will need to create a monitor. Use the subproccess to run the simulator
#make sure that the compile output is converted to its text form

process = subprocess.Popen(
    ["./telemetry_sim"],
    stdout=subprocess.PIPE,
    text=True
)

for line in process.stdout:
    line = line.strip()
    print("Received raw line:", line) # will edit this later to only use the line value