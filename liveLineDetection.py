from lineDetect import getLinedImg
import cv2

if __name__ == "__main__":

    vid = cv2.VideoCapture(0)

    NOT_CLOSE = "NOT_CLOSE"
    CLOSE = "CLOSE"

    while True:
        ret, frame = vid.read()
        # lineFrame, close_edge = getLinedImg(frame)
        # cv2.imshow('frame', lineFrame)
            
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    cv2.destroyAllWindows()
