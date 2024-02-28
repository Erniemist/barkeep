from typing import Protocol

from src.discord.member.discord_member_interface import DiscordMemberInterface


class ClientInterface(Protocol):
    def find_member(self, member_id) -> DiscordMemberInterface:
        raise NotImplementedError()