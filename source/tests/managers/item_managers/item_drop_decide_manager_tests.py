import unittest

from managers.item_managers.item_drop_decide_manager import ItemDropDecideManager


class ItemDropDecideManagerTests(unittest.TestCase):
    
    def test_drop(self):
        self.manager.drop()
    
    def setUp(self):
        self.manager = ItemDropDecideManager()