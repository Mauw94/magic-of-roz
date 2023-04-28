import unittest

from arcade import Sprite

from services.collision_detection_service import CollisionDetectionService


class CollisionDetectionServiceTests(unittest.TestCase):

    def test_coins_collision_detection_increases_score(self):
        c = []
        t = 5
        for _ in range(t):
            c.append(Sprite())

        score = self.s.coins_collision_detection(c)

        assert score == t

    def test_player_getting_hit_by_enemy(self):
        pass
    
    def setUp(self):
        self.s = CollisionDetectionService()
