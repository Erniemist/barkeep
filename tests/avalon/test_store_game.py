import pytest

from src.avalon.Roles.loyal_servant import LoyalServant
from src.avalon.Roles.merlin import Merlin
from src.avalon.game import to_json, make_players, from_json
from tests.mocks.client import Client
from tests.mocks.discord_member import DiscordMember


def test_storing():
    players = make_players(
        [
            DiscordMember("Alice", 1),
            DiscordMember("Bob", 2),
        ],
        [
            Merlin.name,
            LoyalServant.name,
        ],
    )

    expected = '[{"member_id": 1, "role": "Merlin"}, {"member_id": 2, "role": "Loyal Servant"}]'
    actual = to_json(players)

    assert actual == expected, actual


@pytest.mark.asyncio
async def test_loading():
    game_data = '[{"member_id": 1, "role": "Merlin"}, {"member_id": 2, "role": "Loyal Servant"}]'

    players = await from_json(Client(), game_data)

    alice = players[0]
    assert alice.discord_member.get_id() == 1
    assert alice.role.name == "Merlin"

    bob = players[1]
    assert bob.discord_member.get_id() == 2
    assert bob.role.name == "Loyal Servant"
