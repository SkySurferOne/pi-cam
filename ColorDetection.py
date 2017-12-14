import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    photo = cv2.imread("chleb.jpeg")

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    red2lower1 = np.array([0,100,100])
    red2upper1 = np.array([10,255,255])

    red2lower2 = np.array([160, 100, 100])
    red2upper2 = np.array([179, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask1 = cv2.inRange(hsv, red2lower1, red2upper1)
    mask2 = cv2.inRange(hsv, red2lower2, red2upper2)
    mask = cv2.add(mask1, mask2)
    mask_inv = cv2.bitwise_not(mask)

    # Bitwise-AND mask and original image
    frame = cv2.bitwise_and(frame, frame, mask=mask_inv)
    res = cv2.bitwise_and(photo, photo, mask = mask)

    frame = cv2.add(frame, res)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()