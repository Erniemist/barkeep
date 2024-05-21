import discord

from src import utilities, suggestions
from src.avalon import proposal_view
from src.avalon.game import load_players, display_turn_order
from src.avalon.start_game_view import StartGameView
from src.config import DISCORD_TOKEN, AVALON_ENABLED
from src.discord.client.client import Client
from src.drink import get_drink_repository


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
    @client.tree.command()
    async def start_game(interaction: discord.Interaction):
        """Start a game of avalon"""
        await interaction.response.send_message(
            "",
            view=StartGameView(),
            embed=discord.Embed(
                title="Roles",
                description="No roles selected",
                color=discord.Color.light_embed(),
            ),
        )


    @client.tree.command()
    async def propose_quest(interaction: discord.Interaction):
        """Propose a quest"""
        view = await proposal_view.make(interaction.client)
        await interaction.response.send_message(view=view)


    @client.tree.command()
    async def check_turn_order(interaction: discord.Interaction):
        """Check the turn order. Unaware of next quest sender"""
        players = await load_players(interaction.client)
        await display_turn_order(interaction, players)

client.run(DISCORD_TOKEN)
