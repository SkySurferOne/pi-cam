from camera.PhotoEffects import EffectBundle, AddObjectsPhotoEffect
from camera.constants import ASSETS_DIR



class RoyalEffectBundle(EffectBundle):

    def __init__(self) -> None:
        super().__init__()

        object_effect = AddObjectsPhotoEffect(ASSETS_DIR + 'crown.png',
                                                                    AddObjectsPhotoEffect.ObjectPositionEnum.ABOVE)

        self.effect_manager.add(object_effect)

    def apply(self, image):
        return self.effect_manager.apply_all(image)
