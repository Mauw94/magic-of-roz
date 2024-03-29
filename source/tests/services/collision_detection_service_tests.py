import unittest

from arcade import Sprite

from services.collision_detection_service import CollisionDetectionService
from entities.attacks.enemy_attacks.zombie_attack import ZombieAttack
from tests.helpers.char_creator import create_mock_character


class CollisionDetectionServiceTests(unittest.TestCase):

    def test_coins_collision_detection_increases_score(self):
        c = []
        t = 5
        for _ in range(t):
            c.append(Sprite())

        score = self.s.coins_collision_detection(c)

        assert score == t

    def test_player_getting_hit_by_enemy(self):
        a = ZombieAttack()
        p = create_mock_character()

        cur_hp = p.resource_manager.cur_hp
        d = a.get_damage()
        p.resource_manager.decrease_hp(d)
        
        assert p.resource_manager.cur_hp == cur_hp - d

    def setUp(self):
        self.s = CollisionDetectionService()
