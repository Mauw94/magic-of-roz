import mongomock

from entities.player.player import Player
from managers.data_managers.characters_manager import CharactersManager
from entities.classes.class_type import ClassTypeEnum

# create mock character


def create_mock_character() -> Player:
    chars_manager = CharactersManager(__mock_collection())
    chars_manager.save_player_character_info("test1", ClassTypeEnum.WARRIOR)
    c = chars_manager.get_player_characters()
    p = chars_manager.load_player_object(c[0])
    p.setup()

    return p


def __mock_collection():
    return mongomock.MongoClient().db.collection
