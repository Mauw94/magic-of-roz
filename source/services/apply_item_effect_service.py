from typing import List

import arcade

from entities.player.player import Player
from entities.items.consumables.health_globe import HealthGlobe
from entities.items.consumables.gold_coin import GoldCoin
from entities.items.consumables.mana_globe import ManaGlobe
from services.damage_event_service import TextEvent, TextEventService
from managers.resource_managers.sound_manager import SoundManager
from helpers.static_data import COIN_COLLECT_SOUND, HP_ADD_SOUND, MANA_ADD_SOUND


class ApplyItemEffectService:
    def __init__(self, text_event_service: TextEventService):
        self.text_event_service = text_event_service
        self.sound_manager = SoundManager()

    def apply_item_effect(self, items: List[arcade.Sprite], player: Player) -> None:
        for item in items:
            if type(item) is HealthGlobe:
                self.sound_manager.play_sound(HP_ADD_SOUND)
                self.text_event_service.add_to_events(
                    TextEvent(
                        "+" + str(item.add_life) + " hp",
                        player.center_x,
                        player.center_y + 60,
                        arcade.csscolor.GREEN,
                        18,
                    )
                )
                player.resource_manager.add_hp(item.add_life)
            elif type(item) is ManaGlobe:
                self.sound_manager.play_sound(MANA_ADD_SOUND)
                self.text_event_service.add_to_events(
                    TextEvent(
                        "+" + str(item.add_mana) + " mana",
                        player.center_x,
                        player.center_y + 60,
                        arcade.csscolor.BLUE,
                        18,
                    )
                )
                player.resource_manager.add_mana(item.add_mana)
            elif type(item) is GoldCoin:
                self.sound_manager.play_sound(COIN_COLLECT_SOUND)
                self.text_event_service.add_to_events(
                    TextEvent(
                        "+" + str(1),
                        player.center_x - 15,
                        player.center_y + 60,
                        arcade.csscolor.YELLOW,
                        18,
                    )
                )

                # TODO: increase gold count for player, also save this stat
            item.remove_from_sprite_lists()
