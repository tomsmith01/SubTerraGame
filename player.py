from enum import Enum
from random import Random

class Player:
    def __init__(self, type):
        self.health_points = 3
        self.player_type = type
        if self.player_type == isinstance(PlayerType.BODYGUARD):
            pass

class PlayerType(Enum):
    BODYGUARD = 1
