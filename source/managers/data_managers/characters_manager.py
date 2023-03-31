from data.mongodb_connector import get_database
from entities.player.player import Player
from entities.classes.class_type import ClassType
from entities.player.character_info import CharacterInfo
from managers.data_managers.characters_stat_manager import CharactersStatManager

CHARACTERS_COLLECTION = "characters"

class CharactersManager():
    
    def __init__(self):
        self.db = get_database()
        self.collection = self.db[CHARACTERS_COLLECTION]
        self.c_stat_manager = CharactersStatManager()
        
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
                return self.c_stat_manager.necromancer_base_stats()
            case ClassType.WARRIOR:
                return self.c_stat_manager.warrior_base_stats()
            case ClassType.DRUID:
                return self.c_stat_manager.druid_base_stats()
            case ClassType.WIZARD:
                return self.c_stat_manager.wizard_base_stats()
            case _:
                raise Exception("unkown class type")

    def _get_player_class_from_str(self, c: str) -> ClassType:
        match c.upper():
            case "DRUID":
                return ClassType.DRUID
            case "WARRIOR":
                return ClassType.WARRIOR
            case "NECROMANCER":
                return ClassType.NECROMANCER
            case "WIZARD":
                return ClassType.WIZARD
            case _:
                raise Exception("unkown class type")