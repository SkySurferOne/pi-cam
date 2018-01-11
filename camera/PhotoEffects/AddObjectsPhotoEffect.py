import cv2
import numpy as np

from camera.PhotoEffects.PhotoEffect import PhotoEffect
from enum import Enum
from math import floor

def nothing(self, x):
    pass

class AddObjectsPhotoEffect(PhotoEffect):
    def __init__(self, object_image, object_position) -> None:

        '''
            :param object_image: filename
            '''
        super().__init__()
        self.object_image = object_image
        self.object_position = object_position


    def apply_filter(self, image):
        cascPath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascPath)
        #
        cv2.namedWindow('trackbar_image')
        cv2.createTrackbar('colormap', 'trackbar_image', 0, 12, nothing)
        cv2.createTrackbar('R', 'trackbar_image', 0, 255, nothing)
        cv2.createTrackbar('G', 'trackbar_image', 0, 255, nothing)
        cv2.createTrackbar('B', 'trackbar_image', 0, 255, nothing)

        switch = 'Colorize\n0 : OFF \n1 : ON'
        cv2.createTrackbar(switch, 'trackbar_image', 0, 1, nothing)
        #
        # cap = cv2.VideoCapture(0)
        #
        anterior = 0
        #
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(90, 90)
        )

        self.add_object_to_image(faces, image)

        colormap_num = cv2.getTrackbarPos('colormap', 'trackbar_image')
        r = cv2.getTrackbarPos('R', 'trackbar_image')
        g = cv2.getTrackbarPos('G', 'trackbar_image')
        b = cv2.getTrackbarPos('B', 'trackbar_image')
        s = cv2.getTrackbarPos(switch, 'trackbar_image')

        print(colormap_num)
        if colormap_num == -1:
            colormap_num = 0

        if colormap_num != 0:
            img = cv2.applyColorMap(image, colormap_num - 1)
        else:
            img = image

        if s != 0:
            color = np.zeros(shape=img.shape, dtype=np.uint8)
            color[:] = [b, g, r]
            img = cv2.add(img, color)
        return img

    def set_colormap_num(self, colormap_num):
        self.colormap_num = colormap_num

    def add_object_to_image(self, faces, image):
        for (x, y, w, h) in faces:
            obj_img = cv2.imread(self.object_image)
            if self.object_position == self.ObjectPositionEnum.ABOVE:
                height, width = obj_img.shape[:2]
                res = cv2.resize(obj_img, (w, floor((w/width) * height)), interpolation=cv2.INTER_CUBIC)
                roi = image[y-floor((w/width) * height):y, x:(x + w)]

                obj_imggray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
                ret, mask = cv2.threshold(obj_imggray, 10, 255, cv2.THRESH_BINARY)
                mask_inv = cv2.bitwise_not(mask)
                img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
                img2_fg = cv2.bitwise_and(res, res, mask=mask_inv)
                dst = cv2.add(img1_bg, img2_fg)
                image[y - floor((w / width) * height):y, x:(x + w)] = dst
            else:
                res = cv2.resize(obj_img, (w, h), interpolation=cv2.INTER_CUBIC)
                roi = image[y:(y + h), x:(x + w)]

                obj_imggray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
                ret, mask = cv2.threshold(obj_imggray, 10, 255, cv2.THRESH_BINARY)
                mask_inv = cv2.bitwise_not(mask)
                img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
                img2_fg = cv2.bitwise_and(res, res, mask=mask_inv)
                dst = cv2.add(img1_bg, img2_fg)
                image[y:(y + h), x:(x + w)] = dst

    class ObjectPositionEnum(Enum):
        ON = 'on'
        ABOVE = 'above'