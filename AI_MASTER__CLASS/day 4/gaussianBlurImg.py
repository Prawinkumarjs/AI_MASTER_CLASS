import cv2                                       # work well

img = cv2.imread("Captainmarvel.jpg")

gaussianBlurImg = cv2.GaussianBlur(img,(25, 25), 0)
# syntax : dst = cv2.GaussianBlur(src,(kernel),boarderType)
cv2.imwrite("gaussianImage2.jpg", gaussianBlurImg)
