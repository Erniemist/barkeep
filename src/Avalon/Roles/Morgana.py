from src.Avalon.Roles.Role import Role
from src.DiscordMemberInterface import DiscordMemberInterface


class Morgana(Role):
    team = Role.EVIL
    name = "Morgana"

    def __init__(self, member: DiscordMemberInterface):
        super().__init__(member)

    def info(self, players: list[Role], player) -> str:
        other_evil_players = [
            player.player.name
            for player in players
            if player.is_evil() and player.player != self.player
        ]
        return f"You are Morgana. You know that {' and '.join(other_evil_players)} is your sinister accomplice."
