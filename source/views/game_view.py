import os
import arcade
import random
from helpers.consts import Consts
from entities.player import Player
from input.keys import Keys
from arcade.experimental.lights import Light, LightLayer

AMBIENT_COLOR = (10, 10, 10)

class GameView(arcade.View):
    def __init__(self) -> None:
        super().__init__()
        
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        
        self.handle_input = Keys()
        
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        
        self.scene = None
        self.player = None
        self.tile_map = None
        self.camera = None
        self.gui_camera = None
        self.physics_engine = None                
        
        self.light_layer = None
        self.player_light = None
        
        # TODO load sounds                
    
    def on_show_view(self):        
        self.setup()
        
    def setup(self):    
        self.camera = arcade.Camera(self.window.width, self.window.height)
        self.gui_camera = arcade.Camera(self.window.width, self.window.height)
        
        # map_name = ":resources:tiled_maps/level_1.json"
        
        # self.tile_map = arcade.load_tilemap(
        #     map_name, Consts.SPRITE_SCALING_TILES
        # )
        # self.scene = arcade.Scene.from_tilemap(self.tile_map)
        self.scene = arcade.Scene()
        self.background_sprite_list = arcade.SpriteList()
        
        self.player = Player()
        self.player.center_x = Consts.SCREEN_WIDTH / 2
        self.player.center_y = Consts.SCREEN_HEIGHT / 2
        self.scene.add_sprite("Player", self.player)    
           
        for x in range(-128, 2000, 128):
            for y in range(-128, 1000, 128):
                sprite = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png")
                sprite.position = x, y
                self.background_sprite_list.append(sprite)             
                
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player,
            gravity_constant=0
        )

        self.light_layer = LightLayer(Consts.SCREEN_WIDTH, Consts.SCREEN_HEIGHT)
        self.light_layer.set_background_color(arcade.color.BLACK)        
        
        radius = 950
        mode = "soft"
        color = arcade.color.WHITE
        self.player_light = Light(0, 0, radius, color, mode)
        self.light_layer.add(self.player_light)
        
        self.player_light.position = self.player.position
        
        self.coins = arcade.SpriteList()
        # Add some random coins just for the sake of it for now
        for i in range(50):
            coin = arcade.Sprite(":resources:images/items/coinGold.png", Consts.SPRITE_SCALING_TILES)
            coin.center_x = random.randrange(Consts.SCREEN_WIDTH)
            coin.center_y = random.randrange(Consts.SCREEN_HEIGHT)
            self.coins.append(coin)                
        
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
        self.scene.update_animation(delta_time)
        self.center_camera_to_player()                

    def center_camera_to_player(self, speed=0.2):
        screen_center_x = self.camera.scale * (
            self.player.center_x - (self.camera.viewport_width / 2)
        )
        screen_center_y = self.camera.scale * (
            self.player.center_y - (self.camera.viewport_height / 2)
        )
        
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        
        player_centered = (screen_center_x, screen_center_y)        
        
        self.camera.move_to(player_centered, speed)
        
    def on_draw(self):
        self.clear()
        self.camera.use()
        
        with self.light_layer:
            self.background_sprite_list.draw()
            self.coins.draw()
            self.scene.draw()
            
        self.gui_camera.use()        
        
        self.light_layer.draw(ambient_color=AMBIENT_COLOR)
        