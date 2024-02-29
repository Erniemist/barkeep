from typing import List

from src.avalon.player import Player
from src.avalon.Roles.role import Role


def find_other_evils(players: List[Player], me: Player):
    other_evil_players = [
        player.name for player in players if player.is_evil() and player != me
    ]
    return other_evil_players


class Morgana(Role):
    team = Role.EVIL
    name = "Morgana"

    def info(self, players: List[Player], player: Player) -> str:
        other_evil_players = find_other_evils(players, player)
        return f"You are Morgana. You know that {' and '.join(other_evil_players)} is your sinister accomplice."
