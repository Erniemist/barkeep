from abc import ABC


class Role(ABC):
    team: str
    name: str
    GOOD = "good"
    EVIL = "evil"


    def __init__(self, player):
        self.player = player

    def info(self, players) -> str:
        raise NotImplemented
