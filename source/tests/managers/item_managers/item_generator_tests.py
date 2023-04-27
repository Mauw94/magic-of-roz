import unittest

from managers.item_managers.item_generator import ItemGenerator
from entities.items.consumables.health_globe import HealthGlobe
from entities.items.consumables.mana_globe import ManaGlobe


class ItemGeneratorTests(unittest.TestCase):

    def test_generate_health_globe(self):
        x_loc, y_loc = 100, 100
        h = self.item_generator.gen_health_globe(x_loc, y_loc)

        assert type(h) is HealthGlobe

    def test_generate_mana_globe(self):
        x_loc, y_loc = 100, 100
        m = self.item_generator.gen_mana_globe(x_loc, y_loc)

        assert type(m) is ManaGlobe

    def setUp(self):
        self.item_generator = ItemGenerator()
