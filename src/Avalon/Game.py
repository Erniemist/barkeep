import random

import discord

from src.Avalon.Roles.Role import assign_role


class Game:
    def __init__(self, players: list[discord.Member], roles: list[str]):
        self.characters = [assign_role(player, role) for player, role in zip(players, roles)]
        random.shuffle(self.characters)

    def give_info(self):
        for character in self.characters:
            character.player.send(character.info(self.characters))

    def display_turn_order(self):
        return [character.player.display_name for character in self.characters]
