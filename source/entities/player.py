from helpers.consts import Consts
from entities.entity import Entity

class Player(Entity):
    def __init__(self):
        super().__init__("male_person", "malePerson")
    
    def update_animation(self, delta_time: float = 1 / 60):
        if self.change_x < 0 and self.facing_direction == Consts.RIGHT_FACING:
            self.facing_direction = Consts.LEFT_FACING
        elif self.change_x > 0 and self.facing_direction == Consts.LEFT_FACING:
            self.facing_direction = Consts.RIGHT_FACING
        
        if self.change_x == 0:
            self.texture = self.idle_texture_pair[self.facing_direction]
            return
        
        self.cur_texture += 1
        if self.cur_texture > 7:
            self.cur_texture = 0
        self.texture = self.walk_textures[self.cur_texture][self.facing_direction]