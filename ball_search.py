import cv2 as cv
from cv2 import VideoCapture
import numpy as np


#Initialization of camera to be used
VideoCapture = cv.VideoCapture(0)

prevCircle = None

dist = lambda x1, y1, x2, y2: (x1 - x2)**2 + (y1-y2)**2

while True:
    ret, frame = VideoCapture.read()
    if not ret: break
    
    #COnverts the video into B&W
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    #Makes the video blur
    blurframe = cv.GaussianBlur(grayframe, (29,29), 0)
    
    circles = cv.HoughCircles(blurframe, cv.HOUGH_GRADIENT, 1.2, 50, 
                              param1= 100, param2=50, minRadius= 30, maxRadius= 500)
    
    
    if circles is not None:
        circles = np.uint(np.around(circles))    
        chosen = None
        for i in  circles[0, :]:
            if chosen is None: chosen = i
            if prevCircle is not None:
                if dist(chosen[0], chosen[1], prevCircle[0], prevCircle[1]) <=dist(i[0], i[1], prevCircle[0], prevCircle[1]):
                    chosen = i
        cv. circle(frame, (chosen[0], chosen[1]), 1, (0, 100, 100), 2,)
        cv.circle(frame, (chosen[0], chosen[1]), chosen[2], (255, 0, 255), 3)
        prevCircle = chosen
   
   
   
    cv.imshow("circles", frame)
    if cv.waitKey(1) & 0xFF ==ord("q"): break
    
VideoCapture.release()
cv.destroyAllWindows