from typing import Tuple
from entities.enemies.zombie_enemy import ZombieEnemey
from helpers.consts import Consts
import random


class EntitySpawnService:
    def __init__(self):
        self.enemy_spawn_locations = []
        self.max_distance_between = 100

    def spawn_zombie_enemy(self, hpbar_list) -> ZombieEnemey:
        x, y = self.__determine_x_y()
        zombie = ZombieEnemey(x, y, hpbar_list)
        self.enemy_spawn_locations.append([x, y])

        return zombie

    def clear_spawn_locations(self):
        self.enemy_spawn_locations = []

    def __determine_x_y(self) -> Tuple[int, int]:
        x = random.randrange(Consts.SCREEN_WIDTH)
        y = random.randrange(Consts.SCREEN_HEIGHT)

        for point in self.enemy_spawn_locations:
            x_diff = abs(point[0] - x)
            y_diff = abs(point[1] - y)

            if x_diff < self.max_distance_between or y_diff < self.max_distance_between:
                self.__determine_x_y()

        return x, y
