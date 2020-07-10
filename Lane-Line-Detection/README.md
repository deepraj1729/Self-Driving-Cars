# Lane-Line Detection:
Detect lane-lines from input images and videos using OpenCV Python

## Usage:
- Install necessary requirements with pip
    
      pip install -r requirements.txt
- To detect lane lines on input images:
    
      python runImg.py 
- To detect lane lines on input videos:
      
      python runVideo.py

## Preprocessing Steps:
### Original Image
<img src="https://github.com/deepraj1729/Self-Driving-Cars/blob/master/Lane-Line-Detection/img/test_img.jpg" width = "900" height = "400">

### GrayScale
<img src="https://github.com/deepraj1729/Self-Driving-Cars/blob/master/Lane-Line-Detection/output/gray_image.png" width = "900" height = "400">

### Gaussian Blur
<img src="https://github.com/deepraj1729/Self-Driving-Cars/blob/master/Lane-Line-Detection/output/gaussian_blur_image.png" width = "900" height = "400">

### Canny Edges Detection
<img src="https://github.com/deepraj1729/Self-Driving-Cars/blob/master/Lane-Line-Detection/output/canny_image.png" width = "900" height = "400">

### Region of Interest
<img src="https://github.com/deepraj1729/Self-Driving-Cars/blob/master/Lane-Line-Detection/output/region_of_interest.png" width = "900" height = "400">

### Masked Lane Lines detected 
<img src="https://github.com/deepraj1729/Self-Driving-Cars/blob/master/Lane-Line-Detection/output/line_detected_masked.png" width = "900" height = "400">

### Combined Image
<img src="https://github.com/deepraj1729/Self-Driving-Cars/blob/master/Lane-Line-Detection/output/combined_image.png" width = "900" height = "400">

### Optimized Final Image
<img src="https://github.com/deepraj1729/Self-Driving-Cars/blob/master/Lane-Line-Detection/output/avg_combined_image.png" width = "900" height = "400">

### Output Video (Animated GIF)
![gif](lane_lines.gif)
