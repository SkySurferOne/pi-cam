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
        cascPath = ASSETS_DIR + "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascPath)
        anterior = 0
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(90, 90)
        )

        self.add_object_to_image(faces, image)
        return image

    def add_object_to_image(self, faces, image):
        for (x, y, w, h) in faces:
            obj_img = cv2.imread(ASSETS_DIR + self.object_image)
            lower = [0, 255, 0]
            upper = [10, 255, 10]
            lower = np.array(lower, dtype="uint8")
            upper = np.array(upper, dtype="uint8")

            height, width = obj_img.shape[:2]
            if self.object_position == self.ObjectPositionEnum.ABOVE:
                res = cv2.resize(obj_img, (w, floor((w / width) * height)), interpolation=cv2.INTER_CUBIC)
                new_height, new_width = res.shape[:2]
                img_bnd_x1 = x
                img_bnd_x2 = (x + w)
                img_bnd_y1 = (y - new_height)
                img_bnd_y2 = y
            elif self.object_position == self.ObjectPositionEnum.AROUND:
                res = cv2.resize(obj_img, (2 * w, 2 * h), interpolation=cv2.INTER_CUBIC)
                new_height, new_width = res.shape[:2]
                img_bnd_x1 = (floor(x - w / 2))
                img_bnd_x2 = (floor(x - w / 2)) + new_width
                img_bnd_y1 = (floor(y - h / 2))
                img_bnd_y2 = (floor(y - h / 2)) + new_height
            else:
                res = cv2.resize(obj_img, (w, h), interpolation=cv2.INTER_CUBIC)
                new_height, new_width = res.shape[:2]
                img_bnd_x1 = x
                img_bnd_x2 = (x + w)
                img_bnd_y1 = y
                img_bnd_y2 = (y + h)

            roi = image[img_bnd_y1:img_bnd_y2, img_bnd_x1:img_bnd_x2]
            hr, wr = roi.shape[:2]

            if hr == new_height and wr == new_width:
                mask = cv2.inRange(res, lower, upper)
                mask_inv = cv2.bitwise_not(mask)
                img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
                img2_fg = cv2.bitwise_and(res, res, mask=mask_inv)
                dst = cv2.add(img1_bg, img2_fg)
                image[img_bnd_y1:img_bnd_y2, img_bnd_x1:img_bnd_x2] = dst

    class ObjectPositionEnum(Enum):
        ON = 'on'
        ABOVE = 'above'
        AROUND = 'around'
