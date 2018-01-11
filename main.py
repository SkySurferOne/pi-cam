# <<<<<<< HEAD
# import numpy as np
# import cv2
# #from matplotlib import pyplot as plt
#
#
# def laplacian(img):
#     return cv2.Laplacian(img, cv2.CV_64F)
#
#
# def sobel(img, axis='x'):
#     if axis == 'x':
#         return cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
#
#     return cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
#
#
# def nothing(x):
#     pass
#
#
# if __name__ == '__main__':
#
#     #
#     cascPath = "haarcascade_frontalface_default.xml"
#     faceCascade = cv2.CascadeClassifier(cascPath)
#     #
#     cv2.namedWindow('image')
#     cv2.createTrackbar('colormap', 'image', 0, 12, nothing)
#     cv2.createTrackbar('R', 'image', 0, 255, nothing)
#     cv2.createTrackbar('G', 'image', 0, 255, nothing)
#     cv2.createTrackbar('B', 'image', 0, 255, nothing)
#
#     switch = 'Colorize\n0 : OFF \n1 : ON'
#     cv2.createTrackbar(switch, 'image', 0, 1, nothing)
#
#     cap = cv2.VideoCapture(0)
#     #
#     # anterior = 0
#     #
#     while(True):
#         # Capture frame-by-frame
#         ret, frame = cap.read()
#
#         # Our operations on the frame come here
#         # img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         # img = laplacian(frame)
#         # img = sobel(frame, axis='y')
#
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#         faces = faceCascade.detectMultiScale(
#             gray,
#             scaleFactor=1.1,
#             minNeighbors=5,
#             minSize=(90, 90)
#         )
#
#         # Draw a rectangle around the faces
#         for (x, y, w, h) in faces:
#             img2 = cv2.imread('mustache-and-glasses.jpg')
#             res = cv2.resize(img2,(w, h), interpolation = cv2.INTER_CUBIC)
#             #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
#             # rows, cols, channels = res.shape
#             roi = frame[y:(y+h), x:(x+w)]
#
#             img2gray = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
#             ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
#             mask_inv = cv2.bitwise_not(mask)
#             img1_bg = cv2.bitwise_and(roi,roi,mask = mask)
#             img2_fg = cv2.bitwise_and(res,res,mask = mask_inv)
#             # Put logo in ROI and modify the main image
#             dst = cv2.add(img1_bg,img2_fg)
#             frame[y:(y+h), x:(x+w)] = dst
#
#         colormap_num = cv2.getTrackbarPos('colormap', 'image')
#         r = cv2.getTrackbarPos('R', 'image')
#         g = cv2.getTrackbarPos('G', 'image')
#         b = cv2.getTrackbarPos('B', 'image')
#         s = cv2.getTrackbarPos(switch, 'image')
#
#         print(colormap_num)
#         if colormap_num == -1:
#             colormap_num = 0
#
#         if colormap_num != 0:
#             img = cv2.applyColorMap(frame, colormap_num-1)
#         else:
#             img = frame
# =======
import threading
import argparse

from camera import Camera
from camera.constants import ASSETS_DIR
from web_server import run_app

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", '--server_ip', help="Http server ip. If empty uses 127.0.0.1.", default='127.0.0.1')
    args = parser.parse_args()

    cam = Camera('pi-cam', 0)
# >>>>>>> master
#
#         if s != 0:
#             color = np.zeros(shape=img.shape, dtype=np.uint8)
#             color[:] = [b,g,r]
#             img = cv2.add(img, color)
#
#
# <<<<<<< HEAD
#         # Display the resulting frame
#         cv2.imshow('frame', img)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
# =======
    camera_thread = threading.Thread(target=cam.start_capturing)
    camera_thread.start()

    webapp_thread = threading.Thread(target=run_app, args=(cam, args.server_ip, ))
    webapp_thread.start()
# >>>>>>> master

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

