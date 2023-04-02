import arcade
from entities.attacks.ranged_attack import RangedAttack


class NormalRangedAttack(RangedAttack):
    def __init__(self):
        super().__init__("space_shooter", "laserBlue01")

        self.damage = 0
        self.sound = arcade.load_sound(":resources:sounds/hurt5.wav")

    def set_damage(self, damage: int):
        self.damage = damage
