from typing import Tuple
from entities.enemies.zombie_enemy import ZombieEnemey
from helpers.consts import Consts
from helpers.logging.logger import Logger
import random


class EntitySpawnService:
    def __init__(self):
        self.enemy_spawn_locations = []
        self.max_distance_between = 650
        Logger.log_object_creation(
            "EntitySpawnService", "EntitySpawnServiceClass")

    def spawn_zombie_enemy(self, hpbar_list) -> ZombieEnemey:
        x, y = self.__determine_x_y()
        zombie = ZombieEnemey(x, y, hpbar_list)
        self.enemy_spawn_locations.append([x, y])

        Logger.log_info("Spawning enemy")

        return zombie

    def clear_spawn_locations(self):
        self.enemy_spawn_locations = []

    def __determine_x_y(self) -> Tuple[int, int]:
        x = random.randrange(Consts.SCREEN_WIDTH)
        y = random.randrange(Consts.SCREEN_HEIGHT)

        for point in self.enemy_spawn_locations:
            manhatten_dist = abs((x - point[0])) + abs((y - point[1]))

            if manhatten_dist < self.max_distance_between:
                self.__determine_x_y()

        return x, y
