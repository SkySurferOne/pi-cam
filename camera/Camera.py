import numpy as np
import cv2
import datetime
from enum import Enum

from camera.PhotoEffects import SunnyEffectBundle, OldPhotoEffectBundle
from camera.PhotoEffects.TestEffectBundle import TestEffectBundle
from camera.constants import ASSETS_DIR, TMP_DIR


class Camera:

    def __init__(self, frame_name = 'frame', camera_num=0):
        self.camera_num = camera_num
        self.capturing_on = True
        self.cap = None
        self.frame_name = frame_name
        self.current_effect_bundle = None
        self.current_frame = None

    def start_capturing(self):
        print('Start capturing')

        if self.cap is not None:
            self.stop_capturing()

        self.cap = cv2.VideoCapture(self.camera_num)

        while (self.capturing_on):
            # Capture frame-by-frame
            ret, frame = self.cap.read()

            # Process image
            if self.current_effect_bundle:
                frame = self.current_effect_bundle.apply(frame)

            self.current_frame = frame

            cv2.imshow(self.frame_name, frame)

            if cv2.waitKey(5) & 0xFF == 27:
                self.stop_capturing()

    def stop_capturing(self):
        self.capturing_on = False

        self.cap.release()
        cv2.destroyAllWindows()

    def set_effect_bundle(self, effect_enum):
        if self.EffectBundleEnum.SUNNY == effect_enum:
            self.current_effect_bundle = SunnyEffectBundle()
        elif self.EffectBundleEnum.OLD_PHOTO == effect_enum:
            self.current_effect_bundle = OldPhotoEffectBundle()
        elif self.EffectBundleEnum.TEST == effect_enum:
            self.current_effect_bundle = TestEffectBundle()
        elif self.EffectBundleEnum.NO_FILTER == effect_enum:
            self.current_effect_bundle = None

    def get_photo_name(self):
        now = datetime.datetime.now()
        return '[{}.{}.{}, {}:{}:{}:{}] captured_photo.jpg'.format(
             now.year, now.month,
             now.day, now.hour,
             now.minute, now.second,
             now.microsecond)

    def save_photo(self):
        if self.current_frame is not None:
            photo_name = self.get_photo_name()
            photo_dir = TMP_DIR + photo_name
            cv2.imwrite(photo_dir, self.current_frame)
            return photo_name
        else:
            raise Exception('current_frame is not set yet')

    class EffectBundleEnum(Enum):
        SUNNY = 'sunny'
        OLD_PHOTO = 'old-photo'
        TEST = 'test'
        NO_FILTER = 'no-filter'
