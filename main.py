import discord

from src import utilities, suggestions
from src.avalon.commands import start_game, check_turn_order
from src.config import DISCORD_TOKEN, AVALON_ENABLED
from src.discord.client.client import Client
from src.drink import get_drink_repository
from src.avalon.game import load_game
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


if AVALON_ENABLED:
    client.tree.add_command(start_game)  # type: ignore
    client.tree.add_command(check_turn_order)  # type: ignore
client.run(DISCORD_TOKEN)
