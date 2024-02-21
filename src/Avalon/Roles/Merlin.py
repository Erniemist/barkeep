from src.Avalon.Roles.Role import Role


class Merlin(Role):
    team = Role.GOOD
    name = "Merlin"

    def __init__(self, player):
        super().__init__(player)

    def info(self, players: list[Role]) -> str:
        evil_players = [player.player for player in players if player.is_evil()]
        return f"You are Merlin. {' and '.join(evil_players)} are Evil."
