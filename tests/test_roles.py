from src.avalon.game import Game
from src.avalon.Roles.loyal_servant import LoyalServant
from src.avalon.Roles.merlin import Merlin
from src.avalon.Roles.minion import Minion
from src.avalon.Roles.morgana import Morgana
from src.avalon.Roles.percival import Percival
from tests.mocks.discord_member import DiscordMember


def test_info():
    game = Game(
        members=[
            DiscordMember(name)
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
        "Albert": "You are a Loyal Servant of King Arthur of Britain. You don't know anything.",
        "Bernard": "You are Merlin. Colin and Dan are Evil.",
        "Colin": "You are a Loathsome Minion of Mordred. Your dark allies are: Dan.",
        "Dan": "You are Morgana. Your dark allies are: Colin.",
        "Emily": "You are Percival. "
        + "Bernard and Dan are Merlin and Morgana, but you know not who is who...",
    }

    output = {player.name: info for player, info in game.get_info()}

    assert expectations == output, output
