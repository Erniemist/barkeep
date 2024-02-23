from abc import ABC


class DiscordMemberInterface(ABC):

    def send(self, message):
        pass

    def name(self) -> str:
        return ""

