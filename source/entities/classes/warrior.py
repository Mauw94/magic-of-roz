from source.entities.classes.class_type import ClassType


class Warrior():
    def __init__(self):
        self.type = ClassType.WARRIOR

    def get_class_type(self) -> ClassType:
        return self.type
