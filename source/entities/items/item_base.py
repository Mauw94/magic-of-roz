import arcade
from entities.items.item_type import ItemTypeEnum
from helpers.texture_loader import TextureLoader

class ItemBase(arcade.Sprite):
    texture_loader = TextureLoader("ItemBaseClass")
    
    def __init__(self, type: ItemTypeEnum, folder, file):
        super().__init__()
        
        self.type = type
        
        path = f":resources:images/{folder}/{file}.png"
        
        self.texture = self.texture_loader.load_texture(path)
        self.set_hit_box(self.texture.hit_box_points)
    
    def update(self):
        pass
    
    def update_animation(self, delta_time: float = 1 / 60):
        pass