from src.Avalon.Roles.Role import Role
from src.DiscordMemberInterface import DiscordMemberInterface


class LoyalServant(Role):
    team = Role.GOOD
    name = "Loyal Servant"

    def __init__(self, member: DiscordMemberInterface):
        super().__init__(member)

    def info(self, players: list[Role], player) -> str:
        return "You are a Loyal Servant of King Arthur of Britain. You don't know anything."
