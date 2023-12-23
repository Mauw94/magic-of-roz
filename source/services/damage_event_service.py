import arcade
from engine_extensions.drawing_engine import DrawingEngine
from helpers.logging.logger import Logger


# TODO: keep track of the lifetime inside the DamageEvent object
# when lifetime expires the object can be removed
# this way we don't need a queue to store events,
# but multiple events can happen at the same time
# give an event also a slight different x and y value
# so they don't all overlap at the same position

class DamageEvent:
    def __init__(
        self, text: str, x: int, y: int, color: arcade.csscolor, font_size: int
    ):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.font_size = font_size

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


class DamageEventService:
    def __init__(self):
        self.time_to_show_dmg_text = 15
        self.cur_show_dmg_text = 0
        self.queue = []
        self.cur_event: DamageEvent = None

    def draw(self):
        self.update()

    def add_to_queue(self, event: DamageEvent):
        Logger.log_info("Add new event to EventService")
        self.queue.append(event)

    def update(self):
        if len(self.queue) == 0 and self.cur_event is None:
            pass
        elif len(self.queue) > 0 and self.cur_event is None:
            self.cur_event = self.queue.pop()

        if self.cur_event is not None:
            self.cur_show_dmg_text += 1
            if self.cur_show_dmg_text >= self.time_to_show_dmg_text:
                self.cur_show_dmg_text = 0
                self.cur_event = None

    def draw(self):
        if self.cur_event is not None:
            DrawingEngine.draw_damage_text(
                self.cur_event.get_text(),
                self.cur_event.get_x(),
                self.cur_event.get_y(),
                self.cur_event.get_color(),
                self.cur_event.get_font_size(),
            )
