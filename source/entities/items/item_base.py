import arcade
from helpers.texture_loader import TextureLoader
from helpers.consts import Consts


class ItemBase(arcade.Sprite):
    texture_loader = TextureLoader("ItemBaseClass")

    def __init__(self, folder, file):
        super().__init__()

        path = f":resources:images/{folder}/{file}.png"

        self.scale = Consts.SPRITE_SCALING_PLAYER
        self.texture = self.texture_loader.load_texture(path)
        self.set_hit_box(self.texture.hit_box_points)
        self.value = 0

    def update(self):
        pass

    def update_animation(self, delta_time: float = 1 / 60):
        pass
