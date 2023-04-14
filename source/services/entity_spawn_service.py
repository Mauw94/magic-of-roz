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
        self._cur_wave = 0
        self._zombies_to_spawn = 0
        self._cur_level = 1  # level will stay 1 for now

    def set_zombies_to_spawn_in_wave(self, zombies) -> None:
        self._zombies_to_spawn = zombies

    def set_spawn_timer(self, st) -> None:
        self._spawn_timer = st

    # spawns multiple zombies at once
    # n of zombies set beforehand
    def spawn_zombie_wave(self) -> list[ZombieEnemy]:
        if self._zombies_to_spawn == 0:
            raise Exception("Define numbers of zombies to spawn")

        self._cur_t += 1
        if self._cur_t == self._spawn_timer:
            self._cur_t = 0
            self._cur_wave += 1

            # increase zombies to spawn every 3 waves
            if self._cur_wave % 3 == 0:
                self._zombies_to_spawn *= 1.5
                self._zombies_to_spawn = int(self._zombies_to_spawn)

            # spawn zombies
            z = []
            for _ in range(self._zombies_to_spawn):
                x, y = self.__determine_x_y()
                z.append(ZombieEnemy(x, y))

            return z
        else:
            return None

    def spawn_zombie(self) -> ZombieEnemy:
        self._cur_t += 1
        if self._cur_t == self._spawn_timer:
            self._cur_t = 0
            x, y = self.__determine_x_y()
            zombie = ZombieEnemy(x, y)
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
