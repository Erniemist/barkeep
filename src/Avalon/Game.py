import random

import discord

from src.Avalon.Roles.LoyalServant import LoyalServant
from src.Avalon.Roles.Merlin import Merlin
from src.Avalon.Roles.Minion import Minion
from src.Avalon.Roles.Morgana import Morgana
from src.Avalon.Roles.Percival import Percival


def assign_role(player, role_name):
    if role_name is "Loyal Servant":
        return LoyalServant(player)
    if role_name is "Morgana":
        return Morgana(player)
    if role_name is "Merlin":
        return Merlin(player)
    if role_name is "Percival":
        return Percival(player)
    if role_name is "Loathsome Minion of Mordred":
        return Minion(player)


class Game:
    def __init__(self, players: list[discord.Member], roles: list[str]):
        self.characters = [assign_role(player, role) for player, role in zip(players, roles)]
        random.shuffle(self.characters)

    def give_info(self):
        for character in self.characters:
            character.player.send(character.info(self.characters))

    def display_turn_order(self):
        return [character.player.display_name for character in self.characters]
