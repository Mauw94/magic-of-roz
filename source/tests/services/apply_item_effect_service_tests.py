import unittest
import mongomock

from services.apply_item_effect_service import ApplyItemEffectService
from entities.classes.warrior import Warrior
from entities.items.consumables.health_globe import HealthGlobe
from managers.data_managers.characters_manager import CharactersManager
from entities.classes.class_type import ClassTypeEnum


class ApplyItemEffectServiceTests(unittest.TestCase):

    def test_apply_item_effect(self):
        self.chars_manager.save_player_character_info(
            "test1", ClassTypeEnum.WARRIOR)
        chars = self.chars_manager.get_player_characters()
        p = self.chars_manager.load_player_object(chars[0])
        p.setup()

        assert p is not None
        assert p.resource_manager.get_cur_hp() == 110
        
        p.resource_manager.cur_hp -= 20
        assert p.resource_manager.get_cur_hp() == 90

        item = HealthGlobe(10, 10)  # base healthglobe adds 15 life
        self.service.apply_item_effect([item], p)

        assert p.resource_manager.get_cur_hp() == 105

    def setUp(self):
        self.service = ApplyItemEffectService()
        self.chars_manager = CharactersManager(self.__mock_collection())

    def __mock_collection(self):
        return mongomock.MongoClient().db.collection
