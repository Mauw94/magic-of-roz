from entities.attacks.ranged_attack import RangedAttack
import arcade

class ZombieAttack(RangedAttack):
    def __init__(self):
        super().__init__("space_shooter", "meteorGrey_med1")

        self.damage = 7
        self.sound = arcade.load_sound(":resources:sounds/hurt5.wav")
