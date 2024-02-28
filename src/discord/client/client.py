import discord
from discord import app_commands

from src.discord.member.discord_member import DiscordMember
from src.discord.member.discord_member_interface import DiscordMemberInterface


class Client(discord.Client):
    server: discord.Guild

    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        with open("server_id.txt", mode="r", encoding="utf-8") as file:
            server_id = file.readline().strip()
        self.server = await self.fetch_guild(int(server_id))
        self.tree.copy_global_to(guild=self.server)
        await self.tree.sync(guild=self.server)

    def find_member(self, member_id: int) -> DiscordMemberInterface:
        member = self.server.get_member(member_id)  # pylint: disable=no-member
        if member is None:
            raise ValueError(f"Couldn't find member {member_id}")
        return DiscordMember(member)
