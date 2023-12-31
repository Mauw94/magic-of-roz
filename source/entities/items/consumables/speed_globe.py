from entities.items.item_base import ItemBase


class SpeedGlobe(ItemBase):
    def __init__(self, x, y):
        super().__init__("items", "gemYellow")

        self.center_x = x
        self.center_y = y

        self.value = 20
