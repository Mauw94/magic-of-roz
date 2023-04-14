from typing import Tuple
from entities.enemies.zombie_enemy import ZombieEnemy
from helpers.consts import Consts
from helpers.logging.logger import Logger
import random


class EntitySpawnService:
    def __init__(self):
        self.enemy_spawn_locations = []
        self.max_distance_between = 100
        
        self._spawn_timer = 0
        self._cur_t = 0

    def set_spawn_timer(self, st) -> None:
        self._spawn_timer = st
        
    def spawn_zombie_enemy(self) -> ZombieEnemy:
        # more logic to spawn more and faster during level, depending on level etc
        self._cur_t += 1
        if self._cur_t == self._spawn_timer:            
            x, y = self.__determine_x_y()
            zombie = ZombieEnemy(x, y)
            self.enemy_spawn_locations.append([x, y])

            Logger.log_info("Spawning enemy")

            self._cur_t = 0
            
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
