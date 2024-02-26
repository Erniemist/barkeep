import random
from typing import Generator

from src.Avalon.Player import Player
from src.Avalon.Roles import RoleFactory
from src.Avalon.Roles.LoyalServant import LoyalServant
from src.Avalon.Roles.Merlin import Merlin
from src.Avalon.Roles.Minion import Minion
from src.Avalon.Roles.Morgana import Morgana
from src.Avalon.Roles.Percival import Percival
from src.DiscordMemberInterface import DiscordMemberInterface


class Game:
    ROLES = [LoyalServant.name, Morgana.name, Merlin.name, Percival.name, Minion.name]

    def __init__(self, members: list[DiscordMemberInterface], role_names: list[str]):
        random.shuffle(members)
        random.shuffle(role_names)
        self.players = [
            Player(member, RoleFactory.from_name(role_name))
            for member, role_name in zip(members, role_names)
        ]

    def get_info(self) -> Generator[tuple[Player, str], None, None]:
        for player in self.players:
            yield player, player.info(self.players)

    def display_turn_order(self) -> str:
        return '\n '.join([player.name for player in self.players])
