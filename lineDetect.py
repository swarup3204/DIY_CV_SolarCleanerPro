import cv2
import numpy as np

'''input : numpy array, return (numpy array,edge_close)'''
def getLinedImg(img):
    ans = -1
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150,apertureSize = 3)
    lines = cv2.HoughLines(edges,1,np.pi/180, 200)
    line_length = 2000
    try:
        for r_theta in lines[0]:
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
                cv2.line(img,(x1,y1), (x2,y2), (0,0,255),2)
    except:
        pass
    return img,ans

if __name__ == '__main__':
    img = cv2.imread('img5.jpg')
    new_img = getLinedImg(img)
    cv2.imwrite('linesDetected.jpg', new_img)
