import arcade
from entities.attacks.normal_ranged_attack import NormalRangedAttack
from entities.attacks.special_ranged_attack import SpecialRangedAttack
from entities.attacks.enemy_attacks.zombie_attack import ZombieAttack
from entities.enemy import Enemy
from helpers.logging.logger import Logger
from typing import TYPE_CHECKING, List

from managers.resource_managers.sound_manager import SoundManager
from helpers.static_data import COIN_COLLECT_SOUND
from entities.player.player import Player
if TYPE_CHECKING:
    from views.game_view import GameView


class CollisionDetectionService:
    def __init__(self):
        pass

    # TODO move collision methods to gameview
    # and pass objects to correct methods
    def collision_detection(self, game: 'GameView'):
        self.sound_manager = SoundManager()

        # self.__coins_collision_detection(game)
        # self.__bullet_collision_detection(game)
        # self.__enemy_attack_collision_detection(game)

    def coins_collision_detection(self, coin_hit_list: List[arcade.Sprite]) -> int:
        s = 0
        for c in coin_hit_list:
            s += 1
            c.remove_from_sprite_lists()
            self.sound_manager.play_sound(COIN_COLLECT_SOUND)

        return s

    def bullet_collision_detection(self, attacks: List[arcade.Sprite], enemies: List[arcade.Sprite]) -> None:
        for a in attacks:
            attack_hit_list = arcade.check_for_collision_with_list(a, enemies)
            if attack_hit_list:
                if type(a) is ZombieAttack:
                    return
                a.remove_from_sprite_lists()
                for e in attack_hit_list:
                    e.hit(a.damage())
                    if e.health <= 0:
                        e.remove_from_sprite_lists()

    def enemy_attack_collision_detection(self, attacks: List[arcade.Sprite], players: List[arcade.Sprite], player: Player) -> None:
        for a in attacks:
            attack_hit_list = arcade.check_for_collision_with_list(a, players)
            if attack_hit_list:
                if type(a) is ZombieAttack:
                    a.remove_from_sprite_lists()
                    player.resource_manager.cur_hp -= a.damage()
                    player.play_hit_sound()

    def __enemy_attack_collision_detection(self, game: 'GameView'):
        for attack in game.scene["Attacks"]:
            attack_hit_list = arcade.check_for_collision_with_list(
                attack, game.scene["Player"])
            if attack_hit_list:
                if type(attack) is ZombieAttack:
                    game.player.resource_manager.cur_hp -= attack.damage()
                    game.player.play_hit_sound()
                    attack.remove_from_sprite_lists()
