import unittest

from src.Avalon.Roles.LoyalServant import LoyalServant
from src.Avalon.Roles.Merlin import Merlin
from src.Avalon.Roles.Minion import Minion


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


if __name__ == '__main__':
    unittest.main()
