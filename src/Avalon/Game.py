import random

import discord

from src.Avalon.Roles.LoyalServant import LoyalServant
from src.Avalon.Roles.Merlin import Merlin
from src.Avalon.Roles.Minion import Minion
from src.Avalon.Roles.Morgana import Morgana
from src.Avalon.Roles.Percival import Percival


def assign_role(player, role_name):
    if role_name == LoyalServant.name:
        return LoyalServant(player)
    if role_name == Morgana.name:
        return Morgana(player)
    if role_name == Merlin.name:
        return Merlin(player)
    if role_name == Percival.name:
        return Percival(player)
    if role_name == Minion.name:
        return Minion(player)
    raise DomainException(f'{role_name} not recognised')


class Game:
    def __init__(self, players: list[discord.Member], roles: list[str]):
        self.characters = [assign_role(player, role) for player, role in zip(players, roles)]
        random.shuffle(self.characters)

    def get_info(self):
        for character in self.characters:
            yield character.player, character.info(self.characters)

    def display_turn_order(self):
        return '\n '.join([character.player.display_name for character in self.characters])
