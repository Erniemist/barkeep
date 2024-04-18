from abc import ABC


class Role(ABC):
    team: str
    name: str
    GOOD = "good"
    EVIL = "evil"

    def info(self, players, player) -> str:
        raise NotImplemented

    def is_evil(self):
        return self.team == Role.EVIL

    @staticmethod
    def join_names(names: list[str]):
        if len(names) == 0:
            return "nobody"
        if len(names) == 1:
            return names[0]
        if len(names) == 2:
            return f"{names[0]} and {names[1]}"
        return ", ".join(names[:-1]) + ", and " + names[-1]
