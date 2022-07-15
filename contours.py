import cv2
import numpy as np
from lineDetect import getLinedImg


def getContours(image):
    image =  cv2.GaussianBlur(image,(9,7),cv2.BORDER_DEFAULT)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    edged = cv2.Canny(gray, 30, 200)

    contours, hierarchy = cv2.findContours(edged,
        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    return edged,contours


if __name__ == '__main__':
# Let's load a simple image with 3 black squares
    for i in range(1,16):
        image = cv2.imread(f'dataset/img ({i}).png')
        image =  cv2.GaussianBlur(image,(9,7),cv2.BORDER_DEFAULT)
        line_img = getLinedImg(image)
        # Grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Find Canny edges
        edged = cv2.Canny(gray, 30, 200)

        # Finding Contours
        # Use a copy of the image e.g. edged.copy()
        # since findContours alters the image
        contours, hierarchy = cv2.findContours(edged,
            cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        cv2.imwrite(f'contour/img ({i}).png', edged)

        print("Number of Contours found = " + str(len(contours)))

        # Draw all contours
        # -1 signifies drawing all contours
        cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

        cv2.imwrite(f'contour_color/img ({i}).png', image)
        cv2.imwrite(f'contour_line/img ({i}).png', line_img)
