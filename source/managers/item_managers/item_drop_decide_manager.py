from entities.items.item_base import ItemBase
from helpers.random import get_random
from entities.items.item_type import ItemTypeEnum
from managers.item_managers.item_generator import ItemGenerator
from helpers.logging.logger import Logger


class ItemDropDecideManager:
    def __init__(self):
        self._item_generator = ItemGenerator()

    def drop(self, x, y) -> ItemBase:
        self.x_drop_loc = x
        self.y_drop_loc = y
        match self.__item_type_to_generate():
            case ItemTypeEnum.CONSUMABLE:
                return self.__generate_consumable()
            case ItemTypeEnum.WEARABLE:
                return self.__generate_wearable()

    def __generate_consumable(self) -> ItemBase:
        return self._item_generator.determine_consumable_item(self.x_drop_loc, self.y_drop_loc)

    def __generate_wearable(self) -> ItemBase:
        return self._item_generator.determine_wearable_item(self.x_drop_loc, self.y_drop_loc)

    def __item_type_to_generate(self) -> ItemTypeEnum:
        match get_random(0, len(ItemTypeEnum) - 1):
            case 0:
                return ItemTypeEnum.CONSUMABLE
            case 1:
                return ItemTypeEnum.WEARABLE
            case _:
                Logger.log_error(
                    "Tried to generate itemtype that does not exist")
