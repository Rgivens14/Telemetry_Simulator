# Industrial Telemetry Simulator





*An industrial telemetry simulation with end-to-end ingestion and monitoring system built with C, Python, and SQLite.*





### Architecture Flow:

C Simulator (stdout JSON) --> Python Ingestion --> SQLite DB \& Alert Logger --> CLI Inspection





### Prerequisites:

*GCC / Clang*

*Python 3.10+*

*pytest*



### Build \& Run Instructions:



*# 1. Compile C binary*

gcc telemetry\_sim.c -o telemetry\_sim



*# 2. Run live monitor*

python3 cli.py



*# 3. Query historical statistics*

python3 cli.py --summary



*# 4. Run automated test suite*

python3 -m pytest







