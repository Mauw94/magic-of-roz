from managers.entity_managers.attack_entity_type import AttackEntityType
from entities.attacks.ranged_attack import RangedAttack
from entities.attacks.normal_ranged_attack import NormalRangedAttack
from entities.attacks.special_ranged_attack import SpecialRangedAttack


class AttackEntityManager:
    def __init__(self):
        pass

    def create_attack(self, attack_type: AttackEntityType, dmg: int, mana: int) -> RangedAttack:
        match attack_type:
            case AttackEntityType.NORMAL_RANGED:
                na = NormalRangedAttack()
                na.set_damage(dmg)
                na.set_mana_cost(mana)
                return na
            case AttackEntityType.SPECIAL_RANGED:
                sra = SpecialRangedAttack()
                sra.set_damage(dmg)
                sra.set_mana_cost(mana)
                return SpecialRangedAttack()
            case _:
                raise Exception("unknown attack type")
