from typing import List

from src.Avalon.Player import Player
from src.Avalon.Roles.Role import Role


class Merlin(Role):
    team = Role.GOOD
    name = "Merlin"

    def info(self, players: List[Player], player: Player) -> str:
        evil_players = [player.name for player in players if player.is_evil()]
        return f"You are Merlin. {' and '.join(evil_players)} are Evil."
