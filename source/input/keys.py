import arcade
from typing import TYPE_CHECKING
from helpers.consts import Consts

if TYPE_CHECKING:
    from views.game_view import GameView


class Keys:
    def process_keychange(self, game: "GameView"):
        pass
        if game.right_pressed and not game.left_pressed:
            game.player.change_x = game.player.movement_speed
        elif game.left_pressed and not game.right_pressed:
            game.player.change_x = -game.player.movement_speed
        elif game.up_pressed and not game.down_pressed:
            game.player.change_y = game.player.movement_speed
        elif game.down_pressed and not game.up_pressed:
            game.player.change_y = -game.player.movement_speed

        # TODO fix for smoother movement
        # elif game.down_pressed and game.right_pressed and not game.up_pressed and not game.left_pressed:
        #     game.player.change_x = Consts.PLAYER_MOVEMENT_SPEED
        #     game.player_change_y = -Consts.PLAYER_MOVEMENT_SPEED
        else:
            game.player.change_x = 0
            game.player.change_y = 0

    def on_key_press(self, game: "GameView", key, modifiers):
        if key == arcade.key.A:
            game.left_pressed = True
        elif key == arcade.key.D:
            game.right_pressed = True
        elif key == arcade.key.S:
            game.down_pressed = True
        elif key == arcade.key.W:
            game.up_pressed = True

        if key == arcade.key.PLUS:
            game.camera.zoom(0.01)
        elif key == arcade.key.MINUS:
            game.camera.zoom(-0.01)

        # if key == arcade.key.Q:
        #     game.player.normal_ranged_attack_pressed = True

        # if key == arcade.key.E:
        #     game.player.special_ranged_attack_pressed = True

        if key == arcade.key.ESCAPE:
            game.escape_pressed = True

        if key == arcade.key.E:
            game.player.inventory.move_left()
        if key == arcade.key.Q:
            game.player.inventory.move_right()

        if key == arcade.key.F:
            game.player.inventory.use_item()

        self.process_keychange(game)

    def on_key_release(self, game: "GameView", key, modifiers):
        if key == arcade.key.A:
            game.left_pressed = False
        elif key == arcade.key.D:
            game.right_pressed = False
        elif key == arcade.key.S:
            game.down_pressed = False
        elif key == arcade.key.W:
            game.up_pressed = False

        # if key == arcade.key.Q:
        #     game.player.normal_ranged_attack_pressed = False

        # if key == arcade.key.E:
        #     game.player.special_ranged_attack_pressed = False

        if key == arcade.key.ESCAPE:
            game.escape_pressed = False

        self.process_keychange(game)

    def on_mouse_scroll(self, game, x, y, scroll_x, scroll_y):
        game.camera.zoom(-0.01 * scroll_y)

    def on_mouse_press(self, game: "GameView", x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            game.player.normal_ranged_attack_pressed = True
            game.player.set_mouse_pos(x, y)

    def on_mouse_release(self, game: "GameView", x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            game.player.normal_ranged_attack_pressed = False
