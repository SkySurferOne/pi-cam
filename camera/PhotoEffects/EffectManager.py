from camera.PhotoEffects import PhotoEffect


class EffectManager:

    def __init__(self) -> None:
        self.effects = []

    def add(self, photo_effect: PhotoEffect):
        self.effects.append(photo_effect)

    def apply_all(self, img):
        for pe in self.effects:
            img = pe.apply_filter(img)

        return img
