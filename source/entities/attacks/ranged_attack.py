import arcade
from helpers.texture_loader import TextureLoader
from helpers.consts import Consts


class RangedAttack(arcade.Sprite):
    texture_loader = TextureLoader("RangedAttackClass")

    def __init__(self, folder, file):
        super().__init__()

        self.damage = 0
        self.mainPath = f":resources:images/{folder}/{file}"
        self.scale = Consts.SPRITE_SCALING_TILES
        self.sound = None

        self.texture_pair = self.texture_loader.load_texture_pair(
            f"{self.mainPath}.png")
        self.texture = self.texture_pair[0]
        self.set_hit_box(self.texture.hit_box_points)

    def play_shooting_sound(self):
        if self.sound is not None:
            arcade.play_sound(self.sound)
