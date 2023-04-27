import unittest

from managers.item_managers.item_drop_decide_manager import ItemDropDecideManager
from entities.enemies.zombie_enemy import ZombieEnemy


class ItemDropDecideManagerTests(unittest.TestCase):

    def test_decide_if_item_can_drop(self):
        x, y = 10, 10
        z = ZombieEnemy(x, y)
        z.drop_chance_range = (50, 100)
        self.manager.set_random_drop_chance_seed(50, 100)
        r = self.manager.decide_if_item_can_drop(z)

        assert r == True

    def test_drop(self):
        x_loc = 100
        y_loc = 100
        item = self.manager.drop(x_loc, y_loc)

        assert item is not None
        assert item.center_x == x_loc
        assert item.center_y == y_loc

    def setUp(self):
        self.manager = ItemDropDecideManager()
