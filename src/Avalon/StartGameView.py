import discord

from src.Avalon.Game import Game
from src.Avalon.Player import Player
from src.Avalon.Roles.Role import Role


class StartGameView(discord.ui.View):

    def __init__(self, roles: list):
        self.roles=[discord.SelectOption(label=role, value=role) for role in roles]
        super().__init__()
    @discord.ui.select(cls=discord.ui.UserSelect, max_values=12)
    async def select_players(self, interaction, select: discord.ui.UserSelect):
        return await interaction.response.send_message(
            f"Selected {', '.join([user.display_name for user in select.values])}!")

    @discord.ui.select(cls=discord.ui.Select,
                       options=[discord.SelectOption(label=role, value=role) for role in Game.ROLES],
                       max_values=len(Game.ROLES))
    async def select_roles(self, interaction, select: discord.ui.Select):
        if len(self.select_roles.values) != len(self.select_players.values):
            self.start.disabled = True
        return await interaction.response.send_message(f"Selected {', '.join([role for role in select.values])}")

    @discord.ui.button(label="cancel", disabled=False)
    async def cancel(self, interaction, button):
        self.clear_items()
        return await interaction.response.send_message("The game is over! That was quick")

    @discord.ui.button(label="start", disabled=False)  # Button Logic needs fixing. I couldn't make it work.
    async def start(self, interaction, button):
        if len(self.select_roles.values) != len(self.select_players.values):
            raise ValueError
        players = [Player(member) for member in self.select_players.values]
        game = Game(self.select_players.values, self.select_roles.values)
        await interaction.response.send_message(f'The turn order is\n{game.display_turn_order()}')
        for player, info in game.get_info():
            print(player, info)
