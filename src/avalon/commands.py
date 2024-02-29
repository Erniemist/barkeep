import discord

from main import client
from src.avalon.game import Game, load_game
from src.avalon.start_game_view import StartGameView


@discord.app_commands.command()
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


@discord.app_commands.command()
async def check_turn_order(interaction: discord.Interaction):
    """Check the turn order. Unaware of next quest sender"""
    with open("data/avalon/game.json", "r", encoding="utf-8") as file:
        game = await load_game(client, file.readline())
        await interaction.response.send_message(game.display_turn_order())
