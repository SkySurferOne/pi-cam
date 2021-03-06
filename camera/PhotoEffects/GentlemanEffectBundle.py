from camera.PhotoEffects import ColorMapPhotoEffect
from camera.PhotoEffects import EffectBundle, AddObjectsPhotoEffect


class GentlemanEffectBundle(EffectBundle):

    def __init__(self) -> None:
        super().__init__()

        color_map_effect = ColorMapPhotoEffect(2)
        object_effect = AddObjectsPhotoEffect('gentleman.png', AddObjectsPhotoEffect.ObjectPositionEnum.ON)

        self.effect_manager.add(object_effect)
        self.effect_manager.add(color_map_effect)

    def apply(self, image):
        return self.effect_manager.apply_all(image)
