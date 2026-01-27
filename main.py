import csv
import json
import sys

# Method to read CSV
def read_csv_sensor(file_path):
    latitudes, longitudes, ids = [], [], []
    try:
        with open(file_path, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                latitudes.append(float(row["latitude"]))
                longitudes.append(float(row["longitude"]))
                ids.append(int(row["id"]))
        return list(zip(latitudes, longitudes, ids))
    except FileNotFoundError:
        print(f"CSV file not found: {file_path}")
        sys.exit(1)
    except PermissionError:
        print(f"No permission to read file: {file_path}")
        sys.exit(1)
    except KeyError as e:
        print(f"Missing column in CSV: {e}")
        sys.exit(1)

# Method to read JSON
def read_json_sensor(file_path):
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
        coords = []
        for row in data:
            coords.append((float(row["latitude"]), float(row["longitude"]), int(row["id"])))
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
    return [(round(lat, precision), round(lon, precision), _id) for lat, lon, _id in coords]

# Method to find collisions (return pairs of IDs)
def find_collisions(sensor1_coords, sensor2_coords):

    # Map coordinates to IDs for sensor1
    coord_to_ids1 = {}
    for lat, lon, _id in sensor1_coords:
        key = (lat, lon)
        if key not in coord_to_ids1:
            coord_to_ids1[key] = []
        coord_to_ids1[key].append(_id)
    
    collisions = []
    
    # Iterate sensor2 and check for collisions
    for lat, lon, id2 in sensor2_coords:
        key = (lat, lon)
        if key in coord_to_ids1:
            for id1 in coord_to_ids1[key]:
                collisions.append((id1, id2))
    
    return collisions

# Main
def main():

    if len(sys.argv) < 3:
        print("Usage: python script.py <CSV_file> <JSON_file> [precision]")
        sys.exit(1)

    csv_file = sys.argv[1]
    json_file = sys.argv[2]
    precision = int(sys.argv[3]) if len(sys.argv) >= 4 else 3

    # Read sensors
    sensor1_coords = read_csv_sensor(csv_file)
    sensor2_coords = read_json_sensor(json_file)

    # Round coordinates
    sensor1_coords = round_coords(sensor1_coords, precision)
    sensor2_coords = round_coords(sensor2_coords, precision)

    # Find collisions
    collisions = find_collisions(sensor1_coords, sensor2_coords)

    # Print results
    if collisions:
        print(f"Found {len(collisions)} collisions:")
        for id1, id2 in collisions:
            print(f"Sensor 1 ID: {id1}, Sensor 2 ID: {id2}")
    else:
        print("No collisions found.")

if __name__ == "__main__":
    main()