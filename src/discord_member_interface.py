from abc import ABC


class DiscordMemberInterface(ABC):
    async def send(self, message):
        raise NotImplementedError

    def name(self) -> str:
        raise NotImplementedError
