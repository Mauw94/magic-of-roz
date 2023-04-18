import unittest

from managers.entity_managers.attack_entity_manager import AttackEntityManager
from entities.attacks.normal_ranged_attack import NormalRangedAttack
from managers.entity_managers.attack_entity_type import AttackEntityType
from entities.attacks.special_ranged_attack import SpecialRangedAttack


class AttackEntityManagerTests(unittest.TestCase):
    
    def test_creating_normal_ranged_attack(self):
        damage = 5
        mana_cost = 7
        a = self.manager.create_attack(AttackEntityType.NORMAL_RANGED, damage, mana_cost)
        
        assert type(a) is NormalRangedAttack
        assert a.get_damage() == damage
        assert a.get_mana_cost() == mana_cost

    def test_creating_special_ranged_attack(self):
        damage= 10
        mana_cost = 8
        a = self.manager.create_attack(AttackEntityType.SPECIAL_RANGED, damage, mana_cost)
        
        assert type(a) is SpecialRangedAttack
        assert a.get_damage() == damage
        assert a.get_mana_cost() == mana_cost
        
    def setUp(self) -> None:
        self.manager = AttackEntityManager()