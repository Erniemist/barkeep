from src.avalon.Roles.loyal_servant import LoyalServant
from src.avalon.Roles.merlin import Merlin
from src.avalon.Roles.minion import Minion
from src.avalon.Roles.morgana import Morgana
from src.avalon.Roles.percival import Percival
from src.avalon.Roles.role import Role


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

    raise ValueError(f"{name} is not a role")
