from camera.PhotoEffects import ColorMapPhotoEffect
from camera.PhotoEffects import EffectBundle, AddObjectsPhotoEffect
from camera.PhotoEffects import GreenScreenPhotoEffect
from camera.PhotoEffects import EffectBundle, AddObjectsPhotoEffect
from camera.PhotoEffects import GreenScreenPhotoEffect



class SkiingEffectBundle(EffectBundle):

    def __init__(self) -> None:
        super().__init__()

        green_screen = GreenScreenPhotoEffect('slope.png', 'green')
        # color_map_effect = ColorMapPhotoEffect(7)
        object_effect = AddObjectsPhotoEffect('goggles.png',AddObjectsPhotoEffect.ObjectPositionEnum.ON)

        self.effect_manager.add(green_screen)
        # self.effect_manager.add(color_map_effect)
        self.effect_manager.add(object_effect)

    def apply(self, image):
        return self.effect_manager.apply_all(image)


