from entities.items.item_base import ItemBase


class TestArmour(ItemBase):
    def __init__(self, x, y):
        super().__init__("items", "coinSilver")

        self.center_x = x
        self.center_y = y
