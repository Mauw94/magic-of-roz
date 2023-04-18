import unittest

from managers.resource_managers.sound_manager import SoundManager


class SoundManagerTests(unittest.TestCase):
    def test_setting_volume(self):
        self.sm.set_preferred_sound_volume(1)
        
        assert self.sm.get_volume() == 1

    def setUp(self) -> None:
        self.sm = SoundManager()
