import discord

from src.discord_member_interface import DiscordMemberInterface


def from_id(member_id: int, guild: discord.Guild):
    member = guild.get_member(member_id)
    if member is None:
        raise ValueError(f"Could not find member for id {member_id}")

    return DiscordMember(member)


class DiscordMember(DiscordMemberInterface):
    def __init__(self, member: discord.Member):
        self.member = member

    async def send(self, message):
        await self.member.send(message)

    def get_id(self):
        return self.member.id

    def name(self) -> str:
        return self.member.display_name
