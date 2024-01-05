from engine_extensions.drawing_engine import DrawingEngine
from helpers.consts import Consts
from entities.entity import Entity
from entities.attacks.normal_ranged_attack import NormalRangedAttack
from entities.attacks.special_ranged_attack import SpecialRangedAttack
from helpers.logging.logger import Logger
from typing import TYPE_CHECKING

from entities.player.character_info import CharacterInfo
from managers.entity_managers.attack_entity_manager import AttackEntityManager
from managers.resource_managers.resource_manager import ResourceManager
from managers.entity_managers.attack_entity_manager import AttackEntityType
from managers.data_managers.file_save_manager import save_character
from helpers.static_data import ENEMY_HIT_SOUND
from entities.attacks.ranged_attack import RangedAttack
from entities.player.inventory import Inventory
from entities.items.item_base import ItemBase

if TYPE_CHECKING:
    from views.game_view import GameView
import arcade
import math

# NOTE: when modifying stats, always call resourcemanager first on the player obj


class Player(Entity):
    def __init__(self, character_info: dict):
        super().__init__("male_adventurer", "maleAdventurer")

        # TODO: items
        # TODO: inventory

        self.inventory = Inventory()

        self.character_info = self._create_char_stats(character_info=character_info)
        self.attack_entity_manager = AttackEntityManager()
        self.resource_manager = ResourceManager()

        self.center_x = Consts.SCREEN_WIDTH // 2
        self.center_y = Consts.SCREEN_HEIGHT // 2

        self.can_use_ranged_attack = False

        self.normal_ranged_attack_pressed = False
        self.special_ranged_attack_pressed = False

        self.normal_shoot_timer = 0
        self.ranged_attack_timer = 0

        self.hit = False
        self.hit_sound = ENEMY_HIT_SOUND

        self.movement_speed = Consts.PLAYER_MOVEMENT_SPEED
        self.__movement_speed_increase_timer = 0
        self.__item_effect_movement_speed_applied = False

        self.__mouse_pos = (0, 0)

    def setup(self):
        self.health = self.character_info.get_stats()["hp"]
        self.mana = self.character_info.get_stats()["mana"]
        # TODO set regen values in char info
        self.resource_manager.set_max_mana(self.mana)
        self.resource_manager.set_mana_regen_values(30)
        self.resource_manager.set_max_hp(self.health)
        self.resource_manager.set_hp_regen_values(50)

    def update(self):
        self.update_animation()
        self.resource_manager.regen_mana()
        self.resource_manager.regen_hp()

        if self.__item_effect_movement_speed_applied:
            self.__temp_increase_movement()

    def apply_item_effect_movement(
        self, movement_speed_increase: int, timer: int
    ) -> None:
        Logger.log_game_event("Applying movement speed effect")
        self.__item_effect_movement_speed_applied = True
        self.__movement_speed_increase_timer = timer
        self.movement_speed += movement_speed_increase

    def __temp_increase_movement(self) -> None:
        self.__movement_speed_increase_timer -= 1

        if self.__movement_speed_increase_timer <= 0:
            Logger.log_game_event("Movement speed buff worn off")
            self.__item_effect_movement_speed_applied = False
            self.movement_speed = Consts.PLAYER_MOVEMENT_SPEED

    def draw(self):
        # draw item effect
        if self.__item_effect_movement_speed_applied:
            DrawingEngine.draw_text(
                f"Speed increase: {self.__movement_speed_increase_timer}",
                self.center_x - (Consts.SCREEN_WIDTH / 2) + 30,
                self.center_y + (Consts.SCREEN_HEIGHT / 2) - 50,
                arcade.csscolor.YELLOW,
                10,
            )

        # draw inventory
        items = self.inventory.get_items()
        if len(items) > 0:
            for index, item in enumerate(items):
                x = self.center_x + (Consts.SCREEN_WIDTH / 2) - (30 + index * 45)
                y = self.center_y + (Consts.SCREEN_HEIGHT / 2) - 100
                DrawingEngine.draw_item_texture(x, y, 0.3, item.texture)

        # ## draw inventory size
        # DrawingEngine.draw_text(
        #     f"Inventory count: {len(self.inventory.get_items())}",
        #     self.center_x + (Consts.SCREEN_WIDTH / 2) - 300,
        #     self.center_y + (Consts.SCREEN_HEIGHT / 2) - 60,
        #     arcade.csscolor.YELLOW,
        #     14,
        # )

        # draw hp
        DrawingEngine.draw_text(
            f"HP: {self.resource_manager.get_cur_hp()}",
            self.center_x - (Consts.SCREEN_WIDTH / 2) + 50,
            self.center_y - (Consts.SCREEN_HEIGHT / 2) - 20,
            arcade.csscolor.RED,
            18,
        )

        # draw mana
        DrawingEngine.draw_text(
            f"Mana: {self.resource_manager.get_cur_mana()}",
            self.center_x + (Consts.SCREEN_WIDTH / 2) - 130,
            self.center_y - (Consts.SCREEN_HEIGHT / 2) - 20,
            arcade.csscolor.BLUE,
            18,
        )

        # draw level
        DrawingEngine.draw_text(
            f"Level: {self.character_info.get_level()}",
            self.center_x + (Consts.SCREEN_WIDTH / 2) - (Consts.SCREEN_WIDTH / 2) - 200,
            self.center_y - (Consts.SCREEN_HEIGHT / 2) - 20,
            arcade.csscolor.WHITE,
            18,
        )

        # draw experience
        DrawingEngine.draw_text(
            f"Exp: {self.character_info.get_current_experience()} / 100",
            self.center_x + (Consts.SCREEN_WIDTH / 2) - (Consts.SCREEN_WIDTH / 2) - 20,
            self.center_y - (Consts.SCREEN_HEIGHT / 2) - 20,
            arcade.csscolor.WHITE,
            18,
        )

        # draw name above player
        offset = DrawingEngine.calcuate_offset_text_center_above_entity(
            self.character_info.get_name(), 14, self.width
        )  # returns a tuple[int, int]
        DrawingEngine.draw_text(
            f"{self.character_info.get_name()}",
            self.center_x - offset[0],
            self.center_y + 20 + offset[1],
            arcade.csscolor.WHITE,
            14,
        )

        # draw gold counter
        DrawingEngine.draw_text(
            f"Gold: {self.character_info.get_gold()}",
            self.center_x + (Consts.SCREEN_WIDTH / 2) - 100,
            self.center_y + (Consts.SCREEN_HEIGHT / 2) - 60,
            arcade.csscolor.YELLOW,
            14,
        )

    def add_item_to_inventory(self, item: ItemBase) -> bool:
        return self.inventory.add_item(item)

    def use_item_in_inventory(self, index: int) -> None:
        pass

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

    def normal_ranged_attack(self, game: "GameView"):
        if self.resource_manager.cur_mana >= Consts.NORMAL_ATTACK_MANA_COST:
            if self.can_use_ranged_attack:
                if self.normal_ranged_attack_pressed:
                    Logger.log_game_event("Performing normal ranged attack")
                    bullet = self.attack_entity_manager.create_attack(
                        AttackEntityType.NORMAL_RANGED,
                        self.character_info.get_normal_damage(),
                        Consts.NORMAL_ATTACK_MANA_COST,
                    )
                    self.resource_manager.decrease_mana(bullet.get_mana_cost())
                    bullet.play_shooting_sound()

                    self.__calculate_and_x_y_change_for_bullet(bullet)

                    game.scene.add_sprite("Attacks", bullet)
                    self.can_use_ranged_attack = False
            else:
                self.__increase_shoot_timer()

    def special_ranged_attack(self, game: "GameView"):
        if self.resource_manager.cur_mana >= Consts.SPECIAL_ATTACK_MANA_COST:
            if self.can_use_ranged_attack:
                if self.special_ranged_attack_pressed:
                    Logger.log_game_event("Performing special ranged attack")
                    bullet = self.attack_entity_manager.create_attack(
                        AttackEntityType.SPECIAL_RANGED,
                        self.character_info.get_special_damage(),
                        Consts.SPECIAL_ATTACK_MANA_COST,
                    )
                    self.resource_manager.decrease_mana(bullet.get_mana_cost())
                    bullet.play_shooting_sound()

                    self.__calculate_and_x_y_change_for_bullet(bullet)

                    game.scene.add_sprite("Attacks", bullet)
                    self.can_use_ranged_attack = False
            else:
                self.__increase_shoot_timer()

    def __calculate_and_x_y_change_for_bullet(self, bullet: RangedAttack) -> ():
        actual_x = Consts.SCREEN_WIDTH // 2
        actual_y = Consts.SCREEN_HEIGHT // 2

        bullet.center_x = self.center_x
        bullet.center_y = self.center_y

        x_diff = self.__mouse_pos[0] - actual_x
        y_diff = self.__mouse_pos[1] - actual_y

        angle = math.atan2(y_diff, x_diff)
        bullet.angle = math.degrees(angle)

        match bullet:
            case SpecialRangedAttack():
                # always want to rotate a special ranged attack 90 degrees
                # because the texture is loaded with a -90 degree angle
                if bullet.angle < 0:
                    bullet.angle += 270
                else:
                    bullet.angle += 90
            case NormalRangedAttack():
                if bullet.angle < 0:
                    bullet.angle += 360
            case _:
                raise Exception("unknown bullet class type")

        bullet.change_x = math.cos(angle) * Consts.PLAYER_ATTACK_PARTICLE_SPEED
        bullet.change_y = math.sin(angle) * Consts.PLAYER_ATTACK_PARTICLE_SPEED

    def __increase_shoot_timer(self) -> None:
        self.ranged_attack_timer += 1
        if self.ranged_attack_timer == Consts.PLAYER_ATTACK_SPEED:
            self.can_use_ranged_attack = True
            self.ranged_attack_timer = 0

    def set_mouse_pos(self, x: int, y: int) -> None:
        self.__mouse_pos = (x, y)

    def play_hit_sound(self):
        if self.hit_sound is not None:
            self.sound_manager.play_sound(self.hit_sound)

    def add_experience(self, experience: int):
        self.character_info.add_experience(experience)
        save_character(
            self.character_info.get_uid(), self.character_info.get_all_char_info()
        )

    def add_gold(self, gold: int):
        self.character_info.add_gold(gold)
        save_character(
            self.character_info.get_uid(), self.character_info.get_all_char_info()
        )

    def _create_char_stats(self, character_info: dict) -> CharacterInfo:
        info = CharacterInfo()
        info.set_info(character_info)

        return info

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
