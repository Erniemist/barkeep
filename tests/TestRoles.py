import random
import unittest

from src.Avalon.Game import Game
from src.Avalon.Roles.LoyalServant import LoyalServant
from src.Avalon.Roles.Merlin import Merlin
from src.Avalon.Roles.Minion import Minion
from src.Avalon.Roles.Morgana import Morgana
from src.Avalon.Roles.Percival import Percival
from tests.MockDiscordMember import MockDiscordMember


class TestRoles(unittest.TestCase):
    def test_info(self):
        random.seed(11)
        game = Game(
            members=[MockDiscordMember(name) for name in ["Albert", "Bernard", "Colin", "Dan", "Emily"]],
            roles=[LoyalServant.name, Merlin.name, Minion.name, Morgana.name, Percival.name],
        )

        expectations = {
            "Colin": "You are Percival. Emily and Dan are Merlin and Morgana, but you know not who is who...",
            "Albert": "You are a Loyal Servant of King Arthur of Britain. You don't know anything.",
            "Bernard": "You are a Loathsome Minion of Mordred. You know that Emily is your dark ally.",
            "Emily": "You are Morgana. You know that Bernard is your sinister accomplice.",
            "Dan": "You are Merlin. Bernard and Emily are Evil.",
        }

        output = {player.name: info for player, info in game.get_info()}

        assert expectations == output, output


if __name__ == '__main__':
    unittest.main()
