from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.avalon.player import Player

from src.avalon.Roles.role import Role


class Merlin(Role):
    team = Role.GOOD
    name = "Merlin"

    def info(self, players: list[Player], player: Player) -> str:
        evil_players = [player.name for player in players if player.is_evil()]
        return f"You are Merlin. {' and '.join(evil_players)} are Evil."
