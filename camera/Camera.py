import numpy as np
import cv2

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

    def set_effect_bundle(self):
        print('set_effect_bundle')
        self.current_effect_bundle = TestEffectBundle()
