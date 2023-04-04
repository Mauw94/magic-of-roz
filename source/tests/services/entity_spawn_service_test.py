import unittest

from services.entity_spawn_service import EntitySpawnService
from entities.enemies.zombie_enemy import ZombieEnemy


class EntitySpawnServiceTest(unittest.TestCase):

    def test_spawn_zombie(self):
        z = self.s.spawn_zombie_enemy(None)

        assert z is type(ZombieEnemy)

    def setUp(self) -> None:
        self.s = EntitySpawnService()
