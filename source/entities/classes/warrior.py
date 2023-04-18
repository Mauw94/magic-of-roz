from entities.player.player import Player
from helpers.logging.logger import Logger
from entities.player.character_info import CharacterInfo


class Warrior(Player):
    def __init__(self, c_info: dict):
        super().__init__()

        Logger.log_object_creation("Creating a Warrior", "WarriorClass")

        self.character_info = self._create_char_stats(c_info)

    def _create_char_stats(self, c_info: dict) -> CharacterInfo:
        c_stats = CharacterInfo()
        c_stats.set_info(c_info)

        return c_stats
