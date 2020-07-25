from dataclasses import dataclass


@dataclass
class PixelLocation:
    label: str
    x_pixel: int
    y_pixel: int
    latitude: float
    longitude: float


