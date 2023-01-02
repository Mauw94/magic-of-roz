from entities.entity import Entity
from helpers.consts import Consts

class Enemy(Entity):
    def __init__(self, folder, file):
        super().__init__(folder, file)
        
        self.should_update_walk = 0
        self.boundary_left, self.boundary_right, self.boundary_bottom, self.boundary_top = 200
    
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