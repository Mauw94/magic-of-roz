from enum import Enum
from entities.attacks.ranged_attack import RangedAttack
from entities.attacks.normal_ranged_attack import NormalRangedAttack
from entities.attacks.special_ranged_attack import SpecialRangedAttack
from helpers.logging.logger import Logger


class AttackEntityType(Enum):
    NORMAL_RANGED = 0
    SPECIAL_RANGED = 1
    NORMAL_CLOSE = 2
    SPECIAL_CLOSE = 3


# handles creating different kinds of attacks


class AttackEntityManager:
    def __init__(self):
        self._objects_created = 0

    # pass attack type, damage it does and mana cost
    def create_attack(
        self, attack_type: AttackEntityType, dmg: int, mana_cost: int
    ) -> RangedAttack:
        match attack_type:
            case AttackEntityType.NORMAL_RANGED:
                return self._normal_ranged_attack(dmg, mana_cost)
            case AttackEntityType.SPECIAL_RANGED:
                return self._special_ranged_attack(dmg, mana_cost)
            case _:
                raise Exception("unknown attack type")

    def _normal_ranged_attack(self, damage: int, mana_cost: int) -> NormalRangedAttack:
        Logger.log_object_creation("NormalRangedAttack", "AttackEntityManager")

        normal_ranged_attack = NormalRangedAttack(mana_cost=mana_cost, damage=damage)
        self._objects_created += 1

        return normal_ranged_attack

    def _special_ranged_attack(
        self, damage: int, mana_cost: int
    ) -> SpecialRangedAttack:
        Logger.log_object_creation("SpecialRangedAttack", "AttackEntityManager")

        special_ranged_attack = SpecialRangedAttack(mana_cost=mana_cost, damage=damage)
        self._objects_created += 1

        return special_ranged_attack
