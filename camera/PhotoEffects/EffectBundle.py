from camera.PhotoEffects.EffectManager import EffectManager


class EffectBundle:

    def __init__(self) -> None:
        self.effect_manager = EffectManager()

    def apply(self, image):
        pass
