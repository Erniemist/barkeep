from discord import app_commands

import discord

from src import utilities, suggestions
from src.drink import get_drink_repository
from src.avalon.game import Game
from src.avalon.start_game_view import StartGameView


class Client(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        with open("server_id.txt", mode="r", encoding="utf-8") as file:
            server_id = file.readline().strip()
        self.server = discord.Object(id=server_id)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=self.server)
        await self.tree.sync(guild=self.server)


client = Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    print(f"Logged in as {client.user} (ID: {client.user.id})")
    print("------")


@client.tree.command()
async def hello(interaction: discord.Interaction):
    """Says hello!"""
    await interaction.response.send_message(f"Hi, {interaction.user.mention}")


@client.tree.command()
async def drink(interaction: discord.Interaction):
    """Barkeep will recommend you a drink"""
    await interaction.response.send_message(
        f"Might I suggest {get_drink_repository().get_drink()}?",
    )


@client.tree.command()
async def suggest(interaction: discord.Interaction, suggestion: str):
    """Make a suggestion to improve the bot"""
    suggestions.add_suggestion(utilities.sanitise(suggestion))
    await interaction.response.send_message("I'll take a note of that.")


@client.tree.command()
async def start_game(interaction: discord.Interaction):
    """Start a game of avalon"""
    await interaction.response.send_message("", view=StartGameView(Game.ROLES))


with open("token.txt", mode="r", encoding="utf-8") as f:
    token = f.readline().strip()
client.run(token)
