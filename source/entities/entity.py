import arcade
from helpers.texture_loader import TextureLoader
from helpers.consts import Consts

class Entity(arcade.Sprite):
    texture_loader = TextureLoader()
    
    def __init__(self, folder, file):
        super().__init__()
        
        self.facing_direction = Consts.RIGHT_FACING
        
        self.cur_texture = 0
        self.scale = Consts.SPRITE_SCALING_PLAYER
        
        main_path = f":resources:images/animated_characters/{folder}/{file}"
        
        self.idle_texture_pair = self.texture_loader.load_texture_pair(
            f"{main_path}_idle.png")
        
        self.walk_textures = []
        for i in range(8):
            texture = self.texture_loader.load_texture_pair(
                f"{main_path}_walk{i}.png"
            )
            self.walk_textures.append(texture)
        
        self.texture = self.idle_texture_pair[0]
        self.set_hit_box(self.texture.hit_box_points)