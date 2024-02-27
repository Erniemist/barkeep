import random
from typing import Generator, Sequence

from src.avalon.player import Player
from src.avalon.Roles import role_factory
from src.avalon.Roles.loyal_servant import LoyalServant
from src.avalon.Roles.merlin import Merlin
from src.avalon.Roles.minion import Minion
from src.avalon.Roles.morgana import Morgana
from src.avalon.Roles.percival import Percival
from src.discord_member_interface import DiscordMemberInterface


class Game:
    ROLES = [LoyalServant.name, Morgana.name, Merlin.name, Percival.name, Minion.name]

    def __init__(
        self, members: Sequence[DiscordMemberInterface], role_names: Sequence[str]
    ):
        random.shuffle(list(members))
        random.shuffle(list(role_names))
        self.players = [
            Player(member, role_factory.from_name(role_name))
            for member, role_name in zip(members, role_names)
        ]

    def get_info(self) -> Generator[tuple[Player, str], None, None]:
        for player in self.players:
            yield player, player.info(self.players)

    def display_turn_order(self) -> str:
        return "\n ".join([player.name for player in self.players])