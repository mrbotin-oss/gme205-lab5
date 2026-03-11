from shapely.geometry import Polygon, LineString


class SpatialObject:
    def __init__(self, geometry):
        # Store geometry in projected coordinates (meters)
        self.geometry = geometry

    def effective_area(self):
        """Return the spatial area representation of the object.
        Subclasses must implement this behavior.
        """
        raise NotImplementedError


class Parcel(SpatialObject):
    pass

class Building(SpatialObject):
    pass

class Road(SpatialObject):
    pass