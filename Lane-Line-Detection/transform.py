import cv2
import numpy as np

def HoughTransform(img,rho,theta,thresh,minlinelength,maxlinegap):
    lane_lines =  cv2.HoughLinesP(img,rho,theta,thresh,np.array([]),minLineLength=minlinelength,maxLineGap=maxlinegap)
    return lane_lines