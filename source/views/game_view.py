import os
import arcade
import random
from helpers.consts import Consts
from entities.player.player import Player
from input.keys import Keys
from arcade.experimental.lights import Light, LightLayer
from entities.enemies.zombie_enemy import ZombieEnemy
from services.collision_detection_service import CollisionDetectionService
from services.entity_spawn_service import EntitySpawnService
from entities.attacks.normal_ranged_attack import NormalRangedAttack
from helpers.logging.logger import Logger

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
        self.collision_detection_service = CollisionDetectionService()
        Logger.log_object_creation(
            "CollisionDetectionService", "Game_View")

        self.entity_spawn_service = EntitySpawnService()
        self.entity_spawn_service.set_spawn_timer(500)
        self.entity_spawn_service.set_zombies_to_spawn_in_wave(3)
        Logger.log_object_creation(
            "EntitySpawnService", "Game_View")

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

        self.coin_collect_sound = arcade.load_sound(
            ":resources:sounds/coin1.wav")

        self.enemy_attack_timer = 0

    def on_show_view(self):
        self.setup()

    def setup(self):  # TODO: clean this method up
        Logger.log_info("Initializing tilemap")

        map_path = os.path.abspath(
            "./tile-map/maps/town/town.json")
        # map_path = ":resources:tiled_maps/test_map_7.json"
        self.tile_map = arcade.load_tilemap(
            map_path, Consts.MAP_SCALING
        )
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        Logger.log_info("Setting up game")

        self.player.setup()

        self.score = 0
        self.enemy_attack_timer = 0

        self.scene.add_sprite("Player", self.player)
        self.scene.add_sprite_list("Attacks")
        self.scene.add_sprite_list("Enemies")

        self.physics_engine = arcade.PhysicsEngineSimple(self.player, None)

        Logger.log_info("Physics enginge created")

        self.light_layer = LightLayer(
            Consts.SCREEN_WIDTH, Consts.SCREEN_HEIGHT)
        self.light_layer.set_background_color(arcade.color.BLACK)

        radius = 970
        mode = "soft"
        color = arcade.color.WHITE
        self.player_light = Light(0, 0, radius, color, mode)
        self.light_layer.add(self.player_light)

        Logger.log_info("Lights created")

        # TODO move coins and enemies creation to seperate functions
        # Add some random coins just for the sake of it for now
        self.coins = arcade.SpriteList()
        for _ in range(30):
            coin = arcade.Sprite(
                ":resources:images/items/coinGold.png", Consts.SPRITE_SCALING_PLAYER)
            coin.center_x = random.randrange(Consts.SCREEN_WIDTH)
            coin.center_y = random.randrange(Consts.SCREEN_HEIGHT)
            self.coins.append(coin)
        self.scene.add_sprite_list("Coins", True, self.coins)

        self.bar_list = arcade.SpriteList()
        self.scene.add_sprite_list("Bars", self.bar_list)

        Logger.log_info("Sprites intialized")

        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        self.view_left = 0
        self.view_bottom = 0

    def process_keychange(self):
        self.handle_input.process_keychange(self)

    def on_key_press(self, key, modifiers):
        self.handle_input.on_key_press(self, key, modifiers)

    def on_key_release(self, key, modifiers):
        self.handle_input.on_key_release(self, key, modifiers)

    # errors
    # def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
    #     self.handle_input.on_mouse_scroll(self, x, y, scroll_x, scroll_y)

    def on_update(self, delta_time):
        self.physics_engine.update()
        self.player_light.position = self.player.position
        self.scene.update_animation(delta_time, ["Coins"])
        self.collision_detection_service.collision_detection(self)

        # coins hit detection
        coin_hit_list = arcade.check_for_collision_with_list(
            self.player, self.scene["Coins"])
        self.score += self.collision_detection_service.coins_collision_detection(
            coin_hit_list)

        # attack enemies hit detection
        self.collision_detection_service.bullet_collision_detection(
            self.player, self.scene["Attacks"], self.scene["Enemies"])

        # enemy attacks hit detection
        self.collision_detection_service.enemy_attack_collision_detection(
            self.scene["Attacks"], self.scene["Player"], self.player)

        # spawn periodically
        self.__spawn_zombies()

        # attacks
        self.player.normal_ranged_attack(self)
        self.player.special_ranged_attack(self)
        self.scene.update(["Player", "Enemies", "Attacks"])

        self.__enemies_attack()
        self.__scroll_screen()

        if self.escape_pressed:
            # TODO: bug -> screen moves with the player -> reset position?
            Logger.log_game_event("Returning to main menu")
            from views.main_menu import MainMenu
            arcade.set_viewport(0,
                                self.screen_width,
                                0,
                                self.screen_height)
            game_view = MainMenu(
                self.screen_width, self.screen_height)
            self.window.show_view(game_view)

    def on_draw(self):
        self.clear()

        with self.light_layer:
            self.scene.draw()

        self.light_layer.draw(ambient_color=AMBIENT_COLOR)

        self.player.draw()

    def __scroll_screen(self):
        # Scroll left
        left_boundary = self.view_left + (self.window.width / 2)
        if self.player.left < left_boundary:
            self.view_left -= left_boundary - self.player.left

        # Scroll right
        right_boundary = self.view_left + \
            self.window.width - (self.window.width / 2)
        if self.player.right > right_boundary:
            self.view_left += self.player.right - right_boundary

        # Scroll up
        top_boundary = self.view_bottom + \
            self.window.height - (self.window.height / 2)
        if self.player.top > top_boundary:
            self.view_bottom += self.player.top - top_boundary

        # Scroll down
        bottom_boundary = self.view_bottom + (self.window.height / 2)
        if self.player.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player.bottom

        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        arcade.set_viewport(self.view_left,
                            self.window.width + self.view_left,
                            self.view_bottom,
                            self.window.height + self.view_bottom)

    def __enemies_attack(self):
        for enemy in self.scene["Enemies"]:
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
