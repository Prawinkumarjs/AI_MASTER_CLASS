import cv2                            # work well

img = cv2.imread("download (4).jfif")
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


cv2.imwrite("grayImage.png", grayImg)  # save an image with different name and extent


cv2.imshow("Orig", img)  # display img
cv2.imshow("Gray", grayImg)


cv2.waitKey(0)

cv2.destroyAllWindows()
 
