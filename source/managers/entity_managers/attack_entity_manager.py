from managers.entity_managers.attack_entity_type import AttackEntityType
from entities.attacks.ranged_attack import RangedAttack
from entities.attacks.normal_ranged_attack import NormalRangedAttack
from entities.attacks.special_ranged_attack import SpecialRangedAttack
from helpers.logging.logger import Logger


class AttackEntityManager:
    def __init__(self):
        self._objects_created = 0

    def create_attack(self, attack_type: AttackEntityType, dmg: int, mana: int) -> RangedAttack:
        match attack_type:
            case AttackEntityType.NORMAL_RANGED:
                return self._normal_ranged_attack(dmg, mana)
            case AttackEntityType.SPECIAL_RANGED:
                sra = SpecialRangedAttack()
                sra.set_damage(dmg)
                sra.set_mana_cost(mana)
                return SpecialRangedAttack()
            case _:
                raise Exception("unknown attack type")

    def _normal_ranged_attack(self, dmg: int, m: int) -> NormalRangedAttack:
        Logger.log_object_creation("NormalRangedAttack", "AttackEntityManager")
        
        na = NormalRangedAttack()
        na.set_damage(dmg)
        na.set_mana_cost(m)

        self._objects_created += 1

        return na
