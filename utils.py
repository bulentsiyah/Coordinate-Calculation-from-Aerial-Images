from dataclasses import dataclass


@dataclass
class PixelLocation:
    label: str
    x_pixel_position: int
    y_pixel_position: int
    latitude_position: float
    longitude_position: float


