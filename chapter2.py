import cv2
import numpy as np

img = cv2.imread("Resources/girl_with_a_pearl_ring.jpg")
kernel = np.ones((5,5),np.uint8) #unsigned integer of 8 bit
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert image  into different colored image
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0) #kernel size (7,7) sigmax is 0
imgCanny = cv2.Canny(img, 150, 200) #threshold values
imgDialation =  cv2.dilate(imgCanny,kernel,iterations=1) #how much thickness  we  need "iterations=1"
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)