import cv2
import numpy as np
from ROI import getROI
from AVGcolor import getAVGcolor
from contours import getContours

image = cv2.imread('dataset/img (5).png')
new_img = getROI(image)
cv2.imshow('Frame',new_img)

cont_img,contours = getContours(new_img)
print(f"Contours = {len(contours)}")
cv2.imshow('Contours',cont_img)

d_img = np.ones((312,312,3), dtype=np.uint8)
avg_color = getAVGcolor(new_img)
d_img[:,:] = avg_color
cv2.imshow('Average Color',d_img)
print(f"AVG COLOR = {avg_color}")

cv2.waitKey(0)