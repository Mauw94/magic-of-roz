import arcade
import arcade.gui
from views.character_creation import CharacterCreationView
from views.character_selection_view import CharacterSelectionView


class MainMenu(arcade.View):
    def __init__(self, screen_width, screen_height) -> None:
        self.screen_height = screen_height
        self.screen_width = screen_width

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        self.v_box = arcade.gui.UIBoxLayout()

        start_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
        self.v_box.add(start_button.with_space_around(bottom=20))

        char_creation_button = arcade.gui.UIFlatButton(
            text="Create Character", width=200)
        self.v_box.add(char_creation_button.with_space_around(bottom=20))

        char_selection_button = arcade.gui.UIFlatButton(
            text="Character selection", width=200)
        self.v_box.add(char_selection_button.with_space_around(bottom=20))

        quit_button = arcade.gui.UIFlatButton(text="Quit", width=200)
        self.v_box.add(quit_button)

        start_button.on_click = self.on_click_start
        char_creation_button.on_click = self.on_click_char_creation
        char_selection_button.on_click = self.on_click_char_selection
        quit_button.on_click = self.on_click_quit

        self.manager.add(arcade.gui.UIAnchorWidget(
            anchor_x="center_x",
            anchor_y="center_y",
            child=self.v_box
        ))

        super().__init__()

    def on_click_start(self, event):
        print("start: ", event)

    def on_click_char_creation(self, event):
        game_view = CharacterCreationView(
            self.screen_width, self.screen_height)
        self.window.show_view(game_view)

    def on_click_char_selection(self, event):
        game_view = CharacterSelectionView(
            self.screen_width, self.screen_height
        )
        self.window.show_view(game_view)

    def on_click_quit(self, event):
        arcade.exit()

    def on_draw(self):
        self.clear()
        self.manager.draw()
    