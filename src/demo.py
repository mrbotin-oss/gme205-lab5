from shapely.geometry import Polygon, LineString
from spatial import Parcel, Building, Road


def run_demo():

    # Create example geometries
    parcel_geom = Polygon([(0,0), (0,50), (100,50), (100,0)])
    building_geom = Polygon([(0,0), (0,20), (20,20), (20,0)])
    road_geom = LineString([(0,0), (100,0)])

    # Create objects
    parcel = Parcel(parcel_geom)
    building = Building(building_geom, floors=3)
    road = Road(road_geom, width=4)

    # Individual method calls
    print("Individual area calculations:")
    print("Parcel:", parcel.effective_area())
    print("Building:", building.effective_area())
    print("Road:", road.effective_area())

    print("\nPolymorphic behavior demonstration:")

    # Polymorphism
    features = [parcel, building, road]

    for f in features:
        print(type(f).__name__, f.effective_area())


if __name__ == "__main__":
    run_demo()