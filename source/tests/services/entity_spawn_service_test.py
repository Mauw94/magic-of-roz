import unittest

from services.entity_spawn_service import EntitySpawnService
from entities.enemies.zombie_enemy import ZombieEnemy


class EntitySpawnServiceTest(unittest.TestCase):

    def test_spawn_zombie_enemy_wave_2_waves(self):
        st = 50
        z_to_spawn = 3
        self.s.set_spawn_timer(st)
        self.s.set_zombies_to_spawn_in_wave(z_to_spawn)
        z = []

        # first wave spawns 3
        # second wave spawns 3
        # third wave increases int(spawn) * 1.5 = 4
        for _ in range(z_to_spawn):
            for _ in range(st):
                zombies = self.s.spawn_zombie_wave()
                if zombies is not None:
                    for x in zombies:
                        z.append(x)

        assert len(z) == 10

    def test_spawn_zombie_enemy_wave_should_have_all_random_pos(self):
        t = 50
        z_to_spawn = 1
        self.s.set_spawn_timer(t)
        self.s.set_zombies_to_spawn_in_wave(z_to_spawn)

        for _ in range(z_to_spawn):
            for _ in range(t):
                zs = self.s.spawn_zombie_wave()
                if zs is not None:
                    for z in zs:
                        pass

        pass

    def test_spawn_zombie_enemy_wave_returns_none(self):
        self.s.set_spawn_timer(50)
        self.s.set_zombies_to_spawn_in_wave(1)
        z = self.s.spawn_zombie_wave()

        assert z == None

    def test_spawn_zombie_enemy_wave(self):
        z_to_spawn = 3
        self.s.set_spawn_timer(1)
        self.s.set_zombies_to_spawn_in_wave(z_to_spawn)
        z = self.s.spawn_zombie_wave()

        assert len(z) == z_to_spawn

    def test_spawn_zombie_returns_none(self):
        self.s.set_spawn_timer(50)
        z = self.s.spawn_zombie()

        assert z == None

    def test_spawn_zombie(self):
        self.s.set_spawn_timer(1)
        z = self.s.spawn_zombie()

        assert type(z) is ZombieEnemy

    def test_spawning_multiple_enemies(self):
        x = 3
        st = 50
        self.s.set_spawn_timer(st)
        for _ in range(st*x):
            self.s.spawn_zombie()

        assert len(self.s.enemy_spawn_locations) == x

    def test_clear_spawn_locations(self):
        x = 3
        for _ in range(x):
            self.s.spawn_zombie()

        self.s.clear_spawn_locations()

        assert len(self.s.enemy_spawn_locations) == 0

    def setUp(self) -> None:
        self.s = EntitySpawnService()
