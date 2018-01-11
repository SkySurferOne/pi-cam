from camera.PhotoEffects import EffectBundle, AddObjectsPhotoEffect



class GentelmanEffectBundle(EffectBundle):

    def __init__(self) -> None:
        super().__init__()

        object_effect = AddObjectsPhotoEffect.AddObjectsPhotoEffect('mustache-and-glasses.jpg',
                                                                    AddObjectsPhotoEffect.AddObjectsPhotoEffect.ObjectPositionEnum.ON)

        self.effect_manager.add(object_effect)

    def apply(self, image):
        return self.effect_manager.apply_all(image)