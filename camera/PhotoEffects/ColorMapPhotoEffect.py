import cv2
import numpy as np

from camera.PhotoEffects.PhotoEffect import PhotoEffect


class ColorMapPhotoEffect(PhotoEffect):

    def __init__(self, colormap_num=0) -> None:
        super().__init__()
        if colormap_num < 0 or colormap_num > 12:
            raise Exception('Pass number from 0 to 12')

        self.colormap_num = colormap_num

    def apply_filter(self, image):
        if self.colormap_num != 0:
            return cv2.applyColorMap(image, self.colormap_num-1)
        else:
            return image

    def set_colormap_num(self, colormap_num):
        self.colormap_num = colormap_num
