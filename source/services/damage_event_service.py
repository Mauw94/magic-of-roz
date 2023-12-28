import arcade
import random
from engine_extensions.drawing_engine import DrawingEngine
from helpers.logging.logger import Logger


class TextEvent:
    def __init__(
        self, text: str, x: int, y: int, color: arcade.csscolor, font_size: int
    ):
        self.text = text
        self.color = color
        self.font_size = font_size
        self.time_to_show_text = 15
        self.cur_show_text = 0
        self.can_remove = False
        self._max_x_variance = 15
        self._max_y_variance = 20
        self._set_x_y_variance(x, y)

    def update(self):
        self.cur_show_text += 1
        if self.cur_show_text >= self.time_to_show_text:
            self.can_remove = True

    def get_text(self) -> str:
        return self.text

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def get_color(self) -> int:
        return self.color

    def get_font_size(self) -> int:
        return self.font_size

    def _set_x_y_variance(self, x: int, y: int):
        x_variance = random.randint(1, self._max_x_variance)
        y_variance = random.randint(1, self._max_y_variance)
        plus_or_minus = random.randint(1, 2)

        if plus_or_minus == 1:
            self.x = x + x_variance
        elif plus_or_minus == 2:
            self.x = x - x_variance

        self.y = y + y_variance


class TextEventService:
    def __init__(self):
        self.events: list[TextEvent] = []
        self.cur_event: TextEvent = None

    def draw(self):
        self.update()

    def add_to_events(self, event: TextEvent):
        Logger.log_info("Add new event to EventService")
        self.events.append(event)

    def update(self):
        for event in self.events:
            event.update()
            if event.can_remove:
                self.events.remove(event)

    def draw(self):
        for event in self.events:
            DrawingEngine.draw_text(
                event.get_text(),
                event.get_x(),
                event.get_y(),
                event.get_color(),
                event.get_font_size(),
            )
