import cv2
import numpy as np

from camera.PhotoEffects.PhotoEffect import PhotoEffect


class AddColorPhotoEffect(PhotoEffect):

    def __init__(self, r=0, g=0, b=0) -> None:
        super().__init__()
        self.r = r
        self.g = g
        self.b = b

    def apply_filter(self, image):
        color = np.zeros(shape=image.shape, dtype=np.uint8)
        color[:] = [self.b, self.g, self.r]

        return cv2.add(image, color)

    def set_rgb(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
