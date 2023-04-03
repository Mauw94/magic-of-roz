from entities.entity import Entity
from helpers.consts import Consts
from helpers.texture_loader import TextureLoader
from game_objects.health_bar import HealthBar
import arcade


class Enemy(Entity):
    texture_loader = TextureLoader("EnemyClass")

    def __init__(self, folder, file, x, y,  bar_list):
        super().__init__(folder, file)

        self.should_update_walk = 0
        self.health = Consts.MAX_ENEMY_HEALTH

        self.hit_sound = None
        self.attack = None

        self.health_bar = HealthBar(
            self, bar_list, 75, 4, (self.center_x, self.center_y))

        self.center_x = x
        self.center_y = y

    def update(self):
        # Update the enemy's health bar pos
        self.health_bar.position = (
            self.center_x, self.center_y + 32)  # 32 is the offset

        self.update_animation(self)
        return super().update()

    def update_animation(self, delta_time: float = 1 / 60):
        if self.change_x < 0 and self.facing_direction == Consts.RIGHT_FACING:
            self.facing_direction = Consts.LEFT_FACING
        elif self.change_x > 0 and self.facing_direction == Consts.LEFT_FACING:
            self.facing_direction = Consts.RIGHT_FACING

        if self.change_x == 0:
            self.texture = self.idle_texture_pair[self.facing_direction]

        if self.should_update_walk == 3:
            self.cur_texture += 1
            if self.cur_texture > 7:
                self.cur_texture = 0
            self.texture = self.walk_textures[self.cur_texture][self.facing_direction]
            self.should_update_walk = 0
            return

        self.should_update_walk += 1

    def hit(self, damage):
        self.__play_hit_sound()
        self.health -= damage
        self.health_bar.fullness = self.health / Consts.MAX_ENEMY_HEALTH

    def __play_hit_sound(self):
        if self.hit_sound is not None:
            self.sound_manager.play_sound(self.hit_sound)
