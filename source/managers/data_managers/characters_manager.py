from entities.player.player import Player
from entities.classes.class_type import ClassTypeEnum
from entities.player.character_info import CharacterInfo
from managers.data_managers.characters_stat_manager import CharactersStatManager
from entities.classes.necromancer import Necromancer
from entities.classes.druid import Druid
from entities.classes.warrior import Warrior
from entities.classes.wizard import Wizard
from managers.data_managers.file_save_manager import save_new_character_info
import uuid


class CharactersManager:
    def __init__(self, characters: list):
        self.characters = characters
        self.c_stat_manager = CharactersStatManager()

    def get_player_characters(self) -> list:
        return self.characters

    def save_new_character_info(self, name: str, class_type: ClassTypeEnum) -> None:
        base_stats = self.c_stat_manager.get_base_stats_for_class(class_type)

        character_info = CharacterInfo()
        character_info.set_stats(base_stats)
        character_info.set_name(name)
        character_info.set_level(1)
        character_info.set_current_experience(0)
        character_info.set_class_type(class_type)
        character_info.set_u_id(str(uuid.uuid1()))
        character_info.set_gold(0)

        char_info = character_info.get_all_char_info()
        self.characters.append(char_info)
        save_new_character_info(char_info)

    def load_player_object(self, char_info: dict) -> Player:
        c_type = self._get_player_class_from_str(char_info["class"])
        match c_type:
            case ClassTypeEnum.NECROMANCER:
                return Necromancer(char_info)
            case ClassTypeEnum.DRUID:
                return Druid(char_info)
            case ClassTypeEnum.WARRIOR:
                return Warrior(char_info)
            case ClassTypeEnum.WIZARD:
                return Wizard(char_info)
            case _:
                raise Exception("unknown class type")

    def _get_player_class_from_str(self, c: str) -> ClassTypeEnum:
        match c.upper():
            case "DRUID":
                return ClassTypeEnum.DRUID
            case "WARRIOR":
                return ClassTypeEnum.WARRIOR
            case "NECROMANCER":
                return ClassTypeEnum.NECROMANCER
            case "WIZARD":
                return ClassTypeEnum.WIZARD
            case _:
                raise Exception("unkown class type")
