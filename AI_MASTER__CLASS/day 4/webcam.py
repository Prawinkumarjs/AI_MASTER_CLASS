import cv2                                      # import opencv library
vs = cv2.VideoCapture(0)                        # initialize camera      # work well

while True:                                      # infinite loop
    _, img = vs.read()                            # read the frame from camera
    cv2.imshow("VideoStream", img)      # show a frame
    # 3 line,frame will show continuously util
    key = cv2.waitKey(1) & 0xFF                # record my key press-hex
    if key == ord("q"):  
        break                                 # infinite loop will be broken

vs.release()                                  # release the camera

cv2.destroyAllWindows()                      # all opened windows will be closed



