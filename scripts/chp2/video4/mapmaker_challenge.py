

class Point():
    def __init__(self, name, latitude, longitude):
        if not isinstance(name, str):
            raise TypeError("Invalid name. City name must be of type string")
        self.name = name

        if not (-90 <= latitude <= 90) or not (-180 <= longitude <= 180):
            raise ValueError("Invalid latitude, longitude combination.")
        self.latitude = latitude
        self.longitude = longitude


    def get_lat_long(self):
        return (self.latitude, self.longitude)
