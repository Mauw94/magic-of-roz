import unittest

import arcade

from managers.item_managers.item_drop_decide_manager import ItemDropDecideManager
from entities.items.item_base import ItemBase


class ItemDropDecideManagerTests(unittest.TestCase):
    
    def test_drop(self):
        x_loc = 100
        y_loc = 100
        item = self.manager.drop(x_loc, y_loc)
        
        assert item is not None
        
    def setUp(self):
        self.manager = ItemDropDecideManager()