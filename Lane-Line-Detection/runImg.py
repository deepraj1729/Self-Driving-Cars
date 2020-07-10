from utils import show,ROI,displayLineImage,averageSlopeIntercept
from filters import rgbToGray,gaussBlur,cannyEdge,combineImg
from transform import HoughTransform
import numpy as np
import cv2
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Path to image
    img_path = r"img/test_img.jpg"

    # Read Image
    original_img = cv2.imread(img_path)

    # Show original image
    show(original_img,tag = "Original Image")

    #Copy original image
    copyImg = np.copy(original_img)

    #GrayScale image
    grayImg = rgbToGray(copyImg)
    show(grayImg,"Gray Scale Image")
    cv2.imwrite("output/gray_image.png",grayImg)

    #Smoothening Gray image with Gaussian Blur
    gBlur = gaussBlur(grayImg)
    show(gBlur,"Gaussian Blur Image")
    cv2.imwrite("output/gaussian_blur_image.png",gBlur)
    #Canny edge detection
    canny = cannyEdge(gBlur)
    show(canny,"Canny Edges Detected`")
    cv2.imwrite("output/canny_image.png",canny)
    
    # plt.imshow(canny)
    # plt.show()

    #Lane edges using Region of Interest
    roi = ROI(canny)
    show(roi,"Region of Interest (With Bitwise AND)")
    cv2.imwrite("output/region_of_interest.png",roi)
    
    
    #Hough Transform to find lane-lines
    laneLines = HoughTransform(img=roi,rho =2,theta=np.pi/180,thresh=100,minlinelength = 40,maxlinegap = 5)

    #Display lines detected
    lineImg = displayLineImage(original_img,laneLines)
    show(lineImg,"Lines detected Image")
    cv2.imwrite("output/line_detected_masked.png",lineImg)

    #Combine detected line image to original image
    combo_img = combineImg(original_img,lineImg)
    show(combo_img,"Final combined Image")
    cv2.imwrite("output/combined_image.png",combo_img)

    #Optimize detected line image (avg thresholding)
    averaged_lines = averageSlopeIntercept(original_img,laneLines)

    #Display Avg lines detected
    avglineImg = displayLineImage(original_img,averaged_lines)

    #Combine detected line image to original image
    avg_combo_img = combineImg(original_img,avglineImg)
    show(avg_combo_img,"Final optimized combined Image")
    cv2.imwrite("output/avg_combined_image.png",avg_combo_img)



