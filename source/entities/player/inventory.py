from entities.items.item_base import ItemBase
from engine_extensions.drawing_engine import DrawingEngine
from helpers.logging.logger import Logger
from helpers.consts import Consts


class Inventory:
    def __init__(self):
        self.inventory: list[ItemBase] = []

        self.__space = 5
        self.__default_item_widht = Consts.SPRITE_IMAGE_SIZE
        self.__default_item_height = Consts.SPRITE_IMAGE_SIZE

    def add_item(self, item: ItemBase) -> bool:
        if len(self.inventory) < 5:
            self.inventory.append(item)
            return True
        return False

    def get_item(self, index: int) -> ItemBase:
        if len(self.inventory) > 0:
            return self.inventory[index]

    def get_items(self) -> list[ItemBase]:
        return self.inventory

    def draw(self, screen_pos_x: int, screen_pos_y: int, scale: float) -> None:
        self.__draw_inventory_space(screen_pos_x, screen_pos_y, scale)

        if len(self.inventory) > 0:
            for index, item in enumerate(self.inventory):
                x = screen_pos_x - (30 + index * 45)
                y = screen_pos_y
                DrawingEngine.draw_item_texture(x, y, scale, item.texture)

    def __draw_inventory_space(
        self, screen_pos_x: int, screen_pos_y: int, scale: float
    ) -> None:
        for i in range(self.__space):
            x = screen_pos_x - (30 + i * 45)
            y = screen_pos_y
            DrawingEngine.draw_inventory_space(
                x,
                y,
                self.__default_item_widht * scale,
                self.__default_item_height * scale,
            )
