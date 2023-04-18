from entities.attacks.ranged_attack import RangedAttack
import arcade

class SpecialRangedAttack(RangedAttack):
    def __init__(self):
        super().__init__("space_shooter", "laserRed01")
        
        self.get_damage = 50
        self.sound = arcade.load_sound(":resources:sounds/hurt1.wav")
        
        # TODO image needs to be rotated somehow
        # self.texture.image.rotate(90)
        