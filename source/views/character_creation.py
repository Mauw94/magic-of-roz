from datetime import datetime
import arcade
import arcade.gui
from entities.classes.class_type import ClassType
from entities.player import Player
from helpers.consts import Consts
from data.mongodb_connector import get_database

# TODO: show character creation screen when there's no save file yet


class CharacterCreationView(arcade.View):
    def __init__(self, screen_width, screen_height) -> None:
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        self.v_box = arcade.gui.UIBoxLayout(vertical=False)
        self.h_box = arcade.gui.UIBoxLayout()

        n_button = arcade.gui.UIFlatButton(text="Necromancer", width=150)
        self.v_box.add(n_button.with_space_around(right=10))
        d_button = arcade.gui.UIFlatButton(text="Druid", width=150)
        self.v_box.add(d_button.with_space_around(right=10))
        w_button = arcade.gui.UIFlatButton(text="Warrior", width=150)
        self.v_box.add(w_button.with_space_around(right=10))
        wiz_button = arcade.gui.UIFlatButton(text="Wizard", width=150)
        self.v_box.add(wiz_button.with_space_around(right=10))

        back_button = arcade.gui.UIFlatButton(text="Back", width=75)
        self.h_box.add(back_button.with_space_around(top=200))

        self.manager.add(arcade.gui.UIAnchorWidget(
            anchor_x="center_x",
            anchor_y="center_y",
            child=self.v_box
        ))

        self.manager.add(arcade.gui.UIAnchorWidget(
            anchor_x="center_x",
            anchor_y="center_y",
            child=self.h_box
        ))

        self.dbname = get_database()
        self.collection = self.dbname['characters']

        super().__init__()

    def on_draw(self):
        self.clear()
        self.manager.draw()

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
        character_info = {
            "player_id": 1,
            "character_name": self.player_character_name,
            "character_class": self.player_character_class_type.name,
            "creation_time": i
        }

        self.collection.insert_one(character_info)
