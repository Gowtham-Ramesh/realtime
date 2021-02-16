import cv2
import re
import numpy as np 


inputD="C:/Users/Gowtham Ramesh/PycharmProjects/opencv-python/venv/super.png"
a=cv2.imread(inputD)
imgGray = cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
img = cv2.Canny(imgGray,50,50)
cv2.imshow("Image",img)
cv2.waitKey(0)