from src.DiscordMemberInterface import DiscordMemberInterface


class MockDiscordMember(DiscordMemberInterface):

    def __init__(self, player_name):
        self.player_name = player_name
    def send(self, message):
        pass

    def name(self) -> str:
        return self.player_name