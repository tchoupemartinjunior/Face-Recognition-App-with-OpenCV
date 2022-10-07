import cv2
import numpy as np

lower = np.array([15,150,20])
upper = np.array([35,255,255])

cap = cv2.VideoCapture("assets/capture1.mp4")
while True:
    success, img = cap.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(img,lower,upper)
    cv2.imshow('mask',mask)
    cv2.imshow('img',img)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
#cap.release()
cv2.destroyAllWindows()