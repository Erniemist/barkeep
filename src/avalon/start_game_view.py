import discord

from src.avalon.Roles.loyal_servant import LoyalServant
from src.avalon.Roles.minion import Minion
from src.avalon.game import Game, start_game
from src.config import MIN_PLAYERS
from src.discord.member.discord_member import DiscordMember


class StartGameView(discord.ui.View):
    def __init__(self, roles: list[str]):
        self.roles = [
            discord.SelectOption(label=role, value=role) for role in roles
        ] + [
            discord.SelectOption(label=LoyalServant.name, value=LoyalServant.name),
            discord.SelectOption(label=LoyalServant.name, value=LoyalServant.name),
            discord.SelectOption(label=LoyalServant.name, value=LoyalServant.name),
            discord.SelectOption(label=Minion.name, value=Minion.name),
            discord.SelectOption(label=Minion.name, value=Minion.name),
        ]
        super().__init__()

    @discord.ui.select(cls=discord.ui.UserSelect, max_values=12)
    async def select_players(self, interaction: discord.Interaction, _):
        await interaction.response.defer()
        if interaction.message is None:
            raise RuntimeError("No message found on start game interaction")
        self.start.disabled = self.should_disable_button()
        return await interaction.message.edit(
            content=interaction.message.content,
            view=self,
        )

    @discord.ui.select(
        cls=discord.ui.Select,
        options=[discord.SelectOption(label=role, value=role) for role in Game.ROLES],
        min_values=MIN_PLAYERS,
        max_values=len(Game.ROLES),
    )
    async def select_roles(self, interaction: discord.Interaction, _):
        await interaction.response.defer()
        if interaction.message is None:
            raise RuntimeError("No message found on start game interaction")
        self.start.disabled = self.should_disable_button()
        return await interaction.message.edit(
            content=interaction.message.content,
            view=self,
            embed=self.display_selected_roles(interaction),
        )

    def display_selected_roles(self, interaction: discord.Interaction):
        if interaction.message is None:
            raise RuntimeError("No message found on start game interaction")
        embed = interaction.message.embeds[0]
        embed.description = f"You have selected {", ".join(self.select_roles.values)}"
        return embed

    def should_disable_button(self):
        if len(self.select_roles.values) != len(self.select_players.values):
            return True
        if len(self.select_roles.values) < MIN_PLAYERS:
            return True
        return False

    @discord.ui.button(label="cancel", disabled=False)
    async def cancel(self, interaction: discord.Interaction, _):
        self.clear_items()
        return await interaction.response.send_message(
            "The game is over! That was quick"
        )

    @discord.ui.button(label="start", disabled=True)
    async def start(self, interaction: discord.Interaction, _):
        members = [DiscordMember(member) for member in self.select_players.values]
        game = start_game(members, self.select_roles.values)
        await interaction.response.send_message(
            f"The turn order is\n{game.display_turn_order()}"
        )
        for player, info in game.get_info():
            await player.discord_member.send(info)
