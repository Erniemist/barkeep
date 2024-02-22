from abc import ABC

from src.Avalon.Roles.LoyalServant import LoyalServant
from src.Avalon.Roles.Merlin import Merlin
from src.Avalon.Roles.Minion import Minion
from src.Avalon.Roles.Morgana import Morgana
from src.Avalon.Roles.Percival import Percival


def assign_role(player, role_name):
    if role_name is "Loyal Servant":
        return LoyalServant(player)
    if role_name is "Morgana":
        return Morgana(player)
    if role_name is "Merlin":
        return Merlin(player)
    if role_name is "Percival":
        return Percival(player)
    if role_name is "Loathsome Minion of Mordred":
        return Minion(player)


class Role(ABC):
    team: str
    name: str
    GOOD = "good"
    EVIL = "evil"

    def __init__(self, player):
        self.player = player

    def info(self, players) -> str:
        raise NotImplemented

    def is_evil(self):
        return self.team == Role.EVIL
