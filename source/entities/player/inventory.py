import arcade
from entities.items.item_base import ItemBase
from engine_extensions.drawing_engine import DrawingEngine
from helpers.logging.logger import Logger
from helpers.consts import Consts
from services.apply_item_effect_service import ApplyItemEffectService


class Inventory:
    def __init__(self, player, apply_item_effect_service: ApplyItemEffectService):
        self.inventory: list[(ItemBase, int)] = []
        self.selected_item_index: int = 0
        self.player = player

        self.__space = 5
        self.__default_item_widht = Consts.SPRITE_IMAGE_SIZE
        self.__default_item_height = Consts.SPRITE_IMAGE_SIZE
        self.__apply_item_effect_service = apply_item_effect_service

    def add_item(self, item: ItemBase) -> bool:
        if len(self.inventory) < 5:
            cur_len = len(self.inventory)
            self.inventory.insert(0, (item, cur_len))
            return True
        return False

    def move_left(self) -> None:
        self.selected_item_index -= 1
        if self.selected_item_index < 0:
            self.selected_item_index = self.__space - 1

    def move_right(self) -> None:
        self.selected_item_index += 1
        if self.selected_item_index > self.__space - 1:
            self.selected_item_index = 0

    def use_item(self, index: int = None) -> None:
        if index is not None:
            self.selected_item_index = index

        Logger.log_debug(
            f"Attempting to use item in inventory at position: {self.selected_item_index}"
        )

        item = self.get_item(self.selected_item_index)
        if item is not None:
            self.__apply_item_effect_service.apply_item_effect_on_player(
                item[0], self.player
            )
            self.remove_item(self.selected_item_index)

    def get_item(self, index: int) -> (ItemBase, int):
        if len(self.inventory) > 0:
            return next(filter(lambda x: x[1] == index, self.inventory), None)
        return None

    def get_items(self) -> list[(ItemBase, int)]:
        return self.inventory

    def remove_item(self, index: int) -> bool:
        item = self.get_item(index)
        if item is not None:
            self.inventory.remove(item)
            # rearrange item
            inventory_clone: list[(ItemBase, int)] = []
            for index, item in enumerate(reversed(self.inventory)):
                new_item = (item[0], index)
                inventory_clone.insert(0, new_item)
            self.inventory = inventory_clone
            return True
        return False

    def draw(self, screen_pos_x: int, screen_pos_y: int, scale: float) -> None:
        self.__draw_inventory_space(screen_pos_x, screen_pos_y, scale)

        if len(self.inventory) > 0:
            for item in self.inventory:
                x = screen_pos_x - (self.__space - item[1]) * 45
                y = screen_pos_y
                DrawingEngine.draw_item_texture(x, y, scale, item[0].texture)

    def __draw_inventory_space(
        self, screen_pos_x: int, screen_pos_y: int, scale: float
    ) -> None:
        for i in range(self.__space):
            x = screen_pos_x - (self.__space - i) * 45
            y = screen_pos_y

            if i == self.selected_item_index:
                color = arcade.csscolor.BLACK
            else:
                color = arcade.csscolor.WHITE

            DrawingEngine.draw_inventory_space(
                x,
                y,
                self.__default_item_widht * scale,
                self.__default_item_height * scale,
                color,
            )
