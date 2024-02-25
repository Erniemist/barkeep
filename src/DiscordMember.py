import discord

from src.DiscordMemberInterface import DiscordMemberInterface


def from_id(member_id: int, guild: discord.Guild):
    return DiscordMember(guild.get_member(member_id))


class DiscordMember(DiscordMemberInterface):

    def __init__(self, member: discord.Member):
        self.member = member

    async def send(self, message):
        await self.member.send_message(message)

    def get_id(self):
        return self.member.id
