from typing import List

from src.Avalon.Player import Player
from src.Avalon.Roles.Role import Role


class LoyalServant(Role):
    team = Role.GOOD
    name = "Loyal Servant"

    def info(self, players: List[Player], player: Player) -> str:
        return "You are a Loyal Servant of King Arthur of Britain. You don't know anything."
