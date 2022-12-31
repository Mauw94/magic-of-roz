import arcade
from helpers.consts import Consts
from views.main_menu import MainMenu

class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(Consts.SCREEN_WIDTH, Consts.SCREEN_HEIGHT, Consts.SCREEN_TITLE)
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        pass

    def on_draw(self):
        self.clear()

def main():
    window = arcade.Window(Consts.SCREEN_WIDTH, Consts.SCREEN_HEIGHT, Consts.SCREEN_TITLE)
    menu_view = MainMenu(Consts.SCREEN_WIDTH, Consts.SCREEN_HEIGHT)
    window.show_view(menu_view)
    arcade.run()

if __name__ == "__main__":
    main()

