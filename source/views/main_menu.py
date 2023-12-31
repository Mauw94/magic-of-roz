import arcade
import arcade.gui
from views.character_creation_view import CharacterCreationView
from views.character_selection_view import CharacterSelectionView


class MainMenu(arcade.View):
    def __init__(self, screen_width, screen_height) -> None:
        self.screen_height = screen_height
        self.screen_width = screen_width

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(arcade.color.BLUE_GRAY)

        self.v_box = arcade.gui.UIBoxLayout()

        # start_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
        # self.v_box.add(start_button.with_space_around(bottom=20))

        self.char_selection_button = arcade.gui.UIFlatButton(
            text="Character selection", width=200
        )
        self.v_box.add(self.char_selection_button.with_space_around(bottom=20))

        char_creation_button = arcade.gui.UIFlatButton(
            text="Create Character", width=200
        )
        self.v_box.add(char_creation_button.with_space_around(bottom=20))

        self.quit_button = arcade.gui.UIFlatButton(text="Quit", width=200)
        self.v_box.add(self.quit_button)

        # start_button.on_click = self.on_click_start
        char_creation_button.on_click = self.on_click_char_creation
        self.char_selection_button.on_click = self.on_click_char_selection
        self.quit_button.on_click = self.on_click_quit

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x", anchor_y="center_y", child=self.v_box
            )
        )

        super().__init__()

    def on_click_start(self, event):
        self.manager.disable()
        print("start: ", event)

    def on_click_char_creation(self, event):
        game_view = CharacterCreationView(self.screen_width, self.screen_height)
        self.manager.disable()
        self.window.show_view(game_view)

    def on_click_char_selection(self, event):
        game_view = CharacterSelectionView(self.screen_width, self.screen_height)
        self.manager.disable()
        self.window.show_view(game_view)

    def on_click_quit(self, event):
        # disables the mouse_pressed and other events from happening when on another view
        self.manager.disable()
        arcade.exit()

    def on_draw(self):
        self.clear()
        self.manager.draw()
