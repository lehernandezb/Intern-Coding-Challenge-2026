import csv
import json
import argparse
import sys

# Method to read CSV
def read_csv_sensor(file_path):
    latitudes, longitudes = [], []
    try:
        with open(file_path, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                latitudes.append(float(row["latitude"]))
                longitudes.append(float(row["longitude"]))
        return list(zip(latitudes, longitudes))
    except FileNotFoundError:
        print(f"CSV file not found: {file_path}")
        sys.exit(1)
    except PermissionError:
        print(f"No permission to read file: {file_path}")
        sys.exit(1)
    except KeyError as e:
        print(f"Missing column in CSV: {e}")
        sys.exit(1)

# Method to read Json
def read_json_sensor(file_path):
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
        coords = []
        for row in data:
            coords.append((float(row["latitude"]), float(row["longitude"])))
        return coords
    except FileNotFoundError:
        print(f"JSON file not found: {file_path}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Invalid JSON file: {file_path}")
        sys.exit(1)
    except KeyError as e:
        print(f"Missing key in JSON: {e}")
        sys.exit(1)

# Method to round coords
def round_coords(coords, precision):
    return [(round(lat, precision), round(lon, precision)) for lat, lon in coords]

# Method to find collisions
def find_collisions(sensor1_coords, sensor2_coords):
    return set(sensor1_coords).intersection(set(sensor2_coords))

# Main
def main():

    # Read args
    if len(sys.argv) < 3:
        print("Usage: python script.py <CSV_file> <JSON_file> [precision]")
        sys.exit(1)

    csv_file = sys.argv[1]
    json_file = sys.argv[2]

    # Optional rounding precision
    if len(sys.argv) >= 4:
        precision = int(sys.argv[3])
    else:
        precision = 3

    # Read
    sensor1_coords = read_csv_sensor(csv_file)
    sensor2_coords = read_json_sensor(json_file)

    # Round 
    sensor1_coords = round_coords(sensor1_coords, precision)
    sensor2_coords = round_coords(sensor2_coords, precision)

    # Find collisions
    collisions = find_collisions(sensor1_coords, sensor2_coords)

    #Print
    if collisions:
        print(f"Found {len(collisions)} collisions:")
        for lat, lon in collisions:
            print(f"Latitude: {lat}, Longitude: {lon}")
    else:
        print("No collisions found.")

if __name__ == "__main__":
    main()
