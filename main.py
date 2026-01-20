import csv
import json


# Get the data from sensor 1
try:
    sensorLongitude1, sensorLatitude1 = [], []
    with open("SensorData1.csv", newline="") as h:
        sensorData1 = csv.DictReader(h)

        for row in sensorData1:
            sensorLatitude1.append(row["latitude"])
            sensorLongitude1.append(row["longitude"])

except FileNotFoundError:
    print("CSV file not found")
except PermissionError:
    print("No permission to read file")

# Get the data from sensor 2
try: 
    sensorLongitude2, sensorLatitude2 = [], []
    with open("SensorData2.json", "r") as f:
        sensorData2 = json.load(f)

    for row in sensorData2:
            sensorLatitude2.append(row["latitude"])
            sensorLongitude2.append(row["longitude"])  
    
except FileNotFoundError:
    print("File not found")
except json.JSONDecodeError:
    print("Invalid JSON")

# Find collisions, rounded to the nearest int