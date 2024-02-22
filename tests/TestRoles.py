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

    def test_loyal(self):
        players = [
            LoyalServant("Albert"),
            LoyalServant("Bernard"),
            Merlin("Colin"),
            Minion("Dan"),
            Minion("Emily")
        ]
        player = players[1]
        assert player.info(players) == "You are a Loyal Servant of King Arthur of Britain. You don't know anything.",\
            player.info(players)

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
            players) == "You are Percival. Colin and Dan are Merlin and Morgana, but you know not who is who...", player.info(
            players)

    def test_loathsome_minion(self):
        players = [
            LoyalServant("Albert"),
            Percival("Bernard"),
            Merlin("Colin"),
            Morgana("Dan"),
            Minion("Emily")
        ]
        player = players[4]
        assert player.info(
            players) == "You are a Loathsome Minion of Mordred. You know that Dan is your dark ally.", player.info(
            players)

    def test_morgana(self):
        players = [
            LoyalServant("Albert"),
            Percival("Bernard"),
            Merlin("Colin"),
            Morgana("Dan"),
            Minion("Emily")
        ]
        player = players[3]
        assert player.info(
            players) == "You are Morgana. You know that Emily is your sinister accomplice.", player.info(
            players)

    def test_more_evils(self):
        players = [
            Minion("Albert"),
            Minion("Bernard"),
            Minion("Colin"),
            Minion("Dan"),
            Minion("Emily")
        ]
        player = players[4]
        assert player.info(players) == "You are a Loathsome Minion of Mordred. " \
                                       "You know that Albert, Bernard, Colin, and Dan are your dark allies.",\
            player.info(players)

if __name__ == '__main__':
    unittest.main()
