from entities.items.item_base import ItemBase


class HealthGlobe(ItemBase):
    def __init__(self, x, y):
        super().__init__("items", "gemRed")

        self.center_x = x
        self.center_y = y

        self.value = 15
