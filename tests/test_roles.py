import random

from src.avalon.game import Game
from src.avalon.Roles.loyal_servant import LoyalServant
from src.avalon.Roles.merlin import Merlin
from src.avalon.Roles.minion import Minion
from src.avalon.Roles.morgana import Morgana
from src.avalon.Roles.percival import Percival
from tests.mock_discord_member import MockDiscordMember


def test_info():
    random.seed(11)
    game = Game(
        members=[
            MockDiscordMember(name)
            for name in ["Albert", "Bernard", "Colin", "Dan", "Emily"]
        ],
        role_names=[
            LoyalServant.name,
            Merlin.name,
            Minion.name,
            Morgana.name,
            Percival.name,
        ],
    )

    expectations = {
        "Colin": "You are Percival. "
        + "Emily and Dan are Merlin and Morgana, but you know not who is who...",
        "Albert": "You are a Loyal Servant of King Arthur of Britain. You don't know anything.",
        "Bernard": "You are a Loathsome Minion of Mordred. You know that Emily is your dark ally.",
        "Emily": "You are Morgana. You know that Bernard is your sinister accomplice.",
        "Dan": "You are Merlin. Bernard and Emily are Evil.",
    }

    output = {player.name: info for player, info in game.get_info()}

    assert expectations == output, output
