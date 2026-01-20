import csv
import json


# Get the data from sensor 1
try:
    with open("SensorData1.csv", "r") as h:
        sensorData1 = csv.reader(h)
except FileNotFoundError:
    print("CSV file not found")
except PermissionError:
    print("No permission to read file")

# Get the data from sensor 2
try: 
    with open("SensorData2.json", "r") as f:
        sensorData2 = json.load(f)
except FileNotFoundError:
    print("File not found")
except json.JSONDecodeError:
    print("Invalid JSON")
