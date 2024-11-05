import discord
from src.avalon import proposal_view
from src.avalon.game import load_players, display_turn_order
from src.avalon.start_game_view import StartGameView


async def avalon_start_game(interaction: discord.Interaction):
    return interaction.response.send_message(
        "",
        view=StartGameView(),
        embed=discord.Embed(
            title="Roles",
            description="No roles selected",
            color=discord.Color.light_embed(),
        ),
    )


async def avalon_propose_quest(interaction: discord.Interaction):
    """Propose a quest"""
    view = await proposal_view.make(interaction.client)
    await interaction.response.send_message(view=view)


async def avalon_check_turn_order(interaction: discord.Interaction):
    """Check the turn order. Unaware of next quest sender"""
    players = await load_players(interaction.client)
    await display_turn_order(interaction, players)
