from typing import Any
from entities.classes.class_type import ClassTypeEnum
from helpers.logging.logger import Logger


class CharacterInfo:
    def __init__(self):
        self.stats: dict = {}
        self.level: int = None
        self.current_experience: int = None
        self.name: str = None
        self.class_type: ClassTypeEnum = None
        self.gold: int = 0
        self.u_id: str = None

    def set_info(self, character_info: dict) -> None:
        self.set_name(character_info["name"])
        self.set_level(character_info["level"])
        self.set_current_experience(character_info["current_experience"])
        self.set_stats(character_info["stats"])
        self.set_class_type(self._get_player_class_from_str(character_info["class"]))
        self.set_u_id(character_info["u_id"])
        self.set_gold(character_info["gold"])

    def get_normal_damage(self) -> int:
        return self.stats["ap"]

    def get_special_damage(self) -> int:
        return self.stats["ap"] * 2

    def get_name(self) -> str:
        return self.name

    def get_current_experience(self) -> int:
        return self.current_experience

    def get_uid(self) -> str:
        return self.u_id

    def get_gold(self) -> int:
        return self.gold

    def set_name(self, n: str) -> None:
        self.name = n

    def set_level(self, l: int) -> None:
        self.level = l

    def set_gold(self, gold: int) -> None:
        self.gold = gold

    def set_current_experience(self, cur_exp: int) -> None:
        Logger.log_info("Updating player experience")
        self.current_experience = cur_exp

    def add_experience(self, experience: int) -> None:
        Logger.log_info("Player gains experience: " + str(experience))
        self.current_experience += experience
        if self.current_experience >= 100:
            self.level += 1
            temp_xp = self.current_experience
            self.current_experience = 100 - temp_xp

    def add_gold(self, gold: int) -> None:
        Logger.log_info("Player gains gold: " + str(gold))
        self.gold += gold

    def set_stats(self, stats: dict) -> None:
        self.stats = stats

    def set_class_type(self, class_t: ClassTypeEnum):
        self.class_type = class_t

    def set_u_id(self, u_id: str) -> None:
        self.u_id = u_id

    def get_stats(self) -> dict:
        return self.stats

    def get_class(self) -> ClassTypeEnum:
        return self.class_type

    def get_all_char_info(self) -> dict:
        return {
            "stats": self.get_stats(),
            "level": self.level,
            "name": self.name,
            "class": self.class_type.name,
            "current_experience": self.current_experience,
            "u_id": self.u_id,
            "gold": self.gold,
        }

    def get_level(self) -> int:
        return self.level

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
