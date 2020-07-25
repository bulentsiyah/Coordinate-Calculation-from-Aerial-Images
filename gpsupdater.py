import math
from math import atan2, pi

class GPSUpdater:

    @staticmethod
    def distance_bearing_calculator_using_parameters(destination_x, destination_y, source_x, source_y,
                                                     image_height, pixel_in_centimeters ):
        analytical_coordinate_sourceY = image_height - source_y
        analytical_coordinate_destinationY = image_height - destination_y

        bearing = 90 - (180 / pi) * math.atan2(analytical_coordinate_destinationY - analytical_coordinate_sourceY,
                                               destination_x - source_x)

        bearing = bearing * (pi / 180)

        distance = math.sqrt(((analytical_coordinate_destinationY - analytical_coordinate_sourceY) ** 2) + (
                destination_x - source_x) ** 2)
        distance = (distance * pixel_in_centimeters)/100 # dis * self.ratio__pixels_meters
        distance = distance / 1000 #meters

        return distance, bearing