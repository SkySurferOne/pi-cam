from camera.PhotoEffects import EffectBundle, ColorMapPhotoEffect


class SunnyEffectBundle(EffectBundle):

    def __init__(self) -> None:
        super().__init__()

        color_map_effect = ColorMapPhotoEffect(4)

        self.effect_manager.add(color_map_effect)

    def apply(self, image):
        return self.effect_manager.apply_all(image)
