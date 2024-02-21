from discord import app_commands

from Drink import DrinkRepository
import Suggestions
import Utilities
import discord
from discord.ext.commands import Bot
from discord.utils import get


class Client(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        with open('../server_id.txt', 'r') as f:
            server_id = f.readline().strip()
        self.server = discord.Object(id=server_id)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=self.server)
        await self.tree.sync(guild=self.server)


client = Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')


@client.tree.command()
async def hello(interaction: discord.Interaction):
    """Says hello!"""
    await interaction.response.send_message(f'Hi, {interaction.user.mention}')


@client.tree.command()
async def drink(interaction: discord.Interaction):
    """Barkeep will recommend you a drink"""
    await interaction.response.send_message(f'Might I suggest {DrinkRepository.make().get_drink()}?')


@client.tree.command()
async def suggest(interaction: discord.Interaction, suggestion: str):
    """Make a suggestion to improve the bot"""
    Suggestions.add_suggestion(Utilities.sanitise(suggestion))
    await interaction.response.send_message("I'll take a note of that.")


with open('../token.txt', 'r') as f:
    token = f.readline().strip()
client.run(token)
