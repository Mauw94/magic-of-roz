from entities.enemy import Enemy

class ZombieEnemey(Enemy):
    def __init__(self):
        super().__init__("zombie", "zombie")
        
        self.change_x = 2