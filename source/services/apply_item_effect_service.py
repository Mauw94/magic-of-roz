from typing import List

import arcade

from entities.player.player import Player
from entities.items.consumables.health_globe import HealthGlobe
from entities.items.consumables.gold_coin import GoldCoin
from entities.items.consumables.mana_globe import ManaGlobe
from entities.items.consumables.speed_globe import SpeedGlobe
from services.damage_event_service import TextEvent, TextEventService
from managers.resource_managers.sound_manager import SoundManager
from helpers.static_data import (
    COIN_COLLECT_SOUND,
    HP_ADD_SOUND,
    MANA_ADD_SOUND,
    SPEED_ADD_SOUND,
)


class ApplyItemEffectService:
    def __init__(self, text_event_service: TextEventService):
        self.text_event_service = text_event_service
        self.sound_manager = SoundManager(with_preferred_volume=True)

    def apply_item_effect(self, items: List[arcade.Sprite], player: Player) -> None:
        for item in items:
            if type(item) is HealthGlobe:
                self.sound_manager.play_sound(HP_ADD_SOUND)
                added_hp = player.resource_manager.add_hp(item.value)

                self.text_event_service.add_to_events(
                    TextEvent(
                        "+" + str(added_hp) + " hp",
                        player.center_x,
                        player.center_y + 60,
                        arcade.csscolor.GREEN,
                        18,
                    )
                )

            elif type(item) is ManaGlobe:
                self.sound_manager.play_sound(MANA_ADD_SOUND)
                added_mana = player.resource_manager.add_mana(item.value)

                self.text_event_service.add_to_events(
                    TextEvent(
                        "+" + str(added_mana) + " mana",
                        player.center_x,
                        player.center_y + 60,
                        arcade.csscolor.BLUE,
                        18,
                    )
                )

            elif type(item) is SpeedGlobe:
                self.sound_manager.play_sound(SPEED_ADD_SOUND)
                player.apply_item_effect_movement(item.value, 50)

                self.text_event_service.add_to_events(
                    TextEvent(
                        "+" + str(item.value),
                        player.center_x,
                        player.center_y + 60,
                        arcade.csscolor.BLUE,
                        18,
                    )
                )

            elif type(item) is GoldCoin:
                self.sound_manager.play_sound(COIN_COLLECT_SOUND)
                player.add_gold(item.value)

                self.text_event_service.add_to_events(
                    TextEvent(
                        "+" + str(item.value),
                        player.center_x - 15,
                        player.center_y + 60,
                        arcade.csscolor.YELLOW,
                        18,
                    )
                )

            item.remove_from_sprite_lists()
