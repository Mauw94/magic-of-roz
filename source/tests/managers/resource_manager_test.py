import unittest

from managers.resource_managers.resource_manager import ResourceManager


class ResourceManagerTest(unittest.TestCase):
    def test_setting_max_mana(self):
        m = 100
        self.rm.set_max_mana(m)

        assert self.rm.mana_is_full == True
        assert m == self.rm.cur_mana

    def test_setting_max_hp(self):
        hp = 100
        self.rm.set_max_hp(hp)

        assert self.rm.hp_is_full == True
        assert hp == self.rm.cur_hp

    def test_regen_mana(self):
        mana_regen_interval = 50
        self.rm.set_mana_regen_values(mana_regen_interval)
        self.rm.set_max_mana(100)
        self.rm.cur_mana -= 10
        i = 0
        while i < mana_regen_interval:
            self.rm.regen_mana()
            i += 1

        assert self.rm.mana_is_full == False
        assert self.rm.cur_mana == 91

    def setUp(self) -> ResourceManager:
        self.rm = ResourceManager()


if __name__ == '__main__':
    unittest.main()
