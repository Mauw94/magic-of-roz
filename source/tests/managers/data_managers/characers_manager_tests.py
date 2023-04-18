import unittest
import mongomock
from managers.data_managers.characters_manager import CharactersManager
from entities.classes.class_type import ClassType


class CharactersManagerTests(unittest.TestCase):

    def test_saving_player_character_info(self):
        self.manager.save_player_character_info("test123", ClassType.NECROMANCER)
        characters = self.manager.get_player_characters()
        
        assert len(characters) == 1
        assert characters[0]["name"] == "test123"
        
    def test_loading_player_object(self):
        n = "Player1"
        self.manager.save_player_character_info(n, ClassType.DRUID)
        chars = self.manager.get_player_characters()
        p = self.manager.load_player_object(chars[0])
        
        assert p.character_info.name == n
        assert p.character_info.get_name() == n
        assert p.character_info.class_type == ClassType.DRUID
        assert p.character_info.get_class() == ClassType.DRUID
    
    def setUp(self):
        self.manager = CharactersManager(self.__mock_collection())

    def __mock_collection(self):
        collection = mongomock.MongoClient().db.collection
        # objects = [dict({}), dict({})]
        # for o in objects:
        #     collection.insert_one(o)
        
        return collection