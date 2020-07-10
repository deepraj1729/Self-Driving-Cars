from utils import show,ROI,displayLineImage,averageSlopeIntercept
from filters import rgbToGray,gaussBlur,cannyEdge,combineImg
from transform import HoughTransform
import numpy as np
import cv2
import matplotlib.pyplot as plt
import time

if __name__ == '__main__':
    start_time = time.time()
    cap = cv2.VideoCapture("video/lanes.mp4")

    print("Press Escape key (Esc) to exit directly....")
    frame_width = int(cap.get(3)) 
    frame_height = int(cap.get(4)) 
    
    size = (frame_width, frame_height) 
    result = cv2.VideoWriter('output/lane_lines.avi',  cv2.VideoWriter_fourcc(*'MJPG'), 50, size) 

    while(cap.isOpened()):
        _,frame = cap.read()
        try:
            grayImg = cv2.cvtColor(frame.astype('uint8'),cv2.COLOR_RGB2GRAY)

            #Smoothening Gray image with Gaussian Blur
            gBlur = cv2.GaussianBlur(grayImg,(5,5),0)

            #Canny edge detection
            canny = cv2.Canny(gBlur,50,150)

            #Lane edges using Region of Interest
            roi = ROI(canny)
            
            #Hough Transform to find lane-lines
            laneLines = cv2.HoughLinesP(roi,2,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=5)

            #Optimize detected line image (avg thresholding)
            averaged_lines = averageSlopeIntercept(frame,laneLines)

            #Display Avg lines detected
            avglineImg = displayLineImage(frame,averaged_lines)

            #Combine detected line image to original image
            avg_combo_img = cv2.addWeighted(frame,0.8,avglineImg,1,1)

            #Write and show
            result.write(avg_combo_img) 
            cv2.imshow("Optimized Lane-Line Detection",avg_combo_img)
            

            k = cv2.waitKey(1) & 0xFF
            try:
                if k == 27:         # wait for ESC key to exit
                    print("Exited....")
                    cap.release()
                    result.release()
                    cv2.destroyAllWindows()
                    exit()
                elif k == ord('s'): # wait for 's' key to save and exit
                    print("Last frame saved to disc")
                    cap.release()
                    result.release()
                    cv2.destroyAllWindows()
                    exit()
            except Exception as e:
                print("Exiting program....")
                exit()

        except Exception as e:
            cap.release()
            result.release()
            cv2.destroyAllWindows()
            end_time = time.time() 
            time_count = end_time - start_time
            print(time_count)
            exit()