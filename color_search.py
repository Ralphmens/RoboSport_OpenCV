import cv2 as cv
from cv2 import VideoCapture
import numpy as np

lower = np.array([10, 220, 100])
upper = np.array([30, 255, 255])

vid = cv.VideoCapture(0)

while True:
    ret, frame = vid.read()
    if not ret: break
    frame1 = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    mask = cv.inRange(frame1, lower, upper)
    
    contours, hierachy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    if len(contours) != 0:
        for contour in contours:
            if cv.contourArea(contour) > 700:
                x, y, w, h = cv.boundingRect(contour)
                cv.rectangle(frame, (x,y), (x + w, y + h), (0,0,225), 3)
    
    cv.imshow("mask", mask)
    cv.imshow("original", frame)

    
    if cv.waitKey(1) & 0xFF ==ord("q"): break
    
VideoCapture.release()
cv.destroyAllWindows