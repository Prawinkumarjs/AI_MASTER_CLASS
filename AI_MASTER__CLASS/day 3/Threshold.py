import cv2
img = cv2.imread("download (4).jfif")      # work well


grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

threshImg = cv2.threshold(grayImg, 110, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite("thresholdImage2.jpg", threshImg)

cv2.imshow("Img", threshImg)
