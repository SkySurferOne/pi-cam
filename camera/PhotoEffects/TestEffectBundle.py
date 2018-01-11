from camera.PhotoEffects import AddColorPhotoEffect
from camera.PhotoEffects import ColorMapPhotoEffect
from camera.PhotoEffects import EffectBundle
from camera.PhotoEffects import GreenScreenPhotoEffect


class TestEffectBundle(EffectBundle):

    def __init__(self) -> None:
        super().__init__()

        green_screen = GreenScreenPhotoEffect('test_bg.jpeg', 'red')
        color_photo_effect = AddColorPhotoEffect(60, 0, 0)
        color_map_effect = ColorMapPhotoEffect(2)

        self.effect_manager.add(green_screen)
        self.effect_manager.add(color_map_effect)
        self.effect_manager.add(color_photo_effect)

    def apply(self, image):
        return self.effect_manager.apply_all(image)
