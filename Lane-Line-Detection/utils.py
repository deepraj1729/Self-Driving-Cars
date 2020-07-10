import cv2
import numpy as np

def show(image,tag = "Normal"):
    imgTag = "{}".format(tag)
    cv2.imshow(imgTag,image)
    cv2.waitKey(0)

def ROI(img):
    height = img.shape[0]
    triangle = np.array([[[200,height],[1100,height],[550,250]]])
    mask = np.zeros_like(img)
    #filling the mask with ROI
    cv2.fillPoly(mask,triangle,255)
    masked_img = cv2.bitwise_and(img,mask)
    return masked_img


def displayLineImage(img,lines):
    line_img = np.zeros_like(img)
    if lines is not None:
        for line in lines:
            x1,y1,x2,y2 = line.reshape(4)
            cv2.line(line_img,(x1,y1),(x2,y2),(252, 3, 69),10)
    return line_img


def make_coordinates(img,line_parameters):
    try:
        slope, intercept = line_parameters
    except TypeError:
        slope,intercept = 0.01,0.01
        
    #assigning coordinates
    y1 = img.shape[0]
    y2 = int(y1*(3/5))
    x1 = int((y1 - intercept)/slope)
    x2 = int((y2 - intercept)/slope)
    return np.array([x1,y1,x2,y2])

def averageSlopeIntercept(img,lines):
    left_fit = []
    right_fit = []
    for line in lines:
        x1,y1,x2,y2 = line.reshape(4)
        parameters = np.polyfit((x1,x2),(y1,y2),1)
        slope = parameters[0]
        intercept = parameters[1]
        if(slope <0):
            left_fit.append((slope,intercept))
        else:
            right_fit.append((slope,intercept))
    
    left_fit_avg = np.average(left_fit,axis=0)
    right_fit_avg = np.average(right_fit,axis=0)

    left_line = make_coordinates(img,left_fit_avg)
    right_line = make_coordinates(img,right_fit_avg)
    return np.array([left_line,right_line])