from data.mongodb_connector import get_database
from entities.player.player import Player
from entities.classes.class_type import ClassType
from entities.player.character_info import CharacterInfo

CHARACTERS_COLLECTION = "characters"

class CharactersManager():
    
    def __init__(self):
        self.db = get_database()
        self.collection = self.db[CHARACTERS_COLLECTION]
        
    def get_player_characters(self) -> list:
        return list(self.collection.find())

    def save_player_character_info(self, name: str, class_type: ClassType) -> None:
        base_stats = self._get_base_stats_for_class(class_type)
        
        c = CharacterInfo()
        c.set_stats(base_stats)
        c.set_name(name)
        c.set_level(1)
        c.set_class_type(class_type)
        
        c_info = c.get_all_char_info()
        self.collection.insert_one(c_info)
    
    def load_player_object(self, c_info) -> Player:
        print(c_info)
    
    def _get_base_stats_for_class(self, c) -> dict:
        match c:
            case ClassType.NECROMANCER:
                return self._necromancer_base_stats()
            case ClassType.WARRIOR:
                pass
            case ClassType.DRUID:
                pass
            case ClassType.WIZARD:
                pass
            case _:
                raise Exception("unkown class type")
    
    def _necromancer_base_stats(self) -> dict:
        return {
            "hp": 90,
            "ap": 5,
            "as": 1.1,
            "mana": 100,
            "intelligence": 11,
            "strength": 3,
            "dexterity": 5,
            "fire_res": 15,
            "cold_res": 15,
            "lightning_res": 15
        }
    
    def _druid_base_stats(self) -> dict:
        return {
            "hp": 95,
            "ap": 7,
            "as": 0.8,
            "mana": 70,
            "intelligence": 8,
            "strength": 6,
            "dexterity": 5,
            "fire_res": 15,
            "cold_res": 15,
            "lightning_res": 15
        }
    
    def _wizard_base_stats(self) -> dict:
        return {
            "hp": 80,
            "ap": 9,
            "as": 0.8,
            "mana": 110,
            "intelligence": 12,
            "strength": 3,
            "dexterity": 4,
            "fire_res": 15,
            "cold_res": 15,
            "lightning_res": 15
        }
    
    def _warrior_base_stats(self) -> dict:
        return {
            "hp": 110,
            "ap": 7,
            "as": 1,
            "mana": 60,
            "intelligence": 3,
            "strength": 11,
            "dexterity": 5,
            "fire_res": 15,
            "cold_res": 15,
            "lightning_res": 15
        }
    
    def _get_player_class_from_str(self, c: str) -> ClassType:
        match c:
            case "druid":
                return ClassType.DRUID
            case "warrior":
                return ClassType.WARRIOR
            case "necromancer":
                return ClassType.NECROMANCER
            case "wizard":
                return ClassType.WIZARD
            case _:
                raise Exception("unkown class type")