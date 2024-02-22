import unittest

from src.Avalon.Roles.LoyalServant import LoyalServant
from src.Avalon.Roles.Merlin import Merlin
from src.Avalon.Roles.Minion import Minion
from src.Avalon.Roles.Morgana import Morgana
from src.Avalon.Roles.Percival import Percival


class TestRoles(unittest.TestCase):

    def test_merlin(self):
        players = [
            LoyalServant("Albert"),
            LoyalServant("Bernard"),
            Merlin("Colin"),
            Minion("Dan"),
            Minion("Emily")
        ]
        player = players[2]
        assert player.info(players) == "You are Merlin. Dan and Emily are Evil.", player.info(players)

    def test_percival(self):
        players = [
            LoyalServant("Albert"),
            Percival("Bernard"),
            Merlin("Colin"),
            Morgana("Dan"),
            Minion("Emily")
        ]
        player = players[1]
        assert player.info(
            players) == "You are Percival. Colin and Dan are Merlin and Morgana, but you know not who is who..."


if __name__ == '__main__':
    unittest.main()
