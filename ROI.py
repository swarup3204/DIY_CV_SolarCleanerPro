WIDTH = 1600
HEIGHT = 720
def getROI(img):
    return img[HEIGHT//2:(HEIGHT*3)//4,WIDTH//4:(WIDTH*3)//4]

