import os
import arcade
import random
from helpers.consts import Consts
from entities.player import Player
from input.keys import Keys
from arcade.experimental.lights import Light, LightLayer
from entities.enemies.zombie_enemy import ZombieEnemey
from services.collision_detection_service import CollisionDetectionService
from entities.attacks.normal_ranged_attack import NormalRangedAttack

AMBIENT_COLOR = (10, 10, 10)
VIEWPORT_MARGIN = 200


class GameView(arcade.View):
    def __init__(self) -> None:
        super().__init__()

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.handle_input = Keys()
        self.collision_detection_service = CollisionDetectionService()

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        self.scene = None
        self.player = None
        self.tile_map = None
        self.physics_engine = None

        self.light_layer = None
        self.player_light = None

        self.view_left = 0
        self.view_bottom = 0
        self.score = 0

        self.coin_collect_sound = arcade.load_sound(
            ":resources:sounds/coin1.wav")

    def on_show_view(self):
        self.setup()

    def setup(self):
        # map_name = ":resources:tiled_maps/level_1.json"

        # self.tile_map = arcade.load_tilemap(
        #     map_name, Consts.SPRITE_SCALING_TILES
        # )
        # self.scene = arcade.Scene.from_tilemap(self.tile_map)
        self.scene = arcade.Scene()
        self.background_sprite_list = arcade.SpriteList()
        self.score = 0

        self.player = Player()
        self.player.center_x = Consts.SCREEN_WIDTH / 2
        self.player.center_y = Consts.SCREEN_HEIGHT / 2
        self.scene.add_sprite("Player", self.player)

        self.scene.add_sprite_list("Attacks")

        for x in range(-128, 2000, 128):
            for y in range(-128, 1000, 128):
                sprite = arcade.Sprite(
                    ":resources:images/tiles/brickTextureWhite.png")
                sprite.position = x, y
                self.background_sprite_list.append(sprite)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player, None)

        self.light_layer = LightLayer(
            Consts.SCREEN_WIDTH, Consts.SCREEN_HEIGHT)
        self.light_layer.set_background_color(arcade.color.BLACK)

        radius = 950
        mode = "soft"
        color = arcade.color.WHITE
        self.player_light = Light(0, 0, radius, color, mode)
        self.light_layer.add(self.player_light)

        # TODO move coins and enemies creation to seperate functions
        # Add some random coins just for the sake of it for now
        self.coins = arcade.SpriteList()
        for i in range(50):
            coin = arcade.Sprite(
                ":resources:images/items/coinGold.png", Consts.SPRITE_SCALING_TILES)
            coin.center_x = random.randrange(Consts.SCREEN_WIDTH)
            coin.center_y = random.randrange(Consts.SCREEN_HEIGHT)
            self.coins.append(coin)
        self.scene.add_sprite_list("Coins", True, self.coins)

        zombie = ZombieEnemey()
        zombie.center_x = random.randrange(Consts.SCREEN_WIDTH)
        zombie.center_y = random.randrange(Consts.SCREEN_HEIGHT)
        self.scene.add_sprite("Enemies", zombie)

        self.view_left = 0
        self.view_bottom = 0

    def process_keychange(self):
        self.handle_input.process_keychange(self)

    def on_key_press(self, key, modifiers):
        self.handle_input.on_key_press(self, key, modifiers)

    def on_key_release(self, key, modifiers):
        self.handle_input.on_key_release(self, key, modifiers)

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
        self.handle_input.on_mouse_scroll(self, x, y, scroll_x, scroll_y)

    def on_update(self, delta_time):
        self.physics_engine.update()
        self.player_light.position = self.player.position
        self.scene.update_animation(delta_time, ["Player", "Coins", "Enemies"])
        self.collision_detection_service.collision_detection(self)
        self.player.normal_ranged_attack(self)
        self.player.special_ranged_attack(self)
        self.scene.update(["Enemies", "Attacks"])

        for enemy in self.scene["Enemies"]:
            enemy.ranged_attack(self)

        self.scroll_screen()

    def scroll_screen(self):
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

    def on_draw(self):
        self.clear()

        with self.light_layer:
            self.background_sprite_list.draw()
            self.scene.draw()

        self.light_layer.draw(ambient_color=AMBIENT_COLOR)

        arcade.draw_text(
            f"Health: {self.player.health}",
            self.player.center_x - (Consts.SCREEN_WIDTH / 2) + 50,
            self.player.center_y - (Consts.SCREEN_HEIGHT / 2) + 10,
            arcade.csscolor.RED,
            18
        )
