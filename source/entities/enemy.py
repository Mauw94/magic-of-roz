from collections import defaultdict
import heapq
from typing import List, Tuple

import arcade
from entities.entity import Entity
from helpers.consts import Consts
from helpers.texture_loader import TextureLoader
from game_objects.health_bar import HealthBar


class Enemy(Entity):
    texture_loader = TextureLoader("EnemyClass")

    def __init__(self, folder, file, x, y):
        super().__init__(folder, file)

        self.should_update_walk = 0
        self.health = Consts.MAX_ENEMY_HEALTH

        self.hit_sound = None
        self.attack = None

        self.health_bar = HealthBar(
            self, 75, 4, (self.center_x, self.center_y))

        self.center_x = x
        self.center_y = y

        self.can_drop_item = False
        self.drop_chance_range = (0, 0)

    def get_hp_bar(self) -> Tuple[arcade.SpriteSolidColor, arcade.SpriteSolidColor]:
        return self.health_bar.get_hp_bar()

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
        if self.health < 0:
            self.health = 0
        self.health_bar.fullness = self.health / Consts.MAX_ENEMY_HEALTH

    def __play_hit_sound(self):
        if self.hit_sound is not None:
            self.sound_manager.play_sound(self.hit_sound)

class Pathfinding:
    def __init__(self, w, h):
        self.point_reached = False
        self.width = w
        self.height = h
        self.grid = {}
    
    def init_grid(self, w, h):
        for x in range(w):
            for y in range(h):
                self.grid[(x, y)] = 1
    
    def reset(self, w, h) -> None:
        self.grid = {}
        self.width = w
        self.height = h
        
    def find_path(self, start: Tuple[int, int], end: Tuple[int, int]) -> set:
        distances = {node: float('inf') for node in self.grid}
        distances[start] = 0
        visited = set()
        queue = [(0, start)]
        
        while queue:
            cur_d, cur_node = queue.pop()
            if cur_node in visited:
                continue
            if cur_node == end:
                return visited
                # return distances[cur_node]
            if cur_d > distances[cur_node]:
                continue
            visited.add(cur_node)
            
            for n in self.__neighbours(cur_node[0], cur_node[1]):
                weight = self.grid[n]
                distance = cur_d + weight
                if distance < distances[n]:
                    distances[n] = distance
                    heapq.heappush(queue, (distance, n))
            
        return visited
            
    
    def __neighbours(self, x, y) -> List[int]:
        n = []
        n.append((x - 1, y))
        n.append((x + 1, y))
        n.append((x, y - 1))
        n.append((x, y + 1))
        
        return [x for x in n if x[0] >= 0 and x[0] < self.width and x[1] >= 0 and x[1] < self.height]