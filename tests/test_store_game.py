from src.avalon.Roles.loyal_servant import LoyalServant
from src.avalon.Roles.merlin import Merlin
from src.avalon.game import Game
from tests.mock_discord_member import MockDiscordMember


def test_storing():
    game = Game(
        [
            MockDiscordMember("Alice", 1),
            MockDiscordMember("Bob", 2),
        ],
        [
            Merlin.name,
            LoyalServant.name,
        ],
    )

    expected = '{"players": [{"member_id": 1, "role": "Merlin"}, {"member_id": 2, "role": "Loyal Servant"}]}'  # pylint: disable=line-too-long
    actual = game.to_json()

    assert actual == expected, actual
