from entities.enemy import Enemy
from helpers.consts import Consts
from entities.attacks.enemy_attacks.zombie_attack import ZombieAttack
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from views.game_view import GameView
import random
import arcade
import math
from game_objects.health_bar import HealthBar


class ZombieEnemey(Enemy):
    def __init__(self, bar_list):
        super().__init__("zombie", "zombie", bar_list)

        self.max_move_x = 120  # max movement to x
        self.max_move_y = 120  # max movement to y
        self.steps = 0  # steps

        self.horizontal = True
        self.vertical = False
        self.change_y = 0
        self.change_x = 2
        self.hit_sound = arcade.load_sound(":resources:sounds/hit5.wav")

        self.attack_timer = 0
        self.__attack_interval = 200
        self.attack = None

    def update(self):
        self.__move_n_steps_horizontal(self.max_move_x)
        return super().update()

    def move_random_up_down(self):
        self.steps += 1

        if self.horizontal:
            self.change_x = 2
            self.change_y = 0
            if self.steps >= self.max_move_x:
                if self.facing_direction == Consts.RIGHT_FACING:
                    self.facing_direction = Consts.LEFT_FACING
                elif self.facing_direction == Consts.LEFT_FACING:
                    self.facing_direction = Consts.RIGHT_FACING

                self.change_x *= -1
                self.steps = 0
                self.set_new_dir()

        if self.vertical:
            self.change_x = 0
            self.change_y = 2
            if self.steps >= self.max_move_y:
                self.change_y *= -1
                self.steps = 0
                self.set_new_dir()

    def set_new_dir(self):
        if random.randrange(0, 2) == 0:
            print("0")
            self.horizontal = True
            self.vertical = False
        elif random.randrange(0, 2) == 1:
            print("1")
            self.horizontal = False
            self.vertical = True

    def ranged_attack(self, game: 'GameView'):
        self.attack = ZombieAttack()
        if self.attack_timer >= self.__attack_interval:
            self.attack_player(game)
            game.scene.add_sprite("Attacks", self.attack)
            self.attack_timer = 0

        self.attack_timer += 1

    def attack_player(self, game: 'GameView'):
        curplayer_x = game.player.center_x
        curplayer_y = game.player.center_y

        self.attack.center_x = self.center_x
        self.attack.center_y = self.center_y

        x_diff = curplayer_x - self.attack.center_x
        y_diff = curplayer_y - self.attack.center_y

        angle = math.atan2(y_diff, x_diff)

        self.attack.angle = math.degrees(angle)
        if self.attack.angle < 0:
            self.attack.angle += 360
        self.attack.change_x = math.cos(angle) * 5
        self.attack.change_y = math.sin(angle) * 5

    def __move_n_steps_horizontal(self, steps):
        self.steps += 1

        if self.steps >= steps:
            if self.facing_direction == Consts.RIGHT_FACING:
                self.facing_direction = Consts.LEFT_FACING
            elif self.facing_direction == Consts.LEFT_FACING:
                self.facing_direction = Consts.RIGHT_FACING

            self.change_x *= -1
            self.steps = 0
