class CharactersStatManager():
        
    def __init__(self):
        pass
    
    def mutate_stats_off_level(self, stats: dict, level: int) -> None:
        for d in dict:
            print(d)
    
    def necromancer_base_stats(self) -> dict:
        return {
            "hp": 90,
            "ap": 5,
            "as": 1.1,
            "mana": 100,
            "intelligence": 11,
            "strength": 3,
            "dexterity": 5,
            "fire_res": 15,
            "cold_res": 15,
            "lightning_res": 15
        }
    
    def druid_base_stats(self) -> dict:
        return {
            "hp": 95,
            "ap": 7,
            "as": 0.8,
            "mana": 70,
            "intelligence": 8,
            "strength": 6,
            "dexterity": 5,
            "fire_res": 15,
            "cold_res": 15,
            "lightning_res": 15
        }
    
    def wizard_base_stats(self) -> dict:
        return {
            "hp": 80,
            "ap": 9,
            "as": 0.8,
            "mana": 110,
            "intelligence": 12,
            "strength": 3,
            "dexterity": 4,
            "fire_res": 15,
            "cold_res": 15,
            "lightning_res": 15
        }
    
    def warrior_base_stats(self) -> dict:
        return {
            "hp": 110,
            "ap": 7,
            "as": 1,
            "mana": 60,
            "intelligence": 3,
            "strength": 11,
            "dexterity": 5,
            "fire_res": 15,
            "cold_res": 15,
            "lightning_res": 15
        }
    