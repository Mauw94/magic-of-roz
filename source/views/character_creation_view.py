import arcade
import arcade.gui
import arcade.experimental.uistyle
from entities.classes.class_type import ClassTypeEnum
from managers.data_managers.characters_manager import CharactersManager
from helpers.logging.logger import Logger


class CharacterCreationView(arcade.View):
    def __init__(self, screen_width, screen_height) -> None:
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.characters_manager = CharactersManager([])
        self.player_character_class_type = None
        self.player_character_name = ""

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        self.v_box = arcade.gui.UIBoxLayout(vertical=False)
        self.h_box = arcade.gui.UIBoxLayout()

        self.ui_error_label = arcade.gui.UILabel(
            text="", width=600, height=40, font_size=24, font_name="Kenney Future"
        )
        self.h_box.add(self.ui_error_label.with_space_around(bottom=50))

        self.ui_text_label = arcade.gui.UILabel(
            text="Chosen class: ",
            width=650,
            height=40,
            font_size=24,
            font_name="Kenney Future",
        )
        self.h_box.add(self.ui_text_label.with_space_around(bottom=50))

        n_button = arcade.gui.UIFlatButton(text="Necromancer", width=150)
        self.v_box.add(n_button.with_space_around(right=10))
        d_button = arcade.gui.UIFlatButton(text="Druid", width=150)
        self.v_box.add(d_button.with_space_around(right=10))
        w_button = arcade.gui.UIFlatButton(text="Warrior", width=150)
        self.v_box.add(w_button.with_space_around(right=10))
        wiz_button = arcade.gui.UIFlatButton(text="Wizard", width=150)
        self.v_box.add(wiz_button.with_space_around(right=10))

        self.label = arcade.gui.UILabel(
            text="Character name: ",
            text_color=arcade.color.DARK_RED,
            width=600,
            height=40,
            font_size=24,
            font_name="Kenney Future",
        )

        self.input_name = arcade.gui.UIInputText(font_size=24, width=450)
        self.h_box.add(self.label)
        self.h_box.add(self.input_name)

        create_button = arcade.gui.UIFlatButton(text="Create character", width=150)
        self.h_box.add(create_button.with_space_around(top=200))

        back_button = arcade.gui.UIFlatButton(text="Back", width=75)
        self.h_box.add(back_button.with_space_around(top=30))

        n_button.on_click = self.on_click_necro
        d_button.on_click = self.on_click_druid
        w_button.on_click = self.on_click_warrior
        wiz_button.on_click = self.on_click_wizard
        create_button.on_click = self.on_click_create
        back_button.on_click = self.on_back

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x", anchor_y="center_y", child=self.v_box
            )
        )

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x", anchor_y="center_y", child=self.h_box
            )
        )

        super().__init__()

    def on_click_create(self, event) -> None:
        if len(self.input_name.text) > 0:
            self.player_character_name = self.input_name.text
            if self.player_character_class_type is not None:
                self.create()
                from views.character_selection_view import CharacterSelectionView

                game_view = CharacterSelectionView(
                    self.screen_width, self.screen_height
                )
                self.window.show_view(game_view)
            else:
                self.ui_error_label.text = "Choose a class!"
        else:
            self.ui_error_label.text = "Fill in a character name!"

    def on_click_necro(self, event) -> None:
        self.ui_text_label.text = "Chosen class: Necromancer"
        self.set_player_class_type(ClassTypeEnum.NECROMANCER)

    def on_click_druid(self, event) -> None:
        self.ui_text_label.text = "Chosen class: Druid"
        self.set_player_class_type(ClassTypeEnum.DRUID)

    def on_click_warrior(self, event) -> None:
        self.ui_text_label.text = "Chosen class: Warrior"
        self.set_player_class_type(ClassTypeEnum.WARRIOR)

    def on_click_wizard(self, event) -> None:
        self.ui_text_label.text = "Chosen class: Wizard"
        self.set_player_class_type(ClassTypeEnum.WIZARD)

    def on_back(self, event) -> None:
        from views.main_menu import MainMenu

        game_view = MainMenu(self.screen_width, self.screen_height)
        self.window.show_view(game_view)

    def on_draw(self):
        self.clear()
        self.manager.draw()

    def set_player_class_type(self, type) -> None:
        self.player_character_class_type = type

    def set_player_character_name(self, name) -> None:
        self.player_character_name = name

    def create(self) -> None:
        Logger.log_info("Creating new character")
        self.characters_manager.save_new_character_info(
            self.player_character_name, self.player_character_class_type
        )
