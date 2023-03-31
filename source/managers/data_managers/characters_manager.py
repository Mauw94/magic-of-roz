import datetime
from data.mongodb_connector import get_database

CHARACTERS_COLLECTION = "characters"

class CharactersManager():
    
    def __init__(self):
        self.db = get_database()
        self.collection = self.db[CHARACTERS_COLLECTION]
        
    def get_player_characters(self, id) -> list:
        return list(self.collection.find())

    def save_player_character_info(self, c):
        self.collection.insert_one(c)