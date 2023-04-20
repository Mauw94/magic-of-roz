from entities.items.item_base import ItemBase
from helpers.random import get_random
from entities.items.item_type import ItemTypeEnum


class ItemDropDecideManager:
    def __init__(self):
        pass
    
    def drop(self) -> ItemBase:
        t = self.__item_type_to_generate()
        match t:
            case ItemTypeEnum.CONSUMABLE:
                return self.generate_consumable()
            case ItemTypeEnum.WEARABLE:
                return self.generate_wearable()
    
    def generate_consumable(self) -> ItemBase:
        print("generating consumable")
    
    def generate_wearable(self) -> ItemBase:
        print("generating wearable")
        
    def __item_type_to_generate(self) -> ItemTypeEnum:
        print(len(ItemTypeEnum))
        r = get_random(0, len(ItemTypeEnum) - 1)
        match r:
            case 0:
                return ItemTypeEnum.CONSUMABLE
            case 1:
                return ItemTypeEnum.WEARABLE
            case _:
                raise Exception("ItemType does not exist")