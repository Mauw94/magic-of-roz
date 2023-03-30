from datetime import datetime
import arcade
from entities.classes.class_type import ClassType

from entities.player import Player
from helpers.consts import Consts

# TODO: show character creation screen when there's no save file yet


class CharacterCreationView(arcade.View):
    def __init__(self, screen_width, screen_height) -> None:
        self.screen_width = screen_width
        self.screen_height = screen_height
        super().__init__()

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        arcade.draw_text(
            "Character Creation",
            self.screen_width / 2,
            self.screen_height / 2,
            arcade.color.WHITE,
            font_size=30,
            anchor_x="center"
        )

    def set_player_class_type(self, type):
        self.player_character_class_type = type

    def set_player_character_name(self, name):
        self.player_character_name = name

    def create(self):
        if self.player_character_class_type is not None and self.player_character_name is not None:
            p = Player(Consts.SCREEN_WIDTH // 2,
                       Consts.SCREEN_HEIGHT // 2,
                       self.player_character_class_type,
                       self.player_character_name)
            self.save_player_character_info()
            return p

    def save_player_character_info(self):
        i = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        m = "creation: " + i + "\n" + "player_character_class: " + self.player_character_class_type.name + \
            "\n" + "player_character_name: " + self.player_character_name + "\n\n"

        f = open("character" + i + ".txt", "a")
        f.write(m)
        f.flush()
        f.close()
