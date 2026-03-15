from shapely.geometry import Polygon, LineString
from shapely.ops import transform
from pyproj import Transformer


# Conversion from WGS84 lat/lon to UTM zone 51N N/E
# With the help of ChatGPT
transformer = Transformer.from_crs("EPSG:4326", "EPSG:32651", always_xy=True)

def project_geom(geometry):
    """Convert lat/lon degrees to meters using UTM projection."""
    return transform(transformer.transform, geometry)


class SpatialObject:
    def __init__(self, geometry):
        # Store geometry in projected coordinates (meters)
        self.geometry = project_geom(geometry)

    def effective_area(self):
        """Return the spatial area representation of the object.
        Subclasses must implement this behavior.
        """
        raise NotImplementedError


class Parcel(SpatialObject):
    def effective_area(self):
        # Simple polygon area in m²
        return self.geometry.area


class Building(SpatialObject):
    def __init__(self, geometry, floors=1):
        super().__init__(geometry)
        self.floors = floors

    def effective_area(self):
        # Area × floors
        return self.geometry.area * self.floors


class Road(SpatialObject):
    def __init__(self, geometry, width=5):
        # width is in meters
        super().__init__(geometry)
        self.width = width

    def effective_area(self):
        # Buffer the line by width/2 (Shapely buffer uses radius)
        # return self.geometry.buffer(self.width / 2). area
        return self.geometry.buffer(self.width).area