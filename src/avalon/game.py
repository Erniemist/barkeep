import json
import random
from typing import Generator, Sequence

from src.avalon.player import Player
from src.avalon.Roles import role_factory

from src.discord.member.discord_member_interface import DiscordMemberInterface
from src.discord.client.client_interface import ClientInterface


class Game:
    def __init__(
        self, members: Sequence[DiscordMemberInterface], role_names: Sequence[str]
    ):
        self.players = [
            Player(member, role_factory.from_name(role_name))
            for member, role_name in zip(members, role_names)
        ]

    def get_info(self) -> Generator[tuple[Player, str], None, None]:
        for player in self.players:
            yield player, player.info(self.players)

    def display_turn_order(self) -> str:
        return "\n ".join([player.name for player in self.players])

    def to_json(self) -> str:
        return json.dumps({"players": [player.to_dict() for player in self.players]})


def start_game(
    members: Sequence[DiscordMemberInterface], role_names: Sequence[str]
) -> Game:
    members, role_names = list(members), list(role_names)
    random.shuffle(members)
    random.shuffle(role_names)
    game = Game(members, role_names)
    with open("data/avalon/game.json", "w", encoding="utf-8") as file:
        file.write(game.to_json())
    return game


async def load_game(
    client: ClientInterface,
    game_data: str,
) -> Game:
    players = json.loads(game_data)["players"]
    return Game(
        [await client.find_member(player["member_id"]) for player in players],
        [player["role"] for player in players],
    )
