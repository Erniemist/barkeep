from typing import List

from src.Avalon.Player import Player
from src.Avalon.Roles.Role import Role


def find_other_evils(players: List[Player], me: Player):
    other_evil_players = [
        player.name
        for player in players
        if player.is_evil() and player != me
    ]
    return other_evil_players


class Minion(Role):
    team = Role.EVIL
    name = "Loathsome Minion of Mordred"

    def info(self, players: List[Player], player: Player) -> str:
        other_evils = find_other_evils(players, player)
        if len(other_evils) == 0:
            return f"You are a {Minion.name}. You have no known allies."
        if len(other_evils) == 1:
            return f"You are a {Minion.name}. You know that {other_evils[0]} is your dark ally."
        if len(other_evils) == 2:
            return f"You are a {Minion.name}. You know that {other_evils[0]} and {other_evils[1]} are your dark allies."

        return f"You are a {Minion.name}. " \
            f"You know that {', '.join(other_evils[:-1])}, and {other_evils[-1]} are your dark allies."
