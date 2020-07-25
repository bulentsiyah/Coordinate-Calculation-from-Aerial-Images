import math
from geopy.distance import great_circle, geodesic #,vincenty

class GeoCalculation:

    @staticmethod
    def calculate_new_gps_position(lat1, lon1, distance, bearing):
        R = 6378.1  # Radius of the Earth
        # bearing 1.57 #Bearing is 90 degrees converted to radians.
        # distance  # 0.100 #Distance in km

        lat1 = math.radians(lat1)  # Current lat point converted to radians
        lon1 = math.radians(lon1)  # Current long point converted to radians

        lat2 = math.asin(math.sin(lat1) * math.cos(distance / R) +
                         math.cos(lat1) * math.sin(distance / R) * math.cos(bearing))

        lon2 = lon1 + math.atan2(math.sin(bearing) * math.sin(distance / R) * math.cos(lat1),
                                 math.cos(distance / R) - math.sin(lat1) * math.sin(lat2))

        lat2 = math.degrees(lat2)
        lon2 = math.degrees(lon2)
        
        return lat2, lon2
