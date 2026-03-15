import json
import os
from shapely.geometry import Polygon, LineString
from spatial import Parcel, Building, Road


def load_data(filepath):
    with open(filepath, "r") as f:
        return json.load(f)  # JSON is a list


def create_spatial_objects(data):
    features = []

    for feature in data:
        geom_type = feature["geometry"]["type"]
        coords = feature["geometry"]["coordinates"]
        feature_type = feature.get("type")

        # Create Shapely geometry
        if geom_type == "Polygon":
            geometry = Polygon(coords[0])  # outer ring

        elif geom_type == "LineString":
            geometry = LineString(coords)

        else:
            continue

        # Instantiate the correct class
        if feature_type == "Parcel":
            obj = Parcel(geometry)

        elif feature_type == "Building":
            floors = feature.get("floors", 1)
            obj = Building(geometry, floors)

        elif feature_type == "Road":
            width = feature.get("width", 5)
            obj = Road(geometry, width)

        else:
            continue

        features.append(obj)

    return features


def compute_total_area(features):
    return sum(f.effective_area() for f in features)


def compute_area_by_type(features):
    area_by_type = {}
    for f in features:
        name = type(f).__name__
        area_by_type[name] = area_by_type.get(name, 0) + f.effective_area()
    return area_by_type


def main():
    data = load_data("data/spatial_features.json")
    features = create_spatial_objects(data)

    if not features:
        print("No spatial features found.")
        return

    total_area = compute_total_area(features)
    area_by_type = compute_area_by_type(features)

    print("\nTotal Effective Area (m²):")
    print(round(total_area, 2))

    print("\nArea by Feature Type (m²):")
    for k, v in area_by_type.items():
        print(f"{k}: {round(v, 2)}")


    # Results
    os.makedirs("output", exist_ok=True)

    results = {
        "total_effective_area": round(total_area, 2),
        "area_by_type": {k: round(v, 2) for k, v in area_by_type.items()}
    }

    with open("output/lab5_results.json", "w") as f:
        json.dump(results, f, indent=4)

    print("\nResults saved to output/lab5_results.json")

    
if __name__ == "__main__":
    main()