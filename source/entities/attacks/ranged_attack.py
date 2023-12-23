import arcade
import random
from helpers.texture_loader import TextureLoader
from helpers.consts import Consts
from managers.resource_managers.sound_manager import SoundManager
from helpers.logging.logger import Logger

class RangedAttack(arcade.Sprite):
    texture_loader = TextureLoader("RangedAttackClass")

    def __init__(self, folder, file):
        super().__init__()

        self.sound_manager = SoundManager()
        self.sound_manager.set_preferred_sound_volume(0.1)

        self._mana_cost = 0
        self._damage = 0

        self.mainPath = f":resources:images/{folder}/{file}"
        self.scale = Consts.SPRITE_SCALING_TILES
        self.sound = None

        self.texture_pair = self.texture_loader.load_texture_pair(
            f"{self.mainPath}.png")
        self.texture = self.texture_pair[0]
        self.set_hit_box(self.texture.hit_box_points)

    def play_shooting_sound(self):
        if self.sound is not None:
            self.sound_manager.play_sound(self.sound)

    def get_mana_cost(self) -> int:
        return self._mana_cost

    def set_mana_cost(self, cost) -> None:
        self._mana_cost = cost

    def get_damage(self) -> int:
        # keep some variance in the damage numbers so it isn't always the same.
        max_variance = self._damage // 10

        if max_variance == 0:
            max_variance += 2
        elif max_variance == 1:
            max_variance += 1
            
        offset = random.randint(1, max_variance)
        sign = random.randint(1, 2)
        
        if sign == 1:
            return self._damage + offset
        elif sign == 2:
            return self._damage - offset
        else:
            return self._damage

    def set_damage(self, d) -> None:
        self._damage = d
