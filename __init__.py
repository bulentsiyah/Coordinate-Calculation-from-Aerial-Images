import cv2 
import matplotlib
import matplotlib.pyplot as plt
from utils import PixelLocation
from gpsupdater import GPSUpdater 
from geocalculation import GeoCalculation

def main():
    image = "src/istanbul_aerial_1pixel_10_centimeters.png"

    image = cv2.imread(image, 1)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    height, width = image.shape[:2]
    print(width, height, "width, height")
    ratio_pixel_centimeters = 10

    selected_position = PixelLocation(
        label="GPS location known place",
        x_pixel=int(width / 2) ,
        y_pixel=480,
        latitude=28.971832514674194,
        longitude= 41.01209534207387,
    )

    calculation_position = PixelLocation(
        label="GPS location, location to be calculated",
        x_pixel=int(width / 2) + 1000, # 1000 / ratio_pixel_centimeters =  100 meters east
        y_pixel=480 + 2000, # 2000 / ratio_pixel_centimeters = 200 meters south
        latitude=0.0,
        longitude= 0.0,
    )


    print('selected_position x:{0}, y:{1}, calculation_position x:{2}, y:{3}'.format(selected_position.x_pixel,
    selected_position.y_pixel, 
    calculation_position.x_pixel,
    calculation_position.y_pixel))

    text_selected = 'selected_position latitude:{0:.7f}, longitude:{1:.7f}, '.format(selected_position.latitude,
    selected_position.longitude)
    print(text_selected)

    distance, bearing = GPSUpdater.distance_bearing_calculator_using_parameters(destination_x=calculation_position.x_pixel,
                                                                                     destination_y=calculation_position.y_pixel,
                                                                                    source_x=selected_position.x_pixel,
                                                                                    source_y=selected_position.y_pixel,
                                                                                    image_height=height,
                                                                                    pixel_in_centimeters=ratio_pixel_centimeters)

    print('distance:{0} bearing:{1}'.format(distance,bearing))

    calculation_position.latitude, calculation_position.longitude = GeoCalculation.calculate_new_gps_position(lat1=selected_position.latitude,
    lon1=selected_position.longitude,distance=distance,bearing=bearing)
    

    text_calculation = 'calculation_position latitude:{0:.7f}, longitude:{1:.7f}'.format(calculation_position.latitude,calculation_position.longitude)
    print(text_calculation)


    start_point = (selected_position.x_pixel, selected_position.y_pixel)
    end_point = (calculation_position.x_pixel, calculation_position.y_pixel )

    thickness = 10
    color = (255, 0, 0) 
    image = cv2.line(image, start_point, end_point, color, thickness)


    org_y = 200
    org_x = 10
    org = (org_x, org_y) # x:column y:row 
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 3
    color = (255, 255, 0) 
    paddingText = 50

    cv2.putText(image, text_selected, org, font, fontScale, color, thickness, cv2.LINE_AA) 

    org_y = org_y+3*paddingText+thickness
    org_x = 10
    org = (org_x, org_y)
    cv2.putText(image,text_calculation , org, font, fontScale, color, thickness, cv2.LINE_AA)

    org_y = org_y+3*paddingText+thickness
    org_x = 10
    org = (org_x, org_y)
    cv2.putText(image,'different distance:{0:.2f} meters'.format(distance) , org, font, fontScale, color, thickness, cv2.LINE_AA)



    plt.figure(figsize=(10, 10))
    plt.imshow(image)
    plt.show()


if __name__ == '__main__':
    main()