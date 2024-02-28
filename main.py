import discord

from src import utilities, suggestions
from src.discord.client.client import Client
from src.drink import get_drink_repository
from src.avalon.game import Game
from src.avalon.start_game_view import StartGameView


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
    await interaction.response.send_message(
        "",
        view=StartGameView(Game.ROLES),
        embed=discord.Embed(
            title="Roles",
            description="No roles selected",
            color=discord.Color.light_embed(),
        ),
    )


with open("token.txt", mode="r", encoding="utf-8") as f:
    token = f.readline().strip()
client.run(token)
