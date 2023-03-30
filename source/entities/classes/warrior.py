from source.entities.classes.base import BaseClass
from source.entities.classes.class_type import ClassType


class Warrior(BaseClass):
    def __init__(self):
        self.type = ClassType.WARRIOR
        super.__init__()

    def type(self) -> ClassType:
        return self.type
