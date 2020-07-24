import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8) #pixels (512,512) and  3 channels
# print(img)

# img[:] =  255,0,0 #color the  whole image

# img[200:300, 100:300] =  255,0,0

# cv2.line(img,(0,0),(300,300),(0,255,0),3) #(image, starting  point, ending point, color, thickness)

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) #width, height\

#rectangle

cv2.rectangle(img,(0,0), (250,350),(0,255,255),2)

#fill the rectangle
# cv2.rectangle(img,(0,0), (250,350),(0,255,255),cv2.FILLED)

#cicle
cv2.circle(img,(400,50),30,(255,255,0),5)  #image, center point, radius,

#put text on images
cv2.putText(img," OPENCV ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)  #image, text, where to start, fonts,  scale, color

cv2.imshow("Image", img)

cv2.waitKey(0)