from src.avalon.Roles.loyal_servant import LoyalServant
from src.avalon.Roles.merlin import Merlin
from src.avalon.game import Game, load_game
from tests.mocks.client import Client
from tests.mocks.discord_member import DiscordMember


def test_storing():
    game = Game(
        [
            DiscordMember("Alice", 1),
            DiscordMember("Bob", 2),
        ],
        [
            Merlin.name,
            LoyalServant.name,
        ],
    )

    expected = '{"players": [{"member_id": 1, "role": "Merlin"}, {"member_id": 2, "role": "Loyal Servant"}]}'  # pylint: disable=line-too-long
    actual = game.to_json()

    assert actual == expected, actual


def test_loading():
    game_data = '{"players": [{"member_id": 1, "role": "Merlin"}, {"member_id": 2, "role": "Loyal Servant"}]}'  # pylint: disable=line-too-long

    game = load_game(Client(), game_data)

    alice = game.players[0]
    assert alice.discord_member.get_id() == 1
    assert alice.role.name == "Merlin"

    bob = game.players[1]
    assert bob.discord_member.get_id() == 2
    assert bob.role.name == "Loyal Servant"
