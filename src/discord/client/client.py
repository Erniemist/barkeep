import discord
from discord import app_commands

from src.config import SERVER_ID
from src.discord.member.discord_member import DiscordMember
from src.discord.member.discord_member_interface import DiscordMemberInterface


class Client(discord.Client):
    server: discord.Guild

    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.server = await self.fetch_guild(int(SERVER_ID))
        self.tree.copy_global_to(guild=self.server)
        await self.tree.sync(guild=self.server)

    async def find_member(self, member_id: int) -> DiscordMemberInterface:
        member = await self.server.fetch_member(member_id)  # pylint: disable=no-member
        if member is None:
            raise ValueError(f"Couldn't find member {member_id}")
        return DiscordMember(member)
