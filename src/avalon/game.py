import json
import random
from typing import Sequence

from discord import Interaction

from src.avalon.player import Player
from src.avalon.Roles import role_factory

from src.discord.member.discord_member_interface import DiscordMemberInterface
from src.discord.client.client_interface import ClientInterface


async def start_game(
    interaction: Interaction,
    members: Sequence[DiscordMemberInterface],
    role_names: Sequence[str],
) -> None:
    members, role_names = list(members), list(role_names)
    random.shuffle(members)
    random.shuffle(role_names)

    players = make_players(members, role_names)

    store_players(players)
    await display_turn_order(interaction, players)
    for player in players:
        await player.discord_member.send(player.info(players))


def make_players(
    members: list[DiscordMemberInterface], role_names: list[str]
) -> list[Player]:
    return [
        Player(member, role_factory.from_name(role_name))
        for member, role_name in zip(members, role_names)
    ]


def store_players(players):
    with open("data/avalon/game.json", "w", encoding="utf-8") as file:
        file.write(to_json(players))


def to_json(players: list[Player]) -> str:
    return json.dumps([player.to_dict() for player in players])


async def display_turn_order(interaction: Interaction, players: list[Player]) -> None:
    await interaction.response.send_message(
        "The turn order is\n" + "\n ".join([player.name for player in players])
    )


async def load_players(
    client: ClientInterface,
) -> list[Player]:
    with open("data/avalon/game.json", "r", encoding="utf-8") as file:
        game_data = file.readline()

    return await from_json(client, game_data)


async def from_json(client, game_data) -> list[Player]:
    players = json.loads(game_data)
    return make_players(
        [await client.find_member(player["member_id"]) for player in players],
        [player["role"] for player in players],
    )
