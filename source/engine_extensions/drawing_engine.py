import arcade
from helpers.logging.logger import Logger
from PIL import ImageFont


class DrawingEngine:
    def __init__(self):
        pass

    def draw_text(
        text: str, x: int, y: int, color: arcade.csscolor, font_size: int
    ) -> None:
        arcade.draw_text(text, x, y, color, font_size)

    def calcuate_offset_text_center_above_entity(
        text: str, font_size: int, entity_width: int
    ) -> tuple[int, int]:
        font = ImageFont.load_default()
        size = font.getsize(text)
        x = DrawingEngine.__calc_x_offset(size[0], entity_width)
        return [x, size[1]]

    def __calc_x_offset(font_width: int, entity_width: int) -> int:
        if font_width < entity_width:
            return font_width - (entity_width // 4)
        else:
            return font_width - (entity_width // 2)
