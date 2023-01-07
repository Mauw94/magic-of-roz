from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from views.game_view import GameView
from typing import Tuple
import arcade


class HealthBar:
    def __init__(
        self,
        owner,
        bar_list: arcade.SpriteList,
        width: int,
        height: int,
        position: Tuple[float, float],
        border_size: int = 4
    ):
        self.owner = owner
        self.bar_list = bar_list

        self._box_width = width
        self._box_height = height
        self._center_x = 0
        self._center_y = 0
        self._fullness = 0
        self._full_color = arcade.color.GREEN
        self._background_color = arcade.color.BLACK

        self._background_box = arcade.SpriteSolidColor(
            self._box_width + border_size,
            self._box_height + border_size,
            self._background_color
        )

        self._full_box = arcade.SpriteSolidColor(
            self._box_width,
            self._box_height,
            self._full_color
        )

        self.bar_list.append(self._background_box)
        self.bar_list.append(self._full_box)

        self.fullness = 1  # amount of green to draw in the healthbar
        self.position = position  # position above entities head

    @property
    def position(self):
        return self._center_x, self._center_y

    @position.setter
    def position(self, new_position):
        if new_position != self.position:
            self._center_x, self._center_y = new_position
            self._background_box.position = new_position
            self._full_box.position = new_position
            self._full_box.left = self._center_x - (self._box_width // 2)

    @property
    def fullness(self):
        return self._fullness

    @fullness.setter
    def fullness(self, new_fullness):
        if not 0 <= new_fullness <= 1:
            raise ValueError(
                f"Got {new_fullness}, but fullness must be between 0 and 1."
            )

        self._fullness = new_fullness
        if new_fullness == 0:
            self.bar_list.remove(self._background_box)
            self.bar_list.remove(self._full_box)
        else:
            self._full_box.width = self._box_width * new_fullness
            self._full_box.left = self._center_x - (self._box_width // 2)
