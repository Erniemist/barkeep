from typing import List

from src.avalon.player import Player
from src.avalon.Roles.role import Role


class Morgana(Role):
    team = Role.EVIL
    name = "Morgana"

    def info(self, players: List[Player], player: Player) -> str:
        return f"You are {Morgana.name}. Your dark allies are: {self.join_names(player.other_evils(players))}."
