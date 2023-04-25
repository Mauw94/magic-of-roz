from enum import Enum

from helpers.random import get_random
from entities.items.consumables.health_globe import HealthGlobe
from entities.items.consumables.mana_globe import ManaGlobe
from helpers.logging.logger import Logger
from entities.items.item_base import ItemBase


class ConsumableItemsEnum(Enum):
    HEALTH_GLOBE = 0,
    MANA_GLOBE = 1
    
class ItemGenerator:
    def __init__(self):
        pass
    
    def determine_wearable_item(self, x, y) -> ItemBase:
        pass
    
    def determine_consumable_item(self, x, y) -> ItemBase:
        match get_random(0, len(ConsumableItemsEnum) - 1):
            case 0:
                return self.gen_health_globe(x, y)
            case 1:
                return self.gen_mana_globe(x, y)
            case _:
                Logger.log_error("Tried to generate item consumable type that does not exist")

    def gen_health_globe(self, x, y) -> HealthGlobe:
        Logger.log_object_creation("HealthGlobe", "ItemGenerator")
        return HealthGlobe(x, y)
    
    def gen_mana_globe(self, x, y) -> ManaGlobe:
        Logger.log_object_creation("ManaGlobe", "ItemGenerator")
        return ManaGlobe(x, y)