import unittest

from managers.item_managers.item_drop_decide_manager import ItemDropDecideManager


class ItemDropDecideManagerTests(unittest.TestCase):

    def test_drop(self):
        x_loc = 100
        y_loc = 100
        item = self.manager.drop(x_loc, y_loc)

        assert item is not None
        assert item.center_x == x_loc
        assert item.center_y == y_loc

    def setUp(self):
        self.manager = ItemDropDecideManager()
