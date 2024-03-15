import cv2    # library Import          # work well

img = cv2.imread("download (4).jfif")  # read an image in the name of img

cv2.imwrite("sample1copy.png",img)  # save an image with different name and extention

cv2.imshow("AI_Master_Class",img)  # display img
cv2.waitKey(0)

cv2.destroyAllWindows()
