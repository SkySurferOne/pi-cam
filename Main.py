import numpy as np
import cv2
from matplotlib import pyplot as plt


def laplacian(img):
    return cv2.Laplacian(img, cv2.CV_64F)


def sobel(img, axis='x'):
    if axis == 'x':
        return cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)

    return cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)


def nothing(x):
    pass


if __name__ == '__main__':
    cv2.namedWindow('image')
    cv2.createTrackbar('colormap', 'image', 0, 12, nothing)
    cv2.createTrackbar('R', 'image', 0, 255, nothing)
    cv2.createTrackbar('G', 'image', 0, 255, nothing)
    cv2.createTrackbar('B', 'image', 0, 255, nothing)

    switch = 'Colorize\n0 : OFF \n1 : ON'
    cv2.createTrackbar(switch, 'image', 0, 1, nothing)

    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        # img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # img = laplacian(frame)
        # img = sobel(frame, axis='y')

        colormap_num = cv2.getTrackbarPos('colormap', 'image')
        r = cv2.getTrackbarPos('R', 'image')
        g = cv2.getTrackbarPos('G', 'image')
        b = cv2.getTrackbarPos('B', 'image')
        s = cv2.getTrackbarPos(switch, 'image')

        print(colormap_num)
        if colormap_num == -1:
            colormap_num = 0

        if colormap_num != 0:
            img = cv2.applyColorMap(frame, colormap_num-1)
        else:
            img = frame

        if s != 0:
            color = np.zeros(shape=img.shape, dtype=np.uint8)
            color[:] = [b,g,r]
            img = cv2.add(img, color)

        # Display the resulting frame
        cv2.imshow('frame', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
