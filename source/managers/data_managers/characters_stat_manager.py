from entities.classes.class_type import ClassTypeEnum


class CharactersStatManager():
        
    def __init__(self):
        pass
    
    # TODO: figure out some proper algorythm
    def mutate_stats_off_level(self, class_type: ClassTypeEnum, level: int) -> dict:
        stats = self.get_base_stats_for_class(class_type)
        for x in stats:
            if x[0] == 'a':
                stats[x] *= 0.1 * level
            elif "stat" in x:
                stats[x] *= 1.3 * level
            elif "res" in x:
                stats[x] += 2 * level
            else:
                stats[x] += 7 * level
            
        print(stats)
        return stats
    
    def get_base_stats_for_class(self, c: ClassTypeEnum) -> dict:
        match c:
            case ClassTypeEnum.NECROMANCER:
                return self.necromancer_base_stats()
            case ClassTypeEnum.WARRIOR:
                return self.warrior_base_stats()
            case ClassTypeEnum.DRUID:
                return self.druid_base_stats()
            case ClassTypeEnum.WIZARD:
                return self.wizard_base_stats()
            case _:
                raise Exception("unkown class type")
            
    def necromancer_base_stats(self) -> dict:
        return {
            "hp": 90,
            "ap": 5,
            "as": 1.1,
            "mana": 120,
            "intelligence_stat": 11,
            "strength_stat": 3,
            "dexterity_stat": 5,
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
            "intelligence_stat": 8,
            "strength_stat": 6,
            "dexterity_stat": 5,
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
            "intelligence_stat": 12,
            "strength_stat": 3,
            "dexterity_stat": 4,
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
            "intelligence_stat": 3,
            "strength_stat": 11,
            "dexterity_stat": 5,
            "fire_res": 15,
            "cold_res": 15,
            "lightning_res": 15
        }
    