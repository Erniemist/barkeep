class DiscordMember:
    def __init__(self, player_name="NAME", member_id=0):
        self.player_name = player_name
        self.member_id = member_id

    async def send(self, message) -> None:
        pass

    def name(self) -> str:
        return self.player_name

    def get_id(self) -> int:
        return self.member_id
