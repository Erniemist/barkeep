class MockDiscordMember:
    def __init__(self, player_name):
        self.player_name = player_name

    async def send(self, message) -> None:
        pass

    def name(self) -> str:
        return self.player_name
