import sys
import time

# Python Image Library
from PIL import Image
import cv2
import numpy as np

IMGHEIGHT = 480
IMGWIDTH = 640

def findOrangeBall(pil_image):
    # img = imagepath
    open_cv_image = np.array(pil_image) 
    img = open_cv_image[:, :, ::-1].copy() 
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    blur = cv2.GaussianBlur(hsv,(5,5),0)

    mask = cv2.inRange(blur,(0, 120, 70), (200, 255, 255) )

    im2, contours = cv2.findContours(mask, 1, 2)

    img = mask

    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1.2, 200, param1=100, param2=5, minRadius=5, maxRadius=150)

    best_percentage_orange = 0.15
    x = None
    y = None
    r = None
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for circle in circles[0, :]:
            # 4 Points of Region of interest square
            x_min = circle[0] - circle[2]
            x_max = circle[0] + circle[2]
            y_min = circle[1] - circle[2]
            y_max = circle[1] + circle[2]

            # For now just take the square instead of circle
            roi = img[y_min:y_max, x_min:x_max]

            if roi.shape[0] > 0 and roi.shape[1] > 0:
                # Compute the amount of white pixels (thus the orange ones after applying the mask)
                non_zero = cv2.countNonZero(roi) / float(roi.shape[0] * roi.shape[1])

                # Set the one with the most orange pixels on average as best circle
                if non_zero > best_percentage_orange:
                    x = circle[0]
                    y = circle[1]
                    r = circle[2]
                    best_percentage_orange = non_zero

    # cv2.imshow("orange", mask);
    # cv2.waitKey(0);cv2.destroyAllWindows()
    if((x, y, r) == (None, None, None)):
        return(False, 0, 0, 0, img.shape)
    return(True, x, y, r, img.shape)



def getImage(camProxy): 
    resolution = 2    # VGA
    colorSpace = 11   # RGB

    videoClient = camProxy.subscribe("python_client", resolution, colorSpace, 5)

    # image[6] contains the image data passed as an array of ASCII chars.
    naoImage = camProxy.getImageRemote(videoClient)

    camProxy.unsubscribe(videoClient)

    # Get the image size and pixel array.
    imageWidth = naoImage[0]
    imageHeight = naoImage[1]
    array = naoImage[6]

    # Create a PIL Image from our pixel array.
    im = Image.frombytes("RGB", (imageWidth, imageHeight), array)
    im.save("camImage.png", "PNG")

    # im.show()
    return im
