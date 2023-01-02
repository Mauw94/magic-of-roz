from entities.entity import Entity

class ZombieEnemey(Entity):
    def __init__(self):
        super().__init__("zombie", "zombie")
        
        self.change_x = 2