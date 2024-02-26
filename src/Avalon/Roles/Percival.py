from typing import List

from src.Avalon.Player import Player
from src.Avalon.Roles.Role import Role
from src.DiscordMemberInterface import DiscordMemberInterface


class Percival(Role):
    team = Role.GOOD
    name = "Percival"

    def __init__(self, member: DiscordMemberInterface):
        super().__init__(member)

    def info(self, players: List[Player], player: Player) -> str:
        wizards = [player.name for player in players if player.role.name in ["Morgana", "Merlin"]]
        return f"You are Percival. {' and '.join(wizards)} are Merlin and Morgana, but you know not who is who..."
