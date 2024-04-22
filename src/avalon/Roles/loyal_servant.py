from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.avalon.player import Player

from src.avalon.Roles.role import Role


class LoyalServant(Role):
    team = Role.GOOD
    name = "Loyal Servant"

    def info(self, players: list[Player], player: Player) -> str:
        return "You are a Loyal Servant of King Arthur of Britain. You don't know anything."
