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

# Find collisions, rounded to 3 digits

sensor1Coords, sensor2Coords = [], []
for lat, lon in zip(sensorLatitude1, sensorLongitude1):
    coord = (round(float(lat), 3), round(float(lon), 3))
    sensor1Coords.append(coord)

for lat, lon in zip(sensorLatitude2, sensorLongitude2):
    coord = (round(float(lat), 3), round(float(lon), 3))
    sensor2Coords.append(coord)

# Turing the cords into sets then finding intersection to find collisions 
sensor1Set, sensor2Set = set(sensor1Coords), set(sensor2Coords)
collisions = sensor1Set.intersection(sensor2Set)

if collisions:
    print(f"Found {len(collisions)} collisions:")
    for lat, lon in collisions:
        print(f"Latitude: {lat}, Longitude: {lon}")
else:
    print("No collisions found.")
