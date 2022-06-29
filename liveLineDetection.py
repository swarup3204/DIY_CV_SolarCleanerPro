from lineDetect import getLinedImg
import cv2

vid = cv2.VideoCapture(0)

while(True):
    ret, frame = vid.read()
    lineFrame, close_edge = getLinedImg(frame)
    cv2.imshow('frame', lineFrame)
    print(close_edge)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
