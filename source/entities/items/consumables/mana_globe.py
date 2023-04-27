from entities.items.item_base import ItemBase

# adds n to mana


class ManaGlobe(ItemBase):
    def __init__(self, x, y):
        super().__init__("items", "gemBlue")

        self.center_x = x
        self.center_y = y

        self.add_mana = 50
