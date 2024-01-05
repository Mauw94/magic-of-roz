import os
import arcade
from helpers.consts import Consts
from entities.player.player import Player
from input.keys import Keys
from arcade.experimental.lights import Light, LightLayer
from entities.enemies.zombie_enemy import ZombieEnemy
from services.collision_detection_service import CollisionDetectionService
from services.entity_spawn_service import EntitySpawnService
from helpers.logging.logger import Logger
from entities.items.consumables.health_globe import HealthGlobe
from entities.items.consumables.speed_globe import SpeedGlobe
from services.apply_item_effect_service import ApplyItemEffectService
from services.damage_event_service import TextEventService
from managers.resource_managers.sound_manager import SoundManager
from helpers.static_data import BACKGROUND_GAME_MUSIC

AMBIENT_COLOR = (10, 10, 10)
VIEWPORT_MARGIN = 200


class GameView(arcade.View):
    def __init__(self, screen_w, screen_h, player: Player) -> None:
        super().__init__()

        self.__check_log_file_size()

        self.screen_width = screen_w
        self.screen_height = screen_h

        Logger.log_info("Initializing game")

        # Maybe need this later
        # file_path = os.path.dirname(os.path.abspath(__file__))
        # os.chdir(file_path)

        self.handle_input = Keys()

        self.entity_spawn_service = EntitySpawnService()
        self.entity_spawn_service.set_spawn_timer(500)
        self.entity_spawn_service.set_zombies_to_spawn_in_wave(3)
        Logger.log_object_creation("EntitySpawnService", "Game_View")

        self.text_event_service = TextEventService()
        Logger.log_object_creation("TextEventSerivce", "Game_View")

        self.collision_detection_service = CollisionDetectionService(
            self.text_event_service
        )
        Logger.log_object_creation("CollisionDetectionService", "Game_View")

        self.apply_item_effect_service = ApplyItemEffectService(self.text_event_service)
        Logger.log_object_creation("ApplyItemEffectService", "Game_View")

        self.sound_manager = SoundManager(with_preferred_volume=True)

        # NOTE for testing
        self.sound_manager.set_custom_voume(0)

        self.sound_manager.play_music(BACKGROUND_GAME_MUSIC, looping=True)
        Logger.log_object_creation("SoundManager", "Game_View")

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.escape_pressed = False

        self.scene = None
        self.player = player
        self.tile_map = None
        self.physics_engine = None

        self.light_layer = None
        self.player_light = None

        self.view_left = 0
        self.view_bottom = 0
        self.score = 0

        self.coin_collect_sound = arcade.load_sound(":resources:sounds/coin1.wav")

        self.enemy_attack_timer = 0

    def on_show_view(self):
        self.setup()

    def setup(self):  # TODO: clean this method up
        Logger.log_info("Initializing tilemap")

        # map_path = os.path.abspath("./tile-map/maps/town/town.json")
        # map_path = ":resources:tiled_maps/standard_tileset.json"
        # self.tile_map = arcade.load_tilemap(map_path, Consts.MAP_SCALING)
        # self.scene = arcade.Scene.from_tilemap(self.tile_map)
        self.scene = arcade.Scene()

        Logger.log_info("Setting up game")

        self.player.setup()

        self.score = 0
        self.enemy_attack_timer = 0

        self.scene.add_sprite("Player", self.player)
        self.scene.add_sprite_list("Attacks")
        self.scene.add_sprite_list("Enemies")
        self.scene.add_sprite_list("Items")

        # Add test items
        self.scene["Items"].append(
            SpeedGlobe(self.screen_width // 2 - 150, self.screen_height // 2 + 200)
        )
        self.scene["Items"].append(
            SpeedGlobe(self.screen_width // 2 - 150, self.screen_height // 2 + 400)
        )

        self.physics_engine = arcade.PhysicsEngineSimple(self.player, None)
        Logger.log_info("Physics enginge created")

        self.light_layer = LightLayer(Consts.SCREEN_WIDTH, Consts.SCREEN_HEIGHT)
        self.light_layer.set_background_color(arcade.color.BLUE_GRAY)

        radius = 970
        mode = "soft"
        color = arcade.color.WHITE
        self.player_light = Light(0, 0, radius, color, mode)
        self.light_layer.add(self.player_light)
        Logger.log_info("Lights created")

        self.bar_list = arcade.SpriteList()
        self.scene.add_sprite_list("Bars", self.bar_list)
        Logger.log_info("Sprites intialized")

        # if self.tile_map.background_color:
        #     arcade.set_background_color(self.tile_map.background_color)

        self.view_left = 0
        self.view_bottom = 0

        Logger.log_info("GameView is setup")

    def process_keychange(self):
        self.handle_input.process_keychange(self)

    def on_key_press(self, key, modifiers):
        self.handle_input.on_key_press(self, key, modifiers)

    def on_key_release(self, key, modifiers):
        self.handle_input.on_key_release(self, key, modifiers)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        self.handle_input.on_mouse_press(self, x, y, button, modifiers)

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        self.handle_input.on_mouse_release(self, x, y, button, modifiers)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.player.set_mouse_pos(x, y)

    # errors
    # def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
    #     self.handle_input.on_mouse_scroll(self, x, y, scroll_x, scroll_y)

    def on_update(self, delta_time):
        self.physics_engine.update()
        self.player_light.position = self.player.position
        # self.scene.update_animation(delta_time, ["Coins"])
        self.collision_detection_service.collision_detection(self)

        # event service
        self.text_event_service.update()

        # attack enemies hit detection
        self.collision_detection_service.bullet_collision_detection(
            self.player,
            self.scene["Attacks"],
            self.scene["Enemies"],
            self.scene["Items"],
        )

        # enemy attacks hit detection
        self.collision_detection_service.enemy_attack_collision_detection(
            self.scene["Attacks"], self.scene["Player"], self.player
        )

        # check for item collision with player
        item_list = arcade.check_for_collision_with_list(
            self.player, self.scene["Items"]
        )

        for item in item_list:
            if self.player.add_item_to_inventory(item):
                item.remove_from_sprite_lists()

        # TODO: apply items when selecting from inventory
        # self.apply_item_effect_service.apply_item_effect(item_list, self.player)

        # spawn periodically
        self.__spawn_zombies()

        # attacks
        self.player.normal_ranged_attack(self)
        self.player.special_ranged_attack(self)
        self.scene.update(["Player", "Enemies", "Attacks"])

        self.__enemies_attack()
        self.__scroll_screen()

        if self.escape_pressed:
            Logger.log_game_event("Returning to main menu")
            from views.main_menu import MainMenu

            arcade.set_viewport(0, self.screen_width, 0, self.screen_height)
            game_view = MainMenu(self.screen_width, self.screen_height)
            self.window.show_view(game_view)

    def on_draw(self):
        self.clear()

        with self.light_layer:
            self.scene.draw()

        self.light_layer.draw(ambient_color=AMBIENT_COLOR)

        self.player.draw()
        self.text_event_service.draw()

    def __scroll_screen(self):
        # Scroll left
        left_boundary = self.view_left + (self.window.width / 2)
        if self.player.left < left_boundary:
            self.view_left -= left_boundary - self.player.left

        # Scroll right
        right_boundary = self.view_left + self.window.width - (self.window.width / 2)
        if self.player.right > right_boundary:
            self.view_left += self.player.right - right_boundary

        # Scroll up
        top_boundary = self.view_bottom + self.window.height - (self.window.height / 2)
        if self.player.top > top_boundary:
            self.view_bottom += self.player.top - top_boundary

        # Scroll down
        bottom_boundary = self.view_bottom + (self.window.height / 2)
        if self.player.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player.bottom

        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        arcade.set_viewport(
            self.view_left,
            self.window.width + self.view_left,
            self.view_bottom,
            self.window.height + self.view_bottom,
        )

    def __enemies_attack(self):
        for enemy in self.scene["Enemies"]:
            if type(enemy) is ZombieEnemy:
                enemy.ranged_attack(self)

    def __spawn_zombies(self):
        zombies = self.entity_spawn_service.spawn_zombie_wave()
        if zombies is not None:
            for z in zombies:
                hp_bar = z.get_hp_bar()
                self.scene["Bars"].append(hp_bar[0])
                self.scene["Bars"].append(hp_bar[1])
                self.scene.add_sprite("Enemies", z)

    def __check_log_file_size(self):
        s = os.path.getsize("logs.txt")
        if s > 1000000:
            open("logs.txt", "w").close()  # clears the file
