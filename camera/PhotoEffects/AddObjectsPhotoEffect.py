import cv2
import numpy as np

from camera.PhotoEffects.PhotoEffect import PhotoEffect
from enum import Enum
from math import floor

from camera.constants import ASSETS_DIR


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
        anterior = 0
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(60, 60)
        )

        self.add_object_to_image(faces, image)
        return image


    def add_object_to_image(self, faces, image):
        for (x, y, w, h) in faces:
            obj_img = cv2.imread(ASSETS_DIR +self.object_image)
            if self.object_position == self.ObjectPositionEnum.ABOVE:
                height, width = obj_img.shape[:2]
                res = cv2.resize(obj_img, (w, floor((w/width) * height)), interpolation=cv2.INTER_CUBIC)
                roi = image[y-floor((w/width) * height):y, x:(x + w)]
                hsv = cv2.cvtColor(res, cv2.COLOR_BGR2HSV)
                greenmask = np.array([120, 100, 100])
                mask = cv2.inRange(hsv, greenmask, greenmask)
                mask_inv = cv2.bitwise_not(mask)
                img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
                img2_fg = cv2.bitwise_and(res, res, mask=mask_inv)
                dst = cv2.add(img1_bg, img2_fg)
                image[y - floor((w / width) * height):y, x:(x + w)] = dst
            elif self.object_position == self.ObjectPositionEnum.AROUND:
                res = cv2.resize(obj_img, (2*w, 2*h), interpolation=cv2.INTER_CUBIC)
                roi = image[(y - floor(h/2)):(y + h + floor(h/2)), (x - floor(w/2)):(x + w + floor(w/2))]
                hsv = cv2.cvtColor(res, cv2.COLOR_BGR2HSV)
                greenmask = np.array([120, 100, 100])
                mask = cv2.inRange(hsv, greenmask, greenmask)
                mask_inv = cv2.bitwise_not(mask)
                img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
                img2_fg = cv2.bitwise_and(res, res, mask=mask_inv)
                dst = cv2.add(img1_bg, img2_fg)
                image[(y - floor(h / 2)):(y + h + floor(h / 2)), (x - floor(w / 2)):(x + w + floor(w / 2))] = dst
            else:
                res = cv2.resize(obj_img, (w, h), interpolation=cv2.INTER_CUBIC)
                roi = image[y:(y + h), x:(x + w)]
                hsv = cv2.cvtColor(res, cv2.COLOR_BGR2HSV)
                greenmask = np.array([120, 100, 100])
                mask = cv2.inRange(hsv, greenmask, greenmask)
                mask_inv = cv2.bitwise_not(mask)
                img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
                img2_fg = cv2.bitwise_and(res, res, mask=mask_inv)
                dst = cv2.add(img1_bg, img2_fg)
                image[y:(y + h), x:(x + w)] = dst

    class ObjectPositionEnum(Enum):
        ON = 'on'
        ABOVE = 'above'
        AROUND = 'around'