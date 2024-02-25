import random
from typing import Generator

import discord

from src.Avalon.Player import Player
from src.Avalon.Roles.LoyalServant import LoyalServant
from src.Avalon.Roles.Merlin import Merlin
from src.Avalon.Roles.Minion import Minion
from src.Avalon.Roles.Morgana import Morgana
from src.Avalon.Roles.Percival import Percival
from src.DiscordMemberInterface import DiscordMemberInterface


#game has a list of players a player has a discord member and a role a discord member has a real discord member a role has info
def assign_role(member: DiscordMemberInterface, role_name: str):
    if role_name == LoyalServant.name:
        return Player(member, LoyalServant(member))
    if role_name == Morgana.name:
        return Player(member, Morgana(member))
    if role_name == Merlin.name:
        return Player(member, Merlin(member))
    if role_name == Percival.name:
        return Player(member, Percival(member))
    if role_name == Minion.name:
        return Player(member, Minion(member))
    raise Exception(f'{role_name} not recognised')


class Game:
    ROLES = [LoyalServant.name, Morgana.name, Merlin.name, Percival.name, Minion.name]

    def __init__(self, members: list[DiscordMemberInterface], roles: list[str]):
        random.shuffle(members)
        random.shuffle(roles)
        self.players = [assign_role(member, role) for member, role in zip(members, roles)]

    def get_info(self) -> Generator[tuple[Player, str], None, None]:
        for player in self.players:
            yield player, player.role.info(self.players)

    def display_turn_order(self):
        return '\n '.join([character.player.display_name for character in self.players])
