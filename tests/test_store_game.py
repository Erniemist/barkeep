import json

from src.avalon.Roles.loyal_servant import LoyalServant
from src.avalon.Roles.merlin import Merlin
from src.avalon.game import Game
from tests.mock_discord_member import MockDiscordMember


def test_storing():
    game = Game(
        [
            MockDiscordMember('Alice', 1),
            MockDiscordMember('Bob', 2),
        ],
        [
            Merlin.name,
            LoyalServant.name,
        ],
    )
    assert game.to_json() == '{"players": [{"member_id": 1, "role": "Merlin"}, {"member_id": 2, "role": "Loyal Servant"}]}', game.to_json()
