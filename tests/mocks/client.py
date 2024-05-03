from __future__ import annotations
from typing import TYPE_CHECKING
from tests.mocks.discord_member import DiscordMember

if TYPE_CHECKING:
    from src.discord.member.discord_member_interface import DiscordMemberInterface


class Client:
    async def find_member(self, member_id: int) -> DiscordMemberInterface:
        return DiscordMember(member_id=member_id)
