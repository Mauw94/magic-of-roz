from entities.attacks.ranged_attack import RangedAttack
import arcade


class ZombieAttack(RangedAttack):
    def __init__(self, mana_cost, damage):
        super().__init__("space_shooter", "meteorGrey_med1", mana_cost, damage)

        self.sound = arcade.load_sound(":resources:sounds/hurt5.wav")
