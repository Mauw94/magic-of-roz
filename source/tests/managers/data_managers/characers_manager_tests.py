import unittest
import mongomock
from managers.data_managers.characters_manager import CharactersManager


class CharactersManagerTests(unittest.TestCase):
    
    def test_getting_player_characters(self):
        characters = self.manager.get_player_characters()
        
        assert len(characters) == 2

    def setUp(self):
        self.manager = CharactersManager(self.__mock_collection())
    
    def __mock_collection(self):
        collection = mongomock.MongoClient().db.collection
        objects = [dict({}), dict({})]
        for o in objects:
            collection.insert_one(o)
        
        return collection