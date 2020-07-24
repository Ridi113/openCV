import cv2
import numpy as np

img = cv2.imread("Resources/girl_with_a_pearl_ring.jpg")
print(img.shape)

imgResize = cv2.resize(img,(450,500)) #width first and then height

imgCropped = img[0:500,200:700] #height first and then width

cv2.imshow("Image", img)
cv2.imshow("Image Resized", imgResize)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)