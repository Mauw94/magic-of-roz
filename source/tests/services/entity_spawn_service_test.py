import unittest

from services.entity_spawn_service import EntitySpawnService
from entities.enemies.zombie_enemy import ZombieEnemy


class EntitySpawnServiceTest(unittest.TestCase):

    def test_spawn_zombie(self):
        self.s.set_spawn_timer(1)
        z = self.s.spawn_zombie_enemy()

        assert type(z) is ZombieEnemy

    def test_spawning_multiple_enemies(self):
        x = 5
        st = 50
        self.s.set_spawn_timer(st)
        for _ in range(st*3):
            self.s.spawn_zombie_enemy()

        assert len(self.s.enemy_spawn_locations) == 3

    def test_clear_spawn_locations(self):
        x = 3
        for _ in range(x):
            self.s.spawn_zombie_enemy()

        self.s.clear_spawn_locations()

        assert len(self.s.enemy_spawn_locations) == 0

    def setUp(self) -> None:
        self.s = EntitySpawnService()
