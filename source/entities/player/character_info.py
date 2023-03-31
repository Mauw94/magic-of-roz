from typing import Any
from entities.classes.class_type import ClassType


class CharacterInfo(): 
    def __init__(self):
        self.stats = {}
        self.level = None
        self.name = None
        self.class_type = None
    
    def set_name(self, n: str) -> None:
        self.name = n
    
    def set_level(self, l: int) -> None:
        self.level = l
        
    def set_class_type(self, c: ClassType) -> None:
        self.class_type = c
        
    def set_stats(self, stats: dict) -> None:
        self.stats = stats
        
    def get_stats(self) -> dict: 
        return self.stats

    def get_all_char_info(self) -> dict:
        return {
            "stats": self.get_stats(),
            "level": self.level,
            "name": self.name,
            "class": self.class_type.name
        }