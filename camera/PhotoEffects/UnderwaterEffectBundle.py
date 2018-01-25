from camera.PhotoEffects import ColorMapPhotoEffect
from camera.PhotoEffects import EffectBundle, AddObjectsPhotoEffect
from camera.PhotoEffects import GreenScreenPhotoEffect



class UnderwaterEffectBundle(EffectBundle):

    def __init__(self) -> None:
        super().__init__()

        green_screen = GreenScreenPhotoEffect('underwater.png', 'red')
        color_map_effect = ColorMapPhotoEffect(4)
        object_effect = AddObjectsPhotoEffect('snorkel.png',AddObjectsPhotoEffect.ObjectPositionEnum.AROUND)

        self.effect_manager.add(green_screen)
        self.effect_manager.add(color_map_effect)
        self.effect_manager.add(object_effect)

    def apply(self, image):
        return self.effect_manager.apply_all(image)


