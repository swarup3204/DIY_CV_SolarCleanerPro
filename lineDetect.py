import cv2
import numpy as np

'''input : numpy array, return numpy array'''
def getLinedImg(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150,apertureSize = 3)
    lines = cv2.HoughLines(edges,1,np.pi/180, 200)
    line_length = 2000
    try:
        for i in range(len(lines)):
            for r_theta in lines[i]:
                r,theta = r_theta
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a*r
                y0 = b*r
                x1 = int(x0 + line_length*(-b))
                y1 = int(y0 + line_length*(a))
                x2 = int(x0 - line_length*(-b))
                y2 = int(y0 - line_length*(a))
                cv2.line(img,(x1,y1), (x2,y2), (0,0,255),2)
    except:
        pass
    return img

if __name__ == '__main__':
    img = cv2.imread('image.jpg')
    new_img = getLinedImg(img)
    cv2.imwrite('linesDetected.jpg', new_img)
