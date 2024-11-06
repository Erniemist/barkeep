import discord
from discord import SelectOption

from src.avalon.player import Player
from src.config import MIN_QUESTERS, MAX_QUESTERS


class ProposalSelect(discord.ui.Select):
    def __init__(self, players: list[Player]):
        super().__init__()
        self.options = [
            SelectOption(label=player.name, value=str(player.discord_id))
            for player in players
        ]
        self.min_values = MIN_QUESTERS
        self.max_values = MAX_QUESTERS
