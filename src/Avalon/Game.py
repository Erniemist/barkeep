import random

import discord

from src.avalon.Roles.loyal_servant import LoyalServant
from src.avalon.Roles.merlin import Merlin
from src.avalon.Roles.minion import Minion
from src.avalon.Roles.morgana import Morgana
from src.avalon.Roles.percival import Percival


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
    raise ValueError(f"{role_name} not recognised")


class Game:
    def __init__(self, players: list[discord.Member], roles: list[str]):
        self.characters = [
            assign_role(player, role) for player, role in zip(players, roles)
        ]
        random.shuffle(self.characters)

    def get_info(self):
        for character in self.characters:
            yield character.player, character.info(self.characters)

    def display_turn_order(self):
        return "\n ".join(
            [character.player.display_name for character in self.characters]
        )
