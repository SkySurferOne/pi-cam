import cv2
import numpy as np

from camera.PhotoEffects.PhotoEffect import PhotoEffect
from camera.constants import ASSETS_DIR


class GreenScreenPhotoEffect(PhotoEffect):

    colors = ['red', 'green']

    def __init__(self, bg_image, screen_color='red') -> None:
        """

        :param bg_image: filename
        :param screen_color: color which will be changed for bg_image
        """
        # todo add other colors
        if screen_color not in self.colors:
            raise Exception('There is not {} color'.format(screen_color))

        super().__init__()
        self.bg_image = bg_image
        self.cv_photo = cv2.imread(ASSETS_DIR + bg_image)
        if self.cv_photo is None:
            raise Exception('Cannot read photo file')
        self.screen_color = screen_color

    def apply_filter(self, image):
        height, width = image.shape[:2]
        self.cv_photo = cv2.resize(self.cv_photo, (width, height), interpolation=cv2.INTER_CUBIC)
        mask = None
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # define range of color in HSV
        if self.screen_color == 'red':
            red2lower1 = np.array([0, 100, 100])
            red2upper1 = np.array([10, 255, 255])

            red2lower2 = np.array([160, 100, 100])
            red2upper2 = np.array([179, 255, 255])

            # threshold the HSV image to get only red colors
            mask1 = cv2.inRange(hsv, red2lower1, red2upper1)
            mask2 = cv2.inRange(hsv, red2lower2, red2upper2)
            mask = cv2.add(mask1, mask2)

        elif self.screen_color == 'green':
            green_lower = np.array([20, 100, 50])
            green_upper = np.array([100, 255, 255])

            # threshold the HSV image to get only red colors
            mask = cv2.inRange(hsv, green_lower, green_upper)

        mask_inv = cv2.bitwise_not(mask)

        # bitwise-AND mask and original image
        image = cv2.bitwise_and(image, image, mask=mask_inv)
        res = cv2.bitwise_and(self.cv_photo, self.cv_photo, mask=mask)

        return cv2.add(image, res)

    def set_bg_image(self, bg_image):
        self.bg_image = bg_image
        self.cv_photo = cv2.imread(bg_image)

    def set_screen_color(self, screen_color):
        if screen_color not in self.colors:
            raise Exception('There is not {} color'.format(screen_color))
        self.screen_color = screen_color
