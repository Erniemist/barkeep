import discord

from src.avalon import proposal_view
from src.avalon.game import load_players, display_turn_order
from src.avalon.start_game_view import StartGameView


@discord.app_commands.command()
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


# TODO: restore this to propose_quest when discord fixes itself
@discord.app_commands.command()
async def check_turn_order(interaction: discord.Interaction):
    """Propose a quest"""
    view = await proposal_view.make(interaction.client)
    await interaction.response.send_message(view=view)


# TODO: restore this to check_turn_order when discord fixes itself
@discord.app_commands.command()
async def actual_check_turn_order(interaction: discord.Interaction):
    """Check the turn order. Unaware of next quest sender"""
    players = await load_players(interaction.client)
    await display_turn_order(interaction, players)
