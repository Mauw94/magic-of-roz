from typing import List

import arcade

from entities.player.player import Player
from entities.items.consumables.health_globe import HealthGlobe
from entities.items.consumables.mana_globe import ManaGlobe
from services.damage_event_service import TextEvent, TextEventService


class ApplyItemEffectService:
    def __init__(self, text_event_service: TextEventService):
        self.text_event_service = text_event_service

    def apply_item_effect(self, items: List[arcade.Sprite], player: Player) -> None:
        for item in items:
            if type(item) is HealthGlobe:
                self.text_event_service.add_to_events(
                    TextEvent(
                        "+" + str(item.add_life) + " hp",
                        player.center_x - 15,
                        player.center_y + 60,
                        arcade.csscolor.GREEN,
                        18,
                    )
                )
                player.resource_manager.add_hp(item.add_life)
                item.remove_from_sprite_lists()
            elif type(item) is ManaGlobe:
                self.text_event_service.add_to_events(
                    TextEvent(
                        "+" + str(item.add_mana) + " mana",
                        player.center_x - 15,
                        player.center_y + 60,
                        arcade.csscolor.BLUE,
                        18,
                    )
                )
                player.resource_manager.add_mana(item.add_mana)
                item.remove_from_sprite_lists()
