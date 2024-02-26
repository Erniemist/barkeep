import random
from typing import Generator

from src.Avalon.Player import Player
from src.Avalon.Roles.LoyalServant import LoyalServant
from src.Avalon.Roles.Merlin import Merlin
from src.Avalon.Roles.Minion import Minion
from src.Avalon.Roles.Morgana import Morgana
from src.Avalon.Roles.Percival import Percival
from src.DiscordMemberInterface import DiscordMemberInterface


def assign_role(member: DiscordMemberInterface, role_name: str):
    if role_name == LoyalServant.name:
        return Player(member, LoyalServant())
    if role_name == Morgana.name:
        return Player(member, Morgana())
    if role_name == Merlin.name:
        return Player(member, Merlin())
    if role_name == Percival.name:
        return Player(member, Percival())
    if role_name == Minion.name:
        return Player(member, Minion())
    raise Exception(f'{role_name} not recognised')


class Game:
    ROLES = [LoyalServant.name, Morgana.name, Merlin.name, Percival.name, Minion.name]

    def __init__(self, members: list[DiscordMemberInterface], roles: list[str]):
        random.shuffle(members)
        random.shuffle(roles)
        self.players = [assign_role(member, role) for member, role in zip(members, roles)]

    def get_info(self) -> Generator[tuple[Player, str], None, None]:
        for player in self.players:
            yield player, player.info(self.players)

    def display_turn_order(self):
        return '\n '.join([player.name for player in self.players])
