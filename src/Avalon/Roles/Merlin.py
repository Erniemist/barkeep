from src.Avalon.Roles.Role import Role
from src.DiscordMemberInterface import DiscordMemberInterface


class Merlin(Role):
    team = Role.GOOD
    name = "Merlin"

    def __init__(self, member: DiscordMemberInterface):
        super().__init__(member)

    def info(self, players: list[Role], player) -> str:
        evil_players = [player.player.name for player in players if player.is_evil()]
        return f"You are Merlin. {' and '.join(evil_players)} are Evil."
