from entities.entity import Entity
from helpers.consts import Consts
from helpers.texture_loader import TextureLoader
import arcade

class Enemy(Entity):
    def __init__(self, folder, file):
        super().__init__(folder, file)
        self.texture_loader = TextureLoader()
        
        self.should_update_walk = 0
        self.boundary_left = 200 
        self.boundary_right = 200 
        self.boundary_bottom = 200 
        self.boundary_top = 200      
        self.health = 50
    
        self.hit_sound = None
        self.attack = None
    
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
    
    def play_hit_sound(self):
        if self.hit_sound is not None:
            arcade.play_sound(self.hit_sound)
   