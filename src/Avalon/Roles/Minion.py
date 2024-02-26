from src.avalon.Roles.role import Role


class Minion(Role):
    team = Role.EVIL
    name = "Loathsome Minion of Mordred"

    def __init__(self, player):
        super().__init__(player)

    def info(self, players: list[Role]) -> str:
        other_evils = self.other_evils(players)
        if len(other_evils) == 0:
            return f"You are a {Minion.name}. You have no known allies."
        if len(other_evils) == 1:
            return f"You are a {Minion.name}. You know that {other_evils[0]} is your dark ally."
        if len(other_evils) == 2:
            return f"You are a {Minion.name}. You know that {other_evils[0]} and {other_evils[1]} are your dark allies."

        return (
            f"You are a {Minion.name}. "
            f"You know that {', '.join(other_evils[:-1])}, and {other_evils[-1]} are your dark allies."
        )

    def other_evils(self, players):
        other_evil_players = [
            player.player
            for player in players
            if player.is_evil() and player.player != self.player
        ]
        return other_evil_players
