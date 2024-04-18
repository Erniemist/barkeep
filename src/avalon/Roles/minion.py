from typing import List

from src.avalon.player import Player
from src.avalon.Roles.role import Role


class Minion(Role):
    team = Role.EVIL
    name = "Loathsome Minion of Mordred"

    def info(self, players: List[Player], player: Player) -> str:
        return f"You are a {Minion.name}. Your dark allies are: {self.join_names(player.other_evils(players))}."
