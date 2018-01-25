from camera.PhotoEffects import AddColorPhotoEffect
from camera.PhotoEffects import EffectBundle, AddObjectsPhotoEffect
from camera.PhotoEffects import GreenScreenPhotoEffect
from camera.constants import ASSETS_DIR



class BeachEffectBundle(EffectBundle):

    def __init__(self) -> None:
        super().__init__()

        green_screen = GreenScreenPhotoEffect('beach.png', 'red')
        color_photo_effect = AddColorPhotoEffect(r=30, g=0, b=0)
        object_effect = AddObjectsPhotoEffect('sunglasses.png',AddObjectsPhotoEffect.ObjectPositionEnum.ON)

        self.effect_manager.add(green_screen)
        self.effect_manager.add(color_photo_effect)
        self.effect_manager.add(object_effect)

    def apply(self, image):
        return self.effect_manager.apply_all(image)


