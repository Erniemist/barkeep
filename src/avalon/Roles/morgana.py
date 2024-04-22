from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.avalon.player import Player

from src.avalon.Roles.role import Role


class Morgana(Role):
    team = Role.EVIL
    name = "Morgana"

    def info(self, players: list[Player], player: Player) -> str:
        return f"You are {Morgana.name}. Your dark allies are: {self.join_names(player.other_evils(players))}."
