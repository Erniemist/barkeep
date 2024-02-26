from typing import Self

from src.Avalon.Roles.Role import Role
from src.DiscordMemberInterface import DiscordMemberInterface


class Player:
    def __init__(self, member: DiscordMemberInterface, role: Role):
        self.discord_member = member
        self.role = role
        self.name = member.name()

    def info(self, players: list[Self], player: Self):
        return self.role.info(players, player)
