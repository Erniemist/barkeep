from typing import Self

from src.avalon.Roles.role import Role
from src.discord_member_interface import DiscordMemberInterface


class Player:
    def __init__(self, member: DiscordMemberInterface, role: Role):
        self.discord_member = member
        self.role = role
        self.name = member.name()

    def info(self, players: list[Self]):
        return self.role.info(players, self)

    def is_evil(self):
        return self.role.is_evil()
