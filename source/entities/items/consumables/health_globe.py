from entities.items.item_base import ItemBase


class HealthGlobe(ItemBase):
    def __init__(self, x, y):
        super().__init__("items", "gemRed")
        
        self.center_x = x
        self.center_y = y
        
        # how much hp can be restored?
        # where is it determined how much hp can be restored?
    
    
    