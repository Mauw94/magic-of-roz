import unittest

from services.apply_item_effect_service import ApplyItemEffectService
from entities.items.consumables.health_globe import HealthGlobe
from entities.items.consumables.mana_globe import ManaGlobe
from tests.helpers.char_creator import create_mock_character


class ApplyItemEffectServiceTests(unittest.TestCase):

    def test_apply_item_effect_health_globe(self):
        p = create_mock_character()

        assert p is not None
        assert p.resource_manager.get_cur_hp() == 110

        p.resource_manager.decrease_hp(10)
        assert p.resource_manager.get_cur_hp() == 100

        item = HealthGlobe(10, 10)  # base healthglobe adds 15 life
        self.service.apply_item_effect([item], p)

        assert p.resource_manager.get_cur_hp() == 110

    def test_apply_item_effect_mana_globe(self):
        p = create_mock_character()

        assert p is not None
        assert p.resource_manager.get_cur_mana() == 60

        p.resource_manager.decrease_mana(20)
        assert p.resource_manager.get_cur_mana() == 40

        i = ManaGlobe(10, 10)
        self.service.apply_item_effect([i], p)

        assert p.resource_manager.get_cur_mana() == 60

    def setUp(self):
        self.service = ApplyItemEffectService()
