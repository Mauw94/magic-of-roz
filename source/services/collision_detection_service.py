import arcade
from entities.attacks.enemy_attacks.zombie_attack import ZombieAttack
from entities.attacks.ranged_attack import RangedAttack
from entities.attacks.special_ranged_attack import SpecialRangedAttack
from entities.attacks.normal_ranged_attack import NormalRangedAttack
from entities.enemies.zombie_enemy import ZombieEnemy
from typing import TYPE_CHECKING, List
from helpers.logging.logger import Logger
from managers.resource_managers.sound_manager import SoundManager
from helpers.static_data import COIN_COLLECT_SOUND
from entities.player.player import Player
from managers.item_managers.item_drop_decide_manager import ItemDropDecideManager
from services.damage_event_service import TextEvent, TextEventService

if TYPE_CHECKING:
    from views.game_view import GameView


class CollisionDetectionService:
    def __init__(self, event_service: TextEventService):
        self.sound_manager = SoundManager()
        self.sound_manager.set_preferred_sound_volume(0.1)
        self.item_manager = ItemDropDecideManager()
        self.text_event_service = event_service

    def collision_detection(self, game: "GameView"):
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
    def bullet_collision_detection(
        self,
        player: Player,
        attacks: List[arcade.Sprite],
        enemies: List[arcade.Sprite],
        dropped_items_list: List[arcade.Sprite],
    ) -> None:
        for attack in attacks:
            attack_hit_list = arcade.check_for_collision_with_list(attack, enemies)
            if attack_hit_list:
                if type(attack) is ZombieAttack:
                    return
                attack.remove_from_sprite_lists()
                for enemy in attack_hit_list:
                    if type(enemy) is ZombieEnemy:
                        if (
                            type(attack) is RangedAttack
                            or SpecialRangedAttack
                            or NormalRangedAttack
                        ):
                            enemy.hit(attack.get_damage())
                            self.text_event_service.add_to_events(
                                TextEvent(
                                    str(attack.get_damage()),
                                    enemy.center_x,
                                    enemy.center_y + 50,
                                    arcade.csscolor.RED,
                                    18,
                                )
                            )
                        if enemy.health <= 0:
                            player.add_experience(enemy.experience_yield)
                            hp_bar = enemy.get_hp_bar()
                            hp_bar[0].remove_from_sprite_lists()
                            hp_bar[1].remove_from_sprite_lists()

                            if self.item_manager.decide_if_item_can_drop(enemy):
                                item = self.item_manager.drop(
                                    enemy.center_x, enemy.center_y
                                )
                                Logger.log_game_event("Item dropped {item}")
                                dropped_items_list.append(item)

                            enemy.remove_from_sprite_lists()

    # enemies attacks collision with player
    def enemy_attack_collision_detection(
        self, attacks: List[arcade.Sprite], players: List[arcade.Sprite], player: Player
    ) -> None:
        for attack in attacks:
            attack_hit_list = arcade.check_for_collision_with_list(attack, players)
            if attack_hit_list:
                if type(attack) is ZombieAttack:
                    attack.remove_from_sprite_lists()
                    self.text_event_service.add_to_events(
                        TextEvent(
                            str(-attack.get_damage()),
                            player.center_x - 15,
                            player.center_y + 60,
                            arcade.csscolor.RED,
                            16,
                        )
                    )
                    player.resource_manager.decrease_hp(attack.get_damage())
                    player.play_hit_sound()
