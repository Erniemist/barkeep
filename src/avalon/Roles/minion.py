from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.avalon.player import Player

from src.avalon.Roles.role import Role


class Minion(Role):
    team = Role.EVIL
    name = "Loathsome Minion of Mordred"

    def info(self, players: list[Player], player: Player) -> str:
        return f"You are a {Minion.name}. Your dark allies are: {self.join_names(player.other_evils(players))}."
