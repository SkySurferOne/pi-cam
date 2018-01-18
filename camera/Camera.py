import numpy as np
import cv2
from enum import Enum

from camera.PhotoEffects import BeachEffectBundle
from camera.PhotoEffects import HippieEffectBundle
from camera.PhotoEffects import SkiingEffectBundle
from camera.PhotoEffects import SunnyEffectBundle, OldPhotoEffectBundle, GentlemanEffectBundle, RoyalEffectBundle
from camera.PhotoEffects import UnderwaterEffectBundle
from camera.PhotoEffects.TestEffectBundle import TestEffectBundle


class Camera:

    def __init__(self, frame_name = 'frame', camera_num=0):
        self.camera_num = camera_num
        self.capturing_on = True
        self.cap = None
        self.frame_name = frame_name
        self.current_effect_bundle = None

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
        elif self.EffectBundleEnum.GENTLEMAN == effect_enum:
            self.current_effect_bundle = GentlemanEffectBundle()
        elif self.EffectBundleEnum.ROYAL == effect_enum:
            self.current_effect_bundle = RoyalEffectBundle()
        elif self.EffectBundleEnum.UNDERWATER == effect_enum:
            self.current_effect_bundle = UnderwaterEffectBundle()
        elif self.EffectBundleEnum.SKIING == effect_enum:
            self.current_effect_bundle = SkiingEffectBundle()
        elif self.EffectBundleEnum.HIPPIE == effect_enum:
            self.current_effect_bundle = HippieEffectBundle()
        elif self.EffectBundleEnum.BEACH == effect_enum:
            self.current_effect_bundle = BeachEffectBundle()
        elif self.EffectBundleEnum.NO_FILTER == effect_enum:
            self.current_effect_bundle = None

    class EffectBundleEnum(Enum):
        SUNNY = 'sunny'
        OLD_PHOTO = 'old-photo'
        TEST = 'test'
        GENTLEMAN = 'gentleman'
        ROYAL = 'royal'
        UNDERWATER = 'underwater'
        SKIING = 'skiing'
        HIPPIE = 'hippie'
        BEACH = 'beach'
        NO_FILTER = 'no-filter'
