from typing import Union

import discord


def from_id(member_id: int, guild: discord.Guild):
    member = guild.get_member(member_id)
    if member is None:
        raise ValueError(f"Could not find member for id {member_id}")

    return DiscordMember(member)


class DiscordMember:
    def __init__(self, member: Union[discord.Member, discord.User]):
        if isinstance(member, discord.User):
            raise ValueError('Someone from outside the server tried to join the game?')
        self.member = member

    async def send(self, message) -> None:
        await self.member.send(message)

    def get_id(self):
        return self.member.id

    def name(self) -> str:
        return self.member.display_name
