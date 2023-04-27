import unittest

from entities.attacks.normal_ranged_attack import NormalRangedAttack


class RangedAttackTests(unittest.TestCase):

    def test_normal_ranged_attack_damage(self):
        set_damage = 50
        self.ranged_attack.set_damage(set_damage)
        d = self.ranged_attack.get_damage()

        assert d == set_damage

    def test_normal_ranged_attack_mana(self):
        set_mana = 50
        self.ranged_attack.set_mana_cost(50)
        m = self.ranged_attack.get_mana_cost()

        assert m == set_mana

    def setUp(self):
        self.ranged_attack = NormalRangedAttack()
        pass
