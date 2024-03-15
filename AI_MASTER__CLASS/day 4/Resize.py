import cv2                        # work well
import imutils

img = cv2.imread("Captainmarvel.jpg")
resizeImg = imutils.resize(img, width=50)

cv2.imwrite("resizedImage2.jpg", resizeImg)


