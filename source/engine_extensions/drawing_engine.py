import arcade


class DrawingEngine:
    def __init__(self):
        pass

    def draw_text(text: str, x: int, y: int, color: arcade.csscolor, font_size: int) -> None:
        arcade.draw_text(text, x, y, color, font_size)

    def calcuate_offset_text_center_above_entity(text: str) -> int:
        o = len(text)
        if o >= 19:
            return 95
        elif o >= 17:
            return 87
        elif o >= 15:
            return 75
        elif o >= 12:
            return 70
        elif o >= 10:
            return 63
        elif o >= 7:
            return 50
        elif o >= 5:
            return 20
        else:
            return 15
