from entities.enemy import Enemy
from helpers.consts import Consts
import random
import arcade

class ZombieEnemey(Enemy):
    def __init__(self):
        super().__init__("zombie", "zombie")
        
        self.max_move_x = 120 # max movement to x
        self.max_move_y = 120 # max movement to y
        self.steps = 0 # steps
        
        self.horizontal = True
        self.vertical = False
        self.change_y = 0
        self.change_x = 2
        self.hit_sound = arcade.load_sound(":resources:sounds/hit5.wav")
    
    def update(self):
        self.steps += 1
        
        if self.steps >= self.max_move_x:
            if self.facing_direction == Consts.RIGHT_FACING:
                self.facing_direction = Consts.LEFT_FACING
            elif self.facing_direction == Consts.LEFT_FACING:
                self.facing_direction = Consts.RIGHT_FACING
        
            self.change_x *= -1
            self.steps = 0
                
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
        