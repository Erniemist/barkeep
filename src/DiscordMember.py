import discord

from src.DiscordMemberInterface import DiscordMemberInterface


class DiscordMember(DiscordMemberInterface):

    def __init__(self, member: discord.Member):
        self.member = member

    async def send(self, message):
        await self.member.send_message(message)