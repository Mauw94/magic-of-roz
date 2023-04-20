from typing import Any
from entities.classes.class_type import ClassTypeEnum


class CharacterInfo():
    def __init__(self):
        self.stats = {}
        self.level = None
        self.name = None
        self.class_type = None

    def set_info(self, c_info: dict) -> None:
        self.set_name(c_info["name"])
        self.set_level(c_info["level"])
        self.set_stats(c_info["stats"])
        self.set_class_type(self._get_player_class_from_str(c_info["class"]))

    def get_normal_damage(self) -> int:
        return self.stats["ap"]

    def get_name(self) -> str:
        return self.name

    def set_name(self, n: str) -> None:
        self.name = n

    def set_level(self, l: int) -> None:
        self.level = l

    def set_stats(self, stats: dict) -> None:
        self.stats = stats

    def set_class_type(self, class_t: ClassTypeEnum):
        self.class_type = class_t

    def get_stats(self) -> dict:
        return self.stats

    def get_class(self) -> ClassTypeEnum:
        return self.class_type
    
    def get_all_char_info(self) -> dict:
        return {
            "stats": self.get_stats(),
            "level": self.level,
            "name": self.name,
            "class": self.class_type.name
        }

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