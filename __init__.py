import cv2 
from utils import PixelLocation

def main():
    image = "src/istanbul_aerial_1pixel_10_centimeters.png"

    image = cv2.imread(image, 1)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    height, width = image.shape[:2]
    print(width, height, "width, height")
    ratio_pixel_centimeters = 10

    selected_position = PixelLocation(
        label="GPS location known place",
        x_pixel_position=(int)width/2,
        y_pixel_position=0,
        latitude_position=28.971832514674194,
        longitude_position= 41.01209534207387,
    )

    calculation_position = PixelLocation(
        label="GPS location, location to be calculated",
        x_pixel_position=(int)width/2 + 100, # 100 * ratio_pixel_centimeters = 1000 = 100 meters east
        y_pixel_position=200, # 200 * ratio_pixel_centimeters = 2000 = 200 meters south
        latitude_position=0.0,
        longitude_position= 0.0,
    )


    



if __name__ == '__main__':
    main()