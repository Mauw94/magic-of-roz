from helpers.consts import Consts
from entities.entity import Entity
from entities.attacks.normal_ranged_attack import NormalRangedAttack
from entities.attacks.special_ranged_attack import SpecialRangedAttack
from helpers.logging.logger import Logger
from typing import TYPE_CHECKING

from entities.player.character_info import CharacterInfo
if TYPE_CHECKING:
    from views.game_view import GameView
import arcade


class Player(Entity):
    def __init__(self):
        super().__init__("male_person", "malePerson")

        # TODO: items
        # TODO: inventory

        self.character_info = CharacterInfo()
        self.center_x = Consts.SCREEN_WIDTH // 2
        self.center_y = Consts.SCREEN_HEIGHT // 2

        self.can_shoot_normal_ranged_attack = False
        self.can_shoot_special_ranged_attack = False

        self.normal_ranged_attack_pressed = False
        self.special_ranged_attack_pressed = False

        self.normal_shoot_timer = 0
        self.special_shoot_timer = 0

        self.hit = False
        self.hit_sound = arcade.load_sound(":resources:sounds/hit2.wav")

        self.mana_is_full = True
        self.mana_regen_timer = 0
        self.mana_regen_interval = 50  # TODO move to char info

    def setup(self):
        self.health = self.character_info.get_stats()["hp"]
        self.mana = self.character_info.get_stats()["mana"]
        self.cur_mana = self.mana
        self.mana_is_full = True

    def get_health(self) -> int:
        return self.health

    def get_mana(self) -> int:
        return self.cur_mana

    def update(self):
        self.update_animation()
        self._regen_mana()

    def draw(self):
        arcade.draw_text(
            f"Health: {self.get_health()}",
            self.center_x - (Consts.SCREEN_WIDTH / 2) + 50,
            self.center_y - (Consts.SCREEN_HEIGHT / 2) + 10,
            arcade.csscolor.RED,
            18
        )

        arcade.draw_text(
            f"Mana: {self.get_mana()}",
            self.center_x + (Consts.SCREEN_WIDTH / 2) - 130,
            self.center_y - (Consts.SCREEN_HEIGHT / 2) + 10,
            arcade.csscolor.BLUE,
            18
        )

        offset = self._get_name_offset(self.character_info.get_name())
        arcade.draw_text(
            f"{self.character_info.get_name()}",
            self.center_x - offset,
            self.center_y + 20,
            arcade.csscolor.WHITE,
            14
        )

    def update_animation(self, delta_time: float = 1 / 60):
        if self.change_x < 0 and self.facing_direction == Consts.RIGHT_FACING:
            self.facing_direction = Consts.LEFT_FACING
        elif self.change_x > 0 and self.facing_direction == Consts.LEFT_FACING:
            self.facing_direction = Consts.RIGHT_FACING

        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.idle_texture_pair[self.facing_direction]
            return

        self.cur_texture += 1
        if self.cur_texture > 7:
            self.cur_texture = 0
        self.texture = self.walk_textures[self.cur_texture][self.facing_direction]

    # TODO spend mana; regen mana
    # normal ranged attack when pressing Q
    def normal_ranged_attack(self, game: 'GameView'):
        if self.can_shoot_normal_ranged_attack:
            if self.normal_ranged_attack_pressed:
                Logger.log_game_event("Performing normal ranged attack")
                bullet = NormalRangedAttack()
                bullet.set_damage(self.character_info.get_normal_damage())
                self.cur_mana -= bullet.mana_cost
                bullet.play_shooting_sound()
                if self.facing_direction == Consts.RIGHT_FACING:
                    bullet.change_x = Consts.PLAYER_ATTACK_PARTICLE_SPEED
                else:
                    bullet.change_x = -Consts.PLAYER_ATTACK_PARTICLE_SPEED

                bullet.center_x = self.center_x
                bullet.center_y = self.center_y

                game.scene.add_sprite("Attacks", bullet)
                self.can_shoot_normal_ranged_attack = False
        else:
            self.special_shoot_timer += 1
            if self.special_shoot_timer == Consts.PLAYER_ATTACK_SPEED:
                self.can_shoot_normal_ranged_attack = True
                self.special_shoot_timer = 0

    # a lot of duplicate code from normal_ranged_attack
    # -> better way of doing this?
    def special_ranged_attack(self, game: 'GameView'):
        if self.can_shoot_special_ranged_attack:
            if self.special_ranged_attack_pressed:
                Logger.log_game_event("Performing special ranged attack")
                bullet = SpecialRangedAttack()
                bullet.play_shooting_sound()
                if self.facing_direction == Consts.RIGHT_FACING:
                    bullet.change_x = Consts.PLAYER_ATTACK_PARTICLE_SPEED
                else:
                    bullet.change_x = -Consts.PLAYER_ATTACK_PARTICLE_SPEED

                bullet.center_x = self.center_x
                bullet.center_y = self.center_y

                game.scene.add_sprite("Attacks", bullet)
                self.can_shoot_special_ranged_attack = False
        else:
            self.special_shoot_timer += 1
            if self.special_shoot_timer == Consts.PLAYER_ATTACK_SPEED:
                self.can_shoot_special_ranged_attack = True
                self.special_shoot_timer = 0

    def play_hit_sound(self):
        if self.hit_sound is not None:
            arcade.play_sound(self.hit_sound)

    def _regen_mana(self):
        if self.cur_mana >= self.mana:
            return

        self.mana_regen_timer += 1
        if self.mana_regen_timer == self.mana_regen_interval:
            self.cur_mana += 1
            self.mana_regen_timer = 0

    def _get_name_offset(self, name: str) -> int:
        # TODO: decent algo this is dogwater
        o = len(name)
        if o >= 19:
            return 55
        elif o >= 17:
            return 50
        elif o >= 15:
            return 45
        elif o >= 12:
            return 40
        elif o >= 10:
            return 35
        elif o >= 7:
            return 30
        elif o >= 5:
            return 15
        else:
            return 15
