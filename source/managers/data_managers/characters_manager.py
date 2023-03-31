from data.mongodb_connector import get_database
from entities.player import Player
from entities.classes.class_type import ClassType

CHARACTERS_COLLECTION = "characters"

class CharactersManager():
    
    def __init__(self):
        self.db = get_database()
        self.collection = self.db[CHARACTERS_COLLECTION]
        
    def get_player_characters(self) -> list:
        return list(self.collection.find())

    def save_player_character_info(self, c) -> None:
        self.collection.insert_one(c)
    
    def load_player_object(self, c_info) -> Player:
        print(c_info)
    
    def get_player_class(self, c) -> ClassType:
        match c:
            case "druid":
                return ClassType.DRUID
            case "warrior":
                return ClassType.WARRIOR
            case "necromancer":
                return ClassType.NECROMANCER
            case "wizard":
                return ClassType.WIZARD
            case _:
                raise Exception("unkown class type")