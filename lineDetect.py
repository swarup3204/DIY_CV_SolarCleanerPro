import cv2
import numpy as np

'''input : numpy array, return (numpy array,edge_close)'''
def getLinedImg(img):
    new_img = np.copy(img)
    gray = cv2.cvtColor(new_img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150,apertureSize = 3)
    lines = cv2.HoughLines(edges,1,np.pi/180, 200)
    line_length = 2000
    try:
        for line in lines[:3]:
            for r_theta in line:
                r,theta = r_theta
                if theta > 1.4 and theta < 1.8: 
                    a = np.cos(theta)
                    b = np.sin(theta)
                    x0 = a*r
                    y0 = b*r
                    x1 = int(x0 + line_length*(-b))
                    y1 = int(y0 + line_length*(a))
                    x2 = int(x0 - line_length*(-b))
                    y2 = int(y0 - line_length*(a))
                    cv2.line(new_img,(x1,y1), (x2,y2), (0,0,255),2)
    except:
        pass
    return new_img

def colorDetect(img):
    print(img)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([100,0,0])
    upper_blue = np.array([255,150,150])
  
    # Here we are defining range of bluecolor in HSV
    # This creates a mask of blue coloured 
    # objects found in the frame.
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    print(mask)
    res = cv2.bitwise_and(img,img, mask= mask)
    return res


if __name__ == '__main__':
    for i in range(1,16):
        img = cv2.imread(f'dataset\img ({i}).png')
        new_img3 = colorDetect(img)
        # new_img2 = getLinedImg(new_img3)
        cv2.imwrite(f'results_line_detection_thresholding\linesDetected{i}.png', new_img3)
