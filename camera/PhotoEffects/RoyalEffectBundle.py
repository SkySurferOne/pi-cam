from camera.PhotoEffects import EffectBundle, AddObjectsPhotoEffect
from camera.PhotoEffects import GreenScreenPhotoEffect



class RoyalEffectBundle(EffectBundle):

    def __init__(self) -> None:
        super().__init__()

        green_screen = GreenScreenPhotoEffect('palace.png', 'green')
        object_effect = AddObjectsPhotoEffect('crown.png', AddObjectsPhotoEffect.ObjectPositionEnum.ABOVE)

        self.effect_manager.add(green_screen)
        self.effect_manager.add(object_effect)

    def apply(self, image):
        return self.effect_manager.apply_all(image)


