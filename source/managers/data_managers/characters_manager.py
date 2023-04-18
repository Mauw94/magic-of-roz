from data.mongodb_connector import get_database
from entities.player.player import Player
from entities.classes.class_type import ClassType
from entities.player.character_info import CharacterInfo
from managers.data_managers.characters_stat_manager import CharactersStatManager
from entities.classes.necromancer import Necromancer
from entities.classes.druid import Druid
from entities.classes.warrior import Warrior
from entities.classes.wizard import Wizard

class CharactersManager():

    def __init__(self, collection):
        self.collection = collection
        self.c_stat_manager = CharactersStatManager()

        # test stuff
        # self.c_stat_manager.mutate_stats_off_level(ClassType.NECROMANCER, 3)

    def get_player_characters(self) -> list:
        return list(self.collection.find())

    def save_player_character_info(self, name: str, class_type: ClassType) -> None:
        base_stats = self.c_stat_manager.get_base_stats_for_class(class_type)

        c = CharacterInfo()
        c.set_stats(base_stats)
        c.set_name(name)
        c.set_level(1)
        c.set_class_type(class_type)

        c_info = c.get_all_char_info()
        self.collection.insert_one(c_info)

    def load_player_object(self, c_info: dict) -> Player:
        c_type = self._get_player_class_from_str(c_info["class"])
        match c_type:
            case ClassType.NECROMANCER:
                return Necromancer(c_info)
            case ClassType.DRUID:
                return Druid(c_info)
            case ClassType.WARRIOR:
                return Warrior(c_info)
            case ClassType.WIZARD:
                return Wizard(c_info)
            case _:
                raise Exception("unknown class type")

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
