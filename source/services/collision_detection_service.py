import arcade
from entities.attacks.enemy_attacks.zombie_attack import ZombieAttack
from typing import TYPE_CHECKING, List

from managers.resource_managers.sound_manager import SoundManager
from helpers.static_data import COIN_COLLECT_SOUND
from entities.player.player import Player
if TYPE_CHECKING:
    from views.game_view import GameView


class CollisionDetectionService:
    def __init__(self):
        self.sound_manager = SoundManager()
        self.sound_manager.set_preferred_sound_volume(0.1)

    def collision_detection(self, game: 'GameView'):
        pass

    # player collision with coins
    def coins_collision_detection(self, coin_hit_list: List[arcade.Sprite]) -> int:
        s = 0
        for c in coin_hit_list:
            s += 1
            c.remove_from_sprite_lists()
            self.sound_manager.play_sound(COIN_COLLECT_SOUND)

        return s

    # player bullet collision with enemies
    def bullet_collision_detection(self, player: Player, attacks: List[arcade.Sprite], enemies: List[arcade.Sprite]) -> None:
        for a in attacks:
            attack_hit_list = arcade.check_for_collision_with_list(a, enemies)
            if attack_hit_list:
                if type(a) is ZombieAttack:
                    return
                a.remove_from_sprite_lists()
                for e in attack_hit_list:
                    e.hit(a.damage())
                    if e.health <= 0:
                        player.kill_counter += 1
                        hp_bar = e.get_hp_bar()
                        hp_bar[0].remove_from_sprite_lists()
                        hp_bar[1].remove_from_sprite_lists()
                        e.remove_from_sprite_lists()

    # enemies attacks collision with player
    def enemy_attack_collision_detection(self, attacks: List[arcade.Sprite], players: List[arcade.Sprite], player: Player) -> None:
        for a in attacks:
            attack_hit_list = arcade.check_for_collision_with_list(a, players)
            if attack_hit_list:
                if type(a) is ZombieAttack:
                    a.remove_from_sprite_lists()
                    player.resource_manager.cur_hp -= a.damage()
                    player.play_hit_sound()
