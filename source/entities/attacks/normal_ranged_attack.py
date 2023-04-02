import arcade
from entities.attacks.ranged_attack import RangedAttack


class NormalRangedAttack(RangedAttack):
    def __init__(self):
        super().__init__("space_shooter", "laserBlue01")

        self._mana_cost = 10

        self.damage = 0
        self.sound = arcade.load_sound(":resources:sounds/hurt5.wav")

    def set_damage(self, damage: int) -> None:
        self.damage = damage

    @property
    def mana_cost(self) -> int:
        return self._mana_cost

    @mana_cost.setter
    def mana_cost(self, cost) -> None:
        self._mana_cost = cost
