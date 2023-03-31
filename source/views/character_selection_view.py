import arcade
import arcade.gui
from data.mongodb_connector import get_database


class CharacterSelectionView(arcade.View):
    def __init__(self):
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        characters = self.get_player_characters()

        if len(characters) > 0:
            self.v_box = arcade.gui.UIBoxLayout()
            for c in characters:
                button = arcade.gui.UIFlatButton(
                    text=c["character_name"] + " - " + c["character_class"].lower(), width=200)

                @button.event("on_click")
                def on_click(event):
                    print(c["character_name"])

                self.v_box.add(button.with_space_around(bottom=20))

            self.manager.add(arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box
            ))

        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        super().__init__()

    # def on_click(self, event):
    #     print(event)

    def get_player_characters(self) -> list:
        db = get_database()
        c = list(db['characters'].find())
        return c

    def on_draw(self):
        self.clear()
        self.manager.draw()
