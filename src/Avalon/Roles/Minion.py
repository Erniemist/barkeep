from src.Avalon.Roles.Role import Role


class Minion(Role):
    team = Role.EVIL
    name = "Loathsome Minion of Mordred"

    def __init__(self, player):
        super().__init__(player)

    def info(self, players: list[Role]) -> str:
        other_evil_players = [
            player.player
            for player in players
            if player.is_evil() and player.player != self.player
        ]
        return f"You are a {Minion.name}. You know that {' and '.join(other_evil_players)} is your dark ally."
