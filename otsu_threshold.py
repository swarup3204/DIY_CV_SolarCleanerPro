# Python program to illustrate
# Otsu thresholding type on an image

# organizing imports
import cv2
from cv2 import imshow
import numpy as np

# path to input image is specified and
# image is loaded with imread command


def otsu_threshold(img):
    # cv2.cvtColor is applied over the
    # image input with applied parameters
    # to convert the image in grayscale
    new_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    new_img = np.invert(new_img)

    # applying Otsu thresholding
    # as an extra flag in binary
    # thresholding
    ret, thresh1 = cv2.threshold(new_img,150,255,cv2.THRESH_BINARY)

    # the window showing output image
    # with the corresponding thresholding
    # techniques applied to the input image
    # print(thresh1)

    # De-allocate any associated memory usage
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()

    # thresh1 = cv2.GaussianBlur(thresh1,(7,7),cv2.BORDER_DEFAULT)

    return thresh1,new_img


if __name__ == '__main__':
    for i in range(1, 16):
        img = cv2.imread(f'dataset\img ({i}).png')
        new_img,new_img2 = otsu_threshold(img)
        cv2.imwrite(f'otsu_threshold_results\img ({i}).png', new_img)
        cv2.imwrite(f'otsu_threshold_results_ori\img ({i}).png', new_img2)
