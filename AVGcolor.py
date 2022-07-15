import numpy as np
def getAVGcolor(img):
    average_color_row = np.average(img, axis=0)
    average_color = np.average(average_color_row, axis=0)
    return average_color