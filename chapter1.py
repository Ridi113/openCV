import cv2

# read images
img = cv2.imread("Resources/girl_with_a_pearl_ring.jpg") # imread meaning reading this package

cv2.imshow("Output", img) #imshow(name of the  window, the file to  show)
cv2.waitKey(0) # 0 means infinite limit


# read  videos
cap = cv2.VideoCapture("Resources/game.mp4")

while True:
    success, img2 = cap.read()
    cv2.imshow("Video", img2)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

#read webcam
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True:
    success, img3 = cap.read()
    cv2.imshow("Video2", img3)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
