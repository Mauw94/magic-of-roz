from typing import Any
import arcade
import arcade.gui
from data.mongodb_connector import get_database
from entities.player.player import Player
from helpers.consts import Consts
from entities.classes.class_type import ClassType
from managers.data_managers.characters_manager import CharactersManager


class CharSelectButton(arcade.gui.UIFlatButton):
    def __init__(self, x: float = 0, y: float = 0, width: float = 100, height: float = 50, text="", size_hint=None, size_hint_min=None, size_hint_max=None, style=None, **kwargs):
        super().__init__(x, y, width, height, text, size_hint,
                         size_hint_min, size_hint_max, style, **kwargs)

    def on_click(self, event: arcade.gui.UIOnClickEvent):
        # TODO create method that parses the gathered player to player obj
        self.characters_manager.load_player_object(self.character_info)

    def set_char_info(self, c_info: Any) -> None:
        self.character_info = c_info
    
    def set_characters_manager(self, c_manager: CharactersManager) -> None:
        self.characters_manager = c_manager

# TODO show character level


class CharacterSelectionView(arcade.View):
    def __init__(self, screen_w, screen_h):
        self.screen_width = screen_w
        self.screen_height = screen_h

        self.characters_manager = CharactersManager()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        characters = self.characters_manager.get_player_characters()
        self.v_box = arcade.gui.UIBoxLayout()

        if len(characters) > 0:
            for c in characters:
                button = CharSelectButton(
                    text=c["name"] + " - " + c["class"].lower(), width=200)
                button.set_characters_manager(self.characters_manager)
                button.set_char_info(c)
                self.v_box.add(button.with_space_around(bottom=20))

        else:
            ui_error_label = arcade.gui.UILabel(text="No characters found",
                                                     width=450,
                                                     height=40,
                                                     font_size=24,
                                                     font_name="Kenney Future")

            self.v_box.add(ui_error_label.with_space_around(bottom=20))
            back_button = arcade.gui.UIFlatButton(text="Back", width=200)
            self.v_box.add(back_button)

            back_button.on_click = self.on_click_back

        self.manager.add(arcade.gui.UIAnchorWidget(
            anchor_x="center_x",
            anchor_y="center_y",
            child=self.v_box
        ))
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)
        super().__init__()

    def on_click_back(self, event):
        from views.main_menu import MainMenu
        game_view = MainMenu(
            self.screen_width, self.screen_height)
        self.window.show_view(game_view)

    def on_draw(self):
        self.clear()
        self.manager.draw()
