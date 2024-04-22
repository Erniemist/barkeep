from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.discord.member.discord_member_interface import DiscordMemberInterface

from typing import Protocol


class ClientInterface(Protocol):
    async def find_member(self, member_id: int) -> DiscordMemberInterface:
        raise NotImplementedError()
