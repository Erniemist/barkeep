from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.avalon.player import Player

from src.avalon.Roles.role import Role


class Percival(Role):
    team = Role.GOOD
    name = "Percival"

    def info(self, players: list[Player], player: Player) -> str:
        wizards = [
            player.name
            for player in players
            if player.role.name in ["Morgana", "Merlin"]
        ]
        return f"You are Percival. {' and '.join(wizards)} are Merlin and Morgana, but you know not who is who..."
