from abc import ABC

from src.DiscordMemberInterface import DiscordMemberInterface


class Role(ABC):
    team: str
    name: str
    GOOD = "good"
    EVIL = "evil"

    def info(self, players, player) -> str:
        raise NotImplemented

    def is_evil(self):
        return self.team == Role.EVIL
