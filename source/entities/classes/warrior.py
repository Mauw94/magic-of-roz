from entities.player.player import Player
from helpers.logging.logger import Logger
from entities.player.character_info import CharacterInfo


class Warrior(Player):
    def __init__(self, c_info: dict):
        super().__init__(c_info)

        Logger.log_object_creation("Creating a Warrior", "WarriorClass")
