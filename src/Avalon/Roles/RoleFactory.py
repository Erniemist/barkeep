from src.Avalon.Roles.LoyalServant import LoyalServant
from src.Avalon.Roles.Merlin import Merlin
from src.Avalon.Roles.Minion import Minion
from src.Avalon.Roles.Morgana import Morgana
from src.Avalon.Roles.Percival import Percival
from src.Avalon.Roles.Role import Role


def from_name(name: str) -> Role:
    if name == LoyalServant.name:
        return LoyalServant()
    if name == Morgana.name:
        return Morgana()
    if name == Merlin.name:
        return Merlin()
    if name == Percival.name:
        return Percival()
    if name == Minion.name:
        return Minion()

    raise Exception(f'{name} is not a role')
