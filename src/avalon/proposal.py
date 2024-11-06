from discord import Interaction

from src.avalon.game import load_players
from src.avalon.player import Player


async def submit_proposal(interaction: Interaction, player_ids: list[str]):
    questers = [
        player
        for player in await load_players(interaction.client)
        if str(player.discord_id) in player_ids
    ]

    await display(interaction, questers)


async def display(interaction: Interaction, questers: list[Player]) -> None:
    await interaction.response.send_message(
        "The proposal is\n" + "\n ".join([quester.name for quester in questers])
    )
