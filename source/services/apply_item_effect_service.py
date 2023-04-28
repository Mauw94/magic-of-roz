from typing import List

import arcade

from entities.player.player import Player
from entities.items.consumables.health_globe import HealthGlobe
from entities.items.consumables.mana_globe import ManaGlobe


class ApplyItemEffectService:
    def __init__(self):
        # pass player and item list
        # check per item what the enhancement is for the player
        pass

    def apply_item_effect(self, items: List[arcade.Sprite], player: Player) -> None:
        for item in items:
            if type(item) is HealthGlobe:
                player.resource_manager.add_hp(item.add_life)
            elif type(item) is ManaGlobe:
                player.resource_manager.add_mana(item.add_mana)
