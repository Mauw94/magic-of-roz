import unittest

from managers.resource_managers.resource_manager import ResourceManager


class ResourceManagerTests(unittest.TestCase):
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

    def test_regen_hp(self):
        hp_regen_interval = 50
        self.rm.set_hp_regen_values(hp_regen_interval)
        self.rm.set_max_hp(100)
        self.rm.cur_hp -= 10
        i = 0
        while i < hp_regen_interval:
            self.rm.regen_hp()
            i += 1
            
        assert self.rm.hp_is_full == False
        assert self.rm.cur_hp == 91
    
    def test_get_cur_hp(self):
        self.rm.set_max_hp(100)
        self.rm.cur_hp -= 50
        
        assert self.rm.get_cur_hp() == 50
        
    def test_get_cur_mana(self):
        self.rm.set_max_mana(100)
        self.rm.cur_mana -= 50
        
        assert self.rm.get_cur_mana() == 50
    
    def setUp(self) -> None:
        self.rm = ResourceManager()


if __name__ == '__main__':
    unittest.main()
