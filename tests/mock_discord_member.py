class MockDiscordMember:
    def __init__(self, player_name, id=0):
        self.player_name = player_name
        self.id = id

    async def send(self, message) -> None:
        pass

    def name(self) -> str:
        return self.player_name

    def get_id(self) -> int:
        return self.id
