import arcade
from engine_extensions.drawing_engine import DrawingEngine
from helpers.logging.logger import Logger


class DamageEvent:
    def __init__(
        self, text: str, x: int, y: int, color: arcade.csscolor, font_size: int
    ):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.font_size = font_size
        self.time_to_show_text = 15
        self.cur_show_text = 0
        self.can_remove = False

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


class DamageEventService:
    def __init__(self):
        self.events: list[DamageEvent] = []
        self.cur_event: DamageEvent = None

    def draw(self):
        self.update()

    def add_to_events(self, event: DamageEvent):
        Logger.log_info("Add new event to EventService")
        self.events.append(event)

    def update(self):
        for event in self.events:
            event.update()
            if event.can_remove:
                self.events.remove(event)

    def draw(self):
        for event in self.events:
            DrawingEngine.draw_damage_text(
                event.get_text(),
                event.get_x(),
                event.get_y(),
                event.get_color(),
                event.get_font_size(),
            )
