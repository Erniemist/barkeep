from src.DiscordMemberInterface import DiscordMemberInterface


class Player:

    def __init__(self, member:DiscordMemberInterface):
        self.discord_member = member
        self.name = member.name()