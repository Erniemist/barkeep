from typing import Protocol


class DiscordMemberInterface(Protocol):
    async def send(self, message) -> None:
        raise NotImplementedError

    def name(self) -> str:
        raise NotImplementedError
    def get_id(self) -> int:
        raise NotImplementedError
