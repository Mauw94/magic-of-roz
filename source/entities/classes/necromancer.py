from entities.classes.class_type import ClassType
from entities.player.player import Player
from helpers.consts import Consts
from helpers.logging.logger import Logger
from entities.player.character_info import CharacterInfo


class Necromancer(Player):
    def __init__(self, c_info: dict):
        super().__init__()

        Logger.log_object_creation("Creating NECROMANCER", "NecromancerClass")

        self.character_info = self._create_char_stats(c_info)

    def _create_char_stats(self, c_info: dict) -> CharacterInfo:
        c_stats = CharacterInfo()
        c_stats.set_name(c_info["name"])
        c_stats.set_level(c_info["level"])
        c_stats.set_stats(c_info["stats"])
        c_stats.set_class_type(ClassType.NECROMANCER)

        return c_stats
