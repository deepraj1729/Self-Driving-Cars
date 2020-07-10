import cv2

def rgbToGray(img):
    gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    return gray


def gaussBlur(img):
    gBlur = cv2.GaussianBlur(img,(5,5),0)
    return gBlur

def cannyEdge(img):
    cannyImg = cv2.Canny(img,50,150)
    return cannyImg

def combineImg(img1,img2):
    combo_img = cv2.addWeighted(img1,0.8,img2,1,1)
    return combo_img