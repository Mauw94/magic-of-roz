import arcade
from entities.attacks.normal_ranged_attack import NormalRangedAttack
from entities.attacks.special_ranged_attack import SpecialRangedAttack
from entities.attacks.enemy_attacks.zombie_attack import ZombieAttack
from entities.enemy import Enemy
from helpers.logging.logger import Logger
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from views.game_view import GameView


class CollisionDetectionService:
    def __init__(self):
        Logger.log_object_creation(
            "CollisionDetectionService", "CollisionDetectionServiceClass")

    def collision_detection(self, game: 'GameView'):
        self.__coins_collision_detection(game)
        self.__bullet_collision_detection(game)
        self.__enemy_attack_collision_detection(game)

    def __coins_collision_detection(self, game: 'GameView'):
        coin_hit_list = arcade.check_for_collision_with_list(
            game.player, game.scene["Coins"])
        for coin in coin_hit_list:
            game.score += 1
            coin.remove_from_sprite_lists()
            arcade.play_sound(game.coin_collect_sound)

    def __bullet_collision_detection(self, game: 'GameView'):
        for attack in game.scene["Attacks"]:
            attack_hit_list = arcade.check_for_collision_with_list(
                attack, game.scene["Enemies"])
            if attack_hit_list:
                if type(attack) is ZombieAttack:  # TODO create EnemyAttack super class
                    return
                attack.remove_from_sprite_lists()
                for enemy in attack_hit_list:
                    enemy.hit(attack.damage())
                    if enemy.health <= 0:
                        enemy.remove_from_sprite_lists()

    def __enemy_attack_collision_detection(self, game: 'GameView'):
        for attack in game.scene["Attacks"]:
            attack_hit_list = arcade.check_for_collision_with_list(
                attack, game.scene["Player"])
            if attack_hit_list:
                if type(attack) is ZombieAttack:
                    game.player.health -= attack.damage()
                    game.player.play_hit_sound()
                    attack.remove_from_sprite_lists()
