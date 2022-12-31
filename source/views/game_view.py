import os
import arcade
from helpers.consts import Consts
from entities.player import Player
from input.keys import Keys

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
        
        # TODO load sounds
        # TODO create input handler class        
        
    
    def on_show_view(self):        
        self.setup()
        
    def setup(self):    
        self.camera = arcade.Camera(self.window.width, self.window.height)
        self.gui_camera = arcade.Camera(self.window.width, self.window.height)
        
        map_name = ":resources:tiled_maps/grass.json"
        
        self.tile_map = arcade.load_tilemap(
            map_name, Consts.SPRITE_SCALING_TILES
        )
        self.scene = arcade.Scene.from_tilemap(self.tile_map)
        #self.scene = arcade.Scene()
        self.player = Player()
        self.player.center_x = Consts.SPRITE_SIZE * 1 + Consts.SPRITE_SIZE / 2
        self.player.center_y = Consts.SPRITE_SIZE * 1 + Consts.SPRITE_SIZE / 2
        self.scene.add_sprite("Player", self.player)    
           
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player,
            gravity_constant=0
        )

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
        
        # print(self.player.change_x)
        # print("X: ", self.player.center_x)
        # print("Y: ", self.player.center_y)

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
        self.scene.draw()
        self.gui_camera.use()