from entities.items.item_base import ItemBase
from helpers.random import get_random
from entities.items.item_type import ItemTypeEnum
from managers.item_managers.item_generator import ItemGenerator
from helpers.logging.logger import Logger
from entities.enemy import Enemy


class ItemDropDecideManager:
    def __init__(self):
        self._item_generator = ItemGenerator()
        self.min_drop_chance_seed = None
        self.max_drop_chance_seed = None

    def set_drop_chance_seed(self, min, max) -> None:
        self.min_drop_chance_seed = min
        self.max_drop_chance_seed = max

    def get_drop_chance_seeed(self) -> ():
        return (self.min_drop_chance_seed, self.max_drop_chance_seed)

    def decide_if_item_can_drop(self, enemy: Enemy) -> bool:
        if enemy.can_drop_item == False:
            return False

        if (
            self.min_drop_chance_seed is not None
            and self.max_drop_chance_seed is not None
        ):
            chance = get_random(self.min_drop_chance_seed, self.max_drop_chance_seed)
        else:
            chance = get_random(0, 1000)

        return (
            enemy.drop_chance_range[1] >= chance
            and enemy.drop_chance_range[0] <= chance
        )

    def drop(self, x, y) -> ItemBase:
        self.x_drop_loc = x
        self.y_drop_loc = y
        match self.__item_type_to_generate():
            case ItemTypeEnum.CONSUMABLE:
                return self.__generate_consumable()
            case ItemTypeEnum.WEARABLE:
                return self.__generate_wearable()
            case ItemTypeEnum.GOLD:
                return self.__generate_gold_coin()

    def __generate_gold_coin(self) -> ItemBase:
        return self._item_generator.gen_gold_coin(self.x_drop_loc, self.y_drop_loc)

    def __generate_consumable(self) -> ItemBase:
        return self._item_generator.determine_consumable_item(
            self.x_drop_loc, self.y_drop_loc
        )

    def __generate_wearable(self) -> ItemBase:
        return self._item_generator.determine_wearable_item(
            self.x_drop_loc, self.y_drop_loc
        )

    def __item_type_to_generate(self) -> ItemTypeEnum:
        match get_random(0, len(ItemTypeEnum) - 1):
            case 0:
                return ItemTypeEnum.CONSUMABLE
            case 1:
                return ItemTypeEnum.WEARABLE
            case 2:
                return ItemTypeEnum.GOLD
            case _:
                Logger.log_error("Tried to generate itemtype that does not exist")
