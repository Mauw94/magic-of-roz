from entities.items.item_base import ItemBase
from entities.items.item_type import ItemTypeEnum


class HealthGlobe(ItemBase):
    def __init__(self, x, y):
        super().__init__(ItemTypeEnum.CONSUMABLE, "tiles", "torch1")
        
        self.center_x = x
        self.center_y = y
        
        # how much hp can be restored?
        # where is it determined how much hp can be restored?
    
    
    