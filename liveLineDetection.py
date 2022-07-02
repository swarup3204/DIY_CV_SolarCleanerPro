from lineDetect import getLinedImg
import cv2

if __name__ == "__main__":
    
    vid = cv2.VideoCapture(0)

    NO_EGDE_FOUND = "NO_EGDE_FOUND"
    NOT_CLOSE = "NOT_CLOSE"
    CLOSE = "CLOSE"

    while(True):
        ret, frame = vid.read()
        lineFrame, close_edge = getLinedImg(frame)
        cv2.imshow('frame', lineFrame)
        if close_edge != NO_EGDE_FOUND:
            print(close_edge)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    cv2.destroyAllWindows()
