from __future__ import annotations
from typing import Protocol
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.discord.member.discord_member_interface import DiscordMemberInterface


class ClientInterface(Protocol):
    async def find_member(self, member_id: int) -> DiscordMemberInterface:
        raise NotImplementedError()
