from entities.items.item_base import ItemBase


class Inventory:
    def __init__(self):
        self.__space = 5
        self.inventory: list[ItemBase] = []

    def add_item(self, item: ItemBase) -> bool:
        if len(self.inventory) < 5:
            self.inventory.append(item)
            return True
        return False

    def get_item(self, index: int) -> ItemBase:
        if len(self.inventory) > 0:
            return self.inventory[index]

    def get_items(self) -> list[ItemBase]:
        return self.inventory
