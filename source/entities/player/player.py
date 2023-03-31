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
    def __init__(self, x, y):
        super().__init__("male_person", "malePerson")
        
        # character info
        # TODO: items
        # TODO: inventory
        self.character_info = CharacterInfo()
        
        self.center_x = x
        self.center_y = y

        self.can_shoot_normal_ranged_attack = False
        self.can_shoot_special_ranged_attack = False

        self.normal_ranged_attack_pressed = False
        self.special_ranged_attack_pressed = False

        self.normal_shoot_timer = 0
        self.special_shoot_timer = 0

        self.health = 100
        self.hit = False
        self.hit_sound = arcade.load_sound(":resources:sounds/hit2.wav")

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

    def normal_ranged_attack(self, game: 'GameView'):
        if self.can_shoot_normal_ranged_attack:
            if self.normal_ranged_attack_pressed:
                Logger.log_game_event("Performing normal ranged attack")
                bullet = NormalRangedAttack()
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
