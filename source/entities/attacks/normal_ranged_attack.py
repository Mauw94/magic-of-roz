import arcade
from entities.attacks.ranged_attack import RangedAttack


class NormalRangedAttack(RangedAttack):
    def __init__(self, mana_cost, damage):
        super().__init__("space_shooter", "laserBlue01", mana_cost, damage)

        self.sound = arcade.load_sound(":resources:sounds/hurt5.wav")
